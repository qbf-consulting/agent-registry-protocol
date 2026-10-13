---
layout: default
title: "Research Agenda"
nav_exclude: false
nav_order: 4
document_status: informative
permalink: /docs/research-agenda/
---

# Research agenda

This agenda records the research questions that sit around, behind and beyond the Agent Registry Protocol. It is intentionally broader than the current specification while remaining anchored in implementable evidence.

## Research posture

ARPA should not become a catalogue of unconstrained agent-governance aspirations. Every research question should eventually produce at least one of the following:

- a testable requirement;
- a negative result;
- a worked scenario;
- an implementation report;
- a conformance vector;
- an architecture decision record;
- an interoperability profile;
- a governance or assurance note.

## Core research questions

| ID | Question | Near-term artifact |
|---|---|---|
| RQ-001 | What makes an agent registry materially different from a directory, catalogue or discovery endpoint? | Reference architecture and ADR |
| RQ-002 | Which lifecycle states are invariant across domains, and which must remain profile-specific? | Lifecycle conformance vectors |
| RQ-003 | How should delegated authority be verified when agent identity, operator identity, issuer competence and workflow authorization are separated? | Delegation experiment |
| RQ-004 | What evidence must survive deregistration, compromise, retirement, withdrawal or operator transfer? | Evidence-retention experiment |
| RQ-005 | How can registry federation work without laundering trust from a weaker registry into a stronger relying context? | Federation experiment |
| RQ-006 | How should cross-registry discovery distinguish search convenience from authoritative resolution? | Discovery profile |
| RQ-007 | What makes historical reconstruction reliable enough for later dispute, audit or redress? | Historical-resolution evidence profile |
| RQ-008 | How should revocation effectiveness, enforcement convergence and relying-party notification be separated? | Revocation experiment |
| RQ-009 | How can privacy-preserving continuity support accountability without creating universal agent tracking? | Privacy note and vectors |
| RQ-010 | What minimum evidence should an external implementation report contain? | Implementation report guide |
| RQ-011 | How should ARPA compose with trust registries, verifiable credentials, DIDs, A2A, MCP-style agent ecosystems and risk-assessment systems? | Integration maps |
| RQ-012 | What does assurance mean for an agent registry before external certification exists? | Assurance boundary note |

## Evaluation criteria

A research output is useful when it improves at least one of these properties:

- **Answerability:** a relying party can answer a concrete authority, lifecycle, delegation or evidence question.
- **Falsifiability:** a claim can be tested, contradicted or narrowed through evidence.
- **Interoperability:** independent systems can exchange state without hidden semantic assumptions.
- **Contestability:** a subject, operator, relying party or affected person can challenge a registry assertion.
- **Operational clarity:** registry operators know what to retain, publish, revoke, suspend, reconstruct or refuse.
- **Assurance value:** the output helps reviewers determine whether a registry claim should be trusted.

## Near-term lab increments

1. **Federated registry experiment** — test conflict, competence and replay behavior across two registries.
2. **Delegated authority experiment** — separate agent identity, operator identity, issuer competence and task authorization.
3. **Historical reconstruction experiment** — reconstruct requested-time state after later withdrawal or compromise.
4. **External implementation report** — define the minimum evidence package for an independently operated implementation.
5. **Assurance composition note** — explain how ARPA evidence can be consumed by adjacent assurance systems without implying certification.

## Non-goals

This agenda does not attempt to standardize all agent behavior, all AI-governance obligations, all runtime safety controls or all legal accountability questions. It focuses on the registry layer and the evidence needed to make registry-mediated reliance inspectable and contestable.
