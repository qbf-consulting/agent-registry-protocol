---
layout: default
title: "Lab Experiments"
nav_exclude: false
document_status: informative
permalink: /docs/experiments/
---

# Lab experiments

Experiments convert open agent-governance questions into bounded, reviewable work. They are not release promises and they do not create normative protocol requirements until a later governed change explicitly promotes them.

## Experiment template

Each experiment should define:

| Field | Purpose |
|---|---|
| Hypothesis | The claim being tested |
| Scope | The smallest useful system boundary |
| Setup | Required registries, agents, keys, fixtures and policies |
| Expected evidence | Files, logs, reports or vectors produced by the run |
| Failure modes | What would disprove, narrow or defer the hypothesis |
| Promotion path | How useful results could become documentation, vectors, profiles or specification text |

## Candidate experiments

### EXP-001 — Federated registry conflict

**Hypothesis:** two registries can exchange or project agent state without implying that the receiving registry accepts the source registry's authority for every relying context.

**Evidence target:** conflict matrix, competence-preservation rules, example federation records, negative vectors.

### EXP-002 — Delegated authority separation

**Hypothesis:** agent identity, operator identity, issuer competence, delegated authority and workflow authorization can be evaluated separately without losing usability.

**Evidence target:** worked delegated-action scenario, proof-input matrix, positive and negative vectors.

### EXP-003 — Historical reconstruction after withdrawal

**Hypothesis:** requested-time registry state can be reconstructed after later withdrawal, compromise or retirement if provenance, selected records, later material events and reconstruction quality are retained.

**Evidence target:** reconstruction receipts, later-event disclosure examples, quality-level classification.

### EXP-004 — Revocation effectiveness versus enforcement convergence

**Hypothesis:** revocation effectiveness can be represented separately from distributed enforcement convergence, allowing relying parties to distinguish authority status from operational propagation.

**Evidence target:** revocation event sequence, enforcement acknowledgement model, stale-reliance negative cases.

### EXP-005 — Discovery without authority laundering

**Hypothesis:** discovery services can improve findability while preserving the rule that discovery is not authority.

**Evidence target:** search/discovery boundary examples, non-authoritative projection warnings, dereference failure cases.

### EXP-006 — Privacy-preserving continuity

**Hypothesis:** scoped continuity can support audit and redress without creating a universal correlation handle for all agent contexts.

**Evidence target:** scoped identifier patterns, minimization rules, continuity limits, privacy negative cases.

### EXP-007 — External implementation report

**Hypothesis:** an independently operated implementation can produce a small, repeatable evidence bundle sufficient to compare behavior against ARPA conformance expectations.

**Evidence target:** implementation report, fixture results, conformance declaration, operator statement and known deviations.

### EXP-008 — Assurance composition

**Hypothesis:** ARPA evidence can feed an assurance process without ARPA claiming to certify the agent, registry, operator or relying-party decision.

**Evidence target:** assurance-consumer mapping, evidence sufficiency table, non-certification language.

## Experiment lifecycle

| State | Meaning |
|---|---|
| Proposed | Idea is captured but not yet executable |
| Designed | Hypothesis, setup and evidence target are clear |
| Running | Implementation or evidence work is active |
| Observed | Results exist and can be reviewed |
| Promoted | Result became a profile, vector, guide, ADR or specification proposal |
| Closed | No further work is planned |

## Promotion discipline

An experiment should be promoted only when the evidence clarifies behavior that implementers, operators or reviewers can act on. Negative results are acceptable and should be retained where they prevent over-design or unsafe assumptions.
