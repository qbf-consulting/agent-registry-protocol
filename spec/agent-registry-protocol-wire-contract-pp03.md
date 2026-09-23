---
layout: default
title: "ARPA Candidate Wire-Contract Coherence Amendment PP-03"
nav_exclude: true
---

# ARPA Candidate Wire-Contract Coherence Amendment PP-03

**Status:** Candidate Specification amendment  
**Amendment ID:** ARPA-CAND-PP-03  
**Normative baseline:** ARPA v0.9.0 Candidate Specification  
**Also applies with:** ARPA v0.9.1 Adversarial Hardening, ARPA-CAND-PP-01 and ARPA-CAND-PP-02  
**Date:** 2026-09-23  
**License:** CC BY 4.0

## Status and authority

This amendment hardens the Candidate wire contract without rewriting the v0.9.0 baseline in place. Where this amendment explicitly reconciles Candidate prose with a controlled registry, JSON Schema or OpenAPI surface, this amendment controls.

Machine-readable requirements are published at `registries/wire-contract-requirements-pp03.json`; executable boundary evidence is published at `conformance/test-vectors/wire-contract-pp03.json` and validated by `scripts/validate_wire_contract_pp03.py`.

## 1. Controlled vocabulary coherence

The Candidate prose remains authoritative for base vocabularies. Controlled registries MAY additionally contain governed extensions and deprecated compatibility aliases, but every such entry MUST declare its class and status so that a validator can distinguish base vocabulary from extensions and migration aliases.

For the base surfaces covered by this amendment:

- Candidate §24.2 defines the base event vocabulary;
- Candidate §34.2 defines the base error-code vocabulary;
- Candidate §13.4 defines the base relationship vocabulary;
- Candidate lifecycle registration states are controlled by `registries/lifecycle-statuses.json`;
- governed extension namespaces are controlled by `registries/extension-namespaces.json`.

A base registry entry and its governing JSON Schema MUST NOT disagree. Deprecated aliases MUST identify a replacement where an exact replacement exists. Profile-specific or project-specific extensions MUST be explicitly classified as extensions rather than presented as base Candidate vocabulary.

## 2. Authority evaluation result and `not_applicable`

Authority evaluation is represented by `schemas/authority-evaluation-result.schema.json`.

`not_applicable` is a normal authority-evaluation outcome. It is not:

- a lifecycle state;
- an HTTP/protocol error;
- a substitute for `deny`; or
- a substitute for `indeterminate`.

It MAY be returned only when the selected policy or profile does not govern the requested operation. A `not_applicable` result MUST include at least one stable reason code explaining the non-applicability.

The following conditions MUST NOT yield `not_applicable`: missing authority, missing delegation, expired/revoked/suspended authority, stale or conflicting material state, unknown critical extensions, unavailable or unsupported evidence, incomparable scope, unrecognized issuer, or any inability to determine authority. Such cases yield `deny`, `indeterminate`, or a protocol error according to the failure layer.

Protocol errors are reserved for malformed requests, unsupported protocol/profile/version negotiation, invalid wire representations, unavailable protocol services and equivalent transport/protocol failures. They do not encode a valid policy outcome.

**Compatibility classification:** additive. Existing affirmative/negative outcomes remain valid; this amendment makes the pre-existing `not_applicable` outcome machine-readable and removes ambiguous encodings.

## 3. Time boundaries and clock profile

Unless a stricter profile applies, authority validity remains half-open:

`effective_from <= evaluation_time < effective_until`.

An action evaluated exactly at `effective_from` is inside the interval. An action evaluated exactly at `effective_until` is outside it.

Where timestamp precision or clock skew can affect an authority decision, the selected deployment/profile MUST expose, directly or by stable policy reference:

- timestamp precision;
- maximum permitted clock skew; and
- treatment of future-dated material observations.

No universal skew value is imposed by this amendment. A clock-ambiguous material state MUST remain non-affirmative until the selected policy resolves the ambiguity.

## 4. Collective-principal snapshot semantics

A threshold, quorum, role or other collective-principal evaluation MUST bind the decision to one stated membership/controller and exercise-rule snapshot, identified by a stable snapshot/checkpoint identifier or equivalent digest.

Each approval counted toward the collective rule MUST be valid under that same snapshot unless the governing rule explicitly permits cross-snapshot composition and the evidence proves the permitted transition.

Approvals collected across membership removal/re-addition, role change, rule change or stale membership MUST NOT be combined by default.

Decision evidence MUST retain the snapshot/checkpoint identifier used to evaluate membership and the exercise rule.

## 5. Parent authority linkage

A delegated Authority Envelope MUST identify the parent authority statement from which its delegated scope derives using `derives_from`.

`derives_from` is optional for a root authority grant and REQUIRED by Candidate semantics whenever the envelope represents delegated authority derived from an upstream authority statement. Implementations MUST NOT invent a second competing parent-link field.

**Compatibility classification:** additive for root grants; conditionally required for delegated envelopes. Existing delegated records that lack an unambiguous parent reference require migration before claiming PP-03 conformance.

## 6. RFC 9457 Problem Details

Protocol-significant HTTP failures use RFC 9457 Problem Details extended by the ARPA fields defined in `schemas/problem-details.schema.json`.

The stable ARPA error code is carried in `code`. The `type` URI for a registered code is:

`https://qbfconsulting.digital/problems/arpa/{code}`

where `{code}` is the exact registered ARPA code.

Unknown material error semantics MUST fail safely. A client MUST NOT reinterpret an unknown material error as success.

## 7. Media type and content negotiation

The Candidate media type remains:

`application/agent-registry+json`

No `application/arpa+json` alias is introduced.

For HTTP APIs, `application/agent-registry+json` is the preferred ARPA representation. `application/json` MAY be supported as a compatibility fallback when the payload semantics are identical. A server MUST NOT vary normative semantics solely because the generic fallback was negotiated.

No media-type parameter is required by PP-03. Protocol/profile version negotiation remains explicit in the governing contract rather than being silently inferred from an unregistered media-type parameter.

## 8. Extension namespaces

Candidate-conformant project namespaces use collision-resistant HTTPS namespace identifiers under project-controlled authority:

`https://qbfconsulting.digital/ns/arpa/`

A deployment MAY define an external extension namespace using another collision-resistant URI/URN/reverse-DNS authority that it controls. The namespace MUST be globally collision-resistant and MUST identify an owner and schema/policy authority.

The former `https://arpa.example/...` identifiers are placeholders only. They are retained in the controlled registry solely as deprecated migration aliases and MUST NOT be used for new conformant extensions.

## 9. Conformance automation

Repository validation MUST fail when:

- base event registry and event-schema vocabularies drift;
- base relationship registry and relationship-schema vocabularies drift;
- lifecycle registration states and status-schema registration values drift;
- Candidate base error codes are absent from the controlled registry;
- a registered ARPA Problem Details code is not machine representable;
- `not_applicable` is accepted without reason semantics or for a prohibited failure case;
- PP-03 time-boundary vectors are absent or inconsistent;
- collective-principal churn vectors omit snapshot binding;
- a delegated-envelope example used by PP-03 lacks parent linkage;
- placeholder extension namespaces are marked active; or
- the OpenAPI authority-evaluation and Problem Details surfaces are not schema-bound.

## 10. IETF extraction boundary

This amendment is Candidate-first. Eligible protocol-core semantics may be extracted into a future `draft-sankarshan-agent-registry-protocol-03` under issue #47. Published `-02` remains immutable.

IETF-specific IANA registry design, reference classification, idnits work and standards-process editorial decisions remain outside this amendment.
