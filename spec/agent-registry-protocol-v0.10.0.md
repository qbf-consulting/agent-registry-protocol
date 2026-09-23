---
layout: default
title: "Agent Registry Protocol and Architecture (ARPA)"
nav_exclude: true
---

# Agent Registry Protocol and Architecture (ARPA)

## A Distributed Authority-Control Plane for Delegated Action

**Category:** Standards Track  
**Intended Status:** Candidate Specification  
**Version:** 0.10.0  
**Date:** 2026-09-23  
**Author:** Sankarshan Mukhopadhyay  
**License:** CC BY 4.0  

---

## Status of This Memo

This document is the authoritative consolidated Candidate Specification for Agent Registry Protocol and Architecture (ARPA) v0.10.0. It consolidates the architecture, normative protocol requirements, conformance targets, extension boundaries, implementation contracts, and evidence expectations into a single specification surface.

This document is not an adopted standard and does not claim certification, accreditation, legal recognition, formal cryptographic review, or production security approval. Normative requirements define behavior necessary for the applicable conformance target. Explanatory text, implementation notes, examples, deployment patterns, and appendices are informative unless a section explicitly states otherwise.

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) (RFC 2119, RFC 8174) when, and only when, they appear in all capitals, as shown here. Use of these terms does not imply IETF process or endorsement; they are adopted here solely as a precise, widely understood requirements vocabulary.

---

## Abstract

This document specifies an architecture, information model, protocol surface, processing model, lifecycle framework, security architecture, governance model, and conformance requirements for registries of software agents that act on behalf of principals.

The specification is founded on the proposition that an agent registry is not merely a directory of autonomous software objects. It is a distributed authority-control plane for delegated action. A registry conforming to this specification therefore makes separate but linked claims about agent identity, software version, operational deployment, control, accountability, delegated authority, capability, assurance, runtime state, governance, and redress.

The protocol is designed to help a relying party answer four progressively stronger questions:

1. **Identification:** What agent is this, and is it the same logical agent previously encountered?
2. **Attribution:** Who operates, controls, sponsors, governs, or accepts responsibility for it?
3. **Authorization:** Why may this agent perform this particular action, for this principal, under these conditions?
4. **Accountability:** What evidence exists, what institution governs the action, and how can an error or harm be challenged and repaired?

The specification defines persistent identity and lineage, typed relationships, authority envelopes, delegation chains, capability and assurance records, multidimensional status, point-in-time resolution, authority and reliance evaluation, execution evidence, registry federation, explicit recognition, privacy-preserving resolution, governance, appeal, and conformance profiles.

---

## Document Conventions

This draft uses four kinds of text:

- **Normative requirements** contain requirements terms and define conformance behavior.
- **Rationale** explains the design problem or failure mode addressed by a requirement.
- **Implementation notes** describe non-exclusive implementation approaches.
- **Examples** illustrate behavior but do not override normative language.

Unless explicitly stated otherwise, examples use JSON and HTTP for readability. The architecture is transport-independent and proof-format-independent.

---

## Candidate Specification Control

This document is the sole authoritative prose specification for ARPA v0.10.0. Schemas, controlled registries, OpenAPI and AsyncAPI descriptions, conformance vectors, implementation reports, and evidence bundles are subordinate machine-readable artifacts. Where an inconsistency is found, implementations MUST fail safely, record the conflict, and open a specification defect rather than infer an affirmative authority decision.

### Normative and informative content

Sections 12 through 37 are normative except where marked as rationale, example, implementation note, deployment guidance, or informative interoperability material. Sections 1 through 11 establish the architectural and authority model and are normative where they use BCP 14 requirement terms. Appendices are informative unless a requirement explicitly incorporates an appendix item.

### Conformance targets

ARPA defines the following independently claimable conformance targets:

- Registry publisher
- Registry consumer or resolver
- Authority evaluator
- Event publisher
- Event consumer or enforcement point
- Proof verifier
- Policy adapter
- Federation participant
- ARPA–TRQP projection adapter

An implementation MUST declare each target it claims, the profiles and versions implemented, its known deviations, and the evidence supporting the claim. Conformance to one target MUST NOT be presented as conformance to another.

### Stable Candidate requirements

The following requirement identifiers anchor the Candidate Specification. Detailed requirements in later sections refine these controls and are traceable through the conformance manifests.

| ID | Candidate requirement | Primary target |
| --- | --- | --- |
| ARPA-CAND-001 | Implementations MUST distinguish identity, authority, assurance, proof validity, registry operation, and lifecycle status. | Registry, consumer |
| ARPA-CAND-002 | Delegation MUST NOT expand the issuer's effective scope. | Authority evaluator |
| ARPA-CAND-003 | Recognition MUST be scoped, current, withdrawable, and non-transitive unless explicitly declared. | Registry, evaluator |
| ARPA-CAND-004 | Technical federation MUST NOT imply governance recognition or authority transfer. | Federation participant |
| ARPA-CAND-005 | Revocation MUST produce durable evidence and MUST NOT be considered converged until applicable enforcement acknowledgements exist. | Publisher, consumer, enforcement point |
| ARPA-CAND-006 | Unknown, conflicting, stale, unsupported, or unavailable authority MUST resolve to deny or indeterminate and MUST NOT result in implicit allow. | Evaluator |
| ARPA-CAND-007 | Events MUST be persistently sequenceable, replayable, deduplicated, and processable idempotently. | Event publisher, consumer |
| ARPA-CAND-008 | Proof validity MUST NOT be interpreted as authority validity. | Proof verifier, evaluator |
| ARPA-CAND-009 | Policy decisions MUST retain policy version, evaluated inputs, outcome, reason codes, conditions, prohibitions, and evidence references. | Policy adapter |
| ARPA-CAND-010 | Capability and conformance claims MUST be machine-readable, versioned, and evidence-bounded. | Implementation |
| ARPA-CAND-011 | ARPA–TRQP projection support MUST be declared independently from ARPA and TRQP conformance. | Projection adapter |
| ARPA-CAND-012 | A query projection MUST preserve scope and MUST NOT produce an affirmative result for revoked, suspended, expired, stale, conflicting, or unresolved authority. | Projection adapter |

### Consolidation provenance

ARPA v0.10.0 is a normative consolidation release. It incorporates the approved semantics of ARPA v0.9.0, the v0.9.1 adversarial-hardening amendment, `ARPA-CAND-PP-01`, `ARPA-CAND-PP-02`, and `ARPA-CAND-PP-03`. Those historical artifacts remain immutable provenance records but are no longer required as overlay documents for implementing the current Candidate baseline.

The consolidation does not make the ARPA implementation-release line or the IETF Internet-Draft revision line equivalent to this Candidate version. Published Internet-Draft revisions remain immutable publication artifacts; protocol-core semantics cross into a later IETF revision only through the governed IETF delta process.

### Artifact authority and traceability

Every objectively testable normative requirement MUST map to at least one test or inspection procedure and an expected evidence output. Machine-readable artifacts MUST identify their specification version and governing authority. Extensions MUST use a registered namespace, declare version and authority, and MUST NOT redefine a core field or weaken a fail-safe requirement.

The machine-readable normative requirement catalogue is published at `registries/normative-requirements.json`. Each captured BCP 14 clause has a stable content-derived requirement identifier, specification section, verification procedure, and expected evidence output. `scripts/validate_normative_requirements.py` MUST fail when the catalogue is stale, duplicate, or no longer covers the normative Candidate Specification text. Requirement identifiers change only when the normative clause itself changes materially.

## Table of Contents

### Part I: Context and Requirements

1. Introduction  
2. Problem Statement  
3. Scope  
4. Use Cases  
5. Requirements and Failure Modes  
6. Design Principles  
7. Terminology  

### Part II: Architecture

8. Architectural Overview  
9. Trust and Authority Boundaries  
10. Logical Planes  
11. Roles and Responsibilities  
12. Identifier and Namespace Model  
13. Record and Relationship Model  
14. Registry and Enforcement Interaction  

### Part III: Normative Protocol

15. Agent Registration  
16. Version and Deployment Management  
17. Relationship Management  
18. Delegation and Authority  
19. Capability and Assurance  
20. Lifecycle and Status  
21. Query Protocol  
22. Authority Evaluation  
23. Reliance Evaluation  
24. Events and Subscriptions  
25. Execution and Decision Receipts  
26. Federation and Recognition  
27. Governance, Appeals, and Redress  

### Part IV: Cross-Cutting Requirements

28. Processing Rules  
29. Security Architecture  
30. Privacy Architecture  
31. Scalability and Availability  
32. Audit and Transparency  
33. Versioning and Extensibility  
34. Error Handling  

### Part V: Conformance and Deployment

35. Conformance Profiles  
36. Conformance Requirements  
37. Test Vectors and Interoperability Testing  
38. Deployment Patterns  
39. Operational Guidance  
40. Open Issues  
41. IANA Considerations  

Appendix A. Example Records  
Appendix B. Example Queries and Negative Outcomes  
Appendix C. Reference State Machines  
Appendix D. Conformance Checklist  
Appendix E. Threat Model  
Appendix F. Privacy Patterns  
Appendix G. Design Rationale  
Appendix H. Change Log

---

# 1. Introduction

Software agents increasingly act with varying degrees of autonomy across digital systems. They retrieve information, negotiate with services, invoke tools, access protected data, initiate transactions, coordinate subordinate agents, and generate outputs that may materially affect people and institutions.

A conventional service registry can identify a network location and describe a set of functions. That model is insufficient when an agent acts under delegated authority.

For delegated action, a relying party needs to determine:

- which agent is involved;
- whether the presented agent is the same logical agent previously encountered;
- which runtime or deployment is currently executing;
- who operates, controls, sponsors, or is accountable for the agent;
- which principal authorized the action;
- which action classes, resources, purposes, limits, and prohibitions apply;
- whether further delegation is permitted;
- which capabilities were declared, tested, or independently assured;
- whether the current deployment remains within the scope of applicable assurance;
- whether the agent or its authority has been suspended, restricted, compromised, revoked, retired, or superseded;
- what evidence exists for a particular action;
- which governance framework applies; and
- how an affected party may challenge, appeal, or obtain redress.

This specification defines a registry architecture capable of answering those questions.

The registry is not required to store all underlying evidence, confidential delegation terms, or operational telemetry directly. It is required to provide authoritative, policy-aware, and verifiable resolution paths to those materials and to communicate their current status, provenance, and applicability.

The architectural objective is therefore not universal trust certification. It is machine-resolvable reliance.

---

# 2. Problem Statement

## 2.1 From Service Discovery to Delegated Action

Traditional registries and service catalogs generally answer a bounded set of questions: what a service is called, where it can be reached, which protocol it supports, and which organization publishes it. Those answers are useful for routing and discovery. They are insufficient when a software agent can cause effects in the world on behalf of another party.

An agent may access protected records, recommend or determine eligibility, prepare a transaction, submit a transaction, alter a workflow, instruct another agent, or exercise a permission originally granted to a human or institution. In those circumstances, the relying party needs to understand not merely the agent's advertised functionality, but the institutional and technical basis on which the proposed action may be accepted.

A directory entry can state that an agent supports `purchase.submit`. It cannot, by that statement alone, establish that the agent may submit purchase order 456 for principal P, in India, before a particular expiry time, below a stated monetary ceiling, after obtaining an approval, while avoiding prohibited suppliers. The missing information is not descriptive metadata. It is bounded authority.

## 2.2 The Four Registry Questions

A registry intended for delegated action MUST be capable of supporting four distinct classes of resolution:

| Function | Question | Typical Evidence |
| --- | --- | --- |
| Identification | What agent is this? | Identifier, key binding, version, deployment, lineage |
| Attribution | Who stands behind or controls it? | Operator, controller, accountable entity, governance relationships |
| Authorization | Why may it perform this action? | Authority envelope, delegation chain, approvals, policy decision |
| Accountability | How can the act be examined or repaired? | Receipts, evidence, incident records, appeal and redress routes |

These functions are cumulative but not interchangeable. An agent can be identified without being authorized. An operator can be attributable without accepting liability for every action. An assurance provider can verify controls without granting authority. A valid delegation can exist while the runtime is compromised or the assurance has expired.

## 2.3 Structural Risks Addressed by This Specification

This specification addresses recurring failure modes in agent infrastructure:

- treating registration as evidence of trustworthiness;
- treating control of a key or registry record as authority to act;
- treating an advertised capability as permission;
- allowing authority to persist after a change of principal, controller, operator, or deployment;
- applying assurance obtained for one version or environment to another;
- relying on current state when a dispute requires historical state;
- publishing revocation without ensuring that credentials, sessions, or subordinate delegations are disabled;
- allowing opaque federation to create accidental transitive trust;
- providing no protocol-visible route for correction, appeal, or redress; and
- relying on stale projections without disclosing their age or provenance.

## 2.4 Registry Role in the Control Loop

The registry defined here is not assumed to execute every action itself. It participates in a wider control loop:

```text
Identity and relationship resolution
              |
              v
Authority and reliance evaluation
              |
              v
Policy decision and required approvals
              |
              v
Runtime policy enforcement
              |
              v
Execution and evidence production
              |
              v
Status, audit, incident, and redress feedback
```

The registry establishes and resolves authoritative conditions of reliance. A Policy Decision Point evaluates those conditions against action context and relying-party policy. A Policy Enforcement Point controls actual execution. Evidence and status updates feed back into later decisions.

A registry that publishes authority but cannot communicate status changes to enforcement surfaces MAY conform only to lower profiles. It MUST NOT claim conformance to a delegated-authority or high-assurance profile unless the profile's enforcement and revocation requirements are met.

## 2.5 Desired Outcome

The desired outcome is not a universal list of trusted agents. Such a list would conceal differences in purpose, risk, jurisdiction, governance, assurance scope, and acceptable failure.

The desired outcome is a common protocol through which a relying party can determine whether the conditions for a particular act are satisfied, not satisfied, or indeterminate, and can obtain evidence explaining that determination.

---

# 3. Scope

## 3.1 In Scope

This specification defines requirements for:

- registration of persistent agent identifiers;
- representation of agent versions, deployments, and lineage;
- binding of agents to cryptographic keys and service endpoints;
- representation of developers, publishers, deployers, operators, controllers, sponsors, principals, accountable entities, assurance providers, governance authorities, and infrastructure providers;
- delegation and authority records;
- authority evaluation;
- capability declarations, verifications, and authorizations;
- assurance claims and conformance profiles;
- lifecycle, operational, security, and authority status;
- point-in-time state resolution;
- registry query and discovery interfaces;
- event publication and subscription;
- execution and decision receipts;
- federation and recognition between registries;
- governance and redress metadata;
- security, privacy, audit, and availability controls; and
- conformance testing.

## 3.2 Out of Scope

This specification does not define:

- a universal agent communication protocol;
- a universal task protocol;
- a universal ontology for every possible agent capability;
- a universal legal theory of agency;
- a universal liability regime;
- a mandatory distributed ledger implementation;
- a mandatory credential format;
- a mandatory cryptographic suite;
- a mandatory policy language;
- a universal reputation score;
- a universal definition of a “trusted agent”; or
- a requirement that all registry data be public.

Implementations MAY use distributed ledgers, transparency logs, conventional databases, content-addressed stores, confidential computing systems, federated databases, or combinations thereof, provided that the conformance and security requirements of this specification are met.

---

# 4. Use Cases

This section describes representative use cases used to derive and pressure-test the requirements. The examples are not exhaustive and do not mandate particular sectors.

## 4.1 Low-Risk Informational Agent

A research assistant publishes summaries from public sources. A relying party needs to resolve the agent's identifier, publisher, endpoints, supported protocols, current version, and retirement status. No transactional authority is exercised.

This use case motivates the Discovery Registry profile. It demonstrates that a lightweight registry remains valuable and that the higher-assurance features in this specification are progressive rather than universally mandatory.

## 4.2 Enterprise Workflow Agent

An enterprise agent reads restricted project records, creates tickets, and modifies workflow states. The enterprise must know which deployment is executing, which operator is responsible, which data-access capabilities are authorized, whether required assurance remains valid, and which actions were taken.

This use case requires typed relationships, deployment identity, structured capabilities, operational status, assurance, and execution receipts.

## 4.3 Procurement Agent with Bounded Spending Authority

A principal delegates to an agent the ability to prepare and submit purchases from approved suppliers. The delegation includes a per-transaction ceiling, an aggregate ceiling, a geographic scope, an expiry, prohibited related-party transactions, and a requirement for human approval above a threshold.

The agent later delegates only the supplier-validation step to a subordinate agent. The subordinate agent must not inherit submission authority or spending limits that are irrelevant to its task.

This use case requires authority envelopes, delegation narrowing, approval conditions, quantitative limits, downstream lineage, decision receipts, and cascade revocation.

## 4.4 Healthcare Data-Access Agent

An agent coordinates patient scheduling and retrieves limited clinical information. The agent may access data only for a declared care purpose and only through a deployment operating in an approved region. It may not make clinical decisions or expose records to a general-purpose subordinate agent.

This use case requires purpose limitation, data classification, jurisdiction and deployment constraints, explicit prohibitions, privacy-preserving status and authorization proofs, and evidence access controls.

## 4.5 Public-Service Eligibility Agent

An agent assists with public-benefit eligibility. Its output may materially affect access to an essential service. The governing institution requires independent assurance, explainable policy versions, human escalation, point-in-time reconstruction, appeal, correction, and continuity arrangements when the agent is suspended.

This use case requires the High-Assurance or Fiduciary profile. It demonstrates that redress and service continuity are part of system correctness rather than external administrative concerns.

## 4.6 Financial or Fiduciary Agent

An agent acts under duties to a principal or beneficiary. Its technical capability includes transfers, but its current authority permits only portfolio analysis and preparation of instructions. An interface that treats capability as permission could produce unauthorized movement of assets.

This use case requires strict separation of declared, verified, and authorized capabilities; explicit beneficiary and duty metadata; prohibited actions; and a strong enforcement boundary.

## 4.7 Change of Operator

An agent is transferred from one operator to another while retaining its persistent identifier. Existing assurance was based partly on the former operator's controls, and several principals have active delegations.

The registry must not silently carry all relationships forward. Each assurance claim and delegation must state whether it terminates, remains valid, enters review, or requires reissuance or novation.

## 4.8 Compromised Runtime

An agent's core registration remains valid, but a deployment key is compromised. The security authority quarantines the deployment, while another approved deployment remains available.

This use case demonstrates why registration, operational, security, authority, and assurance status are multidimensional and why restrictions may apply to a deployment rather than the entire logical agent.

## 4.9 Stale Projection

A discovery index reports an agent as active, but the authoritative status service suspended it two minutes earlier. A low-risk search result may tolerate the delay; a financial action may not.

This use case requires source provenance, projection lag, relying-party freshness policy, authoritative fallback, and `indeterminate` outcomes when current status cannot be established.

## 4.10 Conflicting Federation Status

One recognized registry reports an agent as active, while another reports it as suspended for the relevant jurisdiction. The local relying policy must determine precedence or return an indeterminate decision. Technical ability to read both records does not itself resolve institutional conflict.

## 4.11 Emergency Suspension, Appeal, and Restoration

A governance authority imposes an emergency suspension after a credible incident report. The operator contests the attribution. The registry preserves the suspension event, records the appeal, supports investigation, and later restores a restricted status after remediation.

This use case requires rapid containment, due process, historical preservation, structured reasons, restoration semantics, and subscriber notification.

## 4.12 End-to-End Delegated Action Flow

The common successful path is:

```text
1. Discover candidate agent
2. Resolve identity, version, deployment, and relationships
3. Verify registry and governance recognition
4. Resolve assurance and current multidimensional status
5. Resolve authority envelope and delegation lineage
6. Evaluate action-specific scope, limits, prohibitions, and approvals
7. Obtain required approvals
8. Issue a short-lived decision receipt
9. Enforce the decision at the execution boundary
10. Produce an execution receipt and supporting evidence
11. Publish material events and retain evidence for audit or redress
```

