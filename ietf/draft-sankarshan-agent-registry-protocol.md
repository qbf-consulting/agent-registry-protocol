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

ARPA defines protocol behavior for:

* persistent agent identifiers and deployment identifiers;
* registration and update of agent records;
* typed relationships between agents, principals, operators, controllers, accountable entities, and other actors;
* representation of bounded delegated authority;
* capability and assurance references without treating either as authorization;
* multidimensional lifecycle and authority status;
* current and point-in-time resolution;
* registry discovery and query behavior;
* event publication sufficient to communicate material status changes;
* deterministic processing of stale, conflicting, unavailable, and unsupported state;
* error representation;
* extension and version negotiation rules; and
* evidence references supporting later audit or reliance evaluation.

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

ARPA separates three functions:

1. **Resolution** obtains registry state and evidence references.
2. **Decision** evaluates that state against action context and relying-party policy.
3. **Enforcement** permits, restricts, or denies an actual action.

A registry response MUST NOT claim that a relying party is required to authorize an action unless the registry is itself the applicable policy decision authority for that action and this role is explicitly represented. A resolver MUST NOT infer authorization solely from successful resolution.

## Protocol Roles

An implementation can act as one or more of:

* registry publisher;
* resolver or registry consumer;
* authority evaluator;
* event publisher;
* event consumer or enforcement point; or
* federation participant.

An implementation claiming conformance to one role MUST NOT imply conformance to another role.

## Authority Invariants

An authority evaluator conforming to this document:

* MUST verify that a delegation issuer possessed the effective authority being delegated;
* MUST NOT allow delegation to expand the issuer's effective scope;
* MUST apply explicit validity intervals, conditions, prohibitions, resource limits, action limits, and delegation-depth limits;
* MUST treat revoked, suspended, expired, stale, conflicting, unavailable, or unverifiable material authority as non-affirmative;
* MUST NOT infer transitive recognition unless a transitive relationship is explicitly declared and permitted by policy; and
* MUST retain enough input and result information to explain an affirmative or negative authority evaluation.

# Identifier Model

## Agent Identifiers

An Agent Identifier MUST be a URI conforming to {{RFC3986}}. Its scheme and dereference behavior are deployment choices unless another specification defines them. ARPA does not define a new URI scheme in this document.

An Agent Identifier MUST identify the logical agent rather than a single software build, process, network endpoint, or ephemeral runtime session.

Registries MUST NOT silently reassign an Agent Identifier to a different logical agent. If an identifier becomes unusable, the registry SHOULD publish a terminal status or supersession relationship rather than reuse it.

## Deployment Identifiers

A deployment MUST have an identifier unique within the scope of the authoritative registry. A deployment identifier SHOULD be globally unique when deployments are expected to move between registries or administrative domains.

A deployment record MUST identify the logical Agent Identifier and SHOULD identify the agent version from which the deployment was created.

# Record Envelope

Every ARPA record returned by the protocol MUST contain an envelope with at least:

~~~~ json
{
  "record_type": "agent",
  "record_id": "urn:example:record:1234",
  "subject": "https://registry.example/agents/7f6a",
  "issuer": "https://registry.example",
  "issued_at": "2026-08-18T12:00:00Z",
  "valid_from": "2026-08-18T12:00:00Z",
  "version": "1",
  "source": "https://registry.example/records/1234"
}
~~~~

A record that expires MUST contain `valid_until`. A record that supersedes another record SHOULD contain a reference to the superseded record. A derived record MUST identify the authoritative source and SHOULD identify when the derived representation was produced.

The `record_type` value identifies the record semantics. Unknown record types MUST NOT be interpreted as a known type. A resolver MAY retain unknown record types as opaque evidence.

# Agent Resource Model

An agent resource SHOULD contain:

* the Agent Identifier;
* human-readable labels, if available;
* current version and deployment references;
* relationship references;
* service endpoint references;
* capability declaration references;
* authority references;
* lifecycle status;
* evidence references; and
* representation metadata including source and freshness.

