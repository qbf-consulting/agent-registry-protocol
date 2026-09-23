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
