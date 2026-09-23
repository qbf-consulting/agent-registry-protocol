# Public repository baseline

This record captures the repository-owned controls reviewed under issue #15. It is repository assurance evidence, not external certification.

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| Purpose, maturity, authority and known limits | PASS | `README.md`, `GOVERNANCE.md`, `KNOWN_LIMITATIONS.md` | Pre-1.0 status remains intentionally experimental. |
| Licensing | PASS | `LICENSE` | None identified. |
| Security reporting | PASS | `SECURITY.md` | GitHub private-vulnerability-reporting enablement remains hosted setting evidence. |
| Contribution/community/support guidance | PASS | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, issue and PR templates | None identified. |
| Dependency update management | PASS | `.github/dependabot.yml` | Hosted Dependabot enablement remains platform evidence. |
| Repository hygiene | PASS | `.gitignore`; committed `.DS_Store` removed in baseline remediation | None identified. |
| CI / Pages / draft validation | PASS / bounded | `.github/workflows/validate.yml`, `pages.yml`, `ietf-draft.yml` | Workflow results remain execution evidence, not protocol assurance by themselves. |
| Default-branch protection | PARTIAL | active `protect-main` ruleset requires PRs, resolved conversations, linear history, and blocks deletion/non-fast-forward updates | Required CI/status check is not present in the observed ruleset; tracked separately. |
| Release/version provenance | PASS | `CHANGELOG.md`, `CITATION.cff`, `.github/workflows/release.yml`, versioned release requests, release notes/status surfaces | Publication is workflow-gated and remains a governed maintainer decision. |
| Authority boundary | PASS | `GOVERNANCE.md`, specification/docs | ARPA does not acquire authority owned by external semantic/assurance systems. |

## Completion boundary

Repository-file baseline gaps are closed by the associated remediation PR. The missing required-status-check rule is a GitHub-hosted setting and is tracked separately rather than being represented as PASS.
