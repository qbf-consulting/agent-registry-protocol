# ARPA Internet-Draft `-01` Baseline Review

**Status:** working revision-control artifact  
**Issue:** #32  
**Baseline:** published `draft-sankarshan-agent-registry-protocol-00`  
**Target:** repository development toward `draft-sankarshan-agent-registry-protocol-01`

## Purpose

This review records the evidence used to decide which ARPA semantics should cross from the richer project specification into the narrower IETF protocol core. The published `-00` remains immutable historical evidence. Repository edits after publication represent candidate `-01` work and do not rewrite `-00`.

The review uses five authority surfaces:

1. `spec/agent-registry-protocol-v0.9.0.md`;
2. normative Candidate amendments;
3. machine-readable schemas and registries;
4. OpenAPI/AsyncAPI and implementation behaviour; and
5. conformance, adversarial and interoperability evidence.

A finding is accepted for IETF extraction only when its protocol significance is clear and its governing ARPA semantics are explicit enough to test or inspect.

## Disposition model

| Disposition | Meaning |
|---|---|
| `ietf-normative` | Interoperable protocol behaviour that should become normative I-D text. |
| `ietf-informative` | Context useful to IETF readers but not an interoperability requirement. |
| `base-only` | Valid ARPA semantics that remain outside the IETF protocol core. |
| `deferred` | Potentially relevant, but evidence or design maturity is insufficient. |
| `rejected` | Does not belong in the protocol revision. |

## Baseline findings

### ARPA-IETF-001 — Agent Identifier scheme alignment

**Finding:** semantic contradiction.

The Candidate Specification defines the `agentreg:` URI syntax:

```text
agentreg:<registry-namespace>:<agent-local-id>
```

The OpenAPI contract constrains `agent_id` to `^agentreg:`. The current IETF source instead says that an Agent Identifier may use any RFC 3986 URI scheme and that ARPA does not define a new URI scheme.

**Risk:** two independently conforming implementations can emit incompatible identifier forms while each appears to follow an authoritative project surface.

**Disposition:** `ietf-normative`.

**Required base action:** make the existing Candidate identifier contract explicitly controlling for ARPA Core protocol interchange and state that alternate external identifiers may be carried as aliases or mapped identifiers rather than replacing the ARPA Agent Identifier.

**Required IETF action:** describe the `agentreg:` syntax, preserve RFC 3986 framing, and make any required IANA URI-scheme action explicit rather than claiming no new scheme exists.

**Evidence:** Candidate §12.2; `openapi/arpa-openapi.yaml`; agent-core schema/examples; existing implementations and conformance declarations.

---

### ARPA-IETF-002 — Historical resolution contract

**Finding:** implementation semantics are stronger and more explicit than the original Candidate wording.

Current implementation artifacts expose deterministic historical resolution that distinguishes requested time from evaluation time, selected records, later material events, reconstruction status and evidence lineage. The IETF source contains the same core concept, but the protocol contract needs one stable set of semantic fields independent of whether a deployment exposes the operation as `?at=` or a dedicated historical-resolution resource.

**Risk:** one implementation can treat historical lookup as a simple time-filtered current response while another treats it as a reproducible reconstruction operation.

**Disposition:** `ietf-normative`.

**Required base action:** state the minimum semantic result contract for historical resolution and make path layout explicitly non-normative.

**Required IETF action:** require requested time, resolution/evaluation time, selected-record provenance, later material events and reconstruction quality/limitations; permit discoverable path mappings.

**Evidence:** `schemas/historical-resolution.schema.json`; historical-resolution vectors and validator; Python/TypeScript historical outcome equivalence; OpenAPI historical-resolution operation.

---

### ARPA-IETF-003 — Deterministic RFC 9457 error contract

**Finding:** the IETF source recommends RFC 9457 and stable ARPA error codes, while the OpenAPI contract and registry already make structured problem responses operationally significant.

**Risk:** clients may fall back to prose parsing or map unknown/indeterminate failures to success if stable machine semantics are optional or under-specified.

**Disposition:** `ietf-normative`.

**Required base action:** define the minimum ARPA HTTP Problem Details contract: stable `type`, HTTP `status`, stable ARPA `code`, non-normative human text, and safe handling of unknown codes/extensions.

**Required IETF action:** use RFC 9457 as the interoperable HTTP error envelope and require a stable ARPA code for protocol-significant failures.

**Evidence:** `openapi/arpa-openapi.yaml`; `registries/error-codes.json`; HTTP implementations and security regression coverage.

---

### ARPA-IETF-004 — Critical extension and version handling

**Finding:** ARPA already has extension namespaces and an `ARPA-EXT-CRITICAL-UNKNOWN` error code, but the cross-surface rule needs to be explicit: unknown critical semantics cannot be ignored, while non-critical unknown extensions may be preserved or ignored only when core interpretation is unchanged.

**Risk:** permissive extension handling can create accidental authority broadening or silent semantic downgrade.

**Disposition:** `ietf-normative`.

**Required base action:** define critical-extension processing, namespace/version requirements and the fail-safe rule.

**Required IETF action:** carry only the transport/protocol behaviour needed for interoperable extension processing; project-specific extension registries remain non-IETF governance artifacts.

**Evidence:** Candidate artifact-authority rules; `registries/extension-namespaces.json`; `registries/error-codes.json`; adversarial unknown-critical-extension case.

---

## Explicitly not promoted in this tranche

The following remain outside `-01` unless new evidence changes the disposition:

- governance, appeal and redress workflow design — `base-only`;
- ARPA conformance-profile hierarchy — `base-only`;
- A2A publication/compatibility profile — `base-only`;
- ARPA–TRQP projection — `base-only`;
- assurance scoring or certification — `rejected` as protocol-core behaviour;
- mandatory proof/signature suite — `deferred`;
- execution/decision receipt protocol as an independent wire contract — `deferred`.

## External IETF adjacency check

Current IETF work on agent identity, delegation and discovery reinforces the need to keep ARPA's scope narrow. ARPA should not become a universal agent identity, invocation, task or messaging protocol. Its distinctive protocol contribution remains registry-visible identity continuity, bounded authority, lifecycle, provenance, recognition boundaries and deterministic resolution semantics.

Related drafts should therefore be tracked for terminology and composability, not copied into ARPA absent a concrete interoperability dependency.

## Completion gate for `-01`

The revision is ready for submission consideration only when:

- every normative `-01` delta has a source ARPA requirement or amendment;
- the delta register contains no unclassified normative change;
- identifier, historical-resolution, error and extension semantics are mechanically checked across the relevant project artifacts;
- `make release-check` passes;
- `make ietf-check` passes against the `-01` generated artifact name;
- the diff from published `-00` is reviewed as a protocol-semantic diff, not merely an editorial diff; and
- deferred/base-only topics remain outside the IETF source.
