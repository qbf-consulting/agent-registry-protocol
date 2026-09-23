# Action-Specific Authority Evaluation
{: #action-specific-authority}

ARPA resolution can expose authority state, but consequential systems often need to decide whether that state supports one particular action at one particular time. This section defines the protocol-visible invariants for such an evaluation. It does not define a universal policy language or require that the registry make the final authorization decision.

## Action Context

An authority evaluation that can affect whether a material action is accepted MUST be bound to an explicit action context. The context MUST identify the action or action class, the target resource, evaluation time, and every material constraint needed to interpret the authority envelope.

Where an approval, signature, receipt, or downstream execution could otherwise be replayed or substituted across actions, the context MUST also contain a canonical action digest or equivalent stable binding.

Successful authentication, registration, discovery, capability advertisement, signature verification, or registry resolution MUST NOT by itself be treated as authority for that action.

## Current Authority and Constraint Preservation

An affirmative authority evaluation MUST require current effective authority at evaluation time.

Expired, suspended, revoked, stale, conflicting, unavailable, unverifiable, or otherwise indeterminate material authority state MUST NOT produce an affirmative result.

The evaluator MUST preserve all applicable action, resource, purpose, counterparty, jurisdiction, value, rate, temporal, prohibition, and delegation-depth constraints. Evaluation MUST NOT enlarge an authority envelope.

## Approval Binding

When additional approval is required, every approval counted by the evaluator MUST be bound to the exact action being evaluated or to a canonical digest that unambiguously identifies that action.

An approval for a different action, resource, amount, counterparty, material parameter, or action digest MUST NOT satisfy the requirement. Expired, revoked, unverifiable, or materially incomplete approval evidence MUST NOT be counted.

When required approval evidence is missing or its current state cannot be established, the outcome MUST remain non-affirmative.

## Collective Principals

Some principals exercise authority collectively through a threshold, quorum, role, or other governed exercise rule. ARPA does not require a particular collective-identifier format or threshold cryptosystem, but an evaluator processing collective-principal authority MUST establish the current controller or membership set, the current exercise rule, and the contributions counted toward satisfaction of that rule.

Membership in a collective MUST NOT be interpreted as independent possession of the collective authority.

A controller MUST NOT be counted more than once toward a threshold unless the governing rule explicitly defines multiple independently exercisable roles and the evidence establishes those roles.

Stale membership or a superseded exercise rule MUST NOT authorize a new material action. Missing material membership or rule evidence MUST remain indeterminate.

## Execution Binding and Reproducibility

A downstream system MUST NOT accept or execute a materially different action context from the one evaluated without a new authority evaluation or a policy-proven equivalence.

An implementation producing an authority evaluation SHOULD retain enough decision input metadata to reproduce material results, subject to privacy and retention constraints. This normally includes evaluation time, authoritative source or checkpoint, selected authority/lifecycle records, the action context or action digest, material constraints, approval or collective-rule evidence, and the result.

# Relationship to Adjacent IETF Work
{: #adjacent-ietf-work}

ARPA is intended to compose with existing identity, authorization, attestation, and transparency mechanisms rather than replace them.

The WIMSE architecture {{WIMSE-ARCH}} defines workload identity and describes delegation and impersonation as security-context concerns that can be bound to workload identity. ARPA can consume workload identity as evidence about the executing workload while separately resolving agent/principal relationships, bounded authority, lifecycle state, and historical authority context. A WIMSE-authenticated workload is therefore not automatically authorized under ARPA.

OAuth 2.0 Token Exchange {{RFC8693}} provides a mechanism for exchanging security tokens and representing delegation or impersonation in token-processing systems. ARPA does not replace that grant or token mechanism. An OAuth token can be an input to authorization, while ARPA supplies registry-visible authority provenance, scope, lifecycle, relationship, and reconstruction evidence that a relying party can evaluate alongside the token.

Current WIMSE discussion of cross-organizational agent delegation {{WIMSE-CROSS-ORG}} identifies recursive attenuation, principal binding, independently administered domains, and verifiable delegation chains as open requirements. ARPA's contribution is complementary: it defines registry-visible bounded authority and fail-safe resolution semantics, including current/historical state and action-specific evaluation. It does not require that delegated authority be encoded in a particular credential or token format.

Remote attestation under the RATS architecture {{RFC9334}} can provide evidence about an execution environment and appraisal results. Such evidence MAY be referenced by ARPA as assurance input, but successful attestation MUST NOT be interpreted as proof that a principal delegated authority for a particular action.

SCITT {{RFC9943}} provides transparency architecture for signed statements and verifiable receipts. ARPA MAY reference transparency evidence or receipts to strengthen provenance and later audit, but inclusion in a transparency service MUST NOT confer agent authority, governance recognition, or permission to act.

These boundaries preserve a central ARPA rule: identity, authentication, evidence integrity, transparency, capability, and delegated authority are related but distinct protocol properties.
