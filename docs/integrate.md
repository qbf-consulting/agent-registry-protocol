---
layout: default
title: "5. Integrate & Interoperate"
nav_exclude: false
nav_order: 7
permalink: /docs/integrate/
document_status: informative
---

# Integrate and interoperate

ARPA is designed to compose with adjacent protocols and governance architectures without collapsing their trust semantics into ARPA or importing theirs as implicit authority.

## Integration paths

| Integration | Guide/profile | Boundary to preserve |
|---|---|---|
| TGA agentic governance architecture | [TGA Agentic Governance Alignment](architecture/tga-agentic-governance-alignment.md) | ARPA is an optional control-plane realization, not the complete agentic runtime |
| A2A Agent Cards | [A2A Registry Integration Guide](a2a-registry-integration-guide.md) | Publication/discovery is not authority |
| A2A protocol profile | [ARPA A2A v1.0 Profile](../spec/profiles/arpa-a2a-v1.0-interoperability-profile.md) | Task completion is not ARPA authorization |
| TRQP | [ARPA–TRQP architecture](architecture/trqp-arpa-interoperability.md) | TRQP remains a read-only projection interface |
| General registry exchange | [Interoperability guide](interoperability.md) | Recognition and authority remain scoped |

## TGA agentic-governance relationship

Trust Graph Artifacts' Agentic Systems Architecture and Governance guide provides a protocol-neutral method for bounded jobs, authority, delegation, capability separation, governed execution, evidence, revocation and assurance. ARPA can implement selected discovery, authority-control, lifecycle, federation and evidence responsibilities within that architecture.

The relationship is intentionally non-dependent:

```text
TSMM -> canonical semantics
TGA  -> generic governance / assurance pattern
TIS  -> portable executable contracts
ARPA -> optional registry / authority-control realization
```

The machine-readable declaration is `interop/tga-agentic-governance-alignment.json` and is release-gated by `scripts/validate_tga_alignment.py`.

## TypeScript integration surface

The v0.9.5 development track provides:

- a thin Node.js HTTP service;
- an `ArpaClient` for registry discovery, resolution and authority evaluation;
- A2A publication projection helpers;
- conservative Agent Card compatibility classification;
- Python↔TypeScript HTTP interoperability evidence.

See [TypeScript implementation](typescript-implementation.md) for supported and deferred behaviour.

## Experimental operational reliance

See the [operational assurance evidence disposition](operational-assurance-disposition.md) for optional observation, longitudinal, dependency and composite reliance profiles. Their derived results cannot create or modify an action-specific ARPA authority decision.
