# Capstone — Modern Data Engineering for AI Systems

A single, integrated data pipeline that takes an order event from a Kafka topic all the way to
a cited, retrieval-grounded answer — passing through a governed Delta Lakehouse, a
Great-Expectations quality gate, OpenLineage-tracked lineage, and Airflow orchestration along
the way.

## What this project does

E-commerce order events are the domain, but the point of the project is the **pipeline
architecture**, not the domain: it demonstrates, with real libraries end to end, how a modern
AI-system data platform is actually built.

1. **Ingestion** — a Kafka producer publishes order events; a Kafka consumer validates every
   event against a Pydantic v2 data contract (`OrderEventContract`) before it's allowed
   anywhere near storage. Anything that fails validation — a missing customer id, a negative
   quantity, a malformed country code — is routed to a quarantine dead-letter file with the
   rejection reason, never silently dropped.
2. **Delta Lakehouse** — valid events land in a Bronze table (raw, append-only), get merged
   into a Silver table with a real Delta `MERGE` keyed on `order_id` (so re-deliveries update
   rather than duplicate), and are aggregated into a Gold table of per-country revenue. Schema
   enforcement is proven by a deliberately incompatible write that Delta rejects.
3. **RAG pipeline** — a small knowledge base describing the pipeline's own architecture is
   chunked, indexed in ChromaDB (dense) and BM25 (sparse), fused with Reciprocal Rank Fusion,
   reranked with a cross-encoder, and answered with inline citations back to the source chunks.
4. **Orchestration** — an Airflow DAG (`ingest_orders >> quality_gate >> lakehouse_merge >>
   gold_aggregate >> rag_index`) wires every stage together. Because `quality_gate` is upstream
   of everything else, a failed quality check means Airflow's scheduler never runs the rest of
   that pipeline execution.
5. **Quality + Lineage** — a Great Expectations suite gates the Silver layer against six DAMA
   data-quality dimensions, and OpenLineage emits real START/COMPLETE/FAIL events for every
   stage, written as durable JSON lines.

## Why this design

Each deliverable is deliberately wired into the *next* one instead of standing alone: ingestion
feeds the lakehouse, the lakehouse's Gold layer is part of what RAG indexes, the quality gate
sits structurally upstream in the DAG (not just logically), and lineage wraps every stage
uniformly through one `track_stage()` context manager rather than being bolted on separately
per component. That's what "one working pipeline" means in the capstone rubric, as opposed to
five components that each run in isolation.

## Project structure

```
src/
  ingestion/        Pydantic data contract, Kafka producer, Kafka consumer + quarantine
  lakehouse/         Delta Bronze/Silver/Gold, real MERGE, schema-enforcement proof
  rag/               Chunking, ChromaDB, BM25, RRF fusion, cross-encoder rerank, citations
  quality/           Great Expectations suite that gates (raises + halts) on failure
  lineage/           OpenLineage START/COMPLETE/FAIL event emitter
  orchestration/     Airflow DAG wiring every stage together
notebooks/
  capstone_pipeline.ipynb   Single executable run of the whole pipeline (see below)
docs/
  ARCHITECTURE.md    Full design writeup and component-by-component rationale
run_logs/            Captured output from real runs of every stage (see "Evidence of runs")
data/                Generated at runtime (bronze/silver/gold/quarantine/chroma) — gitignored
```

## Prerequisites

- Python 3.11+
- Java 11+ (needed by PySpark/Delta Lake and by the local Kafka broker)
- A Kaggle account is **not** required for this capstone's own data (it uses synthetic order
  events); Day 4's lab notebook that inspired the quality-gate design does use the UCI Online
  Retail dataset via `kagglehub`, referenced in `docs/ARCHITECTURE.md` for context.

## Install & run

```bash
git clone https://github.com/Emad404/capstone-modern-data-engineering.git
cd capstone-modern-data-engineering
pip install -r requirements.txt
```

