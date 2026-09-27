\
# Rafeeq — Tawseel agentic operations system. SDA-AIE-311 course repo.
#
# Every target below has been run and verified in a Layer-A-only sandbox
# (no langgraph/fastapi/pytest/qdrant-client installed — see
# docs/OFFLINE_MODE.md); targets that genuinely need a Layer-B package
# say so and fail with an actionable ImportError rather than a bare
# traceback (SPEC §1's import-guard rule).

SHELL := /bin/bash
export PYTHONPATH := src
export RAFEEQ_MODEL_MODE ?= stub
export RAFEEQ_VECTOR_MODE ?= simple
export RAFEEQ_EMBED_MODE ?= hashing

.PHONY: help doctor data test test-offline bench bench-security redteam eval dashboard \
        serve mcp-orders mcp-logistics mcp-billing mcp-customer \
        compose-up compose-down clean \
        lab1 lab2 lab3 lab4 lab5 lab6 lab7 lab8 lab9 \
        sim-no-terminate sim-prompt-authz sim-memory-leak sim-lost-handoff \
        sim-retry-write sim-react-thrash sim-stale-policy sim-swallowed-error

help:
	@echo "Rafeeq / Tawseel — common targets (see README.md for the full quickstart):"
	@echo "  make doctor           preflight: python, deps, data, model/vector mode, gateway, docker, per-lab offline verdict"
	@echo "  make data             regenerate data/*.json + data/tickets_eval.jsonl (deterministic, seeded)"
	@echo "  make test-offline     unit + security test suites, stdlib runner (no pytest needed)"
	@echo "  make test             same as test-offline, using pytest if it is installed"
	@echo "  make bench            TawseelBench + cross-module harness over the stub target"
	@echo "  make bench-security   TawseelBench's security family only (TB-037..TB-050), gates on 0"
	@echo "  make redteam          full red-team corpus; writes reports/SECURITY_REPORT.md"
	@echo "  make eval             evaluations.harness over data/tickets_eval.jsonl"
	@echo "  make dashboard        render reports/DASHBOARD.md"
	@echo "  make serve            run the Rafeeq service (fastapi if installed, else stdlib fallback) on :8000"
	@echo "  make mcp-orders       run the orders MCP server standalone (stdio transport; needs 'mcp')"
	@echo "  make mcp-logistics    run the logistics MCP server standalone"
	@echo "  make mcp-billing      run the billing MCP server standalone"
	@echo "  make mcp-customer     run the customer/CRM MCP server standalone"
	@echo "  make lab N=3          run Lab N's solution/verify.py (e.g. make lab N=3)"
	@echo "  make sim-<name>       run one labs/sim/sim_<name>.py script directly"
	@echo "  make compose-up       docker compose --profile labs up (offline/stub, no external services)"
	@echo "  make compose-down     docker compose down for both profiles"
	@echo "  make clean            remove __pycache__, reports/traces, generated reports"

doctor:
	python3 scripts/doctor.py

data:
	python3 data/generate.py
	python3 scripts/selfcheck.py

test-offline: data
	python3 tests/unit/run_without_pytest.py
	python3 tests/security/run_without_pytest.py

test: data
	@if command -v pytest >/dev/null 2>&1; then \
		pytest tests/unit tests/security -v; \
	else \
		echo "pytest not installed — falling back to the stdlib runners (same checks, see docs/OFFLINE_MODE.md)"; \
		$(MAKE) test-offline; \
	fi

bench: data
	python3 scripts/run_bench.py --target stub --suite both

bench-security: data
	python3 -m evaluations.security.runner --target stub

redteam: data
	python3 -m rafeeq.security.red_team

eval: data
	python3 -m evaluations.harness --target stub --out reports/eval_stub_ci.json

dashboard: data
	python3 evaluations/dashboard.py --target stub

serve:
	python3 -m rafeeq.service.api

mcp-orders:
	python3 mcp_servers/orders_server.py

mcp-logistics:
	python3 mcp_servers/logistics_server.py

mcp-billing:
	python3 mcp_servers/billing_server.py

mcp-customer:
	python3 mcp_servers/customer_server.py

# `make lab N=3` -> labs/lab03/solution/verify.py (zero-padded).
lab: data
	@test -n "$(N)" || (echo "usage: make lab N=<1-9>" && exit 1)
	python3 labs/lab0$(N)/solution/verify.py

lab1: data
	python3 labs/lab01/solution/verify.py
lab2: data
	python3 labs/lab02/solution/verify.py
lab3: data
	python3 labs/lab03/solution/verify.py
lab4: data
	python3 labs/lab04/solution/verify.py
lab5: data
	python3 labs/lab05/solution/verify.py
lab6: data
	python3 labs/lab06/solution/verify.py
lab7: data
	python3 labs/lab07/solution/verify.py
lab8: data
	python3 labs/lab08/solution/verify.py
lab9: data
	python3 labs/lab09/solution/verify.py

sim-no-terminate:
	python3 labs/sim/sim_no_terminate.py
sim-prompt-authz: data
	python3 labs/sim/sim_prompt_authz.py
sim-memory-leak:
	python3 labs/sim/sim_memory_leak.py
sim-lost-handoff:
	python3 labs/sim/sim_lost_handoff.py
sim-retry-write: data
	python3 labs/sim/sim_retry_write.py
sim-react-thrash:
	python3 labs/sim/sim_react_thrash.py
sim-stale-policy:
	python3 labs/sim/sim_stale_policy.py
sim-swallowed-error: data
	python3 labs/sim/sim_swallowed_error.py

compose-up:
	docker compose -f deployment/docker-compose.yml --profile labs up --build

compose-down:
	docker compose -f deployment/docker-compose.yml --profile labs down
	docker compose -f deployment/docker-compose.yml --profile full down

clean:
	find . -name "__pycache__" -not -path "./.git/*" -exec rm -rf {} + 2>/dev/null || true
	rm -rf reports/traces reports/audit
	rm -f reports/eval_stub_ci.json reports/eval_stub_ci.md reports/SECURITY_REPORT.md reports/DASHBOARD.md
