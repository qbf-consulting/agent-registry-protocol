# ARPA Internet-Draft `-03` Submission Package

This file records the governed repository evidence, selected build artifact, and publication closeout for revision `-03` of the Agent Registry Protocol Internet-Draft. It preserves the historical `-00`, `-01`, and `-02` evidence packages unchanged.

## Published draft identity

- Draft: `draft-sankarshan-agent-registry-protocol-03`
- Title: Agent Registry Protocol
- Intended status: Standards Track
- Group: Individual Submission
- Published: 28 September 2026
- Pages: 44
- Author: Sankarshan Mukhopadhyay
- Affiliation: QBF Consulting LLP
- Contact: `sankarshan@qbfconsulting.digital`
- Published predecessor: `draft-sankarshan-agent-registry-protocol-02` (23 September 2026, 34 pages)
- IETF archive: <https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-03.txt>
- Datatracker: <https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/>
- HTMLized: <https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol>
- Diff from `-02`: <https://author-tools.ietf.org/iddiff?url2=draft-sankarshan-agent-registry-protocol-03>

## Governed source state

Revision `-03` was prepared through PR #62 and tracked by issue #47.

- Selected protocol-content source commit: `055db6179c627f08fdef83681e17f61eeaee3541`
- Merge commit: `81a0c228d2fb053ededd69a7bc57a98120a60b17`
- Published comparison baseline: `draft-sankarshan-agent-registry-protocol-02`
- Current ARPA project baseline: Candidate v0.10.0
- Candidate evidence baseline commit: `7200c8512a13615d84c9711ac550da36ae338dd9`
- Revision baseline: `REVISION_03_BASELINE.md`
- Machine-readable delta register: `spec-delta-v03.yaml`
- Governing Candidate hardening: `ARPA-CAND-PP-03`
- Readiness checklist: `REVISION_03_CHECKLIST.md`

The checked-in `ietf/draft-sankarshan-agent-registry-protocol.md` continues to preserve the historical `-00` authoring baseline. The `-03` build deterministically reconstructs the published revision lineage plus governed `-03` additions.

## Material `-02 → -03` changes

Revision `-03` adds or tightens protocol-core semantics for:

- stable authority-evaluation outcomes, including `not_applicable`;
- delegated parent-authority linkage;
- inclusive `valid_from` / exclusive `valid_until` temporal boundaries;
- discoverable clock-profile assumptions;
- single-snapshot collective-principal evaluation;
- RFC 9457 ARPA Problem Details and stable core error codes;
- `application/agent-registry+json` and its IANA registration request;
- collision-resistant extension namespaces;
- stable core relationship and event vocabulary;
- provenance requirements for externally resolved authority evidence;
- ToIP TRQP v2.0 Authorization/Recognition evidence composition without substituting TRQP results for ARPA decisions;
- independence of ARPA delegation from future TRQP delegation-query work;
- optional ToIP TSP composition with a normative non-conferral rule;
- Candidate/IETF precedence for IETF conformance;
- pinned WIMSE references; and
- optional SCITT receipt identifiers as evidence references without authority conferral.

TRQL dependency, TSP VID-to-`agentreg:` projection, A2A task/messaging semantics, business workflow, settlement, reputation, project assurance scoring, and governance redress workflows remain outside this revision.

## Validation and artifact evidence

### Dedicated IETF workflow

- Workflow: `IETF Internet-Draft`
- Workflow run: `36393777707` — PASS
- Workflow source SHA: `055db6179c627f08fdef83681e17f61eeaee3541`
- Artifact ID: `10956953699`
- Artifact name: `draft-sankarshan-agent-registry-protocol-03`
- Artifact bundle SHA-256: `bcae38ccf756c9d233896b5b1f7323d1c37c413026d4c0e47d9b664f850c7c12`

### Full repository validation

- Workflow: `Validate`
- Workflow run: `36393777797` — PASS
- Workflow source SHA: `055db6179c627f08fdef83681e17f61eeaee3541`
- Repository validation: PASS
- Pages/publication validation: PASS

Post-merge `main` validation, IETF build, Pages deployment, and CodeQL also completed successfully before submission.

## Rendered file digests

| File | SHA-256 |
|---|---|
| `draft-sankarshan-agent-registry-protocol-03.xml` | `ce2ce9f5a30cb43b94e77e2d5eaf8a1a274cedd4eb62dd60993aee560ceb3ec4` |
| `draft-sankarshan-agent-registry-protocol-03.txt` | `86e137d302ffeab0ac4f98ef8040197aecc3e9be3ab38c8af6bec544da88d432` |
| `draft-sankarshan-agent-registry-protocol-03.html` | `1bbc27b18706bfd144b8f05577b87d5079a593cab9aa62ce0ce7d08997437317` |

## Manual artifact review

The generated `-03` artifacts were reviewed for draft identity, Standards Track intended status, author/affiliation metadata, successful RFCXML/TXT/HTML rendering, absence of placeholder residue, preservation of existing IANA requests, the media-type registration request, consistent wire vocabulary, TRQP/TSP/WIMSE/SCITT composition boundaries, Candidate v0.10.0 precedence wording, and absence of unrelated project/profile promotion.

The selected plaintext renders as 44 pages versus 34 pages for published `-02`. A normalized `-02 → -03` diff was reviewed and no unintended protocol-semantic churn was identified.

## Published result

Revision `-03` was successfully submitted and posted to the IETF repository.

- Publication date: `2026-09-28`
- Draft: `draft-sankarshan-agent-registry-protocol-03`
- Group: Individual Submission
- Pages: 44
- IETF archive: <https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-03.txt>
- Datatracker: <https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/>
- HTMLized: <https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol>
- Diff from previous revision: <https://author-tools.ietf.org/iddiff?url2=draft-sankarshan-agent-registry-protocol-03>

The IETF archive is the immutable historical authority for published `-03`. Repository changes after publication do not alter that artifact; future protocol changes must be governed as `-04` or later work.

## Submission disposition

**PUBLISHED AND REPOSITORY-CLOSEOUT COMPLETE.**

The governed source/build state, rendered artifact review, publication metadata, and canonical IETF references are now bound together in this evidence record.
