---
layout: default
title: "Delegated Authority Research Note"
nav_exclude: false
document_status: informative
permalink: /docs/research/delegated-authority/
---

# Delegated authority research note

This note is informative. It does not modify the ARPA Candidate Specification, the IETF Internet-Draft track, conformance profiles, schemas, or implementation behavior. It records the research boundary that motivates several ARPA design choices: an agent's existence or identity is not sufficient to prove authority for a consequential action.

## Research question

How can a registry make agents discoverable and governable without causing relying parties to treat registration, identity, discovery, delegation, authorization, and execution authority as the same claim?

## Boundary statement

ARPA treats agent registration as a control-plane assertion. A registry can state that an agent exists, describe lifecycle state, expose governed metadata, publish evidence, and identify relevant controllers or issuers. That does not by itself prove that the agent may perform a specific action for a specific principal in a specific workflow at a specific time.

A useful delegated-authority model needs at least six separable questions:

| Question | Example decision |
|---|---|
| Does the agent exist? | Is there a registered or resolvable agent record? |
| Is the agent identity stable enough for this use? | Is the identifier scoped, current, dereferenceable, and not contradicted by retained evidence? |
| Who controls or operates the agent? | Which controller, operator, issuer, or registry is competent for the claim being evaluated? |
| What authority was delegated? | Which action, resource, scope, duration, and constraints are covered? |
| Is the delegation still effective? | Has it expired, been suspended, revoked, narrowed, or superseded? |
| Is this workflow allowed to rely on it? | Does the relying party's policy accept the evidence, freshness, registry, and assurance level? |

Collapsing these questions creates unsafe authority laundering. Discovery can be mistaken for authorization. Registration can be mistaken for permission. Operator identity can be mistaken for delegated authority. Historic authority can be mistaken for current authority.

## Delegation dimensions

A delegation claim is useful only when its limits are inspectable. The minimum dimensions worth testing are:

- **principal** — who delegated or authorized the action;
- **agent** — which agent instance, class, or registered identity receives authority;
- **action** — what the agent may do;
- **resource** — what object, dataset, account, service, workflow, or relying context is affected;
- **scope** — the boundaries and exclusions attached to the authority;
- **time** — validity, evaluation time, and historical reconstruction boundary;
- **evidence** — records, proofs, issuer competence, provenance, and retained state;
- **enforcement** — whether downstream systems have converged on the authority status;
- **redress** — who can challenge, correct, suspend, revoke, or appeal the authority.

ARPA's registry model can carry and expose parts of this evidence, but relying parties remain responsible for policy decisions unless a governed profile says otherwise.

## Revocation and enforcement convergence

Revocation is not the same as enforcement convergence.

A registry may record that a delegation has been revoked or that an agent state has changed. That does not prove every dependent system has observed the event, invalidated caches, stopped pending work, or corrected stale projections. A useful implementation should preserve this distinction in its evidence and user-visible decisions.

| State | Meaning |
|---|---|
| Revocation recorded | The competent source has recorded a revocation or suspension event. |
| Revocation effective | The governing rules treat the authority as no longer effective from a defined time or event. |
| Enforcement propagated | Downstream systems have observed the change. |
| Enforcement acknowledged | Affected systems have provided evidence that the change was applied. |
| Residual risk retained | Gaps, late events, or stale reliance remain visible for audit or redress. |

## Research implications

This note suggests several follow-on work items without resolving them normatively:

1. Develop a delegated-action experiment that tests whether identity, delegation, authorization, and workflow permission can be evaluated independently.
2. Add negative cases where discovery, registration, or operator identity is incorrectly accepted as delegated authority.
3. Compare delegated-authority receipts across current resolution and historical reconstruction.
4. Require implementation reports to disclose whether they evaluate authority directly or merely expose registry state.

## Non-goals

This note does not define a legal agency model, impose a universal authorization framework, replace workflow-specific access control, or claim that ARPA by itself certifies an agent's permission to act.

## Related issues

- Closes #74 when merged.
- Supports #79.