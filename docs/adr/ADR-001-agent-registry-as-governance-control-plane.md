---
layout: default
title: "ADR-001: Agent registry as governance control plane"
nav_exclude: false
document_status: informative
permalink: /docs/adr/001-agent-registry-as-governance-control-plane/
---

# ADR-001: Agent registry as governance control plane

## Status

Accepted as repository positioning guidance. Informative unless separately promoted into normative specification text.

## Context

Agent ecosystems often begin with discovery: how can a caller find an agent and its endpoint? Discovery is necessary but insufficient for consequential reliance. A relying party also needs to know whether the agent is registered, who controls it, what authority it has, whether that authority is current, which evidence supports the claim and how the claim can be challenged.

Treating the registry as a simple directory would collapse discovery, identity, authority, lifecycle and assurance into one weak abstraction.

## Decision

ARPA treats an agent registry as an authority-control plane for governed agent state.

The registry may expose discovery functions, but its architectural value is the governed publication and evaluation of agent identity, lifecycle, delegation, evidence, federation and redress semantics.

## Consequences

This decision supports:

- explicit separation of registration and authorization;
- lifecycle state as a first-class reliance input;
- retained evidence and historical reconstruction;
- conflict and competence handling across registries;
- conformance vectors for negative authority cases;
- integration with assurance systems without claiming certification.

It also constrains the repository:

- ARPA should not become a general-purpose catalogue protocol;
- discovery convenience must not override authority semantics;
- federation must preserve provenance and competence boundaries;
- implementation guides must disclose unsupported authority behavior;
- lab experiments must remain tied to evidence and governance questions.

## Alternatives considered

### Registry as directory

Rejected. Too weak for consequential reliance because it cannot answer authority, revocation, competence or redress questions.

### Registry as certification authority

Rejected. Too strong and misleading. ARPA can publish and preserve evidence for assurance consumers, but it does not itself certify safety, legality or suitability.

### Registry as credential issuer

Rejected as the primary model. ARPA may consume or project credential-derived state, but the registry role is not reducible to credential issuance.

## Review trigger

Revisit this ADR if future implementation evidence shows that most useful deployments need only discovery and lifecycle publication, or if external interoperability work demonstrates a better abstraction for authority-control behavior.
