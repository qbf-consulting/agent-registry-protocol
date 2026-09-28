# ARPA Internet-Draft `-03` Submission Package

This file records the governed repository evidence selected for the prospective submission of revision `-03` of the Agent Registry Protocol Internet-Draft. It preserves the published `-02` evidence in `SUBMISSION_PACKAGE_02.md` unchanged.

## Draft identity

- Draft: `draft-sankarshan-agent-registry-protocol-03`
- Title: Agent Registry Protocol
- Intended status: Standards Track
- Submission type: IETF individual submission
- Author: Sankarshan Mukhopadhyay
- Affiliation: QBF Consulting LLP
- Contact: `sankarshan@qbfconsulting.digital`
- Published predecessor: `draft-sankarshan-agent-registry-protocol-02` (23 September 2026, 34 pages)
- Generated candidate date: 28 September 2026
- Generated candidate expiry: 1 April 2027
- Generated candidate pages: 44

## Governed source state

Revision `-03` is prepared through PR #62 and tracked by issue #47.

- Selected protocol-content source commit: `055db6179c627f08fdef83681e17f61eeaee3541`
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

- stable authority-evaluation outcomes, including `not_applicable` as a normal policy/profile outcome distinct from protocol error, `deny`, and `indeterminate`;
- delegated parent-authority linkage using `derives_from` or an explicitly negotiated equivalent;
- inclusive `valid_from` / exclusive `valid_until` temporal boundaries;
- discoverable clock-skew, precision, and future-observation policy where material;
- single-snapshot collective-principal threshold/quorum evaluation;
- RFC 9457 ARPA Problem Details with stable core error codes;
- `application/agent-registry+json` as the ARPA-specific JSON media type and an IANA registration request;
- collision-resistant extension namespaces;
- stable core relationship and event vocabulary;
- provenance requirements for externally resolved trust/authority evidence;
- ToIP TRQP v2.0 Authorization/Recognition evidence composition without substituting TRQP results for ARPA decisions;
- independence of ARPA delegation from future TRQP delegation-query design;
- optional ToIP TSP carriage/authentication composition with a normative non-conferral rule;
- deferred TRQL dependency and deferred TSP VID-to-`agentreg:` projection;
- Candidate/IETF precedence for IETF conformance;
- WIMSE Architecture pinned to `draft-ietf-wimse-arch-08`;
- cross-organizational delegation pinned to `draft-reece-wimse-cross-org-delegation-02`; and
- optional SCITT receipt identifiers as evidence references without authority conferral.

The revision does not import A2A task/messaging semantics, business workflow, settlement, reputation, project assurance scoring, governance redress workflows, a universal action vocabulary, or mandatory TRQP/TSP/SCITT/WIMSE dependencies.

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

The equivalent pull-request-triggered IETF and Validate workflows also passed for the same protocol-content state.

## Rendered file digests

The selected IETF workflow artifact was downloaded and independently inspected.

| File | SHA-256 |
|---|---|
| `draft-sankarshan-agent-registry-protocol-03.xml` | `ce2ce9f5a30cb43b94e77e2d5eaf8a1a274cedd4eb62dd60993aee560ceb3ec4` |
| `draft-sankarshan-agent-registry-protocol-03.txt` | `86e137d302ffeab0ac4f98ef8040197aecc3e9be3ab38c8af6bec544da88d432` |
| `draft-sankarshan-agent-registry-protocol-03.html` | `1bbc27b18706bfd144b8f05577b87d5079a593cab9aa62ce0ce7d08997437317` |

## Manual artifact review

The generated `-03` artifacts were reviewed for:

- correct draft identity `draft-sankarshan-agent-registry-protocol-03`;
- Standards Track intended status and Individual Submission presentation;
- QBF Consulting LLP affiliation and author contact;
- successful RFCXML v3, plaintext and HTML rendering;
- absence of `TODO`, `FIXME`, `TBD`, and placeholder residue;
- preservation of the `agentreg` URI-scheme and `agent-registry` well-known URI IANA requests;
- presence of the `application/agent-registry+json` media-type registration;
- removal of stale `operated-by` / `authorized-by` relationship spellings from the rendered draft;
- consistent `valid_from` / `valid_until` temporal naming;
- presence of core ARPA error, relationship, and event vocabularies;
- presence of the Wire-Contract Precision for Revision 03 section;
- presence of Federated Trust Resolution and ToIP Composition;
- TRQP v2.0 treated as external evidence input rather than substituted authorization;
- TSP treated as optional and non-conferring;
- WIMSE references pinned to the reviewed revisions;
- SCITT evidence-reference composition retaining the non-conferral rule;
- Candidate v0.10.0 precedence wording;
- presence of a specific `-03` changelog entry; and
- absence of unrelated project/profile promotion.

The selected plaintext renders as 44 pages versus 34 pages for published `-02`.

A normalized `-02 → -03` textual diff was reviewed. Apart from revision identity, generated date/expiry, table-of-contents/page-flow changes, reference updates, and the governed `-03` additions/corrections, no unintended protocol-semantic churn was identified.

## Submission disposition

**Repository disposition: READY FOR FINAL IETF SUBMISSION CHECKS.**

The repository, generated artifact, semantic-diff, and manual-review gates are complete. Remaining actions are intentionally external publication actions:

1. run final IETF Author Tools/submission validation against the selected RFCXML v3;
2. upload the RFCXML v3 as revision `-03` of the existing Datatracker document;
3. verify Datatracker/IETF archive publication; and
4. update repository publication evidence with the canonical `-03` URL/date and closeout state.

Until those external actions occur, this package records a submission-ready `-03` candidate, not a published revision.
