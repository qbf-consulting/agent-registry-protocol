# Wire-Contract Precision for Revision 03

This section promotes protocol-core wire-contract semantics from ARPA Candidate v0.10.0 and Candidate Wire-Contract Coherence Amendment PP-03. The project schemas and vectors are implementation evidence; the normative requirements for this Internet-Draft are the requirements stated here.

## Authority Evaluation Outcomes

An authority evaluation outcome MUST be one of `allow`, `allow_with_conditions`, `deny`, `indeterminate`, or `not_applicable`.

`not_applicable` is a normal authority-evaluation outcome. It is not a lifecycle state and it is not an HTTP or protocol error. It MAY be returned only when the selected policy or profile does not govern the requested operation. A `not_applicable` result MUST include at least one stable reason code identifying the non-applicability basis.

Missing authority, missing delegation, expired, revoked or suspended authority, stale or conflicting material state, an unknown critical extension, unavailable or unsupported material evidence, incomparable scope, an unrecognized issuer, or inability to determine authority MUST NOT produce `not_applicable`. Those conditions produce `deny`, `indeterminate`, or a protocol error according to the failure layer.

Protocol errors represent malformed requests, unsupported protocol/profile/version negotiation, invalid wire representations, unavailable protocol services, or equivalent failures. They MUST NOT be used as a substitute for a valid policy outcome.

## Parent Authority Linkage

A delegated authority envelope MUST identify the parent authority statement from which its delegated scope derives using `derives_from` or an exactly equivalent field defined by a negotiated representation profile.

A root authority grant MAY omit `derives_from`. A delegated envelope MUST NOT omit the parent link when the omission prevents a resolver from evaluating monotonic delegation or current parent status.

Implementations MUST NOT infer parent authority solely from issuer identity, record ordering, network location, or an unauthenticated relationship.

## Temporal Boundaries and Clock Profile

Authority validity is half-open:

~~~~
effective_from <= evaluation_time < effective_until
~~~~

An evaluation exactly at `effective_from` is inside the interval. An evaluation exactly at `effective_until` is outside it.

Where timestamp precision or clock skew can materially affect an authority decision, the selected deployment or profile MUST expose, directly or by stable policy reference, the timestamp precision, maximum permitted clock skew, and treatment of future-dated material observations.

This document does not define a universal skew tolerance. Clock-ambiguous material authority state MUST remain non-affirmative until the applicable policy resolves the ambiguity.

## Collective-Principal Snapshot Binding

A threshold, quorum, role, or other collective-principal evaluation MUST bind the decision to one stated membership/controller and exercise-rule snapshot, identified by a stable checkpoint, version, or digest.

Each approval counted toward the collective rule MUST be valid under that same snapshot unless the governing rule explicitly permits cross-snapshot composition and the evidence proves the permitted transition.

Approvals collected across membership removal and re-addition, material role change, exercise-rule change, or stale membership MUST NOT be combined by default.

Decision evidence MUST retain the snapshot/checkpoint used for the membership and exercise-rule evaluation.

## ARPA Problem Details

Protocol-significant HTTP errors MUST use Problem Details {{RFC9457}} unless a negotiated transport profile defines another interoperable error representation.

An ARPA Problem Details object MUST contain `type`, `title`, `status`, and `code`. The `code` value MUST be a stable machine-readable ARPA error code. The `type` URI SHOULD be stable and dereferenceable documentation SHOULD describe its semantics.

Human-readable `title` or `detail` fields MUST NOT be the sole machine contract. A client that encounters an unknown material error code or extension MUST NOT interpret the response as success.

## Media Type

The media type for ARPA JSON representations is `application/agent-registry+json`.

HTTP servers implementing this representation MUST emit `Content-Type: application/agent-registry+json` for ARPA-specific JSON representations unless an explicit compatibility mode has negotiated `application/json`.

A deployment MAY support `application/json` as a compatibility fallback only when the represented ARPA semantics are identical. A server MUST NOT change normative interpretation solely because the generic fallback is used.

Protocol and profile version negotiation remain explicit in the representation or registry metadata. This revision does not define a media-type version parameter.

## Extension Namespaces

Extensions MUST use collision-resistant identifiers. URI- or URN-based namespace identifiers SHOULD use an authority controlled by the extension owner. An extension MUST identify its owner/authority, version, criticality, and processing semantics.

An implementation MUST NOT treat an unrecognized namespace as a known extension merely because its local name resembles a known field.

# Federated Trust Resolution and ToIP Composition

ARPA can consume authoritative evidence from trust infrastructures outside an ARPA registry. Such composition does not transfer decision semantics from the external protocol into ARPA.

