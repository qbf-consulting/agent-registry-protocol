---
layout: default
title: "Lab Interoperability Programme"
nav_exclude: false
document_status: informative
permalink: /docs/interop/lab-interoperability-programme/
---

# Lab interoperability programme

This programme describes how ARPA should collect interoperability evidence before any v1.0 or broader lab proposal claims are made.

## Purpose

Interoperability is not demonstrated by one reference implementation or by schema validation alone. The lab should collect evidence that independently built or independently operated systems can exchange registry-relevant state while preserving ARPA semantics.

## Interoperability dimensions

| Dimension | Question |
|---|---|
| Syntax | Can systems parse the same records, events, receipts and evidence bundles? |
| Semantics | Do systems reach the same authority, lifecycle and historical-resolution outcomes? |
| Negative behavior | Do systems reject the same invalid, stale, conflicted or unsupported inputs? |
| Federation | Can state be projected across registries without laundering authority? |
| Discovery | Can systems expose findability without implying authorization? |
| Evidence | Can reviewers reconstruct why a decision was reached? |
| Operations | Can operators revoke, suspend, transfer and recover without silent ambiguity? |

## Evidence levels

| Level | Description |
|---|---|
| L0 — Repository-local | Repository-owned implementation and vectors only |
| L1 — Cross-runtime | More than one implementation track under repository stewardship |
| L2 — External codebase | Separate codebase consumes ARPA artifacts |
| L3 — Independently operated | Distinct operator runs tests and reports evidence |
| L4 — Multi-party exercise | Multiple operators exchange records or events in a bounded plugfest |

Current repository-owned Python and TypeScript tracks are valuable L1 evidence. They should not be overstated as L3 or L4 evidence.

## Candidate plugfest scenarios

1. **Read-only registry consumption** — external client resolves agent identity, lifecycle state and evidence references.
2. **Delegated action resolution** — two implementations evaluate the same delegated authority bundle.
3. **Federated projection** — registry B consumes selected records from registry A with provenance and competence limits.
4. **Historical reconstruction** — implementations reconstruct requested-time state from retained evidence and later material events.
5. **Discovery boundary** — search or discovery output is consumed without being treated as authority.
6. **Revocation propagation** — systems distinguish effective revocation from enforcement convergence.

## Minimum test matrix

| Scenario | Positive case | Negative case |
|---|---|---|
| Identity resolution | Valid `agentreg:` identifier resolves | Non-canonical or unsupported identifier fails safely |
| Lifecycle | Active state permits reliance within scope | Suspended or retired state blocks reliance |
| Delegation | Scoped delegation is sufficient | Delegation exceeds subject, action, time or issuer competence |
| Evidence | Required proof inputs are present | Missing or stale proof inputs fail closed |
| Federation | Provenance and competence are preserved | Imported record is treated as local authority |
| Historical | Requested-time state is reconstructed with quality disclosure | Later material event is hidden or ignored |

## Reporting

Interoperability reports should disclose:

- implementation identity and operator;
- ARPA baseline and profiles used;
- fixtures and vectors executed;
- deviations and unsupported features;
- whether tests were run by repository maintainers, implementers or independent operators;
- retained evidence bundle location.

## Promotion path

Interoperability findings can become:

- conformance vectors;
- implementation guide updates;
- protocol clarification amendments;
- experiment notes;
- v1.0 readiness evidence;
- lab proposal supporting material.

## Boundary

This programme does not claim completed interoperability. It defines how the repository will collect and classify evidence so future claims are appropriately scoped.
