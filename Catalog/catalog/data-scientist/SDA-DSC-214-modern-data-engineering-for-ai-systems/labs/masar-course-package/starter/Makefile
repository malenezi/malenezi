# Masar Lakehouse — one command per thing you actually want to do.
#
#   make            list every target
#   make doctor     is this machine ready?
#   make pipeline   build the entire medallion, end to end
#
# The pipeline runs through orchestration/run_local.py by default, so it works
# with or without Airflow. Set USE_AIRFLOW=1 to route it through Airflow once
# you have installed it.

SHELL := /bin/bash
.DEFAULT_GOAL := help
.ONESHELL:

PY            ?= python
PIP           ?= $(PY) -m pip
DATE          ?= 2026-06-01
FROM          ?= 2026-06-01
TO            ?= 2026-06-05
DBT           ?= dbt
DBT_DIR       := dbt/masar
DBT_FLAGS     := --project-dir $(DBT_DIR) --profiles-dir $(DBT_DIR)
LAKEHOUSE     ?= ./lakehouse
USE_AIRFLOW   ?= 0
TS            := $(shell date +%Y%m%dT%H%M%S)

export PYTHONPATH := $(CURDIR)/src:$(PYTHONPATH)
export AIRFLOW_HOME := $(CURDIR)/orchestration/airflow
export AIRFLOW__CORE__DAGS_FOLDER := $(CURDIR)/orchestration/dags
export AIRFLOW__CORE__LOAD_EXAMPLES := False

.PHONY: help doctor install data land gate silver gold stream serve pipeline \
        pipeline-backfill test lint format clean clean-all dbt-deps dbt-run \
        dbt-test dbt-docs gx optimize vacuum up down snapshot preflight \
        lab8-baseline lab8-fixed pa1-setup pa2-setup pa3-setup

## ---------------------------------------------------------------- help ----

help:            ## List every target with its description
	@echo "Masar Lakehouse — SDA-DSC-214"
	@echo
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'
	@echo
	@echo "  Common overrides: DATE=2026-06-02  USE_AIRFLOW=1  FROM=... TO=..."

## ------------------------------------------------------------- setup ----

install:         ## Install the pinned stack and the package in editable mode
	$(PIP) install -r requirements.txt -r requirements-dev.txt
	$(PIP) install -e .

doctor:          ## Check Java, Python, Spark, Delta, dbt, GX, Kafka, Redis
	@$(PY) scripts/doctor.py

up:              ## Start Kafka + Redis (needed from Day 4)
	docker compose up -d
	@echo "waiting for healthchecks…"
	@docker compose ps

down:            ## Stop Kafka + Redis (add -v yourself to drop volumes)
	docker compose down

data:            ## Generate the synthetic Masar dataset from the pinned seed
	@if [ -x data/generators/generate_masar.py ] || [ -f data/generators/generate_masar.py ]; then \
	   $(PY) data/generators/generate_masar.py; \
	   $(PY) data/generators/inject_defects.py; \
	 else \
	   echo "data/generators not found — the raw feeds are already committed."; \
	   ls -1 data/raw 2>/dev/null | head || echo "  (and data/raw is missing: ask the instructor)"; \
	 fi

## ------------------------------------------------------- medallion ----

land:            ## Land every raw feed into bronze (append-only, with lineage)
	$(PY) -m masar.ingest.land_bronze --feed all --date $(DATE)

profile:         ## Profile bronze for swamp smells
	$(PY) -m masar.ingest.profile_bronze bronze/trips      --key trip_id
	$(PY) -m masar.ingest.profile_bronze bronze/gps_events --key event_id
	$(PY) -m masar.ingest.profile_bronze bronze/drivers    --key driver_id

gate:            ## Run the quality gate: fail-fast, quarantine, promote
	$(PY) -m masar.quality.gate --from-bronze --batch-id make_$(TS)

silver:          ## Build silver.trips and silver.drivers (Spark path)
	$(PY) -m masar.transform.build_silver --target all

gold:            ## Build the gold marts and the feature tables
	$(PY) -m masar.transform.build_gold --mart all
	$(PY) -m masar.transform.build_eta_features --fixed

stream:          ## Replay GPS into Kafka, then drain it into bronze and silver
	@echo "starting producer (50k pings) …"
	$(PY) -m masar.stream.gps_producer --limit 50000 --rate 2000
	@echo "draining Kafka -> bronze.gps_events …"
	$(PY) -m masar.stream.ingest_gps_stream --once
	@echo "conforming -> silver.vehicle_positions …"
	$(PY) -m masar.stream.build_vehicle_positions --once

serve:           ## Materialise online features, then prove offline == online
	$(PY) -m masar.serve.materialize_online
	$(PY) -m masar.serve.bi_view
	$(PY) -m masar.serve.consistency_check
	$(PY) -m masar.serve.pdpl_boundary_check

pipeline:        ## THE one command: land -> gate -> silver -> gold -> maintain
	@mkdir -p logs
ifeq ($(USE_AIRFLOW),1)
	airflow dags test masar_medallion $$(date +%Y-%m-%d) 2>&1 \
	  | tee logs/pipeline_$(TS).log
else
	$(PY) orchestration/run_local.py --run --ds $(DATE) 2>&1 \
	  | tee logs/pipeline_$(TS).log
