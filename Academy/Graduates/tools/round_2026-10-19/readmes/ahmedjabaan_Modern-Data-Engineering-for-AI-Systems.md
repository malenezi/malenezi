# Modern Data Engineering for AI Systems - Capstone Project

## 📌 Project Overview
This repository contains the full end-to-end Capstone implementation for the **Modern Data Engineering for AI Systems** training program delivered by **SDAIA Academy** (Instructor: Mohammed Albeladi).

The project integrates real-world data engineering and AI components into a unified, resilient data pipeline. The architecture covers resilient data ingestion, ACID-compliant storage with Delta Lake, hybrid search with Cross-Encoder reranking for RAG, quality gate checks, and OpenLineage telemetry tracking—all orchestrated via Apache Airflow.

---

## 🏗️ Pipeline Architecture & Deliverables

1. **Ingestion & Data Contract (Kafka + Pydantic)**
   - Streaming data ingestion verified using `confluent-kafka`.
   - Data contract enforcement using `Pydantic`.
   - Malformed records automatically routed to a Dead-Letter Queue (DLQ) with logged rejection reasons.

2. **Delta Lakehouse (Bronze, Silver, Gold Layers)**
   - Built on `PySpark` and `delta-spark`.
   - **Bronze Layer**: Stores raw validated ingestion payload.
   - **Silver Layer**: Schema enforcement demonstrated and real `MERGE` (upsert) operation performed on `transaction_id`.
   - **Gold Layer**: Genuine business aggregations computed (total revenue & transaction metrics).

3. **Production RAG Pipeline (Hybrid Search + RRF + Reranker)**
   - **Dense Search**: Dense vector index constructed using `SentenceTransformer` and `FAISS`.
   - **Sparse Search**: Lexical keyword search indexed via `BM25`.
   - **Rank Fusion**: Combined dense and sparse candidate sets using Reciprocal Rank Fusion (RRF).
   - **Reranking**: Final context reranked using a `Cross-Encoder` (`ms-marco-MiniLM-L-6-v2`) with grounded citations.

4. **Quality Gate & Data Lineage (Great Expectations + OpenLineage)**
   - Data quality rules evaluated on Gold layer metrics prior to downstream consumption.
   - Pipeline halts upon validation failures.
   - Emits real `OpenLineage` lifecycle events (`START`, `COMPLETE`, `FAIL`).

5. **Pipeline Orchestration (Apache Airflow)**
   - Apache Airflow DAG defining explicit task dependencies:
     `kafka_ingestion -> delta_lakehouse -> quality_gate -> rag_pipeline`

---

## 🚀 How to Run

### Google Colab / Executed Notebook
1. Open the provided `.ipynb` notebook in Google Colab.
2. Run Cells 1 through 5 sequentially.
3. Live outputs and execution logs capture explicit evidence for both success paths and failure paths (DLQ quarantine and quality check gating).

---

## 🛠️ Tech Stack & Real Libraries Used
- **Data Contract**: `pydantic`
- **Ingestion**: `confluent-kafka`
- **Lakehouse Engine**: `pyspark`, `delta-spark`
- **Vector Store & Search**: `faiss-cpu`, `rank_bm25`, `sentence-transformers`
- **Quality & Telemetry**: `great-expectations`, `openlineage-python`
- **Orchestration**: `apache-airflow`

---

## 🏫 Training Program Attribution
- **Program Name**: Modern Data Engineering for AI Systems Capstone Project
- **Delivered by**: SDAIA Academy
- **Platform**: Learning Space
- **Trainer**: Mohammed Albeladi

---

## 🔗 Reference
For more details about the academy programs, visit [SDAIA Academy on GitHub](https://github.com/SDAIAAcademy).
