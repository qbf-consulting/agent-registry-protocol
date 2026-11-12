import type { Decision } from "./types.js";

export type ReconstructionStatus =
  | "authoritative_complete"
  | "authoritative_partial"
  | "reconstructed_complete"
  | "reconstructed_partial"
  | "indeterminate";

export type HistoricalEffect = "none" | "prospective" | "retroactive" | "governance_defined" | "indeterminate";

export interface EffectiveRecord {
  record_id: string;
  version?: string;
  effective_from: string;
  effective_until?: string | null;
  digest?: string;
  [key: string]: unknown;
}

export interface HistoricalEvidence {
  references: string[];
  integrity_status: "verified" | "partial" | "failed" | "not_available" | string;
  lineage_mechanism?: string | null;
}

export interface HistoricalResolutionDocument {
  subject: string;
  requested_time: string;
  evaluation_time: string;
  state_at_requested_time: Record<string, unknown>;
  current_state: Record<string, unknown>;
  reconstruction_status: ReconstructionStatus;
  selected_records: EffectiveRecord[];
  event_checkpoint?: string | null;
  later_material_events: Array<{ historical_effect?: HistoricalEffect; effective_at?: string; [key: string]: unknown }>;
  historical_effect: HistoricalEffect;
  retention: { evidence_available: boolean; status: string; boundary?: string | null };
  evidence: HistoricalEvidence;
  warnings: string[];
}

export interface HistoricalAssessment {
  usable: boolean;
  reconstructionStatus: ReconstructionStatus;
  historicalEffect: HistoricalEffect;
  stateAtRequestedTime?: Record<string, unknown>;
}

const parseTime = (value: string): number => {
  const parsed = Date.parse(value);
  if (Number.isNaN(parsed)) throw new Error(`Invalid RFC3339 timestamp: ${value}`);
  return parsed;
};

/** Select effective records at a requested time without substituting current state. */
export function selectEffectiveRecords(records: EffectiveRecord[], at: string): EffectiveRecord[] {
  const requested = parseTime(at);
  return records
    .filter((record) => {
      const from = parseTime(record.effective_from);
      const until = record.effective_until == null ? Number.POSITIVE_INFINITY : parseTime(record.effective_until);
      return from <= requested && requested < until;
    })
    .sort((a, b) => parseTime(a.effective_from) - parseTime(b.effective_from));
}

/**
 * Evaluate whether a historical-resolution response is safe to rely on.
 * This independently enforces ARPA v0.9.4 fail-closed historical invariants.
 */
export function assessHistoricalResolution(document: HistoricalResolutionDocument): Decision<"usable" | "indeterminate"> & HistoricalAssessment {
  const requested = parseTime(document.requested_time);
  const evaluated = parseTime(document.evaluation_time);
  if (requested > evaluated) {
    return {
      outcome: "indeterminate", usable: false,
      reconstructionStatus: "indeterminate", historicalEffect: "indeterminate",
      reasonCodes: ["requested_time_after_evaluation_time"]
    };
  }

  if (document.retention.status === "outside_retention" || !document.retention.evidence_available) {
    return {
      outcome: "indeterminate", usable: false,
      reconstructionStatus: "indeterminate", historicalEffect: "indeterminate",
      reasonCodes: ["historical_evidence_outside_retention"]
    };
  }

  if (document.evidence.integrity_status === "failed" || document.evidence.integrity_status === "not_available") {
    return {
      outcome: "indeterminate", usable: false,
      reconstructionStatus: "indeterminate", historicalEffect: "indeterminate",
      reasonCodes: ["historical_evidence_integrity_unusable"]
    };
  }

  if (document.reconstruction_status === "indeterminate" || document.historical_effect === "indeterminate") {
    return {
      outcome: "indeterminate", usable: false,
      reconstructionStatus: document.reconstruction_status,
      historicalEffect: document.historical_effect,
      reasonCodes: ["historical_reconstruction_indeterminate"]
    };
  }

  if (requested < evaluated && Object.is(document.state_at_requested_time, document.current_state)) {
    return {
      outcome: "indeterminate", usable: false,
      reconstructionStatus: "indeterminate", historicalEffect: "indeterminate",
      reasonCodes: ["current_state_substituted_for_historical_state"]
    };
  }

  return {
    outcome: "usable", usable: true,
    reconstructionStatus: document.reconstruction_status,
    historicalEffect: document.historical_effect,
    stateAtRequestedTime: document.state_at_requested_time,
    reasonCodes: ["historical_state_reconstructed_with_qualified_evidence"]
  };
}

/**
 * Optional bitemporal profile. The authoritative record must attest a complete
 * event-history window; silence alone is not proof of historical absence.
 * `recorded_at` is authoritative source commit time, NOT client observed_at.
 */
export interface BitemporalRecord extends EffectiveRecord {
  recorded_at?: string;
  logical_key: string;
  supersedes?: string[];
}
export interface BitemporalResult {
  outcome: "determinate" | "indeterminate";
  selected_record_ids: string[];
  reason_codes: string[];
}
export function selectBitemporalRecords(
  records: BitemporalRecord[],
  context: { effective_at: string; evidence_as_of: string; evaluation_time: string; history_complete_through?: string }
): BitemporalResult {
  const fail = (reason: string): BitemporalResult => ({
    outcome: "indeterminate", selected_record_ids: [], reason_codes: [reason]
  });
  let effective: number, cutoff: number, evaluation: number, coverage: number;
  try {
    effective = parseTime(context.effective_at);
    cutoff = parseTime(context.evidence_as_of);
    evaluation = parseTime(context.evaluation_time);
    coverage = context.history_complete_through ? parseTime(context.history_complete_through) : NaN;
    for (const r of records) {
      parseTime(r.effective_from);
      if (r.effective_until != null) parseTime(r.effective_until);
      if (r.recorded_at != null) parseTime(r.recorded_at);
    }
  } catch {
    return fail("invalid_temporal_input");
  }
  if (effective > evaluation || cutoff > evaluation) return fail("cutoff_or_effective_time_after_evaluation");
  if (!Number.isFinite(coverage) || coverage < cutoff) return fail("incomplete_authoritative_record_history");
  if (records.some(r => !r.recorded_at)) return fail("missing_authoritative_recording_time");
  if (records.some(r => !r.logical_key || !r.record_id)) return fail("missing_record_identity");
  if (new Set(records.map(r => r.record_id)).size !== records.length) return fail("duplicate_record_identity");
  const known = records.filter(r => parseTime(r.recorded_at!) <= cutoff);
  const ids = new Set(known.map(r => r.record_id));
  const effectiveKnown = known.filter(r =>
    parseTime(r.effective_from) <= effective &&
    (r.effective_until == null || effective < parseTime(r.effective_until))
  );
  // A supersession must be visible by the cutoff. Do not infer correction
  // solely from a later effective timestamp or the arrival of a newer record.
  for (const r of effectiveKnown) {
    if ((r.supersedes ?? []).some(id => !ids.has(id))) return fail("unknown_supersession_target");
    if ((r.supersedes ?? []).includes(r.record_id)) return fail("self_supersession");
  }
  const excluded = new Set(effectiveKnown.flatMap(r => r.supersedes ?? []));
  const selected = effectiveKnown.filter(r => !excluded.has(r.record_id));
  if (new Set(selected.map(r => r.logical_key)).size !== selected.length)
    return fail("contradictory_effective_claims_without_supersession");
  return {
    outcome: "determinate",
    selected_record_ids: selected.map(r => r.record_id).sort(),
    reason_codes: ["complete_authoritative_history_at_cutoff"]
  };
}