A capability declaration MUST NOT be interpreted as authorization. An endpoint reference MUST NOT be interpreted as proof that the endpoint is controlled by the principal for whom an action is proposed.

# Relationship Model

A relationship record MUST contain:

* a relationship type;
* a source subject;
* a target subject;
* an issuer;
* scope;
* effective time; and
* current status.

Where absence of a relationship would change an authorization outcome, the response MUST provide either the relationship or a machine-readable indication that authoritative relationship state could not be established.

Registries MUST NOT infer a broader relationship from a narrower one. For example, an `operated-by` relationship MUST NOT be interpreted as an `authorized-by` relationship unless a separate specification explicitly defines such equivalence.

# Authority Envelope

An authority envelope represents bounded authority. It MUST contain:

* `issuer`;
* `subject`;
* `actions` or an equivalent action scope;
* `valid_from`;
* status information; and
* a stable identifier for the authority statement.

When applicable it MUST also contain:

* resources or resource classes;
* purpose restrictions;
* conditions;
* prohibitions;
* monetary, rate, geographic, or other limits;
* `valid_until`;
* delegation depth or prohibition on further delegation;
* evidence references; and
* the authority statement from which the issuer derives the delegated scope.

An authority envelope MUST NOT be interpreted independently of its current status and applicable parent authority. Delegation MUST NOT increase the issuer's effective action, resource, purpose, temporal, geographic, monetary, or delegation scope.

# Lifecycle and Status

ARPA represents lifecycle state as multiple dimensions rather than a single `active` flag. A response MAY expose dimensions including registration, operational, security, authority, and assurance status.

A registry MUST distinguish at least the following effects when they are applicable:

* active or current;
* suspended;
* revoked;
* expired;
* superseded;
* retired; and
* indeterminate or unavailable.

A resolver MUST NOT map `indeterminate`, `unavailable`, `conflicting`, or `stale` material authority state to an affirmative authorization outcome.

A registry publishing revocation or suspension SHOULD expose an event or other freshness mechanism enabling consumers to discover the change promptly. A publisher MUST NOT describe revocation as fully converged merely because the registry record changed if downstream enforcement acknowledgements are required by the applicable profile.

# HTTP API

ARPA uses HTTP semantics as defined by {{RFC9110}}. Registries MUST use HTTPS for network deployments that carry non-public data or authority information unless an equivalent authenticated and confidential transport is provided by the deployment environment.

This document defines the following logical resources. Deployments MAY choose different path layouts if discoverable metadata maps the logical operations unambiguously.

| Operation | Example target | Purpose |
|---|---|---|
| Registry metadata | `GET /.well-known/agent-registry` | Discover protocol metadata |
| List/discover agents | `GET /agents` | Query discoverable agents |
| Resolve agent | `GET /agents/{id}` | Resolve current agent state |
| Historical resolution | `GET /agents/{id}?at={time}` | Resolve effective-time state |
| Resolve authority | `GET /agents/{id}/authority` | Resolve authority statements |
| Resolve status | `GET /agents/{id}/status` | Resolve lifecycle/status state |
| Register agent | `POST /agents` | Create an agent registration |
| Update registration | `PUT /agents/{id}` | Replace an owned registration |

