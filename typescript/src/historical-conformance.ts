import fs from "node:fs";
import path from "node:path";
import { assessHistoricalResolution, selectBitemporalRecords } from "./historical.js";
import { readJson, repositoryRoot } from "./repository.js";

interface ManifestVector {
  id: string;
  path: string;
  expected_reconstruction_status: string;
  expected_historical_effect: string;
}
interface Manifest { profile: string; version: string; vectors: ManifestVector[]; }

const manifest = readJson<Manifest>("conformance/test-vectors/historical/manifest.json");
const results = manifest.vectors.map((entry) => {
  const document = readJson<any>(`conformance/test-vectors/historical/${entry.path}`);
  const assessment = assessHistoricalResolution(document);
  const expectedUsable = entry.expected_reconstruction_status !== "indeterminate" && entry.expected_historical_effect !== "indeterminate" && document.evidence.integrity_status !== "failed" && document.retention.status !== "outside_retention";
  const passed = document.reconstruction_status === entry.expected_reconstruction_status
    && document.historical_effect === entry.expected_historical_effect
    && assessment.usable === expectedUsable;
  return {
    id: entry.id,
    passed,
    reconstruction_status: document.reconstruction_status,
    historical_effect: document.historical_effect,
    reliance_outcome: assessment.outcome,
    reason_codes: assessment.reasonCodes
  };
});

const report = {
  report_type: "arpa-typescript-historical-resolution-report",
  arpa_baseline: manifest.version,
  implementation: "arpa-typescript",
  implementation_version: "0.3.0",
  independence_statement: "Historical reliance logic is implemented from ARPA v0.9.4 historical-resolution requirements and fixtures without importing Python behavioural code.",
  vectors: { total: results.length, passed: results.filter((r) => r.passed).length, failed: results.filter((r) => !r.passed).length },
  results
};
const out = path.join(repositoryRoot, "artifacts/typescript/historical-resolution-report.json");
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, JSON.stringify(report, null, 2) + "\n");
console.log(`TypeScript historical resolution: ${report.vectors.passed}/${report.vectors.total} vectors passed`);
if (report.vectors.failed > 0) process.exitCode = 1;

const bitemporal = readJson<{ vectors: Array<{ id: string; records: any[]; context: { effective_at: string; evidence_as_of: string; evaluation_time: string; history_complete_through?: string }; expected: { outcome: string; selected_record_ids: string[]; reason_code: string } }> }>("conformance/test-vectors/bitemporal/fixtures.json");
const bitemporalResults = bitemporal.vectors.map(vector => {
  const got = selectBitemporalRecords(vector.records, vector.context);
  return { id: vector.id, passed: got.outcome === vector.expected.outcome
    && JSON.stringify(got.selected_record_ids) === JSON.stringify(vector.expected.selected_record_ids)
    && got.reason_codes.includes(vector.expected.reason_code), outcome: got.outcome };
});
console.log(`TypeScript bitemporal: ${bitemporalResults.filter(r => r.passed).length}/${bitemporalResults.length} vectors passed`);
if (bitemporalResults.some(r => !r.passed)) process.exitCode = 1;
