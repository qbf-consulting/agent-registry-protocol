/** Compare independent TS composition to the Python-created shared bounded evidence vectors. */
import fs from "node:fs";
import path from "node:path";
import { repositoryRoot } from "./repository.js";
import { evaluateModeledReliance, type EvidenceFinding } from "./operational-reliance.js";

type Case = { id: string; dimensions: EvidenceFinding; expected: { outcome: string; reasons: string[]; authority_implication: boolean } };
const source = path.join(repositoryRoot, "artifacts/operational-reliance/cross-runtime-input.json");
if (!fs.existsSync(source)) throw new Error("Python cross-runtime inputs missing; run scripts/validate_reliance_cross_runtime.py --prepare first");
const vectors = JSON.parse(fs.readFileSync(source, "utf8")) as { cases: Case[] };
const results = vectors.cases.map((test) => {
  const actual = evaluateModeledReliance(test.dimensions);
  const passed = actual.outcome === test.expected.outcome &&
    actual.authority_implication === test.expected.authority_implication &&
    JSON.stringify(actual.reasons) === JSON.stringify(test.expected.reasons);
  return { id: test.id, expected: test.expected, actual, passed };
});
const output = { contract: "informative-composite-reliance-v0.1.0", implementation: "typescript-independent-composition-only",
  passed: results.length > 0 && results.every(r=>r.passed), results,
  limitations: ["python-derived-observation-and-dependency-dimensions", "no-independent-source-verification", "no-runtime-authorization"] };
const destination = path.join(repositoryRoot, "artifacts/operational-reliance/typescript-cross-runtime-report.json");
fs.mkdirSync(path.dirname(destination), { recursive: true });
fs.writeFileSync(destination, JSON.stringify(output, null, 2)+"\n");
console.log("Operational reliance TS composition: "+results.filter(x=>x.passed).length+"/"+results.length);
if (!output.passed) process.exitCode=1;
