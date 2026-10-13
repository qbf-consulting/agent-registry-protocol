---
layout: default
title: "ADR-004 Federation Does Not Imply Transitive Trust"
nav_exclude: false
document_status: informative
permalink: /docs/adr/adr-004-federation-does-not-imply-transitive-trust/
---

# ADR-004 — Federation does not imply transitive trust

## Status

Accepted as an informative architecture decision record.

## Context

Federated registries may reference, project, mirror, summarize, cache, or exchange agent state. Without explicit boundaries, a receiving registry's publication could be misunderstood as acceptance of the source registry's authority for every relying context. That would create transitive-trust leakage and make stale or partial projections appear authoritative.

## Decision

ARPA documentation and lab-track material will preserve the rule that federation does not imply transitive trust.

A federated or projected record should preserve provenance, claim source, freshness, competence boundary, and receiving-registry policy. Relying parties should be able to distinguish original authority, projection, cache, search result, policy overlay, and local restriction.

## Consequences

- Federation experiments should include conflict cases and stale projection cases.
- Implementation reports should disclose whether federated state is authoritative, projected, cached, or policy-filtered.
- Documentation should avoid implying that a registry accepts all upstream claims merely because it exposes them.
- Any future normative federation profile should be introduced through a separate governed change.

## Non-goals

This ADR does not define a full federation protocol, require universal registry interoperability, settle competence rules, or modify the Candidate Specification.

## Related issues

- Closes part of #77 when merged.
- Supports #76 and #79.