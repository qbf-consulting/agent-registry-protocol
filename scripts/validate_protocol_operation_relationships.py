#!/usr/bin/env python3
"""Validate informative, version-pinned external operation projections.

This validates relationship declarations, not runtime authority decisions or TRQP
endpoint conformance. Standard library only.
"""
import json
from pathlib import Path

DEFAULT = Path(__file__).resolve().parents[1] / "interop/protocol-operation-relationships.json"

class RelationshipError(ValueError):
    pass

def validate(data):
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        raise RelationshipError("unsupported relationship schema")
    if data.get("status") != "informative":
        raise RelationshipError("relationship declarations must remain informative")
    if data.get("normative_source") != "ARPA Candidate v0.10.0":
        raise RelationshipError("source baseline mismatch")
    if data.get("profile") != "arpa-trqp-query-projection-0.1":
        raise RelationshipError("projection profile mismatch")
    rows = data.get("relationships")
    if not isinstance(rows, list) or len(rows) != 2:
        raise RelationshipError("expected exactly two TRQP projection relationships")
    ids, external, operations = set(), set(), set()
    expected_sources = {"authorization": "authority-evaluation", "recognition": "recognition-resolution"}
    for row in rows:
        if not isinstance(row, dict):
            raise RelationshipError("relationship must be an object")
        ident = row.get("id")
        if not isinstance(ident, str) or not ident or ident in ids:
            raise RelationshipError("missing or duplicate relationship id")
        ids.add(ident)
        if row.get("relationship") != "projects-to":
            raise RelationshipError("projection must not be misclassified as carriage, consumption or profiling")
        src, target = row.get("source"), row.get("target")
        if not isinstance(src, dict) or not isinstance(target, dict):
            raise RelationshipError("missing source or target")
        operation = target.get("operation")
        if (src.get("protocol"), src.get("version"), src.get("operation")) != (
            "ARPA", "0.10.0", expected_sources.get(operation)):
            raise RelationshipError("source operation or version mismatch")
        if target.get("protocol") != "TRQP" or target.get("version") != "2.0":
            raise RelationshipError("target protocol or version mismatch")
        if operation not in expected_sources:
            raise RelationshipError("unsupported target operation")
        key = (target["protocol"], target["version"], operation)
        if key in external:
            raise RelationshipError("duplicate external operation mapping")
        external.add(key)
        operations.add(operation)
        authority = row.get("authority")
        if not isinstance(authority, dict) or authority.get("source_of_determination") != "ARPA" or authority.get("transfers_authority") is not False:
            raise RelationshipError("authority boundary must be explicit and non-transferring")
        semantics = row.get("semantics")
        if not isinstance(semantics, dict) or any(semantics.get(field) is not True for field in (
            "information_loss_disclosed", "unknown_does_not_authorize", "historical_result_is_not_current")):
            raise RelationshipError("required projection safeguards missing")
        conformance = row.get("conformance")
        if not isinstance(conformance, dict) or conformance.get("arpa_and_trqp_independent") is not True:
            raise RelationshipError("independent conformance must be declared")
    if operations != set(expected_sources):
        raise RelationshipError("authorization and recognition must each map once")
    return True

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    validate(json.loads(args.path.read_text(encoding="utf-8")))
    print("PASS informative TRQP operation relationships")

if __name__ == "__main__":
    main()
