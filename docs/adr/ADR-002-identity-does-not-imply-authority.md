---
layout: default
title: "ADR-002 Identity Does Not Imply Authority"
nav_exclude: false
document_status: informative
permalink: /docs/adr/adr-002-identity-does-not-imply-authority/
---

# ADR-002 — Identity does not imply authority

## Status

Accepted as an informative architecture decision record.

## Context

ARPA registers and resolves agent-related information. Implementers and relying parties may be tempted to treat a registered agent identity as proof that the agent is allowed to act. That shortcut would create authority laundering: a registry or discovery event would be upgraded into permission for a consequential action.

## Decision

ARPA documentation and lab-track material will preserve the rule that identity does not imply authority.

Agent identity, registration, discovery, delegation, authorization, recognition, workflow permission, and execution authority are separate decision surfaces. A registry may expose evidence relevant to those decisions, but relying parties must evaluate the applicable evidence, competence, policy, scope, and time boundary.

## Consequences

- Research notes and experiments should include negative cases where registration or discovery is incorrectly accepted as authority.
- Implementation reports should disclose whether they evaluate authority or merely expose registry state.
- Documentation should avoid language that suggests that resolving an agent identifier alone authorizes action.
- Conformance or profile work may later define stricter delegated-authority behavior, but only through an explicit governed change.

## Non-goals

This ADR does not define a universal authorization framework, replace workflow access control, create legal agency semantics, or modify the Candidate Specification.

## Related issues

- Closes part of #77 when merged.
- Supports #74 and #79.