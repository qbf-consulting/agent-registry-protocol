---
layout: default
title: "Project Governance"
nav_exclude: true
---

# Project Governance

## Purpose

This document defines how the Agent Registry Protocol project develops from an initial community draft into an implementable and independently reviewable protocol proposal.

## Stewardship, authorship and repository authority

The Agent Registry Protocol is authored and maintained by **Sankarshan Mukhopadhyay** (`sankarshan@qbfconsulting.digital`) and is stewarded through **QBF Consulting LLP**. QBF Consulting LLP hosts and administers the canonical project repository and publication infrastructure.

Organizational stewardship does not erase or replace individual authorship or contribution history. Repository ownership identifies the current project home and governance surface; it does not retrospectively transfer authorship of historical contributions.

`PROJECT-STATUS.yaml` is the authoritative repository-local declaration for maturity, lifecycle, operational status, specification status, intended use, normative scope, explicit non-authority boundaries, validation commands, evidence outputs, and known limitations. Portfolio-level presentation does not override this repository-local status contract.

This repository may define and approve ARPA protocol semantics, record models, lifecycle processing, controlled registries, profiles, conformance targets, and repository-produced evidence. It does **not** acquire authority over TRQP, A2A, relying-party policy, legal recognition, accreditation, certification, or other upstream/sibling standards merely by mapping to or interoperating with them.

Maintainers may delegate review or change ownership within a documented issue, pull request, or governance record, but delegation is bounded by the delegated change scope and remains revocable by the repository governance process. Releases, status claims, protocol profiles, and controlled identifiers are deprecated, superseded, or withdrawn through recorded changes; historical versions and evidence are retained where needed for auditability and historical resolution.

## Decision model

The project currently uses a maintainer-led, review-driven model. Maintainers are responsible for preserving architectural coherence, transparent issue resolution, and clear separation between accepted behavior, experimental proposals, and open questions.

Consensus is preferred. Where consensus is not achievable, maintainers may record a provisional decision together with objections, trade-offs, and conditions for reconsideration.

## Change classes

### Editorial

Clarifications, formatting, examples, and corrections that do not alter protocol semantics.

### Compatible protocol change

New optional behavior or clarification that does not invalidate conforming implementations.

### Breaking protocol change

A change to required fields, processing behavior, lifecycle semantics, error behavior, or conformance expectations that may invalidate an implementation.

### Governance change

A change to project decision-making, licensing, contribution rules, or publication status.

Breaking and governance changes require an issue, explicit review period, and changelog entry.

## Specification maturity

Documents may be marked:

- **Exploratory Note**
- **Community Draft**
- **Implementation Draft**
- **Interoperability Draft**
- **Candidate Specification**
- **Stable Specification**
- **Deprecated**

The current specification is a **Community Draft**.

## Release policy

Repository releases should identify:

- specification version;
- maturity level;
- material changes;
- compatibility effects;
- implemented and planned surfaces;
- known limitations; and
- security-relevant changes.

## Appeals and corrections

Project decisions may be challenged through a governance issue. The issue should identify the contested decision, affected stakeholders, evidence, and requested remedy. Maintainers must record the disposition and rationale.

## Standards-body neutrality

This project may be proposed to, compared with, or aligned to standards-development work. Until formally adopted, it must remain clearly identified as an independent protocol project stewarded by QBF Consulting LLP, not as work adopted by an external standards organization.

## Controlled protocol registries

Changes to record types, relationship types, lifecycle states, event types, error/reason codes, proof purposes, extension namespaces or conformance profiles require a documented authority owner, interoperability analysis, security/privacy review, migration impact and conformance vectors. Identifiers are deprecated or superseded, never silently reassigned.

## Normative artifact coherence

A change to normative prose must evaluate schemas, controlled registries, OpenAPI/AsyncAPI, examples, vectors, reference behavior and migration guidance. Conflicts between prose and machine-readable artifacts are release-blocking unless explicitly recorded as a known limitation.
