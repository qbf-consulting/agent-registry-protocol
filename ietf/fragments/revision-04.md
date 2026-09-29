# Protocol Interoperability and Security Hardening for Revision 04

This section promotes protocol-core semantics from ARPA Candidate v0.10.0 and Candidate Protocol Interoperability Amendment PP-04. The Candidate amendment and project artifacts are evidence and source governance; the normative requirements for this Internet-Draft are stated here.

## Protocol-Core Wire Structures

The following tables define the minimum protocol-core JSON contract for revision -04. Fields not listed here MAY be added only under the extension rules of this document. A field marked required MUST be present whenever the corresponding structure is carried on the wire.

### Common Record Envelope

| Field | JSON type | Cardinality | Requirement |
|---|---|---|---|
| `id` | string | 1 | Stable record identifier. |
| `record_type` | string | 1 | Identifies the record kind. |
| `version` | string | 1 | Representation/schema version for this IETF profile. |
| `issuer` | string | 1 | Identifier of the authority publishing the record. |
| `valid_from` | date-time string | 1 | Inclusive lower validity bound. |
| `valid_until` | date-time string | 0..1 | Exclusive upper validity bound when present. |
| `status` | object | 0..1 | Multi-dimensional status; when material to authority, absence MUST NOT be interpreted as active. |
| `proof` | object | 0..1 | Proof metadata/bytes as defined by the selected proof profile. |
| `extensions` | object | 0..1 | Namespaced extensions, including criticality metadata. |

### Agent Resource

An Agent Resource MUST contain the common envelope plus:

| Field | JSON type | Cardinality | Requirement |
|---|---|---|---|
| `agent_id` | string | 1 | Canonical `agentreg:` Agent Identifier. |
| `display_name` | string | 0..1 | Human-readable only; MUST NOT be used for identifier equality. |
| `endpoints` | array | 0..n | Service endpoints with protocol/profile metadata. |
| `relationships` | array of references | 0..n | References to typed relationship records. |

### Relationship Record

A Relationship Record MUST contain the common envelope plus:

| Field | JSON type | Cardinality | Requirement |
|---|---|---|---|
| `relationship_type` | string | 1 | Registered/core value or collision-resistant extension value. |
| `subject` | string | 1 | Entity from which the typed edge originates. |
| `related_entity` | string | 1 | Entity to which the typed edge points. |
| `scope` | object | 0..1 | Scope limiting the relationship. |
| `authority_source` | string | 1 | Stable source establishing the relationship. |

Relationship semantics MUST NOT be inferred from field position alone. In particular, `operated_by` and `controlled_by` MUST NOT be interpreted as `acts_for` or `delegates_to`.

### Authority Envelope

An Authority Envelope MUST contain the common envelope plus:

| Field | JSON type | Cardinality | Requirement |
|---|---|---|---|
| `principal` | string | 1 | Principal whose authority is being represented. |
| `delegate` | string | 1 | Agent/entity receiving bounded authority. |
| `actions` | array | 1..n | Permitted action/action-class identifiers. |
| `resources` | array | 0..n | Resource scope when applicable. |
| `constraints` | object | 0..1 | Limits, conditions, and prohibitions. |
| `derives_from` | string | 0..1 | Parent authority reference; REQUIRED for delegated authority and MAY be absent for a root grant. |
| `further_delegation` | boolean/object | 0..1 | Whether and under what limits further delegation is permitted. |

A delegated Authority Envelope without the required `derives_from` linkage is invalid when parent state is needed to establish monotonic delegation.

### Event

An Event MUST contain:

| Field | JSON type | Cardinality | Requirement |
|---|---|---|---|
| `event_id` | string | 1 | Stable event identifier. |
| `event_type` | string | 1 | Core or namespaced event type. |
| `source` | string | 1 | Registry/event-source identifier. |
| `sequence` | integer or string | 1 | Source ordering position/checkpoint. |
| `event_time` | date-time string | 1 | Time asserted by the event source. |
| `subject` | string | 1 | Affected record/entity. |
| `data` | object | 0..1 | Event-specific content. |

### Registry Metadata

The `/.well-known/agent-registry` representation MUST contain:

