# Rust identifier-resolution experiment

This directory contains a bounded, informative Rust implementation used by
ARPA issue #85. It is not a replacement for the Python or TypeScript tracks
and is not a general Rust SDK.

## Scope

The implementation covers only the observable Profile A identifier-resolution
semantics exercised by:

- `conformance/test-vectors/TV-A-01-active-record.json`
- `conformance/test-vectors/TV-A-02-not-found.json`
- `conformance/test-vectors/TV-A-03-terminal-not-notfound.json`

It deliberately does not implement authority evaluation, registry mutation,
persistence, federation, historical resolution, or an HTTP server.

Discovery and successful resolution do not imply recognition, trust, or
authorization.

## Run

```bash
cargo test --manifest-path rust/Cargo.toml
python3 scripts/run_rust_conformance.py
python3 scripts/validate_typescript_interoperability.py
```

The harness produces `artifacts/rust/conformance-report.json`. Repository CI
uploads that report with the interoperability evidence bundle.

## Dependency and licensing boundary

The Rust crate uses only the Rust standard library. Source code and generated
machine-readable evidence are Apache-2.0 under the repository artifact license
policy.

This is repository-owned implementation diversity. It is not external
organizational independence or independent assurance.
