---
layout: default
title: "EXP-001 Federated Registry Conflict"
nav_exclude: false
document_status: informative
permalink: /docs/experiments/exp-001-federated-registry-conflict/
---

# EXP-001 — Federated registry conflict

This experiment packet is informative. It does not modify the ARPA Candidate Specification, the IETF Internet-Draft track, conformance profiles, schemas, or implementation behavior.

## Hypothesis

Two registries can exchange, project, or reference agent state without implying that the receiving registry accepts the source registry's authority for every relying context.

A useful federation model should let a relying party distinguish:

- an authority conflict;
- a projection conflict;
- a freshness failure;
- a relying-party policy conflict;
- an indeterminate reconstruction boundary.

## Scenario

A relying party receives information about the same agent from two registries.

- Registry A is competent for the agent's original registration and lifecycle state.
- Registry B publishes a projection used by a relying workflow.
- Registry A records a suspension event.
- Registry B still exposes an active projection because of delay, policy difference, cache staleness, or incomplete event propagation.
- The relying party asks whether the agent may be accepted for a consequential workflow.

The experiment tests whether the registry and evidence model can represent the conflict without falsely treating federation as transitive trust.

## Participants and roles

| Participant | Role |
|---|---|
| Source registry | Publishes original agent state, lifecycle events, delegation references, and retained evidence. |
| Receiving registry | Publishes a projection, mirror, cache, summary, or federation-derived view. |
| Agent controller | Has a relationship to the agent and may trigger lifecycle or delegation updates. |
| Relying party | Evaluates whether the available evidence is acceptable for a workflow. |
| Auditor or reviewer | Examines retained records and determines whether the experiment result is reproducible. |

## Input conditions

The experiment should define fixture data for at least four paths:

| Case | Source state | Receiving state | Expected classification |
|---|---|---|---|
| A | Active | Active | No conflict detected, subject to policy acceptance. |
| B | Suspended | Active | Freshness failure or projection conflict. |
| C | Revoked | Active | Authority conflict unless receiving registry has a competent override. |
| D | Active | Suspended | Relying-party policy conflict or receiving-registry local restriction. |
| E | Missing retained records | Active | Indeterminate reconstruction boundary. |

## Expected behavior

A successful experiment should show that an implementation or evidence packet can:

1. identify the source of each claim;
2. identify which source is competent for which claim type;
3. distinguish original authority from projection;
4. disclose freshness, cache, retention, and event-sequence limits;
5. avoid silently upgrading a projection into authority;
6. produce a relying-party decision receipt that states the basis of acceptance, rejection, or indeterminacy.

## Evidence to retain

The experiment packet should retain or produce:

- source registry fixture records;
- receiving registry projection records;
- lifecycle event records;
- relevant policy or competence declarations;
- evaluation receipt;
- conflict classification;
- freshness and cache metadata;
- retained-record provenance;
- implementation notes and known deviations.

## Outcome model

| Outcome | Meaning |
|---|---|
| Pass | The packet distinguishes authority, projection, freshness, and relying-policy conflicts using retained evidence. |
| Fail | The packet collapses federation into transitive trust or presents stale projected state as authoritative state. |
| Indeterminate | Required retained records, policy checkpoints, or competence declarations are absent or contradictory. |
| Out of scope | The scenario depends on rules or claims outside the declared ARPA profile or experiment boundary. |

## Unresolved questions

- What minimum metadata is needed to make projection freshness inspectable?
- Should competence be declared per registry, per claim type, per agent class, or per relying-party context?
- How should implementations expose cache-derived state without encouraging unsafe reliance?
- When should an experiment result become a conformance vector rather than remain a worked scenario?

## Promotion path

If useful, results from this experiment may later be promoted into:

- negative conformance vectors for authority laundering;
- implementation-report requirements for federation and projection behavior;
- a registry-federation research note revision;
- a profile-specific clarification if repeated independent implementation evidence shows stable behavior.

Promotion requires a separate governed change. This experiment does not itself create normative requirements.

## Related issues

- Closes #76 when merged.
- Supports #79.