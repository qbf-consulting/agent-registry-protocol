---
layout: default
title: Authority Non-Amplification
parent: Assure & Conform
---
# Authority Non-Amplification

ARPA already requires delegation attenuation, explicit scope proof, competent authority sources, fail-closed handling of missing authority, and discovery-is-not-authority semantics. This note names a cross-cutting failure pattern without changing those protocol semantics.

**Authority laundering** occurs when influence, repetition, reputation, discovery, projection, possession of unrelated authority, or another non-authoritative property is incorrectly treated as authority for the action being evaluated.

The governing rule is:

> Communication, repetition, endorsement, aggregation, projection, discovery, reputation, or transformation MUST NOT increase the authority available from competent authoritative provenance and applicable scope.

The adversarial suite at `conformance/test-vectors/adversarial/authority-laundering-v0.10.0.json` pressure-tests this rule.

An evidence change is handled separately: authoritative evidence can change whether a policy predicate applies, but that event is not itself an authority grant.

## Research provenance

This test tranche was informed by TSMM decision-resolution work and a read-only review of the independent Protocol of Care for Agents experiment:

- https://github.com/JessHines360/protocol-of-care-for-agents
- https://github.com/JessHines360/protocol-of-care-for-agents/blob/main/experiments/SIMULATION_01_RUNBOOK.md

ARPA does not adopt upstream normative vocabulary and has no dependency on that repository. No upstream writes were made.
