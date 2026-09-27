# =============================================================================
# SDA-AIE-214 · Building Retrieval-Augmented Generation Systems · SDAIA Academy
# Dalil (دليل) course asset repository
#
# Everything a participant needs to run is a make target, on purpose: on Day 4
# a stranger must be able to clone the repo and reach a working assistant with
# `make demo` in ten minutes. Commands nobody can remember are commands nobody
# reproduces, and an unreproducible benchmark is not evidence.
# =============================================================================
SHELL := /bin/bash
PY    := python3
export PYTHONPATH := src

CORPUS   ?= data/corpus/corpus_v1
CHUNKS   ?= data/index/chunks.jsonl
MODEL    ?=
BACKEND  ?= memory

.DEFAULT_GOAL := help

# ---------------------------------------------------------------- environment
.PHONY: help doctor install install-full
help:  ## show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
	  awk 'BEGIN{FS=":.*?## "}{printf "  \033[1m%-22s\033[0m %s\n",$$1,$$2}'

install:  ## minimal deps — everything except models and Qdrant
	pip install -e ".[dev]"

install-full:  ## everything, including embedding models and vector DB client
	pip install -e ".[full,dev]"

doctor:  ## check the environment BEFORE the lab, not during it
	@$(PY) scripts/doctor.py

# --------------------------------------------------------------------- corpus
.PHONY: corpus corpus-fetch corpus-verify eval-sets
corpus-fetch:  ## download Layer A (real SDAIA documents) — needs network
	$(PY) corpus/fetch_corpus.py

corpus-verify:  ## re-hash Layer A against LOCK.json
	$(PY) corpus/fetch_corpus.py --verify
	$(PY) corpus/validate_corpus.py

corpus:  ## generate Layer B (synthetic overlay) — deterministic, offline
	$(PY) corpus/build_layer_b.py

eval-sets:  ## derive probes, labels, golden set and red-team sets from the corpus
	$(PY) scripts/build_eval_sets.py

# -------------------------------------------------------------------- ingest
.PHONY: ingest ingest-naive ingest-v2
ingest-naive:  ## Lab 1: the deliberately bad baseline
	$(PY) -m dalil.ingest.pipeline --corpus $(CORPUS) --out data/index --naive --no-ocr

ingest:  ## Lab 2: format dispatch + Arabic OCR + structure-aware chunking
	$(PY) -m dalil.ingest.pipeline --corpus $(CORPUS) --out data/index \
	  --ocr-lang ara --ocr-psm 6 --ocr-binarise

ingest-v2:  ## Day 4: layer corpus_v2 on top and re-stamp lifecycle
	$(PY) -m dalil.ingest.pipeline --corpus data/corpus/corpus_v1 \
	  --overlay data/corpus/corpus_v2 --corpus-version v2 --out data/index \
	  --ocr-lang ara --ocr-psm 6 --ocr-binarise

# --------------------------------------------------------------------- index
.PHONY: qdrant index index-stats
qdrant:  ## start the vector database
	docker compose up -d qdrant

index:  ## Lab 3: embed and upsert into Qdrant (idempotent)
	$(PY) scripts/build_index.py --chunks $(CHUNKS) $(if $(MODEL),--model $(MODEL),)

index-stats:
	$(PY) -c "from dalil.index.collection import collection_stats; print(collection_stats())"

# ----------------------------------------------------------------- retrieval
.PHONY: eval-retrieval ablation ef-sweep
eval-retrieval:  ## Lab 3/4: recall@k, nDCG and the per-class table
	$(PY) scripts/run_retrieval_eval.py --mode reranked --backend $(BACKEND) \
	  $(if $(MODEL),--model $(MODEL),)

ablation:  ## Lab 4: sparse vs dense vs hybrid vs reranked, side by side
	@for m in sparse dense hybrid reranked; do \
	  echo "=== $$m ==="; \
	  $(PY) scripts/run_retrieval_eval.py --mode $$m --backend $(BACKEND) \
	    $(if $(MODEL),--model $(MODEL),) --out reports/retrieval_$$m.json \
	    --by-class-out reports/by_class_$$m.json | head -12; \
	done

ef-sweep:  ## Lab 3 step 4: recall vs latency as ef grows
	@for ef in 32 64 128 256; do \
	  echo "ef=$$ef"; DALIL_EF=$$ef $(PY) scripts/run_retrieval_eval.py \
	    --mode hybrid --backend $(BACKEND) --out reports/ef_$$ef.json | head -8; \
	done

# ----------------------------------------------------------------- generation
.PHONY: ask probe demo
ask:  ## ask one question:  make ask Q="ما مقدار بدل السكن للمرتبة 11؟"
	$(PY) scripts/ask.py --chunks $(CHUNKS) $(if $(MODEL),--model $(MODEL),) "$(Q)"

probe:  ## run a probe set:  make probe SET=failure_gallery
	$(PY) scripts/run_probes.py --set $(SET) --chunks $(CHUNKS)

demo:  ## the capstone demo path — clone to running
	$(PY) scripts/demo.py

# ----------------------------------------------------------------- evaluation
.PHONY: eval-golden eval-ragas gate baseline redteam staleness tau-sweep report
eval-golden:  ## Lab 6 step 1: run the 120-question golden set
	$(PY) scripts/run_golden_set.py --chunks $(CHUNKS) $(if $(MODEL),--model $(MODEL),)

eval-ragas:  ## Lab 6 step 2: RAGAS over the golden run
	$(PY) -m dalil.evaluation.ragas_harness --samples reports/golden_run.jsonl

gate:  ## Lab 6 step 3: fail the build on a regression
	$(PY) -m dalil.evaluation.gate --current reports/ragas_report.json

baseline:  ## record the current run as the baseline (do this in its OWN commit)
	$(PY) -m dalil.evaluation.gate --current reports/ragas_report.json --update-baseline

redteam:  ## Day 3: unanswerable-question red-team
	$(PY) scripts/run_redteam.py --suite unanswerable --chunks $(CHUNKS)

staleness:  ## Day 4: the F8 drill, filtering on vs off
	$(PY) scripts/run_redteam.py --suite staleness --chunks data/index/chunks_v2.jsonl

tau-sweep:  ## choose the refusal threshold with evidence, not vibes
	$(PY) scripts/run_redteam.py --suite tau-sweep --chunks $(CHUNKS)

report:  ## assemble EVALUATION.md from the report files
	$(PY) -m dalil.evaluation.report

# ----------------------------------------------------------------- benchmarks
.PHONY: bench-miracl bench-beir bench-techqa bench-all
bench-miracl:  ## Arabic retrieval reality check
	$(PY) -m dalil.benchmarks.miracl_ar --limit 200 $(if $(MODEL),--model $(MODEL),)

bench-beir:  ## metric-code validation against published baselines
	$(PY) -m dalil.benchmarks.beir --dataset scifact $(if $(MODEL),--model $(MODEL),)

bench-techqa:  ## refusal behaviour on a public enterprise-support set
	$(PY) -m dalil.benchmarks.techqa

bench-all: bench-miracl bench-beir bench-techqa

# ----------------------------------------------------------------------- dev
.PHONY: test lint clean all
test:  ## run the test suite
	$(PY) -m pytest tests -q

lint:
	$(PY) -m ruff check src scripts corpus tests || true

clean:
	rm -rf reports data/index

all: corpus eval-sets ingest eval-retrieval eval-golden eval-ragas gate  ## full offline pipeline
