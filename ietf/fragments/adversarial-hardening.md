# Adversarial Authority Processing

This section hardens authority-processing boundaries that can otherwise admit divergent or permissive interpretations. It does not broaden authority. A resolver or authority evaluator MUST treat ambiguity in a material authority boundary as non-affirmative.

## Delegation Scope Intersection

The effective authority of a downstream delegation MUST be the semantic intersection of the issuer's effective authority and the downstream delegation's declared scope.

For every constrained dimension, the evaluator MUST establish that the downstream constraint denotes a semantic subset of the effective upstream constraint. Relevant dimensions include actions, resources, purposes, jurisdictions, time, quantitative limits, approvals, prohibitions, assurance requirements, deployment constraints, and delegation depth.

Omission of an upstream constraint MUST NOT remove or wildcard that constraint. An omitted constrained dimension inherits the effective upstream constraint unchanged.

If two scope expressions use different vocabularies, taxonomies, jurisdiction models, resource grammars, or policy languages and no governed subset relation can be established, the evaluator MUST return a non-affirmative result. It MUST NOT infer narrowing from syntactic similarity.

A downstream delegation MUST NOT remove a mandatory upstream prohibition merely by omitting it.

## Time Boundaries

Unless a deployment profile defines a stricter rule, validity intervals are half-open: an authority is temporally applicable when `valid_from <= evaluation_time < valid_until`. If `valid_until` is absent, no upper time bound is asserted by that field, but revocation, suspension, supersession, or another material status boundary still applies.

An action evaluated exactly at `valid_until` is outside the validity interval.

A consequential deployment MUST define permitted clock skew and timestamp precision. Future-dated or clock-ambiguous material status outside the permitted skew MUST NOT yield an affirmative authority result.

Where contradictory material events have the same wall-clock timestamp, an authoritative sequence, checkpoint, or equivalent ordering mechanism MUST resolve their order. If the contradiction remains unordered, the affected state MUST be non-affirmative.

## Non-Applicability

`not_applicable` is not an authority-failure result. It MAY be returned only when the requested operation is outside the declared authority-evaluation domain of the selected policy or profile.

Missing delegation, expired or revoked authority, unavailable or unsupported evidence, an unrecognized issuer, incomparable scope, stale material state, conflicting material state, or inability to determine authority MUST NOT be represented as `not_applicable`.

## Recognition Conflicts

A published governance rule MAY establish which source is competent for a particular record type and scope. Where two or more simultaneously competent authoritative sources conflict and no applicable rule deterministically resolves the conflict, the evaluator MUST return a non-affirmative result. It MUST NOT select the most permissive source or retain an earlier affirmative result merely because it is cached.

## Revocation and Enforcement Convergence

An effective authoritative revocation immediately makes the revoked authority non-affirmative for new authority evaluations. Pending or failed enforcement acknowledgement MUST NOT restore or extend that authority.

Revocation convergence is a separate evidence property describing whether applicable enforcement surfaces have acknowledged application. A propagation deadline is an operational bound and MUST NOT be treated as evidence of convergence.

## Reproducible Decisions

For a consequential decision, reproducibility requires the request and material context, evaluation time, policy identifier and version, selected authoritative records or digests, material source checkpoints or sequence positions, freshness inputs, and recognition or issuer-competence state.

Where material state is drawn from multiple independently ordered sources, a decision receipt SHOULD identify the source checkpoint set sufficient to reconstruct the evaluated snapshot. If a coherent material snapshot cannot be established, the decision MUST be non-affirmative.

## Proof Input Semantics

A proof mechanism used for a normative ARPA record MUST define the proof input transformation, excluded or transformed proof fields, deterministic encoding, algorithm or suite identifier, verification-method interpretation, key-status evaluation time, and any domain-separation or replay-binding semantics required by the mechanism.

Canonicalization alone does not define the logical object covered by a proof. Successful proof verification MUST NOT be interpreted as current authority, issuer competence, governance recognition, or acceptable reliance.

## Relationship to Existing IETF Mechanisms

ARPA is designed to compose with existing IETF mechanisms rather than redefine them. OAuth 2.0 {{RFC6749}} and OAuth Authorization Server Metadata {{RFC8414}} can provide authorization and discovery inputs, but possession of an OAuth token or discovery of an authorization server does not by itself establish the registry-visible delegated-authority state defined by ARPA. The `/.well-known/agent-registry` discovery convention follows the Well-Known URI model in {{RFC8615}} and requires the registration discussed in the IANA Considerations section before Standards Track publication. Deployments that use HTTP Message Signatures {{RFC9421}} can protect message authenticity and integrity, but successful signature verification MUST NOT be treated as proof that the signer has current delegated authority for the requested action.
