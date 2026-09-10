---
title: "Agent Registry Protocol"
abbrev: "ARPA"
docname: draft-sankarshan-agent-registry-protocol-00
category: std
ipr: trust200902
submissiontype: IETF
area: "Applications and Real-Time"
workgroup: "Individual Submission"
keyword:
  - software agents
  - agent registry
  - delegated authority
  - lifecycle
  - resolution
  - authorization
stand_alone: yes
pi:
  toc: yes
  sortrefs: yes
  symrefs: yes
  compact: yes
author:
  -
    ins: S. Mukhopadhyay
    name: Sankarshan Mukhopadhyay
    org: QBF Consulting LLP
    email: sankarshan@qbfconsulting.digital
normative:
  RFC2119:
  RFC8174:
  RFC9110:
  RFC9111:
  RFC8259:
  RFC3339:
  RFC3986:
  RFC9457:
informative:
  RFC6749:
  RFC8414:
  RFC8615:
  RFC9421:
  ARPA-SPEC:
    title: "Agent Registry Protocol and Architecture (ARPA) Candidate Specification"
    author:
      -
        ins: S. Mukhopadhyay
        name: Sankarshan Mukhopadhyay
        org: QBF Consulting LLP
    date: 2026-07-16
    target: https://qbf-consulting.github.io/agent-registry-protocol/spec/agent-registry-protocol-v0.9.0.html
---

--- abstract

Software agents increasingly act on behalf of people and organizations across administrative and security boundaries. Existing discovery mechanisms can identify an endpoint or advertise a capability, but they do not by themselves provide a common way to resolve who operates an agent, the bounded authority under which it acts, whether that authority is current, or what evidence supports a reliance decision.

This document defines the Agent Registry Protocol (ARPA), an HTTP and JSON protocol for publishing and resolving information about software agents, their operational deployments, typed relationships, bounded delegated authority, lifecycle status, and associated evidence. ARPA separates identification, authentication, authorization, assurance, and lifecycle state. Registration, successful authentication, capability advertisement, or proof verification does not by itself establish authority to perform an action.

The protocol is designed to support deterministic fail-safe behavior when material authority information is revoked, suspended, expired, stale, conflicting, unavailable, or unverifiable.

--- middle

# Introduction

Software agents can retrieve protected information, invoke tools, modify workflows, initiate transactions, coordinate other agents, and otherwise cause effects on behalf of principals. A relying system evaluating such an action needs more than endpoint discovery. It needs protocol-visible information sufficient to determine which agent is involved, which deployment is executing, who operates or controls it, what delegated authority applies, whether that authority remains effective, and where supporting evidence can be obtained.

ARPA provides a registry and resolution protocol for those questions. It does not define a universal trust score, a universal legal theory of agency, a new authentication protocol, or a mandatory credential format. It also does not treat successful registry resolution as an authorization decision. A relying party combines ARPA resolution results with local policy and any external authentication, credential, or assurance mechanisms required for its context.

The protocol intentionally preserves several non-implication rules:

* discovering an agent does not imply authorization to invoke it;
* control of an identifier or cryptographic key does not imply authority to act for a principal;
* an advertised capability does not imply permission to exercise that capability;
* successful proof verification does not imply that the asserted authority is current or sufficient;
* technical federation does not imply governance recognition; and
* historical registry state is evidence for evaluation, not by itself a legal determination about a historical act.

The wider ARPA project specification {{ARPA-SPEC}} defines additional governance, assurance, conformance, federation, redress, implementation, and deployment material. This Internet-Draft deliberately narrows that work to interoperable protocol behavior.

## Conventions and Requirements Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in BCP 14 {{RFC2119}} {{RFC8174}} when, and only when, they appear in all capitals, as shown here.

HTTP terminology follows {{RFC9110}}. JSON follows {{RFC8259}}. Timestamps use the `date-time` form of {{RFC3339}}.

# Scope

