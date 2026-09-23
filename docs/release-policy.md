---
layout: default
title: "Release Policy"
nav_exclude: true
---

# Release Policy

ARPA maintains distinct version authority surfaces for the Candidate Specification, repository implementation releases, schemas where separately versioned, and IETF Internet-Draft revisions. A change in one surface does not silently advance another.

A Candidate minor release is warranted when approved normative amendments are consolidated into a new authoritative baseline or when compatible protocol semantics materially advance. Repository implementation releases remain independently numbered and MUST NOT be inferred from the Candidate version alone. A repository release is warranted for a new normative capability, machine-verifiable artifact, material interoperability change, completed conformance gate, security or correctness fix, or adoption-ready workflow. Editorial-only changes should normally be batched.

## Readiness gates

A release candidate MUST pass `make validate`, `make test`, `make interop`, and `make report`. Release notes MUST state operational impact, compatibility, evidence produced, security implications, limitations, and migration requirements.

A Candidate Specification requires at least two independently developed interoperable implementations. Repository fixtures, generated variants, and AI-produced derivatives do not satisfy that gate.

## Workflow-based publication

GitHub Releases are published through `.github/workflows/release.yml`. The workflow is a publication control surface, not an alternative version authority.

A release may be initiated either by:

- merging exactly one versioned request under `.github/release-requests/` to `main`; or
- manually dispatching the workflow from `main` with an explicit tag, title, notes file, target commit, and prerelease flag.

Before creating a tag or GitHub Release, the workflow MUST validate the semantic tag, reject an existing tag/release, prove that the target commit is an ancestor of `main`, verify the release-notes file at the exact target, run `make release-check-all`, and run the complete Pages/IETF assurance path through `make pages-check`.

The workflow tags the exact validated target commit. A non-prerelease publication is marked as GitHub's latest release. Release-request files remain in the repository as publication provenance.

Candidate Specification versions, implementation-release versions, schema versions, and IETF Internet-Draft revisions remain independently governed even when a GitHub Release uses the same semantic tag as a Candidate baseline.