Use of `/.well-known/agent-registry` requires an IANA registration before Standards Track publication; see [IANA Considerations](#iana-considerations).

## Registry Metadata

A registry metadata response SHOULD contain:

~~~~ json
{
  "protocol": "arpa",
  "protocol_version": "1",
  "issuer": "https://registry.example",
  "api_base": "https://registry.example/api",
  "supported_record_types": [
    "agent", "relationship", "authority", "status"
  ],
  "historical_resolution": true,
  "events_endpoint": "https://registry.example/events"
}
~~~~

The metadata endpoint MUST NOT imply that every advertised optional feature is authorized for every caller. Access control remains operation-specific.

## Registration

A client creating a registration sends `POST` to the registration collection with a JSON representation of the requested agent record.

The registry MUST authenticate and authorize the registration request according to local policy. ARPA does not define that authentication mechanism.

On successful creation, the registry SHOULD return `201 Created` and a `Location` header identifying the new agent resource. A retry-safe deployment SHOULD support an application-level idempotency mechanism and MUST document its semantics.

A registry MUST reject a request that would reassign an existing persistent Agent Identifier to a different logical agent.

## Current Resolution

A successful current-state resolution returns `200 OK` with the current representation and sufficient freshness/provenance metadata for the client to distinguish authoritative from derived state.

A response MUST identify when material state is derived or cached. Derived material authority state MUST include the authoritative source and freshness information.

`404 Not Found` means that the queried registry has no resolvable resource for the supplied identifier. It MUST NOT be interpreted as evidence that the agent does not exist in any other registry.

## Historical Resolution

Historical resolution uses an `at` query parameter containing an {{RFC3339}} timestamp. The response MUST distinguish:

* the requested effective time;
* the time at which the resolution was performed;
* records selected as effective at the requested time;
* later material events known at evaluation time; and
* reconstruction completeness or limitations.

A historical response MUST NOT silently apply current status to the requested historical time or silently ignore later events that materially affect interpretation.

If the registry cannot reconstruct material historical state with sufficient confidence, it MUST return an indeterminate reconstruction status and MUST NOT present the result as an authoritative affirmative determination.

## Discovery

Discovery endpoints are informational. Search or list results MUST NOT imply authorization, endorsement, assurance, or permission to invoke an agent.

A registry SHOULD minimize information disclosed through unauthenticated discovery. Sensitive relationships, principal linkage, delegated authority details, or operational metadata SHOULD require authorization when disclosure creates material privacy or security risk.

## Authority Resolution

Authority resolution returns one or more authority envelopes and their status. If the registry knows that required parent authority, status, or evidence is missing, stale, conflicting, or unavailable, the response MUST expose that condition rather than omit it in a way that could be interpreted as affirmative authority.

## Conditional Requests and Caching

Registries SHOULD provide validators such as `ETag` where stable representation validators are available. Resolvers SHOULD use conditional requests to reduce load while retaining freshness.

Responses containing authority or security status MUST define cache behavior appropriate to the revocation and freshness requirements of the deployment. Shared caches MUST NOT store confidential responses unless explicitly permitted by applicable HTTP caching rules {{RFC9111}} and response directives.

A stale cached response MUST NOT be used to produce an affirmative authority result when the applicable freshness policy requires newer authoritative state.

# Error Handling

Protocol errors SHOULD use Problem Details for HTTP APIs {{RFC9457}} with an ARPA-specific problem type when interoperable handling is unavailable. The `type` URI SHOULD identify a stable ARPA problem type. The response SHOULD include an ARPA error code suitable for deterministic client behavior.

At minimum, interoperable implementations SHOULD distinguish:

* invalid request;
* unsupported protocol version;
* unsupported record type;
* unauthenticated request;
* unauthorized request;
* record not found;
* stale material state;
* conflicting authoritative state;
* unavailable authoritative state;
* unverifiable evidence;
* revoked or suspended authority; and
* historical reconstruction indeterminate.

Clients MUST NOT treat an unknown error code or unknown Problem Details extension as success.

# Event Model

ARPA defines an event envelope for material changes. An event MUST contain:

* event identifier;
* event type;
* subject;
* issuer;
* event time;
* affected record or status reference; and
* protocol version.

Events SHOULD be immutable once published. A correction SHOULD be represented as a new event referencing the superseded event.

Event consumers MUST support duplicate delivery. Processing the same event identifier more than once MUST NOT expand authority or cause a transition that could not result from a single processing of that event.

A registry MUST define event ordering semantics. If globally monotonic sequence numbers are unavailable, the registry MUST provide enough source-specific ordering information for consumers to detect gaps or ambiguity within the applicable stream.

Revocation and suspension events affecting authority SHOULD be delivered through a mechanism whose expected convergence is documented. A consumer MUST NOT claim enforcement convergence until the acknowledgement or observation requirements of the applicable deployment profile have been satisfied.

# Versioning and Extensions

Protocol versions MUST be explicit in registry metadata and SHOULD be explicit in representations that can cross version boundaries.

An implementation receiving a major protocol version it does not support MUST fail explicitly rather than interpret it as a supported version.

Extensions MUST use collision-resistant names or registered extension identifiers. An extension MUST specify whether it is ignorable. An implementation MUST fail closed when an unknown non-ignorable extension can affect authority, lifecycle, security, privacy, or evidence semantics.

New fields are not automatically safe to ignore. Extension specifications MUST state the processing effect of omission and non-recognition.

# Security Considerations

ARPA exposes information that can influence authorization and operational decisions. An attacker who can forge, suppress, replay, reorder, stale, or selectively disclose registry state can cause both unauthorized action and denial of legitimate action.

Implementations MUST authenticate authoritative sources for material state. Deployments MUST define how source authenticity and integrity are established. HTTPS server authentication can provide transport-level source authentication but does not by itself establish that the server is authoritative for a particular principal, agent, relationship, or authority scope.

Resolvers MUST evaluate freshness for material state. A cryptographically valid but stale authority statement can be unsafe. Caches and federation layers MUST preserve source, issuance time, validity interval, and status information needed to evaluate freshness.

Delegation processing MUST prevent scope amplification. Implementations MUST check that every delegated authority is a subset of the issuer's effective authority after applying conditions, prohibitions, validity, resource scope, action scope, and delegation-depth constraints.

Registries and resolvers MUST treat conflicting authoritative state as non-affirmative until the applicable conflict-resolution policy establishes a competent source or otherwise resolves the conflict. Implementations MUST NOT select the most permissive source merely because it enables an action.

Historical resolution creates evidence-retention risks. A registry that supports historical queries MUST protect retained records against unauthorized alteration and MUST expose reconstruction limitations rather than fabricate completeness.

Events can be replayed, reordered, duplicated, or suppressed. Consumers MUST implement duplicate-safe processing and MUST detect ordering gaps where the source provides sequence information. Material revocation or suspension SHOULD have an out-of-band recovery or resynchronization path when event delivery cannot be trusted.

The protocol does not define credential proof formats or cryptographic suites. Deployments using signed credentials, signed HTTP messages, or proof-bearing records MUST select algorithms and key-management practices appropriate to their threat model. A valid signature MUST NOT be treated as proof of current delegated authority without evaluating the signed semantics and lifecycle state.

Registry discovery can create enumeration and relationship-disclosure risks. Deployments SHOULD minimize unauthenticated discovery, separate public from restricted metadata, and avoid exposing principal-agent relationships or authority details beyond what the caller is permitted to learn.

Implementations MUST apply ordinary HTTP security controls including request size limits, parsing limits, rate limiting, authorization checks, logging controls, and protection against server-side request forgery when dereferencing evidence or federation references.

# Privacy Considerations

Agent registries can expose relationships among people, organizations, agents, deployments, operators, controllers, and delegated authorities. These relationships can reveal organizational structure, sensitive workflows, personal associations, operational capabilities, or transaction intent even when the underlying payloads are not disclosed.

Registries SHOULD minimize collected and published relationship data. A record SHOULD contain only the information required for the relying context. Deployments SHOULD prefer opaque or pairwise identifiers when global correlation is unnecessary.

Discovery and search interfaces SHOULD be treated as distinct privacy surfaces. A registry MAY permit resolution of a known identifier while denying bulk enumeration or broad search. Authorization for discovery MUST NOT be inferred from authorization for resolution.

Historical records increase correlation and retention risk. Deployments MUST define retention periods, access controls, correction procedures, and deletion or tombstoning behavior consistent with their legal and governance obligations. A historical-resolution feature MUST NOT be interpreted as requiring indefinite retention of personal data.

Evidence references can leak sensitive information through URLs, identifiers, query strings, or dereference patterns. Implementations SHOULD avoid embedding confidential data in evidence URLs and SHOULD authorize evidence retrieval independently from registry resolution.

Logs SHOULD avoid storing unnecessary authority contents, credentials, personal identifiers, or evidence payloads. Where audit requirements require retention, access SHOULD be restricted and retention SHOULD be bounded.

Federated registries can amplify privacy risk because data disclosed for one context can be indexed or correlated in another. Federation agreements SHOULD define permitted propagation, purpose restrictions, retention, correction, and withdrawal behavior.

ARPA does not define a legal basis for processing personal data. Implementers are responsible for identifying and satisfying applicable privacy and data-protection requirements.

# Operational Considerations

Deployments SHOULD publish operational metadata sufficient for resolvers to understand supported protocol versions, record types, historical-resolution support, event mechanisms, and relevant freshness expectations.

A registry SHOULD define service-level expectations for material status propagation. Where authority revocation or suspension affects downstream enforcement, the deployment SHOULD define the expected path from authoritative change to consumer observation and enforcement acknowledgement.

Resolvers SHOULD retain enough decision input metadata to reproduce material authority evaluations, subject to privacy and retention constraints. At minimum this normally includes evaluation time, authoritative source, source checkpoint or version, selected records, freshness assessment, and result.

Registries SHOULD provide backup, restoration, and compromise-recovery procedures. Recovery MUST NOT silently restore superseded or revoked authority as current. A restored registry SHOULD establish a trusted checkpoint before serving affirmative authority results.

# IANA Considerations

This document requests no IANA actions in `-00`.

A future revision may request registration of `/.well-known/agent-registry` in the Well-Known URIs registry and may define or request registries for protocol media types, relation types, or error identifiers if interoperability experience shows that centralized registration is warranted.

Until such registrations are approved, implementations MUST treat names used by this draft as experimental/project-scoped and MUST NOT represent them as IANA-assigned values.

# Conformance

An implementation claiming conformance to this document MUST identify the protocol version and role or roles for which conformance is claimed.

A conforming registry implementation MUST:

* expose protocol metadata;
* preserve persistent identifier semantics;
* distinguish authoritative from derived state;
* expose lifecycle and authority status without mapping indeterminate state to affirmative authority;
* implement current resolution;
* use the defined error behavior or a documented compatible mapping;
* preserve extension/version fail-closed rules; and
* satisfy the security and privacy requirements applicable to the implemented features.

A conforming resolver implementation MUST:

* distinguish resolution from authorization;
* evaluate material freshness;
* fail non-affirmatively on stale, conflicting, unavailable, or unverifiable material authority;
* prevent delegation scope amplification when it evaluates authority;
* preserve unknown non-ignorable extension behavior; and
* retain sufficient decision metadata for reproducibility where it produces authority evaluations.

Historical-resolution conformance additionally requires the implementation to distinguish requested-time state, evaluation-time knowledge, later material events, and reconstruction quality.

Event conformance additionally requires duplicate-safe processing and documented ordering/gap behavior.

# References to the Wider ARPA Project

The repository-maintained Candidate Specification contains governance, assurance, conformance, federation, implementation, redress, test-vector, and deployment material intentionally omitted from this protocol-focused Internet-Draft. The two documents are related but have separate version lines and publication states.

# Acknowledgements

The author thanks contributors and reviewers of the wider Agent Registry Protocol project whose implementation, interoperability, governance, security, privacy, and adversarial-hardening work informed this protocol extraction.

--- back

# Change Log

This section is to be removed by the RFC Editor before publication.

## -00

* Initial individual submission extracted from the ARPA Candidate Specification and implementation corpus.
* Defines HTTP/JSON registry metadata, agent/deployment resources, relationships, authority envelopes, lifecycle/status handling, current and historical resolution, discovery, events, errors, versioning, security, privacy, operations, and conformance.
