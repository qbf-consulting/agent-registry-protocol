---
layout: default
title: "Agent Registry Protocol"
nav_exclude: true
---

# Agent Registry Protocol

[![Specification status](https://img.shields.io/badge/spec-Candidate%20v0.10.0-blue)](https://qbf-consulting.github.io/agent-registry-protocol/spec/agent-registry-protocol-v0.10.0.html)
[![Validation](https://github.com/qbf-consulting/agent-registry-protocol/actions/workflows/validate.yml/badge.svg)](https://github.com/qbf-consulting/agent-registry-protocol/actions/workflows/validate.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/spec-CC%20BY%204.0-lightgrey.svg)](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/LICENSE-CONTENT)
[![Code: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-lightgrey.svg)](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/LICENSE-CODE)

**A modular authority-control protocol for governed agent identity, delegation, recognition, lifecycle, evidence, enforcement and redress.**

> An agent registry is not merely a directory. It is an authority control plane whose claims must be scoped, revocable, inspectable and enforceable.

**Author and maintainer:** Sankarshan Mukhopadhyay, QBF Consulting LLP — `sankarshan@qbfconsulting.digital`  
**Project stewardship:** QBF Consulting LLP

## Why this repository exists

Autonomous and semi-autonomous agents are becoming operational participants in enterprise, public-sector and decentralized trust ecosystems. Existing identity, credential and trust-registry infrastructure can identify parties and carry assertions, but it does not by itself provide a common layer for registering agents, binding operators, evaluating delegated authority, recording lifecycle state, preserving evidence, reconstructing historical state and supporting challenge or redress.

This repository investigates that missing layer.

ARPA is the current reference protocol and implementation surface for this work. The broader repository is an **agent governance laboratory**: a place to test how registries, delegation, lifecycle controls, federation, evidence and assurance can work together without collapsing discovery into authority or registry state into certification.

## Repository status

| Attribute | Value |
|---|---|
| Portfolio tier | Flagship |
| Maturity | Pilot ready |
| Lifecycle | Active |
| Operational status | Active validation |
| Specification status | Candidate Specification v0.10.0 |
| Implementation release | v0.9.5 |
| Normative baseline | ARPA Candidate v0.10.0 consolidated specification |
| Primary artifacts | Specification, schemas, API/event contracts, reference implementations, conformance, evidence, research agenda and lab experiments |
| Release gate | `make release-check-all` |
| Candidate evidence | `artifacts/candidate-specification/evidence-bundle.json`, amendment-specific evidence, and `artifacts/conformance/candidate-consolidation-v0.10.0-validation.json` |
| Authority | Repository-local status and scope in `PROJECT-STATUS.yaml`; process in `GOVERNANCE.md` |

Implementation release numbers and Candidate-specification authority are intentionally distinct. An implementation release does not change the normative baseline merely because its semantic version advances.

## Start here

Choose the path that matches the decision you need to make:

- [Agent Governance Lab](docs/agent-governance-lab.md) — why this repository is broader than a protocol specification.
- [Research Agenda](docs/research-agenda.md) — open questions and near-term research increments.
- [Start Here](docs/start-here.md) — decision-oriented navigation through ARPA.
- [Understand ARPA](docs/understand.md) — concepts, modules and non-implication rules.
- [Build ARPA](docs/build.md) — implementation paths, machine-readable artifacts and developer quickstarts.
- [Assure & Conform](docs/assure.md) — profiles, release gates and evidence.
- [Operate ARPA](docs/operate.md) — deployment, governance, security, privacy and lifecycle operations.
- [Integrate & Interoperate](docs/integrate.md) — A2A, TRQP and cross-runtime integration.
- [Govern & Contribute](docs/govern.md) — change control, releases and repository governance.

Use the [documentation catalogue](docs/index.md) for the complete rendered surface.

## Lab orientation

The lab framing is intentionally concrete. Research questions should become one or more of:

- testable requirements;
- negative vectors;
- implementation reports;
- architecture decision records;
- interoperability profiles;
- pilot-readiness evidence;
- governance, security or privacy notes.

The repository currently includes:

- [Agent governance reference architecture](docs/architecture/agent-governance-reference-architecture.md);
- [Lab experiments catalogue](docs/experiments/README.md);
- [Independent implementation guide](docs/independent-implementation-guide.md);
- [Lab interoperability programme](docs/interop/lab-interoperability-programme.md);
- [Lab contribution pathways](docs/lab-contribution-pathways.md);
- [ADR-001: Agent registry as governance control plane](docs/adr/ADR-001-agent-registry-as-governance-control-plane.md);
- [Registry federation research note](docs/research/registry-federation.md).

## What v0.9.5 delivers

- an independent TypeScript v0.3.0 implementation track over shared normative artifacts;
- Python↔TypeScript deterministic, historical and network interoperability checks;
- A2A publication/compatibility adapters with explicit discovery-is-not-authority semantics;
- deterministic historical authority resolution separating requested-time state from current state;
- explicit reconstruction quality, selected-record provenance, later material events, historical-effect and retention semantics;
- governance/privacy assurance vectors covering administrative capture, revocation convergence, federation conflict, restricted discovery and compromise restoration;
- a canonical sample registry, pilot kit and machine-readable readiness evidence;
- stable Candidate Specification requirements and conformance targets;
- hardened authority, delegation, recognition and fail-closed lifecycle semantics;
- machine-readable compatibility, requirement and evidence artifacts;
- an informative ARPA–TRQP governed query-projection profile;
- flagship documentation, CI, GitHub Pages, contribution controls and AI-use governance.

The repository-owned TypeScript track improves implementation diversity, but it is not external organizational independence evidence. See the [Independent implementation guide](docs/independent-implementation-guide.md) and [Lab interoperability programme](docs/interop/lab-interoperability-programme.md) for how external evidence should be collected.

## IETF Internet-Draft track

ARPA maintains a deliberately separate IETF authoring surface for the interoperable protocol core. The current published revision is **`draft-sankarshan-agent-registry-protocol-04`**, published on **29 September 2026** as an **Individual Submission**, with **56 pages**.

- [Published Internet-Draft](https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/)
- [IETF archive text for `-04`](https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-04.txt)
- [HTMLized `-04`](https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol)
- [IETF authoring and publication record]({{ '/ietf/' | relative_url }})
- [Protocol extraction map](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/ietf/PROTOCOL_EXTRACTION.md)

**Candidate v0.10.0 remains the current ARPA normative project baseline. IETF revision `-04` is the current published protocol-core extraction.** Published revisions `-00` through `-03` remain immutable historical predecessors, and any future IETF revision must begin as an explicit governed delta against published `-04`.

Build and validate the current IETF authoring/reproduction path with `make ietf-setup` followed by `make ietf-check`. Candidate authority and IETF publication authority remain deliberately distinct.

## Validate and produce evidence

```bash
make setup
make release-check-all
```

The full gate validates the Python release surface, TypeScript conformance and historical semantics, A2A adapters, same-corpus Python↔TypeScript equivalence, loopback HTTP network interoperability, Candidate hardening requirements, PP-01 cross-artifact precision and adversarial vector structure.

## ARPA and adjacent systems

ARPA owns the authority, lifecycle, evidence, revocation, enforcement and federation control-plane semantics for governed agent registries. It is designed to compose with adjacent systems without absorbing them:

| Adjacent layer | Relationship |
|---|---|
| DID / identifier infrastructure | Provides identifier and resolution substrate where appropriate |
| Verifiable credentials | Provides assertions that may inform authority, delegation or competence |
| Trust registries | Provide recognition and competence inputs; ARPA does not replace them |
| A2A-style agent ecosystems | Provide publication and discovery contexts that require authority boundaries |
| TRQP | Can expose selected registry state through a read-only governed projection |
| Assurance systems | Can consume ARPA evidence without treating ARPA as certification |

## Public specification and lab review

The ARPA Candidate Specification and the surrounding lab material are open for review. Readers, implementers, standards practitioners, security and privacy reviewers, governance practitioners and other interested parties can use the repository's issue forms to report ambiguities, implementation experience, authority concerns, interoperability gaps, lifecycle problems, security/privacy risks, conformance issues, missing cases or editorial improvements.

- [Open a specification feedback issue](https://github.com/qbf-consulting/agent-registry-protocol/issues/new?template=specification_feedback.yml)
- [Open an implementation report](https://github.com/qbf-consulting/agent-registry-protocol/issues/new?template=implementation_report.yml)
- See [CONTRIBUTING.md](CONTRIBUTING.md) for review and contribution expectations.

## Licensing

ARPA uses artifact-specific licensing so that specification content and executable implementation artifacts have licenses suited to their use:

- **Specification and human-readable content:** [CC BY 4.0](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/LICENSE-CONTENT)
- **Code and executable/machine-readable artifacts:** [Apache License 2.0](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/LICENSE-CODE)

Machine-readable schemas, OpenAPI/AsyncAPI contracts, validators, test vectors, fixtures, mappings, executable configuration and generated machine-readable evidence are treated as software artifacts under Apache-2.0 unless a file explicitly states otherwise. Normative and informative specification prose, documentation, diagrams, governance prose, narrative examples and release notes are content under CC-BY-4.0.

See the repository [licensing map](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/LICENSE), [NOTICE](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/NOTICE), and machine-readable [artifact license policy](licensing/artifact-license-policy.json) for the deterministic classification rules.

## Assurance boundary

The supplied implementations, adversarial fixtures and loopback network tests are repository-controlled candidate evidence, not external certification or proof of universal interoperability. The release does not claim legal authority, production key custody, formal cryptographic review, independent TRQP approval, or completed revocation without enforcement acknowledgement. See [known limitations](KNOWN_LIMITATIONS.md), [AI usage](AI_USAGE.md), [governance](GOVERNANCE.md), and [security](SECURITY.md).
