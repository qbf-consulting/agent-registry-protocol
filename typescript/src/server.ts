import http from "node:http";
import { createHash, randomUUID } from "node:crypto";
import { evaluateAuthority } from "./authority.js";
import { createA2APublicationProjection } from "./a2a.js";
import { MemoryStore } from "./store.js";
import type { AuthorityEvaluationInput } from "./types.js";

const now = () => new Date().toISOString();
const digest = (value: unknown) => `sha256:${createHash("sha256").update(JSON.stringify(value, Object.keys(value as any).sort())).digest("hex")}`;

class InvalidJsonError extends Error {
  constructor() {
    super("invalid JSON request body");
    this.name = "InvalidJsonError";
  }
}

export interface ServerOptions { port?: number; host?: string; store?: MemoryStore; }

export function createArpaServer(options: ServerOptions = {}) {
  const store = options.store ?? new MemoryStore();
  const server = http.createServer(async (req: any, res: any) => {
    const url = new URL(req.url ?? "/", `http://${req.headers.host ?? "127.0.0.1"}`);
    const send = (status: number, body: unknown) => {
      res.writeHead(status, { "content-type": "application/json" });
      res.end(JSON.stringify(body));
    };
    const problem = (status: number, code: string, title: string, detail = "") => send(status, {
      type: `https://arpa.example/problems/${code.toLowerCase()}`,
      title,
      status,
      code,
      detail,
      correlation_id: randomUUID(),
      reason_codes: [],
      retryable: false
    });
    const body = async (): Promise<Record<string, unknown>> => {
      const chunks: any[] = [];
      for await (const chunk of req) chunks.push(chunk);
      try {
        return JSON.parse(Buffer.concat(chunks).toString("utf8") || "{}");
      } catch {
        throw new InvalidJsonError();
      }
    };
    const emit = (subject: string, eventType: string, payload: Record<string, unknown>) => store.addEvent({ event_id: randomUUID(), event_type: eventType, subject, effective_at: now(), issued_at: now(), payload });

    try {
      if (req.method === "GET" && url.pathname === "/health") return send(200, { status: "ok", version: "0.9.5-dev", implementation: "typescript" });
      if (req.method === "GET" && url.pathname === "/registry") return send(200, {
        registry_id: "registry:typescript", name: "ARPA TypeScript Registry", arpa_version: "0.9.0", implementation_release: "0.9.5-dev",
        supported_modules: ["ARPA-Core", "ARPA-Relations", "ARPA-Authority", "ARPA-Evidence"], supported_profiles: ["A", "C"],
        authoritative_base_uri: `http://${options.host ?? "127.0.0.1"}:${options.port ?? 8081}`, conformance_declaration_uri: "urn:arpa:typescript:conformance",
        event_retention_seconds: 86400, status_max_age_seconds: 300
      });

      if (req.method === "POST" && url.pathname === "/agents") {
        const record = await body(); const aid = record.agent_id ?? record.subject;
        if (typeof aid !== "string" || !aid.startsWith("agentreg:")) return problem(422, "ARPA-ID-INVALID", "Invalid agent identifier");
        if (store.recordsForSubject(aid).some((r) => r.record_type === "agent_core")) return problem(409, "ARPA-STATE-TRANSITION-INVALID", "Identifier already issued");
        store.putRecord(record); emit(aid, "agent.registered", { record_id: record.record_id }); return send(201, record);
      }
      if (req.method === "POST" && url.pathname === "/records") {
        const record = await body(); store.putRecord(record);
        const subject = record.agent_id ?? record.subject ?? record.record_id;
        emit(typeof subject === "string" ? subject : JSON.stringify(subject), "agent.metadata.updated", { record_id: record.record_id, record_type: record.record_type });
        return send(201, record);
      }
      if (req.method === "GET" && url.pathname === "/agents") {
        const cores = store.allRecords().filter((r) => r.record_type === "agent_core");
        const items = cores.flatMap((core) => {
          const aid = String(core.agent_id ?? core.subject ?? "");
          const refs = store.recordsForSubject(aid).filter((r) => r.record_type === "agent-description-reference" && (r.disclosure_class ?? "public") === "public");
          if (!refs.length) return [];
          return [createA2APublicationProjection(core as any, refs[refs.length - 1] as any)];
        });
        return send(200, { items, next_cursor: null });
      }
      const agentMatch = /^\/agents\/(.+)$/.exec(url.pathname);
      if (req.method === "GET" && agentMatch && !url.pathname.includes("/historical-resolution") && !url.pathname.includes("/events") && !url.pathname.includes("/status")) {
        const aid = decodeURIComponent(agentMatch[1]!); const records = store.recordsForSubject(aid, url.searchParams.get("at") ?? undefined);
        const core = records.filter((r) => r.record_type === "agent_core");
        if (!core.length) return problem(404, "ARPA-ID-NOT-FOUND", "Agent not found");
        return send(200, { agent: core[core.length - 1], records, resolution_time: now(), at: url.searchParams.get("at"), authoritativeness: "authoritative", projection_lag_seconds: 0 });
      }
      const histMatch = /^\/agents\/(.+)\/historical-resolution$/.exec(url.pathname);
      if (req.method === "GET" && histMatch) {
        const aid = decodeURIComponent(histMatch[1]!); const at = url.searchParams.get("at");
        if (!at) return problem(422, "ARPA-HISTORICAL-TIME-REQUIRED", "Historical resolution requires at");
        const historical = store.recordsForSubject(aid, at); const current = store.recordsForSubject(aid);
        const hs = historical.filter((r) => r.record_type === "status").at(-1); const cs = current.filter((r) => r.record_type === "status").at(-1);
        if (!hs) return problem(409, "ARPA-HISTORICAL-EVIDENCE-UNAVAILABLE", "Historical status unavailable");
        if (!cs) return problem(409, "ARPA-AUTHORITY-INDETERMINATE", "Current status unavailable");
        const checkpoint = store.events(aid).at(-1)?.sequence ?? 0;
        return send(200, { subject: aid, requested_time: at, evaluation_time: now(), state_at_requested_time: hs, current_state: cs,
          reconstruction_status: "authoritative_complete", selected_records: historical.map((r) => ({ record_id: r.record_id ?? "unknown", version: String(r.schema_version ?? "1"), effective_from: r.effective_from ?? r.issued_at, effective_until: r.effective_until ?? null, digest: digest(r) })),
          event_checkpoint: `event:${checkpoint}`, later_material_events: [], historical_effect: "none", retention: { evidence_available: true, status: "available", boundary: null },
          evidence: { references: [`event:${checkpoint}`], integrity_status: "verified", lineage_mechanism: "typescript-memory-event-sequence" }, warnings: [] });
      }
      if (req.method === "POST" && url.pathname === "/authority/evaluate") {
        const payload = await body(); const result = evaluateAuthority(payload as unknown as AuthorityEvaluationInput);
        const receipt = { record_id: randomUUID(), record_type: "decision-receipt", schema_version: "1.0.0", issuer: "pdp:typescript", subject: String((payload.request as any)?.agent ?? "unknown"), issued_at: now(), effective_from: now(), effective_until: null, status: "issued", request_digest: digest(payload), decision: result.outcome, reason_codes: result.reasonCodes, evaluator: "pdp:typescript", policy_version: "typescript-0.3.0" };
        store.putRecord(receipt); return send(200, { decision: result.outcome, reason_codes: result.reasonCodes, decision_receipt: receipt });
      }
      if (req.method === "GET" && url.pathname === "/events") return send(200, { events: store.events(undefined, Number(url.searchParams.get("after") ?? 0)), after: Number(url.searchParams.get("after") ?? 0) });
      return problem(404, "ARPA-ID-NOT-FOUND", "Endpoint not found");
    } catch (error) {
      if (error instanceof InvalidJsonError) {
        return problem(400, "ARPA-INVALID-JSON", "Invalid JSON", "Request body must contain valid JSON.");
      }
      return problem(500, "ARPA-INTERNAL", "Internal error", "The server could not process the request.");
    }
  });
  return { server, store };
}

if (process.argv[1]?.endsWith("server.js")) {
  const port = Number(process.env.ARPA_TS_PORT ?? "8081");
  const host = process.env.ARPA_TS_HOST ?? "127.0.0.1";
  const { server } = createArpaServer({ port, host });
  server.listen(port, host, () => console.log(`ARPA TypeScript server listening on http://${host}:${port}`));
}
