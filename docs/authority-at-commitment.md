# Authority at Commitment Projection

**Status:** informative implementation profile over the current ARPA Candidate baseline. This document does not amend the Candidate Specification by itself.

## Purpose

ARPA can supply governed identity, delegation, lifecycle, recognition and authority-state evidence to an action-specific decision. This projection makes explicit what a relying system must still establish before treating an agent's message or signature as authority for a material commitment.

The central rule is:

> **Discovery and authentication establish who the actor is; ARPA authority state contributes evidence about what the actor may do; the relying policy still decides whether this exact action is authorized now.**

## Projection

An action-specific commitment check consumes:

- principal and agent identifiers;
- an ARPA authority/delegation envelope;
- the exact action and resource;
- material constraints such as counterparty, jurisdiction or value;
- evaluation time;
- current lifecycle/revocation evidence;
- required approval evidence, where applicable; and
- the relying policy/version.

The check produces `allow`, `deny`, or `indeterminate` without transferring decision authority to discovery metadata or to ARPA itself.

## Required invariants

1. **Identity is not commitment authority.** A resolvable Agent Identifier, valid Agent Card, valid signature, registration, capability claim or reputation signal cannot independently authorize the commitment.
2. **Exact-action binding.** The action or canonical action digest evaluated by policy must be the one later executed or accepted.
3. **Current authority.** Expired, suspended or revoked authority cannot authorize a new commitment.
4. **Constraint preservation.** Scope, resource, jurisdiction, counterparty, value and other material limits cannot be enlarged by the projection.
5. **Approval binding.** When approval is required, it must cover the exact action digest and remain valid at evaluation time.
6. **Unknown is not allow.** Missing, stale, conflicting or unsupported material authority state remains `indeterminate` or `deny`.
7. **Historical reconstruction is explicit.** A later reconstruction identifies both the historical time being evaluated and the current reconstruction time.
8. **Layer separation.** ARPA does not own negotiation sequencing, runtime retry/budget admission, settlement or reputation.

## Example

```json
{
  "principal": "org:buyer.example",
  "agent_id": "agentreg:buyer.example:sourcing-1",
  "authority_envelope": {
    "effective_from": "2026-09-01T00:00:00Z",
    "effective_until": "2026-10-01T00:00:00Z",
    "action_classes": ["procurement.commit"],
    "resource_scope": ["opportunity:42"],
    "required_approvals": ["procurement-lead-above-100000"],
    "limits": {"amount_max": 100000}
  },
  "request": {
    "action": "procurement.commit",
    "resource": "opportunity:42",
    "amount": 90000,
    "action_digest": "sha256:<canonical-action-digest>",
    "time": "2026-09-22T12:00:00Z"
  }
}
```

A conforming integration independently evaluates the envelope and current lifecycle state. It does not infer permission from the fact that the agent was discovered or authenticated.

## Conformance evidence

The repository carries focused vectors under `conformance/test-vectors/authority-at-commitment/`. They deliberately cover an admitted in-scope action, expired authority, scope/value exceedance, wrong-action approval and unavailable authority state.

These vectors are implementation evidence for this projection only. They do not create a new universal negotiation protocol or expand the published IETF draft by implication.

## Collective principal projection

The same decision boundary can consume authority that belongs to a collective
principal and is exercisable only under a current threshold or approval rule.
This projection does not convert each controller into an independent grantor.

When `collective_authority` evidence is supplied, an allow decision additionally
requires:

- current membership evidence;
- a current exercise rule;
- a declared threshold;
- enough distinct current controllers to satisfy it;
- every counted approval bound to the exact action digest; and
- current approval validity at evaluation time.

Observed insufficient participation or stale membership/rule evidence produces
`deny`. Missing material composition evidence remains `indeterminate`.
Duplicate controller evidence cannot be counted twice.

The projection remains format-neutral. ARPA does not prescribe the threshold
cryptosystem, collective-identifier method, or upstream protocol representation.