| Field | JSON type | Cardinality | Requirement |
|---|---|---|---|
| `registry_id` | string | 1 | Stable registry identity. |
| `protocol_version` | string | 1 | ARPA protocol version/profile identifier. |
| `base_endpoint` | URI string | 1 | Base endpoint for the selected protocol surface. |
| `supported_profiles` | array | 1..n | Supported representation/conformance profiles. |
| `events_endpoint` | URI string | 0..1 | Present only when the event contract is supported. |
| `write_policy` | URI/string | 0..1 | Stable policy reference for mutation authorization when writes are supported. |
| `clock_profile` | object/reference | 0..1 | Required when clock/skew assumptions can affect material decisions. |

### Authority Evaluation Result Wire Object

An Authority Evaluation Result MUST contain:

| Field | JSON type | Cardinality | Requirement |
|---|---|---|---|
| `decision` | string | 1 | One of `allow`, `allow_with_conditions`, `deny`, `indeterminate`, or `not_applicable`. |
| `reason_codes` | array of strings | 1..n | Stable machine-readable reasons. |
| `evaluation_time` | date-time string | 1 | Time at which the result was evaluated. |
| `policy` | object | 1 | MUST identify policy id, version, and applicability. |
| `conditions` | array | 0..n | REQUIRED and non-empty for `allow_with_conditions`. |
| `evidence` | array of references | 0..n | Material evidence/authority references. |
| `source_checkpoint` | string | 0..1 | REQUIRED when derived/historical/projected state materially contributed. |
| `freshness` | object/reference | 0..1 | REQUIRED when freshness can affect the result. |

## Representation Field Mapping

This document uses the IETF wire names `valid_from`, `valid_until`, and `version`. The corresponding ARPA Candidate v0.10.0 machine-contract names are `effective_from`, `effective_until`, and `schema_version`.

The mapping is exact and lossless. Implementations MUST NOT interpret an absent alternate field as an unbounded interval, default version, or equivalent value unless an explicitly selected representation profile defines that behavior. If both mapped names are present in a representation, they MUST carry equivalent values; conflicting values make the representation invalid.

## Authority Evaluation Result

A protocol-visible authority evaluation result MUST contain a `decision`, one or more `reason_codes`, `evaluation_time`, and the selected policy identifier, version, and applicability state.

When the decision is `allow_with_conditions`, at least one condition MUST be present.

When external, derived, historical, or projected evidence materially contributes to the result, the result MUST retain direct or stable references to that evidence and to the source checkpoint, version, or digest needed to reproduce the material evaluation.

Where freshness can affect the result, the result MUST carry a freshness bound or stable freshness-policy reference.

Only `allow` and `allow_with_conditions` are affirmative outcomes. `deny`, `indeterminate`, and `not_applicable` are non-affirmative outcomes and MUST NOT be collapsed into one another.

## Status Composition

Lifecycle, security, operational, and authority status are independent dimensions.

A material revoked, suspended, quarantined, compromised, retired, or otherwise restrictive state MUST prevent an affirmative result unless the selected profile explicitly defines a narrower safe interpretation.

Unknown, stale, conflicting, or unsupported material status MUST remain non-affirmative. An implementation MUST NOT silently collapse a restrictive state to `active`.

## Agent Identifier Syntax and Equality

The Agent Identifier uses the `agentreg` URI scheme:

~~~~
agentreg = "agentreg:" registry-namespace ":" agent-local-id
registry-namespace = 1*( unreserved / pct-encoded / sub-delims / "@" )
agent-local-id = 1*( unreserved / pct-encoded / sub-delims / "@" / ":" )
~~~~

The ABNF uses the `unreserved`, `pct-encoded`, and `sub-delims` productions from {{RFC3986}} and the core ABNF rules of {{RFC5234}}.

The scheme name is case-insensitive. The scheme-specific components are case-sensitive unless the assigning registry publishes a stronger normalization rule.

Percent-encoded octets MUST NOT be decoded before identifier equality comparison except where an assigning registry's published normalization profile explicitly permits equivalent normalization. Producers SHOULD emit a single canonical spelling and MUST NOT use percent-encoding to disguise the component delimiter.

Registries using human-readable Unicode identifiers MUST address normalization and confusable/homograph risk in their identifier-allocation policy.

## JSON Proof Inputs

Where an ARPA JSON proof profile signs or hashes a JSON representation and does not define another canonicalization, the JSON Canonicalization Scheme {{RFC8785}} MUST be used.

A parser MUST reject duplicate JSON member names before canonicalization or proof verification.

