# ARPA Internet-Draft Revision `-01` Readiness Checklist

**Target:** `draft-sankarshan-agent-registry-protocol-01`  
**Tracking issue:** #32  
**Published baseline:** `draft-sankarshan-agent-registry-protocol-00`

This checklist governs preparation of revision `-01`. It does not alter or replace the retained `-00` submission checklist and package evidence.

## 1. Change authority and traceability

- [x] Published `-00` identified as immutable baseline.
- [x] Human-readable `-00 → -01` baseline review recorded in `REVISION_01_BASELINE.md`.
- [x] Machine-readable disposition register recorded in `spec-delta-v01.yaml`.
- [x] Each accepted normative delta identifies its governing ARPA source and evidence.
- [x] Base-only/deferred semantics are explicitly excluded from the IETF core.

## 2. Candidate Specification source semantics

- [x] `agentreg:` identifier contradiction resolved through a Candidate amendment.
- [x] Historical-resolution minimum semantics defined independently of HTTP path layout.
- [x] RFC 9457 Problem Details machine contract defined.
- [x] Critical-extension/version fail-safe semantics defined.
- [x] Machine-readable v0.9.2 requirement catalogue added.
- [x] Positive/negative v0.9.2 protocol-precision vectors added.
- [x] Cross-artifact validation script added.

## 3. IETF extraction

- [x] v0.9.1 adversarial-hardening fragment retained.
- [x] v0.9.2 protocol-precision fragment added.
- [x] `-01` build changes revision identity without mutating the checked-in `-00` authoring baseline.
- [x] `agentreg:` scheme semantics extracted into the generated `-01`.
- [x] RFC 7595 reference and URI-scheme IANA request added by the governed build transform.
- [x] `/.well-known/agent-registry` IANA request added by the governed build transform.
- [x] IETF extraction map updated.

## 4. Automated validation

- [ ] `python3 scripts/validate_protocol_precision.py` passes in CI.
- [ ] `python3 scripts/validate_ietf_draft.py` passes in CI.
- [ ] `make ietf-check` builds and validates `-01` RFCXML/TXT/HTML.
- [ ] `rfclint` passes when available.
- [ ] Main repository validation passes for the branch.
- [ ] GitHub Pages publication validation passes with `-01` generated artifacts.

## 5. Protocol diff review

Before submission, review the generated `-00 → -01` semantic delta and confirm:

- [ ] every added or strengthened `MUST`, `MUST NOT`, `SHOULD`, and `MAY` is intentional;
- [ ] no project-only governance, A2A, TRQP, assurance-profile or redress semantics leaked into the I-D;
- [ ] the `agentreg:` URI scheme syntax and IANA request are internally consistent;
- [ ] historical resolution remains a resolution/evidence operation rather than a legal determination;
- [ ] Problem Details does not leak sensitive authority/evidence information;
- [ ] unknown critical extensions fail safely;
- [ ] no change weakens the v0.9.1 fail-safe authority invariants.

## 6. IETF submission hygiene

- [ ] Generated plaintext has been reviewed as the submission artifact.
- [ ] `idnits`/Datatracker submission checks have no unresolved blocking findings.
- [ ] References and IANA considerations are current.
- [ ] Change summary for `-01` is concise and matches the actual semantic diff.
- [ ] Datatracker upload is performed only after the repository PR is accepted and merged.

## Submission decision

Revision `-01` is **not submission-ready** until all unchecked automated-validation, semantic-diff, and submission-hygiene gates above are complete.
