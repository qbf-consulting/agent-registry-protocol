---
layout: default
title: "Candidate Specification implementation guide"
nav_exclude: true
---

# Candidate Specification v0.10.0 implementation guide

> This path executes the complete repository release gate. For local development validation, use the [Quickstart](quickstart.md). For a pilot registry, use the [15-minute quickstart](implementation-accelerator/01-15-minute-quickstart.md). Compare all journeys in [Start Here](start-here.md).

The current normative project baseline is [ARPA Candidate v0.10.0](../spec/agent-registry-protocol-v0.10.0.md). v0.9.0 and the approved amendment documents remain historical provenance; implementers should not reconstruct the current baseline by manually overlaying them.

## Reading paths

**Architects:** candidate specification → authority model → historical authority resolution → ARPA–TRQP architecture → federation and lifecycle evidence.  
**Implementers:** schemas and APIs → mapping contract → adapters → vectors → implementation report.  
**Assurance reviewers:** requirements map → validation reports → compatibility matrix → limitations → evidence bundle.

## One-command validation

```bash
make setup
make release-check
```

The release gate additionally validates the v0.10.0 consolidation manifest, amendment-to-baseline normative carry-over, historical amendment immutability, and the protected IETF `-02` control files.