Proof verification establishes integrity or authenticity only for the covered representation. A valid proof MUST NOT substitute for current lifecycle, authority, policy, freshness, or status evaluation.

## Freshness and HTTP Caching

A response carrying material authority or status MUST expose enough information to determine freshness through a generated time, validity bound, authoritative source time, source checkpoint/version/digest, or a stable freshness-policy reference.

Derived or projected state MUST identify its authoritative source and material observation time or lag.

An HTTP cache lifetime MUST NOT exceed the material validity or freshness bound used for authority evaluation. When material freshness cannot be established, the result MUST remain non-affirmative.

## Registration Retry Semantics

ARPA does not define a universal application-level idempotency header for registration.

A client MUST NOT automatically replay a non-idempotent registration request unless a negotiated deployment profile defines retry-safe idempotency semantics.

A profile that supports retry-safe registration MUST define the idempotency key, replay window, duplicate-detection scope, and deterministic response behavior.

## Replacement Semantics

`PUT /agents/{id}` replaces the current representation by creating a new historical version. It MUST NOT erase the prior version.

The path identifier and logical subject identity MUST NOT change through PUT.

A mutable registry MUST support a representation precondition such as `If-Match` with an ETag, or an equivalent version/checkpoint precondition, and MUST reject stale concurrent replacement.

Omission of a material prohibition, constraint, delegation bound, or restrictive status MUST NOT silently widen authority. Authority widening requires explicit governing authority and evidence.

## Event Ordering, Replay, and Gap Handling

An implementation that advertises an ARPA event endpoint MUST provide, for each event, a stable event identifier and a source ordering position or checkpoint sufficient to detect gaps within that source.

Consumers MUST process duplicate events idempotently.

A consumer that detects a material sequence gap MUST NOT continue to assert affirmative state based only on the incomplete stream. It MUST resynchronize from an authoritative snapshot/checkpoint or produce a non-affirmative result.

Event endpoint metadata MUST declare delivery and replay semantics, including whether replay from a checkpoint is supported.

## Write Authorization

Protocol writes are default-deny.

A registry MUST expose or stably reference the policy controlling which authenticated principals may create, replace, or append relationship, authority, and status records.

Operator or controller status alone MUST NOT imply permission to mutate unrelated accountability, delegation, recognition, or authority records.

Unauthorized mutation MUST use ARPA Problem Details and the stable code `ARPA-RECORD-NOT-AUTHORIZED`.

## Critical Extensions

`critical` is the normative term for an extension whose non-recognition can affect authority, lifecycle, security, privacy, or evidence semantics.

An unknown critical extension MUST fail closed. Legacy `ignorable` or `non-ignorable` wording is equivalent only where explicitly mapped to the `critical` property; it is not a second extension model.

## Dereference Security

When dereferencing evidence, federation, source, or other external references, implementations MUST enforce SSRF protections.

Only profile-authorized URI schemes may be dereferenced. The resolved destination and every redirect target MUST be validated against deployment origin/network policy.

Unless explicitly trusted by profile, implementations MUST reject loopback, link-local, multicast, and private/internal destinations after resolution and MUST mitigate DNS rebinding.

Implementations MUST enforce request/response size and time limits. Ambient credentials, cookies, and authorization headers MUST NOT be forwarded across origins unless explicitly authorized.

A dereference failure or blocked dereference MUST NOT produce an affirmative authority result.

## Discovery and Search

`/.well-known/agent-registry` is registry capability and metadata discovery.

`GET /agents` is search or listing within a registry already selected by the caller.

Permission to discover registry metadata MUST NOT imply permission to enumerate agents.

## HTTP Operation Surface

The interoperable HTTP core consists of registry metadata discovery, agent resolution/search, registration/replacement when supported, and any event endpoint explicitly advertised under the event contract above.

Relationship, authority, history/lineage, and record-specific operations MAY be exposed by a profile. An implementation MUST NOT advertise an operation as interoperable ARPA core unless its request, response, authorization, error, and version semantics are defined by this document or the selected profile.

## Conformance Matrix

For revision -04, every promoted normative requirement MUST map to an applicable implementation role and at least one positive and one hostile or negative fixture in the version-pinned ARPA conformance corpus.

A conformance claim MUST identify the role or roles claimed. Features that are not implemented MUST NOT be implied by conformance to another role.
