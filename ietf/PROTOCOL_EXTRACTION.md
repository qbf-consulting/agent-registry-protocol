# ARPA → IETF Protocol Extraction Map

This file records which ARPA project surfaces feed the Internet-Draft and which remain outside its normative boundary. It is a scope-control artifact: inclusion in ARPA does not by itself make a project semantic an IETF protocol requirement.

| ARPA surface | IETF treatment | Evidence / source |
|---|---|---|
| Agent Identifier and namespace model | Core normative | v0.9.0 §12.2; v0.9.2 precision §1; OpenAPI `AgentId` contract |
| External/alternate identifiers | Core boundary only | v0.9.2 precision §1; alternate identifiers remain distinct from ARPA Agent Identifier |
| Record envelope and agent model | Core normative | schemas and valid examples |
| Relationships | Core normative | `schemas/relationship.schema.json`, relationship registry |
| Delegation and authority | Core normative | v0.9.0 §18 + v0.9.1 hardening §§1–5; authority schema and vectors |
| Temporal validity and event ordering | Core normative | v0.9.1 hardening §2; `ADV-003`–`ADV-005` |
| Authority outcome / `not_applicable` boundary | Core normative | v0.9.1 hardening §3; `ADV-016` |
| Recognition conflict | Core normative invariant | v0.9.1 hardening §4; `ADV-007`, `ADV-017` |
| Revocation effectiveness vs convergence | Core normative | v0.9.1 hardening §5; `ADV-006` |
| Decision reproducibility/checkpoints | Core normative | v0.9.1 hardening §6; `ADV-020` |
| Proof-input semantics | Core normative minimum | v0.9.1 hardening §7; proof-suite details remain extensible |
| Lifecycle/status | Core normative | lifecycle/status registries and vectors |
| Historical resolution | Core normative | v0.9.2 precision §2; historical schema, vectors and cross-runtime evidence |
| Query/HTTP behavior | Core normative | OpenAPI + reference implementations |
| Events | Core semantics; transport-neutral | AsyncAPI + event registry |
| HTTP Problem Details | Core normative | v0.9.2 precision §3; RFC 9457; OpenAPI Problem schema; error-code registry |
| Critical extension processing | Core normative | v0.9.2 precision §4; `ARPA-EXT-CRITICAL-UNKNOWN`; precision vectors |
| Extension namespace governance | Project-level governance | repository extension registry is not imported as an IETF registry |
| Federation/recognition | Minimal invariants only | detailed profile remains project-level |
| Multi-dimensional status composition | Project-level normative hardening | v0.9.1 hardening §8; IETF retains fail-safe invariant without project profile taxonomy |
| Pairwise continuity | Privacy/security invariant | v0.9.1 hardening §9; proof construction remains outside current I-D |
| Schema correction authority | Project change control | v0.9.1 hardening §10; not wire protocol text |
| Execution/decision receipts | Supporting evidence | potential future protocol work; not promoted by `-01` |
| Governance, appeals, redress | Project-level / deployment profile | remains outside `-01` protocol core |
| Conformance profiles | Supporting assurance | not normative in the I-D |
| A2A interoperability | Separate profile | not IETF protocol core |
| TRQP projection | Separate profile | not IETF protocol core |
| RAHP/governance assurance | Supporting evidence | not IETF protocol text |

## Revision provenance

### Published `-00`

The IETF archive for `draft-sankarshan-agent-registry-protocol-00` is immutable historical authority for the published first revision. The checked-in base authoring source intentionally remains the `-00` authoring baseline so that later revision construction is explicit rather than silently rewriting history.

### Candidate `-01`

The generated `-01` candidate is assembled from three checked-in authoring inputs plus bounded build transformations:

1. `ietf/draft-sankarshan-agent-registry-protocol.md` — published `-00` authoring baseline;
2. `ietf/fragments/adversarial-hardening.md` — protocol-core semantics imported from the v0.9.1 Candidate hardening amendment; and
3. `ietf/fragments/protocol-precision.md` — accepted protocol-core semantics imported from the v0.9.2 protocol-precision amendment.

`scripts/build_ietf_draft.sh` additionally performs reviewable exact-match transformations for revision identity, the `agentreg:` Agent Identifier contract, the RFC 7595 reference and IANA requests. The script fails rather than silently applying those transformations if the expected `-00` baseline text has changed.

The accepted `-00 → -01` propositions and their disposition are recorded in `ietf/spec-delta-v01.yaml`. The human-readable review is `ietf/REVISION_01_BASELINE.md`.

Generated RFCXML, TXT and HTML remain derivative publication artifacts. They do not acquire independent normative authority merely because a build succeeded.

## Non-implication and adversarial invariants retained in the I-D

1. Identity is not authority.
2. Key control is not accountability.
3. Capability is not permission.
4. Proof validity is not authority validity.
5. Federation is not governance recognition.
6. Stale, conflicting, unavailable, unsupported, incomparable or unverifiable material authority is not affirmative authority.
7. Historical state is evidence, not by itself a legal determination.
8. Downstream authority is the semantic intersection of upstream authority and child-declared scope.
9. Omitted upstream constraints and prohibitions do not disappear downstream.
10. `not_applicable` cannot represent failure to establish required authority.
11. Effective revocation is non-affirmative even before enforcement convergence completes.
12. Unresolved conflict between simultaneously competent authoritative sources is non-affirmative.
13. A non-ARPA external identifier is not silently reinterpreted as the ARPA Agent Identifier.
14. Historical resolution does not silently substitute current state for requested-time state.
15. Unknown protocol-significant errors do not become success.
16. Unsupported material critical extensions are not ignored.

## Change control

Every normative I-D change MUST identify:

- the originating ARPA requirement, amendment or issue;
- the affected I-D section or generated transformation;
- the executable test or inspection procedure where objectively testable;
- the evidence artifact expected from validation; and
- whether the change is `ietf-normative`, `ietf-informative`, `base-only`, `deferred`, or `rejected`.

For v0.9.1 hardening, machine-readable requirement-to-vector traceability is recorded in `registries/adversarial-hardening-requirements-v0.9.1.json` and `conformance/test-vectors/adversarial/adversarial-authority-v0.9.1.json`.

For v0.9.2 protocol precision, traceability is recorded in `registries/protocol-precision-requirements-v0.9.2.json`, `conformance/test-vectors/protocol-precision-v0.9.2.json`, and `ietf/spec-delta-v01.yaml`.

This keeps IETF prose reviewable without making the I-D depend on repository-only tooling for normative interpretation, while preserving enough evidence to challenge or reproduce each promoted protocol claim.