endif

pipeline-backfill: ## Re-run the pipeline for a date range: FROM=... TO=...
	@for d in $$($(PY) -m masar.tools.daterange $(FROM) $(TO)); do \
	   echo "=== $$d ==="; \
	   $(PY) orchestration/run_local.py --run --ds $$d || exit 1; \
	 done

snapshot:        ## Snapshot row counts + checksums (Lab 7's recovery drill)
	$(PY) -m masar.tools.snapshot --out logs/snapshot_$(TS).json

preflight:       ## Check a lab's prerequisites: make preflight LAB=7
	$(PY) -m masar.tools.preflight --lab $(or $(LAB),7)

## ------------------------------------------------------------- dbt ----

dbt-deps:        ## Install dbt packages (dbt_utils)
	$(DBT) deps $(DBT_FLAGS)

dbt-run:         ## Run the dbt models (staging -> silver -> gold)
	$(DBT) run $(DBT_FLAGS)

dbt-test:        ## Run the dbt schema tests and singular tests
	$(DBT) test $(DBT_FLAGS)

dbt-docs:        ## Generate and serve the dbt lineage documentation
	$(DBT) docs generate $(DBT_FLAGS)
	$(DBT) docs serve $(DBT_FLAGS)

## --------------------------------------------------------- quality ----

gx:              ## Build the GX suites and validate silver.trips
	$(PY) -m masar.quality.bootstrap --init
	$(PY) quality/suites/silver_trips_suite.py
	$(PY) quality/suites/gps_events_suite.py
	$(PY) -m masar.quality.bootstrap --validate --suite silver_trips.contract --build-docs

observe:         ## Run the four data-SRE signals
	$(PY) -m masar.quality.observe --check all

## ----------------------------------------------------- maintenance ----

optimize:        ## OPTIMIZE + ZORDER every Delta table, reporting file counts
	$(PY) -m masar.delta.maintain

vacuum:          ## VACUUM DRY RUN: list what would be reclaimed, delete nothing
	@echo "Dry run only. Retention is a governance decision — see docs/GOVERNANCE_TEMPLATE.md."
	@echo "To actually reclaim storage, run: make optimize"
	$(PY) -m masar.delta.maintain --dry-run

## -------------------------------------------------- lab 8 drill ----

lab8-baseline:   ## Lab 8: build the LEAKING eta_features and train — expect R2 = 0.943
	$(PY) -m masar.transform.build_eta_features
	$(PY) -m masar.serve.train_eta --features gold.eta_features --split random

lab8-fixed:      ## Lab 8: build the POINT-IN-TIME eta_features and train — expect R2 = 0.712
	$(PY) -m masar.transform.build_eta_features --fixed
	$(PY) -m masar.serve.train_eta --features gold.eta_features --split time --test-days 2

## ------------------------------------------------ assessments (PA) ----
#
# These build DELIBERATELY BROKEN sandboxes under lakehouse/_assessments/.
# They never touch a participant's real bronze/silver/gold tables.
#
# NOTE: the instructor harnesses `make lab5-verify` .. `make lab8-verify`
# referenced by labs/solutions/LAB_0{5,6,7,8}_SOLUTION.md are NOT shipped in
# this release. Each solution guide's section 6 lists the individual checks;
# run those. See CONSISTENCY_REPORT.md.

pa1-setup:       ## PA-1: build the vacuumed, duplicated Delta sandbox
	$(PY) -m scripts.assessments.pa1_setup

pa2-setup:       ## PA-2: recreate the Kafka topic and load the 40k-ping sandbox
	bash scripts/assessments/pa2_setup.sh

pa3-setup:       ## PA-3: build the PA-3 variant of gold.eta_features (5 defects)
	$(PY) -m scripts.assessments.pa3_setup

## ------------------------------------------------------------ dev ----

test:            ## Run the unit tests (no Spark, no Docker, ~1 second)
	$(PY) -m pytest

lint:            ## Lint with ruff
	$(PY) -m ruff check src tests scripts solutions orchestration

format:          ## Format with black and fix what ruff can
	$(PY) -m black src tests scripts solutions orchestration
	$(PY) -m ruff check --fix src tests scripts solutions orchestration

clean:           ## Remove build artefacts, caches and logs (KEEPS the lakehouse)
	rm -rf .pytest_cache .ruff_cache **/__pycache__ src/**/__pycache__ \
	       $(DBT_DIR)/target $(DBT_DIR)/dbt_packages $(DBT_DIR)/logs \
	       logs/*.log quality/gx/uncommitted
	find . -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
	find . -name '*.pyc' -delete
	@echo "cleaned. The lakehouse under $(LAKEHOUSE) is untouched."

clean-all: clean ## Also DELETE the lakehouse. Destructive; asks first.
	@echo "This deletes $(LAKEHOUSE) — every Delta table, every _delta_log,"
	@echo "every version you could have time-travelled to. Re-landing is the"
	@echo "only way back, and it will not reproduce the same commit history."
	@read -p "Type 'yes' to continue: " ans; [ "$$ans" = "yes" ] || exit 1
	rm -rf $(LAKEHOUSE)
	mkdir -p $(LAKEHOUSE) && touch $(LAKEHOUSE)/.gitkeep
	@echo "lakehouse removed. Run: make land && make pipeline"
