# Building Retrieval-Augmented Generation Systems
## بناء أنظمة التوليد المعزز بالاسترجاع

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Building Retrieval-Augmented Generation Systems |
| **Arabic Title** | بناء أنظمة التوليد المعزز بالاسترجاع |
| **Module Code** | SDA-AIE-214 |
| **Level** | Specialist |
| **Duration** | 4 days × 5 learning hours = **20 hours** |
| **Audience** | GenAI engineers building knowledge assistants and enterprise search |
| **Prerequisites** | SDA-AIE-213 |
| **Assessment** | Labs; enterprise RAG project with evaluation |
| **Stackability** | RAG badge · Prerequisite for Agentic AI Systems Engineering · Counts toward AI Engineer Specialist Certificate and GenAI Engineering micro-specialization · Next: SDA-AIE-311 |
| **Tools & Platforms** | Vector DBs (Qdrant/pgvector) · LangChain/LlamaIndex · RAGAS · rerankers |

## Course Description

A deep, practical module on grounding LLMs in enterprise knowledge. Participants build the full RAG pipeline — ingestion, chunking, embedding, vector retrieval, reranking, and generation — and evaluate answer faithfulness systematically. The module covers advanced patterns including hybrid search and multi-document reasoning for production-grade assistants.

The course is built around a single evolving artefact: **"Dalil" (دليل)**, an enterprise knowledge assistant for a fictional Saudi organisation, grounded in a deliberately messy 300-document corpus — HR policies as PDFs (some scanned Arabic), IT procedures as DOCX, intranet pages as HTML, allowance tables as XLSX, plus regulatory circulars that change over time. Every lab builds one stage of Dalil's pipeline: Day 1 ingests the corpus, Day 2 builds the retrieval stack, Day 3 makes answers grounded and measurable, Day 4 adds advanced patterns and assembles the capstone. By the final afternoon each participant owns a production-shaped RAG system with an evaluation harness that proves — with numbers — that its answers are faithful, relevant, and cited. This is the same system shape participants will extend with agents in SDA-AIE-311.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Design end-to-end RAG architectures for enterprise knowledge bases
2. **LO2** — Implement ingestion, chunking, and embedding pipelines for heterogeneous documents
3. **LO3** — Develop retrieval stacks combining vector, keyword, and hybrid search with reranking
4. **LO4** — Evaluate RAG quality using faithfulness, relevance, and answer-correctness metrics
5. **LO5** — Optimize retrieval parameters, context construction, and citation grounding
6. **LO6** — Validate systems against hallucination and stale-knowledge failure modes

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Ground the model in knowledge | M1: RAG Architecture & When to Use It vs Fine-Tuning · M2: Ingestion, Parsing & Chunking | 45% | 55% | Naive-RAG baseline with documented failure gallery + working ingestion pipeline over the Dalil corpus |
| **Day 2** | The retrieval stack | M3: Embeddings & Vector Databases · M4: Hybrid Retrieval & Reranking | 40% | 60% | Qdrant index with measured recall@k + hybrid-with-reranking retriever beating dense-only on the labelled query set |
| **Day 3** | From retrieval to trusted answers | M5: Context Construction & Citation Grounding · M6: RAG Evaluation Frameworks | 35% | 65% | Cited, refusal-capable answer pipeline + RAGAS evaluation harness with regression baseline |
| **Day 4** | Advanced patterns & production | M7: Advanced Patterns — Multi-Hop & Agentic RAG · Capstone | 25% | 75% | Multi-hop-capable Dalil + evaluated capstone system + demo with evaluation report |

## Hour-by-Hour Breakdown

### Day 1 — Ground the Model in Knowledge

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why LLMs fail on enterprise knowledge** + course kickoff | Name the three failure classes RAG addresses (knowledge cutoff, private knowledge, hallucination); tour the Dalil corpus and capstone | Interactive lecture + failure-story discussion | 80/20 |
| 2 | **RAG architecture & the fine-tuning decision** (M1) | Reference architecture components; RAG vs fine-tuning vs hybrid decision framework; cost/latency anatomy | Lecture + architecture walkthrough | 70/30 |
| 3 | **Lab 1 — Naive RAG baseline & failure gallery** | Stand up the 60-line baseline; classify its failures on 12 probe questions into a taxonomy | Guided lab (pairs) | 10/90 |
| 4 | **Ingestion, parsing & chunking strategies** (M2) | Parsing heterogeneous formats; OCR and Arabic text pitfalls; chunking strategies and trade-offs; metadata and document lifecycle | Lecture + parsing-disaster demo | 70/30 |
| 5 | **Lab 2 — Build the ingestion pipeline** | Parse the full corpus, apply structure-aware chunking, attach metadata, measure chunk-quality statistics | Guided lab (pairs) | 10/90 |

### Day 2 — The Retrieval Stack

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Embeddings and vector databases** (M3) | Embedding-model selection (multilingual!); similarity metrics; HNSW and quantization; Qdrant collections, payloads, filters; when pgvector | Lecture + index-internals demo | 70/30 |
| 2 | **Lab 3 — Embed, index, and measure recall** | Embed the chunk set with bge-m3, build the Qdrant collection, benchmark recall@k and latency on the labelled query set | Guided lab | 10/90 |
| 3 | **Hybrid retrieval and reranking** (M4) | Where dense retrieval fails (exact identifiers); BM25/sparse; RRF fusion; cross-encoder rerankers; two-stage retrieval budgets | Lecture + failure-case dissection | 70/30 |
| 4 | **Lab 4 — Hybrid search + reranker** | Add sparse vectors and RRF fusion in Qdrant; add bge-reranker; quantify the improvement per query class | Guided lab | 10/90 |
| 5 | **Retrieval clinic + PA-1** | Tune fetch-k/top-k/filters against the metrics; timed practical: diagnose three broken retrievers | Lab + timed practical assessment | 10/90 |

### Day 3 — From Retrieval to Trusted Answers

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Context construction and citation grounding** (M5) | Token budgets; ordering and lost-in-the-middle; context assembly; citation schemes; refusal behaviour; access-control filtering | Lecture + prompt surgery demo | 70/30 |
| 2 | **Lab 5 — Grounded, cited generation** | Build the context assembler and grounded prompt; emit verifiable citations; implement insufficient-evidence refusal | Guided lab | 10/90 |
| 3 | **RAG evaluation frameworks** (M6) | RAGAS metric suite (faithfulness, relevancy, context precision/recall, correctness); building golden sets; LLM-as-judge caveats; regression gating | Lecture + metric autopsy | 70/30 |
| 4 | **Lab 6 — Evaluation harness & baseline** | Run RAGAS over the 120-question golden set; store the baseline; wire a regression gate into the Makefile/CI | Guided lab | 10/90 |
| 5 | **Hallucination red-team + PA-2** | Attack Dalil with unanswerable, stale-doc, and conflict questions; measure refusal correctness; timed triage practical | Red-team exercise + assessment | 10/90 |

### Day 4 — Advanced Patterns and Production

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Advanced patterns: multi-hop and agentic RAG** (M7) | Query rewriting and decomposition; multi-hop retrieval; corrective/self-RAG loops; routing; when the complexity pays | Lecture + pattern gallery | 60/40 |
| 2 | **Lab 7 — Multi-hop and query intelligence** | Add multi-query rewriting and a two-hop decomposition path; measure gains on the multi-hop query subset | Guided lab | 10/90 |
| 3 | **Capstone assembly I** | Integrate all pipeline stages; freeze corpus v2 (with updated documents — stale-knowledge test); run full evaluation | Project work | 0/100 |
| 4 | **Capstone assembly II + evaluation report** | Tune against the rubric targets; produce `EVALUATION.md` with metric tables; peer review round | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 6-minute demos with live probe questions; rubric scoring; path to SDA-AIE-311 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module evolves the same **Dalil** assistant over the same corpus. Never introduce a throwaway toy corpus — failures found in Lab 1 are *fixed by name* in Labs 2–7, and the capstone is the accumulated system. Keep the Lab 1 failure gallery posted on the wall all four days; strike failures through as the stack eliminates them.
- **Pace control:** Labs 2 and 4 are the overrun-prone ones (parsing surprises; reranker downloads). Publish checkpoint tags (`lab1-start` … `lab7-start`, plus `-solution` tags) so stragglers can fast-forward: `git checkout lab3-start`.
- **Pairing:** rotate pairs daily. Pair a strong-Python participant with a strong-prompting participant; the retrieval stack needs both instincts.
- **Environment strategy:** primary = local Docker (Qdrant container + course LLM gateway); fallback = GitHub Codespaces devcontainer with a shared Qdrant instance per cohort. Models (bge-m3, bge-reranker-v2-m3) are pre-downloaded into the course bundle — classroom bandwidth must never gate a lab.
- **LLM access:** all generation goes through the course's OpenAI-compatible gateway (hosted model or local vLLM) with per-participant keys and spend caps. Pin the model and temperature=0 for every evaluation run — otherwise metric deltas are noise.
- **Language:** deliver in English or Arabic; keep code, identifiers, and commit messages in English. The corpus is deliberately bilingual — Arabic retrieval quality is a first-class topic (M2, M3), not an afterthought.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day 4 afternoon is deliberately theory-light.
- **Assessment logistics:** collect repository URLs at the end of Day 4 Hour 3 so evaluation harnesses can be verified before demos; rubric scoring happens live during Hour 5 demos, with the participant's own RAGAS report open beside the demo.

---

# Module 1 — RAG Architecture and When to Use It versus Fine-Tuning

## Module Overview

**Purpose.** Before building anything, participants must be able to say *why* RAG — and, just as importantly, when *not* RAG. This module establishes the reference architecture for retrieval-augmented generation, gives participants a defensible decision framework for RAG versus fine-tuning versus hybrid approaches, and stands up a deliberately naive baseline whose failures define the syllabus for the rest of the course.

**Business relevance.** Every Saudi enterprise adopting GenAI faces the same first question: "our knowledge is private, current, and access-controlled — how do we get it into the model?" Teams that answer "fine-tune" by reflex burn months and budget re-training on knowledge that changes weekly; teams that answer "RAG" by reflex ship assistants that can't match the required tone or structured output. The engineer who can argue the trade-off with cost, freshness, and auditability numbers is the one trusted with the programme. Under PDPL, the answer also determines *where personal data lives* — in retrievable documents with access control, or baked irreversibly into model weights.

**Industry use cases.**
- A bank's compliance assistant must answer from circulars updated monthly and cite them — RAG, because retraining cadence can never match regulatory cadence and citations require retrieval.
- A national airline fine-tunes a small model for structured output formatting of maintenance reports, but grounds the *content* via RAG over engineering manuals — the hybrid pattern.
- A government-services chatbot must refuse to answer outside its corpus and prove which document produced each answer for audit — retrieval is the only architecture that makes this provable.

**Expected competencies.** After this module a participant can draw the end-to-end RAG reference architecture, place any vendor product in it, run the RAG-vs-fine-tuning decision framework against a real scenario, estimate per-query cost and latency, and operate a minimal working pipeline.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Draw and explain the end-to-end RAG reference architecture (offline + online paths) | LO1 |
| 1.2 | Decide RAG vs fine-tuning vs hybrid for a given scenario using the decision framework | LO1 |
| 1.3 | Estimate per-query latency and cost across pipeline stages | LO1, LO5 |
| 1.4 | Operate a naive RAG baseline and classify its failures into a taxonomy | LO1, LO6 |
| 1.5 | Map each failure class to the pipeline stage (and course module) that fixes it | LO1, LO6 |

## Technical Content

### 1. Why parametric knowledge is not enough

An LLM's weights encode knowledge as of a training cutoff, with no access control, no citations, and no delete button. For enterprise use this creates three structural failures worth naming precisely:

- **Staleness:** the model cannot know last week's circular. No prompt fixes this.
- **Privacy/coverage:** internal policies were never in the training data — the model will *interpolate* an answer that sounds like a policy. This is the most dangerous failure mode because it is fluent.
- **Unverifiability:** even a correct parametric answer cannot say *which document* makes it correct — fatal for regulated workflows where the human must check the source.

RAG's core move: convert "what does the model know?" into "what can the system retrieve?" — shifting knowledge from weights (opaque, frozen, global) to a document index (inspectable, updatable, access-controllable). Generation becomes a *reading comprehension task over retrieved evidence* rather than a recall task.

**Instructor note:** open the hour by asking the un-augmented course LLM three questions about the fictional organisation's travel policy. It answers all three, fluently, wrongly. Screenshot the answers — they return as the villain in Module 6.

### 2. RAG versus fine-tuning: the decision framework

The single most-asked architecture question in enterprise GenAI. Teach it as a table, not a slogan:

| Dimension | RAG | Fine-tuning | Winner when… |
|---|---|---|---|
| Knowledge freshness | Update = re-index a document (minutes) | Update = retrain + re-eval + redeploy (days–weeks) | Knowledge changes faster than release cadence → RAG |
| Source attribution | Native — every answer carries its evidence | None — knowledge is diffused in weights | Citations/audit required → RAG |
| Access control | Filter retrieval per user/role at query time | Impossible — weights are global to all users | Different users may see different documents → RAG |
| Behaviour, tone, format | Prompt-limited | Excellent — the actual strength of fine-tuning | Stable *skill or style*, not facts → fine-tune |
| Domain vocabulary/jargon | Depends on embedding + LLM coverage | Can teach terminology deeply | Dense unfamiliar jargon in *inputs* → consider both |
| Latency | +1 retrieval stage (tens of ms, well-engineered) | No added stage | Ultra-low-latency, closed-domain → fine-tune small model |
| Cost shape | Per-query (retrieval + longer prompts) | Up-front (training) + cheaper queries | High QPS on static knowledge → fine-tune can win |
| Data deletion (PDPL) | Delete document from index — done | Machine unlearning is research, not practice | Right-to-erasure applies → RAG |
| Hallucination control | Grounding + refusal policies + evaluation | Fine-tuning does not stop confabulation | Correctness must be *measurable* → RAG |

The professional answer is usually **RAG first, fine-tune narrowly**: retrieval for knowledge, optionally a small fine-tune (or just few-shot prompting) for format and tone. Fine-tuning *for knowledge injection* is almost always the wrong tool: knowledge in weights is expensive to add, impossible to attribute, and impossible to delete. The framework should be run on the *decomposed* problem — "what must be current?" vs "what must be stylistically consistent?" — because the right answer per component differs.

### 3. The reference architecture

Two paths, one contract between them:

**Offline (indexing) path:** sources → loaders/parsers → cleaning → chunking → metadata enrichment → embedding → vector DB upsert (+ keyword index). Runs on document change events or schedules; its output contract is *the collection*: chunk text + vectors + payload metadata.

**Online (query) path:** user query → (query understanding: rewriting, decomposition — M7) → retrieval (dense + sparse hybrid — M4) → reranking (M4) → context construction (M5) → grounded generation with citations (M5) → (evaluation/telemetry — M6).

```
            OFFLINE                                ONLINE
 sources ─> parse ─> chunk ─> embed ─┐   query ─> rewrite ─> retrieve ─> rerank
 (PDF/DOCX/HTML/XLSX)                │              ▲            │
                                     ▼              │            ▼
                              [ Qdrant collection ]─┘     context builder
                              vectors + payload + sparse         │
                                                                 ▼
                                                     LLM (grounded prompt)
                                                                 │
                                                    answer + citations + telemetry
```

Design decisions participants must learn to *locate* in this diagram: Where does access control apply? (retrieval filter). Where does staleness get fixed? (offline path triggers). Where does hallucination get caught? (context contract + evaluation). Where does latency accumulate? (each online stage — measured in section 4). A vendor pitch is just this diagram with logos; the engineer's job is to know which boxes the product actually covers.

### 4. Cost and latency anatomy

Per-query latency budget for a well-engineered stack (course reference numbers, local models, warm caches):

| Stage | Typical latency | Typical cost driver |
|---|---|---|
| Query embedding | 5–20 ms | negligible |
| Vector search (HNSW, 100k chunks) | 5–30 ms | RAM for index |
| Sparse/keyword search | 5–20 ms | negligible |
| Reranking (cross-encoder, 40 candidates) | 50–300 ms | GPU/CPU compute |
| Generation (500-token answer) | 1–8 s | **dominates cost**: input tokens = context size |
| **Total** | **~1.5–9 s** | context tokens × price |

Two consequences: (1) generation dominates both latency and cost, so *context size discipline* (M5) is the main cost lever — stuffing 20 chunks into the prompt is paying 4× for worse answers; (2) retrieval stages are cheap, so being *generous before the reranker* (fetch 40–100) and *strict after it* (keep 4–8) buys quality nearly free. These two asymmetries drive most tuning decisions in the course.

### 5. The naive baseline — and its failure taxonomy

Lab 1 stands up the classic 60-line pipeline: fixed 500-character chunks, one dense embedding model, top-4 cosine retrieval, chunks pasted into a prompt. It works impressively on easy questions and fails on schedule everywhere else. The course's **failure taxonomy** (participants classify live failures into it):

| # | Failure class | Symptom | Fixed by |
|---|---|---|---|
| F1 | Parsing loss | Answer missing because the table/scan never made it to text | M2 |
| F2 | Fragmentation | Retrieved chunk starts mid-sentence; policy clause split across chunks | M2 |
| F3 | Semantic miss | Right document exists; wrong chunks retrieved (vocabulary gap, Arabic/English mismatch) | M3 |
| F4 | Exact-match miss | Query has an identifier ("Circular 44/2025", "form HR-07") that dense vectors blur | M4 |
| F5 | Precision collapse | Right chunk ranked 9th; junk fills the top-4 | M4 |
| F6 | Context abuse | Model ignores mid-context evidence or blends contradicting chunks | M5 |
| F7 | Ungrounded fluency | Confident answer with no supporting chunk retrieved at all | M5 + M6 |
| F8 | Staleness | Answer cites the superseded 2023 policy that is still in the index | M2 + M6 |

This taxonomy is the course's spine: every later module opens by naming which failure classes it retires.

### 6. Common mistakes & production considerations

1. Choosing fine-tuning for knowledge injection because "RAG is just a workaround" — then discovering update cost, no citations, no deletion.
2. Skipping the baseline: teams that never measured naive RAG cannot prove their sophisticated stack earns its complexity.
3. Treating RAG as a library import — the pipeline is a *system* with eight failure classes, each needing owned engineering.
4. Demo-driven development: validating on five friendly questions; production queries are adversarial, bilingual, and full of typos.
5. Ignoring access control until launch — retrofit is a redesign; the payload filter must exist from the first collection schema.
6. No latency/cost budget per stage — then discovering the reranker or a 16-chunk context blew the SLA.

Production: index freshness SLAs (how stale may an answer legally be?); multi-tenancy strategy (collection-per-department vs payload filters); fallback behaviour when retrieval returns nothing (refuse, never freestyle); logging the *retrieved chunk IDs per answer* — the audit trail regulators will ask for, and the debugging trail engineers will need at 03:00.

## Code Examples

### The naive baseline (Lab 1's starting point — deliberately minimal)

```python
# src/dalil/baseline.py
"""Naive RAG in ~60 lines. This is the course's punching bag:
every module improves one stage of it. Do NOT ship this."""
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams
from sentence_transformers import SentenceTransformer

EMB = SentenceTransformer("BAAI/bge-m3")          # multilingual dense encoder
llm = OpenAI(base_url="http://gateway:8080/v1")   # course LLM gateway
qdr = QdrantClient(url="http://localhost:6333")

COLLECTION = "dalil_naive"


def index(docs: list[dict]) -> None:
    """docs: [{'id': ..., 'text': ...}] — naive fixed-size chunking."""
    chunks = []
    for d in docs:
        text = d["text"]
        for i in range(0, len(text), 500):                 # F2 lives here
            chunks.append({"doc_id": d["id"], "text": text[i:i + 500]})
    qdr.recreate_collection(
        COLLECTION,
        vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
    )
    vecs = EMB.encode([c["text"] for c in chunks], normalize_embeddings=True)
    qdr.upsert(COLLECTION, [
        PointStruct(id=i, vector=v.tolist(), payload=c)
        for i, (v, c) in enumerate(zip(vecs, chunks))
    ])


def ask(query: str, k: int = 4) -> str:
    qv = EMB.encode(query, normalize_embeddings=True)
    hits = qdr.query_points(COLLECTION, query=qv.tolist(), limit=k).points
    context = "\n\n".join(h.payload["text"] for h in hits)  # F5, F6 live here
    resp = llm.chat.completions.create(
        model="course-llm", temperature=0,
        messages=[
            {"role": "system",
             "content": "Answer using the context below.\n\n" + context},
            {"role": "user", "content": query},
        ],
    )
    return resp.choices[0].message.content                  # F7: no citations,
                                                            # no refusal path
```

### The decision framework as a worksheet artefact

```python
# src/dalil/architecture/decision.py
"""RAG-vs-fine-tune scoring worksheet used in the Module 1 workshop.
Not ML — a structured argument. The output is a recommendation WITH reasons,
which is what an architecture review board actually wants."""
from dataclasses import dataclass, field


@dataclass
class Scenario:
    knowledge_change_cadence_days: int      # how often facts change
    citations_required: bool
    per_user_access_control: bool
    style_or_format_requirements: bool      # strict tone/schema outputs
    erasure_obligations: bool               # PDPL right-to-erasure applies
    reasons: list[str] = field(default_factory=list)

    def recommend(self) -> str:
        rag = tune = 0
        if self.knowledge_change_cadence_days < 90:
            rag += 2; self.reasons.append("knowledge changes faster than retrain cadence")
        if self.citations_required:
            rag += 3; self.reasons.append("attribution only possible via retrieval")
        if self.per_user_access_control:
            rag += 3; self.reasons.append("weights cannot enforce per-user access")
        if self.erasure_obligations:
            rag += 3; self.reasons.append("deletion from an index is possible; unlearning is not")
        if self.style_or_format_requirements:
            tune += 2; self.reasons.append("stable style/format is fine-tuning's strength")
        if rag and tune:
            return "HYBRID: RAG for knowledge + narrow fine-tune (or few-shot) for format"
        return "RAG-first" if rag >= tune else "Fine-tune candidate — challenge this in review"
```

### Project layout (the golden-thread repository, kept through the capstone)

```
dalil-rag/
├── pyproject.toml            # deps: langchain, llama-index-core, qdrant-client,
│                             #       sentence-transformers, ragas, fastapi
├── Makefile                  # make ingest / index / eval / api / demo
├── configs/
│   └── settings.example.env  # gateway URL, Qdrant URL, collection names
├── data/
│   ├── corpus_v1/            # 300 heterogeneous documents (course-provided)
│   └── corpus_v2/            # Day-4 update set (staleness drill)
├── eval/
│   ├── golden_qa_v1.jsonl    # 120 curated Q&A pairs (AR/EN)
│   └── retrieval_labels.jsonl# 200 queries -> relevant chunk doc-ids
├── src/dalil/
│   ├── ingest/               # M2: loaders, parsers, chunkers, metadata
│   ├── index/                # M3: embedder, collection schema, upsert
│   ├── retrieve/             # M4: dense, sparse, hybrid, rerank
│   ├── generate/             # M5: context builder, prompts, citations
│   ├── evaluation/           # M6: RAGAS harness, retrieval metrics, gates
│   ├── advanced/             # M7: rewriting, decomposition, routing
│   └── api/                  # thin FastAPI wrapper (SDA-AIE-113 practices)
└── tests/
```