## External Authoritative Evidence

When an external trust query materially contributes to an ARPA authority result, the evaluator MUST retain, directly or by stable reference:

* the external protocol and protocol version;
* source registry or endpoint identity;
* governing authority/trust-domain context when supplied;
* the query inputs material to the result;
* requested/effective time and evaluation time when applicable;
* the returned authorization/recognition result;
* freshness, validity, or expiry information;
* integrity/authentication evidence available to the evaluator; and
* enough source/checkpoint information to reproduce the material evaluation.

An external affirmative result MUST NOT bypass ARPA lifecycle, delegation, action-binding, conflict, critical-extension, freshness, or relying-policy rules.

## ToIP Trust Registry Query Protocol

The Trust Over IP Trust Registry Query Protocol (TRQP) v2.0 {{TRQP-V2}} defines read-only Authorization and Recognition queries over trust registries.

An ARPA implementation MAY use a TRQP Authorization response as evidence that an authority states that an entity is authorized for an action/resource context. It MAY use a TRQP Recognition response as evidence about authority recognition.

A TRQP result MUST be treated as evidence input to ARPA evaluation, not as an ARPA `allow` result by substitution. The ARPA evaluator MUST still determine whether the evidence is current, applicable to the exact action context, within the relevant delegation/recognition scope, and compatible with other material authority state.

TRQP v2.0 does not standardize Delegation queries. ARPA delegation processing therefore MUST NOT depend on a hypothetical TRQP delegation operation. If a later TRQP revision supplies delegation evidence, ARPA MAY consume it only when the evidence preserves ARPA monotonic delegation, parent linkage, lifecycle, temporal, and provenance requirements.

## ToIP Trust Spanning Protocol

The Trust Over IP Trust Spanning Protocol (TSP) {{TOIP-TSP}} defines a spanning-layer mechanism for authenticated and optionally confidential exchanges between endpoints identified by Verifiable Identifiers. The current ToIP specification is experimental.

An ARPA deployment MAY carry ARPA messages over TSP or use a TSP relationship as one source of endpoint/authentication evidence. TSP support is not required for ARPA conformance.

Establishing a TSP relationship, secure channel, or VID binding MUST NOT by itself establish delegated authority, governance recognition, authorization for an action, collective-principal approval, or current lifecycle validity.

A TSP VID MAY be retained as an external or alternate identifier under ARPA mapping rules. This revision does not standardize a TSP-VID-to-`agentreg:` projection.

## Action Vocabulary and TRQL

ARPA requires an explicit action/action-class context and stable action binding where replay or substitution is possible. This revision does not require the ToIP Trust Registry Query Language (TRQL) or any universal action vocabulary.

A deployment MAY map a governance-defined or TRQL-defined action vocabulary into the ARPA action context when the mapping is explicit, versioned, and does not broaden authority.

# Conformance Evidence and Specification Precedence

The wider ARPA project maintains JSON Schemas, controlled registries, conformance vectors, and validators for the Candidate specification. Candidate v0.10.0 and PP-03 artifacts at repository commit `7200c8512a13615d84c9711ac550da36ae338dd9` are informative implementation and test evidence for the wire semantics promoted by this revision.

Those external project artifacts do not override this document for IETF conformance.

Where this Internet-Draft and the wider ARPA Candidate Specification conflict on protocol-core behavior defined by this document, this Internet-Draft is authoritative for conformance to this Internet-Draft. The Candidate Specification remains authoritative for project governance, assurance, profiles, redress, implementation guidance, and other material outside this document's scope.

A conforming implementation SHOULD test both positive and negative boundary cases for `not_applicable`, half-open time validity, collective-principal snapshot binding, parent authority linkage, unknown material errors/extensions, and externally sourced authority evidence.

# Additional Composability Notes

The WIMSE architecture {{WIMSE-ARCH}} treats AI/ML intermediaries and delegated workloads as a workload-identity problem that can involve multi-hop delegation. ARPA supplies registry-visible authority, lifecycle, and action-bound evidence; it does not replace workload authentication.

The cross-organizational delegation problem statement {{WIMSE-CROSS-ORG}} describes requirements for authority that crosses administrative boundaries. ARPA's monotonic delegation and evidence-resolution semantics address one protocol layer of that problem without claiming to solve workload authentication or token issuance.

Where a deployment uses SCITT {{RFC9943}}, a SCITT receipt identifier MAY be carried as an ARPA evidence reference. A SCITT receipt, log entry, or transparency inclusion MUST NOT by itself confer agent authority.
