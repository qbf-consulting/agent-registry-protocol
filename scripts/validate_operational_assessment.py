#!/usr/bin/env python3
"""Deterministic bounded-window operational-evidence assessment; informative ARPA profile."""
import argparse
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
OBS_SCHEMA = json.loads((ROOT / "schemas/operational-observation.schema.json").read_text())
SUMMARY_SCHEMA = json.loads((ROOT / "schemas/operational-evidence-summary.schema.json").read_text())
FIXTURES = ROOT / "conformance/test-vectors/operational-assessment/v0.1.0.json"
METHODS = {"transport_probe", "protocol_probe", "endpoint_control_proof", "other_declared_method"}

def when(value):
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError("timestamp requires timezone")
    return dt

def assess(input_data):
    window = input_data["window"]
    start, end = when(window["start"]), when(window["end"])
    if start >= end:
        raise ValueError("window start must precede end")
    method = input_data["method"]
    if method not in METHODS:
        raise ValueError("unsupported method")
    expected = input_data.get("declared_expected_count")
    if expected is not None and (isinstance(expected, bool) or not isinstance(expected, int) or expected < 0):
        raise ValueError("invalid declared expected count")
    subject = input_data["subject"]
    selected = {}
    duplicates = set()
    for obs in input_data["observations"]:
        errors = list(Draft202012Validator(OBS_SCHEMA, format_checker=FormatChecker()).iter_errors(obs))
        if errors:
            raise ValueError("invalid observation: " + errors[0].message)
        if obs["subject"]["agent_id"] != subject["agent_id"] or obs["subject"]["endpoint_id"] != subject["endpoint_id"]:
            raise ValueError("observation subject mismatch")
        if obs["method"] != method:
            raise ValueError("mixed observation methods")
        observed_at = when(obs["observed_at"])
        if not start <= observed_at < end:
            continue
        oid = obs["observation_id"]
        canonical = json.dumps(obs, sort_keys=True, separators=(",", ":"))
        if oid in selected:
            if selected[oid][0] != canonical:
                raise ValueError("observation identifier collision")
            duplicates.add(oid)
            continue
        selected[oid] = (canonical, obs)
    observations = [v[1] for _, v in sorted(selected.items())]
    counts = Counter(o["outcome"] for o in observations)
    # Conflict is a disagreement from different observers about the same subject, time and method.
    by_instant = {}
    for obs in observations:
        by_instant.setdefault(when(obs["observed_at"]).isoformat(), []).append(obs)
    conflicts = sorted({o["observation_id"] for group in by_instant.values() if len({o["outcome"] for o in group if o["outcome"] in ("success", "failure")}) > 1 for o in group})
    # Freshness is a separate evidence-quality dimension, never a claim of present availability.
    as_of_text = input_data.get("as_of")
    max_age = input_data.get("max_observation_age_seconds")
    if (as_of_text is None) != (max_age is None):
        raise ValueError("both as_of and maximum observation age are required")
    if max_age is not None and (isinstance(max_age, bool) or not isinstance(max_age, int) or max_age < 0):
        raise ValueError("invalid freshness threshold")
    as_of = when(as_of_text) if as_of_text is not None else None
    fresh_count = 0
    stale_ids = []
    future_ids = []
    for item in observations:
        t = when(item["observed_at"])
        if as_of is None:
            continue
        if t > as_of:
            future_ids.append(item["observation_id"])
        elif (as_of - t).total_seconds() > max_age:
            stale_ids.append(item["observation_id"])
        else:
            fresh_count += 1
    if future_ids:
        raise ValueError("observation occurs after assessment as_of")
    freshness = {"evaluated": as_of is not None, "fresh_count": fresh_count,
                 "stale_observation_ids": sorted(stale_ids)}
    # Count sufficiency is a declared sampling condition, NOT verified continuous coverage.
    complete = expected is not None and expected > 0 and len(observations) >= expected and not conflicts and not duplicates and counts["indeterminate"] == 0 and counts["not_performed"] == 0
    if stale_ids or (as_of is not None and not fresh_count):
        complete = False
    outcome = "conflicting_evidence" if conflicts else ("insufficient_evidence" if not observations or not complete else "observations_present")
    summary = {
        "profile_version":"0.1.0", "subject":subject, "window":window, "method":method,
        "observation_count":len(observations),
        "outcome_counts":{x:counts[x] for x in ("success","failure","indeterminate","not_performed")},
        "coverage":{"complete":complete,"declared_expected_count":expected, "basis":"declared_count_only"},
        "freshness":freshness,
        "conflicts":conflicts,
        "source_observation_ids":sorted(selected),
        "assessment_outcome":outcome,
        "authority_implication":False
    }
    errors = list(Draft202012Validator(SUMMARY_SCHEMA, format_checker=FormatChecker()).iter_errors(summary))
    if errors:
        raise ValueError("invalid derived summary: " + errors[0].message)
    return summary

def validate_fixtures():
    cases = json.loads(FIXTURES.read_text())["cases"]
    results = []
    for case in cases:
        try:
            actual = assess(case["input"])
            ok = actual["assessment_outcome"] == case["expected"]
            state = actual["assessment_outcome"]
            # Assertions on derived outputs, not just a coarse outcome label.
            for key, value in case.get("expect_fields", {}).items():
                cursor = actual
                for segment in key.split("."):
                    cursor = cursor[segment]
                ok = ok and cursor == value
        except ValueError as exc:
            state = "error"
            ok = case["expected"] == "error"
        results.append({"id":case["id"],"expected":case["expected"],"actual":state,"passed":ok})
    # Reordering source inputs must not change canonical summary content.
    full = next(c for c in cases if c["id"] == "LA-01-full")
    reordered = next(c for c in cases if c["id"] == "LA-02-reordered")
    equivalent = assess(full["input"]) == assess(reordered["input"])
    results.append({"id":"LA-DET-01-order-invariance","expected":"equivalent","actual":"equivalent" if equivalent else "different","passed":equivalent})
    return {"passed":bool(results) and all(x["passed"] for x in results),"cases":results,"limitations":["modeled-fixtures","no-independent-probe","no-current-state-or-authority-evaluation"]}

if __name__ == "__main__":
    cli=argparse.ArgumentParser()
    cli.add_argument("--output",type=Path)
    args=cli.parse_args()
    report=validate_fixtures()
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report["passed"] else 1)
