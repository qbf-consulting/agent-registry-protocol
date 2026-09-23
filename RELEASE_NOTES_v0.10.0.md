---
layout: default
title: "ARPA Candidate Specification v0.10.0"
nav_exclude: true
---

# ARPA Candidate Specification v0.10.0

**Date:** 23 September 2026  
**Status:** Candidate Specification  
**Release type:** normative Candidate consolidation  
**Implementation release line:** unchanged by this document  
**IETF publication line:** unchanged; `draft-sankarshan-agent-registry-protocol-02` remains the published baseline

## Purpose

ARPA Candidate v0.10.0 replaces the need to reconstruct the current normative protocol by overlaying multiple Candidate amendments on v0.9.0. It consolidates the approved protocol semantics into one authoritative prose baseline while preserving every historical source artifact and its evidence.

The consolidation incorporates:

- ARPA Candidate v0.9.0;
- the v0.9.1 adversarial-hardening amendment;
- `ARPA-CAND-PP-01` protocol precision;
- `ARPA-CAND-PP-02` authority at commitment; and
- `ARPA-CAND-PP-03` wire-contract coherence.

## Material consolidated semantics

The new baseline directly incorporates the previously approved requirements for monotonic delegation and constraint preservation; half-open temporal validity; constrained `not_applicable`; recognition conflict and issuer competence; revocation effectiveness versus enforcement convergence; reproducible evaluation context; proof-input semantics; multidimensional status composition; privacy-preserving identifier continuity; schema-correction authority; deterministic historical resolution; RFC 9457 Problem Details; critical extension handling; action-specific authority evaluation; exact-action approval binding; collective-principal exercise and snapshot semantics; parent-authority linkage; controlled vocabulary coherence; media-type preservation; and governed extension namespaces.

No new architectural layer is introduced merely by consolidating these requirements. The release is a minor Candidate version because the authoritative normative baseline has materially advanced and the overlay model is no longer an adequate implementation surface.

## Traceability and assurance

`registries/candidate-consolidation-v0.10.0.json` records the amendment-section to v0.10.0 integration map and freezes the historical source blob identities used for consolidation.

`scripts/validate_candidate_consolidation.py` is release-gated and verifies:

- v0.10.0 Candidate authority markers;
- frozen historical amendment sources;
- presence of every mapped amendment section;
- normative BCP 14 carry-over from each incorporated section;
- exclusion of IETF process-only boundary text from the protocol body; and
- immutability of the governed published-`-02` IETF control files during this consolidation.

The normative requirement catalogue is regenerated against `spec/agent-registry-protocol-v0.10.0.md` using the existing content-derived identifier policy so unchanged normative clauses retain stable requirement IDs.

## Compatibility

This is a consolidation of already approved Candidate semantics, not a redesign of ARPA. Implementations that were genuinely conformant to the complete v0.9.0 + hardening + PP-01 + PP-02 + PP-03 authority surface should not encounter intentional semantic expansion solely because the text is consolidated.

Where an implementation followed v0.9.0 while ignoring a later controlling amendment, v0.10.0 makes the current requirement explicit in the single normative baseline. Such divergence should be treated as pre-existing amendment non-conformance rather than a newly invented incompatibility.

## IETF relationship

Candidate v0.10.0 does **not** renumber, rewrite, or supersede the published IETF Internet-Draft series.

The current published IETF baseline remains:

`draft-sankarshan-agent-registry-protocol-02` — 23 September 2026.

For future `-03` work:

- published `-02` is the immutable IETF comparison baseline;
- Candidate v0.10.0 is the current ARPA project source baseline; and
- each protocol-core change still requires explicit IETF delta classification and disposition.

Project-only governance, conformance, assurance, deployment and implementation material does not enter the Internet-Draft automatically.

## Historical artifacts

The following remain retained and citable as historical provenance:

- `spec/agent-registry-protocol-v0.9.0.md`;
- `spec/agent-registry-protocol-v0.9.1-hardening.md`;
- `spec/agent-registry-protocol-protocol-precision-pp01.md`;
- `spec/agent-registry-protocol-authority-commitment-pp02.md`; and
- `spec/agent-registry-protocol-wire-contract-pp03.md`.

They should no longer be manually overlaid to determine the current Candidate behavior. New implementation and review work should begin with `spec/agent-registry-protocol-v0.10.0.md`.

## Validation

The consolidation is acceptable only when the repository's normal validation, publication, and IETF reproduction gates are green, including:

```bash
make validate
make pages-check
make ietf-check
make release-check-all
```

A successful Candidate consolidation must leave the published `-02` IETF path unaffected.
