/** Informative modeled operational-reliance combination, not authorization. */
export type EvidenceFinding = {
  authority: "permit" | "deny" | "indeterminate";
  agent_status: "active" | "revoked" | "suspended" | "unknown";
  endpoint_status: "available" | "offline" | "unknown";
  observation_outcome: "observations_present" | "insufficient_evidence" | "conflicting_evidence";
  freshness_evaluated: boolean;
  dependency_readiness: "prerequisites_observed" | "unavailable" | "indeterminate";
};
export type RelianceOutcome = "deny" | "not_established" | "prerequisites_observed";
export function evaluateModeledReliance(v: EvidenceFinding): { outcome: RelianceOutcome; reasons: string[]; authority_implication: false } {
  if (v.authority === "deny" || v.agent_status === "revoked" || v.agent_status === "suspended")
    return { outcome: "deny", reasons: ["authority_or_lifecycle_denial"], authority_implication: false };
  const reasons: string[] = [];
  if (v.authority !== "permit" || v.agent_status !== "active") reasons.push("authority_not_positively_established");
  if (v.endpoint_status !== "available") reasons.push("current_endpoint_state_not_available");
  if (v.observation_outcome !== "observations_present" || v.freshness_evaluated !== true)
    reasons.push("operational_evidence_insufficient_or_unchecked");
  if (v.dependency_readiness !== "prerequisites_observed")
    reasons.push("critical_dependencies_not_established");
  return {
    outcome: reasons.length ? "not_established" : "prerequisites_observed",
    reasons: reasons.sort(),
    authority_implication: false
  };
}
