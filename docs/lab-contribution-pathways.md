---
layout: default
title: "Lab Contribution Pathways"
nav_exclude: false
document_status: informative
permalink: /docs/lab-contribution-pathways/
---

# Lab contribution pathways

The ARPA lab accepts more than code patches. Agent governance needs evidence from implementers, operators, reviewers, policy practitioners, security reviewers and affected communities.

## Contribution types

| Contribution | Useful output |
|---|---|
| Specification feedback | Ambiguity report, missing requirement, unsafe implication, terminology issue |
| Implementation report | Evidence from a repository-owned, external or independently operated implementation |
| Experiment result | Hypothesis, setup, observations, negative results and retained evidence |
| Interoperability profile | Boundary mapping to another protocol or ecosystem |
| Conformance vector | Positive or negative machine-checkable case |
| Deployment report | Pilot topology, operational assumptions and failure modes |
| Threat model | Attack path, control gap or adversarial test case |
| Privacy review | Correlation, minimization, retention or disclosure risk |
| Governance review | Accountability, redress, suspension, appeal or authority concern |
| Documentation improvement | Reader path, implementer guide or operator checklist improvement |

## Preferred contribution framing

A strong contribution states:

1. the decision or failure mode it addresses;
2. the affected ARPA module, profile or guide;
3. the evidence used;
4. the proposed change or observation;
5. the claim it does **not** make.

## Good first lab contributions

- Run the quickstart and report any point where authority semantics are unclear.
- Implement a read-only registry profile and submit an implementation report.
- Add a negative vector for discovery being mistaken as authority.
- Compare ARPA lifecycle states with another agent framework's status model.
- Write an experiment note for delegated authority revocation.
- Review evidence-retention assumptions from a privacy perspective.
- Test a registry-federation conflict and document the result.

## Issue routing

| Contribution | Recommended issue type |
|---|---|
| Ambiguity or defect in protocol text | Specification feedback |
| External implementation evidence | Implementation report |
| Runtime or tool failure | Bug report |
| Larger research or experiment idea | Discussion issue or implementation report with experiment label |

## Review principles

Contributions should be reviewed against these principles:

- preserve the separation of discovery, registration, authority, delegation, enforcement and assurance;
- prefer evidence over assertion;
- retain negative results when they prevent unsafe assumptions;
- avoid expanding ARPA into a universal AI-governance framework;
- disclose scope and independence precisely;
- keep normative changes gated by explicit specification process.

## Community posture

The lab is useful only if it becomes legible to people outside the original authoring context. Contributions that improve external readability, reproducibility and implementability are high-value even when they do not add new protocol features.
