# ARPA Internet-Draft `-00` Submission Readiness Review

Date: 2026-09-12

This review records the repository state used to decide whether `draft-sankarshan-agent-registry-protocol-00` is ready for initial IETF submission. It is intentionally narrower than ARPA project maturity or v1.0 readiness.

## Decision

**Disposition: READY FOR `-00` SUBMISSION, subject to a final green repository/IETF build and author review of the generated RFCXML/TXT/HTML artifacts.**

The remaining gaps are community-review and future-revision work, not reasons to withhold an initial individual Internet-Draft.

## Normative delta audit: ARPA v0.9.1 through v0.9.5

| Project release | Change class | I-D impact | `-00` disposition |
|---|---|---|---|
| v0.9.1 | Implementation accelerator, pilot evidence, deployment guidance | Non-normative implementation evidence | No protocol import required |
| v0.9.2 | A2A v1.0 interoperability profile | Profile-specific projection and implementation guidance; project Candidate Specification remains v0.9.0 normative baseline | Keep outside core `-00`; preserve non-implication that discovery/authentication/task completion do not establish authority |
| v0.9.3 | A2A publication projection, caller-visible discovery, immutable snapshot/source invariants | `GET /agents`, discovery semantics, source/freshness invariants are already represented in the I-D at protocol-core level | No additional normative import required for `-00` |
| v0.9.4 | Historical Authority Resolution, reconstruction status, historical-effect semantics | Material protocol-core topic | Core requirements are already represented: requested time, evaluation time, later material events, reconstruction limitations, indeterminate fail-safe result, and historical state not being a legal determination |
| v0.9.5 | Independent TypeScript implementation, cross-runtime/network evidence | Implementation and interoperability evidence; Candidate Specification remains v0.9.0 normative baseline | Record as implementation evidence; no protocol import required |

### Audit conclusion

No unincorporated v0.9.2-v0.9.5 change requires delaying `-00`. The only clearly protocol-core post-v0.9.1 topic, historical authority resolution, is already present in the draft at the correct abstraction level. Later A2A work remains deliberately profile-specific and should not be allowed to redefine ARPA authority semantics by implication.

## Implementation status

The ARPA repository currently provides two repository-controlled implementation tracks:

- Python reference implementation and HTTP service;
- independent TypeScript implementation consuming shared schemas/vectors without importing Python behavioural code.

The release gate includes deterministic conformance, historical-resolution, cross-runtime comparison and loopback network-interoperability evidence. This is sufficient to support an initial implementation-status statement for an Internet-Draft, but it is **not** independent external implementation evidence. The project must continue to state that limitation explicitly.

For `-00`, implementation evidence is therefore a maturity signal, not a standards claim.

## IANA posture

`-00` explicitly requests **no IANA actions**. This is a deliberate initial-submission posture, not an unresolved placeholder.

The draft notes likely future consideration of:

- `/.well-known/agent-registry` registration;
- media types;
- relationship/error/extension registries where interoperability experience demonstrates a need.

This should be revisited after community review and before Standards Track publication, but it does not block `-00` submission.

## Adjacent IETF work and overlap boundary

### WIMSE

WIMSE defines workload identity architecture, identifiers, credentials and workload-to-workload authentication mechanisms. ARPA should not compete with those mechanisms. Its distinct role is registry-visible agent/deployment relationships, bounded delegated authority, lifecycle/status, historical resolution and evidence needed for reliance decisions.

Boundary rule: **workload identity/authentication can be an input to ARPA resolution or enforcement, but successful workload authentication is not by itself delegated authority.**

Relevant current WIMSE work includes the architecture, Workload Identifier, Workload Credentials, HTTP Signature and mTLS documents, plus emerging agent/delegation proposals. Community discussion should explicitly invite reuse rather than reinvention.

### OAuth / delegated authorization

OAuth defines authorization delegation and token-based access patterns. ARPA does not define a replacement grant protocol or bearer/PoP token format. Its authority envelope and registry state describe the bounded authority and lifecycle evidence that a relying system may evaluate alongside OAuth credentials and local policy.

Boundary rule: **an OAuth access token can carry or exercise authorization, while ARPA resolves the agent/principal/relationship/authority state and its current validity; neither should be silently treated as a substitute for the other.**

### RATS

RATS provides an architecture for remote attestation evidence, appraisal and results. ARPA should treat attestation as optional assurance evidence, not as proof of delegated authority.

Boundary rule: **attestation can establish properties of an execution environment; it does not establish that the agent is authorized by a principal to perform a specific action.**

### SCITT

SCITT work concerns transparency and verifiable statements/supply-chain style evidence. ARPA may reference transparent/verifiable evidence but does not need to define a transparency service itself.

Boundary rule: **provenance/transparency evidence can strengthen an ARPA record, but publication in a transparency system does not confer agent authority.**

## Community preparation

The initial submission should be positioned as an individual draft intended to invite early architectural review. The following are therefore **post-submission/community work**, not `-00` publication blockers:

1. seek WIMSE review, especially on workload/agent identifier and delegation overlap;
2. seek OAuth-area review on delegation/token boundaries;
3. seek RATS/SCITT review on evidence/attestation boundaries;
4. prepare a concise DISPATCH/ART problem statement if there is sufficient interest;
5. capture feedback as GitHub issues and reflect accepted changes in `-01` or later.

## Final repository gate before upload

Before uploading RFCXML v3 to Datatracker:

- `make ietf-check` passes;
- `make release-check-all` passes;
- generated XML, TXT and HTML are manually inspected;
- author name, QBF Consulting LLP affiliation and `sankarshan@qbfconsulting.digital` are present;
- no TODO/placeholders remain;
- IANA section continues to say no actions for `-00`;
- generated checksums/artifacts correspond to the same commit being submitted.

After submission, record the Datatracker URL in the repository and start the community-review tranche rather than continuing to modify `-00` invisibly.