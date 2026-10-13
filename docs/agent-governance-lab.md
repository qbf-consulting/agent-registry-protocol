---
layout: default
title: "Agent Governance Lab"
nav_exclude: false
nav_order: 3
document_status: informative
permalink: /docs/agent-governance-lab/
---

# Agent Governance Lab

This repository is a laboratory for interoperable agent governance. The Agent Registry Protocol (ARPA) is the current reference protocol and implementation surface produced by that work; it is not the whole programme.

## Problem statement

Decentralized trust infrastructure can identify parties, issue credentials, record assertions and expose trust registry state. It still lacks a common operational layer for autonomous or semi-autonomous software agents that act on behalf of people, organizations, communities or systems.

The missing layer is not just discovery. A consequential agent must be registered, scoped, delegated, supervised, suspended, audited, transferred, retired and challenged. Those actions require retained evidence, explicit authority boundaries and operational controls that survive runtime replacement, registry federation and later dispute.

## Why agent registries?

An agent registry is useful when an ecosystem needs to answer all of the following questions at the time of reliance:

- Which agent is being relied on?
- Who operates or controls it?
- What authority has been delegated to it?
- Which lifecycle state is currently effective?
- Which evidence supports that state?
- Which registry or issuer is competent to make that assertion?
- What happens when authority is revoked, transferred, contested or reconstructed historically?

ARPA treats the registry as an authority-control plane, not as a passive directory.

## Scope of the laboratory

The lab investigates how decentralized ecosystems can govern software agents across organizational and jurisdictional boundaries. Its practical work includes:

- a candidate protocol specification;
- reference and independent implementation tracks;
- conformance profiles and release-gated evidence;
- governance, security and privacy guidance;
- integration profiles for adjacent systems;
- adversarial and historical-resolution test vectors;
- experiment notes for unresolved federation, discovery, assurance and redress questions.

## What ARPA provides today

ARPA currently provides a concrete basis for experimentation:

- Candidate Specification v0.10.0 as the project normative baseline;
- Python and TypeScript implementation tracks;
- machine-readable schemas, registries, examples and conformance vectors;
- API, event and evidence contracts;
- A2A and TRQP interoperability material;
- pilot-readiness and governance-readiness assets;
- an IETF Internet-Draft extraction track for protocol-core work.

## What remains deliberately open

A lab should not prematurely collapse unresolved questions into false certainty. The repository therefore treats the following as active research and implementation topics:

- registry federation and conflict handling;
- cross-registry discovery without authority laundering;
- delegation verification across issuers and governance domains;
- revocation propagation and enforcement convergence;
- historical reconstruction after withdrawal, retirement or compromise;
- privacy-preserving continuity across contexts;
- evidence retention, minimization and redress;
- external implementation and interoperability evidence;
- assurance composition with adjacent trust-registry, credential and risk-assessment systems.

## Relationship to the protocol

The protocol is the current executable anchor for the research programme. It constrains speculation by forcing claims to become schemas, wire contracts, lifecycle rules, conformance vectors, evidence artifacts or implementation behavior.

The lab framing prevents the opposite failure mode: treating one candidate protocol as if it had already answered every governance, federation, assurance and adoption question.

## Reviewer orientation

External reviewers should evaluate this repository on two tracks:

| Track | Primary question |
|---|---|
| Protocol track | Are ARPA requirements precise, testable, implementable and bounded? |
| Lab track | Does the repository create a useful experimentation surface for agent governance across decentralized trust ecosystems? |

Both tracks matter. A precise protocol without ecosystem experimentation is brittle. A broad lab without executable artifacts is unfalsifiable.

## Next reading

- [Research agenda](research-agenda.md)
- [Agent governance reference architecture](architecture/agent-governance-reference-architecture.md)
- [Experiments](experiments/README.md)
- [Independent implementation guide](independent-implementation-guide.md)
- [Lab contribution pathways](lab-contribution-pathways.md)
