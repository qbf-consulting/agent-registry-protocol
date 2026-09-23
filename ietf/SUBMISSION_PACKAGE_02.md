# ARPA Internet-Draft `-02` Submission Package

This file records the repository-generated evidence selected for the prospective submission of revision `-02` of the Agent Registry Protocol Internet-Draft. It does not modify or replace the published `-01` evidence in `SUBMISSION_PACKAGE_01.md`.

## Draft identity

- Draft: `draft-sankarshan-agent-registry-protocol-02`
- Title: Agent Registry Protocol
- Intended status: Standards Track
- Submission type: IETF individual submission
- Author: Sankarshan Mukhopadhyay
- Affiliation: QBF Consulting LLP
- Contact: `sankarshan@qbfconsulting.digital`
- Published predecessor: `draft-sankarshan-agent-registry-protocol-01` (21 September 2026)

## Governed source state

Revision `-02` is prepared through PR #46 and tracked by issue #45.

- Selected source commit: `072b900418cfb9a68e8f8dd23c152b899cf19950`
- Revision baseline: `REVISION_02_BASELINE.md`
- Machine-readable delta register: `spec-delta-v02.yaml`
- Candidate normative amendment: `ARPA-CAND-PP-02`
- Candidate amendment source: `spec/agent-registry-protocol-authority-commitment-pp02.md`
- Readiness checklist: `REVISION_02_CHECKLIST.md`

The checked-in `ietf/draft-sankarshan-agent-registry-protocol.md` continues to preserve the historical `-00` authoring baseline. The `-02` build is deterministic and reconstructs the published `-01` semantics plus governed `-02` additions.

## Material `-01 → -02` changes

Revision `-02` adds protocol-core semantics for:

- action-specific authority context and stable action binding;
- current effective authority and material constraint preservation;
- exact-action approval binding;
- collective-principal threshold/quorum/role exercise;
- current membership/controller and exercise-rule evidence;
- prevention of duplicate-controller counting;
- non-affirmative handling of missing, stale or indeterminate material composition evidence; and
- execution re-evaluation when the material action context changes.

It also adds explicit standards-context discussion and informative references for:

- WIMSE workload identity architecture;
- current cross-organizational workload/agent delegation work;
- OAuth 2.0 Token Exchange (RFC 8693);
- RATS architecture (RFC 9334); and
- SCITT architecture (RFC 9943).

The revision does not import A2A messaging/task semantics, TRQP projection, business workflow, settlement, reputation, threshold-cryptography choice, or ARPA project assurance scoring into the IETF core.

## Validation and artifact evidence

The selected source state passed both principal repository gates.

### Dedicated IETF workflow

- Workflow: `IETF Internet-Draft`
- Workflow run: `35804043176` — PASS
- Run number: `214`
- Workflow source SHA: `072b900418cfb9a68e8f8dd23c152b899cf19950`
- Artifact ID: `10727095787`
- Artifact name: `draft-sankarshan-agent-registry-protocol-02`
- Artifact SHA-256: `8bd7f1ce730515371c96e5881afb1ad9b6e874b1f024286843b9b2091298e37b`

### Full repository validation

- Workflow: `Validate`
- Workflow run: `35804043408` — PASS
- Workflow source SHA: `072b900418cfb9a68e8f8dd23c152b899cf19950`
- Repository job: PASS
- Pages/publication job: PASS

## Rendered file digests

The selected IETF workflow artifact was downloaded and independently inspected.

| File | SHA-256 |
|---|---|
| `draft-sankarshan-agent-registry-protocol-02.xml` | `021dfbfcd3a34f3b72b98dba49b7264f6c4a8265f5ab354c4072ec3f50d8eb95` |
| `draft-sankarshan-agent-registry-protocol-02.txt` | `ecfb4ec0792627e64581aaae8b1bd72404f2c69ea850b389243f93eab0e47b26` |
| `draft-sankarshan-agent-registry-protocol-02.html` | `11a7ec3113fb219716074da687603b208902a002694f7ad4f31b266ea76e40ba` |

## Manual artifact review

The generated `-02` artifacts were reviewed on 2026-09-23 for:

- correct draft identity `draft-sankarshan-agent-registry-protocol-02`;
- Standards Track intended status;
- QBF Consulting LLP affiliation and author contact;
- successful RFCXML v3, plaintext and HTML rendering;
- absence of `TODO`, `FIXME`, `TBD` and placeholder residue;
- preservation of the `agentreg` URI-scheme and `agent-registry` well-known URI IANA requests;
- presence of Action-Specific Authority Evaluation and Collective Principals sections;
- presence of the Relationship to Adjacent IETF Work section;
- informative references to RFC 8693, RFC 9334, RFC 9943, WIMSE architecture and cross-organizational delegation work;
- preservation of the ARPA non-implication boundaries;
- presence of a specific `-02` changelog entry; and
- absence of unrelated project-profile promotion.

The selected plaintext renders as 34 pages versus 29 pages for the published `-01` artifact. A normalized `-01 → -02` textual diff was reviewed. Apart from generated date/expiry/page-flow changes, the semantic differences are confined to the governed `-02` additions and their references/changelog.

## Submission disposition

**Repository disposition: READY FOR FINAL IETF SUBMISSION CHECKS.**

The repository, generated artifact and semantic-diff gates are complete. Remaining actions are intentionally external publication actions:

1. run the final IETF Author Tools/submission validation against the selected RFCXML v3;
2. upload the RFCXML v3 as revision `-02`;
3. verify Datatracker publication; and
4. record the published URL/date as repository closeout evidence.

Until those actions occur, this file records a submission-ready candidate, not a published `-02`.
