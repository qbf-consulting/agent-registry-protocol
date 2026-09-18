---
layout: default
title: "ARPA Candidate Protocol Precision Amendment PP-01"
nav_exclude: true
---

# ARPA Candidate Protocol Precision Amendment PP-01

**Status:** Candidate Specification amendment  
**Amendment ID:** ARPA-CAND-PP-01  
**Normative baseline:** ARPA v0.9.0 Candidate Specification  
**Also applies with:** ARPA v0.9.1 Adversarial Hardening amendment  
**Date:** 2026-09-18  
**License:** CC BY 4.0

## Status and authority

This document is a normative precision amendment to the ARPA v0.9.0 Candidate Specification. Its amendment identifier is deliberately independent of implementation-release semantic versions. It resolves cross-artifact ambiguity exposed during preparation of the IETF `-01` revision without changing the repository's implementation release numbering.

For Candidate conformance to the semantics covered here, the v0.9.0 Candidate Specification, the applicable v0.9.1 Adversarial Hardening amendment, and this amendment MUST be evaluated together. Where this amendment resolves an ambiguity among project prose, schemas, API contracts or implementation behaviour, this amendment controls for the semantics defined here.

Machine-readable requirements are published at `registries/protocol-precision-requirements-pp01.json`. Boundary vectors are published at `conformance/test-vectors/protocol-precision/protocol-precision-pp01.json` and are validated by `scripts/validate_protocol_precision.py`.

## 1. ARPA Agent Identifier

The protocol Agent Identifier used for ARPA Core interchange MUST use the `agentreg:` URI scheme defined by ARPA v0.9.0 §12.2:

```text
agentreg:<registry-namespace>:<agent-local-id>
```

An implementation MUST NOT emit a non-`agentreg:` URI as the ARPA Agent Identifier merely because that URI identifies the same agent in another identity or discovery system.

External identifiers, DIDs, HTTPS identifiers, platform identifiers or other aliases MAY be represented as alternate identifiers or mappings, but they MUST remain distinguishable from the ARPA Agent Identifier.

A resolver that receives a syntactically valid URI using an unsupported identifier scheme MUST NOT silently reinterpret it as an ARPA Agent Identifier. It MAY resolve the identifier through an explicitly configured mapping mechanism, provided that the returned ARPA record preserves the resulting `agentreg:` identifier and the mapping provenance.

Registries MUST NOT silently reassign an `agentreg:` identifier to a different logical agent.

## 2. Historical resolution result contract

Historical resolution is a reconstruction operation, not merely a current response filtered by timestamp.

A successful historical-resolution result MUST identify, directly or by stable reference:

- the requested effective time;
- the time at which resolution/evaluation was performed;
- the authoritative or derived records selected as effective at the requested time;
- provenance sufficient to identify the source and version/checkpoint of each selected material record;
- later material events known at evaluation time that affect interpretation of the historical result; and
- a reconstruction status or equivalent quality statement that distinguishes complete, partial, unavailable, conflicting and integrity-failed reconstruction where those states are applicable.

A registry MUST NOT silently substitute current state for requested-time state.

A registry MUST NOT silently omit a later material event when that event changes how the historical result can safely be interpreted.

If material historical evidence is unavailable, conflicting, fails integrity validation or cannot be reconstructed to the degree required by the applicable policy, the result MUST be non-affirmative and MUST expose the applicable reconstruction condition.

HTTP path layout is not part of this semantic requirement. A deployment MAY expose historical resolution through an `at` parameter, a dedicated resource, or another discoverable operation mapping, provided that the result contract above is preserved.

## 3. HTTP Problem Details contract

An ARPA HTTP API MUST represent protocol-significant errors using RFC 9457 Problem Details unless a governing transport profile defines another interoperable error representation.

An ARPA Problem Details response for a protocol-significant failure MUST contain:

- `type`, identifying a stable problem type URI;
- `title`, as human-readable non-normative text;
- `status`, containing the applicable HTTP status code; and
- `code`, containing a stable ARPA error code.

Human-readable `title` and `detail` values MUST NOT be the sole machine contract for client behaviour.

Problem extensions such as reason codes, correlation identifiers and retry metadata MAY be included when applicable. They MUST NOT expose confidential evidence, hidden authority relationships, internal exception details or security-sensitive implementation state beyond the caller's authorization.

A client that does not recognize an ARPA error code or Problem Details extension MUST NOT interpret the response as success. Unknown error semantics affecting authority, integrity, lifecycle or reconstruction MUST remain non-affirmative.

A server MUST NOT mark a failure `retryable=true` unless replay of the same operation under the documented retry conditions is safe with respect to duplicate authoritative state and external side effects.

## 4. Critical extensions and version handling

Every ARPA extension that can change interpretation of core identity, authority, lifecycle, evidence, proof, recognition or decision semantics MUST declare whether it is critical to processing.

A critical extension MUST identify a namespace and version sufficient for an implementation to determine whether it understands the required semantics.

If a receiver does not understand or support a critical extension that is material to the requested operation, it MUST return a non-affirmative result or protocol error. It MUST NOT ignore the extension and continue as though the extension were absent.

Unknown non-critical extensions MAY be ignored or retained as opaque data only when doing so cannot change core interpretation, broaden authority, suppress a prohibition, hide a lifecycle restriction or convert unknown/indeterminate state into success.

An extension MUST NOT redefine a core ARPA field in place. A semantic change to a core field requires an applicable ARPA specification version change.

An implementation MUST NOT claim support for an extension version that it cannot process according to the extension's declared semantics.

## 5. Cross-artifact consistency

The Candidate Specification remains the authoritative prose surface. Machine-readable contracts MUST remain consistent with the governing normative semantics.

For the semantics in this amendment:

- OpenAPI Agent Identifier parameters MUST constrain ARPA Agent Identifiers to `agentreg:`;
- historical-resolution schemas/contracts MUST expose requested-time and reconstruction semantics;
- the ARPA error registry MUST contain stable codes for protocol-significant failures used by conformance tests; and
- the extension/error surfaces MUST include an explicit unknown-critical-extension failure condition.

A release validation gate MUST fail when these machine-readable surfaces contradict this amendment.

## 6. IETF extraction boundary

The interoperable protocol semantics in Sections 1 through 4 are eligible for extraction into the ARPA Internet-Draft.

Project governance for the ARPA extension namespace registry, Candidate conformance profiles, appeals/redress workflows, A2A profiles and TRQP projection remains outside the IETF protocol core unless a later revision explicitly establishes an interoperability requirement and evidence for promotion.

The IETF draft MUST NOT be treated as authority to broaden or replace the richer ARPA project governance model. Conversely, project-only semantics MUST NOT silently become IETF interoperability requirements.
