# ARPA Internet-Draft `-03` Baseline Review

**Status:** governed revision-control artifact  
**Tracking issue:** #47  
**Published baseline:** `draft-sankarshan-agent-registry-protocol-02` (23 September 2026)  
**Current ARPA source baseline:** Candidate v0.10.0  
**Target:** `draft-sankarshan-agent-registry-protocol-03`

## Purpose

This review governs the evolution from published `-02` to `-03`. The IETF archive copy of `-02` is immutable. Candidate v0.10.0 is the current ARPA project source baseline, but no Candidate clause enters the IETF draft without explicit disposition here.

Revision `-03` has two goals:

1. close interoperability gaps exposed by the adversarial review of `-02` using Candidate PP-03 evidence; and
2. define clean composability boundaries with ToIP TRQP/TRQL/TSP without making ARPA dependent on non-IETF protocols.

## Dispositions

### ARPA-IETF-201 — External authoritative trust resolution
**Disposition:** `ietf-normative` — accepted.

ARPA may consume externally resolved authorization/recognition evidence, but an external query result is evidence input, not an ARPA authorization decision. Source, governing context, freshness/effective time, query context, and material provenance must be retained when they affect an authority result.

### ARPA-IETF-202 — TRQP Authorization/Recognition interoperability
**Disposition:** `ietf-normative` — accepted.

ToIP TRQP v2.0 is an approved, read-only trust-registry query protocol for Authorization and Recognition queries. ARPA may use a TRQP response as external authority/recognition evidence. ARPA processing must preserve TRQP provenance and must still apply ARPA lifecycle, delegation, action-binding, freshness, conflict, and relying-policy rules.

### ARPA-IETF-203 — Provenance of externally resolved authority evidence
**Disposition:** `ietf-normative` — accepted.

External evidence that materially contributes to an ARPA result must retain enough provenance to reproduce the material evaluation.

### ARPA-IETF-204 — Delegation independence
**Disposition:** `ietf-normative` — accepted.

TRQP v2.0 standardizes Authorization and Recognition queries and deliberately defers Delegation queries. ARPA delegation therefore remains independently defined. A future TRQP delegation operation may be consumed as evidence only if it preserves ARPA delegation invariants.

### ARPA-IETF-205 — TSP composability
**Disposition:** `ietf-informative` — accepted.

The ToIP Trust Spanning Protocol (TSP) can be an optional authenticated/confidential spanning substrate for ARPA exchanges. TSP is currently an experimental specification (0.2), so `-03` does not make it a conformance dependency or normative transport.

### ARPA-IETF-206 — TSP non-implication
**Disposition:** `ietf-normative` — accepted as a non-implication rule.

A secure TSP relationship/channel/VID does not by itself establish delegated authority, governance recognition, action authorization, collective approval, or lifecycle validity.

### ARPA-IETF-207 — TSP VID / ARPA identifier projection
**Disposition:** `defer`.

The mapping is useful profile work but not required for core `-03` interoperability. Existing ARPA alternate-identifier/mapping rules are sufficient for now.

### ARPA-IETF-208 — TRQL / action-vocabulary interoperability
**Disposition:** `defer`.

ARPA continues to require explicit action context and stable action binding. No TRQL dependency is introduced until a sufficiently stable query-language specification and interoperability evidence exist.

### ARPA-IETF-209 — Formal wire-contract extraction
**Disposition:** `ietf-normative` — accepted selectively.

Candidate PP-03 supplies stable semantics and machine contracts for authority-evaluation outcomes, RFC 9457 extensions, parent linkage, temporal boundaries, collective snapshots, content type, and namespace processing. `-03` promotes those protocol-core semantics into prose. Candidate JSON Schemas/test vectors remain version-pinned implementation/conformance evidence rather than a second normative IETF specification surface.

### ARPA-IETF-210 — Shared protocol vocabularies and IANA strategy
**Disposition:** `defer` for new centralized value registries; `ietf-normative` for stable wire values used by this document.

`-03` defines stable error/outcome/extension processing and registers the ARPA media type. It does not create new IANA registries for every relationship, event, record, or error vocabulary in an individual-submission revision. Those registries remain a future standards-process decision once extension policy and implementation experience justify centralized allocation.

