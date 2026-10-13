---
layout: default
title: "ADR-003 Historical Reconstruction Is Evidence-Bound"
nav_exclude: false
document_status: informative
permalink: /docs/adr/adr-003-historical-reconstruction-is-evidence-bound/
---

# ADR-003 — Historical reconstruction is evidence-bound

## Status

Accepted as an informative architecture decision record.

## Context

ARPA supports reasoning about agent state, lifecycle events, authority, and evidence. Reviewers may ask whether a registry can answer as-of questions after withdrawal, compromise, migration, or retirement. A registry can support historical reconstruction only to the extent that relevant records, policies, events, and provenance were retained and can be evaluated.

## Decision

ARPA documentation and lab-track material will describe historical reconstruction as evidence-bound analysis.

A reconstructed answer must distinguish requested time, evaluation time, selected records, later material events, and reconstruction quality. A reconstruction result should be allowed to be indeterminate when required records are missing, contradictory, out of scope, or outside the declared retention boundary.

## Consequences

- Experiments should disclose retained evidence and reconstruction quality rather than presenting as-of answers as binary truth.
- Implementation reports should identify whether historical behavior is supported, simulated, unavailable, or incomplete.
- Documentation should avoid suggesting that current resolution proves past state.
- Retention failures and integrity gaps should be visible to reviewers and relying parties.

## Non-goals

This ADR does not create a permanent retention mandate, certify historical truth, define legal evidentiary sufficiency, or modify the Candidate Specification.

## Related issues

- Closes part of #77 when merged.
- Supports #75 and #79.