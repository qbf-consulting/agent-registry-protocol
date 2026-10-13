---
layout: default
title: "Roadmap"
nav_exclude: true
---

# Roadmap

This roadmap distinguishes protocol and implementation release work from the broader agent-governance laboratory programme.

## Current posture

ARPA Candidate v0.10.0 is the current normative project baseline. The v0.9.5 line remains the current implementation and cross-runtime interoperability release line. Repository-owned Python and TypeScript tracks provide useful implementation-diversity evidence, but external and independently operated evidence remain required before v1.0 claims should be made.

## Lab roadmap

### Track A — Research and architecture

- [x] Frame the repository as an agent-governance laboratory as well as a protocol repository.
- [x] Publish a research agenda for registry governance, federation, delegation, historical reconstruction, evidence and assurance.
- [x] Publish an agent-governance reference architecture.
- [x] Record the control-plane framing in an architecture decision record.
- [ ] Develop the first full experiment report for registry federation conflict.
- [ ] Develop the first full experiment report for delegated authority separation.
- [ ] Develop the first full experiment report for historical reconstruction after withdrawal or compromise.

### Track B — Interoperability and external implementation

- [x] Publish an independent implementation guide.
- [x] Publish a lab interoperability programme and evidence levels.
- [x] Preserve the distinction between repository-owned implementation diversity and independently operated evidence.
- [ ] Collect at least one external implementation report.
- [ ] Run a bounded read-only registry consumption exercise.
- [ ] Run a bounded federation or projection exercise with retained evidence.
- [ ] Convert useful external findings into conformance vectors or clarification issues.

### Track C — Governance and assurance

- [x] Publish contribution pathways for research, implementation reports, experiments, threat models, privacy review and governance review.
- [ ] Add a compact assurance-composition note explaining how ARPA evidence can be consumed by adjacent assurance systems without implying certification.
- [ ] Expand privacy-preserving continuity analysis with concrete vectors.
- [ ] Add a retained-evidence and redress experiment.

### Track D — Standards and protocol extraction

- [x] Keep ARPA Candidate authority distinct from IETF Internet-Draft publication authority.
- [x] Align documentation with the current published IETF `-04` baseline.
- [ ] Use future IETF revisions only for explicitly selected protocol-core propositions.
- [ ] Keep lab, governance, conformance and deployment material out of IETF drafts unless deliberately extracted.

## Implementation and release history

## v0.9.4 — historical authority resolution and governance alignment

- deterministic requested-time versus current-state resolution;
- historical reconstruction quality and evidence lineage;
- retroactive/prospective lifecycle-effect semantics;
- retention and integrity failure handling;
- machine-readable project status and authority boundaries;
- release-gated historical-resolution conformance evidence.

## v0.9.3 — prior implementation release

- stable normative requirements and traceability;
- independent implementation-path evidence;
- networked federation and durable lifecycle tests;
- proof, key and policy integration boundaries;
- ARPA–TRQP governed query projection;
- compatibility, migration and assurance packages.

## v0.9.5 — TypeScript implementation and cross-runtime assurance

- [x] establish an independent TypeScript implementation track against the v0.9.4 normative baseline;
- [x] consume normative schemas, registries and conformance vectors without duplicating protocol definitions;
- [x] implement deterministic ARPA-Core resolution and ARPA-Authority semantics independently from Python behavior code;
- [x] implement effective-time/historical-resolution reliance semantics, decision receipts and event continuity;
- [x] compare Python and TypeScript deterministic and historical outcomes as a release-gated cross-runtime assurance check;
- [x] emit machine-readable TypeScript implementation, conformance, historical-resolution and equivalence evidence;
- [x] use cross-runtime divergence as a specification-ambiguity signal before v1.0;
- [x] add thin HTTP/client surfaces and Python↔TypeScript network interoperability;
- [x] add A2A publication/compatibility adapters after the core network surface is stable.

The repository-owned TypeScript track is implementation-diversity evidence, but it MUST NOT be represented as external organisational independence for the v1.0 gate.

## v1.0.0 — Stable Initial Release

Promotion requires external implementation experience, independently operated interoperability tests, resolution of Candidate Specification feedback, production deployment evidence for durable events and key management, security review, and confirmation that the normative surface no longer requires material change.

The bounded external interoperability profile and evidence validator are available under `conformance/external/`. External execution and independent review remain pending; publishing the profile does not satisfy this v1.0 gate.

### v0.9.3 delivered — A2A registry convergence

- [x] Publication projection and exact Agent Card URI invariant
- [x] Structured caller-visible discovery
- [x] Resolve/snapshot semantics
- [x] Agent Card compatibility classifier
- [x] Registry-specific conformance evidence

Future work may profile xRegistry, OpenID Federation, DCAT/JSON-LD, peer federation and advanced search without making them ARPA-Core dependencies.
