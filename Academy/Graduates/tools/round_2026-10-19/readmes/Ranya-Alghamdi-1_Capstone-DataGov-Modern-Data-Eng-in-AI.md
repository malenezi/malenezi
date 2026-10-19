# Smart Data Governance & Compliance Lakehouse + RAG Assistant

## Overview

An end-to-end data governance pipeline that mirrors how an organization registers,
validates, stores, and queries its data assets in line with Saudi NDMO governance
standards. Built as the capstone project for the SDAIA Academy "Modern Data
Engineering for AI Systems" training program.

The pipeline covers:
- **Ingestion**: Real-time event ingestion through Apache Kafka with a Pydantic v2
  schema validation gate and a quarantine zone for malformed records.
- **Lakehouse**: A layered Delta Lake architecture (Bronze / Silver / Gold) with a
  real MERGE upsert keyed on a business key, and genuine Gold-layer aggregates.
- **RAG Assistant**: A retrieval-augmented generation pipeline over synthetic NDMO
  policy documents, using hybrid search (dense + BM25), Reciprocal Rank Fusion,
  cross-encoder reranking, and grounded answer generation with cited sources.
- **Orchestration**: An Apache Airflow DAG wiring every stage together, where a
  failed quality gate halts downstream execution.
- **Quality Gate + Lineage**: Great Expectations checks that actively gate the
  pipeline, paired with real OpenLineage START/COMPLETE/FAIL event emission.

Every component uses its real library — no simulations or stand-ins:
`kafka-python-ng`, `pyspark` + `delta-spark`, `chromadb`, `great-expectations`,
`openlineage-python`, `apache-airflow`.

## Architecture

```
Kafka (KRaft) --> Schema Validation Gate --> Quarantine Zone
                        |
                        v
                Bronze (Delta, raw landing)
                        |
                        v
                Silver (Delta, deduplicated + MERGE upsert)
                        |
          +-------------+-------------+
          v                           v
   Gold (Delta aggregates)    Great Expectations Quality Gate
                                       |
                                       v
                          OpenLineage START/COMPLETE/FAIL events
                                       |
                                       v
                         Airflow DAG (orchestrates all stages)


Policy Documents --> Chunking --> ChromaDB (dense) + BM25 (sparse)
                                       |
                                       v
                         Reciprocal Rank Fusion --> Cross-Encoder Rerank
                                       |
                                       v
                    Grounded Answer Generation (Groq API) with citations
```

## Prerequisites

- Google Colab (or any Jupyter environment with a Linux shell)
- Python 3.13
- A free Groq API key ([console.groq.com](https://console.groq.com)) for the RAG
  answer generation step, added as a Colab Secret named `GROQ_API_KEY`

## How to Run

1. Open `Capstone_Project_DataGov_Compliance.ipynb` in Google Colab.
2. Add your Groq API key to Colab Secrets (key icon in the left sidebar) under the
   name `GROQ_API_KEY`, with Notebook access enabled.
3. Run all cells sequentially, top to bottom. Each step is self-contained and
   prints verification output before the next step begins.
4. Kafka, Spark, and Airflow all run locally inside the Colab runtime — no
   external infrastructure is required.

### Expected Output

- **Step 3**: `accepted=40 quarantined=10` — Kafka schema gate accepts/rejects
  records, with rejected records written to `data/quarantine/` as individual JSON
  files.
- **Steps 4-6**: `Bronze row count: 40`, `Silver row count: 42`, `Gold row count: 6`
  confirming the Bronze -> Silver MERGE and the Gold aggregation both ran.
- **Step 7**: A natural-language answer with `[Source N]` citations for each test
  query, grounded in the retrieved policy document chunks.
- **Step 8**: `Overall success: True` on clean data, `Overall success: False` with
  itemized failures on deliberately corrupted data.
- **Step 9**: `Dag run in success state` for the normal run, and `DagRun failed`
  for the forced-failure run, with `write_gold` never executing in the failed run.

## Project Structure

```
data/
  raw_events/          synthetic source events before Kafka
  quarantine/           rejected records with rejection reasons
  delta/bronze/          Bronze Delta table
  delta/silver/          Silver Delta table
  delta/gold/             Gold Delta table
  policy_docs/            NDMO-style policy documents for RAG
  chroma_store/           ChromaDB persistence
  lineage_events/         OpenLineage event log (JSON lines)
  great_expectations/     GE context and expectation suites
dags/                     Airflow DAG definitions
requirements.txt
README.md
```

## Training Program Attribution

Completed as the capstone project for **SDAIA Academy — Modern Data Engineering
for AI Systems** (September 6-10, 2026 cohort). Reference: [github.com/SDAIAAcademy](https://github.com/SDAIAAcademy)
