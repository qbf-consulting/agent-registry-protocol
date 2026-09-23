---
layout: default
title: "Changelog"
nav_exclude: true
---

# Changelog

## Candidate v0.10.0 consolidation (unreleased)

- Consolidated ARPA Candidate v0.9.0, the v0.9.1 adversarial-hardening amendment, `ARPA-CAND-PP-01`, `ARPA-CAND-PP-02`, and `ARPA-CAND-PP-03` into one authoritative Candidate v0.10.0 specification.
- Added a machine-readable consolidation manifest and release-gated validator covering amendment-section mapping, normative carry-over, historical-source immutability, and protected IETF `-02` control files.
- Regenerated the normative-requirements catalogue against v0.10.0 while preserving the existing content-derived identifier policy.
- Reconciled project maturity/status, documentation, and IETF authoring guidance around the new Candidate baseline.
- Preserved published IETF `draft-sankarshan-agent-registry-protocol-02` as an independently versioned immutable baseline; future `-03` work remains an explicit `-02 → -03` delta process.


### Operational resilience assurance (unreleased)

- Added cross-cutting normative resilience requirements for retry ownership, aggregate retry budgets, partial-outage failover, stabilized recovery, event isolation, durable acknowledgement, dependency amplification, cache freshness, and sustained-load progress.
- Added a machine-readable Operational Resilience Declaration, modeled conformance vectors, validator, and evidence bundle addressing review-required gaps from `rahp-toolkit#19`.
- Kept infrastructure mechanisms deployment-neutral: ARPA constrains observable safety outcomes rather than mandating specific retry, cache, queue, service-mesh, or timer implementations.

## Unreleased

### IETF publication-path hardening
- Corrected the IETF landing-page navigation to use Jekyll `relative_url` semantics, preventing nested-page links from resolving under `/docs/ietf/`.
- Kept repository-only IETF authoring guidance linked to its GitHub source rather than to a non-rendered `README.html`.

### Fixed
- Added a canonical rendered `/ietf/` landing page and publication-manifest entry so GitHub Pages validation no longer emits unresolved `ietf/README.md` links.

### IETF Internet-Draft preparation
- Added a dedicated `ietf/` authoring surface for `draft-sankarshan-agent-registry-protocol-00` without replacing the ARPA Candidate Specification.
- Extracted the interoperable protocol core covering identifiers, relationships, bounded delegated authority, lifecycle/status, HTTP registration and resolution, historical resolution, events, errors, extensibility, security and privacy.
- Added an explicit ARPA-to-IETF protocol extraction map and `-00` submission checklist.
- Added Markdown-to-RFCXML v3, plaintext and HTML build tooling plus repository-local validation.
- Added a dedicated GitHub Actions workflow that publishes rendered I-D artifacts for review.
- Separated Internet-Draft revisioning and IETF contribution terms from ARPA project semantic versions and artifact licensing.
- Left prospective IANA registrations intentionally unresolved pending IETF community review rather than pre-allocating protocol namespaces.

### Candidate specification hardening
- Distinguished revocation publication, propagation and enforcement convergence; convergence now requires applicable enforcement acknowledgements.
- Added a normative lifecycle transition registry with explicit ordinary, containment, restoration, terminal and governance-reversal paths.
- Added machine-readable normative requirement traceability and validation evidence.
- Made fail-safe authority outcomes deterministic for stale, conflicting, unavailable or unverifiable material inputs.
- Required Profiles B-D to declare a consequential-action classification policy and Profiles C-D to declare acknowledgement-based revocation convergence.
- Corrected v0.9.0 Candidate-to-schema version mapping and added release-gated consistency checks.

## [0.9.5] - 2026-08-16

### Added
- Independent TypeScript v0.3.0 implementation track consuming shared schemas, registries and conformance vectors without importing Python behavioural code.
- Effective-time and historical-resolution reliance semantics across all 15 v0.9.4 historical vectors.
- Decision receipts, event continuity, thin Node.js HTTP service, reusable `ArpaClient` and in-memory development store.
- A2A publication projection and conservative Agent Card compatibility adapters.
- Machine-readable TypeScript deterministic, historical, A2A, cross-runtime and network-interoperability evidence.
- Task-oriented GitHub Pages journeys: Understand, Build, Assure, Operate, Integrate and Govern.

