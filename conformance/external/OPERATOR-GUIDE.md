---
layout: default
title: "External interoperability operator guide"
nav_exclude: true
document_status: informative
---

# External interoperability operator guide

This guide turns the [external implementation interoperability profile](README.md) into a repeatable operator workflow. The profile is a semantic test selection, not a universal HTTP test client: ARPA implementations may expose different transports and operations. The operator maps each selected case to the implementation's documented interface and records the observed protocol behavior with evidence.

## Before starting

Confirm that:

- the implementation can be identified by a version and source or release reference;
- the test operator is outside the ARPA repository maintainer organization, and can disclose relevant relationships;
- a test or staging environment is available, or the implementation can be exercised safely without production effects;
- the implementation can expose or inject the state needed by the cases, such as revoked authority, stale versions, event sequence gaps, and clock-skew ambiguity;
- test records and captured traces contain no live credentials, private keys, unnecessary personal data, or production secrets.

Do not invent API paths or treat the vector JSON as a complete wire request. Use the implementation's documented interface or test adapter. If a case cannot be exercised safely or the required state cannot be represented, record it as `blocked` or `indeterminate` with an explanation. Do not count an unexercised case as a pass.

## Prepare a run bundle

Use a clean checkout of the repository revision whose profile and vector digests you will test. The profile's normative baseline is Candidate v0.10.0. Record the ARPA repository commit under `execution.repository_revision`; record the implementation's own version, source, and commit under `implementation`.

From the ARPA checkout, install the declared validation dependencies and create a separate evidence directory:

```bash
python3 -m pip install -r scripts/requirements.txt
mkdir -p /path/to/arpa-run/evidence
cp conformance/external/evidence-report-template.json /path/to/arpa-run/report.json
```

Keep the report and evidence artifacts together. Artifact paths in the report are relative to the directory containing `report.json`; do not use absolute paths or `..` path segments. A simple layout is:

```text
arpa-run/
  report.json
  evidence/
    PP04-AER-02.json
    PP04-EXT-02.json
    ...
```

The JSON report needs the operator and implementation metadata, execution status and timestamps, and one result entry per selected case. The validator does not generate these observations. Record actual outcomes and attach sanitized evidence before setting `execution.status` to `complete`.

## Execute the selected cases

Use the exact vector input from the source path and case ID in `profile-v1.0.json`. This table describes the behavior to exercise and the profile outcome to record. It does not prescribe a particular endpoint or HTTP status where the Candidate contract leaves transport choice open.

| Case | Exercise | Expected profile outcome |
|---|---|---|
| `PP04-FIELD-02` | Submit conflicting `effective_from` and `valid_from` values in the same mapping context. | `reject` |
| `PP04-AER-02` | Evaluate the explicitly non-applicable policy case. Confirm it does not produce an affirmative authorization. | `non_affirmative` |
| `PP04-STATUS-02` | Evaluate an otherwise active record with security status `quarantined`. | `non_affirmative` |
| `PP04-ID-02` | Compare `agentreg:Registry:Agent` and `agentreg:registry:Agent`; the differing case must remain distinguishable. | Boolean `false` |
| `PP04-JCS-02` | Parse the supplied raw JSON with a duplicate `a` member before canonicalization. | `reject_duplicate_member` |
| `PP04-FRESH-02` | Evaluate at `00:06Z` when the supplied result expires at `00:05Z`. Use the vector's fixed time, not the wall clock. | `non_affirmative` |
| `PP04-PUT-02` | Apply `If-Match: v3` when the current version is `v4`. | `reject_stale` |
| `PP04-EVENT-02` | Present sequence 41 followed by 43 with 42 absent. Confirm resynchronization is required and no affirmative state is inferred across the gap. | `gap_resync_non_affirmative` |
| `PP04-WRITE-02` | Attempt the write with `authorized: false`, including the stated relationship context. | Error code `ARPA-RECORD-NOT-AUTHORIZED` |
| `PP04-EXT-02` | Process an unsupported extension marked critical. Confirm fail-closed behavior. | `fail_closed` |
| `PP04-SSRF-02` | Pass the supplied link-local metadata destination through the dereference policy check. **Do not make a network request to `169.254.169.254`.** | `reject` |
| `WC-004` | Evaluate an applicable authority request with delegation evidence missing. | `indeterminate` |
| `WC-005` | Evaluate an applicable request whose authority is explicitly revoked. | `deny` |
| `WC-006` | Evaluate exactly at `effective_from`, using the vector's fixed timestamp. | Boolean `true` |
| `WC-007` | Evaluate exactly at `effective_until`, using the vector's fixed timestamp. | Boolean `false` |
| `WC-009` | Inject the vector's four-second observation offset under the five-second skew profile while ambiguity remains unresolved. | `indeterminate` |

