"""Adversarial checks for informative ARPA/TRQP operation relationships."""
import copy
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_protocol_operation_relationships",
    ROOT / "scripts/validate_protocol_operation_relationships.py",
)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

@pytest.fixture
def declared():
    return json.loads((ROOT / "interop/protocol-operation-relationships.json").read_text())

def test_valid_relationships(declared):
    assert module.validate(declared) is True

@pytest.mark.parametrize("mutation", [
    lambda d: d["relationships"][0].update(relationship="carries"),
    lambda d: d["relationships"][0].update(relationship="consumes"),
    lambda d: d["relationships"][0]["target"].update(version="3.0"),
    lambda d: d["relationships"][0]["target"].update(operation="recognition"),
    lambda d: d["relationships"][0]["target"].update(operation="alias"),
    lambda d: d["relationships"][0]["source"].update(version="0.9.0"),
    lambda d: d["relationships"][0]["authority"].update(transfers_authority=True),
    lambda d: d["relationships"][0]["authority"].pop("source_of_determination"),
    lambda d: d["relationships"][0]["semantics"].update(unknown_does_not_authorize=False),
    lambda d: d["relationships"][0]["semantics"].update(information_loss_disclosed=False),
    lambda d: d["relationships"][0]["semantics"].update(historical_result_is_not_current=False),
    lambda d: d["relationships"][0]["conformance"].update(arpa_and_trqp_independent=False),
    lambda d: d["relationships"][1].update(id=d["relationships"][0]["id"]),
    lambda d: d.update(status="normative"),
    lambda d: d.update(schema_version="9.0"),
])
def test_invalid_relationship_rejected(declared, mutation):
    candidate = copy.deepcopy(declared)
    mutation(candidate)
    with pytest.raises(module.RelationshipError):
        module.validate(candidate)
