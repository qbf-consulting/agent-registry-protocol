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
| Primary artifacts | Specification, schemas, API/event contracts, reference implementations, conformance and evidence |
| Release gate | `make release-check-all` |
| Candidate evidence | `artifacts/candidate-specification/evidence-bundle.json`, amendment-specific evidence, and `artifacts/conformance/candidate-consolidation-v0.10.0-validation.json` |
| Authority | Repository-local status and scope in `PROJECT-STATUS.yaml`; process in `GOVERNANCE.md` |

Implementation release numbers and Candidate-specification authority are intentionally distinct. An implementation release does not change the normative baseline merely because its semantic version advances.

## What the adversarial hardening adds

The existing Candidate adversarial-hardening amendment closes exploitable ambiguity without changing the core ARPA architecture. It adds:

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

The amendment is retained as historical provenance at [ARPA v0.9.1 Adversarial Hardening](spec/agent-registry-protocol-v0.9.1-hardening.md). Its approved normative semantics are now incorporated directly into [ARPA Candidate v0.10.0](spec/agent-registry-protocol-v0.10.0.md).

## Candidate Protocol Precision Amendment PP-01

[ARPA Candidate Protocol Precision Amendment PP-01](spec/agent-registry-protocol-protocol-precision-pp01.md) resolves four cross-artifact protocol ambiguities identified while preparing IETF revision `-01`:

- the ARPA Core Agent Identifier is the `agentreg:` identifier already required by the Candidate/OpenAPI contract;
- historical resolution is a reconstruction operation with explicit requested/evaluation time, provenance, later material events and reconstruction quality;
- protocol-significant HTTP failures use an RFC 9457 Problem Details contract with stable machine semantics; and
- unsupported material critical extensions fail safely rather than being silently ignored.

PP-01 retains its stable amendment ID and provenance. Its semantics, together with `ARPA-CAND-PP-02` and `ARPA-CAND-PP-03`, are incorporated into Candidate v0.10.0. Historical amendment requirements and vectors remain retained for auditability and regression assurance; `registries/candidate-consolidation-v0.10.0.json` records the consolidation map.

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

ARPA maintains a deliberately separate IETF authoring surface for the interoperable protocol core. The current published revision is **`draft-sankarshan-agent-registry-protocol-02`**, published on **23 September 2026**. Published IETF revisions are immutable and are not renumbered when the ARPA Candidate baseline advances.

- [Published Internet-Draft](https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/)
- [IETF archive text for `-02`](https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-02.txt)
- [IETF authoring and submission guide]({{ '/ietf/' | relative_url }})
- [Protocol extraction map](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/ietf/PROTOCOL_EXTRACTION.md)

**Candidate v0.10.0 is now the current ARPA project source baseline.** It does not rewrite published `-02`. Future `-03` work is governed as an explicit `-02 → -03` IETF delta, with Candidate v0.10.0 providing the project semantics from which protocol-core propositions may be selected. A Candidate change crosses the IETF boundary only through explicit disposition; project-only governance, conformance, deployment and assurance material does not enter the draft automatically.

Build and validate the current published-draft reproduction path with `make ietf-setup` followed by `make ietf-check`. Candidate consolidation is release-gated so that the governed `-02` control files remain unchanged.

## Start here

- [Authority at commitment projection](docs/authority-at-commitment.md) — action-specific authority, exact-action approval and fail-safe evidence boundaries

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

The full gate validates the Python release surface, TypeScript conformance and historical semantics, A2A adapters, same-corpus Python↔TypeScript equivalence, loopback HTTP network interoperability, Candidate hardening requirements, PP-01 cross-artifact precision, and adversarial vector structure.

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