For text outcomes, `observed_outcome` uses the profile symbol shown above. For a boolean case, record the actual boolean. Preserve the raw response or test trace as evidence so a reviewer can assess how the symbol was derived. For rejection cases, include the machine-readable error details where available; a timeout or server error is not evidence of a correct protocol rejection.

Each case's evidence should show enough to reproduce and inspect the result: the sanitized input or operation, the observed response/state, relevant implementation version, and any setup needed to establish the test state. Avoid bundling unrelated logs or secrets. If evidence must be redacted, record what was removed and why.

## Record one result

Add a result object to `results` for every profile case. For example, after observing the revoked-authority case:

```json
{
  "case_id": "WC-005",
  "status": "pass",
  "observed_outcome": "deny",
  "notes": "Decision returned by the implementation's documented authority evaluation operation.",
  "evidence": [
    {
      "path": "evidence/WC-005.json",
      "sha256": "REPLACE_WITH_64_LOWERCASE_HEX_CHARACTERS",
      "media_type": "application/json",
      "description": "Sanitized request and response for revoked-authority case."
    }
  ]
}
```

Use `pass` only when the observed outcome matches the profile and the artifact supports that observation. Use `fail` for an observed mismatch, `indeterminate` when the implementation cannot safely determine the result, `blocked` when the case could not be run, and `not_run` for cases not yet attempted. Include evidence for every attempted case. Leave no required case out of the report; the validator will derive an incomplete run as `INDETERMINATE`.

For each evidence file, compute its digest from the run directory. For example:

```bash
cd /path/to/arpa-run
sha256sum evidence/WC-005.json
```

Copy the resulting lowercase SHA-256 value into the matching artifact entry. The validator checks that the referenced file exists under the report directory and that its bytes match the recorded digest.

## Validate and submit

While collecting results, keep `execution.status` as `in_progress`. Set `started_at` when execution begins and record the environment and ARPA repository revision. Once all 16 cases have a result, set the status to `complete` and add `completed_at`.

From the ARPA checkout, run:

```bash
make external-interop-check REPORT=/path/to/arpa-run/report.json
```

Expected validator outcomes:

- `NOT_ESTABLISHED`: the report is still `not_run`;
- `INDETERMINATE`: the report is in progress, cases are missing, or a result is blocked or indeterminate;
- `FAIL`: an attempted case failed or its observed outcome differs from the pinned expected outcome;
- `PASS`: all selected cases are present, marked pass, match the pinned outcomes, and have valid evidence references and digests.

A successful validator run confirms package consistency, not operator independence, implementation correctness, evidence authenticity, certification, or production readiness. Submit the report and only the reviewed, sanitized evidence artifacts as a pull request or other maintainer-agreed channel. The maintainer reviews operator provenance, test setup, and whether the evidence supports each reported observation.

## If the implementation cannot run a case

Do not modify the pinned profile to fit the implementation. Record the case as `blocked` or `indeterminate`, explain the missing capability or state setup, and retain any safe evidence of the limitation. A repeated gap may justify a future profile revision, adapter, or normative clarification, but that judgment should be made after the first external run is reviewed.
