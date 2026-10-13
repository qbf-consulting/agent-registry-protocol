---
layout: default
title: "Historical Reconstruction Research Note"
nav_exclude: false
document_status: informative
permalink: /docs/research/historical-reconstruction/
---

# Historical reconstruction research note

This note is informative. It does not modify the ARPA Candidate Specification, the IETF Internet-Draft track, conformance profiles, schemas, or implementation behavior. It records a research boundary for as-of reasoning: historical reconstruction is evidence-bound analysis, not a guarantee that past truth can be perfectly restored.

## Research question

How can a registry support as-of evaluation after withdrawal, revocation, compromise, migration, or retirement while making provenance, later material events, and reconstruction limits visible to relying parties?

## Boundary statement

Historical reconstruction is distinct from current resolution.

Current resolution asks what the registry, controller, issuer, or policy source says now. Historical reconstruction asks what a competent evaluator can reconstruct about a requested time using retained records, retained policy, retained evidence, later material events, and the evaluation rules available at evaluation time.

ARPA should therefore preserve four separate concepts:

| Concept | Meaning |
|---|---|
| Requested time | The time for which a party asks about agent state or authority. |
| Evaluation time | The time at which the reconstruction is performed. |
| Selected records | The retained records used to reconstruct the requested-time state. |
| Reconstruction quality | The degree to which retained evidence supports the reconstructed answer. |

## Why this matters

Agent registries may be used in consequential workflows where a later dispute turns on whether an agent was registered, suspended, delegated, recognized, or revoked at a past time. A simple current lookup cannot answer that question safely.

Unsafe shortcuts include:

- treating current state as proof of past state;
- treating missing records as proof that no authority existed;
- ignoring later material events such as compromise, corrected issuer competence, or administrative capture;
- failing to disclose retention gaps;
- presenting reconstructed state as binary truth without quality indicators;
- omitting the difference between registry state and relying-party policy acceptance.

## Reconstruction inputs

A useful reconstruction should identify the evidence used and its limitations. Candidate inputs include:

- retained agent records;
- lifecycle and status events;
- delegation records;
- issuer competence and recognition records;
- revocation, suspension, correction, and appeal records;
- policy version or rule checkpoint;
- proof inputs and verification logs;
- registry federation events;
- later material events;
- retention or integrity failure notices.

These inputs should be cited or referenced in a way that allows another evaluator to understand the basis of the answer, even when the answer remains indeterminate.

## Reconstruction quality

A reconstruction result should avoid overclaiming. The following quality levels are useful for experiments and implementation reports:

| Quality | Meaning |
|---|---|
| Complete | Required records and policy checkpoints are retained and internally consistent. |
| Partial | Some evidence exists but material records, policy versions, or event sequences are incomplete. |
| Contradicted | Retained evidence contains unresolved conflicts from competent sources. |
| Unverifiable | The records needed for a defensible answer are missing, corrupted, or outside the registry boundary. |
| Not applicable | The requested reconstruction falls outside the profile, retention policy, or registry role. |

`Not applicable` should not be usable to bypass an authority failure. It should only describe a boundary of the reconstruction request.

## Research implications

This note suggests several follow-on work items without resolving them normatively:

1. Build a historical reconstruction experiment for withdrawn or compromised agent authority.
2. Add negative cases where current state is incorrectly used as past state.
3. Require implementation reports to disclose retained records, reconstruction quality, and later material events.
4. Test how federation conflicts affect historical reconstruction when source and receiving registries retain different records.

## Non-goals

This note does not create a permanent retention mandate, certify historical truth, replace evidentiary rules in legal proceedings, or require every ARPA deployment to support historical reconstruction beyond its stated profile and retained evidence.

## Related issues

- Closes #75 when merged.
- Supports #79.