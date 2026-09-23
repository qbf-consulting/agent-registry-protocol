---
layout: default
title: "Repository Positioning"
nav_exclude: true
document_status: informative
---

# Repository Positioning

The Agent Registry Protocol is the normative protocol layer for resolving agent identity, relationships, authority, assurance, status, evidence, and governance. It remains transport-neutral and implementation-neutral.

## Companion-layer relationships

| Companion layer | ARPA relationship | Current repository evidence |
|---|---|---|
| Semantic and relational models | External or future companion | [Architecture-to-module mapping](architecture-to-module-mapping.md) |
| Machine-readable trust-artifact schemas | Implemented as part of ARPA | [Schema catalogue](../schemas/README.md) |
| Directory and resolution protocols | Core ARPA responsibility | [Candidate Specification v0.10.0](../spec/agent-registry-protocol-v0.10.0.md) and API contracts |
| Agent communication and task protocols | External companion with implemented A2A integration | [A2A v1.0 Interoperability Profile](../spec/profiles/arpa-a2a-v1.0-interoperability-profile.md) |
| Policy decision and enforcement systems | Partially implemented through authority evaluation, lifecycle events and receipts | [Protocol modules](protocol-modules.md) and reference implementation |
| Domain-specific assurance profiles | Extensible companion layer | [Profiles A-D](../conformance/README.md) and TRQP projection |
| Governance and pressure-test corpora | Implemented through scenarios and vectors | [Scenario catalogue](../examples/scenarios/README.md) and conformance vectors |

ARPA does not absorb companion-layer ownership. An A2A endpoint, transport authentication result or completed task does not replace ARPA authority, assurance, lifecycle, revocation or governance evidence.

Companion implementations may adopt this protocol without transferring ownership of their transport, schema, governance, or execution models to this repository.


## v0.9.3 A2A registry convergence

See the [A2A Registry Integration Guide](a2a-registry-integration-guide.md) for publication, caller-visible discovery, resolve/snapshot, compatibility and authority-boundary semantics.