ARPA defines protocol behavior for persistent agent identifiers and deployment identifiers; registration and update of agent records; typed relationships; bounded delegated authority; capability and assurance references; multidimensional lifecycle and authority status; current and point-in-time resolution; discovery and query behavior; material status events; deterministic processing of stale, conflicting, unavailable, and unsupported state; error representation; extension and version negotiation; and evidence references.

ARPA does not define a universal agent-to-agent messaging protocol, task protocol, reputation system, liability regime, credential format, signature suite, policy language, distributed ledger, or mandatory storage architecture.

# Terminology

**Agent:** A software entity capable of performing actions with some degree of autonomy.

**Agent Identifier:** A persistent URI identifying a logical agent independently of a particular version or deployment.

**Deployment:** An operational instance of an agent version in a particular execution context.

**Principal:** A person or organization on whose behalf an agent may act.

**Operator:** The entity responsible for running an agent deployment.

**Controller:** An entity with material technical or administrative control over an agent or deployment.

**Accountable Entity:** An entity identified by the registry as accepting a defined accountability role for an agent or class of actions.

**Relationship:** A typed, scoped, time-bounded statement linking two registry subjects.

**Authority Envelope:** A bounded representation of authority delegated from an issuer to a subject, including permitted actions, resources, conditions, prohibitions, delegation depth, and validity interval.

**Resolver:** A client that queries one or more ARPA registries.

**Relying Party:** A system or actor that uses ARPA data as one input to a local trust or authorization decision.

**Registry:** A service that publishes ARPA records and resolution responses.

**Authoritative Record:** A record for which the publishing registry is identified as an authoritative source within the applicable scope.

**Derived Record:** A cached, indexed, projected, or federated representation whose authoritative source is elsewhere.

**Material State:** State whose absence or change can alter an authorization or reliance outcome.

# Protocol Model

## Separation of Resolution, Decision, and Enforcement

ARPA separates resolution, decision, and enforcement. A registry response MUST NOT claim that a relying party is required to authorize an action unless the registry is itself the applicable policy decision authority for that action and this role is explicitly represented. A resolver MUST NOT infer authorization solely from successful resolution.

## Protocol Roles

An implementation can act as one or more of registry publisher, resolver or registry consumer, authority evaluator, event publisher, event consumer or enforcement point, or federation participant. An implementation claiming conformance to one role MUST NOT imply conformance to another role.

## Authority Invariants

An authority evaluator conforming to this document MUST verify that a delegation issuer possessed the effective authority being delegated; MUST NOT allow delegation to expand the issuer's effective scope; MUST apply explicit validity intervals, conditions, prohibitions, resource limits, action limits, and delegation-depth limits; MUST treat revoked, suspended, expired, stale, conflicting, unavailable, or unverifiable material authority as non-affirmative; MUST NOT infer transitive recognition unless explicitly declared and permitted by policy; and MUST retain enough information to explain an authority evaluation.

# Identifier Model

## Agent Identifiers

An Agent Identifier MUST be a URI conforming to {{RFC3986}}. Its scheme and dereference behavior are deployment choices unless another specification defines them. ARPA does not define a new URI scheme in this document. An Agent Identifier MUST identify the logical agent rather than a single software build, process, network endpoint, or ephemeral runtime session. Registries MUST NOT silently reassign an Agent Identifier to a different logical agent.

## Deployment Identifiers

A deployment MUST have an identifier unique within the scope of the authoritative registry. A deployment identifier SHOULD be globally unique when deployments are expected to move between registries or administrative domains. A deployment record MUST identify the logical Agent Identifier and SHOULD identify the agent version from which the deployment was created.

# Record Envelope

Every ARPA record returned by the protocol MUST contain an envelope with at least `record_type`, `record_id`, `subject`, `issuer`, `issued_at`, `valid_from`, `version`, and `source`. A record that expires MUST contain `valid_until`. A derived record MUST identify the authoritative source and SHOULD identify when the derived representation was produced. Unknown record types MUST NOT be interpreted as a known type.

# Agent Resource Model

