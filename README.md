---
layout: default
title: "Agent Registry Protocol"
nav_exclude: true
---

# Agent Registry Protocol

[![Specification status](https://img.shields.io/badge/spec-v0.9.1%20hardening-blue)](https://qbf-consulting.github.io/agent-registry-protocol/spec/agent-registry-protocol-v0.9.1-hardening.html)
[![Validation](https://github.com/qbf-consulting/agent-registry-protocol/actions/workflows/validate.yml/badge.svg)](https://github.com/qbf-consulting/agent-registry-protocol/actions/workflows/validate.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/spec-CC%20BY%204.0-lightgrey.svg)](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/LICENSE-CONTENT)
[![Code: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-lightgrey.svg)](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/LICENSE-CODE)

**A modular authority-control protocol for governed agent identity, delegation, recognition, lifecycle, evidence, enforcement and redress.**

> An agent registry is not merely a directory. It is an authority control plane whose claims must be scoped, revocable, inspectable and enforceable.

**Author and maintainer:** Sankarshan Mukhopadhyay, QBF Consulting LLP — `sankarshan@qbfconsulting.digital`  
**Project stewardship:** QBF Consulting LLP

## Repository status

| Attribute | Value |
|---|---|
| Portfolio tier | Flagship |
| Maturity | Pilot ready |
| Lifecycle | Active |
| Operational status | Active validation |
| Specification status | Candidate hardening |
| Implementation release | v0.9.5 |
| Normative baseline | v0.9.0 Candidate Specification + v0.9.1 adversarial-hardening amendment |
| Primary artifacts | Specification, schemas, API/event contracts, reference implementations, conformance and evidence |
| Release gate | `make release-check-all` |
| Candidate evidence | `artifacts/candidate-specification/evidence-bundle.json` |
| Authority | Repository-local status and scope in `PROJECT-STATUS.yaml`; process in `GOVERNANCE.md` |

## What the v0.9.1 hardening adds

The v0.9.1 Candidate amendment closes adversarially exploitable ambiguity without changing the core ARPA architecture. It adds:

- monotonic delegation intersection and explicit subset-proof requirements;
- half-open validity intervals and explicit clock/event-ordering behavior;
- a narrow definition of `not_applicable` so it cannot bypass authority failure;
- stricter handling of conflicts between simultaneously competent authoritative sources;
- explicit separation of revocation effectiveness from enforcement convergence;
- decision-reproducibility requirements over evaluation time and source checkpoints;
- minimum proof-input semantics beyond canonicalization alone;
- monotonic composition rules for independent status dimensions;
- privacy-preserving cross-context continuity requirements for scoped identifiers;
- a schema-correction authority boundary; and
- a release-gated adversarial conformance corpus with 20+ hostile boundary cases.

The normative amendment is [ARPA v0.9.1 Adversarial Hardening](spec/agent-registry-protocol-v0.9.1-hardening.md). The underlying consolidated Candidate architecture remains [ARPA v0.9.0](spec/agent-registry-protocol-v0.9.0.md); for v0.9.1 conformance the two are evaluated together, with the amendment controlling where it narrows or resolves an ambiguous v0.9.0 rule.

## What v0.9.5 delivers

- an independent TypeScript v0.3.0 implementation track over shared normative artifacts;
- 27/27 Python↔TypeScript deterministic and historical outcome-equivalence checks;
- a thin TypeScript HTTP service, reusable `ArpaClient`, and 7/7 network interoperability checks;
- A2A publication/compatibility adapters with explicit discovery-is-not-authority semantics;
- a task-oriented documentation architecture organized around Understand, Build, Assure, Operate, Integrate, and Govern;
- deterministic historical authority resolution separating requested-time state from current state;
- explicit reconstruction quality, selected-record provenance, later material events, historical-effect and retention semantics;
- fifteen release-gated historical-resolution vectors with machine-readable evidence;
- eight release-gated governance/privacy assurance vectors covering administrative capture, revocation convergence, federation conflict, restricted discovery and compromise restoration;
- portfolio-aligned `PROJECT-STATUS.yaml` with executable status/authority validation;
- A2A registry publication semantics separating portable Agent Cards, publication projections and authorization overlays;
- structured caller-visible discovery, exact Agent Card URI preservation and immutable snapshot/reference semantics;
- Agent Card compatibility classification and twelve additional registry-assurance vectors;
- an executable 15-minute path from clone to a resolved governed agent;
- a canonical sample registry, pilot kit and machine-readable readiness evidence;
- stable Candidate Specification requirements and conformance targets;
- hardened authority, delegation, recognition and fail-closed lifecycle semantics;
- two independently structured projection implementations with disclosed limits;
- network-boundary discovery and durable event replay, deduplication and acknowledgement tests;
- production-oriented proof, key and policy integration boundaries;
- machine-readable compatibility, requirement and evidence artifacts;
- an informative ARPA–TRQP governed query-projection profile with architecture guidance, mappings and 13 positive/negative vectors;
- flagship documentation, CI, GitHub Pages, contribution controls and AI-use governance.

## IETF Internet-Draft track

ARPA maintains a deliberately separate IETF authoring surface for the protocol core. The initial individual-draft series is **`draft-sankarshan-agent-registry-protocol`**. It does not replace the ARPA Candidate Specification or reuse ARPA semantic-version numbers.

The v0.9.1 hardening rules that affect the interoperable protocol core are synchronized into `ietf/fragments/adversarial-hardening.md`. The IETF build deterministically inserts that source fragment into the generated draft before RFCXML/TXT/HTML generation.

- [IETF authoring and submission guide]({{ '/ietf/' | relative_url }})
- [Protocol extraction map](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/ietf/PROTOCOL_EXTRACTION.md)
- [`-00` submission checklist](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/ietf/SUBMISSION_CHECKLIST.md)
- [Internet-Draft base source](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/ietf/draft-sankarshan-agent-registry-protocol.md)
- [IETF adversarial-hardening source fragment](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/ietf/fragments/adversarial-hardening.md)

Build and validate the draft with `make ietf-setup` followed by `make ietf-check`. GitHub Actions automatically regenerates RFCXML v3, TXT and HTML whenever an IETF source/build input changes and publishes the generated outputs through the Pages pipeline after complete publication validation. A project-level `spec/` edit alone does not rewrite IETF source; protocol-core changes must be synchronized explicitly, as this hardening work does.

## Start here

Choose the path that matches the decision you need to make:

- [Understand ARPA](docs/understand.md) — concepts, modules and non-implication rules.
- [Build ARPA](docs/build.md) — implementation paths, machine-readable artifacts and developer quickstarts.
- [Assure & Conform](docs/assure.md) — profiles, release gates and evidence.
- [Operate ARPA](docs/operate.md) — deployment, governance, security, privacy and lifecycle operations.
- [Integrate & Interoperate](docs/integrate.md) — A2A, TRQP and cross-runtime integration.
- [Govern & Contribute](docs/govern.md) — change control, releases and repository governance.

Use [Start Here](docs/start-here.md) for the decision router or the [documentation catalogue](docs/index.md) for the complete rendered surface.

## Validate and produce evidence

```bash
make setup
make release-check-all
```

The full gate validates the Python release surface, TypeScript conformance and historical semantics, A2A adapters, same-corpus Python↔TypeScript equivalence, loopback HTTP network interoperability, Candidate hardening requirements and adversarial vector structure.

## TypeScript and cross-runtime assurance

The [TypeScript implementation](docs/typescript-implementation.md) independently implements the supported ARPA semantics, exposes a development HTTP/client surface, and emits deterministic, historical, A2A and network interoperability evidence. Repository-owned implementation diversity improves pre-v1.0 assurance but does not substitute for externally operated independent implementation evidence.

## ARPA and TRQP

ARPA owns the authority, lifecycle, evidence, revocation, enforcement and federation control plane. TRQP is treated as an external, minimal read-only query interface. The optional v0.9.0 projection demonstrates how selected ARPA authorization and recognition state can be exposed without merging the protocols or implying cross-protocol conformance.

## Public specification review

The ARPA Candidate Specification is open for public review. Readers, implementers, standards practitioners, security and privacy reviewers, and other interested parties can use the repository's **Specification feedback** issue form to report ambiguities, governance or authority concerns, interoperability gaps, lifecycle problems, security/privacy risks, conformance issues, missing cases, or editorial improvements.

[Open a specification feedback issue](https://github.com/qbf-consulting/agent-registry-protocol/issues/new?template=specification_feedback.yml) or see [CONTRIBUTING.md](CONTRIBUTING.md) for review and contribution expectations.

## Licensing

ARPA uses **artifact-specific licensing** so that specification content and executable implementation artifacts have licenses suited to their use:

- **Specification and human-readable content:** [CC BY 4.0](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/LICENSE-CONTENT)
- **Code and executable/machine-readable artifacts:** [Apache License 2.0](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/LICENSE-CODE)

Machine-readable schemas, OpenAPI/AsyncAPI contracts, validators, test vectors, fixtures, mappings, executable configuration and generated machine-readable evidence are treated as software artifacts under Apache-2.0 unless a file explicitly states otherwise. Normative and informative specification prose, documentation, diagrams, governance prose, narrative examples and release notes are content under CC-BY-4.0.

See the repository [licensing map](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/LICENSE), [NOTICE](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/NOTICE), and machine-readable [artifact license policy](licensing/artifact-license-policy.json) for the deterministic classification rules.

## Assurance boundary

The supplied implementations, adversarial fixtures and loopback network tests are repository-controlled candidate evidence, not external certification or proof of universal interoperability. The release does not claim legal authority, production key custody, formal cryptographic review, independent TRQP approval, or completed revocation without enforcement acknowledgement. See [known limitations](KNOWN_LIMITATIONS.md), [AI usage](AI_USAGE.md), [governance](GOVERNANCE.md), and [security](SECURITY.md).
