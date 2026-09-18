# ARPA Internet-Draft Revision `-01` Semantic Review

**Target:** `draft-sankarshan-agent-registry-protocol-01`  
**Published baseline:** `draft-sankarshan-agent-registry-protocol-00`  
**Tracking issue:** #32  
**Review basis:** governed build transforms, IETF source fragments, machine-readable delta register, generated RFCXML/TXT/HTML validation

## Review purpose

This review records whether the `-00 → -01` change set alters protocol semantics only where the repository has an explicit governing proposition and evidence trail. It is not a general editorial review of the entire draft.

The published `-00` remains immutable. Revision `-01` is generated from the retained `-00` authoring baseline plus bounded transformations and two governed protocol-core fragments.

## Accepted semantic deltas

### 1. Agent Identifier alignment — `ARPA-IETF-001`

`-00` allowed any RFC 3986 URI scheme and stated that ARPA defined no new scheme. `-01` instead requires the ARPA Agent Identifier to use:

```text
agentreg:<registry-namespace>:<agent-local-id>
```

External identifiers remain distinguishable aliases or mapped identifiers. An unsupported external identifier scheme cannot be silently reinterpreted as the ARPA Agent Identifier.

**Disposition:** intentional normative clarification of the existing Candidate/OpenAPI contract.

**Interoperability consequence:** independently implemented ARPA Core endpoints now have one protocol identifier form rather than a deployment-selected URI scheme.

### 2. Adversarial authority processing

Revision `-01` imports the protocol-core subset of the Candidate adversarial-hardening amendment. The added requirements cover:

- semantic intersection of delegated authority;
- non-removal of upstream constraints/prohibitions by omission;
- half-open time boundaries;
- bounded use of `not_applicable`;
- non-affirmative handling of unresolved competent-source conflict;
- separation of revocation effectiveness from enforcement convergence;
- reproducible authority decisions using evaluation time and material source checkpoints; and
- proof-input semantics that do not treat successful signature verification as proof of current delegated authority.

**Disposition:** intentional protocol hardening. These rules narrow permissive ambiguity; they do not grant new authority.

### 3. Historical resolution — `ARPA-IETF-002`

Revision `-01` makes historical resolution a reconstruction operation rather than a timestamp-filtered current-state response. A successful result identifies requested time, evaluation/resolution time, selected-record provenance, later material events, and reconstruction quality or limitations.

Unavailable, conflicting, integrity-failed, or insufficiently reconstructable material evidence remains non-affirmative.

**Disposition:** intentional normative precision aligned with existing schema, implementation and conformance evidence.

**Boundary:** HTTP path layout remains discoverable rather than normative.

### 4. HTTP Problem Details — `ARPA-IETF-003`

Revision `-01` strengthens RFC 9457 Problem Details from recommended behavior to the interoperable ARPA HTTP error contract for protocol-significant failures, unless another governing transport profile defines an interoperable representation.

Machine behavior depends on stable problem type, HTTP status and stable ARPA code. Human-readable text is not the machine contract, and unknown material error semantics never become success.

**Disposition:** intentional normative precision.

### 5. Critical extension processing — `ARPA-IETF-004`

Revision `-01` requires material critical extensions to expose sufficient namespace/version identity for support determination. Unsupported material critical extensions fail non-affirmatively rather than being ignored.

Unknown non-critical extensions may be ignored or retained only when doing so cannot broaden authority, suppress restrictions or convert unknown/indeterminate state into success.

**Disposition:** intentional fail-safe extension rule.

### 6. IANA actions

Revision `-01` requests:

- permanent registration of the `agentreg` URI scheme under RFC 7595; and
- registration of the `agent-registry` well-known URI suffix under RFC 8615.

RFC 8615 is promoted from the `-00` informative reference set to the `-01` normative reference set rather than duplicated.

**Disposition:** required consequence of standardizing the protocol identifier and well-known discovery resource.

## Normative-language review

The added or strengthened BCP 14 language is confined to the accepted protocol-core propositions above. In particular:

- `MUST`/`MUST NOT` additions around `agentreg:` are limited to identifier interoperability and non-reinterpretation;
- authority-processing requirements only narrow or fail closed on ambiguity and do not create new grants;
- historical-resolution requirements govern evidence/reconstruction semantics and do not make a legal determination;
- Problem Details requirements govern machine-readable failure semantics;
- extension requirements govern safe processing of unknown material semantics; and
- IANA text creates registration requests, not runtime authority semantics.

No reviewed normative addition imports project-specific governance, A2A interoperability, TRQP projection, assurance certification/profile hierarchy, appeals/redress workflow, or a mandatory proof/signature suite.

## Scope-leak review

The following remain explicitly outside revision `-01`:

- project governance, appeals and redress;
- A2A profile semantics;
- TRQP projection;
- assurance scoring/certification and project conformance profiles;
- mandatory credential/proof/signature suite; and
- execution/decision receipts as an independent wire protocol.

No source-level `-01` transform or fragment reviewed here makes these IETF protocol requirements.

## Build and evidence review

The dedicated IETF gate requires:

```text
python3 scripts/validate_protocol_precision.py
python3 scripts/validate_ietf_draft.py
make ietf-check
```

The repository validation additionally exercises the Python implementation, TypeScript implementation, cross-runtime outcome equivalence and network interoperability. GitHub Pages separately validates publication reachability and the staged generated `-01` artifacts.

Generated RFCXML/TXT/HTML remain derivative evidence; the governed authoring sources and delta register remain the change-authority surfaces.

## Residual pre-submission checks

Repository acceptance does not substitute for Datatracker submission checks. Before uploading revision `-01`:

- inspect the final generated plaintext as the submission artifact;
- run the available IETF/Datatracker submission hygiene checks (including idnits or successor checks where available);
- confirm references and IANA considerations remain current at submission time; and
- ensure the uploaded artifact is byte-equivalent to the accepted generated revision.

These are submission-time gates, not reasons to leave the repository evolution tranche unmerged once repository CI and semantic review are green.

## Review conclusion

The `-00 → -01` semantic change set is bounded and traceable. The changes strengthen interoperability and fail-safe authority behavior without expanding ARPA into a general agent identity, messaging, invocation, governance, A2A or TRQP protocol. The revision may proceed through repository acceptance once the final CI run for the reviewed head is green.
