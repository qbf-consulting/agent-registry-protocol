#!/usr/bin/env python3
"""Validate optional operational observation schema and representative fixtures."""
import argparse
import json
from pathlib import Path
from datetime import datetime
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/operational-observation.schema.json"
VECTORS = ROOT / "conformance/test-vectors/operational-observation/v0.1.0.json"

def validate():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    vectors = json.loads(VECTORS.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    results = []
    seen = set()
    for case in vectors["cases"]:
        if case["id"] in seen:
            raise ValueError("Duplicate case identifier: " + case["id"])
        seen.add(case["id"])
        errors = list(validator.iter_errors(case["observation"]))
        timestamp_errors = []
        for field in ("observed_at", "issued_at"):
            value = case["observation"].get(field)
            if value is not None:
                try:
                    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
                    if dt.tzinfo is None or dt.utcoffset() is None:
                        raise ValueError("timezone required")
                except (ValueError, TypeError, AttributeError):
                    timestamp_errors.append(field + ": invalid offset-aware timestamp")
        actual = "fail" if errors or timestamp_errors else "pass"
        results.append({"id":case["id"],"expected":case["expected"],"actual":actual,"passed":actual==case["expected"],"errors":[e.message for e in errors] + timestamp_errors})
    return {"profile_version":vectors["profile_version"],"passed":bool(results) and all(r["passed"] for r in results),"cases":results,"limitations":["schema-fixture-evidence-only","no-live-probing","no-cryptographic-verification"]}

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    report=validate()
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":report["passed"],"case_count":len(report["cases"]),"failed_cases":[r for r in report["cases"] if not r["passed"]]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