### Changed
- Expanded Python↔TypeScript assurance from 12 deterministic vectors to 27 deterministic + historical equivalence checks.
- Added 7/7 loopback HTTP interoperability checks, including TypeScript-client consumption of the Python registry.
- `make release-check-all` now gates network interoperability in addition to repository and TypeScript validation.
- Clarified artifact-specific licensing: human-readable specification/documentation is CC-BY-4.0; code and executable/machine-readable artifacts are Apache-2.0.
- Updated repository citation and implementation metadata to v0.9.5 while retaining the v0.9.0 Candidate Specification as the normative baseline.

### Assurance boundary
- Both runtime implementations remain repository-controlled; external independently operated implementation evidence is still required for v1.0.
- The TypeScript HTTP server uses in-memory persistence and is not a production registry deployment.

## [0.9.4] - 2026-08-11

### Added
- Machine-readable `PROJECT-STATUS.yaml` aligned with the portfolio member status contract.
- Historical Authority Resolution response schema, reconstruction-status registry, and historical-effect registry.
- Fifteen historical-resolution conformance vectors and release-gated evidence generation.
- Historical Authority Resolution implementation and governance guide.

### Changed
- Point-in-time semantics now explicitly separate requested-time state, current state, later material events, retention status, and evidence lineage.
- Revocation, compromise, supersession, and recognition withdrawal can declare prospective, retroactive, governance-defined, or indeterminate historical effect.
- Repository validation now checks the portfolio status contract and historical-resolution artifacts.
- ARPA–TRQP guidance now preserves requested-time versus evaluation-time semantics for projected historical queries.

### Assurance boundary
- Historical registry state is evidence for relying-party evaluation; it is not itself a legal or policy determination that a historical action must be accepted.

## [0.9.3] - 2026-08-10

### Added
- A2A publication projection schema separating Agent Card, publication metadata and authorization context.
- Structured caller-visible `GET /agents` discovery contract.
- Immutable snapshot/reference and exact source-URI invariants.
- Agent Card compatibility result schema and executable compatibility classifier.
- Twelve A2A registry assurance vectors and dedicated evidence artifacts.
- A2A Registry Integration Guide with federation-neutral implementation guidance.

### Changed
- A2A profile now formalizes list/search, resolve and snapshot semantics.
- Reference service and release metadata advance to implementation release v0.9.3.
- Registry discovery explicitly carries no authority implication.

### Assurance boundary
- Publication, discoverability and endpoint authentication do not establish authority or permission to invoke.


## [0.9.2] - 2026-07-30

### Added
- Versioned ARPA A2A v1.0 interoperability profile and implementation guide.
- Machine-readable A2A field, claim, precedence and safe-failure mapping.
- A2A task, context, interface, terminal-state and artifact-digest evidence fields for Execution Receipts.
- Controlled A2A interoperability error codes and six executable conformance vectors.

### Changed
- Agent Description References now classify A2A profile, disclosure context, representation version, protocol versions and validity.
- Agent Card ARPA extensions now declare profile, registry, extension version, event and conformance endpoints.
- Release validation now checks A2A interoperability and preserves ARPA authority precedence over card content.

### Documentation
- Added a Start Here decision page linking architecture, local validation, pilot, release, conformance and A2A journeys.
- Added explicit normative, profile-normative and informative document boundaries.
- Linked conformance declarations, implementation reports, schemas, vectors and validation evidence.
- Added machine-verifiable documentation reachability and catalogue assurance.
- Fixed GitHub Pages publication-manifest generation so explicit Jekyll permalinks resolve to their actual rendered output paths.

### Assurance boundary
- A2A discovery, authentication and task completion do not imply ARPA authority, capability verification, assurance or governance recognition.


## [0.9.1] - 2026-07-18

### Added
- Implementation Accelerator with a 15-minute executable quickstart.
- Canonical Acme pilot registry fixtures and API consumer collections.
- Automated pilot-readiness evidence generation.
- Pilot governance, security, operations and exit checklists.
- Deployment profiles, delegation tutorial and production-hardening guidance.

### Changed
- Reference implementation metadata now advertises implementation release 0.9.1.
- GitHub Pages navigation exposes an implementation-first journey.


## [Unreleased]

