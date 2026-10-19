# Hail Heritage RAG | راوي حائل الذكي

## Modern Data Engineering for Advanced AI Systems

[SDAIA Academy](https://github.com/SDAIAAcademy)

## Project Description

**Hail Heritage RAG** is a full Retrieval-Augmented Generation (RAG) application developed as a capstone project for **Modern Data Engineering for Advanced AI Systems**.

The project demonstrates an integrated AI data architecture that combines document ingestion, data-quality validation, privacy-aware preprocessing, chunking, multilingual embeddings, vector search, grounded generation, source traceability, audit logging, and retrieval evaluation.

The proposed use case focuses on authorized knowledge about museums and visitor centers in the Hail Region. The application converts trusted documents into a searchable semantic knowledge base and answers questions from retrieved evidence instead of relying only on the language model's internal knowledge.

> **Submission scope:** the repository contains a runnable local proof of concept. Enterprise technologies mentioned in the roadmap are architectural extensions, not claims of deployed infrastructure.

## Problem Statement

Museum and visitor-center knowledge may be distributed across field surveys, reports, policies, visitor information, and institutional documents. This creates three practical problems:

1. manual search is slow;
2. source verification is difficult;
3. a standalone generative model may produce unsupported answers.

Hail Heritage RAG addresses these problems by making retrieval evidence part of the answer path.

## Objectives

- Build a complete document-to-answer RAG pipeline.
- Support Arabic-first semantic search using multilingual embeddings.
- Apply a data-quality gate before vector indexing.
- Redact common personal-data patterns before indexing.
- Return source names, chunk IDs, and similarity scores with answers.
- Abstain when retrieved evidence is too weak.
- Keep an audit trail for ingestion and query events.
- Demonstrate an event-driven architecture pattern.
- Provide a small evaluation harness for retrieval behavior.

## Course Alignment

| Course Component | Project Implementation |
|---|---|
| Modern Data Architecture | Decoupled ingestion, quality, knowledge, AI, and API layers |
| Real-Time / Event-Driven Pipelines | Async Producer/Broker/Consumer simulation in `app/stream_demo.py` |
| Vector Databases | ChromaDB with cosine similarity |
| Advanced RAG | Chunking, multilingual embeddings, top-k retrieval, thresholding, grounded prompt |
| Data Quality | Completeness, supported type, duplicate detection, quarantine |
| Governance | PII-pattern redaction, authorized-source rule, audit logging |
| Lineage / Traceability | Source, chunk ID, ingestion time, request ID, audit events |
| Evaluation | Retrieval test harness and grounded/abstention demo |
| Architecture Integration | All components exposed through one FastAPI application |

## Architecture

```text
Authorized Documents
        |
        v
Ingestion -> Quality Gate ----fail----> Quarantine
        |
        v
PII Redaction + Audit Metadata
        |
        v
Recursive Chunking
        |
        v
Multilingual Embeddings
        |
        v
ChromaDB Vector Store
        ^
        |
User -> FastAPI -> Query Embedding -> Top-k Retrieval
                                    |
                             Confidence Threshold
                              /             \
                        evidence          weak evidence
                           |                  |
                      Optional LLM          Abstain
                           |
                 Answer + Sources + Scores
                           |
                         Audit
```

See `ARCHITECTURE.md` for design rationale and the production roadmap.

## Repository Structure

```text
hail_heritage_rag_final/
├── app/
│   ├── main.py
│   ├── pipeline.py
│   ├── documents.py
│   ├── quality.py
│   ├── vector_store.py
│   ├── llm.py
│   ├── audit.py
│   ├── models.py
│   ├── config.py
│   ├── stream_demo.py
│   └── evaluate.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── quarantine/
├── storage/chroma/
├── logs/
├── tests/
├── ARCHITECTURE.md
├── PROJECT_PRESENTATION.md
├── SUBMISSION_CHECKLIST.md
├── requirements.txt
├── .env.example
└── README.md
```

## Full RAG Application

### Indexing Pipeline

`Load -> Validate -> Redact -> Chunk -> Embed -> Store`

1. **Load:** PDF, TXT, and Markdown documents.
2. **Validate:** reject empty/short, unsupported, or duplicate documents.
3. **Redact:** mask common email, Saudi mobile-number, and 10-digit ID patterns.
4. **Chunk:** recursively create bounded text chunks.
5. **Embed:** create multilingual semantic embeddings.
6. **Store:** persist vectors and metadata in ChromaDB.

### Query Pipeline

`Question -> Embed -> Similarity Search -> Threshold -> Context -> Generate -> Evidence`

1. embed the question with the same embedding model;
2. retrieve top-k semantically similar chunks;
3. convert cosine distance to a similarity score;
4. remove results below the configured threshold;
5. build a grounded context;
6. generate an optional LLM answer or return retrieved evidence;
7. return source metadata and audit the request.

## Quick Start

Python 3.11+ is recommended.

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Create the local environment file by copying `.env.example` to `.env`.

Run:

```bash
uvicorn app.main:app --reload
```

Open Swagger:

`http://127.0.0.1:8000/docs`

## Demo Workflow

### 1. Ingest authorized documents

Place `.pdf`, `.txt`, or `.md` files in `data/raw/`, then call:

```bash
curl -X POST http://127.0.0.1:8000/ingest
```

Accepted documents are redacted when a configured PII pattern is detected, chunked, embedded, and indexed. Failed documents are copied to `data/quarantine/`.

### 2. Ask a grounded question

```bash
curl -X POST http://127.0.0.1:8000/query   -H "Content-Type: application/json"   -d "{\"question\":\"كيف تتعامل المنصة مع البيانات الشخصية؟\"}"
```

The API response includes the answer, retrieved sources, chunk IDs, similarity scores, a `grounded` flag, and a request ID.

### 3. Optional LLM generation

The application can demonstrate retrieval without an LLM key. To enable generated answers, configure:

```env
OPENROUTER_API_KEY=your_key
OPENROUTER_MODEL=qwen/qwen3-coder:free
```

Never commit `.env`.

## Data Quality

The local quality gate checks:

- **Completeness:** document contains enough extractable text.
- **Validity:** supported file type.
- **Uniqueness:** duplicate content is rejected.
- **Privacy signal:** common PII patterns are detected and redacted.

Documents that fail the quality gate are quarantined before vector indexing.

## Governance and Traceability

- Ingest only authorized documents.
- Common email, Saudi mobile, and 10-digit ID patterns are masked before indexing.
- Secrets stay outside Git through `.env`.
- Every ingestion and query event is appended to `logs/audit.jsonl`.
- Indexed metadata records the source, chunk index, ingestion time, and PII-redaction flag.
- The query response exposes source and chunk evidence.

The regex-based PII detector is a teaching implementation, not an enterprise DLP system.

## Evaluation

Run:

```bash
python -m app.evaluate
pytest -q
```

Recommended production metrics:

- Context Relevance
- Groundedness
- Answer Relevance
- Retrieval hit rate
- Abstention accuracy
- Latency
- Quality-gate rejection rate

## Event-Driven Demonstration

```bash
python -m app.stream_demo
```

The local async demo models the pattern:

`Producer -> Broker -> Consumer -> Quality/Index Action`

A production architecture can replace this simulation with Kafka or Redpanda.

## Architectural Decisions

**Why ChromaDB?**  
It is lightweight and appropriate for a laptop-based capstone while still demonstrating vector persistence and similarity retrieval.

**Why multilingual Sentence Transformers?**  
The knowledge is Arabic-first, while technical metadata can be English.

**Why threshold retrieval?**  
Weak retrieval should lead to abstention rather than confident unsupported generation.

**Why FastAPI?**  
It exposes the pipeline as a testable service and provides Swagger documentation automatically.

**Why local-first?**  
The course asks for integrated architectural thinking. A reproducible local implementation is preferable to claiming enterprise services that were not actually deployed.

## Production Roadmap

`Local PoC -> Kafka/Redpanda -> Governed Lakehouse -> Distributed Vector DB -> Airflow/Prefect -> Kubernetes -> Centralized Observability + IAM`

Possible production substitutions include Great Expectations for stronger validation, a distributed vector database such as Qdrant or Milvus, and enterprise secrets/access-control services.

## Limitations

- PII detection is regex-based and can miss contextual personal information.
- PDF extraction depends on embedded text; scanned PDFs need an OCR stage not included here.
- The embedding model downloads on first use.
- ChromaDB is configured locally.
- The sample knowledge is project documentation, not an authoritative museum database.
- The event-driven component is a local simulation.
- Production deployment requires formal IAM, monitoring, backup, policy enforcement, and security review.

## Responsible Use

Only process documents you are authorized to use. Do not ingest confidential, personal, copyrighted, or restricted content without permission.

## Presentation

A ready presentation script is available in `PROJECT_PRESENTATION.md`.

## Submission Checklist

See `SUBMISSION_CHECKLIST.md` before uploading the repository.

## Author

Name: عبد الرحمن بن نوران الرشيدي  
Program: Modern Data Engineering for Advanced AI Systems  
Academy: SDAIA Academy  
Date: September 2026


## Submission Guide

For the trainer/reviewer:
- `PROJECT_DESCRIPTION.md` — concise project description.
- `COURSE_ALIGNMENT.md` — mapping to the five-day course and capstone requirements.
- `ARCHITECTURE.md` — architecture and design decisions.
- `PROJECT_PRESENTATION.md` — presentation notes.
- `SUBMISSION_CHECKLIST.md` — final review checklist.
- `FINAL_STATUS.md` — validation status and limitations.

The repository contains a local proof of concept. Production technologies in the roadmap are future extensions, not claims of deployed infrastructure.
