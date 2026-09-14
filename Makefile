.PHONY: pilot-up pilot-down pilot-seed pilot-check pilot-reset setup validate test interop candidate run report typescript-check cross-runtime network-interop ietf-setup ietf-repo-check ietf-build ietf-lint ietf-check pages-manifest pages-build pages-stage-ietf pages-validate docs-links pages-check release-check release-check-all package clean
setup:
	python3 -m pip install -r scripts/requirements.txt
validate:
	python3 scripts/validate_examples.py
	python3 scripts/validate_test_vectors.py
	python3 scripts/validate_extended_vectors.py
	python3 scripts/validate_artifacts.py
	python3 scripts/validate_normative_requirements.py
	python3 scripts/validate_candidate_hardening.py
	python3 scripts/validate_kya_os_profile.py
	python3 scripts/validate_repository.py
	python3 scripts/validate_licensing.py
	python3 scripts/validate_candidate.py
	python3 scripts/validate_historical_resolution.py
	python3 scripts/validate_a2a_interoperability.py
	python3 scripts/validate_governance_assurance.py
	python3 scripts/validate_operational_resilience.py
	python3 scripts/validate_tga_alignment.py
	python3 scripts/validate_tsms_external_conformance.py
	python3 scripts/validate_ietf_draft.py
test:
	python3 -m pytest -q
interop:
	python3 scripts/run_interoperability.py
candidate:
	python3 scripts/run_candidate_program.py
run:
	python3 -m uvicorn reference.app:app --host 127.0.0.1 --port 8000
report:
	python3 scripts/generate_implementation_report.py

typescript-check:
	cd typescript && (if [ -x node_modules/.bin/tsc ] || command -v tsc >/dev/null 2>&1; then npm run release-check; else npm install --ignore-scripts --no-audit --no-fund && npm run release-check; fi)

cross-runtime:
	python3 scripts/validate_typescript_interoperability.py

network-interop:
	cd typescript && npm run build
	python3 scripts/run_typescript_network_interop.py

ietf-setup:
	gem install kramdown-rfc --no-document
	python3 -m pip install -r ietf/requirements.txt

ietf-repo-check:
	python3 scripts/validate_ietf_draft.py

ietf-build: ietf-repo-check
	scripts/build_ietf_draft.sh

ietf-lint: ietf-build
	@if command -v rfclint >/dev/null 2>&1; then rfclint ietf/generated/draft-sankarshan-agent-registry-protocol-00.xml; else echo "rfclint unavailable; xml2rfc build validation completed"; fi

ietf-check: ietf-lint
	@grep -q "draft-sankarshan-agent-registry-protocol-00" ietf/generated/draft-sankarshan-agent-registry-protocol-00.txt
	@grep -q "Security Considerations" ietf/generated/draft-sankarshan-agent-registry-protocol-00.txt
	@grep -q "IANA Considerations" ietf/generated/draft-sankarshan-agent-registry-protocol-00.txt

pages-manifest:
	python3 scripts/build_publication_manifest.py
pages-build: pages-manifest
	bundle exec jekyll build --trace --baseurl "/agent-registry-protocol"
pages-stage-ietf: pages-build ietf-check
	mkdir -p _site/ietf/generated
	cp ietf/generated/draft-sankarshan-agent-registry-protocol-00.xml _site/ietf/generated/
	cp ietf/generated/draft-sankarshan-agent-registry-protocol-00.txt _site/ietf/generated/
	cp ietf/generated/draft-sankarshan-agent-registry-protocol-00.html _site/ietf/generated/
	: > _site/ietf/generated/rfc-local.css
	sha256sum \
		_site/ietf/generated/draft-sankarshan-agent-registry-protocol-00.xml \
		_site/ietf/generated/draft-sankarshan-agent-registry-protocol-00.txt \
		_site/ietf/generated/draft-sankarshan-agent-registry-protocol-00.html \
		_site/ietf/generated/rfc-local.css \
		> _site/ietf/generated/SHA256SUMS.txt
pages-validate: pages-stage-ietf
	python3 scripts/validate_publication.py --baseurl "/agent-registry-protocol"
docs-links: pages-stage-ietf
	python3 scripts/validate_docs_links.py --baseurl "/agent-registry-protocol"
pages-check: pages-validate docs-links
release-check: validate test interop candidate report
release-check-all: release-check typescript-check cross-runtime network-interop
package: release-check-all
clean:
	rm -rf .pytest_cache __pycache__ reference/__pycache__ scripts/__pycache__ independent_impl/__pycache__ typescript/dist typescript/node_modules
	rm -f ietf/generated/*.xml ietf/generated/*.txt ietf/generated/*.html ietf/generated/*.pdf


pilot-up:
	docker compose up --build -d

pilot-down:
	docker compose down

pilot-reset:
	docker compose down -v

pilot-seed:
	python3 implementation-accelerator/scripts/seed_registry.py

pilot-check:
	python3 scripts/validate_pilot.py
