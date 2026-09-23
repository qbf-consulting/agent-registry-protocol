# ARPA Internet-Draft `-02` Submission Package

This file records the governed repository evidence, selected build artifact, and publication closeout for revision `-02` of the Agent Registry Protocol Internet-Draft. It does not modify or replace the historical `-00` or `-01` evidence packages.

## Published draft identity

- Draft: `draft-sankarshan-agent-registry-protocol-02`
- Title: Agent Registry Protocol
- Intended status: Standards Track
- Group: Individual Submission
- Published: 23 September 2026
- Pages: 34
- Author: Sankarshan Mukhopadhyay
- Affiliation: QBF Consulting LLP
- Contact: `sankarshan@qbfconsulting.digital`
- Published predecessor: `draft-sankarshan-agent-registry-protocol-01` (21 September 2026)
- IETF archive: <https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-02.txt>
- Datatracker: <https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/>
- HTMLized: <https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol>
- Diff from `-01`: <https://author-tools.ietf.org/iddiff?url2=draft-sankarshan-agent-registry-protocol-02>

## Governed source state

Revision `-02` was prepared through PR #46 and tracked by issue #45.

- Selected source commit: `072b900418cfb9a68e8f8dd23c152b899cf19950`
- Merge commit: `42c0376572dbfa1b97a8bcfb71b4c6a0273053e4`
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

It also adds explicit standards-context discussion and informative references for WIMSE workload identity architecture, cross-organizational workload/agent delegation work, OAuth 2.0 Token Exchange (RFC 8693), RATS architecture (RFC 9334), and SCITT architecture (RFC 9943).

The revision does not import A2A messaging/task semantics, TRQP projection, business workflow, settlement, reputation, threshold-cryptography choice, or ARPA project assurance scoring into the IETF core.

## Validation and artifact evidence

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

The post-merge IETF, repository, Pages/deployment, and CodeQL checks on `main` also completed successfully.

## Rendered file digests

| File | SHA-256 |
|---|---|
| `draft-sankarshan-agent-registry-protocol-02.xml` | `021dfbfcd3a34f3b72b98dba49b7264f6c4a8265f5ab354c4072ec3f50d8eb95` |
| `draft-sankarshan-agent-registry-protocol-02.txt` | `ecfb4ec0792627e64581aaae8b1bd72404f2c69ea850b389243f93eab0e47b26` |
| `draft-sankarshan-agent-registry-protocol-02.html` | `11a7ec3113fb219716074da687603b208902a002694f7ad4f31b266ea76e40ba` |

## Manual artifact review

The generated `-02` artifacts were reviewed on 23 September 2026 for draft identity, intended status, affiliation/contact metadata, successful RFCXML/TXT/HTML rendering, absence of placeholder residue, preservation of the IANA requests, presence of the new authority-at-commitment and collective-principal material, standards-context references, non-implication boundaries, and absence of unrelated project-profile promotion.

The selected plaintext renders as 34 pages versus 29 pages for published `-01`. A normalized `-01 → -02` textual diff was reviewed; apart from generated date/expiry/page-flow differences, the semantic changes are confined to the governed `-02` additions and their references/changelog.

## Published result

Revision `-02` was successfully submitted and posted to the IETF repository.

- Publication date: `2026-09-23`
- Draft: `draft-sankarshan-agent-registry-protocol-02`
- Group: Individual Submission
- Pages: 34
- IETF archive: <https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-02.txt>
- Datatracker: <https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/>
- HTMLized draft: <https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol>
- Diff from previous revision: <https://author-tools.ietf.org/iddiff?url2=draft-sankarshan-agent-registry-protocol-02>

The IETF archive is the immutable historical authority for published `-02`. Repository changes after publication do not alter that artifact; future protocol changes are candidate work for `-03` or later.

## Submission disposition

**PUBLISHED AND REPOSITORY-CLOSEOUT COMPLETE.**

The governed source/build state, rendered artifact review, publication metadata, and canonical IETF references are now bound together in this evidence record.