**Recommended: run `notebooks/capstone_pipeline.ipynb` in Google Colab.** It runs every stage
top to bottom, including the two stages that need outbound internet beyond package installs —
a local Kafka broker (downloaded from `downloads.apache.org`) and the RAG embedding/reranker
models (downloaded from `huggingface.co` on first use). Colab has both Java preinstalled and
unrestricted internet, so those cells work there without any extra setup.

**Run individual stages locally** (no Kafka broker or GPU needed for these):

```bash
python -m src.quality.expectations_gate    # Great Expectations gate — pass + halt-on-failure
python -m src.lineage.lineage_emitter      # OpenLineage START/COMPLETE/FAIL events
python -m src.rag.rag_pipeline             # Chunking + BM25 + RRF + citations (BM25-only)
python -m src.lakehouse.delta_pipeline     # Delta Bronze/Silver/Gold + MERGE (needs Java)
```

**Run the Airflow DAG against the real scheduler (optional — evidence already captured, see below):**

Airflow is deliberately *not* in `requirements.txt` — it pins its own dependencies very
strictly and bundling it with everything else can break the whole install if your Python
version doesn't match what Airflow supports that day. Install it in its own isolated
environment (a fresh virtualenv, or its own Colab runtime) if you want to rerun this stage:

```bash
python -m venv af_venv && source af_venv/bin/activate
pip install "apache-airflow==2.9.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.3/constraints-3.12.txt"
export AIRFLOW_HOME=$(pwd)/airflow_home
export AIRFLOW__CORE__DAGS_FOLDER=$(pwd)/src/orchestration
export AIRFLOW__CORE__LOAD_EXAMPLES=False
airflow db init
airflow dags test capstone_pipeline 2026-01-01
```

## Evidence of runs

`run_logs/` contains captured output from real executions of every stage, produced while
building this repository (not hand-written):

| File | What it proves |
|---|---|
| `ingestion_contract_test.log` | The Pydantic contract accepts 8/11 events and quarantines the 3 malformed ones with correct reasons |
| `quality_gate_run.log` | Great Expectations passes clean data (6/6) and **blocks** dirty data (duplicate PK + out-of-range quantity) |
| `lineage_events.jsonl` / `lineage_run.log` | Real OpenLineage START/COMPLETE/FAIL events, including a FAIL event on a deliberately raised exception |
| `rag_bm25_run.log` | Chunking, BM25 retrieval, RRF fusion, and cited-answer generation, end to end |
| `airflow_dag_test_run.log` | All 5 DAG tasks executed and marked SUCCESS by the real Airflow scheduler (`airflow dags test`) |
| `lakehouse_run.log` | Honest record of the one component (Delta/Spark) blocked by this build environment's network policy — see `docs/ARCHITECTURE.md`, "Known sandbox limitation" |

Running `notebooks/capstone_pipeline.ipynb` in Colab regenerates all of the above plus the
Kafka round-trip and the full dense+BM25 hybrid RAG output.

## Configuration / environment variables

| Variable | Used by | Purpose |
|---|---|---|
| `AIRFLOW_HOME` | Airflow | Where Airflow stores its metadata DB and logs |
| `AIRFLOW__CORE__DAGS_FOLDER` | Airflow | Points the scheduler at `src/orchestration/` |
| `KAFKA_BOOTSTRAP_SERVERS` (defaults to `localhost:9092` in code) | `src/ingestion/kafka_*.py` | Kafka broker address |

No API keys or secrets are required to run this project — nothing in it calls a paid external
API. `.gitignore` still excludes `.env` / `kaggle.json` / credential files as a matter of
standard practice.

## Submission checklist

Every rubric line item, mapped to exactly where it's satisfied in this repo, plus the physical
steps still required before submitting the GitHub link (pushing, and the one Colab run needed
to capture Kafka/Delta/full-RAG output) — see `docs/CHECKLIST.md`.

## Training program attribution

This project was completed as the capstone for **Modern Data Engineering for AI Systems**,
delivered by **SDAIA Academy** via Learning Space, trainer **Mohammed Albeladi** (5-day
program, June 2026 cohort).

SDAIA Academy on GitHub: https://github.com/SDAIAAcademy
