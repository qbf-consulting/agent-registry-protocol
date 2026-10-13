---
layout: default
title: "Registry Federation Research Note"
nav_exclude: false
document_status: informative
permalink: /docs/research/registry-federation/
---

# Registry federation research note

## Question

How can agent registries exchange or project state without converting federation into unbounded trust inheritance?

## Working position

Registry federation should preserve provenance, competence, scope and conflict information. A receiving registry may make another registry's records visible, but visibility must not imply local authority unless the receiving governance domain explicitly accepts that authority for the relying context.

## Failure modes

| Failure mode | Risk |
|---|---|
| Authority laundering | A weak or compromised registry becomes trusted because a stronger registry republishes its records |
| Provenance loss | Relying parties cannot determine where a claim originated |
| Conflict flattening | Simultaneous but inconsistent records are hidden behind a single projected status |
| Scope expansion | A record valid in one context is treated as valid in another |
| Revocation delay | Receiving registries continue serving stale authority after source revocation |
| Privacy amplification | Federation creates wider correlation than the original registry intended |

## Minimum federation metadata

A federated projection should preserve at least:

- source registry identifier;
- source record identifier;
- selected source checkpoint or version;
- source competence claim;
- receiving registry interpretation;
- time requested and time evaluated;
- known conflicts;
- later material events when reconstructing historically;
- whether the receiving registry accepts, rejects, warns on or merely republishes the source claim.

## Experiment candidate

Use two registries and one relying party:

1. Registry A publishes an active agent record.
2. Registry B consumes or projects the record.
3. Registry A suspends the agent.
4. Registry B is evaluated before and after receiving the suspension event.
5. The relying party asks whether the agent is authoritative at requested time T1 and T2.

The experiment should show whether Registry B can disclose provenance, freshness, conflict status and its own acceptance boundary.

## Expected output

- a sequence diagram;
- example federated records;
- positive and negative vectors;
- recommended conformance assertions;
- documentation update for the interoperability programme.

## Open issues

- Whether federation requires a common transport profile;
- how to express source competence without requiring a single global trust framework;
- whether imported records should use separate identifiers or canonical source identifiers;
- how much retained evidence is sufficient for later dispute;
- whether privacy controls should be source-declared, receiver-enforced or both.
