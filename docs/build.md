---
layout: default
title: "2. Build ARPA"
nav_exclude: false
nav_order: 4
permalink: /docs/build/
document_status: informative
---

# Build ARPA

This is the primary developer journey. Start with the smallest executable surface that matches your role, then expand only when the required governance semantics demand it.

## Fastest paths

| Goal | Start here | What you should produce |
|---|---|---|
| Run the repository locally | [Quickstart](quickstart.md) | Passing schema, vector and service checks |
| Stand up a pilot | [15-minute quickstart](implementation-accelerator/01-15-minute-quickstart.md) | Pilot-readiness evidence |
| Choose an implementation shape | [Implementation selection guide](implementation-selection-guide.md) | Explicit supported modules/profiles |
| Implement from the specification | [Implementor guide](implementor-guide.md) | Protocol-conformant behaviour |
| Use TypeScript/Node.js | [TypeScript implementation](typescript-implementation.md) | TypeScript conformance and interoperability evidence |
| Understand the supplied Python service | [Reference implementation architecture](reference-implementation-architecture.md) | Reference service understanding, not normative behaviour |

## Machine-readable sources developers should prefer

- [`schemas/`](../schemas/README.md) for validation contracts;
- [`registries/`](../registries/README.md) for governed values and codes;
- [`openapi/arpa-openapi.yaml`](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/openapi/arpa-openapi.yaml) for HTTP surface definitions;
- [`asyncapi/arpa-events.yaml`](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/asyncapi/arpa-events.yaml) for event contracts;
- [Conformance guide](conformance-guide.md) for executable behavioural expectations and links to the governed test-vector corpus.

Do not copy constants or behavioural assumptions from another implementation when a normative artifact or conformance vector exists.

## TypeScript developer path

```bash
cd typescript
npm install
npm run release-check
```

To run the local TypeScript HTTP service:

```bash
npm run network-server
```

The TypeScript implementation is deliberately repository-artifact driven and behaviourally independent from the Python reference implementation.

## Next

After local implementation succeeds, continue to [Assure](assure.md) before treating the implementation as interoperable or release-ready.