An agent resource SHOULD contain the Agent Identifier, labels if available, current version and deployment references, relationship references, service endpoint references, capability declaration references, authority references, lifecycle status, evidence references, and representation metadata. A capability declaration MUST NOT be interpreted as authorization. An endpoint reference MUST NOT be interpreted as proof that the endpoint is controlled by the principal for whom an action is proposed.

# Relationship Model

A relationship record MUST contain a relationship type, source subject, target subject, issuer, scope, effective time, and current status. Where absence of a relationship would change an authorization outcome, the response MUST provide either the relationship or a machine-readable indication that authoritative relationship state could not be established. Registries MUST NOT infer a broader relationship from a narrower one.

# Authority Envelope

An authority envelope represents bounded authority. It MUST contain `issuer`, `subject`, `actions` or equivalent action scope, `valid_from`, status information, and a stable identifier. When applicable it MUST also contain resources, purpose restrictions, conditions, prohibitions, limits, `valid_until`, delegation depth, evidence references, and parent authority. Delegation MUST NOT increase the issuer's effective scope.

# Lifecycle and Status

ARPA represents lifecycle state as multiple dimensions rather than a single `active` flag. A registry MUST distinguish applicable effects including active/current, suspended, revoked, expired, superseded, retired, and indeterminate/unavailable. A resolver MUST NOT map `indeterminate`, `unavailable`, `conflicting`, or `stale` material authority state to an affirmative authorization outcome.

# HTTP API

ARPA uses HTTP semantics as defined by {{RFC9110}}. Registries MUST use HTTPS for network deployments that carry non-public data or authority information unless an equivalent authenticated and confidential transport is provided.

Logical operations include registry metadata at `GET /.well-known/agent-registry`, agent discovery, current and historical resolution, authority and status resolution, registration, and update. Use of `/.well-known/agent-registry` requires an IANA registration before Standards Track publication.

## Registry Metadata

Registry metadata SHOULD identify the protocol, protocol version, issuer, API base, supported record types, historical-resolution support, and event endpoint. Metadata MUST NOT imply that every advertised optional feature is authorized for every caller.

## Registration

A registry MUST authenticate and authorize registration requests according to local policy. On successful creation it SHOULD return `201 Created` and a `Location` header. A registry MUST reject a request that would reassign an existing persistent Agent Identifier to a different logical agent.

## Current Resolution

A successful current-state resolution returns `200 OK` with the current representation and sufficient freshness/provenance metadata to distinguish authoritative from derived state. `404 Not Found` MUST NOT be interpreted as evidence that the agent does not exist in another registry.

## Historical Resolution

Historical resolution uses an `at` query parameter containing an {{RFC3339}} timestamp. Responses MUST distinguish requested effective time, evaluation time, records selected as effective, later material events, and reconstruction limitations. If material historical state cannot be reconstructed with sufficient confidence, the result MUST be indeterminate rather than affirmative.

## Discovery

Discovery endpoints are informational. Search or list results MUST NOT imply authorization, endorsement, assurance, or permission to invoke an agent. Sensitive discovery SHOULD require authorization when disclosure creates material privacy or security risk.

## Authority Resolution

Authority resolution returns authority envelopes and status. Missing, stale, conflicting, or unavailable required authority state MUST be exposed rather than omitted in a way that could be interpreted as affirmative authority.

## Conditional Requests and Caching

Registries SHOULD provide validators such as `ETag`. A stale cached response MUST NOT be used to produce an affirmative authority result when freshness policy requires newer authoritative state. Shared caches MUST follow {{RFC9111}}.

# Error Handling

Protocol errors SHOULD use Problem Details for HTTP APIs {{RFC9457}}. Clients MUST NOT treat an unknown error code or unknown Problem Details extension as success.

# Event Model

ARPA defines an event envelope for material changes. Events SHOULD be immutable once published. Event consumers MUST support duplicate delivery and MUST NOT allow duplicate processing to expand authority. A registry MUST define event ordering semantics. A consumer MUST NOT claim enforcement convergence until applicable acknowledgement or observation requirements have been satisfied.

