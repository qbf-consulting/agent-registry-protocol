# Protocol Precision for Revision 01

This section carries protocol-core precision requirements derived from the ARPA v0.9.2 Candidate amendment. It does not import project-only governance, conformance profiles, A2A integration, TRQP projection, or redress workflows.

## Historical Resolution Semantics

Historical resolution is a reconstruction operation rather than a simple timestamp filter over current state.

A successful historical-resolution result MUST identify, directly or by stable reference:

* the requested effective time;
* the resolution or evaluation time;
* the material records selected as effective at the requested time;
* source and version or checkpoint provenance for selected material records;
* later material events known at evaluation time that affect interpretation; and
* reconstruction quality or limitations.

A registry MUST NOT silently substitute current state for requested-time state. It MUST NOT silently omit a later material event when that event changes safe interpretation of the historical result.

If material historical evidence is unavailable, conflicting, fails integrity validation, or cannot be reconstructed to the degree required by applicable policy, the result MUST remain non-affirmative and MUST expose the applicable reconstruction condition.

The HTTP path layout for the logical historical-resolution operation is discoverable rather than normative. A deployment MAY use an `at` parameter, a dedicated historical-resolution resource, or another unambiguous operation mapping, provided that the semantic result above is preserved.

## HTTP Problem Details

An ARPA HTTP API MUST represent protocol-significant errors using Problem Details {{RFC9457}} unless a governing transport profile defines another interoperable error representation.

A protocol-significant Problem Details response MUST provide a stable problem `type`, the applicable HTTP `status`, and a stable ARPA `code`. Human-readable `title` and `detail` text is informative and MUST NOT be the sole machine contract for client behavior.

A client that does not recognize an ARPA error code or Problem Details extension MUST NOT interpret the response as success. Unknown error semantics affecting authority, integrity, lifecycle, or historical reconstruction remain non-affirmative.

Problem extensions MAY include reason codes, correlation identifiers, and retry metadata. Such fields MUST NOT expose confidential evidence, hidden authority relationships, internal exception details, or other security-sensitive implementation state beyond the caller's authorization.

## Critical Extension Processing

An extension that can change interpretation of core identity, authority, lifecycle, evidence, proof, recognition, or decision semantics MUST declare whether it is critical to processing.

A critical extension MUST identify a namespace and version sufficient for a receiver to determine whether it supports the required semantics.

If a receiver does not understand or support a critical extension material to the requested operation, it MUST return a non-affirmative result or protocol error. It MUST NOT ignore the extension and continue as though it were absent.

Unknown non-critical extensions MAY be ignored or retained as opaque data only when doing so cannot change core interpretation, broaden authority, suppress a prohibition, hide a lifecycle restriction, or convert unknown or indeterminate state into success.

An extension MUST NOT redefine a core ARPA field in place. A semantic change to a core field requires an applicable protocol-version change.