### Security and governance assurance
- Completed a full combined RAHP + security-hardening audit against RAHP Toolkit v1.0.0.
- Strengthened Profile C/D high-impact administrative authorization, Profile B-D due-process/redress requirements, discovery privacy, sensitive relationship disclosure and federation conflict handling.
- Added eight release-gated governance-assurance vectors covering administrative capture, revocation convergence, federation conflict/withdrawal, restricted discovery and compromise restoration.
- Added machine-readable and human-readable audit evidence under `artifacts/governance-assurance/` and `docs/assurance/`.


### Fixed
- Corrected GitHub Pages licensing links so extensionless repository license/control files are resolved through their canonical GitHub source URLs rather than being rewritten as non-existent Jekyll pages.

### Fixed
- Linked all published historical release notes, Implementation Accelerator assets, pilot-readiness checklists, and the federated-pilot topology from the documentation catalogue so every generated page is reachable from the assured navigation roots.
- Preserved strict documentation reachability validation rather than excluding published evidence and governance pages from the publication surface.

### Fixed

- Replaced the brittle GitHub Pages minimum HTML-count assertion with deterministic required-page, Mermaid, and unresolved-link checks.

### Changed

- Hardened GitHub Pages publication so Markdown documentation across the repository, including the Candidate Specification, profiles, conformance material, governance documents, and worked scenarios, is rendered as HTML.
- Added a complete documentation catalogue and updated the site landing page.
- Added deterministic Pages build assertions for required pages, Mermaid rendering, rendered-page coverage, and unresolved Markdown links.
- Updated GitHub-hosted JavaScript actions to Node 24-capable major versions where applicable.

## [0.9.0] - 2026-07-16

### Added

- Candidate Specification requirements and conformance targets.
- Machine-readable requirement traceability and compatibility matrix.
- Two separately structured ARPA–TRQP projection implementations.
- Network-boundary metadata discovery and durable event replay/deduplication/checkpoint evidence.
- Informative ARPA–TRQP architecture, machine-readable mapping, discovery declaration model and 13 projection vectors.
- Candidate validation report and evidence bundle.
- Migration guidance from v0.5.0.

### Changed

- Repository status advanced from interoperability draft to Candidate Specification.
- Release gate now includes candidate mapping, adapter equivalence, network and durable-event validation.

### Assurance boundary

The release does not claim external implementation independence, formal TRQP conformance, production deployment assurance, certification or legal recognition.


## [0.5.0] - 2026-07-15

### Added

- six composable protocol modules and explicit non-implication rules;
- normative ARPA-Core Identity and Discovery, Identifier/Alias, and Agent Card interoperability profiles;
- Capability Declaration, Capability Verification, Redress Record, Conformance Declaration, Agent Description Reference, Identifier Alias, Agent Card extension and Registry Metadata schemas;
- controlled registries for record, relationship, lifecycle, event, error, reason, proof-purpose, extension and profile identifiers;
- OpenAPI 3.1 REST contract and AsyncAPI event contract;
- runnable FastAPI/SQLite reference registry, resolver, event replay service and policy decision point;
- multidimensional implementation-report schema and generator;
- identifier, implementor, deployment, security, privacy, conformance, governance and migration guidance;
- twelve end-to-end governance scenarios;
- Makefile, Dockerfile, Compose configuration and expanded CI.

### Changed

- advanced the community draft to v0.5.0;
- clarified that Profile A is independently implementable and unsupported higher-module operations return a deterministic error;
- formalized self-declared Agent Card capabilities as distinct from verification, authorization and assurance;
- strengthened transfer, issuer-competence and alias conflict semantics;
- reframed conformance as protocol, semantic, cryptographic, operational, governance and enforcement evidence.

### Security

- documented alias hijacking, issuer confusion, projection poisoning, replay, event gaps, malicious extensions, transfer abuse and revocation-convergence risks;
- added negative validation and service tests for non-reassignment and alias conflict.

## [0.3.0] - 2026-07-15

- Initial machine-readable schemas, examples, profile matrices and executable conformance vectors.

### Candidate specification consolidation correction

- Consolidated the v0.9.0 Candidate requirements into the authoritative protocol specification.
- Removed the unchanged v0.5.0 draft and detached candidate overlay to eliminate competing specification surfaces.
- Updated all repository references, schemas, manifests, validation rules, and documentation to point to `spec/agent-registry-protocol-v0.9.0.md`.