## Hands-on Lab 1 — Naive RAG Baseline and Failure Gallery

| | |
|---|---|
| **Objective** | Run the naive pipeline over a 25-document corpus slice, then systematically break it: classify its behaviour on 12 probe questions into the failure taxonomy, producing the failure gallery the whole course will retire |
| **Duration** | 50 minutes |
| **Setup** | Python 3.12; `docker compose up qdrant`; course bundle models pre-downloaded; `git checkout lab1-start`; gateway key from instructor |

**Instructions & tasks**

1. *(10 min)* Run `make ingest-naive` over `corpus_v1/slice_25/`; confirm chunk count (~900) and inspect five random chunks — note every chunk that starts or ends mid-sentence.
2. *(10 min)* Ask the five "friendly" questions from `probes/easy.jsonl` — verify the baseline looks good. Record answers.
3. *(20 min)* Run the 12 adversarial probes (`probes/failure_gallery.jsonl`): exact circular IDs, Arabic queries against English documents, questions whose answer lives in a table, questions about superseded policy, and two questions the corpus cannot answer. For each: capture the answer, the retrieved chunk IDs, and assign a failure class F1–F8 with one sentence of evidence.
4. *(5 min)* Compare classifications with a neighbouring pair; resolve disagreements by inspecting retrieved chunks, not by debating the answer text.
5. *(5 min)* Commit `FAILURE_GALLERY.md` (the course's most-referenced artefact) with message `docs: baseline failure gallery`.

**Expected output**
```
$ make ingest-naive
Parsed 25 docs -> 912 chunks (naive 500-char) -> dalil_naive collection
$ make probe SET=failure_gallery
12 probes answered. Typical classification:
  F1 x2 (table + scanned PDF)   F3 x2 (AR->EN vocabulary gap)
  F4 x2 (circular ID, form code) F5 x1  F6 x1  F7 x2 (unanswerable -> confident)
  F8 x2 (superseded policy cited)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Qdrant connection refused | Container not up / port clash | `docker compose ps`; default port 6333; check `QDRANT_URL` |
| bge-m3 downloads mid-lab | Bundle cache not linked | `export HF_HOME=/course/models`; verify with `make doctor` |
| All probes answered "correctly" | Participant using solution branch or friendly probes | Confirm `lab1-start` and `failure_gallery.jsonl` |
| Gateway 429 | Spend cap / burst | Keys are rate-limited by design; add `--delay 2` to probe runner |
| Arabic text renders as boxes | Terminal font, not data | Inspect via the provided notebook, not the shell |

**Instructor notes.** Resist the urge to fix anything today — the pedagogy is *diagnosis before treatment*. The two F7 probes (unanswerable questions answered confidently) produce the strongest reactions; read one aloud. Fast finishers: vary `k` from 2 to 10 and watch F5 worsen as F3 improves — the precision/recall tension previews Module 4.

## Mini Exercises

**Quiz (5 questions)**
1. Which failure class can *no* amount of prompt engineering fix in a purely parametric LLM? → staleness (F8's root cause).
2. A client wants per-department answer visibility. RAG or fine-tune, and why? → RAG; weights cannot enforce per-user access.
3. Which pipeline stage dominates per-query cost? → generation — input tokens (context size).
4. Why is "fetch 50, keep 5" economically rational? → retrieval is cheap, context tokens are expensive; reranking bridges them.
5. True/False: fine-tuning reduces hallucination on private facts. → **False** — it adds fluent confabulation of facts it half-learned.

**Debugging exercise.** Given a transcript where Dalil answers a question about "remote work allowance" from the *travel* allowance policy, decide from the retrieved chunk IDs alone whether it is F3 (semantic miss) or F5 (precision collapse) — teaches reading retrieval logs before touching prompts.

**Code-review exercise.** Review `baseline.py` against a production checklist: name six things missing (citations, refusal, access filter, error handling, idempotent indexing, telemetry). Each maps to a later module — write which.

**Discussion questions.**
- Your CTO read that long-context models "make RAG obsolete" — 1M-token contexts can hold the whole corpus. Construct the rebuttal with numbers (cost per query, latency, access control, freshness, attribution) and the concession (small static corpora).
- Which of the eight failure classes would be *most damaging* in your organisation, and which probe question would you write for it?

## Case Study — RAG or Fine-Tune at a National Telecom

**Scenario.** A Saudi telecom's network-operations division wants an assistant over 6,000 pages of internal procedures: incident runbooks (updated weekly), vendor equipment manuals (static, jargon-dense), and HR/safety policies (quarterly, audit-sensitive). A vendor proposes fine-tuning a 70B model on everything for SAR 2.1M; an internal team proposes RAG; the CIO wants one recommendation.

**Business context.** Incident response time is the division's KPI; a wrong runbook step during an outage is a national-news event. Safety-policy answers must cite the exact clause for HSE audits. The vendor's retraining quote for updates is SAR 180k per cycle.

**Technical challenge.** Run the decision framework per document class, not per project — and design the architecture that follows from it.

**Constraints.** Runbooks change weekly (freshness); equipment manuals use vendor jargon the base model handles poorly (vocabulary); audit requires clause-level citations (attribution); field engineers and contractors must see different subsets (access control); data residency requires on-prem inference.

**Solution approach (facilitate, don't lecture).** Decomposition: runbooks + policies → RAG (freshness, citations, filtering are hard requirements — fine-tuning fails all three). Equipment jargon → measured first: benchmark the embedding model and base LLM on vendor-manual questions; if the vocabulary gap is real, the *cheap* fixes come first (domain synonym expansion at query time, better chunk context), with a narrow domain-adaptive fine-tune as a last resort *for the embedder*, not the generator. The SAR 2.1M proposal fails on update cost alone: 52 runbook updates/year × retrain cycles is architecturally absurd versus re-indexing in minutes.

**Discussion questions.**
1. Which single requirement kills the pure fine-tuning proposal fastest? (weekly freshness — or per-role access; both are absolute)
2. The vendor counters: "we'll fine-tune monthly and RAG the deltas." What operational complexity does this hybrid actually create, and when is it ever right?
3. Design the two-line test that proves whether the jargon problem is in the *embedder* or the *generator*.
4. What does the on-prem constraint change about model selection across the pipeline?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Baseline stands up end-to-end | Functionality | index + 17 probes complete without error | `make probe` |
| Failure gallery completeness | Diagnosis | 12/12 probes classified with evidence | gallery review |
| Classification accuracy | Diagnosis | ≥ 9/12 match reference classification | vs instructor key |
| Per-query latency (baseline) | Performance | recorded p50/p95 (typ. ~2.5 s / ~6 s) | probe runner timings |
| Per-query cost (baseline) | Cost | computed from token counts | gateway usage log |
| Decision-framework worksheet | Design | scenario scored with ≥ 4 cited reasons | workshop artefact |

**Example benchmark table (filled during lab):**

| Probe set | Answered | Correct | Cited | Refused when unanswerable |
|---|---|---|---|---|
| easy (5) | 5 | 5 | 0 | n/a |
| failure_gallery (12) | 12 | 3 | 0 | 0/2 |

## Required Visuals and Training Assets

### Diagrams
1. **RAG reference architecture (course anchor)** — *Purpose:* the map every later module colours in. *Elements:* offline path (sources → parse → chunk → embed → collection) and online path (query → rewrite → retrieve → rerank → context → LLM → cited answer), with module numbers M2–M7 stamped on their stages and failure classes F1–F8 pinned where they occur. *Style:* two horizontal lanes meeting at the collection; course palette; English labels with Arabic subtitles. *Designer note:* this diagram reprints as an A2 wall poster — the failure pins are physical stickers removed as modules complete.
2. **RAG vs fine-tune decision matrix** — *Elements:* the nine-dimension table rendered as a visual scorecard with icons (clock=freshness, quote=citation, lock=access, eraser=deletion). *Style:* printable A4 worksheet version + slide version.
3. **Latency/cost waterfall** — *Elements:* stacked horizontal bars per stage (embed, search, rerank, generate) with ms and halalas-per-query annotations; a second bar showing the 16-chunk-context anti-pattern doubling the generation bar. *Style:* waterfall chart.
4. **Failure taxonomy card** — *Elements:* F1–F8 with symptom one-liners and "fixed in Mx" pointers. *Style:* trading-card grid, printable; participants keep it on their desks all week.

### Images (screenshots)
1. **The un-augmented LLM confidently wrong** — *why:* the course's opening villain; *content:* gateway chat answering a fictional travel-policy question with invented clause numbers.
2. **Qdrant dashboard with `dalil_naive` collection** — *why:* participants verify their state; *content:* 912 points, vector size 1024, cosine.
3. **Probe runner terminal output** — *why:* expected-output reference; *content:* 12 probes with retrieved-chunk IDs and latency per query.
4. **A mid-sentence chunk in the inspector notebook** — *why:* makes F2 visceral; *content:* chunk starting "…of the allowance shall not" with no antecedent.

### Simulations
1. **Long-context temptation** — *Setup:* provided script stuffs all 25 documents into a single 180k-token prompt and asks the same probes. *Expected:* comparable accuracy on easy probes, 40–60× the token cost, 30 s+ latency, and still no citations or access control. *Learning objective:* "just use long context" priced honestly.
2. **Fine-tune mirage** — *Setup:* a provided LoRA fine-tuned on 25 policy documents (trained by course team). *Expected:* fluent policy-flavoured answers with wrong specifics; no way to trace or fix a single wrong fact. *Learning objective:* knowledge-injection fine-tuning fails exactly as the framework predicts.

### Interactive Activities
- **Architecture placement game (15 min):** vendor-product cards (managed vector DB, embedding API, "RAG-in-a-box", eval SaaS, reranker API) physically placed onto the reference architecture poster; class challenges each placement.
- **Decision-framework workshop (15 min):** four scenario cards (hospital protocols, tender-writing assistant, call-centre scripts, legal precedent search); groups score with the worksheet and defend in 90 seconds.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `corpus_v1/slice_25/` | Course-synthesised fictional org documents (AR/EN) | PDF/DOCX/HTML | 25 docs | Lab 1 baseline |
| `probes/easy.jsonl` + `probes/failure_gallery.jsonl` | Course-authored | JSONL | 5 + 12 | Failure gallery |
| LoRA adapter `policy-mirage` | Course team | safetensors | ~160 MB | Fine-tune mirage sim |

### Demo Requirements
- **Instructor demo:** the villain screenshot live (un-augmented LLM inventing policy), then the baseline answering the same question correctly — then *immediately* failing an F4 probe. The whiplash is the lesson.
- **Student demo:** two pairs present one failure each with retrieved-chunk evidence at end of Hour 3.
- **Expected outputs:** every pair has a committed `FAILURE_GALLERY.md`; the wall poster has 8 failure pins placed.

---

# Module 2 — Document Ingestion, Parsing, and Chunking Strategies

## Module Overview

**Purpose.** Retrieval can only surface text that made it into the index correctly. This module owns the offline path's front half — turning a heterogeneous, messy document corpus into clean, well-bounded, richly-tagged chunks. It retires the two failure classes that no amount of clever retrieval can fix after the fact: **F1 (parsing loss)** and **F2 (fragmentation)**, and lays the metadata foundation that later kills **F8 (staleness)**. The slogan for the module: *garbage in the index is garbage in every answer, forever.*

**Business relevance.** Every Saudi enterprise knowledge base is a graveyard of formats: HR policies exported to PDF (some scanned from paper, in Arabic), IT runbooks in DOCX, intranet pages in HTML, allowance and grade tables in XLSX, and regulatory circulars that supersede one another quarterly. Teams that treat ingestion as `text = pdf.extract_text()` ship assistants that silently cannot answer any question whose evidence lived in a table, a scan, or a two-column layout — and they do not find out until a user does. The engineer who can quantify *what fraction of the corpus survived parsing* is the one who can promise coverage instead of hoping for it.

**Industry use cases.**
- A bank's policy assistant must answer from allowance tables locked inside scanned PDFs — OCR quality *is* answer coverage; a 6% character-error rate on Arabic numerals becomes wrong SAR amounts in answers.
- A ministry's circular archive supersedes documents monthly; without `effective_date`/`superseded_by` metadata, the index cheerfully serves 2023 rules beside 2025 rules with no way to prefer the current one.
- An engineering-manual assistant fragments a safety procedure across three chunks; the retrieved middle chunk says "…do not proceed until" with the antecedent and the consequence both lost.

**Expected competencies.** After this module a participant can build a format-dispatching loader, choose and justify a chunking strategy per document type, run and evaluate OCR on Arabic scans, attach a lifecycle-aware metadata schema, and measure chunk quality with numbers rather than vibes.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Build a format-dispatching ingestion pipeline for PDF/DOCX/HTML/XLSX | LO2 |
| 2.2 | Diagnose and mitigate parsing loss, including tables and multi-column layout | LO2, LO6 |
| 2.3 | Run OCR on Arabic scans and evaluate character-error rate | LO2 |
| 2.4 | Select a chunking strategy per document type and justify the trade-off | LO2, LO5 |
| 2.5 | Attach lifecycle metadata that enables freshness filtering and citation | LO2, LO5 |

## Technical Content

### 1. The ingestion contract: where RAG quality is actually won

The offline path's output is a list of chunks, each a `(text, metadata)` pair. Everything downstream — embedding, retrieval, reranking, generation — operates only on this artefact. Two invariants must hold or the whole pipeline inherits a defect it cannot repair:

- **Fidelity:** the chunk text faithfully represents the source. A table flattened to `"1200 1500 1800"` with no column headers is *technically* text and *practically* useless — the numbers have lost their meaning.
- **Self-containment:** a chunk should be answerable-from on its own. A chunk that begins mid-clause forces the retriever to also find its neighbours, which it usually won't.

The expensive lesson: **retrieval tuning cannot recover information destroyed at parse time.** If the allowance figure never became searchable text, no embedding model, reranker, or prompt will find it. This is why the module sits early and why its acceptance criteria are measured, not assumed.

**Instructor note:** open by running the naive baseline's parser over one scanned Arabic HR PDF from Lab 1 and printing the extracted text — it comes back empty or as boxes. Pin that empty output next to the F1 sticker on the wall poster. This is the concrete villain the module defeats.

### 2. Parsing heterogeneous formats

Each format fails differently; a production loader dispatches on type and handles each failure mode explicitly:

| Format | Primary tool | Silent failure mode | Mitigation |
|---|---|---|---|
| Digital PDF | PyMuPDF (`fitz`) | Two-column layout read across columns; tables collapsed | block/word extraction with coordinates; table detection |
| Scanned PDF | Tesseract / a layout-OCR model | Returns empty text — looks like a blank document | detect "no text layer" → route to OCR |
| DOCX | `python-docx` / `unstructured` | Tables and text-boxes skipped; only paragraphs read | iterate tables explicitly; serialise cells |
| HTML | `trafilatura` / BeautifulSoup | Nav bars, cookie banners, and footers become "content" | main-content extraction; strip boilerplate |
| XLSX | `openpyxl` / pandas | Merged cells and multi-row headers scramble rows | header-aware serialisation to key-value text |

The design principle is a **parser registry**: one dispatch function maps a MIME type / extension to a handler that returns a normalised `ParsedDocument` (blocks with type tags: heading, paragraph, table, list-item). Tables are never flattened to bare numbers — they are serialised so each cell carries its row and column context (`"Grade 9 | Housing Allowance | 3,200 SAR/month"`). This one decision fixes the single most common F1 failure in enterprise corpora.

### 3. OCR and the Arabic text problem

Arabic ingestion is a first-class topic, not a footnote — roughly a third of the Dalil corpus is Arabic, and some of it is scanned.

- **Detection first:** a PDF page with a text layer needs no OCR; one without returns empty. Route only text-less pages to OCR — OCR is slow and lossy, so never apply it blindly.
- **Arabic-specific pitfalls:** right-to-left reading order, cursive letter-joining, diacritics, and the Arabic-Indic vs Western digit sets (٠١٢٣ vs 0123). A naive OCR pass mangles reading order and misreads digits — fatal when the digit *is* the answer (an allowance amount, a circular number).
- **Normalisation:** unify digit sets, strip tatweel (ـ elongation), normalise alef/hamza variants, and preserve—don't collapse—meaningful whitespace. Do this consistently at ingest **and** at query time, or Arautomated queries won't match indexed text (a preview of F3, next module).
- **Measure it:** run OCR against a small hand-transcribed gold set and report **character-error rate (CER)**. The course target is CER ≤ 5% on the Arabic scan subset; above that, answers about numbers become untrustworthy and the fix is a better OCR model, not a better retriever.

### 4. Chunking strategies and their trade-offs

Chunking decides what unit of text becomes retrievable. The strategies, worst to best for enterprise policy documents:

| Strategy | How | Pro | Con |
|---|---|---|---|
| Fixed-size (naive) | every N characters | trivial | shreds sentences and clauses (F2) |
| Recursive character | split on ¶ → sentence → word until under size | respects some structure | still blind to document semantics |
| Structure-aware | split on headings/sections, keep tables whole | clauses and tables stay intact | needs a structure-preserving parser (§2) |
| Semantic | split where embedding similarity drops | topically coherent chunks | compute cost; can merge unrelated short sections |

Two parameters govern all of them: **chunk size** (too small → context-starved; too large → dilutes the relevant signal and costs generation tokens) and **overlap** (a window of shared text between neighbours so a clause spanning a boundary survives in at least one chunk). Course defaults after tuning: ~512 tokens with ~64-token overlap for prose, and **one chunk per table/clause regardless of size** for structured content.

The professional stance: **structure-aware first, tune size second.** A section-aware splitter that keeps a policy clause and its table together eliminates most F2 failures before size tuning even begins. Chunk size is a dial you turn *after* the structure is right — turning it first is polishing shattered glass.

### 5. Metadata enrichment and the document lifecycle

A chunk is not just text; it is text **plus a payload** that later stages depend on:

- **Provenance:** `source_path`, `doc_id`, `page`, `section_title` — these become the citation (M5) and the audit trail. A chunk you cannot cite is a chunk you cannot ship in a regulated workflow.
- **Access control:** `department`, `sensitivity` — the retrieval filter (M4/M5) reads these. If they are not attached at ingest, per-user access is a redesign later (Module 1's warning made concrete).
- **Lifecycle:** `effective_date`, `version`, `superseded_by`, `language`. This is the anti-staleness machinery: when corpus_v2 lands on Day 4, the superseded 2023 policy is *marked*, not deleted, and retrieval can prefer current documents. Without these fields, F8 is unfixable.

Metadata is cheap to attach at ingest and expensive to backfill — attach the full schema from the first document, even fields you don't use yet.

### 6. Common mistakes & production considerations

1. Trusting `extract_text()` and never measuring what fraction of the corpus produced usable text — the silent-coverage-gap that dooms the whole assistant.
2. Flattening tables to bare numbers, destroying the exact facts users most often ask for.
3. OCR-ing every page blindly (slow, lossy) instead of only text-less pages.
4. Fixed-size chunking because it is one line of code — buying F2 fragmentation across the entire corpus.
5. Chunking before parsing is trustworthy — you cannot chunk structure you never extracted.
6. No document-lifecycle metadata — superseded documents live forever in the index, indistinguishable from current ones.
7. Inconsistent Arabic normalisation between ingest and query — indexed text and queries silently stop matching.

Production: incremental re-ingestion on document-change events (don't rebuild 300 docs to update one); idempotent upserts keyed on `doc_id` + content hash so re-running ingestion is safe; a parse-quality dashboard (chunks/doc, empty-text docs, table count) reviewed on every corpus update; and a quarantine for documents that fail parsing thresholds rather than silently indexing junk.

## Code Examples

### The parser registry (format dispatch with explicit failure handling)

```python
# src/dalil/ingest/loaders.py
"""Format-dispatching loader. Returns a normalised ParsedDocument whose
blocks carry a type tag — the structure the chunker (structure-aware) needs."""
from dataclasses import dataclass, field
from pathlib import Path

import fitz                      # PyMuPDF
import openpyxl
import trafilatura
from docx import Document as Docx


@dataclass
class Block:
    text: str
    kind: str                    # "heading" | "paragraph" | "table" | "list"


@dataclass
class ParsedDocument:
    doc_id: str
    blocks: list[Block] = field(default_factory=list)
    needs_ocr: bool = False      # set when a PDF page has no text layer


def load(path: Path) -> ParsedDocument:
    dispatch = {".pdf": _load_pdf, ".docx": _load_docx,
                ".html": _load_html, ".htm": _load_html, ".xlsx": _load_xlsx}
    handler = dispatch.get(path.suffix.lower())
    if handler is None:
        raise ValueError(f"unsupported format: {path.suffix} ({path.name})")
    return handler(path)


def _load_pdf(path: Path) -> ParsedDocument:
    doc = ParsedDocument(doc_id=path.stem)
    with fitz.open(path) as pdf:
        for page in pdf:
            text = page.get_text("text").strip()
            if not text:                      # F1 root cause: scanned page,
                doc.needs_ocr = True          # route to OCR (see ocr.py)
                continue
            # "blocks" mode preserves reading order for multi-column layouts
            for b in page.get_text("blocks"):
                block_text = b[4].strip()
                if block_text:
                    doc.blocks.append(Block(block_text, "paragraph"))
    return doc


def _load_docx(path: Path) -> ParsedDocument:
    doc = ParsedDocument(doc_id=path.stem)
    dx = Docx(path)
    for para in dx.paragraphs:
        if para.text.strip():
            kind = "heading" if para.style.name.startswith("Heading") else "paragraph"
            doc.blocks.append(Block(para.text.strip(), kind))
    for table in dx.tables:                   # tables are SKIPPED by naive loaders
        doc.blocks.append(Block(_serialise_table(table), "table"))
    return doc


def _serialise_table(table) -> str:
    """Serialise so each cell keeps its header context — never bare numbers."""
    rows = [[c.text.strip() for c in row.cells] for row in table.rows]
    if not rows:
        return ""
    header, *body = rows
    lines = [" | ".join(f"{h}: {v}" for h, v in zip(header, r)) for r in body]
    return "\n".join(lines)


def _load_html(path: Path) -> ParsedDocument:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    main = trafilatura.extract(raw) or ""     # strips nav/cookie/footer boilerplate
    doc = ParsedDocument(doc_id=path.stem)
    for para in filter(None, (p.strip() for p in main.split("\n"))):
        doc.blocks.append(Block(para, "paragraph"))
    return doc


def _load_xlsx(path: Path) -> ParsedDocument:
    doc = ParsedDocument(doc_id=path.stem)
    wb = openpyxl.load_workbook(path, data_only=True)
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            continue
        header = [str(h) if h is not None else "" for h in rows[0]]
        for r in rows[1:]:
            cells = " | ".join(f"{h}: {v}" for h, v in zip(header, r)
                               if v is not None)
            if cells:
                doc.blocks.append(Block(f"[{ws.title}] {cells}", "table"))
    return doc
```

### Arabic-aware OCR with a quality gate

```python
# src/dalil/ingest/ocr.py
"""OCR only text-less pages; normalise Arabic; measure CER against a gold set."""
import re
import pytesseract
from pdf2image import convert_from_path

_ARABIC_INDIC = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
_TATWEEL = "ـ"


def normalise_arabic(text: str) -> str:
    """MUST be applied identically at ingest AND query time (prevents F3)."""
    text = text.translate(_ARABIC_INDIC)          # ٠١٢ -> 012 (digits are answers)
    text = text.replace(_TATWEEL, "")             # strip elongation
    text = re.sub("[إأآا]", "ا", text)            # normalise alef variants
    text = re.sub(r"\s+", " ", text)              # collapse runaway whitespace
    return text.strip()


def ocr_pdf(path, dpi: int = 300) -> list[str]:
    pages = convert_from_path(str(path), dpi=dpi)
    out = []
    for img in pages:
        # ara+eng: the corpus is bilingual; psm 4 = single column of text
        raw = pytesseract.image_to_string(img, lang="ara+eng", config="--psm 4")
        out.append(normalise_arabic(raw))
    return out


def character_error_rate(hypothesis: str, reference: str) -> float:
    """CER = edit_distance / len(reference). Course gate: <= 0.05 on scans."""
    import Levenshtein
    if not reference:
        return 0.0
    return Levenshtein.distance(hypothesis, reference) / len(reference)
```

### Structure-aware chunking with lifecycle metadata

```python
# src/dalil/ingest/chunker.py
"""Structure-aware chunking: split on headings, keep tables whole, add overlap
only within prose. Emits chunks with the FULL metadata payload (M4/M5 depend on it)."""
from dataclasses import dataclass
from datetime import date

from dalil.ingest.loaders import Block, ParsedDocument


@dataclass
class Chunk:
    text: str
    metadata: dict


def chunk_document(doc: ParsedDocument, meta: dict,
                   target_tokens: int = 512, overlap_tokens: int = 64) -> list[Chunk]:
    chunks: list[Chunk] = []
    section_title = meta.get("title", doc.doc_id)
    buffer: list[str] = []

    def flush():
        if buffer:
            chunks.append(_emit(" ".join(buffer), section_title, meta))
            buffer.clear()

    for block in doc.blocks:
        if block.kind == "heading":
            flush()
            section_title = block.text                 # citations point at sections
        elif block.kind == "table":
            flush()
            chunks.append(_emit(block.text, section_title, meta))  # table = 1 chunk
        else:
            buffer.append(block.text)
            if _tokens(" ".join(buffer)) >= target_tokens:
                flush()
    flush()
    return _add_overlap(chunks, overlap_tokens)


def _emit(text: str, section: str, meta: dict) -> Chunk:
    return Chunk(text=text, metadata={
        "doc_id": meta["doc_id"],
        "source_path": meta["source_path"],
        "section_title": section,
        "language": meta.get("language", "unknown"),
        # --- access control (M4/M5 retrieval filter reads these) ---
        "department": meta.get("department", "public"),
        "sensitivity": meta.get("sensitivity", "internal"),
        # --- lifecycle (anti-staleness machinery, F8) ---
        "effective_date": meta.get("effective_date", str(date.today())),
        "version": meta.get("version", "1"),
        "superseded_by": meta.get("superseded_by"),      # None == current
    })


def _tokens(text: str) -> int:
    return max(1, len(text) // 4)                        # ~4 chars/token heuristic
```

## Hands-on Lab 2 — Build the Ingestion Pipeline

| | |
|---|---|
| **Objective** | Parse the full 300-document Dalil corpus with format dispatch + Arabic OCR + structure-aware chunking + lifecycle metadata; measure chunk-quality statistics and prove F1/F2 retreat versus the naive baseline |
| **Duration** | 50 minutes |
| **Setup** | Lab 1 solution; `git checkout lab2-start`; `pip install pymupdf python-docx openpyxl trafilatura pytesseract pdf2image python-Levenshtein`; Tesseract + Arabic language pack pre-installed in the course image |

**Instructions & tasks**

1. *(10 min)* Implement the parser registry `load()` dispatch; run `make ingest` over `corpus_v1/` and read the parse report — note the count of `needs_ocr` documents (~28) and any `unsupported format` errors.
2. *(10 min)* Wire the OCR path for `needs_ocr` documents; run OCR over the scan subset; compute CER against the provided `ocr_gold/` transcripts. Target CER ≤ 5%; if higher, raise DPI to 400 and re-measure.
3. *(15 min)* Implement structure-aware chunking with tables-kept-whole; re-index into the `dalil_ingest` collection; produce chunk-quality stats: chunks/doc, % chunks starting mid-sentence (should drop from ~40% naive to < 8%), table-chunk count.
4. *(10 min)* Attach the full metadata schema; verify five random chunks carry `department`, `effective_date`, and `section_title`. Confirm one known allowance figure is now present as searchable text (it was lost in Lab 1).
5. *(5 min)* Re-run three Lab 1 F1/F2 probes; confirm the evidence text is now retrievable. Strike F1 and F2 off the wall poster. Commit `feat(ingest): structure-aware bilingual pipeline`.

**Expected output**
```
$ make ingest
Parsed 300 docs: 214 digital, 28 scanned->OCR, 41 docx, 12 html, 5 xlsx
  0 unsupported, 3 quarantined (parse-quality below threshold)
Chunks: 4,812 (avg 16.0/doc)  tables kept whole: 342
Mid-sentence starts: 6.1%  (naive baseline: 41.3%)
OCR CER on scan subset: 3.8%  (gate: <= 5.0%)  PASS
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `needs_ocr` on a digital PDF | Text layer present but selectable-only in one font | Lower the empty-text threshold; inspect with `page.get_text("dict")` |
| OCR CER ~18% on Arabic | Wrong PSM or missing `ara` pack | `--psm 4`; verify `tesseract --list-langs` shows `ara`; raise DPI |
| Tables still flattened to numbers | Loader used naive text mode | Confirm `_serialise_table` runs; check `kind=="table"` blocks exist |
| Arabic query still misses | Normalisation at ingest only, not query | Apply `normalise_arabic` in the query path too (foreshadows M3) |
| Chunk count explodes to 30k | Overlap applied across tables | Overlap prose only; tables are atomic chunks |

**Instructor notes.** The money moment is step 4: the allowance figure that produced a confident-wrong answer in Lab 1 is now retrievable — pull it up on the projector beside the F1 sticker and remove the sticker physically. The OCR CER measurement (step 2) is where DS-background participants first feel that "coverage" is a number they own. Fast finishers: try semantic chunking on one long policy and compare chunk coherence to structure-aware — usually a wash for policy docs, which teaches "don't pay for semantic chunking without evidence."

## Mini Exercises

**Quiz (5 questions)**
1. Which failure class is impossible to fix downstream if parsing drops a table? → F1 (parsing loss) — the fact never became searchable text.
2. Why OCR only text-less pages instead of every page? → OCR is slow and lossy; digital text is already perfect and cheaper.
3. What two chunk parameters trade context against precision? → chunk size and overlap.
4. Why must Arabic normalisation run at both ingest and query time? → otherwise indexed text and queries diverge and stop matching (F3).
5. True/False: bigger chunks always improve answers. → **False** — they dilute the relevant signal and inflate generation cost.

**Debugging exercise.** Given a chunk that reads `"…shall not exceed"` with no antecedent and its neighbour that reads `"The housing allowance"`, decide whether the fix is smaller chunks, more overlap, or structure-aware splitting — and defend why structure-aware is the root-cause fix while overlap is a band-aid.

**Code-review exercise.** Review an ingestion PR that: OCRs every page unconditionally, flattens tables with `" ".join(cells)`, and omits `effective_date`. Name the failure class each choice re-introduces (F1 via table flattening, F8 via missing lifecycle, plus a performance regression from blind OCR).

**Discussion questions.**
- Your corpus is 60% Arabic scans with CER stuck at 9%. Do you ship, invest in a better OCR model, or scope out the scanned subset — and how do you communicate the coverage limit to users honestly?
- A stakeholder wants "just re-ingest everything nightly." What does idempotent, change-triggered incremental ingestion buy you over a nightly full rebuild at 300 → 30,000 → 3M documents?

## Case Study — The Allowance Table That Nobody Could Retrieve

**Scenario.** A Saudi government agency's HR assistant, built on naive RAG, answers salary-grade and allowance questions confidently and wrongly. Investigation shows the authoritative figures live in an XLSX grade table and a scanned Arabic PDF appendix — neither of which produced usable text. 22% of the corpus (by document count) contributed *zero* searchable content.

**Business context.** Wrong allowance answers create pay-expectation disputes and erode trust in the whole assistant within a week of launch; the agency's audit unit requires that every answer cite a source document and page.

**Technical challenge.** Raise real coverage from 78% to ≥ 98% of documents without changing the retrieval or generation stack — proving the problem is entirely in ingestion.

**Constraints.** The XLSX has merged multi-row headers; the scanned appendix is Arabic with Arabic-Indic digits; some circulars are superseded but visually identical to current ones; every chunk must carry citable provenance for the audit unit.

**Solution approach (facilitate, don't lecture).** Header-aware XLSX serialisation so each figure keeps its grade and allowance-type context; detect-then-OCR the scanned appendix with Arabic normalisation and a CER gate; attach `effective_date`/`superseded_by` so the current circular is preferable to its predecessor; and a parse-quality dashboard that flags the three still-unparseable documents for manual transcription rather than silent inclusion. Zero retrieval changes — the coverage jump is entirely upstream.

**Discussion questions.**
1. Which single ingestion defect caused the most wrong answers — table flattening or missing OCR? How would you measure it?
2. The superseded-but-identical circulars: is de-duplication an ingestion job, a metadata job, or a retrieval job? (metadata + retrieval — you mark, then prefer)
3. What is the honest coverage number to report to the audit unit, and how do you keep it current as the corpus grows?
4. Design the two-line acceptance test that would have blocked launch until coverage crossed 98%.

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Document parse-success rate | Coverage | ≥ 98% of docs produce usable text | parse report |
| Mid-sentence chunk starts | Chunk quality | < 8% (naive ~41%) | chunk analyser |
| Table chunks preserved whole | Chunk quality | 100% of detected tables | table-chunk count |
| OCR character-error rate (scans) | Fidelity | ≤ 5% on Arabic scan subset | vs `ocr_gold/` |
| Metadata completeness | Governance | 100% chunks carry provenance + lifecycle | schema validator |
| Incremental re-ingest correctness | Reliability | changed doc only → idempotent upsert | change-event test |

**Example benchmark table (filled during lab):**

| Pipeline | Docs with text | Chunks | Mid-sentence starts | Tables whole | OCR CER |
|---|---|---|---|---|---|
| Naive (Lab 1) | 78% | 8,900 (500-char) | 41.3% | 0% | n/a (no OCR) |
| Structure-aware (Lab 2) | 99.0% | 4,812 | 6.1% | 100% | 3.8% |

## Required Visuals and Training Assets

### Diagrams
1. **Ingestion pipeline flow** — *Purpose:* the offline path's front half, coloured into the course anchor diagram. *Elements:* sources (PDF/DOCX/HTML/XLSX icons) → parser registry (dispatch fan-out) → OCR branch for text-less pages → normalisation → structure-aware chunker → metadata enrichment → chunks. *Style:* left-to-right pipeline; F1 and F2 stickers shown being removed at the parse and chunk stages. *Designer note:* reuse the Module 1 palette; stamp "M2" on these stages of the wall poster.
2. **Chunking-strategy comparison** — *Elements:* one policy clause shown chunked four ways (fixed / recursive / structure-aware / semantic) with fragmentation highlighted in red on fixed and preserved clauses in green on structure-aware. *Style:* four-panel before/after.
3. **Table-serialisation before/after** — *Elements:* an allowance table shown flattened to bare numbers (useless) vs serialised with header context (searchable). *Style:* split panel with the same source table.
4. **Document-lifecycle timeline** — *Elements:* a circular superseded by a newer version; `effective_date`/`superseded_by` fields annotated; the index keeping both but marking one current. *Style:* timeline strip feeding into the anti-staleness (F8) motif.

### Images (screenshots)
1. **Empty extraction from a scanned Arabic PDF** — *why:* makes F1 visceral; *content:* the naive extractor returning "" beside the actual scanned page.
2. **Serialised table chunk in the inspector notebook** — *why:* shows the fix; *content:* `"Grade 9 | Housing Allowance | 3,200 SAR/month"` as searchable text.
3. **OCR CER report terminal** — *why:* coverage-as-a-number; *content:* per-document CER with the 5% gate line.
4. **Chunk-quality dashboard** — *why:* participants verify their state; *content:* chunks/doc histogram, mid-sentence-start percentage, table count.

### Simulations
1. **Blind-OCR cost** — *Setup:* provided script OCRs all 300 documents unconditionally. *Expected:* 40× ingest time, and *worse* text on digital PDFs than their native text layer. *Learning objective:* detect-then-OCR beats OCR-everything.
2. **Chunk-size sweep** — *Setup:* re-index at 128/256/512/1024 tokens and re-run the same 12 probes. *Expected:* tiny chunks starve context; huge chunks retrieve but bury the answer. *Learning objective:* the size/precision trade-off, seen not asserted.

### Interactive Activities
- **Format autopsy (15 min):** each pair gets one "hostile" document (merged-cell XLSX, two-column PDF, boilerplate-heavy HTML) and must produce clean chunks, then present the one trick that mattered.
- **Metadata design workshop (10 min):** groups design the payload schema for a new sensitive-HR document class (which fields enable access control vs freshness vs citation) and defend each field's later consumer.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `corpus_v1/` | Course-synthesised fictional Saudi org (AR/EN) | PDF/DOCX/HTML/XLSX | 300 docs | Full ingestion pipeline |
| `ocr_gold/` | Hand-transcribed scan subset | TXT | 20 pages | CER measurement |
| `chunk_quality/reference_stats.json` | Reference solution output | JSON | 1 file | Chunk-stat comparison |

### Demo Requirements
- **Instructor demo:** live parse of one scanned Arabic HR PDF — empty naive output, then detect-then-OCR producing correct normalised digits — then the allowance figure appearing as a retrievable chunk.
- **Student demo:** two pairs present their chunk-quality stats and the one document that fought back hardest.
- **Expected outputs:** every pair has `corpus_v1` fully ingested into `dalil_ingest`, F1 and F2 stickers removed from the poster.

---

# Module 3 — Embeddings and Vector Databases

## Module Overview

**Purpose.** Chunks become *retrievable* only once they are embedded into vectors and stored where similarity search is fast. This module owns the second half of the offline path and the first half of the online path: choosing an embedding model (multilingual, because Dalil is bilingual), understanding similarity metrics and approximate-nearest-neighbour indexes, and operating a real vector database. It retires **F3 (semantic miss)** — the right document exists but the wrong chunks are retrieved because of a vocabulary or language gap.

**Business relevance.** The embedding model is the single most consequential quality decision in a RAG system after ingestion, and the one teams most often get wrong by defaulting to an English-only model on a bilingual corpus. In the Saudi enterprise a user asks "بدل السكن" (housing allowance) and the answer lives in an English HR policy — only a genuinely multilingual embedding space bridges that gap. Meanwhile the vector database is the piece that must stay fast and cheap as the corpus grows from thousands to millions of chunks; the engineer who understands HNSW and quantization is the one who keeps p95 latency flat while the index 100×'s.

**Industry use cases.**
- A bilingual policy assistant where 40% of queries are Arabic against a partly-English corpus — multilingual embeddings are the difference between 0.55 and 0.90 recall@10.
- A legal-precedent search where near-duplicate documents must be distinguished — similarity metric and vector normalisation choices decide whether the right precedent ranks first or fifth.
- A cost-constrained deployment indexing 5M chunks on commodity RAM — scalar quantization cuts index memory 4× with a measured recall cost the team accepts on purpose.

**Expected competencies.** After this module a participant can select and justify an embedding model for a bilingual corpus, explain cosine vs dot-product and why normalisation matters, reason about HNSW parameters and quantization trade-offs, build and operate a Qdrant collection with payload filters, and benchmark recall@k and latency against a labelled query set.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Select an embedding model for a bilingual corpus and justify it with recall numbers | LO3 |
| 3.2 | Explain similarity metrics and the role of vector normalisation | LO3 |
| 3.3 | Reason about HNSW parameters and quantization trade-offs | LO3, LO5 |
| 3.4 | Build a Qdrant collection with payloads, filters, and correct schema | LO3 |
| 3.5 | Benchmark recall@k and query latency on a labelled query set | LO3, LO6 |

## Technical Content

### 1. What an embedding is and why the model choice dominates

An embedding maps text to a fixed-length vector such that semantically similar texts land near each other. Retrieval then becomes nearest-neighbour search in that vector space. Two properties decide everything:

- **Coverage of the languages and domain.** A model trained mostly on English produces a vector space where Arabic queries and English documents are *far apart even when they mean the same thing* — the direct cause of F3 on a bilingual corpus. The course uses **`BAAI/bge-m3`**: multilingual (100+ languages), 1024-dimensional, and capable of dense, sparse, and multi-vector output (the sparse capability matters in M4).
- **Symmetry of use.** Some models are trained for query↔document asymmetry (a short question vs a long passage). bge-m3 handles both; models that require an instruction prefix (`"query: …"`, `"passage: …"`) must have it applied consistently or retrieval silently degrades.

The professional habit: **never adopt an embedding model without measuring recall@k on your own labelled queries.** Leaderboard scores are on other people's data; your corpus and your users' phrasing are what matter.

### 2. Similarity metrics and normalisation

Three metrics appear in practice:

| Metric | Definition | Use when |
|---|---|---|
| Cosine | angle between vectors | text similarity (default; magnitude-invariant) |
| Dot product | cosine × magnitudes | vectors already normalised, or magnitude carries signal |
| Euclidean (L2) | straight-line distance | rarely for text; some image models |

For text, **cosine is the default** because it ignores vector magnitude and compares *direction* (meaning). The critical operational detail: if you L2-**normalise** embeddings at index and query time, cosine and dot product become equivalent — and dot product is faster. bge-m3 vectors are normalised (`normalize_embeddings=True`), so the Qdrant collection uses `Distance.COSINE` and the two agree. Forgetting to normalise consistently is a classic silent-quality bug: half your vectors long, half short, rankings scrambled.

### 3. Approximate nearest neighbour: HNSW and its knobs

Exact nearest-neighbour search is O(N) per query — fine for 10k chunks, ruinous for 10M. Vector databases use **HNSW** (Hierarchical Navigable Small World), a graph index giving ~log(N) search with tunable accuracy:

- **`m`** — edges per node. Higher `m` → better recall, more memory. Course default 16.
- **`ef_construct`** — search width during index build. Higher → better graph, slower build. Default 100.
- **`ef` (search)** — candidate list size at query time. **The recall/latency dial you actually turn in production:** higher `ef` → higher recall, higher latency. Default 64; raise it if recall@k is short of target.

The mental model participants must hold: HNSW trades a little accuracy for a lot of speed, and `ef` is how you buy accuracy back per-query without rebuilding anything.

### 4. Quantization: the memory/recall trade

Full 1024-dim float32 vectors cost 4 KB each — 4 GB per million chunks, in RAM. **Scalar quantization** (float32 → int8) cuts that ~4× with a small, *measurable* recall cost; **binary quantization** cuts it ~32× with a larger cost, usable when followed by a rescoring pass over full vectors. The discipline is the same as everywhere in this course: **quantize on purpose, with a measured recall delta you chose to accept**, not by default and not by fear. Qdrant supports quantization as a collection setting with optional on-the-fly rescoring, so the full vectors can refine the quantized shortlist.

### 5. Operating Qdrant: collections, payloads, filters

Qdrant (the course's primary vector DB; pgvector is the "when you already run Postgres" alternative) stores **points** = `(id, vector, payload)`. The payload is the metadata from M2, and it is not decoration — it is the **access-control and freshness filter**:

- **Payload indexes** on `department`, `language`, `superseded_by` make filtered search fast. A query from an HR user filters `department in {hr, public}` *inside* the ANN search, not after — so a user never even retrieves a document they may not see (Module 1's access-control requirement, now concrete).
- **Filtering + ANN** interact: aggressive filters can starve HNSW of candidates, so Qdrant offers payload-index-aware search. Teach the failure: a filter so narrow that recall collapses because the graph can't find enough matching neighbours.
- **pgvector when:** the data already lives in Postgres, scale is modest (< ~1M vectors), and transactional consistency with relational data matters more than peak ANN performance.

### 6. Common mistakes & production considerations

1. Using an English-only embedding model on a bilingual corpus — the number-one cause of F3 in Saudi deployments.
2. Inconsistent normalisation between index and query — scrambled rankings, no error raised.
3. Forgetting the instruction prefix a model requires — silent recall loss.
4. Never measuring recall@k — flying blind; you cannot tell a good retriever from a bad one.
5. Rebuilding the whole index to add documents instead of upserting — minutes become hours at scale.
6. Applying access control *after* retrieval (post-filter) instead of *inside* it — a data-leak waiting to happen and slower besides.
7. Quantizing by default without measuring the recall cost — accepting quality loss you never quantified.

Production: index freshness (upsert on document change, keyed on `doc_id`); collection versioning and blue-green re-embedding when the embedding model changes (a model swap invalidates every vector — treat it as a migration); memory sizing (`vectors × dim × bytes` + HNSW graph overhead); and monitoring recall@k on a rolling labelled set so silent degradation surfaces.

## Code Examples

### Embedding and Qdrant collection with payload indexes

```python
# src/dalil/index/collection.py
"""Build the Dalil collection: bge-m3 dense vectors, cosine, payload indexes
for access-control + freshness filtering. Upsert is idempotent on doc_id+chunk."""
import hashlib

from qdrant_client import QdrantClient
from qdrant_client.models import (Distance, PayloadSchemaType, PointStruct,
                                  VectorParams, ScalarQuantization,
                                  ScalarQuantizationConfig, ScalarType)
from sentence_transformers import SentenceTransformer

EMB = SentenceTransformer("BAAI/bge-m3")     # multilingual, 1024-dim, normalised
DIM = 1024
COLLECTION = "dalil"


def build_collection(qdr: QdrantClient) -> None:
    qdr.recreate_collection(
        COLLECTION,
        vectors_config=VectorParams(size=DIM, distance=Distance.COSINE),
        # scalar quantization: ~4x smaller, rescore with full vectors keeps recall
        quantization_config=ScalarQuantization(
            scalar=ScalarQuantizationConfig(type=ScalarType.INT8, always_ram=True)),
    )
    # Payload indexes => filtering happens INSIDE the ANN search (fast + secure)
    for field, schema in [("department", PayloadSchemaType.KEYWORD),
                          ("language", PayloadSchemaType.KEYWORD),
                          ("superseded_by", PayloadSchemaType.KEYWORD),
                          ("effective_date", PayloadSchemaType.DATETIME)]:
        qdr.create_payload_index(COLLECTION, field_name=field, field_schema=schema)


def _point_id(doc_id: str, idx: int) -> str:
    # Stable id => re-ingesting the same chunk UPDATES it (idempotent upsert)
    return hashlib.sha1(f"{doc_id}:{idx}".encode()).hexdigest()


def index_chunks(qdr: QdrantClient, chunks: list) -> int:
    texts = [c.text for c in chunks]
    vecs = EMB.encode(texts, normalize_embeddings=True, batch_size=64)
    points = [
        PointStruct(id=_point_id(c.metadata["doc_id"], i),
                    vector=v.tolist(), payload={**c.metadata, "text": c.text})
        for i, (c, v) in enumerate(zip(chunks, vecs))
    ]
    qdr.upsert(COLLECTION, points, wait=True)
    return len(points)
```

### Filtered dense retrieval (access control + freshness inside the search)

```python
# src/dalil/retrieve/dense.py
"""Dense retrieval with payload filters. The filter enforces access control and
prefers current documents — applied INSIDE the ANN search, never after it."""
from qdrant_client import QdrantClient
from qdrant_client.models import (Filter, FieldCondition, MatchValue, IsNullCondition,
                                  PayloadField, SearchParams)
from sentence_transformers import SentenceTransformer

from dalil.ingest.ocr import normalise_arabic     # SAME normalisation as ingest

EMB = SentenceTransformer("BAAI/bge-m3")


def dense_search(qdr: QdrantClient, query: str, *, department: str,
                 top_k: int = 8, ef: int = 128, current_only: bool = True):
    qv = EMB.encode(normalise_arabic(query), normalize_embeddings=True)

    must = [Filter(should=[                       # user sees their dept + public
        FieldCondition(key="department", match=MatchValue(value=department)),
        FieldCondition(key="department", match=MatchValue(value="public")),
    ])]
    if current_only:                              # prefer non-superseded docs (F8)
        must.append(IsNullCondition(is_null=PayloadField(key="superseded_by")))

    hits = qdr.query_points(
        COLLECTION, query=qv.tolist(), limit=top_k,
        query_filter=Filter(must=must),
        search_params=SearchParams(hnsw_ef=ef),   # the recall/latency dial
        with_payload=True,
    ).points
    return hits
```

### Recall@k and latency benchmark harness

```python
# src/dalil/evaluation/retrieval_metrics.py
"""Measure recall@k and latency against retrieval_labels.jsonl:
each query lists the doc_ids that CONTAIN the answer. This is how we prove F3 retreats."""
import json
import time
from statistics import median


def recall_at_k(qdr, search_fn, labels_path: str, k: int = 10) -> dict:
    labels = [json.loads(line) for line in open(labels_path, encoding="utf-8")]
    hits_at_k, latencies = [], []
    for row in labels:
        relevant = set(row["relevant_doc_ids"])
        t0 = time.perf_counter()
        results = search_fn(qdr, row["query"], department=row.get("department", "public"),
                            top_k=k)
        latencies.append((time.perf_counter() - t0) * 1000)
        retrieved_docs = {h.payload["doc_id"] for h in results}
        hits_at_k.append(1.0 if relevant & retrieved_docs else 0.0)
    return {
        "queries": len(labels),
        f"recall@{k}": round(sum(hits_at_k) / len(hits_at_k), 3),
        "latency_p50_ms": round(median(latencies), 1),
        "latency_p95_ms": round(sorted(latencies)[int(0.95 * len(latencies))], 1),
    }
```

## Hands-on Lab 3 — Embed, Index, and Measure Recall

| | |
|---|---|
| **Objective** | Embed the Lab 2 chunk set with bge-m3, build the Qdrant `dalil` collection with payload filters, and benchmark recall@k and latency on the 200-query labelled set — proving F3 retreats versus an English-only baseline |
| **Duration** | 50 minutes |
| **Setup** | Lab 2 solution; `git checkout lab3-start`; `docker compose up qdrant`; `pip install qdrant-client sentence-transformers`; bge-m3 pre-downloaded in the course bundle |

**Instructions & tasks**

1. *(5 min)* Build the collection with cosine + payload indexes; confirm `qdr.get_collection("dalil")` reports vector size 1024 and the four payload indexes.
2. *(10 min)* Embed and upsert all Lab 2 chunks; verify point count matches chunk count and that re-running the upsert changes nothing (idempotency check).
3. *(15 min)* Run `recall_at_k` at k=1/5/10 with bge-m3; then swap to the provided English-only model `all-MiniLM-L6-v2` and re-run. Record both in `RETRIEVAL.md` — the Arabic-query subset is where the gap is largest.
4. *(10 min)* Tune the `ef` search parameter (32 → 256); plot recall@10 vs p95 latency; pick the knee of the curve as your default.
5. *(5 min)* Verify the access-control filter: an HR-department query must never retrieve a `department="finance"` chunk. Strike F3 off the wall poster. Commit `feat(index): bge-m3 collection with filtered retrieval`.

**Expected output**
```
$ make eval-retrieval
Collection dalil: 4,812 points, dim 1024, cosine, quantization int8
bge-m3       recall@10 = 0.91  (AR subset 0.88)  p50 12ms  p95 34ms
MiniLM (EN)  recall@10 = 0.63  (AR subset 0.29)  p50 9ms   p95 22ms
ef sweep: 32->0.84  64->0.89  128->0.91  256->0.915  (knee at ef=128)
access-control check: 0/50 cross-department leaks  PASS
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Arabic recall near 0 | English-only model or normalisation skipped at query | Use bge-m3; apply `normalise_arabic` in the query path |
| Recall lower than expected everywhere | Vectors not normalised | `normalize_embeddings=True` at index AND query |
| Filtered search returns nothing | Filter too narrow / missing payload index | Create the payload index; widen filter; check field names |
| Upsert doubles point count | Non-stable ids (used enumerate index only) | Hash `doc_id:chunk_idx` for stable ids |
| p95 latency spikes | `ef` too high for the recall you need | Drop to the knee-of-curve value |

**Instructor notes.** The bge-m3 vs MiniLM Arabic-subset gap (0.88 vs 0.29) is the module's thesis in one table — put both on the shared board and let it land before explaining why. The `ef` sweep teaches that recall is a purchasable, per-query quantity. Fast finishers: enable binary quantization + rescoring and measure the recall delta — usually tiny, memory 8× smaller, a real production lever.

## Mini Exercises

**Quiz (5 questions)**
1. Why does an English-only embedding model cause F3 on a bilingual corpus? → Arabic queries and English passages land far apart in its vector space even when they mean the same thing.
2. When are cosine and dot product equivalent? → when vectors are L2-normalised.
3. Which HNSW parameter do you tune per-query to buy recall without rebuilding? → `ef` (search).
4. What does scalar quantization cost and save? → ~4× less memory for a small, measurable recall drop.
5. True/False: applying access control after retrieval is fine as long as filtered results aren't shown. → **False** — the user already retrieved documents they may not see; filter inside the search.

**Debugging exercise.** Given a query "circular 44/2025 leave policy" that retrieves semantically-similar-but-wrong leave circulars, decide whether this is F3 (semantic miss, fixable with a better embedder) or F4 (exact-identifier miss, needs sparse/hybrid) — and justify why the identifier makes this M4's problem, not M3's.

**Code-review exercise.** Review an indexing PR that: uses `all-MiniLM-L6-v2`, normalises at index but not at query, and post-filters departments in Python after retrieval. Name the recall and security defects each introduces.

**Discussion questions.**
- Your corpus grows from 5k to 5M chunks and RAM cost triples. Walk through quantization, sharding, and re-embedding-on-model-change as levers, and which you'd reach for first.
- The team wants to swap bge-m3 for a newer embedding model. Why is this a migration, not a config change, and how do you roll it out without a recall regression?

## Case Study — The Bilingual Recall Cliff at a National HR Platform

**Scenario.** A national HR shared-services platform launches a knowledge assistant that tests beautifully in English demos and collapses in production: 41% of real queries are Arabic, and on those queries recall@10 is 0.30. The retrieval, reranking, and generation code are all "correct" — the embedding model (`all-MiniLM-L6-v2`) simply cannot place Arabic queries near English HR passages.

**Business context.** Arabic-speaking employees are the majority of users; an assistant that fails for them fails, full stop. Leadership had approved launch on English-only demo metrics — a governance lesson in itself.

**Technical challenge.** Lift Arabic recall@10 from 0.30 to ≥ 0.85 without touching ingestion, and quantify the memory/latency cost of doing so at 5M chunks.

**Constraints.** On-prem inference (data residency); a fixed RAM budget that a 1024-dim float32 index at 5M vectors would blow; consistent Arabic normalisation must be retrofitted across both ingest and query without re-parsing the corpus.

**Solution approach (facilitate, don't lecture).** Swap to bge-m3 (multilingual) as a blue-green re-embedding migration; apply identical Arabic normalisation at ingest and query; fit the RAM budget with int8 scalar quantization plus full-vector rescoring, measuring the recall delta (≈ 0.01) so the trade is explicit; and stand up a rolling Arabic-subset recall monitor so a future model or normalisation change cannot silently regress it.

**Discussion questions.**
1. Which single change recovered the most Arabic recall — the model or the normalisation? Design the ablation that answers it.
2. Why is an embedding-model swap a full re-index rather than an in-place update?
3. At 5M vectors, which is the bigger risk to manage — memory or latency — and how does quantization shift that balance?
4. What launch gate would have caught the Arabic cliff before production? (recall@k on a bilingual labelled set, not English demos)

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| recall@10 (overall) | Retrieval quality | ≥ 0.88 | labelled query set |
| recall@10 (Arabic subset) | Retrieval quality | ≥ 0.85 | AR-only labels |
| Query latency p95 | Performance | ≤ 40 ms (100k chunks) | benchmark harness |
| Access-control leakage | Security | 0 cross-department hits | filter test (50 probes) |
| Index memory | Cost | within budget after quantization | Qdrant telemetry |
| Upsert idempotency | Reliability | re-ingest changes 0 points | idempotency check |

**Example benchmark table (filled during lab):**

| Embedding model | recall@1 | recall@10 | AR recall@10 | p95 latency | index size |
|---|---|---|---|---|---|
| all-MiniLM-L6-v2 (EN) | 0.38 | 0.63 | 0.29 | 22 ms | 0.4 GB |
| bge-m3 (multilingual) | 0.64 | 0.91 | 0.88 | 34 ms | 1.0 GB |
| bge-m3 + int8 quant | 0.63 | 0.90 | 0.87 | 29 ms | 0.28 GB |

## Required Visuals and Training Assets

### Diagrams
1. **Vector-space intuition (bilingual)** — *Purpose:* make F3 visual. *Elements:* a 2-D projection showing an Arabic query near its English passage under bge-m3, but far from it under an English-only model. *Style:* two side-by-side scatter plots with the same points, connectors drawn. *Designer note:* stamp "M3 retires F3" and reuse the course palette.
2. **HNSW graph search** — *Elements:* a small navigable-small-world graph with the greedy search path highlighted; `m`, `ef_construct`, `ef` annotated on the structure they control. *Style:* graph diagram with a traced query path.
3. **Recall vs latency curve (ef sweep)** — *Elements:* recall@10 and p95 latency plotted against `ef`, knee-of-curve marked. *Style:* dual-axis line chart.
4. **Qdrant point anatomy** — *Elements:* a point = id + vector + payload; payload fields colour-coded by consumer (access control, freshness, citation). *Style:* labelled record diagram feeding the retrieval-filter motif.

### Images (screenshots)
1. **Qdrant dashboard — `dalil` collection** — *why:* participants verify state; *content:* 4,812 points, dim 1024, cosine, int8 quantization.
2. **Recall benchmark terminal** — *why:* expected-output reference; *content:* bge-m3 vs MiniLM recall table with AR subset.
3. **Filtered search returning only permitted departments** — *why:* proves access control; *content:* payload `department` values in results all in the permitted set.
4. **ef-sweep plot** — *why:* the recall-is-purchasable lesson; *content:* the knee-of-curve chart.

### Simulations
1. **Normalisation mismatch** — *Setup:* index normalised, query un-normalised. *Expected:* recall halves with no error raised. *Learning objective:* silent-quality bugs; measure, don't assume.
2. **Filter starvation** — *Setup:* a filter so narrow HNSW can't find candidates. *Expected:* recall collapses despite relevant docs existing. *Learning objective:* filters and ANN interact; payload indexing matters.

### Interactive Activities
- **Model bake-off (15 min):** groups run three embedding models on the same 20 Arabic queries and rank them by recall — the numbers, not opinions, decide.
- **Quantization trade workshop (10 min):** given a RAM budget and a corpus size, groups choose a quantization strategy and defend the recall cost they'll accept.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `retrieval_labels.jsonl` | Course-authored (AR/EN) | JSONL | 200 queries → relevant doc-ids | recall@k benchmark |
| Lab 2 chunk set | Participant output | Qdrant points | 4,812 | the index under test |
| `models/all-MiniLM-L6-v2` | Pre-downloaded | safetensors | ~90 MB | English-only contrast model |

### Demo Requirements
- **Instructor demo:** run the same Arabic query under MiniLM (misses) and bge-m3 (hits) live, then the `ef` sweep showing recall climbing with latency.
- **Student demo:** two pairs present their recall table and chosen `ef` knee.
- **Expected outputs:** every pair has the `dalil` collection benchmarked, F3 sticker removed from the poster.

---

# Module 4 — Hybrid Retrieval and Reranking

## Module Overview

**Purpose.** Dense retrieval is powerful but blind to exact tokens: it blurs "Circular 44/2025" and "form HR-07" into their semantic neighbourhoods, retrieving similar-but-wrong documents. And even when the right chunk is retrieved, it may rank ninth while junk fills the top four. This module builds the two-stage retrieval stack that fixes both: **hybrid search** (dense + sparse/keyword, fused) retires **F4 (exact-match miss)**, and **cross-encoder reranking** retires **F5 (precision collapse)**.

**Business relevance.** Enterprise queries are full of identifiers — circular numbers, form codes, policy IDs, product SKUs — and a system that can't retrieve by exact token is useless for exactly the queries employees ask most. Meanwhile the generation stage (M5) can only reason over what lands in its top-k context; precision at the top of the ranking is what determines answer quality and cost. The engineer who can quantify *per query class* which stage earns its keep is the one who builds retrieval that is both accurate and defensibly not over-engineered.

**Industry use cases.**
- A compliance assistant where every second query names a circular by number — sparse retrieval is the only thing that finds "44/2025" reliably; dense retrieval alone returns the wrong circular.
- A procurement assistant matching exact form codes and part numbers alongside natural-language intent — hybrid fusion serves both in one ranking.
- A high-stakes legal assistant where the correct precedent must rank first, not fifth — a cross-encoder reranker lifts precision@4 enough to change which answer gets generated.

**Expected competencies.** After this module a participant can add sparse vectors and fuse them with dense via RRF, add a cross-encoder reranker in a two-stage budget, diagnose which query classes each stage helps, and quantify the improvement per class rather than in aggregate.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Explain where dense retrieval fails and why sparse/keyword is complementary | LO3 |
| 4.2 | Implement hybrid retrieval with RRF fusion in Qdrant | LO3, LO5 |
| 4.3 | Add a cross-encoder reranker and design the two-stage fetch/keep budget | LO3, LO5 |
| 4.4 | Diagnose retrieval failures by query class and choose the right fix | LO3, LO6 |
| 4.5 | Quantify per-query-class improvement over the dense-only baseline | LO3, LO6 |

## Technical Content

### 1. Where dense retrieval fails

Dense embeddings capture meaning and lose exact tokens. This is a *feature* for paraphrase ("annual leave" ≈ "yearly vacation") and a *bug* for identifiers:

- **Exact identifiers (F4):** "Circular 44/2025", "form HR-07", "Grade 12" — the embedding of "44/2025" is near other circular numbers, so dense retrieval returns *a* circular, rarely *the* one. No amount of embedding quality fixes this; the information the query needs is lexical, not semantic.
- **Rare terms and codes:** low-frequency tokens are under-represented in the embedding space; sparse methods weight them precisely because they are rare (IDF).
- **Long-tail phrasing:** exact quotes and boilerplate match better lexically.

The complement is **sparse retrieval**: BM25 (classic term-frequency/inverse-document-frequency) or learned sparse vectors (SPLADE / bge-m3's sparse output) that score exact and near-exact token overlap. Sparse and dense fail on *different* queries — which is precisely why fusing them beats either alone.

### 2. Fusing dense and sparse: Reciprocal Rank Fusion

Two rankers produce two ordered lists; you need one. **Reciprocal Rank Fusion (RRF)** is the robust default because it combines *ranks*, not scores (which live on incomparable scales):

```
RRF(d) = Σ over rankers r of  1 / (k + rank_r(d))     # k ≈ 60 by convention
```

A document ranked highly by *either* ranker scores well; a document ranked highly by *both* wins. RRF needs no score normalisation and no per-corpus tuning, which is why it outperforms naive weighted-sum fusion in practice. Qdrant supports server-side fusion via named vectors (a dense vector and a sparse vector per point) and a fusion query — the fusion happens in the database, not in Python.

### 3. Reranking: the precision stage

Retrieval (dense, sparse, hybrid) is a *recall* device — cast a wide net (fetch 40–100 candidates) cheaply. But the top of that list is noisy: the right chunk might be ninth (F5). A **cross-encoder reranker** fixes this. Unlike the bi-encoder embedder (which encodes query and document *separately*), a cross-encoder reads the query and each candidate *together* and scores their relevance directly — far more accurate, far more expensive, so it runs only on the shortlist. The course uses **`BAAI/bge-reranker-v2-m3`** (multilingual, pairs with bge-m3).

The **two-stage budget** is the central design pattern, and it follows directly from Module 1's cost asymmetry:

- **Stage 1 (retrieve):** hybrid fetch top-40 — cheap (tens of ms), generous recall.
- **Stage 2 (rerank):** cross-encoder scores those 40, keep top-6 — the expensive-but-accurate refinement.

"Fetch 40, keep 6" is economically rational because retrieval is cheap and generation (which pays per context token) is expensive — the reranker bridges the two by ensuring the 6 chunks that reach the prompt are the *right* 6.

### 4. Tuning the budget: fetch-k, top-k, and filters

Three dials, tuned against the labelled set with metrics, never by feel:

- **fetch-k (stage-1 candidates):** too small starves the reranker of the right chunk; too large wastes rerank compute. Typical 40–80.
- **top-k (kept after rerank):** the context budget for M5. Too small drops needed evidence; too large dilutes and costs generation tokens. Typical 4–8.
- **filters:** the M3 payload filters (department, freshness) still apply — and interact with fetch-k, since aggressive filtering shrinks the candidate pool.

The professional workflow: fix filters by policy, sweep fetch-k and top-k against nDCG/recall on the labelled set, and pick the point where the metric plateaus — paying for more candidates past the plateau is pure waste.

### 5. Diagnosing by query class

The course's diagnostic discipline: never report a single aggregate number; **break metrics out by query class** because the stack helps different classes differently:

| Query class | Dense-only | + Hybrid | + Rerank | Which stage earns it |
|---|---|---|---|---|
| Natural-language ("how much housing allowance?") | good | ≈ | better precision | rerank |
| Exact identifier ("Circular 44/2025") | poor (F4) | **fixed** | ≈ | hybrid (sparse) |
| Mixed ("leave rules in circular 44/2025") | partial | better | better | both |
| Arabic paraphrase | good (bge-m3) | ≈ | better | rerank |

This table is how an engineer justifies complexity: hybrid is *mandatory* if identifier queries exist; reranking is *worth it* if precision@k matters for generation. If a class shows no lift, that stage is not earning its latency for that class — say so.

### 6. Common mistakes & production considerations

1. Dense-only retrieval on a corpus full of identifiers — F4 across the entire identifier-query class.
2. Weighted-sum fusion of raw dense and sparse scores (incomparable scales) instead of rank-based RRF.
3. Reranking the entire corpus instead of a shortlist — hundreds of ms to seconds of latency for no recall gain.
4. fetch-k too small — the reranker can't surface a chunk that stage 1 never fetched.
5. Reporting aggregate retrieval metrics that hide a collapsed query class.
6. Forgetting that the reranker also needs to be multilingual — an English reranker on Arabic pairs re-introduces F3 at the rerank stage.

Production: reranker latency budget (batch the 40 candidates, cap sequence length); GPU vs CPU for the cross-encoder (the course model runs acceptably on CPU for 40 candidates, ~120 ms); caching rerank scores for repeated queries; and monitoring per-class metrics so a corpus shift that hurts one class surfaces before users complain.

## Code Examples

### Hybrid retrieval with RRF fusion in Qdrant

```python
# src/dalil/retrieve/hybrid.py
"""Hybrid retrieval: dense (bge-m3) + sparse (bge-m3 sparse output), fused with
RRF server-side in Qdrant. Retires F4 by scoring exact tokens the dense vector blurs."""
from qdrant_client import QdrantClient
from qdrant_client.models import (FusionQuery, Fusion, Prefetch, SparseVector,
                                  NamedSparseVector, Filter)
from FlagEmbedding import BGEM3FlagModel

from dalil.ingest.ocr import normalise_arabic

_MODEL = BGEM3FlagModel("BAAI/bge-m3", use_fp16=True)
COLLECTION = "dalil"


def _encode(query: str):
    out = _MODEL.encode(normalise_arabic(query),
                        return_dense=True, return_sparse=True)
    dense = out["dense_vecs"].tolist()
    lex = out["lexical_weights"]                 # {token_id: weight}
    sparse = SparseVector(indices=[int(i) for i in lex],
                          values=[float(w) for w in lex.values()])
    return dense, sparse


def hybrid_search(qdr: QdrantClient, query: str, *, query_filter: Filter | None = None,
                  fetch_k: int = 40):
    dense, sparse = _encode(query)
    # Two prefetch branches; Qdrant fuses their RANKS with RRF (no score scaling needed)
    result = qdr.query_points(
        COLLECTION,
        prefetch=[
            Prefetch(query=dense, using="dense", limit=fetch_k, filter=query_filter),
            Prefetch(query=NamedSparseVector(name="sparse", vector=sparse),
                     using="sparse", limit=fetch_k, filter=query_filter),
        ],
        query=FusionQuery(fusion=Fusion.RRF),
        limit=fetch_k, with_payload=True,
    )
    return result.points
```

### Cross-encoder reranking and the two-stage budget

```python
# src/dalil/retrieve/rerank.py
"""Stage 2: cross-encoder reranking of the hybrid shortlist. Fetch 40, keep 6.
Retires F5 by scoring query+chunk TOGETHER, promoting the truly-relevant chunk."""
from dataclasses import dataclass
from FlagEmbedding import FlagReranker

_RERANKER = FlagReranker("BAAI/bge-reranker-v2-m3", use_fp16=True)  # multilingual!


@dataclass
class ScoredChunk:
    doc_id: str
    text: str
    payload: dict
    rerank_score: float


def rerank(query: str, candidates, top_k: int = 6) -> list[ScoredChunk]:
    if not candidates:
        return []
    pairs = [[query, c.payload["text"]] for c in candidates]
    scores = _RERANKER.compute_score(pairs, normalize=True)   # batched, one pass
    scored = [
        ScoredChunk(doc_id=c.payload["doc_id"], text=c.payload["text"],
                    payload=c.payload, rerank_score=float(s))
        for c, s in zip(candidates, scores)
    ]
    scored.sort(key=lambda x: x.rerank_score, reverse=True)
    return scored[:top_k]                        # the 6 chunks that reach the prompt


def retrieve_and_rerank(qdr, query, *, query_filter=None, fetch_k=40, top_k=6):
    """The full two-stage stack used everywhere downstream."""
    from dalil.retrieve.hybrid import hybrid_search
    shortlist = hybrid_search(qdr, query, query_filter=query_filter, fetch_k=fetch_k)
    return rerank(query, shortlist, top_k=top_k)
```

### Per-query-class evaluation

```python
# src/dalil/evaluation/by_class.py
"""Break retrieval metrics out BY QUERY CLASS. Aggregate numbers hide collapsed
classes — this is how we prove hybrid fixes identifiers and rerank fixes precision."""
import json
from collections import defaultdict


def ndcg_at_k(retrieved_ids, relevant_ids, k=6):
    import math
    dcg = sum(1 / math.log2(i + 2) for i, d in enumerate(retrieved_ids[:k])
              if d in relevant_ids)
    ideal = sum(1 / math.log2(i + 2) for i in range(min(len(relevant_ids), k)))
    return dcg / ideal if ideal else 0.0


def evaluate_by_class(retrieve_fn, labels_path: str, k: int = 6) -> dict:
    buckets = defaultdict(list)
    for line in open(labels_path, encoding="utf-8"):
        row = json.loads(line)
        relevant = set(row["relevant_doc_ids"])
        results = retrieve_fn(row["query"])
        ids = [r.doc_id for r in results]
        buckets[row["query_class"]].append(ndcg_at_k(ids, relevant, k))
    return {cls: round(sum(v) / len(v), 3) for cls, v in buckets.items()}
```

## Hands-on Lab 4 — Hybrid Search Plus Reranker

| | |
|---|---|
| **Objective** | Add sparse vectors + RRF fusion and a bge-reranker to the Lab 3 retriever; quantify the improvement per query class and prove F4 and F5 retreat |
| **Duration** | 50 minutes |
| **Setup** | Lab 3 solution; `git checkout lab4-start`; `pip install FlagEmbedding`; bge-m3 + bge-reranker-v2-m3 pre-downloaded; the collection must carry a `sparse` named vector (rebuild helper provided) |

**Instructions & tasks**

1. *(5 min)* Rebuild the collection with a `sparse` named vector alongside dense (`make reindex-hybrid`); confirm both vectors exist per point.
2. *(10 min)* Implement `hybrid_search` with RRF; run `evaluate_by_class` for dense-only vs hybrid. Confirm the identifier class jumps (F4 fix) while natural-language stays flat.
3. *(15 min)* Add the cross-encoder reranker; run the full two-stage stack; compare nDCG@6 per class vs hybrid-only. Precision should climb across classes (F5 fix).
4. *(10 min)* Sweep fetch-k (20/40/80) and top-k (4/6/8); find the metric plateau; record chosen budget and its added latency in `RETRIEVAL.md`.
5. *(5 min)* Re-run the Lab 1 F4/F5 probes end-to-end; confirm the identifier probe now retrieves the correct circular and the precision-collapse probe now ranks the right chunk first. Strike F4 and F5 off the poster. Commit `feat(retrieve): hybrid + reranker two-stage stack`.

**Expected output**
```
$ make eval-by-class
                       dense   hybrid   +rerank
natural_language        0.71    0.72     0.83
exact_identifier        0.24    0.79     0.81   <- F4 fixed by sparse
mixed                   0.48    0.66     0.78
arabic_paraphrase       0.69    0.70     0.82
fetch/keep sweep: plateau at fetch_k=40, top_k=6
rerank latency: +118 ms p50 (40 candidates, CPU)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Sparse branch returns nothing | Collection lacks `sparse` named vector | Rebuild with `make reindex-hybrid` |
| Fusion worse than dense alone | Weighted-sum on raw scores instead of RRF | Use `Fusion.RRF` (rank-based) |
| Rerank very slow (seconds) | Reranking the whole corpus, not the shortlist | Rerank only stage-1 candidates (≤ fetch_k) |
| Arabic pairs score low after rerank | English-only reranker | Use `bge-reranker-v2-m3` (multilingual) |
| Identifier still missed | Sparse tokenization dropped the "44/2025" token | Check normalisation didn't strip the identifier |

**Instructor notes.** The per-class table (step 2) is the emotional core: the exact_identifier row leaping from 0.24 to 0.79 is *the* argument for hybrid, and it is invisible in any aggregate number. Let one pair report aggregate-only first, then reveal the class breakdown — the pedagogy is "aggregates lie." Fast finishers: try reranking with a smaller fetch-k and watch a known-relevant chunk fall out of reach — the fetch-k/reranker coupling made concrete.

## Mini Exercises

**Quiz (5 questions)**
1. Why can't a better embedding model fix F4? → the query needs lexical (exact-token) matching, which dense vectors blur by design.
2. Why RRF instead of weighted-sum fusion? → RRF combines ranks, avoiding the incomparable-score-scale problem, with no per-corpus tuning.
3. What makes a cross-encoder more accurate but more expensive than a bi-encoder? → it reads query and document together, so it can't be precomputed and must run per candidate.
4. Why "fetch 40, keep 6"? → retrieval is cheap (be generous for recall), generation is expensive (be strict for cost); the reranker bridges them.
5. True/False: an aggregate nDCG of 0.75 means the retriever is healthy. → **False** — it can hide an identifier class collapsed to 0.24.

**Debugging exercise.** Given a query class where hybrid and rerank both show *zero* lift over dense, decide whether the stage is failing or simply unnecessary for that class — and how you'd tell the difference (inspect whether the right chunk was in fetch-k at all).

**Code-review exercise.** Review a retrieval PR that reranks all 4,812 chunks per query, fuses dense+sparse by adding raw scores, and reports one aggregate recall number. Name the latency, correctness, and diagnostic defect in each.

**Discussion questions.**
- Your corpus has almost no identifiers and all natural-language queries. Is hybrid retrieval worth its added complexity? What evidence settles it?
- Reranking adds 120 ms per query. For a synchronous assistant with a 2 s SLA, when is that worth it — and when would you make reranking optional per query?

## Case Study — The Circular Nobody Could Find

**Scenario.** A regulator's internal assistant, built on a well-tuned dense retriever, fails a whole category of queries: staff searching by circular number ("ما نص التعميم 44/2025؟") get *a* circular back, almost never the right one. Aggregate recall@10 is a healthy 0.86 — but the identifier-query class, 30% of real traffic, sits at 0.23.

**Business context.** Compliance staff search by circular number as their primary workflow; a wrong circular in a compliance answer is a regulatory exposure. The team nearly rebuilt the embedding model before measuring by class.

**Technical challenge.** Lift the identifier class from 0.23 to ≥ 0.80 without harming the natural-language class, and prove the fix is lexical, not semantic.

**Constraints.** Bilingual identifiers (Arabic and Western digits in circular numbers); a 2 s latency SLA that a full-corpus reranker would blow; the natural-language class must not regress.

**Solution approach (facilitate, don't lecture).** Add bge-m3 sparse vectors and RRF fusion — the identifier class jumps immediately because sparse scoring weights the rare "44/2025" token that dense blurred; verify the natural-language class is unchanged (fusion doesn't hurt it). Add the cross-encoder reranker on a 40-candidate shortlist for precision, staying inside the SLA. Report the whole thing *by class* so leadership sees the identifier fix explicitly rather than an aggregate that never revealed the problem.

**Discussion questions.**
1. Why did the team almost fix the wrong thing (the embedder), and what metric discipline would have prevented it?
2. Would query rewriting (M7) be an alternative fix for identifiers, or is sparse retrieval structurally the right tool here?
3. How do you keep bilingual identifiers matchable through normalisation without stripping the identifier itself?
4. Design the launch gate that requires per-class metrics, not aggregates.

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| nDCG@6 (identifier class) | Retrieval quality | ≥ 0.80 (dense-only ~0.24) | per-class eval |
| nDCG@6 (overall) | Retrieval quality | ≥ 0.78 | per-class eval |
| Hybrid beats dense-only | Retrieval quality | ≥ +0.10 nDCG on identifier + mixed | comparison |
| End-to-end retrieve latency p95 | Performance | ≤ 200 ms (fetch 40, rerank 6) | timing |
| Access-control preserved | Security | 0 leaks through fusion path | filter test |
| Per-class reporting present | Diagnosis | all 4 classes reported separately | review |

**Example benchmark table (filled during lab):**

| Configuration | NL | identifier | mixed | AR paraphrase | p95 latency |
|---|---|---|---|---|---|
| dense-only (M3) | 0.71 | 0.24 | 0.48 | 0.69 | 34 ms |
| + hybrid (RRF) | 0.72 | 0.79 | 0.66 | 0.70 | 58 ms |
| + reranker | 0.83 | 0.81 | 0.78 | 0.82 | 176 ms |

## Required Visuals and Training Assets

### Diagrams
1. **Two-stage retrieval architecture** — *Purpose:* the module anchor, coloured into the course diagram. *Elements:* query → dense branch + sparse branch → RRF fusion → 40 candidates → cross-encoder reranker → top-6 → context builder. *Style:* funnel narrowing left to right; "M4 retires F4, F5" stamped. *Designer note:* show fetch-40/keep-6 as an explicit narrowing.
2. **Dense vs sparse complementarity** — *Elements:* a Venn-style panel: queries dense wins (paraphrase), queries sparse wins (identifiers), overlap where both work. *Style:* two-circle diagram with example queries placed.
3. **RRF fusion mechanics** — *Elements:* two ranked lists, per-document reciprocal-rank contributions, fused ranking. *Style:* worked-example table with arrows.
4. **Bi-encoder vs cross-encoder** — *Elements:* bi-encoder (separate encoders, precomputable) vs cross-encoder (joint encoding, per-pair) with a cost/accuracy caption. *Style:* side-by-side architecture sketch.

### Images (screenshots)
1. **Per-class nDCG table terminal** — *why:* the aggregates-lie lesson; *content:* identifier row leaping with hybrid.
2. **Qdrant point with dense + sparse named vectors** — *why:* verify hybrid schema; *content:* a point showing both vectors.
3. **Rerank score reordering** — *why:* makes F5 fix visible; *content:* a chunk moving from rank 9 to rank 1 after reranking.
4. **fetch-k/top-k plateau plot** — *why:* budget tuning; *content:* nDCG vs fetch-k flattening.

### Simulations
1. **Aggregate mask** — *Setup:* report only aggregate recall while the identifier class is collapsed. *Expected:* healthy-looking number, broken workflow. *Learning objective:* per-class metrics are non-negotiable.
2. **Fetch-k starvation** — *Setup:* fetch-k=5 with the relevant chunk at rank 12. *Expected:* reranker can't recover it. *Learning objective:* the reranker only sees what stage 1 fetched.

### Interactive Activities
- **Which stage fixes it? (15 min):** 12 failing query cards sorted onto "needs sparse / needs rerank / needs both / already fine" — defended with retrieved-chunk evidence.
- **Budget auction (10 min):** given a latency budget, groups "spend" it on fetch-k and reranking and justify the allocation against per-class targets.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `retrieval_labels.jsonl` (class-tagged) | Course-authored | JSONL | 200 queries × 4 classes | per-class eval |
| Hybrid `dalil` collection | Participant output | Qdrant points (dense+sparse) | 4,812 | the retriever under test |
| `probes/failure_gallery.jsonl` | Reused from Lab 1 | JSONL | 12 | F4/F5 retirement check |

### Demo Requirements
- **Instructor demo:** the identifier query failing under dense, fixed live by enabling the sparse branch; then a rank-9 chunk promoted to rank 1 by the reranker.
- **Student demo:** two pairs present their per-class improvement table and chosen budget.
- **Expected outputs:** every pair has the two-stage stack with per-class metrics, F4 and F5 removed from the poster.

---

# Module 5 — Context Construction and Citation Grounding

## Module Overview

**Purpose.** Perfect retrieval is wasted if the generation stage ignores the evidence, blends contradictory chunks, or answers confidently when nothing was retrieved. This module owns the online path's business end: assembling retrieved chunks into a token-budgeted context, prompting the LLM to answer *only* from that context with verifiable citations, and — the hardest discipline — refusing to answer when the evidence is insufficient. It retires **F6 (context abuse)** and, together with M6, **F7 (ungrounded fluency)**.

**Business relevance.** In regulated Saudi sectors an answer without a citation is unusable and an *invented* answer is a liability. The difference between a demo and a deployable assistant is almost entirely here: does every claim point to a source the human can check, and does the system say "I don't have that information" instead of confabulating? Under PDPL and audit regimes, the citation *is* the compliance artefact, and the refusal is the safety control. Context discipline is also the main cost lever (Module 1): a lean, well-ordered context is cheaper *and* more accurate than a stuffed one.

**Industry use cases.**
- A bank's compliance assistant must cite the exact circular and clause for every answer and refuse anything outside its corpus — both are hard requirements, not features.
- A government-services chatbot must prove which document produced each sentence for audit and must never freelance a policy it can't ground.
- An internal HR assistant must filter context by the asking employee's access rights so an answer never quotes a document the user isn't cleared to see.

**Expected competencies.** After this module a participant can build a token-budgeted context assembler that orders chunks to beat lost-in-the-middle, write a grounded prompt that emits verifiable citations, implement an insufficient-evidence refusal, and enforce access control at context-construction time.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Assemble a token-budgeted context and order chunks against lost-in-the-middle | LO5 |
| 5.2 | Write a grounded prompt that answers only from provided evidence | LO5 |
| 5.3 | Emit verifiable, chunk-level citations in the answer | LO5, LO4 |
| 5.4 | Implement insufficient-evidence refusal behaviour | LO6 |
| 5.5 | Enforce access-control filtering in context construction | LO5 |

## Technical Content

### 1. The context budget

The LLM's context window is finite and every token costs money and latency (Module 1: generation dominates both). Context construction is a *budgeting* problem:

- **Token accounting:** count tokens with the model's tokenizer, reserve room for the system prompt, the question, and the answer, and fit as many high-value chunks as the remainder allows — typically the top 4–6 from M4, not all 40.
- **More context is not better:** past a point, extra chunks *lower* accuracy (dilution, contradiction) while raising cost — the "stuff 16 chunks" anti-pattern from Module 1, now measured. The reranker (M4) exists precisely so the few chunks that fit are the right ones.
- **Deduplication:** overlapping chunks (from M2 overlap) can repeat the same clause; collapse near-duplicates so the budget isn't spent twice on one fact.

### 2. Ordering and lost-in-the-middle

LLMs attend unevenly across a long context: evidence at the **start and end** is used more reliably than evidence buried in the **middle** — the "lost-in-the-middle" effect. Two consequences for assembly:

- **Order by relevance to the extremes:** place the highest-reranked chunk first (or first-and-last), weaker chunks in the middle. A monotonic best-to-worst top-to-bottom ordering often underperforms a "best at the edges" arrangement for long contexts.
- **Keep contexts short enough that the middle barely exists** — the cheapest defence against lost-in-the-middle is a 4-chunk context where there is no deep middle to lose.

This is F6's mechanism: a right answer retrieved but placed mid-context and ignored. The fix is ordering plus brevity, both governed by the assembler.

### 3. Grounded prompting

The prompt must make the model a *reader*, not a *recaller* (Module 1's core move, realised):

- **Instruction:** "Answer using ONLY the numbered sources below. If the sources do not contain the answer, say you don't have that information. Cite the source number for every claim."
- **Numbered sources:** each chunk is presented with a stable label `[1]`, `[2]`, … and its provenance (doc title, section, effective date) so the model can cite it and the human can verify it.
- **Temperature 0** for every answer that will be evaluated — otherwise metric deltas (M6) are noise (Module 1 delivery-plan rule).
- **No outside knowledge:** the prompt explicitly forbids drawing on parametric knowledge; this is what converts "what does the model know?" into "what do the sources say?" and is the structural defence against F7.

### 4. Citations that can be verified

A citation is only worth anything if a human can follow it to the exact evidence:

- **Chunk-level, not document-level:** cite the specific chunk (and thus section/page) that supports a claim, not just the document — auditors check clauses, not whole PDFs.
- **Machine-verifiable:** the answer emits citation markers (`[2]`) that map to `source_id → {doc_id, section, page, effective_date}`; a post-check can confirm every cited source was actually in the context (catching a model that invents a citation number).
- **Faithfulness precondition:** citations enable M6's faithfulness metric — you cannot measure whether a claim is grounded if you don't know which source was supposed to ground it.

### 5. Refusal and access control

Two safety behaviours live here:

- **Insufficient-evidence refusal (F7):** when retrieval returns nothing relevant (or reranker scores are all below a threshold), the system must refuse — "I don't have information on that in the current policies" — never freestyle. This is a *design decision surfaced as a threshold*: below score τ, refuse; the threshold is tuned against the golden set (M6) to balance helpful answers against confident-wrong ones.
- **Access-control filtering:** the M3/M4 payload filter (department, sensitivity) is applied at retrieval, but context construction is the last line of defence — assert that every chunk entering the prompt is one the asking user may see, and log the check. A user must never receive an answer grounded in a document they aren't cleared for, even by accident.

### 6. Common mistakes & production considerations

1. Stuffing all retrieved chunks into the prompt — dilution, contradiction, and 4× the cost for worse answers.
2. No refusal path — the system confabulates on unanswerable questions (the most dangerous failure, because it's fluent).
3. Document-level citations that auditors can't verify at clause level.
4. Trusting citation markers without checking the cited source was actually in the context.
5. Non-zero temperature on evaluated answers — noisy, irreproducible quality.
6. Applying access control only at retrieval and not re-asserting it at context construction — a defence-in-depth gap.
7. Ignoring contradicting chunks (superseded vs current policy both retrieved) — the prompt must be told to prefer current sources or surface the conflict.

Production: context caching for repeated system prompts; streaming answers with citations resolved at the end; a "conflict detected" response mode when current and superseded sources disagree; and logging the retrieved+cited source IDs per answer (Module 1's audit trail) so every answer is reconstructable.

## Code Examples

### Token-budgeted context assembler with edge-ordering and dedup

```python
# src/dalil/generate/context.py
"""Assemble a token-budgeted, access-checked, edge-ordered context.
Short + well-ordered beats stuffed: this is where F6 is retired and cost is controlled."""
from dataclasses import dataclass
import tiktoken

from dalil.retrieve.rerank import ScoredChunk

_ENC = tiktoken.get_encoding("cl100k_base")


@dataclass
class Source:
    label: int
    text: str
    doc_id: str
    section: str
    effective_date: str


def _tokens(text: str) -> int:
    return len(_ENC.encode(text))


def build_context(chunks: list[ScoredChunk], *, permitted_departments: set[str],
                  token_budget: int = 1800) -> list[Source]:
    # Defence-in-depth: re-assert access control at the LAST gate before the LLM
    chunks = [c for c in chunks if c.payload["department"] in permitted_departments]

    seen, ordered, used = set(), [], 0
    for c in chunks:                              # chunks arrive best-first from rerank
        key = c.text[:120]
        if key in seen:                           # collapse overlap-duplicated clauses
            continue
        cost = _tokens(c.text)
        if used + cost > token_budget:            # stop at the budget, don't stuff
            break
        seen.add(key)
        ordered.append(c)
        used += cost

    # Lost-in-the-middle defence: best chunk first, second-best LAST, rest in middle
    if len(ordered) > 2:
        ordered = [ordered[0], *ordered[2:], ordered[1]]

    return [Source(label=i + 1, text=c.text, doc_id=c.payload["doc_id"],
                   section=c.payload.get("section_title", ""),
                   effective_date=c.payload.get("effective_date", ""))
            for i, c in enumerate(ordered)]
```

### Grounded prompt with citations and refusal

```python
# src/dalil/generate/answer.py
"""Grounded generation: answer ONLY from numbered sources, cite every claim,
refuse when evidence is insufficient. Temperature 0 for reproducible evaluation."""
import json
from openai import OpenAI

from dalil.generate.context import Source

_llm = OpenAI(base_url="http://gateway:8080/v1")

_SYSTEM = """You are Dalil, an enterprise knowledge assistant.
Rules:
1. Answer using ONLY the numbered sources provided. Use no outside knowledge.
2. Cite the source number in square brackets after every claim, e.g. [2].
3. If the sources do not contain the answer, reply exactly:
   "I don't have information on that in the current policies."
4. If sources conflict, prefer the one with the most recent effective_date and say so.
Answer in the language of the question."""

REFUSAL = "I don't have information on that in the current policies."


def _render_sources(sources: list[Source]) -> str:
    return "\n\n".join(
        f"[{s.label}] (section: {s.section}; effective {s.effective_date})\n{s.text}"
        for s in sources)


def answer(query: str, sources: list[Source], *, min_sources: int = 1) -> dict:
    if len(sources) < min_sources:               # nothing retrieved => refuse (F7)
        return {"answer": REFUSAL, "citations": [], "refused": True}

    resp = _llm.chat.completions.create(
        model="course-llm", temperature=0,       # reproducible for M6 evaluation
        messages=[{"role": "system", "content": _SYSTEM},
                  {"role": "user",
                   "content": f"Sources:\n{_render_sources(sources)}\n\nQuestion: {query}"}],
    )
    text = resp.choices[0].message.content.strip()
    cited = _extract_citations(text, sources)     # verify cited nums were in context
    return {"answer": text, "citations": cited, "refused": text == REFUSAL}


def _extract_citations(text: str, sources: list[Source]) -> list[dict]:
    import re
    valid = {s.label: s for s in sources}
    out = []
    for n in {int(m) for m in re.findall(r"\[(\d+)\]", text)}:
        if n in valid:                            # invented citation numbers dropped
            s = valid[n]
            out.append({"source": n, "doc_id": s.doc_id, "section": s.section})
    return out
```

### The end-to-end grounded pipeline

```python
# src/dalil/generate/pipeline.py
"""Wire retrieve -> rerank -> context -> grounded answer. The shape the capstone ships."""
from qdrant_client import QdrantClient

from dalil.retrieve.rerank import retrieve_and_rerank
from dalil.retrieve.hybrid import COLLECTION
from dalil.generate.context import build_context
from dalil.generate.answer import answer, REFUSAL


def ask_dalil(query: str, *, department: str, refuse_below: float = 0.3) -> dict:
    qdr = QdrantClient(url="http://localhost:6333")
    from qdrant_client.models import Filter, FieldCondition, MatchValue
    dept_filter = Filter(should=[
        FieldCondition(key="department", match=MatchValue(value=department)),
        FieldCondition(key="department", match=MatchValue(value="public"))])

    scored = retrieve_and_rerank(qdr, query, query_filter=dept_filter,
                                 fetch_k=40, top_k=6)
    # Refuse if even the best chunk is weakly relevant (F7 threshold, tuned in M6)
    if not scored or scored[0].rerank_score < refuse_below:
        return {"answer": REFUSAL, "citations": [], "refused": True}

    sources = build_context(scored,
                            permitted_departments={department, "public"},
                            token_budget=1800)
    return answer(query, sources)
```

## Hands-on Lab 5 — Grounded, Cited Generation

| | |
|---|---|
| **Objective** | Build the context assembler and grounded prompt; emit verifiable citations; implement insufficient-evidence refusal; prove F6/F7 retreat on the probe set |
| **Duration** | 50 minutes |
| **Setup** | Lab 4 solution; `git checkout lab5-start`; `pip install tiktoken openai`; gateway key from instructor; model pinned, temperature 0 |

**Instructions & tasks**

1. *(10 min)* Implement `build_context` with token budgeting and dedup; verify a 6-chunk shortlist fits the 1800-token budget and near-duplicate chunks are collapsed.
2. *(10 min)* Implement the grounded prompt + `answer`; run five answerable probes; confirm every answer carries `[n]` citations that resolve to real sources.
3. *(10 min)* Implement refusal: run the two unanswerable probes from the failure gallery; confirm the system refuses instead of confabulating (the F7 fix). Tune `refuse_below` so answerable questions aren't wrongly refused.
4. *(10 min)* Add citation verification: inject a prompt that tempts an invented `[9]`; confirm `_extract_citations` drops it. Add the lost-in-the-middle edge-ordering and re-check a long-context probe.
5. *(5 min)* Verify access control: an HR user's query must never produce an answer citing a finance-only chunk. Strike F6 and F7 off the poster. Commit `feat(generate): grounded cited answers with refusal`.

**Expected output**
```
$ make ask Q="How much is the housing allowance for grade 9?"
Grade 9 housing allowance is 3,200 SAR per month [1].
  citations: [{source:1, doc_id:allowance_table_2025, section:"Housing"}]
$ make ask Q="What is the policy on remote work from Mars?"
I don't have information on that in the current policies.   (refused: true)
probe set: 10/10 answerable cited, 2/2 unanswerable refused, 0 invented citations
access-control: 0/40 cross-department citations  PASS
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Model answers unanswerable questions | Refusal instruction weak / threshold too low | Strengthen system rule 3; raise `refuse_below` |
| Answers with no citations | Prompt not enforcing citation | Add explicit "cite after every claim"; few-shot example |
| Invented citation `[9]` present | No post-check | `_extract_citations` drops labels not in context |
| Right answer ignored mid-context | Lost-in-the-middle | Apply edge-ordering; shorten context |
| Finance chunk cited to HR user | Access re-check missing | Filter by `permitted_departments` in `build_context` |

**Instructor notes.** The refusal demo (step 3) produces the strongest reaction of Day 3 — run the "remote work from Mars" probe on the projector and let the class feel the difference between fluent-wrong and honest-refuse. The invented-citation drop (step 4) teaches that trust is verified, not assumed. Fast finishers: add a conflict-detection response when a superseded and a current policy are both retrieved — a direct bridge to M6's staleness red-team.

## Mini Exercises

**Quiz (5 questions)**
1. Why does stuffing 16 chunks into the prompt often *lower* accuracy? → dilution, contradiction, and lost-in-the-middle; the relevant signal is buried.
2. Where in a long context is evidence most reliably used? → the start and end (lost-in-the-middle effect).
3. Why chunk-level rather than document-level citations? → auditors verify clauses; a whole-PDF citation isn't checkable.
4. What is the structural defence against F7 (ungrounded fluency)? → a grounded prompt forbidding outside knowledge plus an insufficient-evidence refusal.
5. True/False: temperature can be left at default for evaluated answers. → **False** — non-zero temperature makes M6 metric deltas noise.

**Debugging exercise.** Given an answer that cites `[3]` for a claim not present in source 3, decide whether the fix is prompt engineering, citation verification, or reranking — and why verification catches the symptom while the root cause may be a weak chunk in context.

**Code-review exercise.** Review a generation PR that: passes all 40 retrieved chunks to the LLM, has no refusal path, uses temperature 0.7, and cites document filenames only. Name the cost, safety, reproducibility, and auditability defect in each.

**Discussion questions.**
- Your refusal threshold trades helpfulness against confident-wrong answers. Who owns setting it — engineering or risk — and what data decides the number?
- A superseded and a current policy are both retrieved and disagree. Should Dalil answer from the current one silently, surface both, or refuse? Argue for a default and its exceptions.

## Case Study — The Assistant That Would Not Say "I Don't Know"

**Scenario.** A government-services assistant, retrieval fully tuned, still fails audit: on questions outside its corpus it invents plausible policy, and its answers cite whole documents rather than clauses, so auditors can't verify anything. In a sample of 200 answers, 12% were confident-wrong on unanswerable questions and 0% had clause-level citations.

**Business context.** The audit unit requires that every answer be traceable to a specific clause and that the assistant *demonstrably* refuse outside its knowledge — a fluent wrong answer to a citizen is worse than no answer.

**Technical challenge.** Drive confident-wrong answers on unanswerable questions to near zero and make 100% of answers clause-cited, without harming the answerable-question quality already achieved.

**Constraints.** Bilingual answers must cite the same clause regardless of query language; refusal must not be so aggressive that it refuses answerable questions; every answer's retrieved and cited source IDs must be logged for audit reconstruction.

**Solution approach (facilitate, don't lecture).** A grounded prompt forbidding outside knowledge; an evidence-strength refusal threshold tuned on the golden set so answerable recall stays high while unanswerable questions are refused; chunk-level citations carrying section and effective-date; a post-generation check that every cited source was actually in context; and per-answer logging of retrieved+cited IDs as the audit artefact. The refusal threshold becomes a governance dial owned jointly by engineering and the audit unit.

**Discussion questions.**
1. What sample of unanswerable questions do you need to set the refusal threshold responsibly, and who authors them?
2. Is a document-level citation ever acceptable, or is clause-level always required in a regulated setting?
3. How do you prove to auditors that the refusal behaviour holds, not just that it exists?
4. Where does the access-control re-check belong, and why is retrieval-only enforcement insufficient?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Citation coverage | Grounding | 100% of non-refusal answers cite ≥ 1 source | citation parser |
| Invented-citation rate | Grounding | 0% (all cited nums in context) | verification check |
| Refusal correctness (unanswerable) | Safety | ≥ 95% refused | unanswerable probe set |
| False-refusal rate (answerable) | Helpfulness | ≤ 5% | answerable probe set |
| Context token budget respected | Cost | ≤ 1,800 tokens/context | tokenizer count |
| Access-control at generation | Security | 0 cross-department citations | filter test |

**Example benchmark table (filled during lab):**

| Configuration | citation coverage | invented citations | unanswerable refused | answerable false-refusals |
|---|---|---|---|---|
| Naive (all chunks, no refusal) | 0% | n/a | 0/12 | 0% |
| Grounded + cited + refusal | 100% | 0% | 12/12 | 3% |

## Required Visuals and Training Assets

### Diagrams
1. **Context-construction pipeline** — *Purpose:* the online path's business end, coloured into the anchor. *Elements:* reranked chunks → access re-check → dedup → token budget → edge-ordering → numbered sources → grounded prompt → cited answer / refusal. *Style:* left-to-right with "M5 retires F6, F7" stamped.
2. **Lost-in-the-middle curve** — *Elements:* answer accuracy vs position of the relevant chunk in context, dipping in the middle; the edge-ordering fix overlaid. *Style:* U-shaped line chart with annotation.
3. **Citation resolution** — *Elements:* answer `[2]` → source label 2 → {doc_id, section, page, effective_date} → original document; an invented `[9]` shown being dropped. *Style:* trace diagram with a verification gate.
4. **Refusal decision** — *Elements:* best rerank score vs threshold τ → answer or refuse; τ tuned against golden set. *Style:* simple threshold flowchart feeding the F7 motif.

### Images (screenshots)
1. **A cited answer** — *why:* target state; *content:* answer with `[1][2]` resolving to sections and dates.
2. **A correct refusal** — *why:* the safety behaviour; *content:* "I don't have information…" on an unanswerable probe.
3. **Invented-citation dropped** — *why:* verification works; *content:* log line showing `[9]` discarded as not-in-context.
4. **Access-control block at generation** — *why:* defence in depth; *content:* a finance chunk excluded for an HR user before prompting.

### Simulations
1. **Stuff-the-context** — *Setup:* pass all 40 chunks vs top-6. *Expected:* accuracy down, cost 5×, lost-in-the-middle visible. *Learning objective:* short beats stuffed.
2. **Refusal threshold sweep** — *Setup:* vary τ from 0.1 to 0.6. *Expected:* trade between false-refusals and confident-wrong answers. *Learning objective:* refusal is a tunable governance dial.

### Interactive Activities
- **Prompt surgery (15 min):** groups iterate the grounded prompt against three adversarial questions and measure citation coverage and refusal correctness after each edit.
- **Citation audit (10 min):** pairs act as auditors, following each other's citations to the exact clause and flagging any that don't verify.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `probes/answerable.jsonl` + `probes/unanswerable.jsonl` | Course-authored (AR/EN) | JSONL | 10 + 12 | citation + refusal checks |
| Reranked shortlists | Participant output | in-memory | — | context assembly input |
| Access-control probe set | Course-authored | JSONL | 40 | cross-department leak test |

### Demo Requirements
- **Instructor demo:** the same corpus answering a real question with clause citations, then refusing an unanswerable one, then dropping an invented citation — the trust chain built live.
- **Student demo:** two pairs present a cited answer and a correct refusal with their tuned threshold.
- **Expected outputs:** every pair has grounded, cited, refusal-capable generation; F6 and F7 removed from the poster.

---

# Module 6 — RAG Evaluation Frameworks

## Module Overview

**Purpose.** Everything so far has been *built*; this module makes it *measurable*. Without evaluation, "our RAG is good" is an opinion and every change is a gamble. This module establishes a systematic evaluation harness — faithfulness, answer relevancy, context precision/recall, and answer correctness — over a curated golden set, wires a regression gate so quality cannot silently degrade, and provides the measurement that finally *proves* **F7 (ungrounded fluency)** is caught and **F8 (staleness)** is defeated.

**Business relevance.** In regulated Saudi sectors, "the model works" must be an evidence pack, not a claim: a faithfulness score, a regression baseline, and a golden set are exactly what model-governance reviews (SAMA-style, PDPL-aligned) ask for. Evaluation is also what lets a team ship *frequently* instead of *fearfully* — a green regression gate means a chunking tweak or a prompt change can merge with confidence. The engineer who can attach numbers to answer quality is the one trusted to change the system.

**Industry use cases.**
- A bank's compliance assistant must demonstrate, with a faithfulness metric, that answers are grounded in cited circulars before each release — the eval report *is* the sign-off.
- A telecom's support RAG gates every prompt change on a golden-set regression run; a change that drops faithfulness below baseline cannot merge.
- A government assistant is red-teamed on unanswerable, stale, and conflicting questions, with refusal correctness measured, before it faces citizens.

**Expected competencies.** After this module a participant can build a golden Q&A set, run the RAGAS metric suite, interpret each metric and its LLM-as-judge caveats, store a baseline, wire a regression gate into CI, and red-team the system for hallucination and staleness with measured outcomes.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Build a golden Q&A set with ground-truth answers and contexts | LO4 |
| 6.2 | Run and interpret the RAGAS metric suite | LO4 |
| 6.3 | Explain LLM-as-judge caveats and control for them | LO4, LO6 |
| 6.4 | Store a baseline and wire a regression gate | LO4, LO6 |
| 6.5 | Red-team for hallucination and staleness with measured outcomes | LO6 |

## Technical Content

### 1. Why RAG needs its own evaluation

RAG has two failure surfaces — *retrieval* (did we find the right evidence?) and *generation* (did we answer faithfully from it?) — and a single accuracy number conflates them. Good evaluation *decomposes* the pipeline, so a regression can be traced to the stage that caused it:

- A drop in **context recall** points at retrieval (M3/M4).
- A drop in **faithfulness** with good context points at generation (M5).
- A drop in **answer correctness** with good faithfulness and recall points at the golden set or the question itself.

This decomposition is the whole reason to prefer a metric *suite* over a single score: it tells you *where* to look.

### 2. The RAGAS metric suite

RAGAS provides reference-free and reference-based metrics computed per question over `(question, retrieved_contexts, answer, ground_truth)`:

| Metric | Question it answers | Stage it indicts | Needs ground truth? |
|---|---|---|---|
| **Faithfulness** | Is every claim in the answer supported by the retrieved context? | generation (F7) | no |
| **Answer relevancy** | Does the answer actually address the question? | generation | no |
| **Context precision** | Are the retrieved chunks relevant (and ranked well)? | retrieval/rerank (F5) | no |
| **Context recall** | Did retrieval fetch the evidence needed for the ground truth? | retrieval (F3/F4) | yes |
| **Answer correctness** | Is the answer factually right vs the reference? | end-to-end | yes |

**Faithfulness is the headline metric for this course**: it directly measures ungrounded fluency (F7). An answer that is fluent, relevant, and *unfaithful* is exactly the dangerous failure Module 1 named — faithfulness puts a number on it.

### 3. Building the golden set

The golden set is the measuring instrument; a bad instrument makes all measurements meaningless:

- **Coverage:** span query classes (natural-language, identifier, mixed, Arabic), difficulty, and — critically — **unanswerable and stale** questions, so refusal and freshness are measured, not assumed.
- **Ground truth:** each answerable question has a reference answer and the doc/chunk that contains it (reuse M3's `retrieval_labels`). Unanswerable questions have ground-truth = refusal.
- **Bilingual:** Arabic and English questions with the same rigour — Arabic evaluation is first-class.
- **Size and stability:** the course uses **120 questions** (`golden_qa_v1.jsonl`); big enough to be stable, small enough to run in CI. Freeze it; adding questions is a deliberate, versioned act (like the fraud course's golden files).

### 4. LLM-as-judge caveats

RAGAS uses an LLM to judge faithfulness/relevancy — powerful but not free of pitfalls, which participants must control:

- **Non-determinism:** pin the judge model and temperature 0; otherwise scores wobble run-to-run and "improvement" is noise.
- **Judge bias:** LLM judges can favour verbose or confident answers; calibrate against a small human-labelled subset to confirm the judge agrees with people.
- **Cost and latency:** judging 120 questions × several metrics is many LLM calls; budget it, cache where possible, and keep the judge model fixed across releases so scores are comparable.
- **Not ground truth:** the judge is an estimator. Treat a 0.02 faithfulness delta as noise; treat a 0.10 drop as a real regression worth blocking on.

### 5. Regression gating and the anti-staleness drill

Evaluation only changes behaviour when it *gates*:

- **Baseline:** store the current metric vector (`baseline.json`); every change is measured against it.
- **Gate:** CI fails if faithfulness or context recall drops more than a tolerance (e.g., 0.03) below baseline — the M4 fraud course's regression-gate pattern, applied to RAG metrics.
- **Staleness (F8) drill:** on Day 4, corpus_v2 introduces updated documents that supersede v1 ones. The eval set includes questions whose *correct* answer changed. A system without lifecycle metadata (M2) and freshness filtering (M3/M5) answers from the stale document and *fails the correctness metric* — proving F8 was real and that the machinery built to defeat it works.
- **Red-team:** adversarial questions — unanswerable, stale, and internally-conflicting — with refusal correctness and freshness measured. This is where F7 and F8 get their final, numeric verdict.

### 6. Common mistakes & production considerations

1. A single accuracy number that can't localise a regression to a stage.
2. A tiny or unbalanced golden set — stable-looking scores that miss whole query classes.
3. Non-pinned judge model/temperature — metric deltas that are pure noise.
4. Treating faithfulness as optional because "the answers look good" — looking good is exactly F7.
5. No unanswerable/stale questions in the golden set — refusal and freshness never measured.
6. Regenerating the baseline casually "to make CI green" — the regression gate disabled (the fraud course's golden-file sin, recurring).

Production: continuous evaluation on a rolling sample of real (anonymised) queries; drift monitoring (faithfulness trending down signals corpus or model drift); human-in-the-loop review of low-faithfulness answers; and an eval report artefact attached to every release as governance evidence.

## Code Examples

### RAGAS evaluation harness

```python
# src/dalil/evaluation/ragas_harness.py
"""Run the RAGAS suite over the 120-question golden set. Pinned judge + temperature 0
=> comparable, gate-able scores. Faithfulness is the headline (F7) metric."""
import json
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (faithfulness, answer_relevancy,
                           context_precision, context_recall, answer_correctness)

from dalil.generate.pipeline import ask_dalil


def _build_eval_rows(golden_path: str) -> Dataset:
    rows = {"question": [], "answer": [], "contexts": [], "ground_truth": []}
    for line in open(golden_path, encoding="utf-8"):
        g = json.loads(line)
        result = ask_dalil(g["question"], department=g.get("department", "public"))
        rows["question"].append(g["question"])
        rows["answer"].append(result["answer"])
        rows["contexts"].append([c["text"] for c in result.get("contexts", [])])
        rows["ground_truth"].append(g["ground_truth"])   # refusal string if unanswerable
    return Dataset.from_dict(rows)


def run_evaluation(golden_path: str = "eval/golden_qa_v1.jsonl") -> dict:
    ds = _build_eval_rows(golden_path)
    report = evaluate(ds, metrics=[
        faithfulness, answer_relevancy,
        context_precision, context_recall, answer_correctness,
    ])                                            # judge model pinned via env/config
    scores = {k: round(float(v), 3) for k, v in report.items()}
    return scores
```

### Regression gate (wired into the Makefile / CI)

```python
# src/dalil/evaluation/gate.py
"""Fail the build if faithfulness or context recall regresses beyond tolerance.
This is what lets the team change the pipeline without fear."""
import json
import sys

TOLERANCE = 0.03
GATED = ("faithfulness", "context_recall")


def check_regression(current: dict, baseline_path: str = "eval/baseline.json") -> int:
    baseline = json.load(open(baseline_path))
    failures = []
    for metric in GATED:
        drop = baseline[metric] - current[metric]
        if drop > TOLERANCE:
            failures.append(f"{metric}: {current[metric]:.3f} "
                            f"(baseline {baseline[metric]:.3f}, -{drop:.3f})")
    if failures:
        print("REGRESSION GATE FAILED:")
        print("\n".join(f"  {f}" for f in failures))
        return 1
    print(f"Regression gate PASSED (tolerance {TOLERANCE})")
    return 0


if __name__ == "__main__":
    from dalil.evaluation.ragas_harness import run_evaluation
    scores = run_evaluation()
    json.dump(scores, open("eval/last_run.json", "w"), indent=2)
    sys.exit(check_regression(scores))
```

### Staleness red-team (the F8 verdict)

```python
# src/dalil/evaluation/staleness_redteam.py
"""Day-4 drill: corpus_v2 supersedes some v1 docs. Questions whose correct answer
CHANGED must now be answered from the current doc. Proves F8 is defeated (or not)."""
import json

from dalil.generate.pipeline import ask_dalil


def run_staleness_redteam(path: str = "eval/staleness_v2.jsonl") -> dict:
    total = correct_current = cited_superseded = 0
    for line in open(path, encoding="utf-8"):
        q = json.loads(line)                      # has current_answer + superseded_answer
        total += 1
        res = ask_dalil(q["question"], department=q.get("department", "public"))
        ans = res["answer"]
        if q["current_answer"] in ans:
            correct_current += 1
        if q["superseded_answer"] in ans:         # answered from the OLD doc == F8
            cited_superseded += 1
    return {
        "questions": total,
        "answered_current": round(correct_current / total, 3),
        "answered_stale": round(cited_superseded / total, 3),   # target: 0.0
    }
```

## Hands-on Lab 6 — Evaluation Harness and Baseline

| | |
|---|---|
| **Objective** | Run RAGAS over the 120-question golden set, store the baseline, wire a regression gate into CI, and run the staleness red-team — measuring F7 and F8 defeated |
| **Duration** | 50 minutes |
| **Setup** | Lab 5 solution; `git checkout lab6-start`; `pip install ragas datasets`; judge model pinned via `configs/eval.env`; temperature 0 |

**Instructions & tasks**

1. *(10 min)* Run `run_evaluation` over `golden_qa_v1.jsonl`; read the five metrics; identify which stage any weak metric indicts.
2. *(10 min)* Store `baseline.json`; deliberately break something (e.g., disable the reranker) and re-run; watch context precision and faithfulness drop — confirm the decomposition points at the right stage.
3. *(10 min)* Wire `gate.py` into the Makefile (`make eval-gate`) and the CI workflow; open a PR with a faithfulness-lowering prompt change and watch the gate block it.
4. *(10 min)* Run the staleness red-team against corpus_v2; confirm `answered_stale` is ~0 with lifecycle filtering on, then toggle filtering off and watch it spike — the F8 proof.
5. *(5 min)* Calibrate the judge: compare RAGAS faithfulness to 10 human labels; confirm agreement within tolerance. Strike F8 off the poster. Commit `feat(eval): RAGAS harness + regression gate + staleness redteam`.

**Expected output**
```
$ make eval
faithfulness 0.91  answer_relevancy 0.88  context_precision 0.84
context_recall 0.89  answer_correctness 0.82   (120 questions, judge pinned)
$ make eval-gate   (after disabling reranker)
REGRESSION GATE FAILED:
  faithfulness: 0.79 (baseline 0.91, -0.12)
  context_recall: 0.71 (baseline 0.89, -0.18)
staleness redteam: answered_current 0.96, answered_stale 0.01  (filtering ON)
                   answered_current 0.44, answered_stale 0.55  (filtering OFF)  <- F8
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Scores wobble run-to-run | Judge temperature not 0 / model not pinned | Pin model + temperature in `eval.env` |
| Faithfulness low but answers look right | Answer includes uncited outside knowledge | Tighten grounded prompt (M5); re-check |
| Context recall low, precision fine | Retrieval missing evidence | Revisit M3/M4 (recall@k, hybrid) |
| Gate never fails | Tolerance too loose / wrong baseline | Set tolerance 0.03; regenerate baseline deliberately |
| Staleness stays high with filtering on | `superseded_by` not set on v2 update | Re-ingest v2 with lifecycle metadata (M2) |

**Instructor notes.** The reranker-off regression (step 2) is the module's thesis: metrics *localise* the damage to a stage. The staleness toggle (step 4) is the course's climax — the same question answered correctly with filtering on and wrongly with it off, live, is the entire golden thread paying off. Emphasise the LLM-as-judge calibration: a metric you haven't checked against humans is a number you don't understand.

## Mini Exercises

**Quiz (5 questions)**
1. Which RAGAS metric directly measures F7 (ungrounded fluency)? → faithfulness.
2. Context recall dropped but faithfulness held — which stage regressed? → retrieval (M3/M4).
3. Why pin the judge model and temperature? → otherwise metric deltas are noise, not signal.
4. Why must the golden set include unanswerable questions? → to measure refusal correctness, not assume it.
5. True/False: a 0.02 faithfulness rise proves an improvement. → **False** — within judge noise; treat small deltas as noise.

**Debugging exercise.** Given an eval run where answer_correctness fell but faithfulness and context_recall are unchanged, decide whether the regression is in the system or in the golden set (a reference answer went stale after corpus_v2) — and how you'd tell.

**Code-review exercise.** Review an eval PR that: uses a single accuracy metric, has 15 English-only golden questions, runs the judge at temperature 0.7, and regenerates the baseline in the same commit as a prompt change. Name the localisation, coverage, noise, and governance defect in each.

**Discussion questions.**
- Your faithfulness is 0.91 but a risk officer wants 0.98. What does closing that gap cost (stricter refusal, smaller context, better rerank) and what does it trade away?
- The judge model itself gets upgraded. Why does that invalidate historical comparisons, and how do you handle the migration?

## Case Study — Proving the Assistant Is Safe Before It Faces Citizens

**Scenario.** A government digital-services team is ready to launch Dalil but cannot get sign-off: leadership asks "how do you *know* it doesn't make things up, and that it uses current policy?" The team has demos, not evidence. A structured evaluation is stood up in a week.

**Business context.** The assistant will answer citizens directly; a confident-wrong or stale-policy answer is a public-trust and compliance event. Sign-off requires an evidence pack a non-engineer risk officer can read.

**Technical challenge.** Produce a defensible evaluation showing faithfulness, correct refusal on unanswerable questions, and correct current-policy answers after a mid-cycle policy update — with a regression gate that keeps it true release-over-release.

**Constraints.** Bilingual golden set; pinned judge for comparability; the eval must run in CI in minutes; the policy-update (staleness) scenario must be part of the evidence, not a footnote.

**Solution approach (facilitate, don't lecture).** Build a 120-question bilingual golden set spanning classes plus unanswerable and stale questions; run RAGAS with a pinned judge and calibrate against human labels; store a baseline and gate CI on faithfulness and context recall; run the corpus_v2 staleness red-team and show `answered_stale ≈ 0` with lifecycle filtering; package the metric tables, the staleness result, and the refusal-correctness number into a one-page evidence pack the risk officer signs.

**Discussion questions.**
1. Which single metric would you put in front of leadership, and why faithfulness over accuracy?
2. How large and how balanced must the golden set be to be credible without being unrunnable in CI?
3. The staleness result depends on M2 metadata and M5 filtering — how do you demonstrate that dependency to non-engineers?
4. What is the ongoing evaluation cadence after launch, and what triggers a re-baseline?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Faithfulness | Grounding (F7) | ≥ 0.90 | RAGAS, pinned judge |
| Context recall | Retrieval | ≥ 0.88 | RAGAS (ground truth) |
| Context precision | Rerank quality | ≥ 0.82 | RAGAS |
| Answer correctness | End-to-end | ≥ 0.80 | RAGAS |
| Answered-stale rate (F8) | Freshness | ≤ 0.02 (filtering on) | staleness red-team |
| Regression gate present | Governance | CI fails on > 0.03 drop | gate run |

**Example benchmark table (filled during lab):**

| Configuration | faithfulness | context recall | context precision | answer correctness | answered-stale |
|---|---|---|---|---|---|
| Baseline (full stack) | 0.91 | 0.89 | 0.84 | 0.82 | 0.01 |
| Reranker disabled | 0.79 | 0.71 | 0.61 | 0.68 | 0.03 |
| Lifecycle filtering off | 0.88 | 0.86 | 0.82 | 0.59 | 0.55 |

## Required Visuals and Training Assets

### Diagrams
1. **RAGAS metric map** — *Purpose:* connect metrics to pipeline stages. *Elements:* the anchor pipeline with each metric pinned to the stage it indicts (context recall→retrieval, faithfulness→generation, etc.). *Style:* the course anchor diagram overlaid with metric badges; "M6 proves F7, F8 defeated" stamped.
2. **Evaluation loop with regression gate** — *Elements:* change → eval → compare to baseline → pass merges / fail blocks; artefact (report) emitted. *Style:* circular workflow with a gate turnstile.
3. **Staleness red-team before/after** — *Elements:* the same question answered from a superseded doc (filtering off) vs the current doc (filtering on); answered-stale bar dropping to ~0. *Style:* before/after split with the F8 sticker being removed.
4. **LLM-as-judge calibration** — *Elements:* RAGAS faithfulness vs human labels scatter, agreement band. *Style:* calibration scatter plot.

### Images (screenshots)
1. **RAGAS report terminal** — *why:* target state; *content:* the five metrics over 120 questions.
2. **Blocked PR on faithfulness regression** — *why:* the gate is real; *content:* CI check failing with the metric drop.
3. **Staleness toggle result** — *why:* the F8 proof; *content:* answered-stale 0.01 vs 0.55.
4. **Judge-calibration plot** — *why:* judges are estimators; *content:* human vs RAGAS agreement.

### Simulations
1. **Regression localisation** — *Setup:* break one stage at a time. *Expected:* the corresponding metric drops, others hold. *Learning objective:* metrics localise damage.
2. **Judge-noise flood** — *Setup:* run the judge at temperature 0.7. *Expected:* scores wobble ±0.05 across runs. *Learning objective:* pin the judge or measure noise.

### Interactive Activities
- **Golden-set authoring (15 min):** groups write five golden questions each (including one unanswerable, one stale) with ground truth, then critique coverage gaps.
- **"Signal or noise?" (10 min):** given pairs of eval runs, teams decide which deltas are real regressions and which are judge noise, and defend the threshold.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `golden_qa_v1.jsonl` | Course-curated (AR/EN) | JSONL | 120 Q&A pairs | RAGAS evaluation |
| `staleness_v2.jsonl` | Course-authored | JSONL | 25 changed-answer questions | F8 red-team |
| `eval/baseline.json` | Reference solution | JSON | 1 file | regression gate |
| `human_labels.jsonl` | Course-labelled subset | JSONL | 10 | judge calibration |

### Demo Requirements
- **Instructor demo:** a live regression — disable the reranker, run the gate, watch it block; then the staleness toggle answering the same question right and wrong.
- **Student demo:** two pairs present their metric tables and one localised regression they diagnosed.
- **Expected outputs:** every pair has a RAGAS baseline, a wired regression gate, and a staleness result; F8 removed from the poster (only advanced-pattern gains remain).

---

# Module 7 — Advanced Patterns: Multi-Hop and Agentic RAG

## Module Overview

**Purpose.** By Module 6 every failure class F1–F8 is retired and the linear pipeline — retrieve, rerank, ground, cite, refuse — is measurably good. But a whole class of *questions* still defeats it: those whose answer requires combining evidence from several documents ("does a grade-9 employee on secondment keep the housing allowance, and for how long?"), those phrased so poorly that a single retrieval misses, and those where the first retrieval is simply wrong and the system should *notice and retry*. This module adds the query-intelligence and control-flow patterns — **query rewriting, multi-query, decomposition, multi-hop retrieval, corrective/self-RAG, and routing** — that turn a static pipeline into a small, disciplined agent. Its governing rule: **add a loop only when a measured question class demands it**, never for architectural fashion.

**Business relevance.** The highest-value enterprise questions are rarely single-fact lookups; they are cross-policy, conditional, and comparative — exactly the ones a linear RAG cannot answer and exactly the ones that make an assistant indispensable rather than a search box. But each advanced pattern buys capability with latency, cost, and complexity, so the engineer who can *prove per query class* that decomposition earns its extra LLM calls is the one who ships intelligence without ambushing the latency budget. This module is also the on-ramp to SDA-AIE-311 (Agentic AI Systems Engineering): Dalil's corrective loop is a one-tool agent, and the same reasoning-plus-retrieval shape scales to the multi-tool agents of the next course.

**Industry use cases.**
- A compliance assistant answering "which of my three active circulars conflict on overtime, and which prevails?" — impossible without decomposition and multi-hop retrieval across documents.
- A benefits assistant handling conditional entitlement questions ("if X and Y, is Z allowed?") where each condition lives in a different policy — the answer is assembled across hops, not found in one chunk.
- A high-stakes assistant that must self-correct: when the first retrieval is off-topic, a corrective-RAG grader triggers a query rewrite and re-retrieval instead of grounding on junk.

**Expected competencies.** After this module a participant can implement multi-query rewriting and question decomposition, build a two-hop retrieval path, add a corrective-RAG self-check that grades retrieval and retries, route queries to the cheapest sufficient path, and measure the accuracy gain against the extra cost per query class — deciding *with numbers* when the complexity pays.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Implement query rewriting and multi-query expansion to recover weak-phrasing recall | LO3, LO5 |
| 7.2 | Decompose a multi-hop question and retrieve across hops | LO1, LO3 |
| 7.3 | Add a corrective/self-RAG loop that grades retrieval and retries | LO1, LO6 |
| 7.4 | Route queries to the cheapest sufficient retrieval path | LO1, LO5 |
| 7.5 | Quantify accuracy gain versus added latency/cost per query class | LO4, LO5 |

## Technical Content

### 1. Where the linear pipeline still fails

The failure taxonomy F1–F8 describes ways a *single* retrieve-then-generate pass goes wrong. Advanced patterns address a different axis — questions the single pass is *structurally* unable to answer well:

- **Multi-hop:** the answer requires facts from two or more documents combined ("secondment rules" × "housing-allowance eligibility"). One retrieval finds one, not the join.
- **Under-specified phrasing:** the user's wording is far from the document's; a single embedding of a vague question misses, where two or three rephrasings would hit.
- **Wrong first retrieval:** occasionally retrieval simply fails, and a linear pipeline grounds confidently on off-topic chunks. A human would notice and search again; a static pipeline won't.
- **Mixed intent:** some queries are chit-chat or out-of-scope; running the full expensive stack on them is waste, and a router should short-circuit.

These are not new failure *classes* to strike off the poster — they are capabilities *added on top* of a system that already scores well, and each must justify its cost.

### 2. Query rewriting and multi-query expansion

The cheapest advanced pattern: fix the *query* before retrieval rather than the retrieval itself.

- **Rewriting:** an LLM rewrites a vague or conversational question into a retrieval-optimised one ("what about mars?" → "remote-work policy for off-site locations"), and resolves pronouns/context in a multi-turn session.
- **Multi-query:** generate 3–4 paraphrases of the question, retrieve for each, and fuse the results (RRF again). This widens recall for under-specified questions at the cost of N retrievals — cheap, because retrieval is cheap (Module 1's asymmetry, reused).
- **HyDE (hypothetical document embeddings):** embed a *hypothetical answer* the LLM drafts, not the question — sometimes closer to the target passage in vector space. Use with care; measure before adopting.

The discipline: multi-query helps the *under-specified* class and does nothing for the *identifier* class (M4 already fixed that). Break the gain out by class or you will pay for expansion where it does not help.

### 3. Decomposition and multi-hop retrieval

For genuinely compositional questions, rewrite is not enough — the question must be *broken into sub-questions*, each retrieved and answered, then composed:

- **Decompose:** an LLM splits "does a seconded grade-9 keep housing allowance and for how long?" into (a) "is a seconded employee eligible for housing allowance?" and (b) "what is the duration limit for retained allowances on secondment?".
- **Retrieve per hop:** each sub-question runs the full M4 two-stage retrieval independently; a later hop may use the answer of an earlier one to form its query (true multi-hop).
- **Compose:** the grounded-generation stage (M5) receives the union of hop evidence and answers with citations spanning documents.

The cost is real — decomposition is one extra LLM call plus one retrieval per hop — so it must be *gated*: only questions a classifier (or the router, §5) flags as multi-hop pay for it. Single-hop questions take the linear path.

### 4. Corrective and self-RAG

The most agent-like pattern: let the system *judge its own retrieval* and act on the judgement.

- **Retrieval grading:** after retrieval, an LLM (or a lightweight classifier) grades whether the retrieved context is actually relevant to the question. This is the same faithfulness instinct from M6, moved *inside* the online loop.
- **Corrective action:** if the grade is "irrelevant", don't ground on junk — rewrite the query and re-retrieve, widen the search (raise `ef`/fetch-k), or fall back to refusal. If "relevant", proceed to generation.
- **Self-RAG / reflection:** the model reflects on its draft answer against the evidence and revises or refuses. This is a controlled, bounded loop — **cap the iterations** (usually 1–2), or an unlucky query loops until the budget dies.

Corrective RAG is where "RAG" becomes "a one-tool agent": retrieval is the tool, the grader is the reasoning, and the retry is the control flow. It is the conceptual bridge to SDA-AIE-311.

### 5. Routing: pay only for the intelligence a query needs

Not every question deserves the full apparatus. A **router** (an LLM classifier or rules) sends each query down the cheapest sufficient path:

| Query type | Path | Cost |
|---|---|---|
| Out-of-scope / chit-chat | refuse or canned reply, no retrieval | ~0 |
| Simple single-fact | linear retrieve → rerank → answer (M2–M5) | 1× |
| Under-specified | multi-query expansion → linear | ~1.5× |
| Multi-hop / conditional | decompose → per-hop retrieval → compose | 2–4× |
| Low-confidence retrieval | corrective loop (grade → rewrite → retry) | 1–2× |

Routing is what keeps advanced patterns economically honest: the expensive paths run only when the query justifies them, so the *average* query stays cheap while the *hard* query gets the machinery it needs. The router's own error modes (mis-routing a multi-hop question to the linear path) become a thing you measure.

### 6. Common mistakes & production considerations

1. Adding decomposition/corrective loops everywhere "to be safe" — multiplying latency and cost on questions that never needed them.
2. Unbounded self-RAG loops — no iteration cap, so a hard query burns the whole budget retrying.
3. Multi-query without fusion — retrieving four lists and concatenating (duplicates, no rank discipline) instead of RRF.
4. Measuring advanced patterns in aggregate — the multi-hop gain is invisible unless you break out the multi-hop query class.
5. A router with no fallback — a mis-classified query gets the wrong path and no recovery.
6. Ignoring that every extra LLM call is a new latency, cost, and *failure* surface — advanced patterns need the same telemetry and evaluation (M6) as the base pipeline.

Production: cache decomposition and rewrite outputs for repeated queries; bound every loop with a hard iteration and wall-clock cap; trace each hop and grade decision (the observability that SDA-AIE-312 formalises); evaluate the advanced paths against the golden set's multi-hop subset with the *same* regression gate; and expose a per-query "path taken" field so operators can see how often the expensive paths fire.

## Code Examples

### Multi-query expansion with RRF fusion

```python
# src/dalil/advanced/multiquery.py
"""Generate paraphrases of an under-specified query, retrieve for each, fuse with RRF.
Widens recall on vague questions; does nothing for identifiers (measure by class)."""
from collections import defaultdict
from openai import OpenAI

from dalil.retrieve.rerank import retrieve_and_rerank

_llm = OpenAI(base_url="http://gateway:8080/v1")


def rewrite_queries(query: str, n: int = 3) -> list[str]:
    resp = _llm.chat.completions.create(
        model="course-llm", temperature=0,
        messages=[{"role": "system",
                   "content": f"Rewrite the user question into {n} diverse, "
                              "retrieval-optimised paraphrases, one per line. "
                              "Preserve any identifiers (circular numbers, form codes) exactly."},
                  {"role": "user", "content": query}])
    lines = [q.strip("-• ").strip() for q in resp.choices[0].message.content.splitlines()]
    return [query] + [q for q in lines if q][:n]        # always keep the original


def multiquery_retrieve(qdr, query, *, query_filter=None, fetch_k=40, top_k=6):
    variants = rewrite_queries(query)
    rrf = defaultdict(float)
    store = {}
    for v in variants:                                  # each variant: full 2-stage
        for rank, chunk in enumerate(
                retrieve_and_rerank(qdr, v, query_filter=query_filter,
                                    fetch_k=fetch_k, top_k=top_k)):
            rrf[chunk.doc_id + chunk.text[:40]] += 1.0 / (60 + rank)   # RRF, k=60
            store[chunk.doc_id + chunk.text[:40]] = chunk
    ranked = sorted(rrf, key=rrf.get, reverse=True)
    return [store[k] for k in ranked[:top_k]]
```

### Question decomposition and multi-hop retrieval

```python
# src/dalil/advanced/multihop.py
"""Decompose a compositional question into sub-questions, retrieve per hop,
and compose. Gated: only multi-hop-classified queries pay this cost."""
import json
from openai import OpenAI

from dalil.retrieve.rerank import retrieve_and_rerank

_llm = OpenAI(base_url="http://gateway:8080/v1")


def decompose(question: str) -> list[str]:
    resp = _llm.chat.completions.create(
        model="course-llm", temperature=0,
        messages=[{"role": "system",
                   "content": "If the question needs facts from multiple policies, "
                              "return a JSON list of 2-3 atomic sub-questions. "
                              "If it is a single lookup, return a one-item list."},
                  {"role": "user", "content": question}])
    try:
        subs = json.loads(resp.choices[0].message.content)
        return subs if isinstance(subs, list) and subs else [question]
    except json.JSONDecodeError:
        return [question]                               # fail safe to single-hop


def multihop_retrieve(qdr, question, *, query_filter=None, top_k=4):
    """Retrieve evidence for each hop; union it for the compose step (M5)."""
    evidence, seen = [], set()
    for sub in decompose(question):
        for chunk in retrieve_and_rerank(qdr, sub, query_filter=query_filter,
                                         fetch_k=40, top_k=top_k):
            key = chunk.doc_id + chunk.text[:40]
            if key not in seen:                         # de-dup across hops
                seen.add(key)
                evidence.append(chunk)
    return evidence
```

### Corrective RAG: grade retrieval, retry, then answer

```python
# src/dalil/advanced/corrective.py
"""Self-check loop: grade whether retrieved context is relevant; if not, rewrite
and retry ONCE; else fall back to refusal. Bounded iterations by design."""
from openai import OpenAI

from dalil.retrieve.rerank import retrieve_and_rerank
from dalil.advanced.multiquery import rewrite_queries
from dalil.generate.context import build_context
from dalil.generate.answer import answer, REFUSAL

_llm = OpenAI(base_url="http://gateway:8080/v1")


def grade_relevance(question: str, chunks) -> bool:
    if not chunks:
        return False
    joined = "\n---\n".join(c.text[:400] for c in chunks[:4])
    resp = _llm.chat.completions.create(
        model="course-llm", temperature=0,
        messages=[{"role": "system",
                   "content": "Does the CONTEXT contain information to answer the "
                              "QUESTION? Reply only 'yes' or 'no'."},
                  {"role": "user", "content": f"QUESTION: {question}\nCONTEXT:\n{joined}"}])
    return resp.choices[0].message.content.strip().lower().startswith("y")


def corrective_answer(qdr, question, *, department, query_filter=None, max_retries=1):
    chunks = retrieve_and_rerank(qdr, question, query_filter=query_filter, top_k=6)
    tries = 0
    while not grade_relevance(question, chunks) and tries < max_retries:
        tries += 1                                       # bounded: never loops forever
        rewritten = rewrite_queries(question, n=1)[-1]   # one corrective rewrite
        chunks = retrieve_and_rerank(qdr, rewritten, query_filter=query_filter, top_k=6)
    if not grade_relevance(question, chunks):            # still junk -> refuse, don't guess
        return {"answer": REFUSAL, "citations": [], "refused": True, "retries": tries}
    sources = build_context(chunks, permitted_departments={department, "public"})
    out = answer(question, sources)
    out["retries"] = tries
    return out
```

## Hands-on Lab 7 — Multi-Hop and Query Intelligence

| | |
|---|---|
| **Objective** | Add multi-query rewriting, a two-hop decomposition path, and a corrective-RAG loop to Dalil; route each query to the cheapest sufficient path; measure the accuracy gain on the multi-hop subset against the added latency/cost |
| **Duration** | 50 minutes |
| **Setup** | Lab 6 solution; `git checkout lab7-start`; gateway key; model pinned, temperature 0; `eval/golden_qa_v1.jsonl` includes a `multi_hop` query class and `probes/multihop.jsonl` |

**Instructions & tasks**

1. *(10 min)* Implement `multiquery_retrieve` with RRF; run the under-specified probe subset linear vs multi-query; confirm recall lifts on vague questions and is flat on identifiers (measure by class).
2. *(15 min)* Implement `decompose` + `multihop_retrieve`; run the 10 multi-hop probes; confirm answers now cite evidence from *two* documents where the linear path cited one and answered partially.
3. *(10 min)* Add the corrective loop (`grade_relevance` + one retry); force a bad first retrieval on a probe and confirm the retry recovers it; verify the iteration cap holds (no infinite loop) and that unrecoverable queries refuse.
4. *(10 min)* Add a simple router (rules or LLM classifier) sending each query to linear / multi-query / multi-hop / corrective; log the path taken per query and the added latency; run the full golden set through the router and re-run the M6 regression gate.
5. *(5 min)* Record the accuracy gain and cost per class in `EVALUATION.md`; confirm the router keeps average latency near the linear baseline while lifting the multi-hop class. Commit `feat(advanced): multi-query, multi-hop, corrective RAG + router`.

**Expected output**
```
$ make eval-advanced
                     linear   +multiquery  +multihop   path
single_fact           0.86       0.86         0.86      linear
under_specified        0.61       0.79         0.80      multiquery
multi_hop              0.34       0.41         0.82      multihop   <- the win
corrective recovery: 7/10 forced-bad-retrievals recovered on retry (cap=1)
router: avg latency 1.9s (linear 1.7s); multi-hop paths fired on 12% of queries
regression gate: PASSED (faithfulness 0.91, context_recall 0.90)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Multi-query duplicates results | Concatenating lists, not fusing | Use RRF across variant result lists |
| Decomposition returns nonsense JSON | Model not constrained | Parse defensively; fall back to single-hop on error |
| Corrective loop never terminates | No iteration cap | Enforce `max_retries`; refuse after the cap |
| Multi-hop no better than linear | Sub-questions too similar to original | Prompt for *atomic, distinct* sub-questions; inspect them |
| Router sends everything to multi-hop | Classifier over-triggers | Tighten the router prompt; measure path distribution |
| Latency balloons | Advanced paths firing on easy queries | Check the router; easy queries must stay linear |

**Instructor notes.** The multi-hop row (0.34 → 0.82) is the module's payoff — put it beside the flat single_fact row so the class sees *both* the win and the discipline: the pattern helps only the class that needs it. The corrective-loop cap is the safety lesson — demo an uncapped loop burning ten retries on one query, then the capped version. Fast finishers: add HyDE to the under-specified path and measure whether it beats multi-query — often a wash, which teaches "measure before adopting the fashionable pattern." This is also the explicit hand-off to SDA-AIE-311: Dalil's corrective loop is a one-tool agent.

## Mini Exercises

**Quiz (5 questions)**
1. Why does multi-query help the under-specified class but not the identifier class? → identifiers were already fixed by sparse retrieval (M4); vague phrasing benefits from paraphrase recall.
2. What makes a question genuinely multi-hop? → its answer requires combining facts from two or more documents that no single retrieval returns together.
3. Why must every self-RAG loop have an iteration cap? → otherwise a hard query retries until the latency/cost budget is exhausted.
4. What does a router buy you? → the expensive paths run only when the query needs them, keeping average cost near the linear baseline.
5. True/False: adding decomposition to every query is a safe default. → **False** — it multiplies cost/latency on the single-hop majority that never needed it.

**Debugging exercise.** Given a multi-hop question that the decomposition splits into two *near-identical* sub-questions, decide whether the fix is a better decomposition prompt, a distinctness check on the sub-questions, or falling back to multi-query — and why identical sub-questions produce no multi-hop gain.

**Code-review exercise.** Review an advanced-RAG PR that: runs decomposition + corrective loop on *every* query with no router, has no iteration cap, and reports one aggregate accuracy number. Name the cost, safety, and diagnostic defect in each, and map each to the production considerations above.

**Discussion questions.**
- Your multi-hop class is only 8% of traffic but the highest-value 8%. How do you justify the added complexity to a latency-conscious product owner — and what number settles it?
- Corrective RAG makes Dalil a one-tool agent. What changes when you add a *second* tool (a calculator, a live API)? Sketch the step from this module to SDA-AIE-311.

## Case Study — The Conditional-Entitlement Question That Needed Two Documents

**Scenario.** A Saudi government HR assistant, fully tuned through Module 6, still fails a category leadership cares about most: conditional entitlement questions like "if an employee is seconded to another ministry, do they keep their housing allowance, and for how long?" The eligibility rule lives in the secondment policy; the duration limit lives in the allowances circular. The linear pipeline retrieves *one* of the two and answers half the question confidently — a partial answer that reads as complete.

**Business context.** These conditional questions are the ones employees most need help with (the simple ones they can look up themselves), so failing them undermines the assistant's core value. A confidently *partial* answer is worse than a refusal because the user doesn't know a condition was missed.

**Technical challenge.** Lift the multi-hop query class from 0.34 to ≥ 0.80 answer-correctness without inflating average latency, and without regressing the single-hop majority that already works.

**Constraints.** A 2 s p95 SLA for the average query; bilingual decomposition (the sub-questions must be generated in the query's language); the multi-hop path must not fire on single-hop questions; every hop's evidence must remain individually citable so the composed answer cites both documents.

**Solution approach (facilitate, don't lecture).** Add a router that classifies conditional/comparative questions to a decomposition path; decompose into atomic sub-questions, retrieve each with the full M4 stack, union the evidence, and compose one grounded answer citing both documents; keep single-hop questions on the fast linear path so average latency barely moves; wrap the whole thing in a corrective grader so a mis-decomposed question re-tries once rather than answering on partial evidence; and evaluate the multi-hop subset under the same M6 regression gate so the gain is proven and protected.

**Discussion questions.**
1. How do you detect a multi-hop question reliably enough to route it without over-triggering on simple ones?
2. When a composed answer cites two documents that subtly disagree, does Dalil surface the conflict, prefer the more recent, or refuse? (link back to M5's conflict handling)
3. What is the honest way to report the multi-hop improvement — aggregate correctness, or the multi-hop-class number — and why?
4. Where does this pattern stop being "RAG" and become "an agent," and what does that imply for the next course?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Multi-hop class answer-correctness | Capability | ≥ 0.80 (linear ~0.34) | golden multi-hop subset |
| Under-specified class recall lift | Capability | ≥ +0.10 over linear | per-class eval |
| Single-hop class (no regression) | Discipline | within 0.02 of linear | per-class eval |
| Corrective recovery rate | Robustness | ≥ 60% of bad retrievals recovered | forced-failure probes |
| Average latency vs linear | Cost | ≤ +0.3 s p95 with routing | timing |
| Regression gate (M6) still green | Governance | faithfulness/recall within tolerance | gate run |

**Example benchmark table (filled during lab):**

| Configuration | single_fact | under_specified | multi_hop | avg p95 latency |
|---|---|---|---|---|
| Linear (M5/M6) | 0.86 | 0.61 | 0.34 | 1.7 s |
| + multi-query | 0.86 | 0.79 | 0.41 | 2.1 s |
| + multi-hop | 0.86 | 0.80 | 0.82 | 2.6 s (path only) |
| + router (blended) | 0.86 | 0.80 | 0.82 | 1.9 s avg |

## Required Visuals and Training Assets

### Diagrams
1. **Advanced-pattern control flow** — *Purpose:* show the pipeline becoming an agent. *Elements:* query → router → {linear | multi-query | decompose→multi-hop | corrective loop} → compose → grounded answer; the corrective retry arrow drawn as a bounded loop. *Style:* the course anchor diagram with a router node and loop-back edge; "M7 adds capability beyond F1–F8" stamped. *Designer note:* this is the diagram that morphs into SDA-AIE-311's multi-tool agent.
2. **Multi-hop decomposition** — *Elements:* one conditional question split into two sub-questions, each retrieving a different document, evidence unioned into one cited answer. *Style:* tree from question to sub-questions to two source documents.
3. **Corrective-RAG loop** — *Elements:* retrieve → grade → (relevant: answer / irrelevant: rewrite→retry, capped) → refuse-on-give-up. *Style:* flowchart with an explicit iteration counter.
4. **Cost-vs-capability by path** — *Elements:* bar chart of accuracy gain and latency cost per path (linear, multi-query, multi-hop, corrective). *Style:* paired bars making the "pay only for what the query needs" point.

### Images (screenshots)
1. **Multi-hop answer citing two documents** — *why:* the capability made visible; *content:* a composed answer with `[1]` from the secondment policy and `[2]` from the allowances circular.
2. **Per-class gain table terminal** — *why:* the discipline lesson; *content:* multi_hop row leaping while single_fact stays flat.
3. **Router path-distribution log** — *why:* proves cost control; *content:* percentage of queries taking each path.
4. **Corrective retry trace** — *why:* the self-correction; *content:* grade=no → rewrite → grade=yes → answer, with the cap shown.

### Simulations
1. **Unbounded loop** — *Setup:* remove the iteration cap on the corrective loop and feed an unanswerable question. *Expected:* the loop retries until the budget dies. *Learning objective:* every agentic loop needs a bound.
2. **Pattern-everywhere cost** — *Setup:* route *all* queries through decomposition + corrective. *Expected:* 3× average latency and cost for near-zero gain on the single-hop majority. *Learning objective:* routing is what makes intelligence affordable.

### Interactive Activities
- **Route this query (15 min):** 15 query cards sorted onto linear / multi-query / multi-hop / corrective / refuse, defended by predicted cost and expected gain, then checked against the router's actual choices.
- **Decompose-off (10 min):** groups hand-decompose three conditional questions, compare to the LLM's decomposition, and identify where atomic-and-distinct sub-questions matter most.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `probes/multihop.jsonl` | Course-authored (AR/EN) | JSONL | 10 conditional/comparative questions | multi-hop capability |
| `golden_qa_v1.jsonl` (multi_hop class) | Course-curated | JSONL | subset of 120 | per-class evaluation |
| `probes/under_specified.jsonl` | Course-authored | JSONL | 10 vague questions | multi-query lift |
| `probes/forced_bad_retrieval.jsonl` | Course-authored | JSONL | 10 | corrective-recovery test |

### Demo Requirements
- **Instructor demo:** the conditional-entitlement question answered partially by the linear path, then fully — citing both documents — by the multi-hop path; then an uncapped corrective loop burning retries vs the capped version.
- **Student demo:** two pairs present their multi-hop gain table and their router's path distribution.
- **Expected outputs:** every pair has multi-query, multi-hop, and a bounded corrective loop behind a router, with per-class gains recorded in `EVALUATION.md` and the M6 gate still green.

---

# Final Capstone Project

## Title: Dalil — A Production-Grade, Evaluated Enterprise RAG Assistant

## Project Scenario

You are the RAG engineer for **"Dalil" (دليل)**, the enterprise knowledge assistant of a fictional Saudi organisation. Over four days you built every stage — ingestion, indexing, hybrid retrieval, grounded generation, evaluation, and advanced patterns — as Labs 1–7. The capstone is not new code from scratch; it is the **integration of those stages into one deployable, evaluated system** over the *full* Dalil corpus, plus your own extension, plus the evidence that proves — with numbers — that Dalil is faithful, cited, fresh, and defensibly not over-engineered. On Day 4 the corpus is upgraded to **corpus_v2** (updated and superseding documents), so your system must demonstrably prefer current policy: the staleness drill is part of the grade, not a footnote.

The deliverable is a repository that *proves its own quality*: a working assistant, an evaluation harness with a regression gate, and an `EVALUATION.md` a non-engineer risk officer can read and sign. This is the exact system shape you will extend with agents and tools in **SDA-AIE-311**.

## Requirements

**Mandatory (maps to grading rubric):**

1. **End-to-end pipeline (LO1, LO2):** ingestion (format dispatch + Arabic OCR + structure-aware chunking + lifecycle metadata) → bge-m3 embedding → Qdrant collection with payload filters → hybrid (dense+sparse RRF) retrieval → cross-encoder reranking → token-budgeted context → grounded, cited, refusal-capable generation. All seven stages integrated and runnable via `make`.
2. **Bilingual quality (LO2, LO3):** the system answers Arabic and English questions with equal rigour; Arabic normalisation applied identically at ingest and query; recall@10 on the Arabic subset ≥ 0.85.
3. **Retrieval stack (LO3):** hybrid + reranker measured *by query class*; the identifier class ≥ 0.80 nDCG@6; per-class reporting present (no aggregate-only numbers).
4. **Grounding & safety (LO5, LO6):** 100% of non-refusal answers carry verifiable chunk-level citations; 0% invented citations; ≥ 95% correct refusal on unanswerable questions; access-control filter enforced at retrieval *and* re-asserted at context construction with 0 cross-department leaks.
5. **Evaluation & regression gate (LO4, LO6):** RAGAS over the 120-question golden set with a pinned judge; faithfulness ≥ 0.90, context recall ≥ 0.88; a stored baseline and a CI regression gate that blocks a > 0.03 drop.
6. **Freshness / anti-staleness (LO6):** run the corpus_v2 staleness red-team; `answered_stale` ≤ 0.02 with lifecycle filtering on; demonstrate the same question answered correctly (filtering on) and wrongly (filtering off).
7. **Repo quality (LO1):** `README.md` runbook (a stranger runs `make demo` in 10 minutes), `EVALUATION.md` with the five course benchmark tables filled from *your* runs, and `DECISIONS.md` with five engineering decisions and rationale.

**One extension (choose at least one):**
- Multi-hop path: decomposition + per-hop retrieval, with the multi-hop golden subset ≥ 0.80 and a router keeping single-hop latency flat.
- Corrective RAG: a bounded self-check loop that grades retrieval and retries once, with a measured recovery rate on forced-bad-retrieval probes.
- Conflict handling: detect and surface a superseded-vs-current policy disagreement rather than silently choosing.
- pgvector variant: reproduce the retrieval stack on pgvector and compare recall/latency to Qdrant with a short trade-off memo.
- Thin FastAPI service: `POST /v1/ask` returning answer + citations + path-taken, with trace-id and model-version headers (reusing SDA-AIE-113 practices).

## Architecture (target state)

```
OFFLINE:  corpus_v1/v2 → parser registry → OCR(text-less) → normalise → structure-aware
          chunk → lifecycle metadata → bge-m3 embed → Qdrant (dense+sparse, payload indexes)

ONLINE:   query → [router] → hybrid retrieve (RRF) → rerank (bge-reranker) → access re-check
          → token-budgeted edge-ordered context → grounded LLM (temp 0) → answer + citations
          → (refuse if evidence < τ)                     └─ telemetry: retrieved+cited IDs, path

EVAL:     golden_qa_v1 (120, AR/EN) → RAGAS (pinned judge) → baseline.json → regression gate (CI)
          corpus_v2 → staleness red-team → answered_stale ≈ 0
```

## Deliverables

1. Git repository URL (public or instructor-shared) with full history and the `lab1..lab7` checkpoint tags visible.
2. `make demo` runs the full assistant over corpus_v2 locally (Qdrant container + gateway) and answers a live probe set.
3. `EVALUATION.md` with the five benchmark tables (ingestion coverage, recall@k, per-class nDCG, grounding/refusal, RAGAS+staleness) filled from your own runs.
4. `README.md` runbook + `DECISIONS.md` (five decisions: e.g., embedding-model choice, chunking strategy, refusal threshold, fetch-k/top-k budget, quantization).
5. 6-minute demo: clone-to-running via `make demo`, one Arabic + one English answer with citations, one correct refusal, the staleness toggle live, and a walk of the RAGAS report + regression gate.

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: Labs 1–2 integrated — corpus ingested, chunk-quality stats pass | End Day 1 | parse coverage ≥ 98%, mid-sentence < 8% |
| M-B: retrieval stack live (Labs 3–4) | End Day 2 | recall@10 ≥ 0.88, identifier class ≥ 0.80, per-class report |
| M-C: grounded + evaluated (Labs 5–6) | End Day 3 | citations 100%, faithfulness ≥ 0.90, gate wired |
| M-D: advanced + corpus_v2 staleness (Lab 7 + extension) | Day 4 H3 | multi-hop/corrective extension + answered_stale ≤ 0.02 |
| M-E: demo + submission | Day 4 H5 | rubric scoring, repo-first |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Ingestion & chunk quality | 12 | ≥ 98% coverage, tables whole, OCR CER ≤ 5%, full lifecycle metadata | Minor gaps (one format weak, CER 5–8%) | Silent coverage loss, flattened tables, no metadata |
| Retrieval quality (hybrid + rerank) | 18 | recall@10 ≥ 0.88, identifier ≥ 0.80, per-class reporting, AR ≥ 0.85 | Aggregate good but one class weak or AR < 0.85 | Dense-only, identifier class collapsed, aggregate-only |
| Grounding, citations & refusal | 18 | 100% cited, 0 invented, ≥ 95% refusal, access re-check clean | Citations mostly right; refusal 85–95% or 1–2 leaks | No refusal path, doc-level or invented citations, leaks |
| Evaluation & regression gate | 20 | RAGAS pinned, faithfulness ≥ 0.90, baseline + CI gate blocks drops | Metrics present but gate partial or judge unpinned | Single accuracy number, no gate, unpinned judge |
| Anti-staleness (corpus_v2) | 12 | answered_stale ≤ 0.02, toggle demonstrated live | Filtering works but drill thin | Stale answers served, no lifecycle filtering |
| Advanced extension | 10 | Extension measured, gated, no regression to base classes | Works but cost/latency not measured | Bolted on everywhere, no router, no numbers |
| Repo, demo & decisions | 10 | `make demo` cold-runs; EVALUATION/DECISIONS show trade-off literacy | Demo works, rationale thin | Cannot run own repo cold |

**Pass ≥ 70. Distinction ≥ 90.** The extension adds up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the evidence first* — the `EVALUATION.md` tables, the CI regression-gate history, the per-class reporting — demo second. The course's thesis is that numbers, not demos, prove a RAG system.
- Anti-pattern flags that cap a criterion at 70%: aggregate-only retrieval metrics hiding a collapsed class; regenerating the RAGAS baseline in the same commit as a quality change; a refusal path that refuses everything (gaming the unanswerable metric while tanking helpfulness); citations that don't resolve to real chunks.
- Verify one claim live: hand the participant a fresh unanswerable question and a fresh identifier question and watch Dalil refuse the first and retrieve the right circular for the second.
- The staleness toggle is the highest-signal live check — a participant who can explain *why* filtering off re-introduces F8 understands the whole golden thread.

## Bonus Tasks (for early finishers / distinction seekers)

1. Binary quantization + rescoring: measure the recall delta and memory saving at the full corpus, and defend the trade.
2. HyDE on the under-specified path: measure whether it beats multi-query, and report the honest (often null) result.
3. Continuous-eval harness: run RAGAS over a rolling sample and plot faithfulness drift across the four days' commits.
4. Bilingual conflict case: author a stale-vs-current Arabic policy pair and show Dalil surfacing the conflict with both citations.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** Which failure class can no amount of prompt engineering fix in a purely parametric LLM? → staleness (knowledge cutoff).
**Q2.** A client needs per-department answer visibility. RAG or fine-tune, and why? → RAG; weights cannot enforce per-user access.
**Q3.** Which pipeline stage dominates per-query cost? → generation — input tokens (context size).
**Q4.** Why "fetch 40, keep 6"? → retrieval is cheap (be generous for recall); generation is expensive (be strict for cost); the reranker bridges them.
**Q5.** Why OCR only text-less pages rather than every page? → OCR is slow and lossy; digital text is already perfect and cheaper.
**Q6.** Why must Arabic normalisation run at both ingest and query time? → otherwise indexed text and queries diverge and stop matching (F3).
**Q7.** What is the root-cause fix for a chunk that starts mid-clause — smaller chunks, more overlap, or structure-aware splitting? → structure-aware splitting (overlap is a band-aid).
**Q8.** Why does an English-only embedding model cause a semantic miss on a bilingual corpus? → Arabic queries and English passages land far apart in its vector space even when they mean the same thing.
**Q9.** When are cosine and dot-product equivalent? → when vectors are L2-normalised.
**Q10.** Which HNSW parameter do you tune per-query to buy recall without rebuilding? → `ef` (search).
**Q11.** Why can't a better embedding model fix an exact-identifier miss ("Circular 44/2025")? → the query needs lexical matching, which dense vectors blur by design; use sparse/hybrid.
**Q12.** Why RRF instead of weighted-sum fusion of dense and sparse scores? → RRF combines ranks, avoiding the incomparable-score-scale problem, with no per-corpus tuning.
**Q13.** What makes a cross-encoder more accurate but more expensive than a bi-encoder? → it reads query and document together, so it can't be precomputed and must run per candidate.
**Q14.** Where in a long context is evidence most reliably used? → the start and end (lost-in-the-middle effect).
**Q15.** What is the structural defence against ungrounded fluency? → a grounded prompt forbidding outside knowledge, plus an insufficient-evidence refusal.
**Q16.** Which RAGAS metric directly measures ungrounded fluency? → faithfulness.
**Q17.** Context recall dropped but faithfulness held — which stage regressed? → retrieval (embedding/hybrid).
**Q18.** Why pin the judge model and temperature in evaluation? → otherwise metric deltas are judge noise, not signal.
**Q19.** Why must every self-RAG / corrective loop have an iteration cap? → otherwise a hard query retries until the latency/cost budget is exhausted.
**Q20.** What does a query router buy you? → the expensive paths (multi-hop, corrective) run only when a query needs them, keeping average cost near the linear baseline.

## Practical Assessments

**PA-1 — Retrieval clinic (25 min, Day 2 H5):** Given three broken retrievers (an English-only embedder on Arabic queries, a dense-only retriever failing identifier queries, and a filter-starved search returning nothing), diagnose each from the metrics and per-class report, and fix it. Scored on: correct diagnosis from evidence (40%), fixes verified against the labelled set (40%), per-class reporting used not aggregates (20%).

**PA-2 — Hallucination & staleness triage (25 min, Day 3 H5):** Given a transcript of Dalil answering unanswerable, stale, and conflicting questions, classify each failure, name the stage that owns the fix (M2 metadata / M3 recall / M4 hybrid / M5 refusal / M6 gate), and write the one-line fix. Scored against the model triage: correctness of classification (50%), stage attribution (30%), governance reasoning — refusal threshold ownership (20%).

**PA-3:** Capstone (rubric above) — 40% of course grade. Labs completion + PA-1/PA-2 — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (7 labs) | 30% | checkpoint commits + expected outputs + poster failure-stickers removed |
| PA-1 + PA-2 | 20% | diagnosis notes + verified fixes + triage |
| Quiz | 10% | 10-question selection |
| Capstone | 40% | rubric, evidence-first (EVALUATION.md + gate history) |

Badge issuance (RAG badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical golden-set answers or copied EVALUATION tables across repos are checked).

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone the course org repo; push checkpoint tags (`lab1-start` … `lab7-start`, plus `-solution` tags) and verify each `git checkout labN-start` lands on a runnable state.
- [ ] Build and cache the model bundle: `BAAI/bge-m3`, `BAAI/bge-reranker-v2-m3`, `all-MiniLM-L6-v2` (contrast), the `policy-mirage` LoRA, and the pinned judge model — classroom bandwidth must never gate a lab.
- [ ] Regenerate `eval/baseline.json` and `eval/golden_qa_v1.jsonl` against the pinned judge + embedding versions; confirm the RAGAS harness and regression gate run green end-to-end.
- [ ] Stage both corpora: `corpus_v1/` (300 docs) and the Day-4 `corpus_v2/` superseding set; verify `ocr_gold/`, `retrieval_labels.jsonl`, `staleness_v2.jsonl`, and all `probes/*.jsonl` are present.
- [ ] Dry-run all 7 labs on a clean machine **and** on the Codespaces devcontainer with a shared Qdrant; time the overrun-prone labs (Lab 2 parsing, Lab 4 reranker download).
- [ ] Print the A2 wall poster (RAG reference architecture with F1–F8 sticker pins) and the desk cards (failure-taxonomy trading cards, RAG-vs-fine-tune scorecard).
- [ ] Provision the LLM gateway with per-participant keys and spend caps; pin model + temperature 0; verify a burst of eval calls stays within rate limits.
- [ ] Confirm classroom network allows the gateway, Qdrant, and HF mirror — or pre-pull everything into the local registry / `HF_HOME`.

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + git + a code editor (VS Code + Python + Docker extensions recommended).
- [ ] Docker Desktop (WSL2 on Windows) or Colima; verify `docker run hello-world` and `docker compose up qdrant`.
- [ ] `pip install qdrant-client sentence-transformers FlagEmbedding pymupdf python-docx openpyxl trafilatura pytesseract pdf2image python-Levenshtein tiktoken openai ragas datasets`
- [ ] Tesseract with the Arabic language pack (`tesseract --list-langs` shows `ara`) — provided in the course image for offline install.
- [ ] Gateway key from the instructor loaded into `configs/settings.env`; confirm `make doctor` prints ✓ for Qdrant, models, Tesseract, and the gateway.
- [ ] Clone the course repo and run `make doctor` (validates all of the above and prints ✓/✗ per component).

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| Qdrant container not up / port 6333 clash | High | `docker compose ps`; check `QDRANT_URL`; first-hour floater support |
| bge-m3 / reranker downloading mid-lab | High | Pre-download into `HF_HOME=/course/models`; verify with `make doctor` |
| Arabic OCR CER stuck high / renders as boxes | High | `--psm 4`, verify `ara` pack, raise DPI to 400; inspect via the notebook not the shell |
| Non-stable point IDs double the collection on re-upsert | Medium | Hash `doc_id:chunk_idx` for idempotent upserts |
| Arabic recall near zero | Medium | Confirm bge-m3 (not MiniLM) and `normalise_arabic` in the *query* path |
| Reranking the whole corpus (seconds of latency) | Medium | Rerank only the stage-1 shortlist (≤ fetch_k) |
| Judge scores wobble run-to-run | Medium | Pin judge model + temperature 0 in `eval.env` |
| Gateway 429 / spend cap | Medium | Keys are rate-limited by design; add `--delay` to runners; batch eval |
| Corrective loop never terminates | Low | Enforce `max_retries`; refuse after the cap |
| DS-background participants anxious about Docker/vector DBs | Medium | Pairing strategy; templates-then-understanding; keep the failure poster as the through-line |

## Timing Recommendations

- Protect Lab 2 (ingestion/OCR) and Lab 4 (hybrid + reranker) at full length — they are the overrun-prone ones; publish `-start` tags so stragglers fast-forward.
- If a cohort is behind, compress M6 theory (it lands through the lab) but never cut Lab 6's staleness toggle — it is the golden thread's payoff.
- If a cohort is strong, pull the multi-hop *and* corrective extension into main scope on Day 4 and add the pgvector comparison as a stretch.
- Hard rule: capstone assembly (Day 4 H3) must start on time with corpus_v2 frozen; cut discussion, not build time. Collect repo URLs at end of Day 4 H3 so harnesses can be verified before demos.

## Discussion Prompts (use during transitions)

1. "Your CTO says 1M-token context windows make RAG obsolete. Rebut it with numbers — cost, latency, access control, freshness, attribution — and concede where it's actually right."
2. "Which of the eight failure classes would be most damaging in *your* organisation, and what probe question would expose it?"
3. "Your assistant scores 0.91 faithfulness in aggregate but collapses on Arabic identifier queries. What does that teach about aggregate metrics?"
4. "Who owns the refusal threshold — engineering or risk — and what does your answer imply about where it lives in the codebase?"
5. "At what point does Dalil stop being 'RAG' and become 'an agent', and what does that mean for the course you take next?"

## Wrap-up (Day 4 final 15 minutes)

- Walk the wall poster: all eight failure stickers removed, each mapped to the module and lab that retired it — the course's spine, made physical.
- Map each mandatory capstone requirement to the module that taught it (one slide), and show the `EVALUATION.md` tables as the evidence pack a risk officer signs.
- Forward pointer: **SDA-AIE-311 (Agentic AI Systems Engineering)** consumes exactly this system shape — Dalil's corrective loop is a one-tool agent; the next course adds planning, multi-tool use via MCP, and multi-agent orchestration on top of the retrieval substrate built here.
- Collect: repository URLs, `EVALUATION.md`, `DECISIONS.md`; issue RAG-badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.12, qdrant-client ≥ 1.9, sentence-transformers / FlagEmbedding for bge-m3 + bge-reranker-v2-m3, RAGAS ≥ 0.1, temperature 0 for every evaluated generation. Verify pinned versions in the course lock file before each delivery.*





