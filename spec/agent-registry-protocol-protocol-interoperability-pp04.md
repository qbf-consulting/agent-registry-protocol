# ARPA Candidate Protocol Interoperability Amendment PP-04

**Amendment ID:** ARPA-CAND-PP-04  
**Status:** Candidate amendment for governed IETF revision -04 extraction  
**Applies to:** ARPA Candidate v0.10.0  
**Tracking:** issue #65

## Purpose

This amendment resolves protocol-level ambiguities that materially affect independent implementation, HTTP mutation safety, event consumption, authority evaluation, identifier processing, freshness, and dereference security. It does not alter the wider ARPA governance model and does not create a new Candidate minor version.

## 1. Canonical wire-name mapping

For protocol-core JSON representations, the Candidate wire names remain canonical for Candidate conformance. An IETF profile MAY use different field names only when it publishes an explicit, lossless mapping.

The following mappings are normative for the IETF extraction:

| Candidate field | IETF field |
|---|---|
| `effective_from` | `valid_from` |
| `effective_until` | `valid_until` |
| `schema_version` | `version` |

An implementation MUST NOT infer an omitted alternate field as unbounded, default, or equivalent unless the selected representation profile explicitly defines that mapping. A representation MUST NOT carry both names with conflicting values.

## 2. Authority evaluation result

A protocol-visible authority evaluation result MUST contain:

- `decision`;
- one or more `reason_codes`;
- `evaluation_time`;
- selected `policy.id`, `policy.version`, and `policy.applicable`;
- `conditions` when the decision is `allow_with_conditions`;
- material authority or evidence references when evidence contributed to the decision;
- a source checkpoint/version/digest when derived or historical state was used; and
- a freshness bound or stable freshness-policy reference whenever staleness can affect the result.

Only `allow` and `allow_with_conditions` are affirmative outcomes. `deny`, `indeterminate`, and `not_applicable` are non-affirmative and MUST remain semantically distinct.

## 3. Multi-dimensional status composition

Lifecycle, security, operational, and authority-status dimensions MUST be evaluated independently before producing an authority outcome.

A material `revoked`, `suspended`, `quarantined`, `compromised`, `retired`, or otherwise restrictive state MUST prevent an affirmative result unless the governing profile explicitly defines a narrower safe interpretation.

Unknown, stale, conflicting, or unsupported material status MUST produce a non-affirmative result.

A restrictive state MUST NOT be silently collapsed to `active`.

## 4. Agent Identifier processing

The `agentreg` identifier is a URI scheme with this profile syntax:

~~~~
agentreg:<registry-namespace>:<agent-local-id>
~~~~

The two scheme-specific components MUST be non-empty URI path-compatible strings. The first literal colon after the scheme separates the registry namespace from the local identifier.

The scheme name is case-insensitive as required by URI processing. The scheme-specific identifier components are case-sensitive unless the assigning registry defines and publishes a stronger normalization rule.

Percent-encoded octets MUST NOT be decoded before identifier equality comparison except where the assigning registry's published normalization profile explicitly permits an equivalent normalization. Producers SHOULD emit a single canonical spelling and MUST NOT use percent-encoding to disguise delimiter characters.

Unicode labels SHOULD be normalized before assignment under the registry's naming policy, and registries MUST address confusable/homograph risk when human-readable identifiers are used.

## 5. JSON proof canonicalization

Where a JSON proof mechanism signs or hashes an ARPA JSON representation and the selected proof profile does not define another canonicalization, RFC 8785 JSON Canonicalization Scheme (JCS) MUST be used.

Duplicate JSON member names MUST be rejected before proof verification or canonicalization.

A valid proof establishes integrity/authenticity only for the covered representation. It MUST NOT substitute for current lifecycle, authority, policy, or status evaluation.

## 6. Freshness and cache safety

A response carrying material authority or status MUST expose enough information to determine freshness through one or more of:

