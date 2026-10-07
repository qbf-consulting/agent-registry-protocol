---
layout: default
title: "External implementation interoperability profile"
nav_exclude: true
document_status: informative
---

# External implementation interoperability profile

This profile defines a bounded way for an implementation operated outside the ARPA repository's maintainer organization to produce reviewable interoperability evidence against **ARPA Candidate Specification v0.10.0**. It packages a reusable test selection and an evidence format. It does not change the Candidate Specification or itself establish conformance.

## Current evidence state

The checked-in `evidence-report-template.json` is intentionally `not_run`. The repository has not yet received a qualifying external execution through this profile. A structurally valid template is not interoperability evidence and does not satisfy the external implementation gate for v1.0.

## Profile scope

Profile `arpa-external-implementation-interop` version `1.0.0` selects 16 existing vectors from the PP-04 protocol interoperability and PP-03 wire-contract suites. They exercise identifier and field handling, non-affirmative authority outcomes, stale state, freshness, conditional update, event-gap handling, critical extensions, dereference safety, applicability, revocation, half-open time intervals, and clock ambiguity. The profile manifest pins each source file by SHA-256 and each case by ID and expected outcome. The repository validator detects drift; updating the selected corpus requires a reviewed profile revision.

This is a semantic interoperability profile, not a complete ARPA profile claim. It does not cover every Candidate requirement, production deployment, cryptographic assurance, federation, governance operation, or security certification. A participant may report unsupported cases; those cases remain gaps and cannot be counted as passes.

## Running the profile

1. Obtain the exact repository revision and profile artifacts identified in `profile-v1.0.json`.
2. Operate the implementation under test independently from the ARPA repository maintainers. Record the operator and implementation provenance and disclose material relationships. Repository ownership alone does not establish organizational independence.
3. Execute each listed vector against the implementation's documented interface. Record the exact observed protocol outcome; do not substitute a local reimplementation of the expected result or merely validate the input fixture.
4. Retain a sanitized request/response, protocol trace, or equivalent per-case artifact. Include its relative path and SHA-256 digest. Remove credentials, private keys, personal data, and unrelated operational details before publication.
5. Populate a report conforming to `evidence-report.schema.json`. Preserve failures, unsupported cases, indeterminate outcomes, and missing evidence as such.
6. Run `make external-interop-check REPORT=path/to/report.json` to validate the profile pin, report shape, selected cases, expected outcomes, and evidence digests.
7. Submit the report and referenced artifacts for maintainer review. The validator checks structure and consistency; it cannot establish operator independence, authenticity of captured traces, or correctness of an implementation. Those require review of provenance and evidence.

## Interpretation

- `not_run` means no execution has been presented.
- `in_progress` means results are incomplete and cannot support an overall pass.
- `complete` means all profile cases have results; the validator derives `PASS`, `FAIL`, or `INDETERMINATE` from those results and their evidence.
- A pass means only that the submitted evidence supports these selected cases for the identified implementation and run. It is not certification, legal recognition, production security approval, or universal interoperability.
- A digest protects artifact integrity after capture; it does not prove who created the artifact or that it is truthful.

No new dependencies or runtime endpoint are required by this profile. Test execution is performed by the participant against their implementation; the repository tooling validates the evidence package and does not contact external systems.