### ARPA-IETF-211 — Authority outcome composition and `not_applicable`
**Disposition:** `ietf-normative` — accepted.

`not_applicable` is a normal authority-evaluation outcome, not lifecycle state and not HTTP/protocol error. It is allowed only when the selected policy/profile does not govern the requested operation and must include stable reason semantics. Missing/revoked/stale/conflicting/unsupported authority cannot be mapped to it.

### ARPA-IETF-212 — ARPA media type and content negotiation
**Disposition:** `ietf-normative` — accepted.

The project-established media type remains `application/agent-registry+json`. `-03` requests registration of that media type. `application/json` may be used only as a semantics-identical compatibility fallback. No `application/arpa+json` alias and no version parameter is introduced.

### ARPA-IETF-213 — Conformance corpus and implementation evidence
**Disposition:** `ietf-informative` — accepted.

The IETF prose is self-contained. Candidate v0.10.0 schemas and PP-03 vectors are cited as implementation/conformance evidence, with a version-pinned repository commit. They do not override this draft.

### ARPA-IETF-214 — Candidate/IETF precedence and reference durability
**Disposition:** `ietf-informative` with conformance-significant clarity — accepted.

For IETF conformance to this draft, this Internet-Draft controls protocol-core behavior. Candidate v0.10.0 remains project authority for wider governance/profile/assurance/redress material outside the draft.

### ARPA-IETF-215 — Temporal precision and discoverable evaluation assumptions
**Disposition:** `ietf-normative` — accepted.

The lower validity bound is inclusive and the upper bound exclusive. Material timestamp precision, permitted clock skew, and future-dated-observation handling must be discoverable by stable policy/profile reference when they affect authority evaluation. No universal skew constant is imposed.

### ARPA-IETF-216 — Collective-principal snapshot semantics
**Disposition:** `ietf-normative` — accepted.

Collective evaluation is bound to one stated membership/controller and exercise-rule snapshot/checkpoint. Cross-snapshot approval composition is prohibited unless explicitly authorized and evidenced.

### ARPA-IETF-217 — Current WIMSE relationship and reference pinning
**Disposition:** `ietf-informative` — accepted.

At the `-03` cut, WIMSE Architecture is pinned to `draft-ietf-wimse-arch-08` and the cross-organizational delegation problem statement to `draft-reece-wimse-cross-org-delegation-02`. Claims are limited to complementarity, not equivalence.

### ARPA-IETF-218 — Evidence-receipt composability
**Disposition:** `ietf-informative` — accepted.

SCITT receipt identifiers may be carried as evidence references where a deployment uses SCITT, but transparency/notarization does not confer agent authority.

## Scope boundary

Revision `-03` does not:

- import A2A task/messaging semantics;
- require TRQP, TSP, TRQL, SCITT, RATS, OAuth, or WIMSE for ARPA conformance;
- standardize a universal action vocabulary;
- standardize a TSP VID-to-`agentreg:` mapping;
- create IANA registries for every Candidate-controlled vocabulary;
- import governance appeal/redress workflows;
- import business approval workflow, settlement, reputation, or assurance scoring; or
- modify published `-02`.

## Evidence basis

Candidate wire-contract hardening is governed by `ARPA-CAND-PP-03` and consolidated into Candidate v0.10.0. The supporting evidence includes:

- `schemas/authority-evaluation-result.schema.json`;
- `schemas/problem-details.schema.json`;
- `registries/wire-contract-requirements-pp03.json`;
- `conformance/test-vectors/wire-contract/wire-contract-pp03.json`; and
- `scripts/validate_wire_contract_pp03.py`.

The Candidate evidence baseline used for this review is repository commit `7200c8512a13615d84c9711ac550da36ae338dd9`.

## Revision quality objective

A successful `-03` should be stronger than `-02` without becoming a protocol omnibus:

1. **wire precision** — close the remaining outcome, parent-link, media-type, time, and collective-snapshot ambiguity;
2. **federated evidence composition** — define how external trust-registry evidence contributes without becoming the decision;
3. **standards composability** — position TRQP, TSP, WIMSE and SCITT precisely and without dependency inflation;
4. **conformance evidence** — keep the prose self-contained while pointing to reproducible, version-pinned machine evidence.
