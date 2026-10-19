# FI'L AI | فِعل

**Arabic Action Intelligence — From Words to Actions**

SDAIA Academy: [https://github.com/SDAIAAcademy](https://github.com/SDAIAAcademy)

Project repository: [https://github.com/rahk2003/fil-ai-arabic-action-intelligence](https://github.com/rahk2003/fil-ai-arabic-action-intelligence)

## ملخص سريع

فِعل منصة ذكاء عربي تحوّل الرسائل إلى إجراءات ومهام قابلة للمراجعة. يضم المشروع:

- واجهة React/TypeScript عربية RTL مع تقويم ميلادي ذكي.
- FastAPI وSQLAlchemy مع SQLite افتراضيًا وPostgreSQL اختياريًا.
- مقارنة فعلية بين TF-IDF + Logistic Regression وCAMeLBERT-DA المضبوط دقيقًا.
- مطابقة سياقية باستخدام multilingual MiniLM مع تأكيد بشري قبل تعديل المهام.
- سجل مهام وتغييرات وتصحيحات بشرية قابل للتدقيق.

للتشغيل المحلي مباشرة، انتقل إلى [Full-stack quick start](#full-stack-quick-start-sqlite). للمنهجية وحدود النتائج، راجع [SDAIA submission readiness](#sdaia-submission-readiness) و[`docs/final_verification_report_ar.md`](docs/final_verification_report_ar.md).

FI'L AI is a local Arabic NLP capstone platform for classifying messages and turning them into reviewable structured actions. It combines the preserved Python NLP pipeline with a React/TypeScript Arabic-first interface, a FastAPI REST service, and either SQLite or PostgreSQL. It supports Modern Standard Arabic and common Saudi expressions, extracts bounded date/time patterns, proposes links to earlier tasks, and stores only user-confirmed changes. It uses no paid API.

> **Primary model comparison (reported synthetic experiment):** on the same 125-message Colab test split, the classical baseline recorded **72.0% accuracy / ≈0.719 Macro-F1**, while fine-tuned CAMeLBERT recorded **89.6% accuracy / ≈0.895 Macro-F1**—an improvement of **+17.6 percentage points in accuracy**. These are synthetic-data results, not real-world accuracy. The repository contains the aggregate result artifact but not the row-level predictions or split membership, so the values are reported experiment results rather than a freshly reproduced evaluation. A separate 24-row repository run produced 95.8%, but those rows overlap the fine-tuning corpus; that number is retained only as a contaminated integration diagnostic with a data-leakage warning.

## What works now

- Arabic-first responsive RTL React application with a Gregorian smart calendar as the landing page, dark/light mode, and real API data.
- FastAPI/Pydantic REST API with local CORS, OpenAPI docs, validation, and persistence.
- Four-class local intent prediction: `new_task`, `reschedule`, `cancellation`, `info_only`.
- Explicit Baseline/CAMeLBERT switcher and same-message comparison in React.
- Lazy, process-cached local CAMeLBERT inference with no silent model substitution.
- Multiple-action extraction with evidence spans and uncertainty warnings.
- Common Saudi/Arabic relative dates and times using `Asia/Riyadh` and an explicit message timestamp.
- Cached local `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` embeddings combined with lexical, entity, and recency evidence for contextual candidates; graceful named lexical fallback and no similarity-only merge.
- SQLAlchemy relational schema for conversations, messages, tasks, task events, predictions, and corrections.
- Existing-record-compatible SQLite default and optional Alembic-managed PostgreSQL.
- Confirmed task history and human corrections held as reviewed training candidates—no online retraining.
- Arabic RTL task dashboard with persisted review queue, search, status filters, deadline sorting, overdue indicators, and full message-linked history.
- Month/week/day Gregorian calendar in `Asia/Riyadh`, including red historical deadlines and the one green current deadline for the same task ID.
- Confirmed manual task creation plus CSV/XLSX preview, row validation, duplicate detection, downloadable templates, and explicit import confirmation.
- Separate raw classifier, rule extraction, contextual action, proposed operation, and user-confirmed persistence stages.
- Five-page Gradio dashboard: analyzer, task dashboard, conversation intelligence, evaluation, and dataset explorer.
- Reproducible baseline/classical evaluation, tests, MASSIVE exploration, annotation workflow, and CAMeLBERT training code/Colab notebook.

CAMeLBERT-DA is now fine-tuned and available from the local `models/FIL_AI_CAMeLBERT/` checkpoint. Its training/evaluation data is synthetic, so this improves the capstone comparison but does not remove the need for a human-verified real-world test set.

## Full-stack quick start (SQLite)

Requirements: Git LFS, Python 3.12, and Node.js 20 or newer. After cloning the repository:

```bash
git lfs install
git lfs pull
python3.12 -m venv .venv312
source .venv312/bin/activate
python -m pip install -r backend/requirements.txt -r requirements-dev.txt -r requirements-embeddings.txt
cp .env.example .env
python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

In a second terminal:

```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

Open `http://127.0.0.1:5173`. API documentation is at `http://127.0.0.1:8000/docs`. With the default environment the API upgrades `data/fil_ai.db` additively and preserves its existing records.

## PostgreSQL option

The Docker service is intentionally database-only so inference and the frontend remain lightweight on an 8 GB Apple Silicon Mac.

```bash
docker compose up -d postgres
cp .env.example .env
```

Set this line in `.env` (change the password outside local-only development):

```dotenv
FIL_AI_DATABASE_URL=postgresql+psycopg://fil_ai:fil_ai_local_only@localhost:5432/fil_ai
FIL_AI_AUTO_CREATE_DB=false
```

Create the PostgreSQL schema:

```bash
source .venv312/bin/activate
python -m alembic -c backend/alembic.ini upgrade head
```

Optionally copy preserved SQLite rows without deleting or changing the SQLite source:

```bash
python backend/scripts/migrate_sqlite_to_postgres.py \
  --sqlite sqlite:///./data/fil_ai.db \
  --postgres postgresql+psycopg://fil_ai:fil_ai_local_only@localhost:5432/fil_ai
```

The copy is idempotent by primary key. Verify row counts before selecting PostgreSQL for the application. Secrets belong only in `.env`, which is ignored by Git.

## REST API

Implemented endpoints:

- `POST /api/analyze` — real local intent inference and action extraction.
- `POST /api/analyze/compare` — run Baseline and CAMeLBERT on the exact same message and persist both predictions against one message.
- `POST /api/conversations/analyze` — ordered related-message analysis and review-only before/after suggestions.
- `GET /api/tasks` and `POST /api/tasks` — list and confirm tasks.
- `POST /api/tasks/import/preview|commit` and `GET /api/tasks/import/template` — safe CSV/XLSX import workflow.
- `GET /api/calendar` — current, historical, pending, and unscheduled task calendar data.
- `GET /api/tasks/{id}` — task detail with original message, original/current deadlines, model evidence, and complete history.
- `PATCH /api/tasks/{id}` and `GET /api/tasks/{id}/history` — confirmed changes and append-only history.
- `GET /api/task-suggestions` — unconfirmed new-task/reschedule/cancellation suggestions.
- `POST /api/task-suggestions/{id}/confirm|reject` — explicitly apply or reject a suggestion; rescheduling never creates a duplicate task.
- `POST /api/feedback` — save corrections as reviewed candidates.
- `GET /api/analytics` — committed model/dataset results plus live database counts.
- `GET /api/datasets/samples` and `GET /api/evaluation/errors|model-comparison` — provenance-aware advanced views.
- `GET /api/health` — database and exact loaded model status.

See [`docs/api.md`](docs/api.md) for contracts and examples and [`docs/full_stack_architecture.md`](docs/full_stack_architecture.md) for the runtime and relational design.

## Recommended macOS setup

Python 3.12 is recommended; the original Python 3.14 environment does not provide all data/Transformer dependencies.

```bash
python3.12 -m venv .venv312
source .venv312/bin/activate
python -m pip install -r requirements.txt -r requirements-dev.txt
python scripts/init_db.py
python app.py
```

Open the local URL printed by Gradio (normally `http://127.0.0.1:7860`).

The Gradio application is preserved as a backup demo. It is independent from the React frontend and was not replaced.

## Intelligent task workflow

`POST /api/analyze` always persists the message and real model prediction. A task suggestion is created only when the separate rule/context interpretation supports `create_task`, `reschedule_task`, or `cancel_task`; a raw classifier label alone is insufficient. The React task dashboard displays unconfirmed rows under **بانتظار المراجعة**.

Nothing changes a task until a user confirms. A confirmed new-task suggestion creates one task and records its original deadline. A confirmed reschedule updates that task's current deadline while keeping the original deadline and message-linked before/after history. A confirmed cancellation changes the same task; it never creates a cancellation-shaped duplicate. Missing dates remain missing unless the reviewer explicitly enters one.

The default application location is:

```bash
cd /Users/rana/Documents/Wesh_Alay_NLP_Starter
```

## Reproduce baseline analysis

```bash
source .venv312/bin/activate
python scripts/analyze_errors.py
```

This does not retrain a model. It writes the requested baseline artifacts under `results/baseline/` and `reports/baseline_error_analysis.md`, including per-class metrics, all 12 errors, duplicate checks, model features, and PNG/CSV confusion matrices.

## Reproduce MASSIVE ar-SA download and exploration

```bash
source .venv312/bin/activate
python -m pip install -r requirements-data.txt
python scripts/download_massive.py
python scripts/explore_dataset.py
python scripts/prepare_massive_candidates.py
```

The downloader first invokes the official `AmazonScience/massive` Hugging Face Datasets loader. If that repository script fails, it downloads Amazon's official MASSIVE 1.1 archive URL referenced by the dataset repository and parses `ar-SA.jsonl` through the Hugging Face Datasets JSON loader. It rejects the data unless locale and split counts are exactly 11,514 train / 2,033 validation / 2,974 test.

Original labels and splits are preserved in `data/raw/amazon_massive/*.parquet`. MASSIVE is CC BY 4.0 virtual-assistant data—not workplace messages. The 5,672 extracted candidates remain `unreviewed` and are excluded from supervised FI'L AI training.

## Reproduce classical model experiment

```bash
python scripts/train_classical.py
python scripts/evaluate_models.py
```

The experiment compares word/character/combined TF-IDF with Logistic Regression and Linear SVM. Selection uses validation data from the original training portion; final comparison uses the same preserved 24-row holdout. The selected v2 model scored 0.500 accuracy / 0.470 macro-F1, below the original 0.494 macro-F1, so `config/active_model.json` keeps the original baseline active.

## Tests

```bash
source .venv312/bin/activate
pytest -q

cd frontend
npm test
npm run build
```

The Python suite includes NLP/storage tests and REST API integration tests against temporary SQLite databases and both real local checkpoints. It verifies explicit CAMeLBERT selection, same-message comparison, lazy loading, and failure without fallback. The frontend suite checks the switcher, comparison contract, metadata rendering, and shared components. The regression case `اكملي التسجيل قبل الساعة التاسعة مساء` remains an expected baseline failure. No sentence-specific classifier rule is used.

## CAMeLBERT local inference and comparison

The API validates this exact mapping before loading weights:

```text
0=cancellation, 1=info_only, 2=new_task, 3=reschedule
```

The checkpoint loads only after an explicit CAMeLBERT request and is cached for the FastAPI process. `auto` selects Apple MPS when available and otherwise CPU; set `FIL_AI_TRANSFORMER_DEVICE=cpu|mps` to make the choice explicit. A failed CAMeLBERT request returns HTTP 503 and is never replaced silently with the baseline.

### Primary reported comparison — shared 125-message synthetic split

The source of truth is [`results/camelbert/colab_reported_metrics.json`](results/camelbert/colab_reported_metrics.json).

| Model | Accuracy | Macro-F1 | Evaluation status |
|---|---:|---:|---|
| Classical baseline | **72.0%** | ≈0.719 | Reported Colab result |
| Fine-tuned CAMeLBERT-DA | **89.6%** | ≈0.895 | Reported Colab result |

Accuracy improvement on the same reported synthetic test split: **+17.6 percentage points**. The experiment used a reported 300/75/125 train/validation/test split from 500 synthetic messages. The repository does not contain the exact 500-row file, split membership, row-level test predictions, or Colab confusion matrix. Therefore these values cannot be freshly reproduced or independently audited from the repository alone. Exact-duplicate and paraphrase-family leakage in that 500-message experiment are not verifiable; a random row-level split could allow closely related paraphrases to cross splits.

### Data Leakage warning — 24-row integration diagnostic only

Reproduce the local integration diagnostic on the preserved repository holdout:

```bash
source .venv312/bin/activate
python scripts/evaluate_camelbert_integration.py --device auto
```

Outputs are written to `results/camelbert/`. This local run observed:

| Model | Accuracy | Macro-F1 | Mean inference latency* |
|---|---:|---:|---:|
| TF-IDF + Logistic Regression | 0.500 | 0.494 | 1.23 ms |
| Fine-tuned CAMeLBERT-DA | 0.958 | 0.958 | 115.47 ms |

\*Observed on the current CPU runtime over 24 synthetic messages; latency varies by device and excludes one-time lazy model loading.

**Do not use 95.8% as the primary model accuracy.** The 24 rows overlap CAMeLBERT fine-tuning data, so this is a contaminated pipeline/integration diagnostic, not an independent performance comparison or a real-world estimate. The raw artifacts remain unchanged and tied to their actual dataset.

The only CAMeLBERT error on this diagnostic was `ما يحتاج ترفعين النموذج بعد القرار الجديد.` (`cancellation` → `new_task`). The two user-reported failures are also reproduced and recorded without hard-coded correction in `results/camelbert/known_failure_cases.csv`.

## Semantic context matching

Install and cache the local embedding model once:

```bash
source .venv312/bin/activate
python -m pip install -r requirements-embeddings.txt
python scripts/evaluate_context_matching.py
```

The verified local runtime loaded exactly `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` on Apple MPS with 384-dimensional normalized vectors. On the tiny eight-pair synthetic test partition shared by both methods, lexical matching obtained precision 1.000, recall 0.250, F1 0.400, and zero false matches; embeddings obtained precision 0.500, recall 0.500, F1 0.500, and two false matches. The embedding threshold selected on only four validation pairs was 0.30 and is not stable enough to drive automatic behavior. Production therefore keeps a more conservative threshold plus entity/recency evidence and explicit confirmation. See `results/context_matching/`.

## CAMeLBERT training provenance

The supplied training program still requires rows marked `human_verified`. Do not retrain from unreviewed corrections.

```bash
python -m pip install -r requirements-transformer.txt
python scripts/train_transformer.py --data data/annotation/annotation_template.csv
```

On an 8 GB Mac, use `notebooks/train_camelbert_colab.ipynb` with a GPU after reviewing privacy requirements. Nothing is uploaded automatically. The script/notebook uses `CAMeL-Lab/bert-base-arabic-camelbert-da` with max length 128, validation, early stopping, and best-checkpoint selection.

## Project map

- `src/fil_ai/` — normalization, inference, extraction, context matching, orchestration, SQLite.
- `backend/` — FastAPI, Pydantic, SQLAlchemy, Alembic, migration utility, and API tests.
- `frontend/` — React, TypeScript, Vite, Tailwind, Recharts, and component tests.
- `scripts/` — data, training, evaluation, analysis, and DB commands.
- `tests/` — normalization, model, extraction, timezone, context, duplicate, and persistence tests.
- `data/raw/amazon_massive/` — official local ar-SA Parquet splits and manifest.
- `data/processed/` / `data/annotation/` — unreviewed candidates and annotation workflow.
- `models/baseline_v1/` — identifiable copy of the original model/training code.
- `results/baseline/original/` — preserved original evaluation artifacts.
- `docs/` / `reports/` — architecture, dataset/model cards, methodology, demo, training, and evaluation.
- `docker-compose.yml` — optional local PostgreSQL 16 service.

## SDAIA submission readiness

| Requirement | Status | Evidence / limitation |
|---|---|---|
| End-to-end Arabic NLP pipeline | Complete | Local classification, normalization, extraction, context suggestions, API, UI, persistence |
| Baseline and improved method on same test set | Complete | `results/model_comparison.csv`; v2 was not promoted because macro-F1 was lower |
| Quantitative evaluation | Complete for synthetic holdout | 50% accuracy / 0.494 macro-F1; not real-world accuracy |
| At least 10 categorized errors | Complete | All 12 holdout errors in `reports/baseline_error_analysis.md` |
| Fine-tuning or evidence-based justification | Complete with limitation | Fine-tuned CAMeLBERT checkpoint is integrated; current labels/evaluation are synthetic rather than real-world verified |
| Embeddings plus decision component | Complete with major evaluation limitation | Local multilingual MiniLM embeddings feed conservative context ranking; same-pair comparison is only 8 synthetic test pairs |
| GitHub instructions and demo material | Complete | This README, `docs/demo_scenarios.md`, `docs/presentation_outline.md` |

Do not mark the scientific evaluation fully ready until a sufficiently sized, privacy-reviewed, human-labeled Saudi workplace test set is locked by conversation/paraphrase family. The next scientific step is dataset review and annotation—not another synthetic-data model claim.

## GitHub submission status

- Public repository: `https://github.com/rahk2003/fil-ai-arabic-action-intelligence`.
- Default branch: `main`.
- The fine-tuned `models/FIL_AI_CAMeLBERT/` checkpoint is versioned with Git LFS; run `git lfs pull` after cloning.
- `.env`, SQLite databases, virtual environments, `node_modules`, build output, and the downloadable embedding cache remain ignored.
- The validated classical `.joblib` checkpoints, source code, tests, documented datasets, evaluation artifacts, and capstone documentation are tracked.

Before the final academy handoff, run the Python tests, frontend tests/build, and inference checks shown above. Then open both `/api/health` and the React dashboard from a clean clone. Never commit tokens, passwords, runtime databases, or private user messages.

## Privacy and scientific limits

- Never use private messages without permission and irreversible de-identification.
- Synthetic metrics cannot establish Saudi-dialect or real-world accuracy.
- MASSIVE labels are never silently mapped to FI'L AI labels.
- Similarity and rules generate suggestions, not proof; all stored task mutations require confirmation.
- Compare models only on the same locked test set.

## Official attribution

- AmazonScience MASSIVE 1.1, CC BY 4.0: https://huggingface.co/datasets/AmazonScience/massive
- CAMeLBERT-DA: https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-da
- Multilingual MiniLM candidate: https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
