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
- Workflow run: `35338636601` — PASS
- Workflow source SHA: `f7fb6cfd478224ce0371fe8339d2a7046967248f`
- Artifact ID: `10544087244`
- Artifact name: `draft-sankarshan-agent-registry-protocol-01`
- Artifact SHA-256: `e3eedd8869029d78d34df4719a764f982751732aade83b26ca9fd4a3d9dadff8`
- Artifact URL: <https://github.com/qbf-consulting/agent-registry-protocol/actions/runs/35338636601/artifacts/10544087244>

The only repository change after the source commit and before this submission-evidence tranche was a GitHub Pages workflow alignment change in `.github/workflows/pages.yml`; no IETF source, fragment, governed semantic input, or `-01` build transform changed.

## Rendered file digests

The selected workflow artifact was downloaded and independently inspected before this evidence record was prepared.

| File | SHA-256 |
|---|---|
| `draft-sankarshan-agent-registry-protocol-01.xml` | `15f1c1c70be10a202e9410ff90c5ef2cf9a395b66f626cf54d0507715cd13d48` |
| `draft-sankarshan-agent-registry-protocol-01.txt` | `78f267eecd1f9fae61b02a520fa99ab6663ad1953ba4de6ae691fae2f8e2a44f` |
| `draft-sankarshan-agent-registry-protocol-01.html` | `d8d9922b3136a1bd780207fc52c79c1ee7d7a24f0483e53f21a06e57aad09f69` |

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

The plaintext artifact identifies the document date as 18 September 2026 and the expiry date as 22 March 2027.

## Submission file

The preferred Datatracker input is:

`draft-sankarshan-agent-registry-protocol-01.xml`

The matching plaintext file may be supplied as the optional rendered form if desired. The HTML file is retained as review evidence and is not required as the primary submission input.

## Remaining external gate

Repository-side preparation is complete. Immediately before upload, the selected XML/TXT pair must still be passed through the IETF Author Tools/Datatracker submission validation path so that any current idnits or submission-system findings can be reviewed against the exact files being uploaded.

That submission-time validation is intentionally not represented as a repository CI result. If it reports no unresolved blocking finding, the XML may be uploaded as revision `-01` of the existing Datatracker document.

After publication, this file should be updated with the publication date and canonical `-01` archive URL, and `REVISION_01_CHECKLIST.md` should record submission/author verification as complete.
