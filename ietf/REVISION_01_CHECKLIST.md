# ARPA Internet-Draft Revision `-01` Readiness Checklist

**Target:** `draft-sankarshan-agent-registry-protocol-01`  
**Tracking issue:** #32  
**Submission-evidence issue:** #35  
**Published baseline:** `draft-sankarshan-agent-registry-protocol-00`

This checklist governs preparation and submission of revision `-01`. It does not alter or replace the retained `-00` submission checklist and package evidence.

## 1. Change authority and traceability

- [x] Published `-00` identified as immutable baseline.
- [x] Human-readable `-00 → -01` baseline review recorded in `REVISION_01_BASELINE.md`.
- [x] Machine-readable disposition register recorded in `spec-delta-v01.yaml`.
- [x] Each accepted normative delta identifies its governing ARPA source and evidence.
- [x] Base-only/deferred semantics are explicitly excluded from the IETF core.
- [x] Protocol-precision work uses stable amendment ID `ARPA-CAND-PP-01` instead of reusing implementation-release semver.

## 2. Candidate Specification source semantics

- [x] `agentreg:` identifier contradiction resolved through Candidate amendment `ARPA-CAND-PP-01`.
- [x] Historical-resolution minimum semantics defined independently of HTTP path layout.
- [x] RFC 9457 Problem Details machine contract defined.
- [x] Critical-extension/version fail-safe semantics defined.
- [x] Machine-readable PP-01 requirement catalogue added.
- [x] Positive/negative PP-01 protocol-precision vectors added.
- [x] Cross-artifact validation script added.

## 3. IETF extraction

- [x] Existing adversarial-hardening fragment retained.
- [x] PP-01 protocol-precision fragment added.
- [x] `-01` build changes revision identity without mutating the checked-in `-00` authoring baseline.
- [x] `agentreg:` scheme semantics extracted into the generated `-01`.
- [x] RFC 7595 reference and permanent URI-scheme IANA request added by the governed build transform.
- [x] RFC 8615 promoted to a normative reference without duplicate reference identity.
- [x] `agent-registry` well-known URI suffix registration record added by the governed build transform.
- [x] Revision `-01` change log added to the generated draft.
- [x] IETF extraction map updated.

## 4. Automated validation

- [x] `python3 scripts/validate_protocol_precision.py` passes in CI.
- [x] `python3 scripts/validate_ietf_draft.py` passes in CI.
- [x] `make ietf-check` builds and validates `-01` RFCXML/TXT/HTML.
- [x] Main repository validation passes.
- [x] Python and TypeScript implementation checks pass.
- [x] Cross-runtime conformance comparison and network interoperability pass.
- [x] GitHub Pages publication validation passes with `-01` generated artifacts.
- [x] Dedicated merged `-01` IETF workflow run `35338636601` completed successfully.
- [x] Exact workflow artifact and SHA-256 evidence recorded in `SUBMISSION_PACKAGE_01.md`.

`rfclint` is not available in the repository CI environment. The generated RFCXML succeeds through the repository's `xml2rfc` validation/build path. Submission-time IETF Author Tools/Datatracker validation remains the authoritative external pre-upload gate.

## 5. Protocol diff review

The source-level and generated-artifact semantic review is recorded in `REVISION_01_SEMANTIC_REVIEW.md`.

- [x] Every added or strengthened `MUST`, `MUST NOT`, `SHOULD`, and `MAY` reviewed for intentionality within the accepted `-01` propositions.
- [x] No project-only governance, A2A, TRQP, assurance-profile or redress semantics leaked into the I-D.
- [x] The `agentreg:` URI scheme syntax and IANA request are internally consistent.
- [x] Historical resolution remains a resolution/evidence operation rather than a legal determination.
- [x] Problem Details requirements avoid making sensitive authority/evidence details mandatory disclosure.
- [x] Unknown material critical extensions fail safely.
- [x] No reviewed change weakens the existing fail-safe authority invariants.
- [x] Revision `-01` change summary matches the reviewed semantic delta.

## 6. Submission artifact review

- [x] Generated plaintext reviewed for identity, metadata and readable rendering.
- [x] Generated RFCXML reviewed as the preferred Datatracker submission input.
- [x] Generated HTML retained and reviewed as rendering evidence.
- [x] No `TODO`, `FIXME`, `TBD`, or placeholder markers found in the selected artifact.
- [x] Exact XML/TXT/HTML SHA-256 digests recorded in `SUBMISSION_PACKAGE_01.md`.
- [x] RFC 7595/RFC 8615 references and the `-01` IANA registration records reviewed.
- [x] Change summary for `-01` is concise and matches the reviewed semantic diff.
- [x] No IETF source or governed `-01` semantic input changed after the selected successful workflow artifact; subsequent pre-evidence change was limited to Pages workflow publication alignment.

## 7. IETF submission hygiene and external gate

Repository acceptance and Datatracker acceptance remain separate gates. The earlier governed evolution tranche established the revision as **repository-ready for merge**; this evidence tranche establishes repository-side pre-submission readiness. Until the external **idnits**/IETF Author Tools/Datatracker validation is clean, the draft remains **not yet Datatracker-submission-ready**.

- [ ] Run IETF Author Tools/Datatracker validation against the exact selected `-01` XML/TXT files and resolve any blocking finding.
- [ ] Upload `draft-sankarshan-agent-registry-protocol-01.xml` as revision `-01` of the existing Datatracker document.
- [ ] Complete author verification/posting if requested by Datatracker.
- [ ] Record the published `-01` archive URL and publication date in `SUBMISSION_PACKAGE_01.md`.

## Repository decision

Revision `-01` is **repository-side pre-submission ready**. The governed semantic delta, generated artifacts, workflow evidence, manual review and cryptographic digests are recorded.

## Submission decision

The repository-side tranche is complete. The only remaining pre-publication activity is the **external IETF submission gate**: validate the exact selected artifact in the current IETF Author Tools/Datatracker path and, if no blocking finding remains, upload it as revision `-01`.

The repository does not claim that an Internet-Draft revision is published until Datatracker has accepted and posted it.
