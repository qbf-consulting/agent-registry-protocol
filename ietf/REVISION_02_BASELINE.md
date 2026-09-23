# ARPA Internet-Draft `-02` Baseline Review

**Status:** working revision-control artifact  
**Tracking issue:** #45  
**Published baseline:** `draft-sankarshan-agent-registry-protocol-01` (21 September 2026)  
**Target:** `draft-sankarshan-agent-registry-protocol-02`

## Purpose

This review governs the evolution from published `-01` to `-02`. The IETF archive copy of `-01` is immutable. Repository changes after that publication are candidates for `-02` only when they establish a protocol interoperability requirement or materially improve the draft's standards context.

## Post-`-01` audit

### ARPA-IETF-101 — Action-specific authority binding

The post-`-01` authority-at-commitment work demonstrates a protocol-significant gap: resolving a valid authority envelope is not sufficient to establish whether one exact consequential action is within scope now.

**Disposition:** `ietf-normative`.

The draft should require explicit action context, stable action binding when replay/substitution is possible, current authority, preservation of material constraints, exact-action approval binding, and non-affirmative treatment of missing or indeterminate material evidence.

### ARPA-IETF-102 — Collective-principal exercise semantics

The composite-principal vectors demonstrate that collective authority cannot safely be reduced to independent authority of each member.

**Disposition:** `ietf-normative`.

The draft should require current membership/controller evidence, a current exercise rule, distinct-controller counting, exact-action binding of counted contributions, and indeterminate handling of missing material composition evidence. The mechanism remains format-neutral.

### ARPA-IETF-103 — Standards-context strengthening

Revision `-01` deliberately kept adjacent-work discussion light. By `-02`, WIMSE has active architecture and workload-credential work, an individual cross-organizational agent-delegation problem statement exists, and ARPA's boundary with OAuth, RATS and SCITT can be stated precisely.

**Disposition:** `ietf-informative`.

The draft should cite and distinguish:

- WIMSE architecture and workload identity;
- cross-organizational workload/agent delegation requirements;
- OAuth 2.0 Token Exchange;
- RATS remote-attestation architecture; and
- SCITT transparency architecture.

The purpose is not citation density. It is to show that ARPA is a registry/authority-resolution protocol that composes with, rather than reimplements, workload authentication, token exchange, attestation, and transparency.

## Explicitly not promoted

The following remain outside `-02`:

- application negotiation sequencing;
- A2A task or messaging semantics;
- TRQP projection;
- project assurance scoring or certification;
- business approval workflow design;
- choice of collective-identifier or threshold-cryptography mechanism;
- settlement and payment protocols;
- reputation;
- governance appeal/redress workflows.

## Normative source

The protocol-core changes in ARPA-IETF-101 and ARPA-IETF-102 are governed by Candidate amendment `ARPA-CAND-PP-02`.

The repository authority-at-commitment vectors remain implementation evidence. PP-02 promotes only the cross-implementation invariants, not the example procurement vocabulary or local evaluator implementation.

## Revision quality objective

Revision `-02` should be stronger than `-01` in three dimensions:

1. **substance** — it closes the action-specific and collective-authority ambiguity;
2. **explanation** — it explains how authority state becomes relevant to an exact action without claiming ARPA is a universal policy engine; and
3. **standards positioning** — it cites adjacent IETF work and states composability boundaries explicitly.

The revision should not grow by importing project-only material that does not improve interoperable protocol behavior.
