---
layout: default
title: "1. Understand ARPA"
nav_exclude: false
nav_order: 3
permalink: /docs/understand/
document_status: informative
---

# Understand ARPA

Use this path when you need the conceptual model before touching implementation code. ARPA separates **identity, relationships, assurance, authority, federation and evidence** so that discovery never silently becomes permission to act.

## Recommended reading order

1. [Design principles](design-principles.md) — the protocol's non-implication and governance rules.
2. [Protocol modules](protocol-modules.md) — what each module owns and depends on.
3. [Architecture-to-module mapping](architecture-to-module-mapping.md) — how protocol responsibilities map into an implementation.
4. [Candidate Specification v0.10.0](../spec/agent-registry-protocol-v0.10.0.md) — the current consolidated normative baseline.
5. [Worked scenarios](../examples/scenarios/README.md) — how the model behaves under operational and failure conditions.

## Keep these boundaries explicit

| Question | ARPA surface |
|---|---|
| Who or what is this agent? | ARPA-Core |
| What relationships connect it to principals/operators? | ARPA-Relations |
| What evidence supports claims about it? | ARPA-Assurance / ARPA-Evidence |
| May it perform this action now? | ARPA-Authority |
| Which external governance domains are recognized? | ARPA-Federation |

A discoverable, authenticated or signed agent is **not automatically authorized**. Implementations should preserve that separation in APIs, data models and user interfaces.

## Next

Developers should continue to [Build ARPA](build.md). Reviewers can go directly to [Assure an implementation](assure.md).