- `generated_at`;
- `valid_until`;
- authoritative `source_time`;
- source checkpoint/version/digest; and
- a stable freshness-policy reference.

Derived or projected state MUST identify its authoritative source and material lag or observation time.

A cache lifetime MUST NOT outlive the material validity/freshness bound used for authority evaluation. When material freshness cannot be established, the result MUST remain non-affirmative.

## 7. Registration idempotency

ARPA core does not mandate a universal application-level idempotency header for registration. Automatic replay of a non-idempotent registration request is unsafe unless a negotiated deployment profile defines an idempotency mechanism.

A deployment profile that supports retry-safe registration MUST define a stable idempotency key, replay window, duplicate-detection scope, and deterministic response semantics.

## 8. PUT replacement and versioning

`PUT /agents/{id}` replaces the current representation by creating a new historical version; it MUST NOT erase prior versions.

The path identifier and logical subject identity MUST NOT change through PUT.

A conforming mutable registry MUST support a precondition mechanism such as `If-Match`/ETag or an equivalent version/checkpoint precondition and MUST reject stale concurrent replacement.

Omission of a material prohibition, constraint, delegation bound, or restrictive status during replacement MUST NOT silently widen authority. Any widening requires explicit governing authority and evidence.

## 9. Event stream contract

When an implementation advertises an ARPA event endpoint, each event MUST carry a stable event identifier and source ordering position or checkpoint sufficient to detect gaps within that source.

Consumers MUST process duplicate events idempotently.

A consumer detecting a material sequence gap MUST NOT continue to assert affirmative state based only on the incomplete stream. It MUST resynchronize from an authoritative snapshot/checkpoint or produce a non-affirmative result.

The endpoint metadata MUST declare delivery and replay semantics, including whether replay from a checkpoint is supported.

## 10. Write authorization

Protocol write authorization is default-deny.

A registry MUST expose or stably reference the policy controlling which authenticated principals may create, replace, or append relationship, authority, and status records.

Operator or controller status alone MUST NOT imply permission to mutate unrelated accountability, delegation, recognition, or authority records.

Unauthorized mutation MUST fail with an ARPA Problem Details response using a stable authorization error code.

## 11. Critical extensions

`critical` is the normative term for an extension whose non-recognition can affect authority, lifecycle, security, privacy, or evidence semantics.

Unknown critical extensions MUST fail closed. The terms `ignorable` and `non-ignorable` are legacy wording and MUST NOT be used as independent normative categories.

## 12. Dereference security

For evidence, federation, source, and other dereferenceable references, implementations MUST apply SSRF controls.

At minimum:

- only profile-authorized URI schemes may be dereferenced;
- the resolved destination MUST be checked against the deployment's allowed-origin/network policy;
- loopback, link-local, multicast, and private/internal destinations MUST be rejected unless explicitly trusted by profile;
- redirect targets MUST be revalidated;
- DNS resolution and redirects MUST be handled so that rebinding cannot bypass destination policy;
- request and response size/time limits MUST be enforced; and
- ambient credentials, cookies, or authorization headers MUST NOT be forwarded across origins unless explicitly authorized.

Dereference failure or blocked dereference MUST NOT produce an affirmative authority result.

## 13. Discovery boundary

`/.well-known/agent-registry` is registry capability and metadata discovery.

`GET /agents` is search/listing within a registry already selected by the caller.

Permission to discover registry metadata MUST NOT imply permission to enumerate agents.

## 14. Conformance evidence

Every IETF -04 normative proposition promoted from this amendment MUST have at least one positive and one hostile/negative fixture.

The -04 IETF conformance matrix MUST identify the applicable role, requirement, positive fixture, negative fixture, and expected outcome.

## Compatibility classification

- Sections 1, 2, 4, 8, and 10 are potentially breaking where implementations relied on ambiguity.
- Sections 3, 5, 6, 7, 9, 11, 12, 13, and 14 are clarifying or additive hardening, except where an implementation previously relied on unsafe behavior.