# Versioning and Extensions

Protocol versions MUST be explicit. An implementation receiving an unsupported major version MUST fail explicitly. Extensions MUST specify whether they are ignorable. Implementations MUST fail closed when an unknown non-ignorable extension can affect authority, lifecycle, security, privacy, or evidence semantics.

# Security Considerations

ARPA exposes information that can influence authorization and operational decisions. Attackers able to forge, suppress, replay, reorder, stale, or selectively disclose registry state can cause unauthorized action or denial of legitimate action. Implementations MUST authenticate authoritative sources for material state and evaluate freshness. Delegation processing MUST prevent scope amplification. Conflicting authoritative state MUST remain non-affirmative until resolved. Historical records and event processing require integrity, replay, ordering, and recovery controls. A valid signature MUST NOT be treated as proof of current delegated authority without evaluating signed semantics and lifecycle state.

# Privacy Considerations

Agent registries can expose relationships among people, organizations, agents, deployments, operators, controllers, and delegated authorities. Registries SHOULD minimize collected and published relationship data. Discovery and search SHOULD be treated as distinct privacy surfaces. Historical records increase correlation and retention risk. Evidence references and logs SHOULD avoid unnecessary confidential data. Federation agreements SHOULD define permitted propagation, purpose restrictions, retention, correction, and withdrawal behavior. ARPA does not define a legal basis for processing personal data.

# Operational Considerations

Deployments SHOULD publish operational metadata sufficient for resolvers to understand supported protocol versions, record types, historical-resolution support, event mechanisms, and freshness expectations. Registries SHOULD define service-level expectations for material status propagation. Resolvers SHOULD retain enough decision input metadata to reproduce material authority evaluations subject to privacy and retention constraints. Recovery MUST NOT silently restore superseded or revoked authority as current.

# Implementation Status

This section records implementation experience for the Internet-Draft and is informational rather than normative.

The ARPA project repository contains a reference implementation, conformance-oriented tests, examples, and interoperability work used to exercise the protocol model. These artifacts are evolving alongside the Candidate Specification and this protocol extraction. Their presence demonstrates implementation work in progress and MUST NOT be interpreted as evidence of IETF consensus, interoperability certification, production readiness, or endorsement of any deployment.

Implementers and reviewers are encouraged to report implementation experience, protocol ambiguities, interoperability findings, and adversarial test results through the repository issue tracker. Material findings may result in changes to subsequent revisions of this Internet-Draft.

# IANA Considerations

This document requests no IANA actions in `-00`. A future revision may request registration of `/.well-known/agent-registry` and other identifiers if interoperability experience warrants it. Until such registrations are approved, implementations MUST treat names used by this draft as experimental/project-scoped and MUST NOT represent them as IANA-assigned values.

# Conformance

An implementation claiming conformance MUST identify the protocol version and role or roles claimed. A conforming registry MUST expose protocol metadata, preserve persistent identifier semantics, distinguish authoritative from derived state, expose lifecycle and authority status without mapping indeterminate state to affirmative authority, implement current resolution, use defined error behavior or a documented compatible mapping, preserve fail-closed extension/version rules, and satisfy applicable security and privacy requirements. A conforming resolver MUST distinguish resolution from authorization, evaluate freshness, fail non-affirmatively on stale/conflicting/unavailable/unverifiable material authority, prevent delegation scope amplification when evaluating authority, preserve unknown non-ignorable extension behavior, and retain sufficient decision metadata where it produces authority evaluations.

# References to the Wider ARPA Project

The repository-maintained Candidate Specification contains governance, assurance, conformance, federation, implementation, redress, test-vector, and deployment material intentionally omitted from this protocol-focused Internet-Draft. The two documents are related but have separate version lines and publication states.

# Acknowledgements

The author thanks contributors and reviewers of the wider Agent Registry Protocol project whose implementation, interoperability, governance, security, privacy, and adversarial-hardening work informed this protocol extraction.