A conforming implementation MAY combine steps, but it MUST preserve the semantic distinctions and evidence required by its declared profile.

---

# 5. Requirements and Failure Modes

## 5.1 Requirement Matrix

| Requirement | Failure Mode Prevented | Required Profiles |
| --- | --- | --- |
| Separate identity from authority | Registration or ownership is mistaken for permission | All |
| Persistent, non-reassignable identifiers | Historical acts become unattributable | All |
| Typed relationships | Developer, operator, controller, principal, and accountable entity collapse into one field | All, progressively stronger |
| Version and deployment binding | Assurance or authorization is applied to a materially different runtime | B-D |
| Authority envelopes | Delegated permission remains implicit, overbroad, or non-verifiable | C-D |
| Delegation narrowing | A subordinate agent expands authority | C-D |
| Multidimensional status | An active registration hides compromise, expiry, or operational restriction | B-D |
| Point-in-time resolution | A dispute cannot reconstruct state at execution time | B-D |
| Status freshness metadata | A relying party accepts stale suspension or revocation information | All |
| Decision and execution receipts | Authorization and execution cannot be reconstructed | B-D |
| Revocation propagation | Runtime access and subordinate authority survive registry revocation | C-D |
| Explicit recognition | Technical federation creates accidental transitive trust | Federated deployments |
| Contestability and redress | Erroneous or abusive registry action cannot be repaired | B-D |
| Privacy by resolution | Public registries expose principals, beneficiaries, or confidential delegation terms | All |

## 5.2 Functional Requirements

A conforming registry MUST provide authoritative resolution of agent identity and lifecycle status. Higher profiles MUST additionally provide structured relationships, versions, deployments, assurance, authority, evidence, and redress as defined later in this document.

The registry MUST distinguish statements that are self-declared from statements independently verified or issued by an authorized third party. A query response MUST permit a relying party to identify the issuer and scope of each material claim.

## 5.3 Interoperability Requirements

Interoperability has at least five dimensions:

1. **Syntactic interoperability:** systems can parse exchanged records.
2. **Semantic interoperability:** systems interpret fields and states consistently.
3. **Cryptographic interoperability:** systems can verify proofs and key bindings.
4. **Governance interoperability:** systems know whose records and decisions are recognized.
5. **Operational interoperability:** systems can meet freshness, event, revocation, and availability expectations.

A deployment claiming federation support MUST publish an interoperability declaration covering all five dimensions. Exchanging valid JSON is not sufficient evidence of registry interoperability.

## 5.4 Reviewability Requirements

A circulation-ready registry profile SHOULD document:

- its threat model;
- authoritative sources and derived projections;
- role separation;
- lifecycle state semantics;
- processing precedence;
- failure behavior;
- freshness targets;
- revocation propagation targets;
- appeal and redress procedures;
- privacy disclosures; and
- known limitations.

## 5.5 Fail-Closed and Fail-Open Behavior

Each profile and deployment MUST declare which operations fail closed, fail open, or enter an indeterminate state when required information is unavailable.

High-risk authority decisions SHOULD fail closed when current authority, security status, or required assurance cannot be established. Discovery and low-risk informational use MAY continue with warnings when policy permits.

An implementation MUST NOT convert missing evidence into an affirmative decision merely to preserve availability.

---

# 6. Design Principles

## 6.1 Identity Is Not Authority

A valid agent identifier MUST NOT be treated as authorization to perform an action.

## 6.2 Key Control Is Not Accountability

Proof of control over a key establishes possession or control of that key. It does not by itself establish legal responsibility, legitimacy, fitness, institutional authority, or fiduciary obligation.

## 6.3 Capability Is Not Permission

An agent’s technical ability, declared capability, verified competence, and delegated permission MUST be modeled as separate concepts.

## 6.4 Authority Is Contextual

Authority MUST be evaluated against the relevant principal, action, resource, purpose, time, jurisdiction, limits, prohibitions, approvals, and delegation chain.

## 6.5 Delegation Is Not Ownership

Transfer of an agent identifier, software artifact, or registry record MUST NOT silently transfer outstanding delegations.

## 6.6 Revocation Must Reach Enforcement Surfaces

Registry status changes MUST be capable of propagating to operational enforcement systems. A registry status flag without a defined enforcement path is insufficient for high-assurance use.

## 6.7 Assurance Is Bound to What Was Evaluated

Assurance MUST be bound to the relevant agent version, artifact, deployment profile, policy bundle, and evaluation scope.

## 6.8 Consequential Action Must Be Reconstructable

For actions within a conformance profile that requires evidence, the system MUST support reconstruction of the identity, authority, policy, approvals, evidence, and outcome that applied at the time of execution.

## 6.9 Registry Decisions Must Be Contestable

A conforming registry MUST provide governed mechanisms to correct, appeal, suspend, restore, and annotate registry decisions.

## 6.10 Derived State Must Disclose Freshness

Indexes, caches, replicas, and aggregators MUST communicate source provenance and freshness.

## 6.11 Federation Must Be Explicit

Trust or recognition between registries, authorities, assurance providers, and governance frameworks MUST be explicitly represented. It MUST NOT be inferred solely from technical interoperability.

## 6.12 Privacy by Resolution

A registry SHOULD reveal only the minimum information required for a relying decision. Confidential evidence and delegation terms SHOULD be resolved through authorized access or selective disclosure rather than broad publication.

---

# 7. Terminology

## 7.1 Agent

A software-based actor capable of receiving inputs, evaluating state, invoking capabilities, producing outputs, or initiating actions with some degree of operational independence.

## 7.2 Agent Identifier

A persistent identifier assigned to a logical agent record.

## 7.3 Agent Version

A distinguishable release or revision of an agent’s software, model configuration, policy bundle, or declared behavior.

## 7.4 Agent Deployment

A specific operational instantiation of an agent version in an execution environment.

## 7.5 Runtime Identity

A cryptographically verifiable identity associated with a currently executing workload or deployment.

## 7.6 Principal

A person, organization, service, institution, or agent that delegates authority to another agent.

## 7.7 Beneficiary

A person, organization, community, or other subject for whose benefit an action is intended.

## 7.8 Developer

The entity that creates or materially develops the agent software or model integration.

## 7.9 Publisher

The entity that releases an identifiable agent artifact or version.

## 7.10 Deployer

The entity that instantiates an agent version in an operational environment.

## 7.11 Operator

The entity responsible for day-to-day operation of an agent deployment.

## 7.12 Controller

An entity authorized to alter configuration, keys, endpoints, permissions, models, tools, or runtime behavior.

## 7.13 Sponsor

An entity that introduces, endorses, or vouches for an agent within an ecosystem.

## 7.14 Accountable Entity

An entity that accepts defined responsibility for specified actions, harms, obligations, or remediation associated with an agent.

## 7.15 Governance Authority

An entity that defines admission, participation, suspension, revocation, recognition, appeal, or redress rules for a registry or ecosystem.

## 7.16 Assurance Provider

An entity that evaluates an agent, artifact, deployment, process, or control environment and issues an assurance claim.

## 7.17 Delegation

A grant of bounded authority from a principal to an agent.

## 7.18 Authority Envelope

A machine-readable record describing the scope, limits, conditions, approvals, validity, and revocation semantics of a delegation.

## 7.19 Capability Declaration

A statement describing what an agent claims to be technically capable of doing.

## 7.20 Capability Verification

Evidence that an agent demonstrated a capability under specified test conditions.

## 7.21 Capability Authorization

A policy or delegation statement permitting an agent to exercise a capability in a defined context.

## 7.22 Assurance Claim

A signed statement that specified controls, criteria, or tests were evaluated against a defined subject and scope.

## 7.23 Registration Status

The administrative lifecycle state of the agent record.

## 7.24 Operational Status

The current availability or permitted operating mode of an agent deployment.

## 7.25 Security Status

The current security condition of an agent, version, deployment, or key set.

## 7.26 Authority Status

The validity state of a delegation or authority envelope.

## 7.27 Execution Receipt

A signed or otherwise tamper-evident record of a completed or attempted action.

## 7.28 Decision Receipt

A signed or otherwise tamper-evident record of an authority or policy evaluation.

## 7.29 Relying Party

An entity that consumes registry data or evidence to decide whether to interact with, authorize, accept, or rely upon an agent.

## 7.30 Recognition

An explicit rule under which one registry or governance domain accepts specified records, issuers, statuses, profiles, or decisions from another domain.

## 7.31 Source of Truth

The authoritative system or record from which a registry state is derived.

## 7.32 Projection

A searchable, indexed, cached, or aggregated representation derived from authoritative records.

---

# 8. Architectural Overview

## 8.1 Registry as a Distributed Control Plane

The term “registry” in this specification refers to a logical system, not necessarily a single database, contract, or administrative organization. A conforming registry may comprise authoritative record stores, status services, indexes, policy decision services, evidence custodians, event streams, governance authorities, and enforcement integrations.

The architecture is distributed because identity, delegation, assurance, operational status, governance, and evidence may have different legitimate issuers and storage requirements. It is an authority-control plane because its primary function is to make the conditions and boundaries of delegated action resolvable and enforceable.

## 8.2 Reference Architecture

```text
                         GOVERNANCE AUTHORITIES
                    Policy | Recognition | Appeal
                                  |
                                  v
+------------------------------------------------------------------+
|                 AUTHORITATIVE REGISTRY SERVICES                  |
| Identity | Relationships | Versions | Deployments | Delegations  |
| Assurance | Status | Recognition | Governance | Redress         |
+------------------------------------------------------------------+
                 |                         |
                 v                         v
+--------------------------------+  +-------------------------------+
| QUERY AND DECISION PLANE       |  | EVENT AND SUBSCRIPTION PLANE  |
| Resolution | Discovery | PDP   |  | Status | Revocation | Incident|
| Point-in-time | Reliance       |  | Replay | Acknowledgement       |
+--------------------------------+  +-------------------------------+
                 |                         |
                 +------------+------------+
                              v
+------------------------------------------------------------------+
|                      RUNTIME ENFORCEMENT                          |
| Workload identity | Capability gateway | PEP | Key/session control|
| Human approval | Sub-agent delegation gate | Emergency containment|
+------------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------------+
|                    EVIDENCE AND ACCOUNTABILITY                    |
| Decision receipts | Execution receipts | Audit | Incident | Redress|
+------------------------------------------------------------------+
```

## 8.3 Core Record Graph

```text
Agent Core Record
 ├── Version Record
 │    ├── Artifact and policy digests
 │    ├── Capability declarations
 │    └── Assurance claims
 ├── Deployment Record
 │    ├── Runtime identity
 │    ├── Service endpoints
 │    └── Operational and security status
 ├── Relationship Records
 │    ├── Developer / publisher
 │    ├── Operator / controller
 │    ├── Accountable entity
 │    └── Governance authority
 ├── Authority Envelopes
 │    └── Delegation lineage
 ├── Decision and Execution Receipts
 └── Lifecycle, incident, appeal, and recognition events
```

## 8.4 Deployment Independence

This specification does not require all data to be co-located. A public identifier record may resolve to a protected authority record, a content-addressed description, an external assurance claim, and a confidential evidence store. The resolver is responsible for presenting enough provenance, status, and access information to support a policy decision.

## 8.5 Normative Boundary

A deployment conforms through observable protocol behavior, record semantics, processing rules, security properties, and declared profile support. It does not conform merely because it uses a particular database, ledger, credential technology, or agent-description format.

---

# 9. Trust and Authority Boundaries

## 9.1 General Model

No component in this architecture is universally trusted. Each actor is trusted only for claims within its authority and declared scope.

| Component or Role | Relied Upon For | Not Relied Upon For |
| --- | --- | --- |
| Registry Operator | Publication and availability of registry state | Truth of every third-party claim |
| Registration Authority | Admission and identifier issuance under its policy | Agent capability or action authorization |
| Identifier Controller | Authorized updates within its control scope | Universal accountability |
| Delegation Issuer | Authority that the issuer is competent to grant | Authority beyond the issuer's own scope |
| Assurance Provider | Evaluation against declared controls and scope | Permission for a particular action |
| Governance Authority | Decisions within its governance domain | Recognition outside that domain |
| Index Operator | Search and projection | Final authoritative status |
| Policy Decision Point | Evaluation under a named policy version | Enforcement of the resulting decision |
| Policy Enforcement Point | Prevention or permission of execution | Truth of registry claims not independently verified |
| Runtime | Execution and receipt production | Self-asserted assurance or unconstrained authority |
| Relying Party | Local reliance policy and final acceptance decision | Modification of authoritative registry state |

## 9.2 Issuer Competence

A record is not acceptable solely because its proof verifies. The relying party MUST also determine whether the issuer was authorized or recognized to issue that record type for the relevant subject and scope.

For example, an operator may be permitted to update a service endpoint but not to name a new accountable entity. An assurance provider may issue a control-evaluation claim but not a delegation. A principal may delegate only authority it possesses.

## 9.3 Trust Chains and Authority Chains

Cryptographic verification chains and authority chains are related but distinct. A proof chain establishes the integrity and origin of records. An authority chain establishes that each delegation was within the delegator's competence and that scope narrowed appropriately.

Implementations MUST validate both where applicable.

## 9.4 Projection Boundary

Indexes and caches are untrusted for finality unless the relying policy explicitly accepts their freshness and proof model. A projection MAY support discovery, but consequential decisions MUST satisfy the profile's authoritative status requirements.

## 9.5 Enforcement Boundary

A registry record does not itself prevent execution. The Policy Enforcement Point is responsible for applying decisions to keys, sessions, APIs, tools, data, or transaction channels. High-assurance claims about revocation MUST include evidence of propagation or a disclosed maximum propagation interval.

## 9.6 Governance Boundary

Technical interoperability does not establish recognition. A relying domain decides which governance authorities, assurance providers, registries, and status decisions it accepts. Recognition MUST be represented explicitly and evaluated as part of reliance.

---

# 10. Logical Planes

## 10.1 Logical Planes

A conforming implementation MUST support the following logical planes, whether implemented as separate services or integrated components:

1. **Identity and Continuity Plane**
2. **Control and Accountability Plane**
3. **Delegation and Authority Plane**
4. **Capability and Assurance Plane**
5. **Operational State and Evidence Plane**
6. **Governance, Contestability, and Redress Plane**
7. **Query and Decision Plane**
8. **Event and Subscription Plane**

## 10.2 Separation of Concerns

Implementations MUST NOT use a single undifferentiated “owner” field as the exclusive representation of all relationships.

Implementations MUST distinguish at minimum:

- agent identity;
- current controller;
- current operator;
- accountable entity;
- principal;
- delegation;
- assurance provider; and
- governance authority.

## 10.3 Authoritative and Derived Data

An implementation MAY maintain different systems for authoritative state, discovery indexes, evidence storage, and operational telemetry.

Every query response derived from non-authoritative data MUST include sufficient provenance to identify:

- the authoritative source;
- the source version, sequence, checkpoint, or transaction;
- the projection update time;
- known lag or staleness; and
- the response generation time.

## 10.4 Public and Confidential Data

The architecture MUST support both public and access-controlled records.

The registry MUST NOT require publication of confidential delegation terms, personal data, proprietary model details, sensitive operational telemetry, or protected evidence.

Where data is withheld, the registry SHOULD publish:

- a stable reference;
- the record type;
- the issuer or authoritative source;
- the current status;
- a digest or commitment where appropriate;
- the access protocol;
- the disclosure policy; and
- sufficient metadata for policy evaluation.

---

# 11. Roles and Responsibilities

A conforming registry deployment MAY combine roles, but role boundaries MUST remain explicit.

## 11.1 Registration Authority

Validates registration requests and creates agent identifiers.

## 11.2 Registry Operator

Operates the authoritative registry services.

## 11.3 Governance Authority

Defines policy and adjudicates participation or enforcement decisions.

## 11.4 Identifier Controller

Controls updates to the core agent record.

## 11.5 Delegation Issuer

Creates authority envelopes.

## 11.6 Assurance Issuer

Creates assurance claims.

## 11.7 Status Authority

Publishes lifecycle, operational, security, or authority status.

## 11.8 Index Operator

Operates a projection or search service.

## 11.9 Evidence Custodian

Stores execution evidence, audit artifacts, or confidential supporting materials.

## 11.10 Resolver

Accepts identifier, status, authority, or reliance queries and returns structured responses.

## 11.11 Policy Decision Point

Evaluates a request against policy, authority, status, assurance, and contextual data.

## 11.12 Policy Enforcement Point

Prevents or permits execution based on a decision.

## 11.13 Appeal Authority

Accepts and adjudicates challenges, corrections, suspensions, or revocation appeals.

---

# 12. Identifier and Namespace Model

## 12.1 Agent Identifier Properties

An agent identifier MUST be:

- globally or federation-wide unique within its declared namespace;
- persistent across routine key rotation;
- resolvable to a current record or an explicit terminal status;
- non-reassignable after retirement or revocation;
- capable of representing lineage; and
- independent of a single network endpoint.

## 12.2 Identifier Syntax

This specification defines the generic URI scheme:

```text
agentreg:<registry-namespace>:<agent-local-id>
```

Example:

```text
agentreg:example.org:8f2b7b4a-6c2d-4ee5-94ac-5a3f6a95d314
```

