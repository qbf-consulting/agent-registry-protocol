from pathlib import Path
import re, sys, json
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
required=['README.md','LICENSE','LICENSE-CONTENT','LICENSE-CODE','licensing/artifact-license-policy.json','CHANGELOG.md','ROADMAP.md','GOVERNANCE.md','CONTRIBUTING.md','SECURITY.md','CODE_OF_CONDUCT.md','CITATION.cff','AI_USAGE.md','PROJECT-STATUS.yaml','schemas/project-status.schema.json','schemas/operational-resilience-declaration.schema.json','PORTFOLIO_STATUS.md','docs/index.md','docs/interoperability.md','docs/release-policy.md','spec/agent-registry-protocol-v0.9.0.md','spec/agent-registry-protocol-v0.10.0.md','docs/architecture/trqp-arpa-interoperability.md','docs/historical-authority-resolution.md','docs/operational-resilience.md','docs/candidate-specification-guide.md','docs/migration-v0.5.0-to-v0.9.0.md','RELEASE_NOTES_v0.9.0.md','RELEASE_NOTES_v0.9.2.md','RELEASE_NOTES_v0.9.4.md','RELEASE_NOTES_v0.9.5.md','RELEASE_NOTES_v0.10.0.md','docs/understand.md','docs/build.md','docs/assure.md','docs/operate.md','docs/integrate.md','docs/govern.md','spec/profiles/arpa-a2a-v1.0-interoperability-profile.md','mappings/a2a-v1.0-arpa-mapping.yaml','.github/workflows/validate.yml','.github/workflows/pages.yml','.github/ISSUE_TEMPLATE/bug_report.yml','.github/ISSUE_TEMPLATE/implementation_report.yml','.github/pull_request_template.md']
errors=[]
for rel in required:
    if not (ROOT/rel).exists(): errors.append(f'missing required flagship artifact: {rel}')
for path in list(ROOT.glob('*.md'))+list((ROOT/'docs').glob('*.md')):
    text=path.read_text()
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
        if target.startswith(('http://','https://','#','mailto:')): continue
        # Jekyll/Liquid URLs are resolved during publication rendering, not
        # against the repository filesystem. Publication validators verify
        # their rendered targets after Jekyll has applied baseurl semantics.
        if '{{' in target and '}}' in target: continue
        clean=target.split('#')[0]
        if clean and not (path.parent/clean).resolve().exists(): errors.append(f'{path.relative_to(ROOT)}: broken local link {target}')
# Federated portfolio member status contract: validate the controlled values and repository-owned authority/evidence fields.
try:
    import yaml
    status=yaml.safe_load((ROOT/'PROJECT-STATUS.yaml').read_text())
    status_schema=json.loads((ROOT/'schemas/project-status.schema.json').read_text())
    for err in Draft202012Validator(status_schema).iter_errors(status):
        errors.append('PROJECT-STATUS.yaml schema: '+err.message)
    expected={
        'maturity':'pilot-ready',
        'lifecycle':'active',
        'operational_status':'active-validation',
        'specification_status':'candidate-specification',
    }
    if status.get('schema_version') != '1.0': errors.append('PROJECT-STATUS.yaml: schema_version must be 1.0')
    project=status.get('project',{})
    for key,value in expected.items():
        if project.get(key)!=value: errors.append(f'PROJECT-STATUS.yaml: {key} must be {value}')
    if project.get('name')!='agent-registry-protocol': errors.append('PROJECT-STATUS.yaml: project.name mismatch')
    authority=status.get('authority',{})
    if not authority.get('normative_scope'): errors.append('PROJECT-STATUS.yaml: authority.normative_scope required')
    if not authority.get('does_not_own'): errors.append('PROJECT-STATUS.yaml: authority.does_not_own required')
    evidence=status.get('evidence',{})
    if 'make release-check' not in evidence.get('validation_commands',[]): errors.append('PROJECT-STATUS.yaml: make release-check must be declared')
    for rel in evidence.get('evidence_outputs',[]):
        if rel != 'artifacts/historical-resolution/evidence-bundle.json' and not (ROOT/rel).exists():
            errors.append(f'PROJECT-STATUS.yaml: declared evidence output missing: {rel}')
except Exception as exc:
    errors.append(f'PROJECT-STATUS.yaml: unreadable: {exc}')

if errors:
    print('\n'.join(errors)); sys.exit(1)
print('validate_repository.py: flagship baseline and local Markdown links OK')
