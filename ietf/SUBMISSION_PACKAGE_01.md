# ARPA Internet-Draft `-01` Submission Package

This file records the exact repository-generated evidence selected for submission of revision `-01` of the Agent Registry Protocol Internet-Draft. It does not modify or replace the published `-00` evidence in `SUBMISSION_PACKAGE.md`.

## Draft identity

- Draft: `draft-sankarshan-agent-registry-protocol-01`
- Title: Agent Registry Protocol
- Intended status: Standards Track
- Submission type: IETF individual submission
- Author: Sankarshan Mukhopadhyay
- Affiliation: QBF Consulting LLP
- Contact: `sankarshan@qbfconsulting.digital`
- Published predecessor: `draft-sankarshan-agent-registry-protocol-00`

## Governed source state

Revision `-01` was prepared and merged through PR #33, `governance(ietf): prepare governed ARPA revision -01`.

- Merge/source commit: `f7fb6cfd478224ce0371fe8339d2a7046967248f`
- Tracking issue for the revision evolution: #32
- Revision baseline: `REVISION_01_BASELINE.md`
- Semantic review: `REVISION_01_SEMANTIC_REVIEW.md`
- Machine-readable delta register: `spec-delta-v01.yaml`
- Readiness checklist: `REVISION_01_CHECKLIST.md`

The checked-in `ietf/draft-sankarshan-agent-registry-protocol.md` intentionally retains the published `-00` authoring baseline. The `-01` build is produced deterministically by `scripts/build_ietf_draft.sh` from that retained baseline plus the governed revision fragments and explicit transforms.

## Validation and artifact evidence

The dedicated IETF workflow completed successfully for the merged `-01` preparation state.

- Workflow: `IETF Internet-Draft`
- Workflow run: `35648110289` — PASS
- Workflow source SHA: `6a55f6804cd0c3c9d606b6cd6c8535ac3e79bee8`
- Artifact ID: `10660732667`
- Artifact name: `draft-sankarshan-agent-registry-protocol-01`
- Artifact SHA-256: `3e546395e3ad8b41b7804114249f48594ca12b9b4b3e897b8fdb4369ba933d37`
- Artifact URL: <https://github.com/qbf-consulting/agent-registry-protocol/actions/runs/35647140995/artifacts/10660099894>

The selected artifact was rebuilt after the submission-time idnits3 check reported `SUBMISSION_TYPE_UNEXPECTED`. The governed `-01` build now removes the inherited `submissiontype: IETF` authoring metadata before RFCXML generation, because the existing Datatracker document has no stream recorded. The build fails if a `submissionType` attribute reappears. No protocol source semantics, fragment content, governed semantic input, IANA request, or conformance behavior changed.

## Rendered file digests

The selected workflow artifact was downloaded and independently inspected before this evidence record was prepared.

| File | SHA-256 |
|---|---|
| `draft-sankarshan-agent-registry-protocol-01.xml` | `3e7f94fdddad1853f87d997c1ba6b2a68b41e4a6d9ff20d7ec6dc3a25c80c066` |
| `draft-sankarshan-agent-registry-protocol-01.txt` | `61e9993c86acee827c11253b46d8fe03477446fdc3d1e1064e399bef61591254` |
| `draft-sankarshan-agent-registry-protocol-01.html` | `7adfae92a89e25c9e679d7fff9ae0992d15a14a10ba7c07c1b588db27c27ce20` |

## Manual artifact review

The generated artifacts were reviewed on 2026-09-22 for:

- correct draft name and revision: `draft-sankarshan-agent-registry-protocol-01`;
- title: `Agent Registry Protocol`;
- Standards Track intended status;
- author and affiliation metadata;
- readable plaintext rendering;
- RFCXML generation;
- HTML generation;
- absence of `TODO`, `FIXME`, `TBD`, or placeholder markers;
- presence of the governed `-01` change log;
- presence of the `agentreg` URI-scheme and `agent-registry` well-known URI IANA requests;
- preservation of the published `-00` baseline as historical evidence;
- absence of a `submissionType` attribute in generated `-01` RFCXML, matching the existing Datatracker document stream state.

The selected plaintext artifact identifies the document date as 21 September 2026 and the expiry date as 25 March 2027. The earlier 18 September rendering was semantically identical apart from generated date/expiry text.

## Published result

Revision `-01` was successfully submitted and posted to the IETF repository.

- Publication date: `2026-09-21`
- Draft: `draft-sankarshan-agent-registry-protocol-01`
- Group: Individual Submission
- Pages: 29
- IETF archive: <https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-01.txt>
- Datatracker: <https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/>
- HTMLized draft: <https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol>
- Diff from previous revision: <https://author-tools.ietf.org/iddiff?url2=draft-sankarshan-agent-registry-protocol-01>

The IETF archive is the immutable historical authority for the published `-01` revision. Repository changes after publication do not alter that artifact; future protocol changes are candidate work for `-02` or later.

## Submission disposition

The corrected RFCXML/TXT submission passed the submission checks and was posted as revision `-01`. The earlier `SUBMISSION_TYPE_UNEXPECTED` metadata issue was resolved before publication by omitting inherited stream metadata from the generated `-01` RFCXML while preserving the frozen `-00` authoring baseline.

This file now serves as the repository-side evidence binding the governed `-01` source/build state to the published IETF revision.
