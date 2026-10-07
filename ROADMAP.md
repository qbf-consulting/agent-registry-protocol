---
layout: default
title: "Roadmap"
nav_exclude: true
---

# Roadmap

## v0.9.4 — historical authority resolution and governance alignment

- deterministic requested-time versus current-state resolution;
- historical reconstruction quality and evidence lineage;
- retroactive/prospective lifecycle-effect semantics;
- retention and integrity failure handling;
- machine-readable project status and authority boundaries;
- release-gated historical-resolution conformance evidence.


## v0.9.3 — Prior implementation release

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
