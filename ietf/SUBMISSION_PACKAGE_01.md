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
- Workflow run: `35647140995` — PASS
- Workflow source SHA: `157c4320b091c14d94040327c0d5b3a0ed3591f1`
- Artifact ID: `10660099894`
- Artifact name: `draft-sankarshan-agent-registry-protocol-01`
- Artifact SHA-256: `507ad8786f93e494fd6d112ce731caf8b9bf80c6f88b0d06d1572b8b4504cdd3`
- Artifact URL: <https://github.com/qbf-consulting/agent-registry-protocol/actions/runs/35647140995/artifacts/10660099894>

The selected artifact was rebuilt on the final pre-submission documentation branch after the evidence/checklist updates. No protocol source, fragment, governed semantic input, or `-01` build transform changed in this tranche. Comparison with the earlier successful `-01` artifact showed only generated document-date/expiry changes.

## Rendered file digests

The selected workflow artifact was downloaded and independently inspected before this evidence record was prepared.

| File | SHA-256 |
|---|---|
| `draft-sankarshan-agent-registry-protocol-01.xml` | `dcf2213336e3b0cd9286ecce6c6341d36b97b370a77b9bc69c57a5aac49b55cf` |
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
- preservation of the published `-00` baseline as historical evidence.

The selected plaintext artifact identifies the document date as 21 September 2026 and the expiry date as 25 March 2027. The earlier 18 September rendering was semantically identical apart from generated date/expiry text.

## Submission file

The preferred Datatracker input is:

`draft-sankarshan-agent-registry-protocol-01.xml`

The matching plaintext file may be supplied as the optional rendered form if desired. The HTML file is retained as review evidence and is not required as the primary submission input.

## Remaining external gate

Repository-side preparation is complete. Immediately before upload, the selected XML/TXT pair must still be passed through the IETF Author Tools/Datatracker submission validation path so that any current idnits or submission-system findings can be reviewed against the exact files being uploaded.

That submission-time validation is intentionally not represented as a repository CI result. If it reports no unresolved blocking finding, the XML may be uploaded as revision `-01` of the existing Datatracker document.

After publication, this file should be updated with the publication date and canonical `-01` archive URL, and `REVISION_01_CHECKLIST.md` should record submission/author verification as complete.
