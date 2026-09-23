---
layout: default
title: "ARPA Candidate Authority-at-Commitment Amendment PP-02"
nav_exclude: true
---

# ARPA Candidate Authority-at-Commitment Amendment PP-02

**Status:** Candidate Specification amendment  
**Amendment ID:** ARPA-CAND-PP-02  
**Normative baseline:** ARPA v0.9.0 Candidate Specification  
**Also applies with:** ARPA v0.9.1 Adversarial Hardening and ARPA-CAND-PP-01  
**Date:** 2026-09-23  
**License:** CC BY 4.0

## Status and authority

This document is a normative precision amendment to the ARPA Candidate Specification. It promotes the protocol-significant subset of the repository's authority-at-commitment work into the Candidate baseline without importing negotiation sequencing, business workflow, settlement, reputation, or application-specific policy.

Machine-readable requirements are published at `registries/authority-commitment-requirements-pp02.json`. Executable boundary evidence is provided by `conformance/test-vectors/authority-at-commitment/` and validated by `scripts/validate_authority_at_commitment.py`.

## 1. Action-specific authority context

When an ARPA authority evaluator determines whether resolved authority state can support a proposed material action, the evaluation MUST be bound to an explicit action context.

The action context MUST identify, directly or by stable reference:

- the action or action class;
- the resource or target to which the action applies;
- the evaluation time;
- all material constraints needed to evaluate the authority envelope; and
- a canonical action digest or equivalent stable action binding when an approval, signature, receipt, or downstream execution can otherwise be replayed or substituted across actions.

A valid identity, signature, registration, capability declaration, endpoint, credential, or successful registry resolution MUST NOT by itself be treated as authority for the action.

## 2. Current authority and constraint preservation

An affirmative authority result MUST require current effective authority at the evaluation time.

Expired, suspended, revoked, stale, conflicting, unavailable, unverifiable, or otherwise indeterminate material authority state MUST NOT produce an affirmative result.

The evaluator MUST apply all material constraints carried by the authority envelope, including applicable action, resource, purpose, counterparty, jurisdiction, value, rate, time, prohibition, and delegation-depth limits. Evaluation MUST NOT enlarge those constraints.

If the proposed action exceeds a material limit or falls outside the applicable scope, the result MUST be non-affirmative.

## 3. Approval binding

When the effective authority or relying policy requires additional approval, each counted approval MUST be bound to the exact action being evaluated or to a canonical digest that unambiguously identifies that action.

An approval for a different action, resource, amount, counterparty, material parameter, or action digest MUST NOT satisfy the requirement.

An expired, revoked, unverifiable, or materially incomplete approval MUST NOT be counted.

Missing required approval evidence produces a non-affirmative result. Where the system cannot establish whether required approval evidence exists or is current, the result MUST remain indeterminate rather than being converted to affirmative.

## 4. Collective-principal authority

An ARPA deployment MAY represent authority that belongs to a collective principal and is exercisable only through a threshold, quorum, role, or other governed exercise rule.

An evaluator processing collective-principal authority MUST distinguish:

- the collective principal whose authority is being exercised;
- the current membership or controller set relevant to the exercise rule;
- the applicable current exercise rule;
- the threshold, quorum, role, or equivalent satisfaction condition;
- each approval or contribution counted toward that condition; and
- the action binding and validity of each counted contribution.

The evaluator MUST NOT infer that an individual member or controller independently holds the collective authority merely because that member participates in the collective.

A member or controller MUST NOT be counted more than once toward a threshold unless the governing rule explicitly defines multiple independent roles and the evidence proves that those roles are separately exercisable by the same entity.

Stale membership or a superseded exercise rule MUST NOT authorize a new material action. Missing material membership or rule evidence MUST remain indeterminate.

## 5. Separation from authentication and execution

Authentication establishes control of credentials or a workload identity; it does not by itself establish action-specific delegated authority.

ARPA authority evaluation supplies protocol-visible authority state and evidence for a relying decision. It does not replace the relying party's policy decision unless the ARPA component is explicitly acting as the applicable policy decision authority.

A downstream system MUST NOT execute or accept a material action under a different action context from the one whose authority was evaluated without performing a new authority evaluation or proving equivalence under the applicable policy.

## 6. Evidence and reproducibility

An implementation producing an authority evaluation SHOULD retain enough evidence to reproduce the material decision, subject to privacy and retention constraints. This normally includes:

- evaluation time;
- authoritative source or checkpoint;
- authority and lifecycle records used;
- action context or canonical action digest;
- material constraints applied;
- approval or collective-rule evidence used; and
- the resulting affirmative, negative, or indeterminate outcome.

Evidence retention does not itself confer authority and MUST NOT override applicable privacy, confidentiality, or minimization requirements.

## 7. IETF extraction boundary

Sections 1 through 6 define protocol-core semantics eligible for extraction into the ARPA Internet-Draft.

The following remain outside the IETF protocol core unless later standardized separately:

- application negotiation sequencing;
- business approval workflow design;
- choice of threshold cryptosystem or collective-identifier mechanism;
- settlement and payment execution;
- reputation;
- ARPA project governance and assurance scoring; and
- A2A/TRQP profile-specific mappings.

The IETF extraction MUST remain mechanism-neutral: implementations can use OAuth, WIMSE workload identity, attestation, transparency receipts, credentials, signatures, or other evidence mechanisms without any one of those mechanisms becoming synonymous with ARPA authority.
