# ARPA Internet-Draft `-04` Baseline Review

**Status:** governed revision-control artifact  
**Tracking issue:** #65  
**Published baseline:** `draft-sankarshan-agent-registry-protocol-03` (28 September 2026)  
**Current ARPA source baseline:** Candidate v0.10.0 + ARPA-CAND-PP-04  
**Target:** `draft-sankarshan-agent-registry-protocol-04`

## Purpose

Revision -04 is an interoperability and security-hardening revision over immutable published -03. It promotes only changes with a demonstrated wire, HTTP, security, or conformance need.

## Finding disposition

- F01: accepted, explicit Candidate↔IETF field mapping; potentially breaking.
- F02: accepted as clarification; core values remain document-defined and extensions collision-resistant; no new centralized IANA value registries in -04.
- F03: deferred as repository-hardening; publication-state automation is useful but not required for protocol correctness.
- F04: accepted as explicit tabulated/prose contracts plus version-pinned machine evidence; no normative JSON Schema appendix in -04.
- F06: accepted; Authority Evaluation Result object made explicit.
- F07: accepted; only allow/allow_with_conditions are affirmative.
- F08: accepted; deterministic fail-safe multi-dimensional status composition.
- F09: accepted; ABNF/equality/normalization defined; Permanent registration posture retained.
- F10: accepted; RFC 8785 default for JSON proof inputs when no proof profile overrides it.
- F11: accepted; protocol-visible freshness and cache bound.
- F12: accepted; role-to-positive/negative conformance matrix required.
- F14: accepted as discoverable profile bound; no universal skew constant.
- F16: accepted; core defines no universal idempotency key, profiles may.
- F17: accepted; PUT creates historical version, preserves identity, requires precondition, prevents omission-based widening.
- F18: accepted for advertised event endpoints; ordering/checkpoint/gap/resync contract required.
- F19: accepted; default-deny write authorization with discoverable policy.
- F20: accepted as cut-time reference validation gate.
- F21: accepted; `critical` becomes the single normative extension term.
- F22: accepted; concrete SSRF/dereference safeguards.
- F23: accepted editorially by using a revision-04 hardening section without adding further ordinal layering to base prose.
- F24: accepted; core vs profile HTTP operation surface clarified.
- F25: accepted; well-known registry metadata discovery separated from agent search.
- F26: substantively closed in -03; retained in -04 contract through explicit Authority Evaluation/parent-link language.
- F27: accepted at cut; front matter/keywords reviewed without gratuitous churn.
- F28: process-only; no status downgrade. Implementation evidence remains informative and version-pinned.

Regression-only F05, F13 and F15 remain closed.

## Compatibility

Potentially breaking: field-name ambiguity closure, Authority Evaluation Result location, identifier equality rules, PUT replacement semantics, write-authorization default-deny.

All other accepted changes are additive or clarifying hardening unless an implementation relied on unsafe ambiguity.

## Candidate-first governance

ARPA-CAND-PP-04 is the governing Candidate amendment. It does not create Candidate v0.11.0. A new Candidate minor version should follow only when the amendment stack is intentionally consolidated into a new baseline.

## Scope boundary

Revision -04 does not standardize a universal authentication protocol, universal action vocabulary, mandatory proof suite, mandatory event transport, TRQL dependency, or new IANA registries for every ARPA vocabulary.