The scheme is defined by the following ABNF ([RFC 5234](https://www.rfc-editor.org/rfc/rfc5234)):

```abnf
agent-identifier  = "agentreg:" registry-namespace ":" agent-local-id
registry-namespace = 1*253( ALPHA / DIGIT / "-" / "." )
agent-local-id      = 1*255( ALPHA / DIGIT / "-" / "_" / "." / ":" )
ALPHA               = %x41-5A / %x61-7A
DIGIT               = %x30-39
```

`registry-namespace` SHOULD be a DNS domain name or an equivalent registry-assigned namespace under the issuing Registration Authority's policy. `agent-local-id` MUST be unique within `registry-namespace` and MUST NOT be reassigned after retirement or revocation (§12.1). Implementations MAY support other identifier schemes. A conformance profile MUST declare supported identifier schemes. Registration of `agentreg` as a permanent URI scheme is an Open Issue (§40.1) and IANA Consideration (§41); until registered, the scheme MUST be treated as provisional and MUST NOT be assumed collision-free with any future IANA-registered scheme of the same name.

## 12.3 Version Identifier

Each materially distinct agent version MUST have a version identifier.

A version identifier SHOULD include or resolve to:

- semantic version;
- artifact digest;
- release timestamp;
- policy bundle identifier;
- model or model-family constraints, when applicable; and
- predecessor version.

## 12.4 Deployment Identifier

Each deployment in an accountable or higher conformance profile MUST have a unique deployment identifier.

## 12.5 Runtime Identifier

High-assurance deployments MUST support runtime identities capable of being cryptographically bound to workload attestations or equivalent integrity evidence.

## 12.6 Identifier Resolution

Resolution MUST return one of:

- `active_record`;
- `terminal_record`;
- `redirect_to_successor`;
- `not_found`;
- `not_authorized`;
- `temporarily_unavailable`; or
- `indeterminate`.

A registry MUST NOT return `not_found` for a known retired, revoked, burned, or superseded identifier.

---



## ARPA-CAND-PP-01 §1 — ARPA Agent Identifier

<!-- consolidated-source: ARPA-CAND-PP-01 §1 -->

The protocol Agent Identifier used for ARPA Core interchange MUST use the `agentreg:` URI scheme defined by ARPA v0.9.0 §12.2:

```text
agentreg:<registry-namespace>:<agent-local-id>
```

An implementation MUST NOT emit a non-`agentreg:` URI as the ARPA Agent Identifier merely because that URI identifies the same agent in another identity or discovery system.

External identifiers, DIDs, HTTPS identifiers, platform identifiers or other aliases MAY be represented as alternate identifiers or mappings, but they MUST remain distinguishable from the ARPA Agent Identifier.

A resolver that receives a syntactically valid URI using an unsupported identifier scheme MUST NOT silently reinterpret it as an ARPA Agent Identifier. It MAY resolve the identifier through an explicitly configured mapping mechanism, provided that the returned ARPA record preserves the resulting `agentreg:` identifier and the mapping provenance.

Registries MUST NOT silently reassign an `agentreg:` identifier to a different logical agent.


# 13. Record and Relationship Model

## 13.1 Record Envelope

Every record defined by this specification MUST use a common envelope.

```json
{
  "record_id": "string",
  "record_type": "string",
  "schema_version": "string",
  "issuer": "string",
  "subject": "string or object",
  "issued_at": "date-time",
  "effective_from": "date-time",
  "effective_until": "date-time or null",
  "status": "string",
  "supersedes": ["record_id"],
  "evidence": ["reference"],
  "governance": ["reference"],
  "proof": {
    "type": "string",
    "verification_method": "string",
    "created": "date-time",
    "value": "string"
  }
}
```

## 13.2 Canonicalization

A conforming implementation MUST define a deterministic serialization or canonicalization method for records that are signed, hashed, or committed.

Unless a conformance profile declares an alternative, implementations MUST use [JSON Canonicalization Scheme (JCS), RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) as the default canonicalization method for JSON-encoded records prior to hashing or signing. A profile MAY declare an alternative canonicalization method (for example, a CBOR deterministic encoding under [RFC 8949](https://www.rfc-editor.org/rfc/rfc8949) §4.2, or a JSON-LD/RDF dataset canonicalization) provided the method is deterministic, is identified in the record's `proof.type`, and is declared in the profile's conformance statement (§35.5).

## 13.3 Agent Core Record

The Agent Core Record MUST include:

- agent identifier;
- human-readable name or label;
- agent class;
- current registration status;
- current canonical version;
- current controller relationships;
- current operator relationships;
- accountable entity relationships;
- canonical description reference;
- service endpoint references;
- key references;
- lineage references;
- governance framework references;
- status endpoints;
- created time;
- last material update time; and
- authoritative source metadata.

Example:

```json
{
  "record_type": "agent_core",
  "agent_id": "agentreg:example.org:agent-123",
  "name": "Procurement Review Agent",
  "agent_class": "delegated_transactional_agent",
  "registration_status": "active",
  "current_version": "agent-version-2.4.1",
  "controllers": ["relationship-controller-1"],
  "operators": ["relationship-operator-1"],
  "accountable_entities": ["relationship-accountable-1"],
  "description": "https://registry.example.org/agents/agent-123/card",
  "service_endpoints": ["endpoint-1", "endpoint-2"],
  "keys": ["key-binding-1", "key-binding-2"],
  "lineage": {
    "predecessors": ["agentreg:example.org:agent-100"],
    "successors": []
  },
  "governance": ["governance-profile-financial-1"],
  "status_endpoints": [
    "https://registry.example.org/agents/agent-123/status"
  ],
  "created_at": "2026-07-15T00:00:00Z",
  "updated_at": "2026-07-15T00:00:00Z"
}
```

## 13.4 Relationship Record

A Relationship Record MUST express:

- subject;
- related entity;
- relationship type;
- scope;
- effective period;
- authority source;
- status;
- revocation semantics; and
- evidence or proof.

Supported base relationship types SHOULD include:

- `developed_by`;
- `published_by`;
- `deployed_by`;
- `operated_by`;
- `controlled_by`;
- `sponsored_by`;
- `accountable_to`;
- `assured_by`;
- `governed_by`;
- `hosted_by`;
- `acts_for`;
- `benefits`;
- `supervises`;
- `delegates_to`; and
- `recognized_by`.

## 13.5 Key Binding Record

A Key Binding Record MUST include:

- agent or deployment identifier;
- key identifier;
- key type;
- intended use;
- controller;
- validity interval;
- rotation or replacement linkage;
- status; and
- proof of control or authorized binding.

Key uses MUST be separated, including where applicable:

- registry administration;
- runtime identity;
- delegation issuance;
- receipt signing;
- payment;
- recovery;
- security suspension; and
- assurance issuance.

## 13.6 Service Endpoint Record

A Service Endpoint Record MUST include:

- endpoint identifier;
- agent or deployment identifier;
- protocol;
- URI;
- purpose;
- authentication requirements;
- region or jurisdiction, where relevant;
- data classification;
- availability status;
- effective period; and
- health or status reference.

## 13.7 Description Record

A Description Record MAY include:

- name;
- description;
- provider information;
- capabilities;
- protocols;
- supported input and output types;
- service endpoints;
- documentation references;
- policy references;
- pricing references;
- privacy notices; and
- user-facing disclosures.

A Description Record MUST NOT be treated as evidence that its claims are true.

## 13.8 Metadata Extensions

Extensions MUST use governed namespaces.

An extension MUST declare:

- namespace;
- schema identifier;
- schema version;
- criticality;
- validation rules; and
- processing semantics.

A relying party MUST reject a record containing an unknown critical extension.

---

# 14. Registry and Enforcement Interaction

## 14.1 Separation of Resolution, Decision, and Enforcement

The registry resolves authoritative records and status. The Policy Decision Point evaluates them against context and policy. The Policy Enforcement Point applies the decision to execution.

These functions MAY be implemented in one product, but their semantics MUST remain distinguishable. A resolver response is not automatically an authorization decision, and an authorization decision is not evidence that enforcement occurred.

## 14.2 Registration Flow

```text
Registration requester
      |
      v
Identifier and namespace validation
      |
      v
Controller and issuer authorization
      |
      v
Core, relationship, version, and deployment records
      |
      v
Governance admission and required assurance
      |
      v
Initial lifecycle state and signed event
```

A registry MUST NOT enter `active` state until the profile's required admission conditions are satisfied.

## 14.3 Delegated Action Flow

```text
Agent presents identity and runtime context
      |
      v
Resolver returns current records and freshness
      |
      v
PDP validates recognition, status, assurance, and delegation
      |
      v
PDP returns decision receipt and conditions
      |
      v
PEP validates receipt freshness and obtains approvals
      |
      v
PEP allows or denies execution
      |
      v
Runtime produces execution receipt
```

The PEP MUST validate that the decision receipt applies to the same agent, deployment, action, resource, and material context presented at execution time.

## 14.4 Revocation Flow

```text
Authorized status authority issues revocation
      |
      v
Authoritative record and event are committed
      |
      v
Caches and projections are invalidated or updated
      |
      v
Enforcement points, key managers, and subscribers are notified
      |
      v
Downstream delegation handling is applied
      |
      v
Acknowledgements and unresolved targets are recorded
```

A delegated-authority profile MUST define which enforcement targets are in scope and the maximum time within which revocation is expected to become effective. Publication of a revocation and expiry of a propagation target do not, by themselves, establish enforcement convergence. A revocation is `published` when the authoritative record and event are committed, `propagating` while applicable enforcement targets remain unacknowledged, and `converged` only when every applicable enforcement target has acknowledged application or has been removed from scope by an authorized governance decision. Unresolved targets MUST remain visible and MUST prevent a `converged` claim.

## 14.5 Appeal and Restoration Flow

```text
Affected party files correction or appeal
      |
      v
Appeal record and applicable interim state are published
      |
      v
Authorized authority reviews evidence
      |
      v
Decision confirms, modifies, or reverses prior action
      |
      v
Restoration or correction event is published
      |
      v
Subscribers and enforcement points update state
```

Restoration MUST NOT erase the historical suspension, revocation, or investigation. It creates a new effective state and preserves the basis for both decisions.

## 14.6 Enforcement Acknowledgement

Where required by profile, an enforcement point MUST emit an acknowledgement identifying:

- the status or authority event applied;
- the affected enforcement surface;
- the time applied;
- any partial failure;
- retry or remediation status; and
- proof or authenticated source.

---



## ARPA-CAND-PP-02 §5 — Separation from authentication and execution

<!-- consolidated-source: ARPA-CAND-PP-02 §5 -->

Authentication establishes control of credentials or a workload identity; it does not by itself establish action-specific delegated authority.

ARPA authority evaluation supplies protocol-visible authority state and evidence for a relying decision. It does not replace the relying party's policy decision unless the ARPA component is explicitly acting as the applicable policy decision authority.

A downstream system MUST NOT execute or accept a material action under a different action context from the one whose authority was evaluated without performing a new authority evaluation or proving equivalence under the applicable policy.


# 15. Agent Registration

## 15.1 Registration Request

A registration request MUST identify the requested namespace, proposed controller, agent class, initial description, governance domain, and proof that the requester is authorized under the applicable registration policy.

## 15.2 Admission Processing

The Registration Authority MUST validate uniqueness, namespace policy, controller authorization, required relationship records, prohibited impersonation, and any profile-specific evidence. It MUST record the policy version used for admission.

## 15.3 Initial State

A newly created identifier SHOULD enter `provisioned` or `pending_assurance`. It MUST NOT enter `active` until all mandatory profile and governance conditions are satisfied.

## 15.4 Registration Evidence

The registration event MUST contain or resolve to the request digest, issuer, controller, governing policy, effective time, initial state, and proof.

## 15.5 Duplicate and Deceptive Registration

Registries MUST define procedures for detecting and resolving duplicate, confusing, or deceptive identifiers and names. Human-readable names MUST NOT be assumed unique.

---

# 16. Version and Deployment Management

## 16.1 Version Record

A Version Record MUST identify the logical agent, version identifier, predecessor, artifact digest, release time, declared capability set, policy bundle, material dependencies, and material-change classification.

## 16.2 Deployment Record

Profiles B through D MUST represent each consequential deployment separately. A Deployment Record MUST identify the agent version, deployer, operator, environment or profile, runtime identity method, service endpoints, jurisdiction, status references, and creation time.

## 16.3 Version-to-Deployment Binding

An operational deployment MUST reference exactly one current agent version at a time. A version transition MUST produce an event and update affected assurance and authority applicability.

## 16.4 Runtime Substitution

A deployment MUST NOT claim the assurance or authority of a registered version if the executing artifact, model configuration, policy bundle, or critical tool set materially differs from the bound version.

## 16.5 Rollback

A rollback to an earlier version MUST be treated as a new deployment transition. The registry MUST reevaluate assurance validity, known vulnerabilities, authority applicability, and policy compatibility.

---

# 17. Relationship Management

## 17.1 Typed Relationships

Relationships MUST be represented as first-class records with issuer, scope, validity, status, and governance basis. A free-text description of a relationship is insufficient for normative processing.

## 17.2 Relationship Authority

The registry MUST define which role may create, modify, or terminate each relationship type. An operator MUST NOT appoint a new accountable entity unless explicitly authorized to do so.

## 17.3 Multiple Relationships

An agent MAY have multiple operators, controllers, principals, beneficiaries, or accountable entities. Each record MUST define scope so that a relying party can determine which relationship applies to the requested action or deployment.

## 17.4 Change and Termination

A relationship change MUST produce an event and trigger impact analysis for linked delegations, assurance claims, deployments, evidence access, and governance recognition.

---

# 18. Delegation and Authority

> **Candidate controls:** ARPA-CAND-001, ARPA-CAND-002, ARPA-CAND-006. Delegation evaluation MUST compute the intersection of all applicable scopes, conditions, prohibitions, validity intervals, and lifecycle states. Circular, expired, suspended, revoked, or unverifiable links MUST NOT yield affirmative authority.

## 18.1 General Requirement

An agent registry supporting consequential action MUST support machine-readable delegation records.

## 18.2 Authority Envelope

An Authority Envelope MUST include:

- authority identifier;
- principal;
- agent;
- issuer;
- action classes;
- resource scope;
- purpose scope;
- jurisdictional scope;
- valid-from and valid-until;
- financial or quantitative limits, where applicable;
- prohibitions;
- required approvals;
- delegation mode;
- downstream delegation limits;
- evidence requirements;
- revocation mechanism;
- status endpoint;
- governance framework;
- redress profile; and
- proof.

## 18.3 Delegation Modes

Supported modes MUST include:

- `non_delegable`;
- `delegable_once`;
- `delegable_within_scope`;
- `delegable_with_explicit_approval`;
- `delegable_to_named_agents`; and
- `delegable_under_governance_profile`.

## 18.4 Delegation Narrowing

A downstream delegation MUST NOT exceed the upstream authority from which it derives.

A conforming authority evaluator MUST verify:

- action subset;
- resource subset;
- purpose subset;
- time subset;
- jurisdiction subset;
- quantitative limits;
- prohibition inheritance;
- approval inheritance;
- assurance requirements;
- delegation depth; and
- revocation status.

## 18.5 Authority Evaluation

An authority evaluation request SHOULD include:

- agent;
- principal;
- action;
- resource;
- purpose;
- amount or quantity;
- jurisdiction;
- current time;
- deployment;
- requested delegation depth;
- assurance context; and
- relying-party policy.

The result MUST be one of:

- `allow`;
- `allow_with_conditions`;
- `deny`;
- `indeterminate`; or
- `not_applicable`.

An `allow_with_conditions` result MUST enumerate all required conditions.

## 18.6 Decision Receipt

Every authority evaluation in accountable or higher profiles MUST produce a Decision Receipt containing:

- request digest;
- decision;
- evaluated authority records;
- evaluated status records;
- evaluated policy version;
- conditions;
- evaluation time;
- validity duration;
- evaluator identity;
- freshness metadata;
- proof; and
- reason codes.

## 18.7 Revocation

Authority revocation MUST specify:

- revoked authority;
- effective time;
- issuer;
- reason;
- scope;
- downstream propagation behavior;
- historical effect;
- enforcement targets;
- required acknowledgements; and
- appeal route.

## 18.8 Cascade Revocation

Where an authority has been delegated further, the system MUST define whether revocation:

- cascades automatically;
- causes downstream suspension pending evaluation;
- affects only new actions;
- affects uncompleted actions;
- affects prior receipts; or
- requires compensating action.

## 18.9 Runtime Enforcement

Delegated authority profiles MUST define integration with policy enforcement points.

A registry MUST distinguish revocation publication, propagation, and enforcement convergence.

A registry MUST NOT claim `converged` revocation unless every applicable enforcement target has emitted an authenticated acknowledgement that the revocation was applied, or an authorized governance decision has explicitly removed that target from scope. A maximum revocation propagation time is an operational objective and MUST NOT be used as evidence of convergence.

If the propagation target expires before convergence, the registry MUST expose a non-converged state, identify unresolved enforcement targets, and apply the profile's fail-safe behavior.

---



## ARPA-HARDENING §1 — Monotonic delegation and scope intersection

<!-- consolidated-source: ARPA-HARDENING §1 -->

The effective authority of a downstream delegation MUST be the semantic intersection of the issuer's effective authority and the downstream delegation's declared scope.

For every constrained dimension, a downstream value MUST be proven to denote a semantic subset of the corresponding effective upstream value. The dimensions include, as applicable, action, resource, purpose, jurisdiction, time, quantitative limits, approvals, prohibitions, assurance requirements, subject constraints, deployment constraints, and delegation depth.

Omission of an upstream constraint MUST NOT remove, reset, wildcard, or otherwise broaden that constraint. A downstream delegation that omits a constrained dimension inherits the effective upstream constraint unchanged.

A prohibition MUST be inherited unless the competent upstream authority explicitly defines a narrower prohibition-removal mechanism and the governing profile permits it. A downstream delegation MUST NOT remove a mandatory prohibition merely by omitting it.

Where two scope expressions use different vocabularies, taxonomies, jurisdiction models, resource grammars, or policy languages, the evaluator MUST establish a governed subset relation before treating the downstream expression as narrower. If the subset relation cannot be established, the result MUST be `deny` or `indeterminate`; it MUST NOT be `allow` or `allow_with_conditions`.

The effective delegation operation is therefore:

```text
effective_authority(child) = effective_authority(parent) ∩ child_declared_scope
```

and the intersection MUST be computed monotonically across the complete delegation lineage.



## ARPA-CAND-PP-02 §4 — Collective-principal authority

<!-- consolidated-source: ARPA-CAND-PP-02 §4 -->

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



## ARPA-CAND-PP-03 §4 — Collective-principal snapshot semantics

<!-- consolidated-source: ARPA-CAND-PP-03 §4 -->

A threshold, quorum, role or other collective-principal evaluation MUST bind the decision to one stated membership/controller and exercise-rule snapshot, identified by a stable snapshot/checkpoint identifier or equivalent digest.

Each approval counted toward the collective rule MUST be valid under that same snapshot unless the governing rule explicitly permits cross-snapshot composition and the evidence proves the permitted transition.

Approvals collected across membership removal/re-addition, role change, rule change or stale membership MUST NOT be combined by default.

Decision evidence MUST retain the snapshot/checkpoint identifier used to evaluate membership and the exercise rule.



## ARPA-CAND-PP-03 §5 — Parent authority linkage

<!-- consolidated-source: ARPA-CAND-PP-03 §5 -->

A delegated Authority Envelope MUST identify the parent authority statement from which its delegated scope derives using `derives_from`.

`derives_from` is optional for a root authority grant and REQUIRED by Candidate semantics whenever the envelope represents delegated authority derived from an upstream authority statement. Implementations MUST NOT invent a second competing parent-link field.

**Compatibility classification:** additive for root grants; conditionally required for delegated envelopes. Existing delegated records that lack an unambiguous parent reference require migration before claiming PP-03 conformance.


# 19. Capability and Assurance

## 19.1 Capability Types

The registry MUST distinguish:

1. capability declaration;
2. capability verification;
3. capability authorization;
4. capability invocation;
5. capability outcome.

## 19.2 Capability Declaration

A declaration SHOULD include:

- capability identifier;
- vocabulary or taxonomy;
- version;
- input types;
- output types;
- preconditions;
- side effects;
- risk classification;
- required permissions;
- supported protocols; and
- claimed limitations.

## 19.3 Capability Verification

A verification record MUST include:

- tested subject;
- tested version;
- tested deployment profile;
- test method;
- test environment;
- evaluator;
- result;
- limitations;
- evidence reference;
- validity period; and
- proof.

## 19.4 Capability Authorization

Capability authorization MUST be represented through authority or policy records, not solely through the description record.

## 19.5 Risk Classification

Registries SHOULD classify capabilities by risk, such as:

- informational;
- advisory;
- data-accessing;
- workflow-modifying;
- transaction-preparing;
- transaction-submitting;
- asset-controlling;
- identity-affecting;
- rights-affecting;
- safety-critical; and
- irreversible.

Higher-risk classes SHOULD trigger stronger conformance requirements.

## 19.6 Capability Drift

A material change to capabilities MUST trigger:

- a new agent version;
- assurance review;
- policy reevaluation;
- updated disclosure;
- updated authorization analysis; and
- relying-party notification where required.

---

## 19.7 Assurance Object

An Assurance Claim MUST include:

- assurance identifier;
- subject;
- subject version;
- artifact digest;
- deployment scope;
- assurance profile;
- evaluated controls;
- evidence references;
- assessor;
- issue time;
- validity period;
- status;
- limitations;
- excluded capabilities;
- re-evaluation triggers; and
- proof.

## 19.8 Assurance Profiles

A registry MAY support multiple assurance profiles.

Each profile MUST define:

- target risk class;
- required controls;
- evaluation method;
- evidence requirements;
- assessor qualification;
- validity duration;
- monitoring requirements;
- incident obligations;
- suspension rules; and
- renewal rules.

## 19.9 Binding Requirements

An assurance claim MUST be bound to all material elements that were evaluated, including as applicable:

- software artifact;
- model identifier or family;
- model configuration;
- policy bundle;
- tools;
- execution environment;
- deployment profile;
- data-processing region;
- key set;
- monitoring configuration; and
- version.

## 19.10 Material Change

A profile MUST define material change.

Examples SHOULD include:

- new model family;
- material model update;
- new high-risk capability;
- change of operator;
- change of accountable entity;
- new external tool;
- new data jurisdiction;
- security-control reduction;
- policy-bundle replacement;
- key compromise; or
- architecture change affecting isolation or authorization.

## 19.11 Assurance Status

Supported assurance states MUST include:

- `valid`;
- `conditional`;
- `expired`;
- `suspended`;
- `revoked`;
- `superseded`; and
- `indeterminate`.

## 19.12 No Universal Trust Flag

A registry MUST NOT reduce assurance to a universal boolean “trusted” field.

---

# 20. Lifecycle and Status

> **Candidate controls:** ARPA-CAND-005, ARPA-CAND-006, and ARPA-CAND-012. Lifecycle state is time-dependent. Implementations MUST preserve effective timestamps and MUST distinguish registry publication of a state change from enforcement convergence.

## 20.1 Registration States

A conforming registry MUST support at least:

- `provisioned`;
- `pending_assurance`;
- `active`;
- `restricted`;
- `suspended`;
- `quarantined`;
- `compromised`;
- `revoked`;
- `retired`;
- `superseded`; and
- `under_investigation`.

## 20.2 State Semantics

### provisioned

An identifier exists, but the agent is not yet eligible for ordinary reliance.

### pending_assurance

Required evaluation or approval is incomplete.

### active

The agent is eligible for interaction subject to authority, assurance, and local policy.

### restricted

The agent may operate only within specified reduced scope.

### suspended

New activity is prohibited or limited pending review, repair, or restoration.

### quarantined

The agent or deployment is isolated due to elevated security or integrity concerns.

### compromised

A material compromise has been confirmed or is treated as confirmed.

### revoked

The registry has terminated recognition or eligibility under the relevant governance framework.

### retired

The agent has ceased operation through an orderly process.

### superseded

A successor agent or version has replaced the current subject.

### under_investigation

A formal review is active. This status alone MUST NOT imply guilt or compromise.

## 20.3 Transition Requirements

Every material lifecycle transition MUST record:

- prior state;
- new state;
- effective time;
- issuing authority;
- reason code;
- governance basis;
- affected scope;
- whether historical actions are affected;
- whether appeal is available;
- whether downstream notifications were emitted; and
- whether enforcement acknowledgement is required.

For a transition that may affect interpretation of earlier state, the event MUST classify its historical effect as one of `none`, `prospective`, `retroactive`, `governance_defined`, or `indeterminate`. A registry MUST NOT infer retroactive effect solely from a current `revoked`, `compromised`, `retired`, `superseded`, or withdrawn state. Retroactive effect requires an applicable governance rule or authoritative event declaration.

Transition legality is governed by `registries/lifecycle-transitions.json`. A conforming implementation MUST reject a lifecycle transition that is absent from that registry or whose declared preconditions are not satisfied. `revoked`, `retired`, and `superseded` are terminal for ordinary administrative processing; any exceptional reversal MUST use a transition explicitly marked `governance_reversal`, identify the competent authority and governance basis, preserve the prior terminal event, and produce a new restoration or correction event. Implementations MUST NOT recreate historical continuity by deleting or rewriting the prior transition.

## 20.4 Transfer and Change of Control

A change in controller, operator, accountable entity, or ownership-like relationship MUST NOT automatically transfer:

- delegations;
- assurance claims;
- runtime credentials;
- payment bindings;
- confidential evidence access;
- downstream authority;
- sponsor endorsements; or
- governance recognition.

Each affected record MUST define whether it:

- terminates;
- remains valid;
- requires novation;
- requires reissuance;
- enters review; or
- becomes restricted.

## 20.5 Retirement

Retirement MUST preserve:

- historical identifier resolution;
- status history;
- lineage;
- prior assurance references;
- prior delegation references, subject to privacy;
- execution evidence references; and
- redress routes.

## 20.6 Supersession

A superseded agent MUST resolve to:

- its historical record;
- the successor reference;
- the effective supersession time;
- the migration policy;
- authority transition rules; and
- whether previous delegation remains valid.

---

## 20.7 Multi-Dimensional Status

A status response MUST distinguish at minimum:

- registration status;
- operational status;
- authority status;
- assurance status;
- security status.

## 20.8 Operational States

Supported operational states SHOULD include:

- `available`;
- `degraded`;
- `restricted`;
- `maintenance`;
- `offline`;
- `draining`;
- `quarantined`; and
- `unknown`.

## 20.9 Security States

Supported security states SHOULD include:

- `normal`;
- `elevated_monitoring`;
- `suspected_compromise`;
- `confirmed_compromise`;
- `containment_in_progress`;
- `recovery_in_progress`;
- `under_investigation`; and
- `unknown`.

## 20.10 Runtime Attestation

High-assurance profiles MUST support evidence that the currently executing workload corresponds to the registered deployment or an approved equivalent.

## 20.11 Freshness

Operational and security status responses MUST include:

- observed_at;
- issued_at;
- valid_until or maximum age;
- source;
- confidence or authority level; and
- evidence reference.

## 20.12 Emergency Suspension

A conforming registry SHOULD support a rapid emergency suspension process distinct from final revocation.

Emergency suspension SHOULD:

- take effect quickly;
- support narrow scope;
- preserve due process;
- require post-action review;
- support restoration;
- produce signed events; and
- notify enforcement points.

---



## ARPA-HARDENING §5 — Revocation effectiveness and convergence

<!-- consolidated-source: ARPA-HARDENING §5 -->

An effective authoritative revocation immediately makes the revoked authority non-affirmative for new authority evaluations. From the revocation's effective time, an authority evaluator MUST NOT return `allow` or `allow_with_conditions` for a new action dependent on that authority.

Revocation convergence is a separate enforcement-evidence property. A registry MUST distinguish at least:

- `revoked_propagation_pending`;
- `revoked_propagation_failed`; and
- `revoked_converged`.

Pending or failed enforcement acknowledgement MUST NOT restore or extend revoked authority. It indicates that enforcement evidence is incomplete or that operational containment has failed.

A propagation deadline is an operational bound, not evidence of convergence. Missing required acknowledgements after the deadline MUST produce a propagation failure or escalation state.



## ARPA-HARDENING §8 — Multi-dimensional status composition

<!-- consolidated-source: ARPA-HARDENING §8 -->

Registration, operational, authority, assurance, and security status MUST remain separate dimensions. Cross-dimensional execution gating MUST NOT rely on a single total ordering of heterogeneous status labels.

Each material status dimension MUST map under the applicable profile/policy to one of:

- `permit`;
- `permit_with_conditions`;
- `deny`; or
- `indeterminate`.

Composition MUST be monotonic toward safety:

1. any applicable `deny` yields a non-affirmative result;
2. an applicable `indeterminate` MUST NOT be converted to `permit` merely because another dimension is affirmative;
3. conditions accumulate unless the governing policy explicitly proves that one condition supersedes another; and
4. a less restrictive status in one dimension MUST NOT cancel a more restrictive material status in another dimension.


# 21. Query Protocol

## 21.1 Transport

The specification is transport-independent.

Implementations MUST provide at least one machine-readable query interface over a secure transport.

HTTP-based deployments SHOULD use:

- HTTPS;
- JSON request and response bodies;
- authenticated access where required;
- stable media types; and
- idempotent semantics for read operations.

## 21.2 Media Type

This specification reserves the provisional media type:

```text
application/agent-registry+json
```

## 21.3 Core Endpoints

A conforming HTTP implementation SHOULD provide:

```text
GET  /agents/{agent_id}
GET  /agents/{agent_id}/status
GET  /agents/{agent_id}/lineage
GET  /agents/{agent_id}/relationships
GET  /agents/{agent_id}/capabilities
GET  /agents/{agent_id}/assurance
GET  /agents/{agent_id}/governance
GET  /agents/{agent_id}/events
POST /authority/evaluate
POST /reliance/evaluate
POST /discovery/search
GET  /records/{record_id}
GET  /events
```

## 21.4 Point-in-Time Queries

All core state queries MUST support a point-in-time parameter.

Example:

```text
GET /agents/{agent_id}?at=2026-07-15T10:00:00Z
```

A point-in-time response MUST disclose whether it is:

- authoritative;
- reconstructed;
- incomplete;
- approximate; or
- indeterminate.

### 21.4.1 Historical Authority Resolution

When `at` is earlier than the response evaluation time, the resolver MUST treat `at` as `requested_time` and MUST evaluate records according to the effective intervals, ordered events, applicable governance rules, and evidence available for that requested time.

A conforming historical result MUST expose, directly or through an equivalent envelope:

- `requested_time`;
- `evaluation_time`;
- `state_at_requested_time`;
- `current_state`;
- `reconstruction_status`;
- the record identifiers, versions, effective intervals, and digests used for reconstruction;
- an event checkpoint when available;
- later material events relevant to interpretation;
- `historical_effect`;
- retention/evidence availability; and
- evidence references and integrity status.

`state_at_requested_time` and `current_state` are independent outputs. A registry MUST NOT substitute current state for historical state. When they differ, the difference MUST be visible to the caller.

Later suspension, revocation, compromise, supersession, recognition withdrawal, governance correction, or integrity failure MUST be disclosed when material to interpretation of the historical result. Each such event MUST classify its historical effect using the controlled vocabulary in `registries/historical-effect-codes.json`.

A later current-state transition does not, by itself, rewrite historical state. Retroactive effect MUST be grounded in an applicable governance rule or authoritative event declaration. Where that effect cannot be resolved, the historical result MUST be `indeterminate` or otherwise explicitly non-affirmative.

A historical-resolution result establishes registry-resolved state and evidence. It MUST NOT be represented as a determination that a relying party is legally, contractually, fiduciary-wise, or operationally required to accept the historical action.

### 21.4.2 Retention and integrity

When the requested time is outside the available retention boundary, the registry MUST disclose that boundary and MUST NOT answer using current state as a substitute. Missing, conflicting, withheld, or integrity-failed evidence MUST be surfaced using a bounded reconstruction status.

The records and material events used for historical reconstruction MUST have tamper-evident lineage. A profile MAY select the lineage mechanism, but the response MUST identify the evidence/integrity status and SHOULD identify the mechanism used.

The machine-readable response contract is defined by `schemas/historical-resolution.schema.json`.

## 21.5 Query Response Envelope

Every response MUST include:

```json
{
  "request_id": "string",
  "result": {},
  "result_status": "success",
  "authoritative": true,
  "source": {
    "registry": "string",
    "checkpoint": "string",
    "source_time": "date-time"
  },
  "projection": {
    "used": false,
    "updated_at": null,
    "lag_seconds": 0
  },
  "generated_at": "date-time",
  "valid_until": "date-time",
  "warnings": []
}
```

## 21.6 Reliability Metadata

A response used for consequential reliance MUST include:

- source identifier;
- source checkpoint;
- source timestamp;
- projection status;
- known lag;
- response timestamp;
- validity window;
- status freshness;
- proof or verification reference; and
- policy version where a decision is returned.

## 21.7 Discovery Search

Discovery MUST support structured filters.

Supported filter classes SHOULD include:

- capability;
- assurance profile;
- governance framework;
- jurisdiction;
- protocol;
- risk class;
- operational status;
- security status;
- accountable entity;
- operator;
- data-handling constraints;
- cost class;
- latency or service-level attributes; and
- recognition domain.

Search results MUST NOT imply authorization or suitability.

## 21.8 Reliance Evaluation

A reliance request SHOULD include:

- candidate agent;
- intended action;
- required assurance profile;
- accepted governance authorities;
- accepted assurance providers;
- maximum status age;
- accepted jurisdictions;
- runtime attestation requirements;
- incident policy;
- delegation requirements;
- privacy requirements; and
- local relying-party policy identifier.

The result MUST include:

- `satisfied`;
- `not_satisfied`;
- `indeterminate`;
- unmet conditions;
- supporting evidence;
- warnings;
- freshness;
- policy version; and
- decision receipt.

## 21.9 Query Authorization

Registries MUST support access-control policy for protected records.

A denied response SHOULD disclose only what policy permits.

## 21.10 Cache Control

Responses MUST specify cacheability and maximum age.

High-risk authority or security queries SHOULD be non-cacheable or short-lived unless protected by signed status objects.

---



## ARPA-CAND-PP-01 §2 — Historical resolution result contract

<!-- consolidated-source: ARPA-CAND-PP-01 §2 -->

Historical resolution is a reconstruction operation, not merely a current response filtered by timestamp.

A successful historical-resolution result MUST identify, directly or by stable reference:

- the requested effective time;
- the time at which resolution/evaluation was performed;
- the authoritative or derived records selected as effective at the requested time;
- provenance sufficient to identify the source and version/checkpoint of each selected material record;
- later material events known at evaluation time that affect interpretation of the historical result; and
- a reconstruction status or equivalent quality statement that distinguishes complete, partial, unavailable, conflicting and integrity-failed reconstruction where those states are applicable.

A registry MUST NOT silently substitute current state for requested-time state.

A registry MUST NOT silently omit a later material event when that event changes how the historical result can safely be interpreted.

If material historical evidence is unavailable, conflicting, fails integrity validation or cannot be reconstructed to the degree required by the applicable policy, the result MUST be non-affirmative and MUST expose the applicable reconstruction condition.

HTTP path layout is not part of this semantic requirement. A deployment MAY expose historical resolution through an `at` parameter, a dedicated resource, or another discoverable operation mapping, provided that the result contract above is preserved.



## ARPA-CAND-PP-03 §7 — Media type and content negotiation

<!-- consolidated-source: ARPA-CAND-PP-03 §7 -->

The Candidate media type remains:

`application/agent-registry+json`

No `application/arpa+json` alias is introduced.

For HTTP APIs, `application/agent-registry+json` is the preferred ARPA representation. `application/json` MAY be supported as a compatibility fallback when the payload semantics are identical. A server MUST NOT vary normative semantics solely because the generic fallback was negotiated.

No media-type parameter is required by PP-03. Protocol/profile version negotiation remains explicit in the governing contract rather than being silently inferred from an unregistered media-type parameter.


# 22. Authority Evaluation

Authority evaluation determines whether a particular action is within a valid delegation and applicable policy. Implementations MUST expose the request, response, and Decision Receipt semantics defined in Sections 18, 21, 25, and 28.

## 22.1 Inputs

The evaluator MUST accept sufficient context to identify the agent, principal, action, resource, purpose, time, deployment, jurisdiction, quantitative values, approval state, and relying policy.

## 22.2 Output

The decision MUST be `allow`, `allow_with_conditions`, `deny`, `indeterminate`, or `not_applicable`. Conditions and reason codes MUST be explicit.

## 22.3 Processing

The evaluator MUST follow Section 28.2. A deployment MUST NOT claim interoperable authority evaluation if it omits delegation-lineage validation, status freshness, or issuer-competence checks required by its profile.

---



## ARPA-HARDENING §3 — `not_applicable` is not an authority bypass

<!-- consolidated-source: ARPA-HARDENING §3 -->

`not_applicable` MAY be returned only where the requested operation is outside the declared authority-evaluation domain of the selected profile or policy.

Absence of authority, missing delegation, expired authority, revoked authority, suspended authority, unsupported evidence, unavailable evidence, an unrecognized issuer, an incomparable scope, an unresolved critical extension, stale material state, or an inability to determine authority MUST NOT produce `not_applicable`.

Where authority evaluation is applicable but cannot produce an affirmative determination, the evaluator MUST return `deny` or `indeterminate` according to the applicable policy and reason codes.



## ARPA-HARDENING §6 — Deterministic evaluation context and checkpoints

<!-- consolidated-source: ARPA-HARDENING §6 -->

A deterministic ARPA decision is a function of the complete evaluation state, not merely a request body and policy identifier.

For consequential authority evaluation, the reproducibility tuple MUST include, directly or by digest/reference:

- request and material context;
- evaluation time;
- policy identifier and version;
- selected authoritative record identifiers and versions/digests;
- material source checkpoints or sequence positions;
- freshness inputs;
- recognition/issuer-competence state; and
- material external evidence used by the policy.

Two evaluations are required to produce the same decision and reason-code set only when this reproducibility tuple is equivalent.

Where a decision depends on multiple independently ordered sources, the decision receipt MUST identify the source checkpoint set sufficient to reconstruct the evaluated snapshot. If no coherent snapshot can be established for material state, the decision MUST be non-affirmative.



## ARPA-CAND-PP-02 §1 — Action-specific authority context

<!-- consolidated-source: ARPA-CAND-PP-02 §1 -->

When an ARPA authority evaluator determines whether resolved authority state can support a proposed material action, the evaluation MUST be bound to an explicit action context.

The action context MUST identify, directly or by stable reference:

- the action or action class;
- the resource or target to which the action applies;
- the evaluation time;
- all material constraints needed to evaluate the authority envelope; and
- a canonical action digest or equivalent stable action binding when an approval, signature, receipt, or downstream execution can otherwise be replayed or substituted across actions.

A valid identity, signature, registration, capability declaration, endpoint, credential, or successful registry resolution MUST NOT by itself be treated as authority for the action.



## ARPA-CAND-PP-02 §2 — Current authority and constraint preservation

<!-- consolidated-source: ARPA-CAND-PP-02 §2 -->

An affirmative authority result MUST require current effective authority at the evaluation time.

Expired, suspended, revoked, stale, conflicting, unavailable, unverifiable, or otherwise indeterminate material authority state MUST NOT produce an affirmative result.

The evaluator MUST apply all material constraints carried by the authority envelope, including applicable action, resource, purpose, counterparty, jurisdiction, value, rate, time, prohibition, and delegation-depth limits. Evaluation MUST NOT enlarge those constraints.

If the proposed action exceeds a material limit or falls outside the applicable scope, the result MUST be non-affirmative.



## ARPA-CAND-PP-02 §3 — Approval binding

<!-- consolidated-source: ARPA-CAND-PP-02 §3 -->

When the effective authority or relying policy requires additional approval, each counted approval MUST be bound to the exact action being evaluated or to a canonical digest that unambiguously identifies that action.

An approval for a different action, resource, amount, counterparty, material parameter, or action digest MUST NOT satisfy the requirement.

An expired, revoked, unverifiable, or materially incomplete approval MUST NOT be counted.

Missing required approval evidence produces a non-affirmative result. Where the system cannot establish whether required approval evidence exists or is current, the result MUST remain indeterminate rather than being converted to affirmative.



## ARPA-CAND-PP-03 §2 — Authority evaluation result and `not_applicable`

<!-- consolidated-source: ARPA-CAND-PP-03 §2 -->

Authority evaluation is represented by `schemas/authority-evaluation-result.schema.json`.

`not_applicable` is a normal authority-evaluation outcome. It is not:

- a lifecycle state;
- an HTTP/protocol error;
- a substitute for `deny`; or
- a substitute for `indeterminate`.

It MAY be returned only when the selected policy or profile does not govern the requested operation. A `not_applicable` result MUST include at least one stable reason code explaining the non-applicability.

The following conditions MUST NOT yield `not_applicable`: missing authority, missing delegation, expired/revoked/suspended authority, stale or conflicting material state, unknown critical extensions, unavailable or unsupported evidence, incomparable scope, unrecognized issuer, or any inability to determine authority. Such cases yield `deny`, `indeterminate`, or a protocol error according to the failure layer.

Protocol errors are reserved for malformed requests, unsupported protocol/profile/version negotiation, invalid wire representations, unavailable protocol services and equivalent transport/protocol failures. They do not encode a valid policy outcome.

**Compatibility classification:** additive. Existing affirmative/negative outcomes remain valid; this specification makes the pre-existing `not_applicable` outcome machine-readable and removes ambiguous encodings.


# 23. Reliance Evaluation

Reliance evaluation determines whether an agent satisfies a relying party's contextual requirements. It is distinct from authority evaluation: an agent may satisfy assurance and governance requirements but lack authority for a particular action, or hold authority while failing the relying party's security or assurance policy.

## 23.1 Request

A request SHOULD identify the intended action, required assurance, accepted governance authorities and assurance providers, maximum status age, jurisdiction, runtime-attestation requirement, incident policy, privacy constraints, and local policy identifier.

## 23.2 Response

The response MUST be `satisfied`, `not_satisfied`, or `indeterminate` and MUST enumerate supporting evidence, unmet conditions, warnings, freshness, and the evaluated policy version.

## 23.3 Processing

The evaluator MUST follow Section 28.3 and produce a Decision Receipt when required by profile.

---

# 24. Events and Subscriptions

> **Candidate control:** ARPA-CAND-007. Candidate-conformant event delivery requires durable sequencing, replay, deduplication, idempotent processing, checkpointing, gap detection, retry, and evidence of consumer acknowledgement.

## 24.1 Event Requirements

Every material state change MUST produce an event.

## 24.2 Event Types

Base event types SHOULD include:

- `agent.registered`;
- `agent.activated`;
- `agent.updated`;
- `agent.restricted`;
- `agent.suspended`;
- `agent.quarantined`;
- `agent.compromised`;
- `agent.revoked`;
- `agent.retired`;
- `agent.superseded`;
- `agent.control_changed`;
- `agent.operator_changed`;
- `agent.accountable_entity_changed`;
- `version.published`;
- `deployment.created`;
- `deployment.attested`;
- `deployment.restricted`;
- `delegation.issued`;
- `delegation.narrowed`;
- `delegation.suspended`;
- `delegation.revoked`;
- `assurance.issued`;
- `assurance.expired`;
- `assurance.suspended`;
- `assurance.revoked`;
- `incident.opened`;
- `incident.updated`;
- `incident.closed`;
- `appeal.filed`;
- `appeal.decided`;
- `status.restored`;
- `recognition.added`;
- `recognition.changed`; and
- `recognition.withdrawn`.

## 24.3 Event Envelope

```json
{
  "event_id": "string",
  "event_type": "agent.suspended",
  "subject": "agentreg:example.org:agent-123",
  "sequence": 1021,
  "occurred_at": "2026-07-15T10:00:00Z",
  "effective_at": "2026-07-15T10:00:00Z",
  "issuer": "registry:example.org",
  "reason_code": "security_review",
  "scope": {},
  "record_refs": [],
  "proof": {}
}
```

## 24.4 Ordering

Events MUST include a per-subject or per-registry ordering mechanism.

## 24.5 Replay

Subscribers MUST be able to request replay from a checkpoint, event identifier, or timestamp.

## 24.6 Delivery Semantics

A registry MUST declare whether event delivery is:

- at-most-once;
- at-least-once; or
- effectively-once.

Consumers MUST be able to deduplicate events using `event_id`.

## 24.7 Enforcement Acknowledgement

Delegated-authority and high-assurance profiles MUST support authenticated acknowledgement events from applicable enforcement points. An acknowledgement MUST identify the revocation or status event, the enforcement surface, the applied time, the outcome, any partial failure, and the authenticated issuer. Absence of a required acknowledgement MUST keep the revocation in a non-converged state.

---

# 25. Execution and Decision Receipts

## 25.1 Applicability

Execution evidence is REQUIRED for accountable, delegated-authority, and high-assurance profiles for actions classified as consequential.

For Profiles B, C, and D, the deployment MUST publish a machine-readable consequential-action classification policy. The policy MUST identify the action classes or decision rules treated as consequential, the risk basis for the classification, the policy identifier and version, and the evidence obligations triggered by the classification. An implementation MUST NOT avoid profile evidence, redress, or enforcement requirements by leaving a materially rights-affecting, asset-controlling, identity-affecting, safety-critical, irreversible, transaction-submitting, or protected-data action unclassified. The conformance declaration MUST identify the applicable classification policy.

## 25.2 Execution Receipt Contents

An Execution Receipt MUST include, as applicable:

- receipt identifier;
- task or transaction identifier;
- agent identifier;
- agent version;
- deployment identifier;
- runtime identifier;
- principal;
- beneficiary;
- authority envelope identifier;
- authority decision receipt;
- policy version;
- action class;
- resource;
- purpose;
- input digest;
- output digest;
- tool and service references;
- approvals obtained;
- downstream delegations;
- start time;
- completion time;
- result;
- side effects;
- error or exception;
- evidence references;
- redress reference; and
- proof.

## 25.3 Confidentiality

Receipts MAY omit confidential payloads while retaining digests, references, or selectively disclosable evidence.

## 25.4 Non-Repudiation and Attribution

A receipt SHOULD support verification that:

- the relevant runtime produced or endorsed it;
- the authority decision existed before or during execution;
- required approvals were obtained;
- the referenced policy version was active; and
- the receipt has not been altered.

## 25.5 Failure Receipts

Failed and denied actions SHOULD produce receipts when they are relevant to audit, abuse detection, or dispute resolution.

## 25.6 Retention

Governance profiles MUST define retention periods for receipts and supporting evidence.

---



## ARPA-CAND-PP-02 §6 — Evidence and reproducibility

<!-- consolidated-source: ARPA-CAND-PP-02 §6 -->

An implementation producing an authority evaluation SHOULD retain enough evidence to reproduce the material decision, subject to privacy and retention constraints. This normally includes:

- evaluation time;
- authoritative source or checkpoint;
- authority and lifecycle records used;
- action context or canonical action digest;
- material constraints applied;
- approval or collective-rule evidence used; and
- the resulting affirmative, negative, or indeterminate outcome.

Evidence retention does not itself confer authority and MUST NOT override applicable privacy, confidentiality, or minimization requirements.


# 26. Federation and Recognition

> **Candidate controls:** ARPA-CAND-003 and ARPA-CAND-004. Recognition is an explicit, scoped, time-bound governance statement. Federation is a technical exchange relationship and MUST NOT be interpreted as recognition, transitive trust, or transfer of authority.

## 26.1 Federation Principle

Registries MAY interoperate technically without mutually recognizing each other’s records.

Recognition MUST be explicit.

## 26.2 Recognition Record

A Recognition Record MUST specify:

- recognizing domain;
- recognized domain or issuer;
- recognized record types;
- recognized assurance profiles;
- recognized governance decisions;
- status handling;
- effective period;
- exclusions;
- transformation rules;
- dispute rules;
- withdrawal semantics; and
- proof.

## 26.3 Partial Recognition

Recognition MAY be partial.

Examples:

- identity records accepted, assurance claims rejected;
- assurance claims accepted only for low-risk actions;
- suspensions recognized immediately, restorations subject to review;
- one jurisdiction’s governance decisions accepted only for specified agents.

## 26.4 Recognition Chains

A registry MUST NOT automatically infer transitive recognition unless explicitly authorized.

## 26.5 Conflicting Status

Where recognized sources conflict, the relying policy MUST define precedence, aggregation, or indeterminate handling. If no applicable rule resolves the conflict, the evaluator MUST return `indeterminate` or a stricter non-affirmative outcome; it MUST NOT select the most permissive source or silently retain a previously affirmative result.

## 26.6 Federation Discovery

A federation SHOULD publish:

- participating registries;
- namespaces;
- supported profiles;
- recognition rules;
- schema versions;
- trust anchors;
- query endpoints; and
- incident contacts.

---



## ARPA-HARDENING §4 — Recognition conflict and issuer competence

<!-- consolidated-source: ARPA-HARDENING §4 -->

A precedence rule MAY establish which source is competent for a particular record type, subject, jurisdiction, or scope. Once a published governance rule establishes that one source is authoritative and another source is non-authoritative for that scope, the lower-precedence statement need not constitute an unresolved authoritative conflict.

Where two or more simultaneously competent authoritative sources conflict and no applicable governance rule removes one source's competence or deterministically resolves the conflict, the evaluator MUST return `deny` or `indeterminate`. It MUST NOT select the most permissive source, retain a cached affirmative result, or reinterpret the conflict as `not_applicable`.

The decision receipt MUST identify the conflicting claims, competence/recognition basis, precedence rule evaluated, and resulting disposition.


# 27. Governance, Appeals, and Redress

## 27.1 Governance Metadata

A conforming registry MUST publish or resolve:

- governance authority;
- governance framework identifier;
- policy version;
- admission criteria;
- monitoring obligations;
- suspension and revocation rules;
- appeal procedure;
- dispute venue;
- incident reporting endpoint;
- recognition policy;
- transparency policy;
- emergency process;
- restoration process;
- data retention rules; and
- redress process.

## 27.2 Reason Codes

Lifecycle and enforcement actions MUST use structured reason codes.

Free-text explanation MAY supplement but MUST NOT replace structured reason codes.

## 27.3 Appeal

A registry MUST support appeal or correction processes for:

- incorrect identity binding;
- unauthorized control change;
- erroneous suspension;
- erroneous revocation;
- inaccurate relationship record;
- incorrect assurance status;
- misattributed execution;
- stale status;
- unlawful or invalid delegation; and
- disputed recognition decision.

## 27.4 Due Process

For Profile B, C, and D deployments, governance profiles MUST specify due-process handling for consequential suspension, revocation, restoration, control change, recognition withdrawal, and disputed execution. At minimum they MUST specify:

- notice;
- opportunity to respond;
- emergency exception;
- evidence standards;
- decision authority;
- time limits;
- publication rules;
- restoration;
- correction;
- compensation or remediation where applicable.

## 27.5 Redress Record

For Profile B, C, and D deployments, a Redress Record MUST be resolvable for consequential actions and lifecycle decisions. It MUST include:

- affected subject;
- complainant class;
- issue type;
- intake endpoint;
- required evidence;
- response time;
- escalation path;
- appeal path;
- available remedies;
- responsible entity; and
- governing policy.

## 27.6 Essential Service Continuity

High-assurance public-service profiles SHOULD define fallback or continuity arrangements when suspension of an agent could deny access to essential services.

---

# 28. Processing Rules

This section defines the normative processing behavior that connects the record model to interoperable decisions.

## 28.1 General Evaluation Rules

An evaluator MUST:

1. validate record syntax and schema;
2. validate proof integrity where required;
3. validate issuer competence and recognition;
4. validate time applicability;
5. validate status and freshness;
6. resolve supersession and lineage;
7. apply profile and relying-party policy;
8. preserve warnings and conflicting evidence; and
9. produce a deterministic outcome for the same inputs, records, and policy version.

An evaluator MUST NOT silently ignore an unknown critical extension, invalid proof, unresolved required status, or unrecognized issuer.

## 28.2 Authority Evaluation Algorithm

A conforming authority evaluator MUST perform the following steps or an equivalent process preserving the same semantics:

1. Resolve the agent identifier.
2. Resolve the relevant agent version and deployment.
3. Confirm that registration status permits the requested class of action.
4. Confirm that operational and security status permit execution.
5. Confirm that all required status records satisfy freshness policy.
6. Resolve the immediate authority envelope for the agent and principal.
7. Resolve the complete delegation lineage required by the envelope.
8. Verify proofs, issuer competence, validity periods, and revocation status for every delegation.
9. Verify that each downstream delegation narrows or preserves, but never expands, upstream action, resource, purpose, jurisdiction, time, quantitative limit, approval, prohibition, assurance, and delegation-depth constraints.
10. Evaluate the requested action, resource, purpose, jurisdiction, amount, time, deployment, and other contextual inputs.
11. Apply mandatory prohibitions before discretionary conditions.
12. Determine required approvals and whether they are already satisfied.
13. Resolve required assurance claims and confirm applicability to the current version and deployment.
14. Evaluate registry, issuer, assurance-provider, and governance recognition.
15. Apply the named relying-party policy.
16. Return `allow`, `allow_with_conditions`, `deny`, `indeterminate`, or `not_applicable`.
17. Produce a Decision Receipt.

A failed mandatory prohibition check MUST result in `deny`. Missing required current status or conflicting authoritative evidence SHOULD result in `indeterminate` unless policy explicitly requires denial.

## 28.3 Reliance Evaluation Algorithm

A reliance evaluator MUST determine whether the candidate agent satisfies the relying party's conditions independently of whether a particular delegation exists. It MUST evaluate, as applicable:

- registry recognition;
- identifier continuity;
- current version and deployment;
- accountable entity;
- required assurance profile;
- assurance-provider recognition;
- material-change status;
- runtime attestation;
- operational and security status;
- open incidents;
- jurisdiction and data-handling constraints;
- governance framework;
- redress availability;
- evidence availability; and
- freshness policy.

The result MUST enumerate unmet or indeterminate conditions. It MUST NOT return a generic `trusted` boolean.

## 28.4 Status Precedence

Status dimensions MUST remain separately visible. For execution gating, the following default precedence SHOULD apply unless a profile defines a stricter rule:

```text
confirmed_compromise
    > quarantined
    > revoked
    > suspended
    > restricted
    > active
```

An `under_investigation` state does not by itself imply compromise. The governing profile MUST define whether it triggers monitoring, restriction, suspension, or no automatic execution effect.

When dimensions conflict, the most restrictive applicable status MUST govern execution. The response MUST preserve all source statuses and explain the precedence rule used.

## 28.5 Point-in-Time Reconstruction

A point-in-time query MUST evaluate records according to their effective intervals, the authoritative event sequence, and the governance rules applicable to the requested time.

The processor MUST:

1. parse and preserve the requested time separately from evaluation time;
2. identify the authoritative subject and applicable namespace;
3. select every record whose effective interval and scope may affect the requested state;
4. validate record proof/integrity and issuer competence;
5. replay or evaluate material lifecycle, relationship, authority, assurance, recognition, compromise, and supersession events through the requested time;
6. apply applicable governance rules and precedence rules;
7. derive `state_at_requested_time` without consulting current state as a substitute;
8. independently resolve `current_state`;
9. identify later material events after the requested time that can affect interpretation;
10. classify the historical effect of those later events;
11. record selected record versions/digests and an event checkpoint where available;
12. evaluate retention and evidence-integrity status; and
13. return a deterministic reconstruction classification.

The response MUST classify reconstruction as one of:

- `authoritative_complete`;
- `authoritative_partial`;
- `reconstructed_complete`;
- `reconstructed_partial`;
- `approximate`; or
- `indeterminate`.

A registry MUST NOT substitute current state for historical state. Missing historical evidence MUST be surfaced rather than inferred as valid. Conflicting authoritative history that cannot be resolved by a published precedence rule MUST result in `indeterminate`.

Where a later event declares `retroactive` effect, the resolver MUST identify the governance basis and MUST expose the event as material to interpretation. Where later compromise has an unknown effective origin, or the governance effect cannot be determined, the historical result MUST NOT be upgraded to an unqualified affirmative state.

An integrity failure in the evidence lineage MUST yield `indeterminate`, `authoritative_partial`, or `reconstructed_partial` according to the surviving evidence. It MUST NOT yield an unqualified `authoritative_complete` or `reconstructed_complete` result.

Historical resolution and relying-party acceptance are separate decisions. An historical result such as active or recognized at time T is an input to relying-party policy and does not itself compel acceptance of an action performed at T.

## 28.6 Material Change Processing

When a material change occurs, the registry MUST determine which linked records are affected. The result for each assurance claim, delegation, relationship, endpoint, and deployment MUST be one of:

- remains valid;
- remains valid with narrowed scope;
- enters review;
- becomes conditional;
- becomes suspended;
- terminates;
- requires reissuance; or
- requires novation.

The change event MUST identify the applicable transition policy.

## 28.7 Revocation and Cascade Processing

On revocation, the processor MUST:

1. validate revocation authority;
2. identify effective time and scope;
3. update authoritative status;
4. identify directly dependent delegations and enforcement surfaces;
5. apply the governing cascade rule;
6. emit events;
7. invalidate applicable cached decisions;
8. notify enforcement points;
9. record acknowledgements and failures; and
10. preserve the prior record for historical resolution.

A downstream delegation MUST NOT remain affirmatively active when its required parent authority is revoked. It MUST become revoked, suspended, or indeterminate according to declared cascade semantics.

After notification, the processor MUST track each applicable enforcement target as `pending`, `acknowledged`, `failed`, or `removed_from_scope`. The processor MUST NOT report `converged` until no target remains `pending` or `failed`. Expiry of a propagation target MUST produce an operational failure or escalation signal; it MUST NOT convert a non-converged revocation into a converged one.

## 28.8 Conflict Processing

When recognized sources conflict, the evaluator MUST apply a published precedence or aggregation policy. If no applicable rule resolves the conflict, the result MUST be `indeterminate`.

The evaluator MUST include:

- conflicting claims;
- issuers;
- effective times;
- recognition basis;
- precedence rule attempted; and
- required remediation or authoritative query.

## 28.9 Decision Validity and Reuse

A Decision Receipt MUST have a bounded validity period. A PEP MUST reject reuse when any material input differs, including agent, deployment, action, resource, amount, purpose, approval state, or relevant status checkpoint.

A status or revocation event affecting the decision MAY invalidate the receipt before its scheduled expiry. Profiles MUST define how invalidation is communicated.

## 28.10 Negative Outcome Examples

### Expired Assurance

```json
{
  "decision": "indeterminate",
  "reason_codes": ["assurance_expired"],
  "required_actions": ["obtain_current_assurance"]
}
```

### Revoked Upstream Delegation

```json
{
  "decision": "deny",
  "reason_codes": [
    "upstream_authority_revoked",
    "downstream_delegation_invalid"
  ]
}
```

### Stale Projection

```json
{
  "decision": "indeterminate",
  "reason_codes": ["projection_lag_exceeds_policy"],
  "authoritative_query_required": true
}
```

### Conflicting Recognized Status

```json
{
  "decision": "indeterminate",
  "reason_codes": ["recognized_sources_conflict"],
  "conflicts": [
    {"source": "registry-a", "status": "active"},
    {"source": "registry-b", "status": "suspended"}
  ]
}
```

---



## ARPA-HARDENING §2 — Temporal interval and clock semantics

<!-- consolidated-source: ARPA-HARDENING §2 -->

Unless a profile explicitly defines a stricter interval, ARPA validity intervals are half-open:

```text
effective_from <= evaluation_time < effective_until
```

A null `effective_until` denotes no declared upper bound; it does not override revocation, suspension, supersession, or another applicable status boundary.

An action evaluated exactly at `effective_until` is outside the interval.

Evaluators MUST normalize timestamps to a common time basis and MUST preserve the original timestamp where required for evidence. Profiles used for consequential action MUST declare permitted clock skew, timestamp precision, and treatment of future-dated observations. A future-dated or clock-ambiguous material status MUST NOT silently produce an affirmative decision.

Where multiple material events have the same wall-clock timestamp, a declared authoritative sequence, checkpoint, or equivalent ordering mechanism MUST determine order. If contradictory events remain unordered after applying the declared ordering mechanism, the affected state MUST be `indeterminate`.



## ARPA-CAND-PP-03 §3 — Time boundaries and clock profile

<!-- consolidated-source: ARPA-CAND-PP-03 §3 -->

Unless a stricter profile applies, authority validity remains half-open:

`effective_from <= evaluation_time < effective_until`.

An action evaluated exactly at `effective_from` is inside the interval. An action evaluated exactly at `effective_until` is outside it.

Where timestamp precision or clock skew can affect an authority decision, the selected deployment/profile MUST expose, directly or by stable policy reference:

- timestamp precision;
- maximum permitted clock skew; and
- treatment of future-dated material observations.

No universal skew value is imposed by this specification. A clock-ambiguous material state MUST remain non-affirmative until the selected policy resolves the ambiguity.


# 29. Security Architecture

> **Candidate control:** ARPA-CAND-008. Cryptographic proof establishes only the claims supported by the proof and trust configuration. It MUST NOT, by itself, establish current authority, assurance, governance recognition, or acceptable reliance.

## 29.1 Threat Model

Implementations MUST consider at least:

- false registration;
- identifier takeover;
- key compromise;
- controller compromise;
- malicious operator;
- compromised registry operator;
- stale index or cache;
- equivocation;
- unauthorized metadata change;
- capability inflation;
- assurance laundering;
- delegation escalation;
- revocation failure;
- downstream delegation persistence;
- replay;
- forged receipts;
- endpoint substitution;
- malicious schema extension;
- denial of service;
- privacy leakage;
- correlation;
- insider abuse;
- compromised policy decision point;
- compromised policy enforcement point;
- malicious federation peer;
- conflicting recognition; and
- governance capture.

## 29.2 Key Separation

High-impact administrative functions MUST use separated keys or authorization roles.

At minimum, high-assurance profiles SHOULD separate:

- control;
- operations;
- delegation;
- assurance;
- payment;
- security suspension;
- recovery; and
- governance enforcement.

## 29.3 Threshold Authorization

Profile C and D deployments MUST require threshold approval, dual control, or an equivalently independent multi-party authorization mechanism for the following high-impact administrative operations:

- change of accountable entity;
- ownership-like transfer;
- security restoration after compromise;
- replacement of recovery keys;
- modification of governance framework;
- broad authority issuance;
- removal of critical prohibitions; and
- deletion or redaction of evidence.

## 29.4 Transaction Intent

Administrative interfaces MUST present human- or machine-verifiable transaction intent before authorization.

Intent SHOULD disclose:

- action;
- subject;
- affected records;
- effective time;
- downstream effects;
- irreversible effects;
- required approvals; and
- policy basis.

## 29.5 Revocation Propagation

A conformance profile MUST define maximum acceptable propagation time from authoritative revocation to enforcement and MUST define the evidence required to establish enforcement convergence. Profiles C and D MUST require authenticated enforcement acknowledgements for applicable enforcement targets. Missing acknowledgements after the propagation target expires MUST be treated as a revocation-propagation failure and MUST NOT be interpreted as convergence.

## 29.6 Stale Data

A relying party MUST be able to enforce maximum age for:

- agent status;
- authority status;
- assurance status;
- runtime attestation;
- incident status; and
- recognition rules.

## 29.7 Endpoint Security

Registries MUST:

- use authenticated transport;
- validate endpoint schemes;
- prevent server-side request forgery in registry fetchers;
- constrain redirects;
- validate content type;
- limit payload size;
- isolate parsing;
- validate schemas; and
- preserve historical versions of critical descriptions.

## 29.8 Schema Security

Unknown critical extensions MUST cause processing failure.

Registries SHOULD maintain:

- extension registries;
- namespace ownership;
- schema signing;
- size limits;
- recursion limits;
- prohibited fields; and
- deprecation rules.

## 29.9 Equivocation

A registry MUST prevent or detect the presentation of conflicting authoritative state to different relying parties.

Suitable mechanisms MAY include:

- transparency logs;
- signed checkpoints;
- append-only journals;
- witness cosigning;
- distributed consensus;
- audit replication; or
- cross-operator reconciliation.

## 29.10 Recovery

Recovery procedures MUST be documented and auditable.

A recovery event MUST NOT silently erase compromise history.

## 29.11 Dependency Security

Assurance and operational profiles SHOULD disclose material dependencies, including:

- model providers;
- tool providers;
- hosting environments;
- identity providers;
- key management systems;
- policy engines; and
- external registries.

## 29.12 Denial of Service

Registries SHOULD support:

- rate limits;
- query cost controls;
- pagination;
- bounded search;
- event backpressure;
- replicated read paths;
- degraded-mode status;
- abuse detection; and
- emergency read-only operation.

---



## ARPA-HARDENING §7 — Proof-input semantics

<!-- consolidated-source: ARPA-HARDENING §7 -->

A proof type used for a normative ARPA record MUST define:

- the exact proof input transformation;
- fields excluded from or transformed before proof computation;
- canonicalization or deterministic encoding;
- algorithm and suite identification;
- domain separation or context binding;
- verification-method interpretation;
- key-status evaluation time; and
- replay/context-binding semantics where replay is material.

Use of JCS or another canonicalization algorithm alone does not define which logical object is signed. An implementation MUST NOT claim proof interoperability unless these proof-input semantics are declared and implemented consistently.

Proof validity continues to establish only the claims supported by the proof and configured trust relationship; it MUST NOT establish authority, recognition, assurance, or acceptable reliance by itself.


# 30. Privacy Architecture

## 30.1 Privacy Objective

The registry MUST support reliable decisions without requiring universal publication of identity, relationship, delegation, telemetry, or evidence data. Privacy is therefore an architectural property of resolution, access, and disclosure, not merely a notice or retention policy.

## 30.2 Public Pointer, Protected Record

A public record MAY reveal only:

- record identifier;
- record type;
- issuer;
- subject commitment or scoped identifier;
- current status;
- digest;
- access endpoint;
- disclosure policy; and
- proof.

The full record MAY remain protected. The resolver MUST distinguish “record exists but access is restricted” from “record not found” where policy permits.

## 30.3 Selective Attribute Disclosure

A registry SHOULD support proofs or attestations of policy-relevant properties without disclosing the complete source record. Examples include:

- authority covers the requested action;
- spending limit is at least the requested amount;
- assurance profile meets a named minimum;
- deployment is within an accepted jurisdiction;
- required human approval was obtained; or
- no disqualifying incident is currently active.

## 30.4 Pairwise and Scoped Identifiers

Where correlation risk is material, a registry MUST support pairwise or context-scoped agent, principal, or relationship identifiers, or document an equivalent privacy control that prevents unnecessary cross-context linkage. A protected linkage MAY connect scoped identifiers to a canonical record for authorized audit or redress.

## 30.5 Confidential Authority Envelopes

An authority envelope MAY contain commercially sensitive or personal terms. A conforming implementation MAY provide a derived authorization proof or decision receipt rather than disclose the complete envelope, provided that the relying party can verify:

- the relevant issuer;
- the requested action and context were evaluated;
- required constraints were applied;
- the authority was current; and
- the decision can be audited by an authorized party.

## 30.6 Confidential Execution Evidence

Execution receipts SHOULD avoid embedding raw protected inputs or outputs. They SHOULD use digests, encrypted references, scoped evidence packages, and access-control policies appropriate to the action.

## 30.7 Query Privacy

Registries MUST consider that search and status queries can reveal intent, relationships, or investigations. Profile B, C, and D deployments MUST support authenticated or otherwise policy-bound queries for non-public data, query minimization, rate controls, and auditable access. Unauthenticated discovery MUST expose only records explicitly classified for public disclosure. Bulk enumeration, status probing, and search telemetry MUST be treated as privacy-sensitive access surfaces.

## 30.8 Correlation and Graph Reconstruction

Persistent public relationship graphs can reveal organizational structure, beneficiaries, suppliers, or personal associations. Deployments MUST assess whether each relationship must be public, ecosystem-visible, pairwise, or confidential, and MUST record the selected disclosure class in deployment policy when the relationship can reveal a natural person, beneficiary, commercially sensitive association, or security-relevant topology.

## 30.9 Data Subject and Affected-Party Rights

Governance profiles for Profile B, C, and D deployments MUST define rights to access, correction, annotation, restriction, and appeal where records or decisions can materially affect a person or organization. Correction MUST preserve necessary audit history without continuing to present incorrect data as current.

## 30.10 Privacy Pattern Declaration

A conforming deployment SHOULD publish which privacy patterns it supports:

- public record;
- public pointer and protected record;
- selective attribute disclosure;
- pairwise identifier;
- confidential authority envelope;
- confidential evidence package;
- privacy-preserving status; and
- protected point-in-time reconstruction.

---



## ARPA-HARDENING §9 — Pairwise identity and continuity

<!-- consolidated-source: ARPA-HARDENING §9 -->

A deployment claiming both privacy-preserving scoped identifiers and cross-context continuity MUST define an authorized mechanism for proving the required continuity predicate without exposing a globally reusable correlator.

The mechanism MAY use protected linkage, selective disclosure, commitments, derived pseudonyms, or another governed proof technique. The specification does not mandate a proof construction.

A relying party MUST NOT infer that two pairwise identifiers represent the same logical agent merely from similarity, metadata correlation, operator identity, or network endpoint overlap.


# 31. Scalability and Availability

## 31.1 Federated Architecture

A scalable deployment SHOULD use federated registries with globally resolvable identifiers and locally governed participation.

## 31.2 Tiered Storage

Implementations SHOULD use storage appropriate to data type:

| Layer | Recommended Data |
| --- | --- |
| Immutable log or transparency layer | Critical identifiers, hashes, status transitions, governance checkpoints |
| Authoritative registry database | Current structured records and relationships |
| Content-addressed storage | Descriptions, schemas, policy bundles, evidence manifests |
| Operational telemetry store | Health, attestation, monitoring data |
| Confidential evidence store | Detailed audit and execution evidence |
| Search index | Discovery and taxonomy-based search |

## 31.3 Read Scalability

Read traffic MAY be served through replicated projections if freshness and provenance requirements are met.

## 31.4 Write Serialization

Implementations MUST define conflict resolution and serialization rules for concurrent updates.

## 31.5 Partition Behavior

A deployment MUST document behavior during network partition, including:

- whether reads continue;
- whether writes continue;
- whether authority decisions fail closed or fail open;
- which statuses are considered safe;
- how reconciliation occurs; and
- how conflicting events are handled.

High-assurance profiles SHOULD fail closed for stale or unavailable authority status.

## 31.6 Pagination

List and search endpoints MUST use bounded pagination.

## 31.7 Bulk Status

Registries SHOULD support bulk status resolution for large relying systems.

## 31.8 Event Scalability

Event systems SHOULD support:

- partitioned topics;
- resumable cursors;
- filtering;
- compaction;
- replay;
- signed checkpoints; and
- subscriber-specific authorization.

---

# 32. Audit and Transparency

## 32.1 Audit Log

A registry MUST maintain tamper-evident audit records for:

- registrations;
- updates;
- control changes;
- key changes;
- delegation issuance and revocation;
- assurance issuance and revocation;
- lifecycle transitions;
- governance decisions;
- recognition changes;
- administrative access;
- evidence access;
- policy changes; and
- recovery operations.

## 32.2 Transparency

Public or ecosystem-level transparency SHOULD include:

- registry policy;
- supported profiles;
- governance authority;
- operator identity;
- audit scope;
- incident statistics;
- suspension and revocation statistics;
- appeal statistics;
- recognition relationships;
- service availability;
- index lag targets;
- revocation propagation targets; and
- material policy changes.

## 32.3 Confidential Audit

Sensitive details MAY be restricted, but independent auditors SHOULD be able to verify required controls.

## 32.4 Checkpoints

A registry SHOULD publish signed checkpoints or equivalent integrity commitments.

---

# 33. Versioning and Extensibility

## 33.1 Specification Version

Every response and record MUST identify the supported specification or schema version.

The record envelope's `schema_version` (§13.1) identifies the version of the per-record-type JSON Schema under `schemas/` and follows its own semantic-versioning track, independent of this document's `Version` header (§ front matter). The two tracks are related as follows: a document major or minor version MAY be released without changing any `schema_version` (editorial or non-normative change); a `schema_version` MAY advance independently of the document version only for schema-level corrections that do not alter normative record semantics (for example, tightening a pattern already implied by prose). Any change to a record's required fields or field semantics MUST be reflected in both the document's Change Log (Appendix H) and a corresponding `schema_version` bump, and the mapping between document version and the `schema_version` values it corresponds to MUST be recorded in `schemas/README.md`. The Candidate Specification v0.9.0 uses the `1.0.0` record schema track unless an individual schema declares a later compatible schema version; the authoritative mapping is maintained in `schemas/README.md` and validated by the repository conformance checks.

## 33.2 Backward Compatibility

Minor versions SHOULD preserve backward compatibility.

Material semantic changes MUST require a new major version.

## 33.3 Deprecation

Deprecated fields or endpoints MUST have:

- deprecation notice;
- replacement;
- migration guidance;
- sunset date; and
- compatibility behavior.

## 33.4 Extension Registry

Communities SHOULD maintain extension registries identifying:

- namespace;
- owner;
- schema;
- criticality;
- version;
- status;
- security considerations; and
- interoperability notes.

## 33.5 Unknown Fields

Unknown non-critical fields MAY be ignored but MUST be preserved where records are relayed or reserialized, unless prohibited by policy.

---



## ARPA-HARDENING §10 — Schema corrections and authority

<!-- consolidated-source: ARPA-HARDENING §10 -->

A schema-only correction MUST NOT acquire de facto normative authority by changing the set of accepted records contrary to published prose.

A schema version MAY advance without a Candidate document version change only when all of the following are true:

- the prior machine-readable artifact is demonstrably defective;
- the governing prose already unambiguously requires the corrected behavior;
- the defect, rationale, and compatibility impact are recorded;
- the correction does not broaden authority or weaken fail-safe processing; and
- repository conformance evidence demonstrates alignment.

If a proposed schema change alters required fields, field semantics, authority interpretation, lifecycle semantics, decision behavior, or the set of records that the prose permits, the Candidate Specification MUST be versioned accordingly.



## ARPA-CAND-PP-01 §4 — Critical extensions and version handling

<!-- consolidated-source: ARPA-CAND-PP-01 §4 -->

Every ARPA extension that can change interpretation of core identity, authority, lifecycle, evidence, proof, recognition or decision semantics MUST declare whether it is critical to processing.

A critical extension MUST identify a namespace and version sufficient for an implementation to determine whether it understands the required semantics.

If a receiver does not understand or support a critical extension that is material to the requested operation, it MUST return a non-affirmative result or protocol error. It MUST NOT ignore the extension and continue as though the extension were absent.

Unknown non-critical extensions MAY be ignored or retained as opaque data only when doing so cannot change core interpretation, broaden authority, suppress a prohibition, hide a lifecycle restriction or convert unknown/indeterminate state into success.

An extension MUST NOT redefine a core ARPA field in place. A semantic change to a core field requires an applicable ARPA specification version change.

An implementation MUST NOT claim support for an extension version that it cannot process according to the extension's declared semantics.



## ARPA-CAND-PP-03 §1 — Controlled vocabulary coherence

<!-- consolidated-source: ARPA-CAND-PP-03 §1 -->

The Candidate prose remains authoritative for base vocabularies. Controlled registries MAY additionally contain governed extensions and deprecated compatibility aliases, but every such entry MUST declare its class and status so that a validator can distinguish base vocabulary from extensions and migration aliases.

For the base surfaces covered by this specification:

- Candidate §24.2 defines the base event vocabulary;
- Candidate §34.2 defines the base error-code vocabulary;
- Candidate §13.4 defines the base relationship vocabulary;
- Candidate lifecycle registration states are controlled by `registries/lifecycle-statuses.json`;
- governed extension namespaces are controlled by `registries/extension-namespaces.json`.

A base registry entry and its governing JSON Schema MUST NOT disagree. Deprecated aliases MUST identify a replacement where an exact replacement exists. Profile-specific or project-specific extensions MUST be explicitly classified as extensions rather than presented as base Candidate vocabulary.



## ARPA-CAND-PP-03 §8 — Extension namespaces

<!-- consolidated-source: ARPA-CAND-PP-03 §8 -->

Candidate-conformant project namespaces use collision-resistant HTTPS namespace identifiers under project-controlled authority:

`https://qbfconsulting.digital/ns/arpa/`

A deployment MAY define an external extension namespace using another collision-resistant URI/URN/reverse-DNS authority that it controls. The namespace MUST be globally collision-resistant and MUST identify an owner and schema/policy authority.

The former `https://arpa.example/...` identifiers are placeholders only. They are retained in the controlled registry solely as deprecated migration aliases and MUST NOT be used for new conformant extensions.


# 34. Error Handling

## 34.1 Error Envelope

```json
{
  "request_id": "string",
  "error": {
    "code": "ARPA-STATUS-STALE",
    "message": "The requested status exceeds the relying policy's maximum age.",
    "details": {},
    "retryable": true
  },
  "generated_at": "date-time"
}
```

## 34.2 Base Error Codes

Implementations SHOULD support:

- `ARPA-INVALID-REQUEST`;
- `ARPA-UNSUPPORTED-VERSION`;
- `ARPA-UNSUPPORTED-PROFILE`;
- `ARPA-IDENTIFIER-NOT-FOUND`;
- `ARPA-RECORD-NOT-AUTHORIZED`;
- `ARPA-SCHEMA-INVALID`;
- `ARPA-PROOF-INVALID`;
- `ARPA-ISSUER-NOT-AUTHORIZED`;
- `ARPA-STATE-TRANSITION-INVALID`;
- `ARPA-STATUS-STALE`;
- `ARPA-AUTHORITY-EXPIRED`;
- `ARPA-AUTHORITY-REVOKED`;
- `ARPA-AUTHORITY-INDETERMINATE`;
- `ARPA-DELEGATION-EXCEEDS-SCOPE`;
- `ARPA-ASSURANCE-EXPIRED`;
- `ARPA-ASSURANCE-NOT-APPLICABLE`;
- `ARPA-RUNTIME-NOT-ATTESTED`;
- `ARPA-POLICY-DENIED`;
- `ARPA-FEDERATION-NOT-RECOGNIZED`;
- `ARPA-CONFLICTING-STATUS`;
- `ARPA-PROJECTION-LAG`;
- `ARPA-RATE-LIMITED`;
- `ARPA-TEMPORARILY-UNAVAILABLE`; and
- `ARPA-INTERNAL-ERROR`.

## 34.3 HTTP Status Code Mapping

Implementations exposing an HTTP transport MUST map `ARPA-*` error codes to HTTP status codes as follows. A profile MAY use a different transport, in which case it MUST publish an equivalent mapping.

| Error code | HTTP status |
| --- | --- |
| `ARPA-INVALID-REQUEST` | 400 |
| `ARPA-UNSUPPORTED-VERSION` | 400 |
| `ARPA-UNSUPPORTED-PROFILE` | 400 |
| `ARPA-IDENTIFIER-NOT-FOUND` | 404 |
| `ARPA-RECORD-NOT-AUTHORIZED` | 403 |
| `ARPA-SCHEMA-INVALID` | 422 |
| `ARPA-PROOF-INVALID` | 422 |
| `ARPA-ISSUER-NOT-AUTHORIZED` | 403 |
| `ARPA-STATE-TRANSITION-INVALID` | 409 |
| `ARPA-STATUS-STALE` | 409 |
| `ARPA-AUTHORITY-EXPIRED` | 403 |
| `ARPA-AUTHORITY-REVOKED` | 403 |
| `ARPA-AUTHORITY-INDETERMINATE` | 409 |
| `ARPA-DELEGATION-EXCEEDS-SCOPE` | 403 |
| `ARPA-ASSURANCE-EXPIRED` | 403 |
| `ARPA-ASSURANCE-NOT-APPLICABLE` | 403 |
| `ARPA-RUNTIME-NOT-ATTESTED` | 403 |
| `ARPA-POLICY-DENIED` | 403 |
| `ARPA-FEDERATION-NOT-RECOGNIZED` | 403 |
| `ARPA-CONFLICTING-STATUS` | 409 |
| `ARPA-PROJECTION-LAG` | 409 |
| `ARPA-RATE-LIMITED` | 429 |
| `ARPA-TEMPORARILY-UNAVAILABLE` | 503 |
| `ARPA-INTERNAL-ERROR` | 500 |

A `retryable: true` error SHOULD be paired with a `Retry-After` header where the status is 429 or 503.

## 34.4 Indeterminate Results

An indeterminate result MUST explain which required inputs, records, or verifications were unavailable or conflicting.

---



## ARPA-CAND-PP-01 §3 — HTTP Problem Details contract

<!-- consolidated-source: ARPA-CAND-PP-01 §3 -->

An ARPA HTTP API MUST represent protocol-significant errors using RFC 9457 Problem Details unless a governing transport profile defines another interoperable error representation.

An ARPA Problem Details response for a protocol-significant failure MUST contain:

- `type`, identifying a stable problem type URI;
- `title`, as human-readable non-normative text;
- `status`, containing the applicable HTTP status code; and
- `code`, containing a stable ARPA error code.

Human-readable `title` and `detail` values MUST NOT be the sole machine contract for client behaviour.

Problem extensions such as reason codes, correlation identifiers and retry metadata MAY be included when applicable. They MUST NOT expose confidential evidence, hidden authority relationships, internal exception details or security-sensitive implementation state beyond the caller's authorization.

A client that does not recognize an ARPA error code or Problem Details extension MUST NOT interpret the response as success. Unknown error semantics affecting authority, integrity, lifecycle or reconstruction MUST remain non-affirmative.

A server MUST NOT mark a failure `retryable=true` unless replay of the same operation under the documented retry conditions is safe with respect to duplicate authoritative state and external side effects.



## ARPA-CAND-PP-03 §6 — RFC 9457 Problem Details

<!-- consolidated-source: ARPA-CAND-PP-03 §6 -->

Protocol-significant HTTP failures use RFC 9457 Problem Details extended by the ARPA fields defined in `schemas/problem-details.schema.json`.

The stable ARPA error code is carried in `code`. The `type` URI for a registered code is:

`https://qbfconsulting.digital/problems/arpa/{code}`

where `{code}` is the exact registered ARPA code.

Unknown material error semantics MUST fail safely. A client MUST NOT reinterpret an unknown material error as success.


# 35. Conformance Profiles

## 35.1 Profile A: Discovery Registry

Suitable for low-risk informational agents.

Required features:

- persistent identifier;
- core record;
- controller or operator relationship;
- description record;
- endpoint records;
- key binding;
- lifecycle status;
- historical resolution;
- basic query interface;
- freshness metadata; and
- governance reference.

## 35.2 Profile B: Accountable Agent Registry

Suitable for agents that access protected data, produce consequential recommendations, or modify workflows.

Includes Profile A plus:

- typed accountability relationships;
- agent versions;
- deployment identifiers;
- assurance claims;
- structured capabilities;
- incident state;
- suspension and restriction;
- point-in-time resolution;
- execution receipts for consequential actions;
- redress metadata; and
- event subscriptions.

## 35.3 Profile C: Delegated Authority Registry

Suitable for agents that transact, commit resources, exercise delegated permissions, or act for principals.

Includes Profile B plus:

- authority envelopes;
- delegation chains;
- authority evaluation;
- decision receipts;
- runtime enforcement integration;
- cascade revocation;
- approval conditions;
- quantitative limits;
- non-delegation controls;
- enforcement acknowledgement; and
- maximum revocation propagation time.

## 35.4 Profile D: High-Assurance or Fiduciary Registry

Suitable for public services, healthcare, finance, legal services, identity-affecting systems, or fiduciary contexts.

Includes Profile C plus:

- identified accountable institution;
- beneficiary and duty metadata;
- explicit prohibitions;
- independent assurance;
- runtime attestation;
- separated administrative keys;
- threshold control;
- continuous monitoring;
- emergency suspension;
- multi-party governance;
- transparency reporting;
- independent appeal;
- evidence retention;
- essential-service continuity;
- periodic control testing; and
- externally auditable enforcement.

## 35.5 Profile Declaration

A registry MUST publicly declare:

- supported profiles;
- supported optional features;
- unsupported requirements;
- cryptographic suites;
- identifier schemes;
- query transports;
- event delivery semantics;
- status freshness targets;
- revocation propagation targets; and
- audit scope.

---

# 36. Conformance Requirements

> **Candidate controls:** ARPA-CAND-009 and ARPA-CAND-010. Each implementation MUST publish a capability declaration, conformance targets, deviations, evidence references, and the exact specification and profile versions evaluated.

## 36.1 Minimum Components

A conforming deployment MUST provide:

- authoritative record store;
- resolver;
- lifecycle status service;
- governance metadata;
- proof verification;
- audit log;
- conformance declaration; and
- security and incident process.

## 36.2 Higher-Profile Components

Profiles B through D progressively require:

- relationship registry;
- assurance service;
- authority service;
- event service;
- evidence service;
- policy decision point;
- enforcement integration;
- appeal service; and
- federation service.

## 36.3 Administrative API

Administrative operations MUST be authenticated, authorized, audited, and policy-constrained.

## 36.4 Idempotency

Create and update operations SHOULD support idempotency keys.

## 36.5 Optimistic Concurrency

Updates SHOULD require an expected version, sequence, or checkpoint to prevent lost updates.

## 36.6 Validation

Registries MUST validate:

- schema;
- signatures or proofs;
- issuer authorization;
- lifecycle transition legality;
- time validity;
- namespace authorization;
- relationship type;
- delegation narrowing;
- extension criticality; and
- governance compatibility.

## 36.7 Fail-Safe Defaults

An implementation MUST NOT produce `allow` or `allow_with_conditions` when any authority, status, assurance, recognition, or governance input required by the applicable profile is stale, unavailable, conflicting, unsupported, unverifiable, or indeterminate, unless the governing relying-party policy explicitly classifies that input as non-material for the requested action. Profiles C and D MUST treat unresolved material inputs as `deny` or `indeterminate`; they MUST NOT fail open.

## 36.8 Observability

Registry operators MUST monitor:

- query availability;
- write availability;
- index lag;
- event lag;
- proof-verification failure;
- stale status;
- policy evaluation errors;
- revocation propagation;
- enforcement acknowledgement;
- abnormal update patterns; and
- federation failures.


## 36.9 Operational Resilience Assurance

Operational resilience is a cross-cutting conformance property and does not define a new Profile A-D tier. A deployment that makes a production or operational-conformance claim MUST publish an Operational Resilience Declaration identifying the applicable failure domains, controls, bounds, verification procedures, evidence references, and known limitations. The declaration MUST conform to `schemas/operational-resilience-declaration.schema.json`.

The requirements in this section constrain observable safety properties. They do not mandate a particular service mesh, queue, cache, retry library, load balancer, database, or deployment platform.

### 36.9.1 Failure domains and retry ownership

A deployment MUST identify the failure domains in which protocol operations can be retried, including application, client library, gateway or proxy, registry service, federation hop, event transport, and downstream dependency layers where those layers are present.

For each failure domain, the deployment MUST identify a retry owner and MUST enforce an aggregate retry budget. Multiple components MUST NOT independently retry the same consequential operation unless they participate in and enforce the same aggregate retry budget.

Retries of the same consequential create, update, delegation, revocation, suspension, recognition, recovery, or administrative operation MUST preserve a stable operation identity and, where idempotency is supported, the same idempotency identity across retrying intermediaries.

A retry policy MUST declare the maximum attempt count or equivalent work bound, maximum retry horizon, retryable failure classes, treatment of server retry hints, and terminal-failure behaviour. Clients and intermediaries SHOULD honor `Retry-After` when supplied for retryable `429` or `503` outcomes.

### 36.9.2 Partial outage, failover, and recovery

A deployment using failover MUST declare endpoint health states and the criteria governing transitions between healthy, degraded, unavailable, and recovering states. A recovering endpoint MUST NOT be restored to unrestricted traffic solely on the basis of a single successful health observation when doing so can create oscillation or overload.

Failover behaviour MUST bound fan-out and MUST remain within the aggregate retry budgets defined by Section 36.9.1. During reduced capacity, an operator MUST provide admission control, load shedding, or an equivalent bounded-work mechanism sufficient to prevent surviving endpoints from being driven into cascading failure.

Rejected, deferred, or shed consequential work MUST be observable. Recovery criteria MUST include a stabilization or hysteresis condition sufficient to prevent repeated traffic oscillation between unhealthy and recovering paths.

### 36.9.3 Event isolation and acknowledgement safety

An event-capable deployment MUST declare the scope within which ordering is guaranteed. Ordering semantics MUST NOT create an indefinite dependency between consequentially unrelated authority-state changes.

A malformed, poison, or repeatedly failing event MUST be isolatable or quarantinable such that it cannot indefinitely prevent unrelated revocation, suspension, recognition, recovery, or other authority-state events from progressing.

Where loss of an event could affect effective authority, revocation, suspension, recognition, or recovery state, upstream acknowledgement MUST occur only after the event has crossed a declared durable-handoff boundary from which processing is recoverable after consumer or process failure.

Skipped, quarantined, or dead-lettered consequential events MUST be observable and MUST have a documented recovery or disposition path.

### 36.9.4 Dependency amplification and cache safety

A deployment that caches authoritative lookup or resolution results MUST bound amplification caused by concurrent cache misses. Request coalescing, bounded concurrency, batching, replicated state, admission control, or another mechanism MAY be used to satisfy this requirement.

Dependency retries MUST use bounded backoff and SHOULD include desynchronization or jitter where synchronized clients could otherwise create a retry wave.

Negative caching MAY be used only where the deployment can demonstrate that the cached negative outcome does not conceal a material state transition. Resilience caching MUST NOT extend authority, revocation, suspension, recognition, assurance, or lifecycle information beyond its applicable freshness, validity, or policy boundary.

Deployments serving synchronized fleets SHOULD desynchronize cache expiry or refresh activity where common expiration points could create a thundering-herd condition.

### 36.9.5 Sustained-load progress and fairness

Sustained load from one principal, tenant, federation peer, operation class, or failure domain MUST NOT indefinitely prevent consequential control-plane operations from making progress.

A deployment MUST define and test a mechanism that preserves bounded progress for revocation, suspension, recovery, incident containment, authority-state updates, and other locally designated safety-critical operations during query or discovery saturation.

### 36.9.6 Required assurance evidence

An operational-resilience evidence bundle MUST identify, at minimum:

- the failure-domain map;
- retry owners and aggregate retry budgets;
- retry horizon and server-hint handling;
- health-state transition and recovery criteria;
- failover and reduced-capacity controls;
- event ordering scope, quarantine behaviour, and durable acknowledgement boundary;
- dependency amplification controls and cache-freshness constraints;
- sustained-load progress controls;
- the conformance vectors executed; and
- known limitations or deployment-specific exclusions.

The repository conformance suite defines portable vectors for lost responses, nested retries, partial outages, recovery flapping, event head-of-line isolation, durable acknowledgement, dependency amplification, and safety-critical progress under load. Passing these repository fixtures demonstrates conformance to the modeled scenarios only; it MUST NOT be represented as proof of production resilience or independent certification.

---



## ARPA-CAND-PP-01 §5 — Cross-artifact consistency

<!-- consolidated-source: ARPA-CAND-PP-01 §5 -->

The Candidate Specification remains the authoritative prose surface. Machine-readable contracts MUST remain consistent with the governing normative semantics.

For the semantics in this specification:

- OpenAPI Agent Identifier parameters MUST constrain ARPA Agent Identifiers to `agentreg:`;
- historical-resolution schemas/contracts MUST expose requested-time and reconstruction semantics;
- the ARPA error registry MUST contain stable codes for protocol-significant failures used by conformance tests; and
- the extension/error surfaces MUST include an explicit unknown-critical-extension failure condition.

A release validation gate MUST fail when these machine-readable surfaces contradict this specification.


# 37. Test Vectors and Interoperability Testing

## 37.1 Required Test Categories

A conformance suite MUST include positive and negative tests for:

- record parsing and proof validation;
- issuer competence;
- legal and illegal lifecycle transitions;
- version and deployment binding;
- delegation narrowing;
- prohibition inheritance;
- approval conditions;
- expiry and clock boundaries;
- upstream and cascade revocation;
- stale projection rejection;
- point-in-time reconstruction;
- conflicting recognized status;
- material change effects;
- event replay and deduplication;
- restoration after appeal;
- unknown critical extensions; and
- privacy-protected record resolution.

## 37.2 Interoperability Matrix

Implementors SHOULD test resolver-to-resolver, resolver-to-PDP, PDP-to-PEP, registry-to-index, registry-to-event-subscriber, and registry-to-federation-peer behavior.

## 37.3 Determinism

Given the same authenticated records, context, and policy version, conforming evaluators SHOULD produce the same decision and reason-code set. Differences caused by local policy MUST be explicitly attributable to the policy identifier.

## 37.4 Test Fixtures

Test fixtures SHOULD include complete record graphs rather than isolated JSON objects. At minimum, a fixture for delegated action should include an agent, version, deployment, relationships, assurance, parent and child delegations, status, policy, and expected decision receipt.

---



## ARPA-HARDENING §11 — Required adversarial conformance assertions

<!-- consolidated-source: ARPA-HARDENING §11 -->

A v0.9.1 conformance suite for authority evaluation MUST include negative or boundary vectors covering at least:

1. omitted parent constraint;
2. incomparable scope vocabularies;
3. exact expiry boundary;
4. unordered contradictory events at the same timestamp;
5. future-dated material status outside permitted skew;
6. authoritative revocation with pending enforcement convergence;
7. conflicting equally competent authoritative sources;
8. stale affirmative projection versus fresh negative authoritative state;
9. unknown critical extension;
10. proof-valid but incompetent issuer;
11. assurance bound to a different deployment;
12. material change after assurance;
13. pairwise identifier continuity without an authorized linkage proof;
14. unavailable historical evidence;
15. retroactive revocation with and without a competent governance basis;
16. missing delegation incorrectly proposed as `not_applicable`;
17. permissive and restrictive recognized sources with unresolved competence conflict;
18. child delegation dropping an upstream prohibition;
19. child delegation changing to an incomparable constraint vocabulary; and
20. replay of a decision or execution receipt after a material authority boundary changes.

Each adversarial vector MUST identify the expected decision or state, required reason codes, decisions that are prohibited, and the evidence required to explain the result.



## ARPA-HARDENING §12 — Conformance disposition

<!-- consolidated-source: ARPA-HARDENING §12 -->

An implementation claiming ARPA v0.9.1 authority-evaluator conformance MUST demonstrate that ambiguous or incomplete authority cannot become affirmative solely through omission, parser behavior, precedence defaults, cache behavior, unavailable evidence, or unsupported semantics.

Passing the repository adversarial vectors demonstrates conformance to the modeled cases only. It is not independent certification, formal verification, or proof that an implementation is secure against every adversarial input.



## ARPA-CAND-PP-03 §9 — Conformance automation

<!-- consolidated-source: ARPA-CAND-PP-03 §9 -->

Repository validation MUST fail when:

- base event registry and event-schema vocabularies drift;
- base relationship registry and relationship-schema vocabularies drift;
- lifecycle registration states and status-schema registration values drift;
- Candidate base error codes are absent from the controlled registry;
- a registered ARPA Problem Details code is not machine representable;
- `not_applicable` is accepted without reason semantics or for a prohibited failure case;
- PP-03 time-boundary vectors are absent or inconsistent;
- collective-principal churn vectors omit snapshot binding;
- a delegated-envelope example used by PP-03 lacks parent linkage;
- placeholder extension namespaces are marked active; or
- the OpenAPI authority-evaluation and Problem Details surfaces are not schema-bound.


# 38. Deployment Patterns

## 38.1 Centralized Authoritative Registry

A single operator maintains authoritative records and exposes replicated read services. This pattern is simple to operate but requires strong audit, role separation, recovery, and governance safeguards.

## 38.2 Consortium Registry

Multiple institutions jointly govern admission or critical state transitions. Threshold authorization and shared transparency mechanisms can reduce unilateral control, while governance complexity and availability requirements increase.

## 38.3 Ledger- or Transparency-Backed Registry

Critical events and commitments are recorded in an append-only verifiable system, while structured records and protected evidence remain off the log. This pattern can improve equivocation detection without forcing all data into a public ledger.

## 38.4 Federated Domain Registries

Domain-specific registries retain local governance and exchange records through explicit recognition. This is the RECOMMENDED pattern for cross-sector or cross-jurisdiction deployment because global resolution does not require global governance.

## 38.5 Enterprise Private Registry

An organization operates a registry for internal agents and selectively exposes externally relevant identity, assurance, or authority records. Private deployment does not remove the need for typed relationships, lifecycle history, or enforcement integration.

## 38.6 Hybrid Public-Private Registry

Public identity, governance, status commitments, and endpoints are combined with protected delegation, assurance evidence, and execution records. This pattern supports accountability while limiting disclosure.

## 38.7 Profile Examples

| Profile | Representative Deployment |
| --- | --- |
| A | Public directory of low-risk research agents |
| B | Enterprise registry for data-access and workflow agents |
| C | Procurement network with bounded transactional delegation |
| D | Public-service, healthcare, financial, legal, or fiduciary agent infrastructure |

---

# 39. Operational Guidance

## 39.1 Recommended Service Decomposition

A production deployment SHOULD consider separate services for:

- identity and record management;
- relationship management;
- delegation and authority;
- assurance;
- status;
- search and indexing;
- event publication;
- evidence storage;
- governance and appeals;
- policy evaluation;
- federation; and
- audit.

## 39.2 Deployment Modes

Supported modes MAY include:

- centralized authoritative registry;
- replicated registry;
- consortium registry;
- ledger-backed registry;
- transparency-log-backed registry;
- federated registry network; and
- hybrid public-private registry.

## 39.3 Registry Operator Separation

High-assurance deployments SHOULD separate the registry operator from at least one of:

- governance authority;
- assurance provider;
- appeal authority;
- evidence auditor; or
- transparency witness.

## 39.4 Operational Runbooks

Operators MUST maintain runbooks for:

- key compromise;
- false registration;
- unauthorized transfer;
- stale projection;
- event delivery failure;
- authority revocation;
- assurance invalidation;
- data breach;
- federation conflict;
- governance emergency;
- recovery; and
- public communication.

## 39.5 Service-Level Objectives

Registries SHOULD publish objectives for:

- query availability;
- write availability;
- status freshness;
- event latency;
- revocation propagation;
- incident acknowledgement;
- appeal acknowledgement;
- point-in-time resolution; and
- evidence retrieval.

## 39.6 Testing

Implementations MUST test:

- legal lifecycle transitions;
- illegal lifecycle transitions;
- delegation narrowing;
- cascade revocation;
- stale-data rejection;
- conflicting status;
- point-in-time resolution;
- key rotation;
- recovery;
- extension handling;
- event replay;
- projection reconciliation;
- federation withdrawal; and
- appeal restoration.

---

# 39A. Informative ARPA–TRQP Query Projection

This section is informative. It documents an interoperability boundary for architects and designers; it does not modify the normative core of ARPA or the Trust Registry Query Protocol (TRQP).

## 39A.1 Layering

ARPA governs the creation, evaluation, lifecycle, evidence, revocation, enforcement, federation, and redress of agent authority state. TRQP is treated as an external read-only query interface capable of exposing selected authorization and recognition answers derived from authoritative state.

```text
ARPA authority-control plane
        |
        v
Governed query projection
        |
        v
TRQP authorization or recognition response
```

ARPA conformance does not imply TRQP conformance. TRQP conformance does not imply ARPA conformance. Projection support MUST be separately versioned and declared under ARPA-CAND-011.

## 39A.2 Projection safety

A projection adapter MUST preserve action, resource, context, validity, recognition scope, prohibitions, and evidence provenance. It MUST NOT broaden delegated or recognized scope, infer transitive recognition, equate technical federation with governance recognition, or convert missing, stale, conflicting, suspended, revoked, expired, or unavailable authority into an affirmative result.

The detailed, machine-verifiable mapping is defined by `mappings/trqp-arpa-query-projection.yaml`. The architecture rationale, information-loss analysis, and sequence diagrams are defined by `docs/architecture/trqp-arpa-interoperability.md`.

## 39A.3 Lifecycle ownership

ARPA owns the operations and evidence through which authority state changes. A TRQP projection queries the resulting state; it is not an ARPA lifecycle API and does not add write operations to TRQP. Discovery metadata for a projection endpoint is an optional ARPA interoperability declaration and MUST NOT be presented as a mandatory registry-of-registries mechanism.

# 40. Open Issues

The following topics require further community specification and implementation feedback:

1. canonical default identifier method;
2. mandatory proof suites and canonicalization;
3. standard capability taxonomies;
4. assurance-control catalogs and assessor accreditation;
5. selective-disclosure and privacy-preserving status formats;
6. interoperable policy languages;
7. execution and decision receipt proof formats;
8. federation discovery and recognition exchange;
9. revocation acknowledgement across heterogeneous enforcement points;
10. conflict resolution across governance domains;
11. self-modifying and continuously learning agents;
12. ephemeral sub-agents and agent swarms;
13. shared runtimes and multi-tenant isolation;
14. model-provider and tool-provider accountability;
15. liability, indemnity, insurance, and bonding metadata;
16. jurisdictional conflict and mandatory local rules;
17. evidentiary admissibility and long-term verification;
18. post-quantum migration;
19. emergency governance abuse prevention;
20. measurement of effective revocation convergence; and
21. interoperability with sector-specific registries and trust infrastructures.

---

# 41. IANA Considerations

This document requests future registration, if standardized, of:

- the `agentreg` URI scheme;
- the `application/agent-registry+json` media type;
- a registry of Agent Registry record types;
- a registry of Agent Registry event types;
- a registry of lifecycle reason codes;
- a registry of conformance profile identifiers; and
- a registry of extension namespaces.

This draft does not make an immediate IANA request.

---

# Appendix A. Example Records

## A.1 Agent Core Record

```json
{
  "record_id": "record-agent-123",
  "record_type": "agent_core",
  "schema_version": "1.0.0",
  "issuer": "registry:example.org",
  "subject": "agentreg:example.org:agent-123",
  "issued_at": "2026-07-15T00:00:00Z",
  "effective_from": "2026-07-15T00:00:00Z",
  "effective_until": null,
  "status": "active",
  "agent_id": "agentreg:example.org:agent-123",
  "name": "Procurement Review Agent",
  "agent_class": "delegated_transactional_agent",
  "current_version": "agent-version-2.4.1",
  "controllers": ["relationship-controller-1"],
  "operators": ["relationship-operator-1"],
  "accountable_entities": ["relationship-accountable-1"],
  "description": "record-description-1",
  "service_endpoints": ["endpoint-1"],
  "keys": ["key-binding-runtime-1", "key-binding-admin-1"],
  "lineage": {
    "predecessors": ["agentreg:example.org:agent-100"],
    "successors": []
  },
  "governance": ["governance-financial-agent-1"],
  "proof": {
    "type": "ExampleSignature2026",
    "verification_method": "registry:example.org#signing-key-1",
    "created": "2026-07-15T00:00:00Z",
    "value": "..."
  }
}
```

## A.2 Relationship Record

```json
{
  "record_id": "relationship-accountable-1",
  "record_type": "relationship",
  "schema_version": "1.0.0",
  "issuer": "registry:example.org",
  "subject": "agentreg:example.org:agent-123",
  "issued_at": "2026-07-15T00:00:00Z",
  "effective_from": "2026-07-15T00:00:00Z",
  "effective_until": null,
  "status": "active",
  "relationship_type": "accountable_to",
  "related_entity": "org:example:procurement-services",
  "scope": {
    "actions": ["purchase.prepare", "purchase.submit"],
    "jurisdictions": ["IN"]
  },
  "authority_source": "governance-financial-agent-1",
  "revocation": {
    "status_endpoint": "https://registry.example.org/records/relationship-accountable-1/status"
  },
  "proof": {}
}
```

## A.3 Authority Envelope

```json
{
  "record_id": "authority-789",
  "record_type": "authority_envelope",
  "schema_version": "1.0.0",
  "issuer": "did:example:principal",
  "subject": {
    "principal": "did:example:principal",
    "agent": "agentreg:example.org:agent-123"
  },
  "issued_at": "2026-07-15T00:00:00Z",
  "effective_from": "2026-07-15T00:00:00Z",
  "effective_until": "2026-08-15T00:00:00Z",
  "status": "active",
  "action_classes": [
    "purchase.prepare",
    "purchase.submit"
  ],
  "resource_scope": [
    "account:procurement:regional"
  ],
  "purpose_scope": [
    "approved-supplier-procurement"
  ],
  "jurisdiction_scope": ["IN"],
  "limits": {
    "currency": "INR",
    "per_transaction": 50000,
    "aggregate": 250000
  },
  "required_approvals": [
    {
      "condition": "amount > 25000",
      "approval": "human-procurement-owner"
    }
  ],
  "prohibitions": [
    "related-party-transactions",
    "supplier-bank-detail-changes"
  ],
  "delegation_mode": "non_delegable",
  "evidence_policy": "evidence-policy-procurement-1",
  "revocation": {
    "status_endpoint": "https://authority.example.org/authority-789/status",
    "cascade": "all_downstream"
  },
  "governance": [
    "governance-procurement-1"
  ],
  "redress_profile": "redress-procurement-1",
  "proof": {}
}
```

## A.4 Assurance Claim

```json
{
  "record_id": "assurance-456",
  "record_type": "assurance_claim",
  "schema_version": "1.0.0",
  "issuer": "assurance-provider:example.net",
  "subject": {
    "agent_id": "agentreg:example.org:agent-123",
    "version": "agent-version-2.4.1",
    "artifact_digest": "sha256:...",
    "deployment_profile": "prod-in-1"
  },
  "issued_at": "2026-07-10T00:00:00Z",
  "effective_from": "2026-07-10T00:00:00Z",
  "effective_until": "2026-10-10T00:00:00Z",
  "status": "valid",
  "profile": "high-assurance-procurement-agent",
  "control_results": [
    {
      "control_id": "AUTH-001",
      "result": "pass",
      "evidence_ref": "evidence-auth-001"
    },
    {
      "control_id": "REV-004",
      "result": "pass",
      "evidence_ref": "evidence-rev-004"
    }
  ],
  "limitations": [
    "excludes-autonomous-bank-detail-modification"
  ],
  "proof": {}
}
```

## A.5 Multi-Dimensional Status

```json
{
  "agent_id": "agentreg:example.org:agent-123",
  "registration": "active",
  "operation": "restricted",
  "authority": "valid",
  "assurance": "conditional",
  "security": "elevated_monitoring",
  "effective_at": "2026-07-15T10:00:00Z",
  "observed_at": "2026-07-15T10:00:05Z",
  "valid_until": "2026-07-15T10:05:05Z",
  "restrictions": [
    "no_transaction_submission"
  ],
  "source": "registry:example.org",
  "appeal_available": true,
  "proof": {}
}
```

---

# Appendix B. Example Queries and Negative Outcomes

## B.1 Authority Evaluation Request

```http
POST /authority/evaluate
Content-Type: application/agent-registry+json
```

```json
{
  "agent": "agentreg:example.org:agent-123",
  "principal": "did:example:principal",
  "action": "purchase.submit",
  "resource": "procurement:order:456",
  "purpose": "approved-supplier-procurement",
  "amount": {
    "currency": "INR",
    "value": 42000
  },
  "jurisdiction": "IN",
  "time": "2026-07-15T10:00:00Z",
  "deployment": "deployment-prod-in-1"
}
```

## B.2 Authority Evaluation Response

```json
{
  "request_id": "request-123",
  "result_status": "success",
  "result": {
    "decision": "allow_with_conditions",
    "authority_reference": "authority-789",
    "required_conditions": [
      {
        "type": "approval",
        "value": "human-procurement-owner"
      }
    ],
    "valid_until": "2026-07-15T10:05:00Z",
    "decision_receipt": "decision-receipt-987"
  },
  "authoritative": true,
  "source": {
    "registry": "authority.example.org",
    "checkpoint": "checkpoint-1123",
    "source_time": "2026-07-15T10:00:00Z"
  },
  "projection": {
    "used": false,
    "updated_at": null,
    "lag_seconds": 0
  },
  "generated_at": "2026-07-15T10:00:01Z",
  "valid_until": "2026-07-15T10:05:00Z",
  "warnings": []
}
```

## B.3 Reliance Evaluation Request

```json
{
  "agent": "agentreg:example.org:agent-123",
  "intended_action": "purchase.submit",
  "required_assurance_profiles": [
    "high-assurance-procurement-agent"
  ],
  "accepted_governance_authorities": [
    "governance:example.org"
  ],
  "maximum_status_age_seconds": 60,
  "required_jurisdictions": ["IN"],
  "runtime_attestation_required": true,
  "incident_policy": "deny_on_confirmed_compromise",
  "delegation_required": true,
  "relying_policy": "policy:buyer.example:procurement-v3"
}
```

## B.4 Discovery Search Request

```json
{
  "capabilities": ["purchase.prepare"],
  "assurance_profiles": ["accountable-agent"],
  "jurisdictions": ["IN"],
  "operational_status": ["available", "restricted"],
  "security_status": ["normal", "elevated_monitoring"],
  "protocols": ["https"],
  "limit": 25,
  "cursor": null
}
```

---

# Appendix C. Reference State Machines

## C.1 Registration State Machine

```text
provisioned
    |
    v
pending_assurance
    |
    +--------------------+
    |                    |
    v                    v
 active              restricted
    |                    |
    +----------+---------+
               |
               v
           suspended
               |
        +------+------+
        |             |
        v             v
   quarantined   under_investigation
        |             |
        +------+------+
               |
        +------+------+
        |             |
        v             v
   compromised      active
        |
        v
      revoked

active ----------> retired
active ----------> superseded
restricted ------> retired
suspended --------> revoked
```

## C.2 Authority State Machine

```text
draft
  |
  v
issued
  |
  v
active
  |
  +----------+-------------+-------------+
  |          |             |             |
  v          v             v             v
restricted suspended     expired       revoked
  |          |
  v          v
active     active
```

## C.3 Assurance State Machine

```text
issued
  |
  v
valid
  |
  +----------+----------+-----------+
  |          |          |           |
  v          v          v           v
conditional expired  suspended   superseded
             |          |
             v          v
          renewed     revoked
```

---

# Appendix D. Conformance Checklist

## D.1 All Profiles

- [ ] Persistent non-reassignable agent identifiers
- [ ] Historical resolution
- [ ] Requested-time and current-state separation
- [ ] Reconstruction-status classification
- [ ] Historical evidence lineage and integrity status
- [ ] Core record
- [ ] Explicit operator or controller relationship
- [ ] Lifecycle state machine
- [ ] Governance metadata
- [ ] Secure query transport
- [ ] Structured errors
- [ ] Provenance and freshness
- [ ] Tamper-evident audit
- [ ] Extension handling
- [ ] Incident process
- [ ] Conformance declaration

## D.2 Profile B

- [ ] Version records
- [ ] Deployment identifiers
- [ ] Accountability relationships
- [ ] Structured capability records
- [ ] Assurance claims
- [ ] Incident states
- [ ] Point-in-time queries
- [ ] Execution receipts
- [ ] Event subscriptions
- [ ] Redress metadata

## D.3 Profile C

- [ ] Authority envelopes
- [ ] Delegation chains
- [ ] Delegation narrowing validation
- [ ] Authority evaluation
- [ ] Decision receipts
- [ ] Runtime enforcement integration
- [ ] Cascade revocation
- [ ] Approval conditions
- [ ] Quantitative limits
- [ ] Revocation propagation target
- [ ] Enforcement acknowledgement

## D.4 Profile D

- [ ] Accountable institution
- [ ] Beneficiary and duty metadata
- [ ] Explicit prohibitions
- [ ] Independent assurance
- [ ] Runtime attestation
- [ ] Key separation
- [ ] Threshold administration
- [ ] Continuous monitoring
- [ ] Emergency suspension
- [ ] Multi-party governance
- [ ] Transparency reporting
- [ ] Independent appeal
- [ ] Evidence retention
- [ ] Essential-service continuity
- [ ] External audit

---

# Appendix E. Threat Model

## E.1 Registration Threats

- fraudulent identity;
- unauthorized agent registration;
- duplicate or deceptive identifiers;
- impersonation;
- fake sponsorship;
- hidden accountable entity.

## E.2 Control Threats

- controller key theft;
- malicious operator;
- unauthorized endpoint change;
- payment diversion;
- recovery abuse;
- operator-controller collusion.

## E.3 Delegation Threats

- overbroad authority;
- delegation replay;
- stale authority;
- unauthorized redelegation;
- scope expansion;
- hidden downstream agents;
- revocation lag;
- conflicting principals.

## E.4 Assurance Threats

- assurance applied to wrong version;
- assurance applied to wrong deployment;
- expired assurance;
- compromised assessor;
- selective disclosure of favorable tests;
- hidden material change;
- misleading “trusted” labels.

## E.5 Runtime Threats

- unregistered deployment;
- runtime substitution;
- model substitution;
- tool substitution;
- policy bypass;
- receipt forgery;
- telemetry suppression;
- compromised enforcement point.

## E.6 Registry Threats

- stale projection;
- equivocation;
- censorship;
- selective availability;
- insider manipulation;
- governance capture;
- log deletion;
- unauthorized correction;
- denial of service.

## E.7 Federation Threats

- malicious peer registry;
- recognition abuse;
- accidental transitive trust;
- conflicting revocation;
- delayed withdrawal;
- schema mismatch;
- jurisdictional conflict.

## E.8 Privacy Threats

- correlation;
- behavioral profiling;
- exposure of principals;
- exposure of beneficiaries;
- disclosure of confidential delegation;
- evidence scraping;
- graph reconstruction.

---

# Appendix F. Privacy Patterns

## F.1 Public Pointer, Protected Record

Publish status, issuer, digest, and access method while keeping the complete record access-controlled.

## F.2 Selective Attribute Proof

Prove a policy-relevant property, such as sufficient authority or assurance, without disclosing the complete source record.

## F.3 Pairwise Identifier

Use a relationship- or domain-specific identifier to reduce cross-context correlation while retaining protected accountability linkage.

## F.4 Confidential Authority Evaluation

Return a signed decision receipt showing that an action was evaluated against current authority without revealing unrelated delegation terms.

## F.5 Confidential Evidence Package

Store detailed execution evidence with an evidence custodian and issue scoped access grants for audit, investigation, or appeal.

## F.6 Privacy-Preserving Status

Permit a verifier to determine that no disqualifying status applies without exposing unrelated incident or identity information.

# Appendix G. Design Rationale

## G.1 Why a Directory Is Insufficient

A directory answers where an agent can be found and how it describes itself. Delegated action requires answers about legitimacy, scope, accountability, and remedy.

## G.2 Why Identity and Delegation Are Separate

Identity is persistent. Delegation is contextual and time-bounded. Combining them causes authority to survive changes in principal, purpose, operator, or control.

## G.3 Why Ownership Is Not Central

Agents may be developed, published, deployed, operated, controlled, sponsored, and legally backed by different entities. A single ownership field obscures the actual accountability graph.

## G.4 Why Status Is Multi-Dimensional

An agent can be registered but offline, authorized but uninsured, operational but under investigation, or assured but no longer delegated. A single active/inactive flag cannot represent these states safely.

## G.5 Why Assurance Is Not Universal Trust

Assurance is always about a defined subject, scope, control set, evaluator, time, and limitation. It cannot establish suitability for every purpose.

## G.6 Why Point-in-Time Resolution Is Required

Disputes concern the state that applied when an action occurred, not merely the current state.

## G.7 Why Revocation Requires Enforcement

A registry can declare that authority no longer exists, but an agent may still retain active credentials, sessions, or runtime access. Effective revocation requires operational convergence.

## G.8 Why Federation Requires Recognition

Technical interoperability does not create institutional legitimacy. Registries need explicit rules for whose records, decisions, and assurance claims they accept.

## G.9 Why Redress Is a Protocol Concern

For consequential agents, the ability to challenge, correct, suspend, restore, and repair is part of system correctness. It cannot be left as an undocumented external process.

## G.10 Central Theory

The central architectural proposition of this specification is:

> **An agent registry should not be designed as a directory of autonomous software objects. It should be designed as a distributed authority-control plane for delegated action.**

A conforming registry therefore exists not merely to make agents visible, but to make their identity, authority, assurance, operation, accountability, and contestability machine-resolvable.

---

# Appendix H. Change Log

## H.0 Version 0.9.0

- Promoted the document to the authoritative Candidate Specification.
- Added stable Candidate requirement identifiers and independent conformance targets.
- Hardened delegation, recognition, lifecycle, durable-event, proof, policy, and evidence semantics.
- Added the informative ARPA–TRQP governed query-projection boundary.
- Required machine-verifiable requirement-to-test-to-evidence traceability.

## H.2 Version 0.5.0

- Added composable protocol modules, ARPA-Core profile, identifier/alias and Agent Card profiles.
- Added normative OpenAPI/event contracts, controlled registries, completed schemas and reference implementation.
- Added multidimensional conformance evidence, extended governance vectors, end-to-end scenarios and deployment guidance.

## H.1 Version 0.3.0

- Attributed the specification to a named author.
- Added an ABNF grammar for the `agentreg` identifier scheme (§12.2).
- Named JCS (RFC 8785) as the default record canonicalization method, with a profile-declared override (§13.2).
- Defined the relationship between the document version and the record `schema_version` track (§33.1).
- Added an HTTP status code mapping for `ARPA-*` error codes (§34.3).
- Corrected Appendix G subsection numbering (previously mislabeled `F.1`–`F.10`).
- Cited BCP 14 (RFC 2119, RFC 8174) for the normative requirements keywords.
- Published JSON Schema (2020-12) definitions for all fourteen record families under `schemas/`, with a shared record envelope.
- Published one valid and one invalid machine-validated example per record family under `examples/`, plus a validation script (`scripts/validate_examples.py`).
- Published conformance test vectors and profile matrices for all four conformance profiles under `conformance/`, each with at least one granting and one blocking test case, plus a reference evaluator and test-vector runner (`scripts/reference_evaluator.py`, `scripts/validate_test_vectors.py`).
- Wired schema and conformance validation into repository CI.

## H.2 Version 0.2.0

- Reorganized the specification into context, architecture, normative protocol, cross-cutting requirements, and conformance parts.
- Added a detailed problem statement and requirement-to-failure-mode mapping.
- Added representative use cases and end-to-end protocol flows.
- Added explicit trust, issuer-competence, projection, enforcement, and governance boundaries.
- Added registration, version, deployment, and relationship-management sections.
- Added normative authority-evaluation, reliance-evaluation, status-precedence, material-change, point-in-time, conflict, and revocation processing rules.
- Added privacy architecture and reusable privacy patterns.
- Added negative decision examples, test requirements, and deployment patterns.
- Clarified the distinction between registry resolution, policy decision, and runtime enforcement.

## H.3 Version 0.1.0

- Established the initial architecture, record model, lifecycle model, protocol endpoints, security considerations, and four conformance profiles.

# End of Candidate Specification


---

# 42. Protocol Modules and Implementation Contracts

## 42.1 Composable modules

ARPA defines `ARPA-Core`, `ARPA-Relations`, `ARPA-Assurance`, `ARPA-Authority`, `ARPA-Evidence`, and `ARPA-Federation`. A conforming deployment MUST declare supported modules. Support for a lower module MUST NOT be interpreted as support for a higher module. The normative dependency and non-implication rules are specified in `docs/protocol-modules.md`.

## 42.2 Core implementation profile

A Profile A implementation MUST satisfy `spec/profiles/arpa-core-identity-discovery-profile.md`. It MAY omit authority, assurance, evidence and federation operations, but MUST return `ARPA-OP-NOT-SUPPORTED` rather than an affirmative or ambiguous result.

## 42.3 Machine-readable contracts

The JSON Schemas, controlled registries, OpenAPI contract, event contract and conformance vectors in this repository are normative implementation artifacts for v0.5.0. Where prose and a machine-readable artifact conflict, an implementation MUST report the conflict; neither form silently overrides the other until corrected through governance.

## 42.4 External descriptions

External Agent Cards and equivalent descriptions are discovery inputs. Their claims are self-declared unless independently verified. Capability description MUST NOT become capability authorization or delegated authority by import.

## 42.5 Conformance evidence

Conformance claims MUST identify protocol, semantic, cryptographic, operational, governance and enforcement dimensions. An implementation report MUST state unsupported dimensions and known limitations.


### v0.10.0 — 2026-09-23

This release consolidates the previously approved v0.9.1 adversarial-hardening amendment and Candidate amendments ARPA-CAND-PP-01, ARPA-CAND-PP-02, and ARPA-CAND-PP-03 into one normative Candidate baseline. Historical amendment documents remain retained as provenance. The consolidation does not alter the independently versioned IETF publication history.
