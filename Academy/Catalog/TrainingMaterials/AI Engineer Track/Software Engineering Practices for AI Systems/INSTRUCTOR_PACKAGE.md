# Software Engineering Practices for AI Systems
## ممارسات هندسة البرمجيات لأنظمة الذكاء الاصطناعي

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Software Engineering Practices for AI Systems |
| **Arabic Title** | ممارسات هندسة البرمجيات لأنظمة الذكاء الاصطناعي |
| **Level** | Practitioner |
| **Duration** | 3 days × 5 learning hours = **15 hours** |
| **Audience** | AI practitioners preparing for production engineering roles |
| **Prerequisites** | SDA-FND-103; SDA-AIE-111 recommended |
| **Assessment** | Labs (60%) + containerised model-service capstone project (40%) |
| **Stackability** | Engineering badge · Required for MLOps and production modules · Next: SDA-AIE-211, SDA-AIE-216 |
| **Tools & Platforms** | FastAPI · Docker · pytest · GitHub Actions · pydantic |

## Course Description

A production-engineering module that turns model builders into software engineers. Participants design clean APIs around models, containerise services with Docker, automate testing and CI/CD, and structure AI codebases for maintainability. These practices underpin every deployment module later in the track.

The course is built around a single evolving artefact: a **fraud-detection model service** that participants refactor, wrap in an API, containerise, test, and ship through a CI/CD pipeline. Every lab produces a component of the final capstone, so by Day 3 each participant owns a working, tested, containerised, pipeline-validated AI service — the same shape of system they will operate in SDA-AIE-211 (MLOps) and SDA-AIE-216.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Design RESTful APIs that expose ML models as reliable services
2. **LO2** — Implement containerised AI services using Docker and compose workflows
3. **LO3** — Develop automated unit, integration, and model-behaviour tests
4. **LO4** — Build CI/CD pipelines that validate and ship AI code changes
5. **LO5** — Apply clean architecture and configuration-management patterns to AI codebases
6. **LO6** — Evaluate code quality using reviews, linting, and static analysis

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | From notebook to service | M1: Structuring AI Projects & Clean Architecture · M2: APIs for Model Serving with FastAPI | 45% | 55% | Clean-architecture project skeleton + working FastAPI prediction endpoint |
| **Day 2** | Ship it in a box, prove it works | M3: Docker & Containerised Services · M4: Testing Strategies for ML Code | 40% | 60% | Containerised service (compose) + passing unit/integration/behaviour test suite |
| **Day 3** | Automate everything | M5: CI/CD with GitHub Actions · M6: Configuration, Secrets & Logging · Capstone | 30% | 70% | Green CI pipeline + hardened service + capstone demo |

## Hour-by-Hour Breakdown

### Day 1 — From Notebook to Service

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why AI systems fail in production** + course kickoff | Recognise the gap between notebook code and production code; identify the 6 engineering practices covered | Interactive lecture + failure-story discussion | 80/20 |
| 2 | **Clean architecture for ML codebases** (M1) | Layered design; dependency rule; separating domain, model, and infrastructure code; src-layout | Lecture + live refactoring demo | 70/30 |
| 3 | **Lab 1 — Refactor the notebook** | Convert a messy fraud-detection notebook into a clean src-layout package | Guided lab (pairs) | 10/90 |
| 4 | **REST API design for model serving** (M2) | Resource design, pydantic validation, error contracts, health/readiness endpoints, versioning | Lecture + API design walkthrough | 70/30 |
| 5 | **Lab 2a — Build the prediction API** | Implement `/v1/predict`, `/health`, schemas, error handling in FastAPI | Guided lab (pairs) | 10/90 |

### Day 2 — Ship It in a Box, Prove It Works

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Lab 2b — Hardening the API** | Add model warm-up on startup, request logging middleware, OpenAPI docs; load-test with `hey` | Lab + micro-lecture | 20/80 |
| 2 | **Docker fundamentals for AI services** (M3) | Images vs containers, layers and caching, multi-stage builds, image size discipline, compose | Lecture + live build demo | 70/30 |
| 3 | **Lab 3 — Containerise the service** | Write multi-stage Dockerfile, .dockerignore, compose file with healthcheck; measure image size and startup | Guided lab | 10/90 |
| 4 | **Testing strategies for ML code** (M4) | Testing pyramid for ML; unit vs integration vs model-behaviour tests; fixtures; invariance/directional tests | Lecture + test-writing demo | 70/30 |
| 5 | **Lab 4 — Test suite** | pytest unit + API integration + behavioural tests; coverage report ≥ 80% on service layer | Guided lab | 10/90 |

### Day 3 — Automate Everything

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **CI/CD for AI codebases** (M5) | Pipeline anatomy; GitHub Actions syntax; quality gates; building and pushing images from CI | Lecture + pipeline dissection | 60/40 |
| 2 | **Lab 5 — Build the pipeline** | Workflow: lint → type-check → test → build image → smoke test; branch protection | Guided lab | 10/90 |
| 3 | **Config, secrets & logging** (M6) + **Lab 6** | pydantic-settings, .env discipline, secret hygiene, structured JSON logging | Micro-lecture + lab | 30/70 |
| 4 | **Capstone assembly** | Integrate all components; complete capstone checklist; peer code review round | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 5-minute demos; rubric-based peer + instructor scoring; path to SDA-AIE-211/216 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module touches the same fraud-detection service. Never introduce a throwaway example codebase — always evolve `fraud-service`. This is what makes the capstone achievable in Day 3 Hour 4.
- **Pace control:** Labs 2a and 3 are the most overrun-prone. Publish checkpoint commits (`lab2-start`, `lab2-solution`, `lab3-start`, ...) in the course repository so stragglers can fast-forward: `git checkout lab3-start`.
- **Pairing:** rotate pairs each day. Pair a strong-Python participant with a strong-ML participant; the skill transfer is the point.
- **Environment strategy:** primary = local Docker Desktop / Colima; fallback = GitHub Codespaces (devcontainer provided). Verify both the week before delivery.
- **Language:** deliver in English or Arabic; keep all code, identifiers, and commit messages in English (production convention in Saudi enterprise environments — mixed-language logs break grep-based operations).
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day-3 afternoon is deliberately lighter on theory.
- **Assessment logistics:** rubric scoring happens live during Day 3 Hour 5 demos; collect repository URLs at the end of Hour 4 so CI status can be verified before demos begin.

---

# Module 1 — Structuring AI Projects and Clean Architecture

## Module Overview

**Purpose.** Most AI failures in production trace back not to bad models but to bad structure: model code welded to I/O code, hidden global state, untestable functions, and paths hard-coded to someone's laptop. This module teaches participants to organise an AI codebase so that the model is a replaceable component inside a well-defined architecture — the precondition for everything else in this course.

**Business relevance.** Enterprises in the Saudi market (banking, telecom, government digital services) increasingly require AI teams to pass the same engineering review gates as any software team. A cleanly structured codebase cuts onboarding time for new engineers from weeks to days, makes security audits tractable, and is a prerequisite for the national push toward production-grade AI services rather than proofs-of-concept.

**Industry use cases.**
- A bank's fraud team must swap a gradient-boosting model for a neural model without touching API or infrastructure code — possible only if the model sits behind a stable internal interface.
- A telecom churn-prediction service must be maintained by a team that did not build it; clean layering plus a standard project layout is what makes the handover survivable.
- A government-services chatbot codebase must pass a third-party security review; reviewers need to locate all external I/O in one layer.

**Expected competencies.** After this module a participant can lay out an AI repository in src-layout, separate domain/service/infrastructure layers, apply the dependency rule, define model interfaces with Python protocols, and defend the structure in a code review.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Explain why notebook-style code fails production review, with concrete failure modes | LO5 |
| 1.2 | Structure an AI repository using src-layout with separated layers | LO5 |
| 1.3 | Apply the dependency rule: domain code imports nothing from infrastructure | LO5 |
| 1.4 | Define a model-loading interface that isolates the ML framework from the service | LO5, LO1 |
| 1.5 | Evaluate a peer's project structure against a review checklist | LO6 |

## Technical Content

### 1. The notebook-to-production gap

A research notebook optimises for iteration speed: everything global, everything mutable, execution order defined by human memory. Production code optimises for the opposite: explicit inputs and outputs, deterministic execution, testability, and the ability to change one thing without breaking five others. The gap shows up as concrete failure modes worth naming in class:

- **Hidden state:** `model` trained in cell 12, used in cell 38 — after cell 25 mutated the feature list. In production this becomes "works on my machine".
- **Environment coupling:** `pd.read_csv("/Users/aisha/data/txns.csv")` — the path *is* the bug. Every I/O location must be injected configuration, never a literal.
- **Import-time side effects:** loading a 2 GB model at module import means every tool that imports the module (test runner, linter worker, docs builder) pays the cost — and the API server can't control *when* loading happens or handle its failure.
- **No seams:** if predict logic, feature engineering, and database access live in one 300-line function, there is nowhere to attach a test, a mock, or a cache.

**Instructor note:** open the provided `notebook_v1.ipynb` (deliberately awful) and have the class call out smells for 5 minutes before you name them formally. Participants find 80% of them unprompted — this builds ownership.

### 2. Clean architecture applied to ML services

Classic clean architecture (Cochito/onion/hexagonal — the names differ, the idea doesn't) arranges code in concentric layers with one rule: **dependencies point inward.**

For an ML service the layers materialise as:

| Layer | Contains | May import | Must never import |
|---|---|---|---|
| **Domain** | Prediction request/result types, feature definitions, business rules (e.g., "score > 0.85 ⇒ block transaction") | stdlib, pydantic | FastAPI, sklearn, boto3, SQL drivers |
| **Service (use-case)** | `FraudScorer.score(txn)` orchestration: validate → featurise → predict → apply policy | Domain, model *interface* | HTTP, Docker, cloud SDKs |
| **Adapters / Infrastructure** | Model loaders (joblib/ONNX), feature store client, database repositories | Service interfaces, frameworks | — |
| **Entrypoints** | FastAPI app, CLI, batch job | Everything below | — |

Two consequences matter most for ML teams:

1. **The model is an adapter.** The service layer depends on a `Model` *protocol* (`predict(features) -> Score`), not on sklearn. Swapping XGBoost for PyTorch, or a local file for a model registry, changes one adapter file. This is the architectural insight that separates this course from a FastAPI tutorial.
2. **Frameworks live at the edge.** FastAPI request models and sklearn objects never appear in domain signatures. When FastAPI 2.0 or a new framework arrives, the blast radius is the entrypoint layer only.

### 3. The standard project layout

The course's canonical layout (participants replicate this in Lab 1 and keep it through the capstone):

```
fraud-service/
├── pyproject.toml            # single source of truth: deps, tool config
├── README.md                 # runbook: how to run, test, build
├── .gitignore
├── .dockerignore
├── Makefile                  # make test / make lint / make run / make image
├── configs/
│   └── settings.example.env  # documented template, never real secrets
├── src/
│   └── fraud_service/
│       ├── __init__.py
│       ├── domain/
│       │   ├── entities.py       # Transaction, FraudScore
│       │   └── policies.py       # decision thresholds as pure functions
│       ├── service/
│       │   ├── scorer.py         # use-case orchestration
│       │   └── interfaces.py     # Model / FeatureRepo protocols
│       ├── adapters/
│       │   ├── sklearn_model.py  # joblib-backed Model implementation
│       │   └── memory_repo.py    # in-memory FeatureRepo (test double lives with prod code deliberately? No →
│       │                         #   real doubles live in tests/; this one is a genuine fallback adapter)
│       ├── api/
│       │   ├── app.py            # FastAPI factory
│       │   ├── schemas.py        # pydantic request/response models
│       │   └── routes.py
│       ├── config.py             # pydantic-settings
│       └── logging_setup.py
├── models/                   # versioned artefacts (or pulled at build/start)
│   └── fraud_xgb_v3.joblib
└── tests/
    ├── unit/
    ├── integration/
    └── behavioural/
```

Why **src-layout** (code under `src/` rather than package at repo root): it forces tests to run against the *installed* package, not the working directory — the same import path CI and the Docker image will use. The classic bug it prevents: tests pass locally because `import fraud_service` resolves to the repo folder, then fail in the container where the package was installed differently.

Key points to emphasise:

- `pyproject.toml` centralises dependencies **and** tool configuration (ruff, pytest, mypy) — one file to review, one file to cache in CI.
- `Makefile` is the team's public API for the repo. `make test` must work on day one and forever; nobody should need to remember pytest flags.
- Model artefacts are **inputs, not source**. Small artefacts may live in `models/` via Git LFS for training simplicity; production-grade flow pulls them from a registry at image build or container start (covered in M3/M6). Never `pickle.load` from an unverified path — pickle executes arbitrary code, so an attacker who can write the model file owns the service.

### 4. Interfaces and dependency injection in Python

Python needs no framework for DI — constructor injection plus `typing.Protocol` suffices, and it is what keeps the service testable:

```python
# src/fraud_service/service/interfaces.py
from typing import Protocol
from fraud_service.domain.entities import FeatureVector, RawScore

class Model(Protocol):
    """Anything that can score a feature vector.

    Implementations: SklearnModel (prod), ConstantModel (tests),
    RemoteModel (future — calls a model server).
    The service layer knows ONLY this signature.
    """
    model_version: str

    def predict_proba(self, features: FeatureVector) -> RawScore: ...
```

```python
# src/fraud_service/service/scorer.py
from dataclasses import dataclass
from fraud_service.domain.entities import Transaction, FraudScore
from fraud_service.domain.policies import decide
from fraud_service.service.interfaces import Model

@dataclass
class FraudScorer:
    """Use-case: score one transaction.

    Note what is ABSENT: no FastAPI, no sklearn, no file paths,
    no logging configuration. Pure orchestration = trivially testable.
    """
    model: Model
    block_threshold: float

    def score(self, txn: Transaction) -> FraudScore:
        features = txn.to_features()           # domain logic
        raw = self.model.predict_proba(features)
        decision = decide(raw, self.block_threshold)
        return FraudScore(
            transaction_id=txn.transaction_id,
            probability=raw.value,
            decision=decision,
            model_version=self.model.model_version,
        )
```

The FastAPI layer (Module 2) constructs `FraudScorer(model=SklearnModel.load(...), block_threshold=settings.threshold)` once at startup. Tests construct `FraudScorer(model=ConstantModel(0.99), block_threshold=0.85)` in one line. That symmetry is the payoff of the whole module.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Dependency rule:* imports point inward; enforce with `ruff` isort sections or `import-linter` contracts (shown in M5's pipeline).
- *One direction of knowledge:* domain knows nothing about persistence or HTTP; adapters know everything about their technology and nothing about each other.
- *Composition root:* exactly one place (the app factory) wires concrete implementations together.
- *Small, boring modules:* a file you can read in two minutes is an asset; a 900-line `utils.py` is a liability. `utils.py` is where cohesion goes to die — ban the filename.

**Common mistakes (each appears in the Lab 1 starter repo deliberately)**
1. Loading the model at import time (`model = joblib.load(...)` at module top level).
2. pydantic API schemas used as domain entities everywhere ("schema leakage") — couples the whole codebase to the HTTP contract.
3. Feature engineering duplicated between training repo and serving repo — the #1 cause of training/serving skew; the fix is a shared, versioned feature module imported by both.
4. `except Exception: pass` around model calls — silently returning stale or default scores.
5. Configuration read via `os.environ["X"]` scattered across 14 files instead of one typed settings object.
6. Test code importing private internals (`from fraud_service.adapters.sklearn_model import _sanitize`) — tests should exercise public seams.

**Production considerations**
- Repository structure is an *operational* interface: on-call engineers navigate your repo at 03:00. Predictability beats cleverness.
- Version everything that affects a prediction: code (git SHA), model (artefact version), features (module version), config (env snapshot). M6 wires these into logs.
- Plan for two consumers from day one: the online API and an offline batch scorer. If both can import the same `FraudScorer`, the architecture is right.

### 6. Real-world example walkthrough

Narrate this (5 minutes, no slides): a regional bank's fraud model — 94% AUC in the notebook — shipped as a 700-line Flask file. Six months later: the data scientist left; a feature was computed differently in training (pandas) vs serving (raw dict math); a silent `except` masked the skew; fraud losses rose 11% before anyone connected the dots. The postmortem's first action item was not "better model" — it was "shared feature module + behavioural tests + layered refactor". This course is that action item, generalised.

## Code Examples

### Domain entities (pure, framework-free)

```python
# src/fraud_service/domain/entities.py
"""Domain entities: the vocabulary of the fraud problem.

Rules for this file:
- imports from stdlib + pydantic ONLY
- no I/O, no framework types, no ML library types
"""
from datetime import datetime
from enum import StrEnum
from pydantic import BaseModel, Field, field_validator


class Channel(StrEnum):
    POS = "pos"
    ECOM = "ecom"
    ATM = "atm"
    TRANSFER = "transfer"


class Transaction(BaseModel):
    """A single card/account transaction to be scored."""
    transaction_id: str = Field(min_length=8)
    amount_sar: float = Field(gt=0, description="Amount in Saudi Riyal")
    channel: Channel
    merchant_category: str
    customer_id: str
    timestamp: datetime

    @field_validator("merchant_category")
    @classmethod
    def normalise_mcc(cls, v: str) -> str:
        # Domain rule: categories are upper-snake, e.g. "GROCERY"
        return v.strip().upper().replace(" ", "_")

    def to_features(self) -> "FeatureVector":
        """Single source of feature logic shared by training & serving.

        Keeping this on the entity (or in one feature module) is the
        primary defence against training/serving skew.
        """
        return FeatureVector(values={
            "amount_log": _log1p(self.amount_sar),
            "channel": self.channel.value,
            "mcc": self.merchant_category,
            "hour_of_day": self.timestamp.hour,
            "is_night": int(self.timestamp.hour < 6),
        })


class FeatureVector(BaseModel):
    values: dict[str, float | int | str]


class RawScore(BaseModel):
    value: float = Field(ge=0.0, le=1.0)


class Decision(StrEnum):
    ALLOW = "allow"
    REVIEW = "review"
    BLOCK = "block"


class FraudScore(BaseModel):
    transaction_id: str
    probability: float
    decision: Decision
    model_version: str


def _log1p(x: float) -> float:
    import math
    return math.log1p(x)
```

### Policy as a pure function

```python
# src/fraud_service/domain/policies.py
"""Business policy: thresholds are BUSINESS decisions, not model decisions.

Pure function => property-based-testable, reviewable by risk officers.
"""
from fraud_service.domain.entities import Decision, RawScore

REVIEW_BAND = 0.15  # width of the manual-review band below block threshold

def decide(score: RawScore, block_threshold: float) -> Decision:
    if score.value >= block_threshold:
        return Decision.BLOCK
    if score.value >= block_threshold - REVIEW_BAND:
        return Decision.REVIEW
    return Decision.ALLOW
```

### The model adapter (framework quarantined)

```python
# src/fraud_service/adapters/sklearn_model.py
"""The ONLY file in the service that imports sklearn/joblib.

If we move to ONNX or a remote model server, we add a sibling
adapter and change one line in the composition root.
"""
from pathlib import Path
import joblib
import pandas as pd

from fraud_service.domain.entities import FeatureVector, RawScore


class SklearnModel:
    def __init__(self, pipeline, model_version: str) -> None:
        self._pipeline = pipeline          # full sklearn Pipeline: encoder + model
        self.model_version = model_version

    @classmethod
    def load(cls, path: Path) -> "SklearnModel":
        """Explicit, failable loading — called by the app factory at
        startup, NEVER at import time. Version travels with the artefact."""
        bundle = joblib.load(path)         # {"pipeline": ..., "version": "v3.2.0"}
        return cls(bundle["pipeline"], bundle["version"])

    def predict_proba(self, features: FeatureVector) -> RawScore:
        frame = pd.DataFrame([features.values])
        proba = float(self._pipeline.predict_proba(frame)[0, 1])
        return RawScore(value=proba)
```

### Composition root

```python
# src/fraud_service/api/app.py  (excerpt — full version in Module 2)
from contextlib import asynccontextmanager
from fastapi import FastAPI

from fraud_service.adapters.sklearn_model import SklearnModel
from fraud_service.config import Settings
from fraud_service.service.scorer import FraudScorer


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Composition root: the one place concrete classes meet.
    Model loads HERE — visible, timed, failable, logged."""
    settings = Settings()                                  # M6: typed config
    model = SklearnModel.load(settings.model_path)         # fails fast if missing
    app.state.scorer = FraudScorer(
        model=model, block_threshold=settings.block_threshold
    )
    yield
    # teardown: close clients, flush logs


def create_app() -> FastAPI:
    return FastAPI(title="Fraud Scoring Service", lifespan=lifespan)
```

## Hands-on Lab 1 — Refactor the Notebook into a Clean Package

| | |
|---|---|
| **Objective** | Transform `notebook_v1.ipynb` (fraud model, deliberately messy) into the canonical src-layout package with domain/service/adapter layers, runnable via `make run-batch` |
| **Duration** | 50 minutes |
| **Setup** | Python 3.12, `uv` or `pip`, course repo cloned, `git checkout lab1-start` |

**Instructions & tasks**

1. *(5 min)* Run the notebook top-to-bottom; note the three execution-order traps flagged with `# SMELL` comments.
2. *(10 min)* Create the skeleton: `pyproject.toml` (name, Python ≥3.12, deps: pydantic, pandas, scikit-learn, joblib), `src/fraud_service/` with `domain/`, `service/`, `adapters/` packages, and `tests/`.
3. *(15 min)* Move code to layers: entities + `to_features()` into `domain/entities.py`; threshold logic into `domain/policies.py`; scoring orchestration into `service/scorer.py` against the `Model` protocol; joblib loading into `adapters/sklearn_model.py`.
4. *(10 min)* Write the batch entrypoint `src/fraud_service/batch.py`: read `data/transactions_sample.csv`, score each row, write `scored.csv`. Wire concretes ONLY here.
5. *(5 min)* Add `Makefile` targets `install`, `run-batch`, `lint` (ruff). Run `make run-batch`.
6. *(5 min)* Commit with message `refactor: extract clean architecture layers from notebook`.

**Expected output**
```
$ make run-batch
Loaded model fraud_xgb v3.2.0 in 0.41s
Scored 5,000 transactions -> scored.csv  (block: 37, review: 214, allow: 4749)
$ ruff check src tests
All checks passed!
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: fraud_service` | Package not installed / not src-layout aware | `pip install -e .` and confirm `[tool.setuptools] package-dir` or hatch src-layout config |
| `joblib` version warning on load | Artefact pickled with different sklearn | Pin sklearn version from `models/MODEL_CARD.md`; discuss artefact/env coupling (foreshadows Docker) |
| Circular import domain ⇄ service | Entity importing scorer | Dependencies point inward only; move shared type into domain |
| Different scores vs notebook | Feature drift during move | Diff `to_features()` output against notebook cell 9 output for 5 sample rows |

**Instructor notes.** The starter notebook contains exactly the six "common mistakes" from the content section — walk the room and check who catches #3 (duplicated feature logic); it is the one with real production consequences. Fast finishers: add `ConstantModel` test double and a first unit test — a perfect bridge to Module 4.

## Mini Exercises

**Quiz (5 questions)**
1. Which import is legal under the dependency rule? (a) domain→sklearn (b) service→FastAPI (c) adapters→service interfaces (d) domain→adapters → **c**
2. Why src-layout? → forces tests/CI/containers to import the installed package, eliminating "works from repo root" bugs.
3. Where may `joblib` be imported? → only in the model adapter.
4. What belongs in the composition root? → construction and wiring of concrete implementations (settings, model, scorer).
5. True/False: pydantic in domain entities violates clean architecture. → **False** (it's a validation library, not an I/O framework — but API schemas must still stay separate).

**Debugging exercise.** Give participants a branch where `entities.py` imports `SklearnModel` for a type hint, creating a cycle. Fix options: `TYPE_CHECKING` guard vs protocol in service layer — discuss why the protocol fix is architecturally correct and the guard is a band-aid.

**Code-review exercise.** Review `review_me_module1.py` (a 180-line "god file" PR). Each pair writes ≥5 review comments; compare against the instructor's model review (provided in solutions repo).

**Discussion questions.**
- Your data scientists say layering "slows experimentation." What hybrid workflow do you propose? (notebooks import the domain feature module; only promoted code gets layered)
- Should the fraud threshold live in code, config, or database? What changes the answer? (audit requirements, change cadence, who owns it)

## Case Study — Recommendation System Monolith at a Regional E-commerce Platform

**Scenario.** "SouqPlus", a Riyadh-based e-commerce platform, runs a product-recommendation engine built by a since-departed contractor: one repository, one 2,400-line module, Flask + pandas + LightGBM + Redis calls interleaved. Black Friday (White Friday) is 10 weeks away.

**Business context.** Recommendations drive 23% of revenue. Two incidents last quarter: a Redis timeout took down the whole API (no separation between cache adapter and scoring logic), and an emergency model swap took 9 days because retraining code and serving code disagreed on 4 of 61 features.

**Technical challenge.** Refactor to clean architecture *incrementally* — the service cannot be frozen for a rewrite.

**Constraints.** Two engineers; zero downtime tolerance during Ramadan-season traffic; the model artefact itself may not be retrained (risk sign-off takes 6 weeks); Arabic + English product metadata must be preserved byte-exact through any refactor.

**Solution approach (facilitate, don't lecture).** Strangler-fig refactor: (1) characterisation tests around current HTTP behaviour first (M4 preview); (2) extract the feature module and make training import it; (3) extract `Model` protocol + LightGBM adapter; (4) extract Redis behind a `FeatureRepo` protocol with a circuit breaker; (5) only then split the API layer. Each step ships independently behind the existing endpoints.

**Discussion questions.**
1. Why must characterisation tests precede any code movement?
2. Which extraction delivers the most risk reduction per engineering day? (feature module — it addresses the skew incident)
3. The CTO proposes a full rewrite in Go "while we're at it." Argue for/against with the 10-week deadline.
4. How do you prove byte-exact metadata behaviour across the refactor? (golden-file tests)

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Import time of `fraud_service` | Performance | < 300 ms (no model load at import) | `python -X importtime -c "import fraud_service"` |
| Batch scoring throughput | Performance | ≥ 2,000 txn/s on lab laptop | `make run-batch` timing |
| Cyclomatic complexity (max) | Code quality | ≤ 10 per function | `ruff` / `radon cc` |
| Layer-violation imports | Code quality | 0 | `import-linter` contract |
| Longest module | Code quality | ≤ 200 lines | `wc -l` in review |
| Time for a newcomer to locate feature logic | Maintainability | < 2 min | pair exercise |

**Example benchmark table (filled during lab):**

| Version | Import time | Batch 5k txns | Max complexity | Layer violations |
|---|---|---|---|---|
| notebook_v1 export | 2.9 s (loads model) | 6.1 s | 24 | n/a (no layers) |
| lab1-solution | 0.18 s | 2.3 s | 7 | 0 |

## Required Visuals and Training Assets

### Diagrams
1. **Clean architecture rings for ML services** — *Purpose:* anchor image for the whole course. *Elements:* four concentric rings (Domain, Service, Adapters, Entrypoints); arrows all pointing inward; callout boxes placing "sklearn adapter", "FastAPI app", "FraudScorer", "Transaction entity" in their rings; a red crossed-out arrow showing domain→sklearn as forbidden. *Style:* flat vector, 4-colour palette, English labels with Arabic subtitles. *Designer description:* "Concentric circles diagram, center labeled Domain with entity icons, outer ring labeled Entrypoints with FastAPI/CLI icons, green arrows inward, one red forbidden arrow outward."
2. **Canonical project tree** — *Purpose:* memorisable reference poster. *Elements:* the `fraud-service/` tree above with per-folder one-line annotations and layer colour-coding matching diagram 1. *Style:* monospace tree on light background, printable A4.
3. **Training/serving skew flow** — *Purpose:* motivate the shared feature module. *Elements:* two parallel pipelines (training, serving) both importing one `features.py` box; a "before" variant with two divergent feature boxes and a warning icon. *Style:* before/after split panel.
4. **Strangler-fig refactor sequence** (case study) — *Purpose:* show incremental extraction. *Elements:* 5 numbered snapshots of the monolith with successive pieces extracted behind interfaces. *Style:* timeline strip.

### Images (screenshots)
1. **IDE screenshot — src-layout in VS Code**: expanded tree with layers visible; *why:* participants mirror it during Lab 1; *content:* exact folder tree, ruff extension active, no red squiggles.
2. **Terminal screenshot — `make run-batch` output**: *why:* expected-output reference; *content:* the model-load line with timing + scored counts exactly as in lab spec.
3. **Terminal screenshot — `python -X importtime` before/after**: *why:* makes the import-time smell measurable; *content:* two runs side by side, 2.9 s vs 0.18 s highlighted.
4. **GitHub screenshot — PR diff of the refactor commit**: *why:* shows reviewable, incremental change; *content:* file-move diff with green/red blocks and a review comment thread.

### Simulations
1. **Import-time model-load hang** — *Setup:* branch `sim-import-load` moves `joblib.load` to module top level and points it at a 1.8 GB artefact on slow storage. *Expected behaviour:* `pytest --collect-only` takes 45+ s; participants must explain why *collecting* tests loads a model. *Learning objective:* import-time side effects punish every tool, not just the server.
2. **Feature-skew incident** — *Setup:* branch `sim-skew` changes serving-side `amount_log` to `log10` while training used `log1p`; scores shift subtly. *Expected behaviour:* batch output diverges from golden file on 12% of rows; no exception raised. *Learning objective:* skew is silent; only shared code or behavioural tests catch it.

### Interactive Activities
- **Architecture review round-table (20 min):** pairs exchange Lab 1 repos and complete the structure checklist (12 items); each pair reports one violation found.
- **"Where does this code live?" card sort (10 min):** 16 code-snippet cards (threshold rule, Redis call, pydantic schema, retry decorator…) physically sorted onto a floor-sized rings diagram.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `transactions_sample.csv` | Synthetic, generated by course tooling (Faker + fraud-pattern injector, SAR amounts, KSA merchant categories) | CSV | 5,000 rows × 9 cols | Lab 1 batch scoring; reused across all modules |
| `fraud_xgb_v3.joblib` | Pre-trained on synthetic set by course team | joblib bundle | ~4 MB | Constant artefact for all labs |
| `golden_scores_v3.csv` | Produced by reference solution | CSV | 5,000 rows | Skew simulation & behavioural tests |

### Demo Requirements
- **Instructor demo:** live refactor of one function from the notebook into `domain/` + adapter, with a test double, in under 8 minutes — rehearse it; the speed *is* the message.
- **Student demo:** two volunteer pairs walk through their layer boundaries at end of Hour 3; class challenges one import decision each.
- **Expected outputs:** green `ruff`, working `make run-batch`, zero import-linter violations.

---

# Module 2 — APIs for Model Serving with FastAPI

## Module Overview

**Purpose.** The API is the model's contract with the world. This module teaches participants to design and implement HTTP APIs that make an ML model consumable, observable, and safe to evolve: resource design, strict validation with pydantic, meaningful errors, health/readiness semantics, and versioning.

**Business relevance.** Every enterprise integration — mobile app, core-banking middleware, government service bus — talks to models through an API. A sloppy contract multiplies integration cost across every consumer; a validation gap becomes a production incident (or a security finding) rather than a 422 response. In regulated Saudi sectors (SAMA-supervised banks, health providers), the API layer is also where auditability requirements land.

**Industry use cases.**
- Fraud scoring called synchronously in the payment path at < 150 ms p99.
- A hospital's triage-assist model consumed by three different EMR vendors — strict schemas are the only thing keeping integrations honest.
- An internal LLM gateway exposing `/v1/chat` with per-team quotas and consistent error envelopes.

**Expected competencies.** Participants can design request/response schemas, implement a FastAPI service with lifespan-managed model loading, dependency-injected services, correct status codes, health vs readiness endpoints, and explain URI versioning trade-offs.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Design a prediction API contract: nouns, verbs, status codes, error envelope | LO1 |
| 2.2 | Implement strict request/response validation with pydantic v2 | LO1, LO5 |
| 2.3 | Manage model lifecycle with FastAPI lifespan + dependency injection | LO1, LO5 |
| 2.4 | Distinguish liveness from readiness and implement both | LO1, LO2 |
| 2.5 | Version an API and evolve a schema without breaking consumers | LO1 |

## Technical Content

### 1. Designing the prediction contract

A model endpoint is just a resource — design it like one:

- **`POST /v1/predictions`** (or `/v1/predict`): POST because scoring is neither safe nor idempotent-by-URL; the request body is the resource being created (a prediction).
- **Batch variant** `POST /v1/predictions:batch` accepting up to N items — decide N (e.g., 256) explicitly and document it; unbounded batch endpoints are self-inflicted DoS.
- **Sync vs async:** if inference p99 < ~1 s, synchronous is right. Longer (LLMs, video) → return `202 Accepted` + job resource (`GET /v1/jobs/{id}`) or stream. State this decision rule; practitioners otherwise cargo-cult one pattern.

**Status-code discipline** (participants memorise this table):

| Situation | Code | Body |
|---|---|---|
| Valid request, scored | 200 | prediction envelope |
| Malformed JSON / schema violation | 422 (FastAPI default) | field-level errors |
| Semantically invalid (e.g., unsupported currency) | 400 | error envelope with `code` |
| Model not loaded yet / dependency down | 503 + `Retry-After` | error envelope |
| Inference exception | 500 (never leak stack trace) | error envelope with `trace_id` |
| Too many items in batch | 413 | error envelope |

**The error envelope** — one shape everywhere:

```json
{"error": {"code": "MODEL_UNAVAILABLE", "message": "Model is loading", "trace_id": "8f3a…"}}
```

Consumers write one error handler, not five. The `code` field is a stable machine contract; `message` is for humans and may change.

### 2. pydantic v2 as the API firewall

Everything crossing the boundary is validated *in* and *out*:

- Request models with constrained types (`Field(gt=0)`, `StrEnum`, length limits) reject garbage before it reaches the model — most "model bugs" in production are actually unvalidated input.
- `model_config = ConfigDict(extra="forbid")` on request schemas: unknown fields are typos or probing; reject them loudly. (Story: a client sending `amount_sr` instead of `amount_sar` for three weeks while the model scored a default value.)
- **Response models are declared too** (`response_model=PredictionResponse`): they guarantee you never leak internal fields (raw feature values, file paths) and they freeze the contract that consumers depend on.
- API schemas ≠ domain entities (Module 1): schemas adapt the wire format; entities carry meaning. Conversion happens in the route function — two lines, cheap, decoupling forever.

### 3. Model lifecycle in the app

The lifespan pattern from Module 1 gets production semantics here:

- **Load once, share safely.** The model loads in `lifespan`, stored on `app.state`. sklearn `predict` is thread-safe for reads; document this reasoning per framework (PyTorch models need `.eval()` + `torch.inference_mode()`).
- **Warm-up:** run one dummy prediction during startup so the first user doesn't pay JIT/lazy-init cost. Measure: first-call latency drops from ~900 ms to ~12 ms for the course model.
- **Fail fast vs degrade:** if the artefact is missing, crash at startup (orchestrators restart and alert) rather than serving 500s forever. If a *secondary* enrichment source is down, degrade with a flag in the response.
- **Dependency injection via `Depends`:** routes receive the scorer through a provider function — swapping it in tests becomes `app.dependency_overrides[get_scorer] = lambda: fake` (Module 4 uses exactly this).

### 4. Health, readiness, and observability hooks

- **`GET /health` (liveness):** "is the process alive?" — returns 200 with build info; does *no* I/O. Container orchestrators kill on failure.
- **`GET /ready` (readiness):** "can I serve correctly right now?" — checks model loaded (+ critical deps). Load balancers route on this. Confusing the two causes restart storms (a slow model download failing liveness gets the container killed mid-download, forever).
- Every response carries `X-Trace-Id` and `X-Model-Version` headers — trivially cheap, invaluable in incident review; wired into logging in Module 6.

### 5. Versioning and evolution

- URI versioning (`/v1/`) — visible, cache-friendly, easy to route; header versioning is cleaner in theory but invisible in logs and curl.
- **Additive changes are free** (new optional response field); **breaking changes require a new version** (removed field, changed semantics, tightened validation).
- Run v1 and v2 side by side; deprecate with `Deprecation` + `Sunset` headers and consumer comms; delete only after traffic hits zero. Model version ≠ API version: swapping v3→v4 of the model behind `/v1/predictions` is fine **if** the contract and score semantics hold; renamed decision categories are an API change.

### 6. Common mistakes & production considerations

1. Returning raw model outputs (`[0.9731]`) with no envelope, no version, no trace id.
2. `def` routes doing CPU-bound inference declared `async` — blocks the event loop; use plain `def` (FastAPI thread-pools it) or a worker pool. This single mistake causes most "FastAPI is slow" complaints.
3. Global mutable model variable swapped at runtime without locking.
4. Validation so loose that `{"amount_sar": -1}` scores successfully.
5. Missing request size limits and timeouts (set in server config — uvicorn `--limit-max-requests`, proxy timeouts).
6. Trusting client-supplied IDs for anything security-relevant.

Production: run under `uvicorn` with multiple workers (`--workers = cores` for CPU-bound sklearn); set `--timeout-keep-alive` sensibly; put concurrency limits at the gateway; log every request with latency (M6); load-test before launch (lab uses `hey`).

## Code Examples

### API schemas (wire contract, separate from domain)

```python
# src/fraud_service/api/schemas.py
"""Wire contract. These models exist for consumers; keep them stable.
They convert to/from domain entities in routes — never leak inward."""
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from fraud_service.domain.entities import Channel, Decision, Transaction


class PredictRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")  # reject unknown fields loudly

    transaction_id: str = Field(min_length=8, max_length=64,
                                examples=["TXN-2026-00042"])
    amount_sar: float = Field(gt=0, le=1_000_000,
                              description="Transaction amount in SAR")
    channel: Channel
    merchant_category: str = Field(min_length=2, max_length=40)
    customer_id: str = Field(min_length=4, max_length=64)
    timestamp: datetime

    def to_domain(self) -> Transaction:
        return Transaction(**self.model_dump())


class PredictResponse(BaseModel):
    transaction_id: str
    fraud_probability: float = Field(ge=0, le=1)
    decision: Decision
    model_version: str
    trace_id: str


class ErrorBody(BaseModel):
    code: str          # stable machine-readable contract
    message: str       # human-readable, may change
    trace_id: str


class ErrorEnvelope(BaseModel):
    error: ErrorBody


class HealthResponse(BaseModel):
    status: str
    git_sha: str
    started_at: datetime
```

### Application factory with lifespan, DI, error envelope

```python
# src/fraud_service/api/app.py
import time
import uuid
from contextlib import asynccontextmanager
from datetime import datetime, timezone

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from fraud_service.adapters.sklearn_model import SklearnModel
from fraud_service.api.routes import router
from fraud_service.config import Settings
from fraud_service.logging_setup import configure_logging, get_logger

log = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    configure_logging(settings.log_level)

    t0 = time.perf_counter()
    model = SklearnModel.load(settings.model_path)   # fail fast if absent
    # Warm-up: pay lazy-init cost now, not on the first user request
    model.predict_proba(_warmup_features())
    log.info("model_loaded", version=model.model_version,
             seconds=round(time.perf_counter() - t0, 3))

    from fraud_service.service.scorer import FraudScorer
    app.state.scorer = FraudScorer(model=model,
                                   block_threshold=settings.block_threshold)
    app.state.started_at = datetime.now(timezone.utc)
    app.state.settings = settings
    yield
    log.info("shutdown_complete")


def create_app() -> FastAPI:
    app = FastAPI(
        title="Fraud Scoring Service",
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs",                     # OpenAPI UI — the free win of FastAPI
    )
    app.include_router(router, prefix="/v1")

    @app.middleware("http")
    async def trace_and_time(request: Request, call_next):
        trace_id = request.headers.get("X-Trace-Id", uuid.uuid4().hex[:16])
        request.state.trace_id = trace_id
        t0 = time.perf_counter()
        response = await call_next(request)
        response.headers["X-Trace-Id"] = trace_id
        response.headers["X-Response-Time-Ms"] = str(
            round((time.perf_counter() - t0) * 1000, 1))
        return response

    @app.exception_handler(Exception)
    async def unhandled(request: Request, exc: Exception):
        # Never leak stack traces to clients; always give them a trace_id
        trace_id = getattr(request.state, "trace_id", "unknown")
        log.error("unhandled_exception", trace_id=trace_id, exc_info=exc)
        return JSONResponse(status_code=500, content={"error": {
            "code": "INTERNAL_ERROR",
            "message": "Unexpected error; contact support with trace_id",
            "trace_id": trace_id}})

    return app


def _warmup_features():
    from fraud_service.domain.entities import Transaction
    return Transaction(
        transaction_id="WARMUP-0000", amount_sar=100.0, channel="pos",
        merchant_category="GROCERY", customer_id="warmup",
        timestamp=datetime.now(timezone.utc)).to_features()
```

### Routes with readiness semantics

```python
# src/fraud_service/api/routes.py
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Request

from fraud_service.api.schemas import (HealthResponse, PredictRequest,
                                       PredictResponse)
from fraud_service.service.scorer import FraudScorer

router = APIRouter()


def get_scorer(request: Request) -> FraudScorer:
    """DI seam: tests override this one function to inject fakes."""
    scorer = getattr(request.app.state, "scorer", None)
    if scorer is None:                       # startup incomplete / failed
        raise HTTPException(status_code=503, detail="Model not ready",
                            headers={"Retry-After": "5"})
    return scorer


@router.post("/predict", response_model=PredictResponse)
def predict(body: PredictRequest,                       # plain def: sklearn is
            request: Request,                            # CPU-bound; FastAPI
            scorer: FraudScorer = Depends(get_scorer)):  # runs it in a thread
    score = scorer.score(body.to_domain())
    return PredictResponse(
        transaction_id=score.transaction_id,
        fraud_probability=round(score.probability, 6),
        decision=score.decision,
        model_version=score.model_version,
        trace_id=request.state.trace_id,
    )


@router.get("/health", response_model=HealthResponse)
def health(request: Request):
    """Liveness: process is up. NO I/O here."""
    return HealthResponse(status="ok",
                          git_sha=request.app.state.settings.git_sha,
                          started_at=request.app.state.started_at)


@router.get("/ready")
def ready(request: Request):
    """Readiness: safe to receive traffic. Checks the model is loaded."""
    if getattr(request.app.state, "scorer", None) is None:
        raise HTTPException(status_code=503, detail="warming up")
    return {"status": "ready", "checked_at": datetime.now(timezone.utc)}
```

## Hands-on Lab 2 — Build and Harden the Prediction API

| | |
|---|---|
| **Objective** | Expose the Lab 1 scorer as a FastAPI service with validation, error envelope, health/readiness, trace headers; verify with OpenAPI UI and a load test |
| **Duration** | 2 × 50 min (Day 1 H5 + Day 2 H1) |
| **Setup** | Lab 1 solution (`git checkout lab2-start`), `pip install "fastapi[standard]" uvicorn httpx hey` (hey binary provided) |

**Part A tasks (50 min)**
1. Implement `schemas.py` exactly per the contract table (10 min).
2. Implement `app.py` factory + lifespan + middleware (15 min).
3. Implement `/v1/predict`, `/v1/health`, `/v1/ready` (15 min).
4. Run `fastapi dev src/fraud_service/api/app.py` → exercise via `/docs`: one valid request, one negative amount, one unknown field (10 min).

**Part B tasks (50 min)**
1. Add warm-up call; measure first-request latency before/after with `curl -w "%{time_total}"` (15 min).
2. Add the global exception handler; prove no stack trace leaks by injecting `raise RuntimeError` behind a temporary `/v1/boom` route, then remove it (10 min).
3. Load test: `hey -n 2000 -c 25 -m POST -D sample.json -T application/json http://localhost:8000/v1/predict`; record p50/p99/RPS into `BENCHMARKS.md` (15 min).
4. Commit: `feat(api): prediction endpoint with validation, health, tracing` (10 min).

**Expected outputs**
```
$ curl -s localhost:8000/v1/predict -d @sample.json -H "content-type: application/json"
{"transaction_id":"TXN-2026-00042","fraud_probability":0.031742,
 "decision":"allow","model_version":"v3.2.0","trace_id":"a1b2c3d4e5f60718"}

hey summary (reference laptop): p50 ≈ 9 ms, p99 ≈ 38 ms, ≈ 1400 req/s, 0 non-2xx
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| First request ~1 s, rest fast | No warm-up | Confirm warm-up runs in lifespan (check startup log line) |
| RPS collapses at concurrency 25 | Route declared `async def` around sklearn call | Change to `def`; explain event-loop blocking on whiteboard |
| 422 on valid-looking JSON | `extra="forbid"` + typo field | Read the 422 body — it names the field; this is the feature working |
| `/ready` 200 before model loaded | Scorer set before load completes | Set `app.state.scorer` only after warm-up |

**Instructor notes.** The async/def trap is the highest-value teachable moment of Day 1 — let one pair hit it naturally, then debug it on the projector. Keep `hey` results from each pair; reuse them in Module 3 to compare container vs bare-metal latency.

## Mini Exercises

**Quiz.** (1) Which code for "model still loading"? → 503 + Retry-After. (2) Why plain `def` for sklearn inference routes? → CPU-bound work would block the event loop in `async def`; thread pool handles it. (3) What does `extra="forbid"` protect against? → typo'd/probing fields silently ignored. (4) Liveness vs readiness in one sentence each. (5) Which changes are non-breaking? adding optional response field ✔ / renaming `fraud_probability` ✘ / widening enum accepted on input ✔ (with care).

**Debugging exercise.** Branch `sim-async-block`: predict route is `async def`, load test shows p99 = 2.4 s. Participants must diagnose with `hey` + `py-spy dump` and fix. 

**Code-review exercise.** Review a PR that returns domain `FraudScore` directly from the route (schema leakage), uses 200 for errors with `{"success": false}`, and logs full request bodies (PII). Find all three.

**Discussion.** Where should authentication live — this service or the gateway? What changes for an internal vs external API?

## Case Study — Medical Triage AI Behind Three Hospital Systems

**Scenario.** A Riyadh health-tech provider serves a triage-priority model to three hospital EMR vendors. Vendor A sends ISO-8601 timestamps, Vendor B sends epoch millis, Vendor C sends `dd/mm/yyyy`. Two integrations silently mis-parse dates; night-shift admissions (when `hour_of_day` matters most) are mis-scored for six weeks.

**Business context.** Patient-safety incident review + regulator (SFDA-adjacent digital health oversight) demands evidence of input validation and versioned contracts within 30 days.

**Technical challenge.** Design a single strict contract that all three vendors can meet, migrate them without downtime, and prove rejection of malformed input.

**Constraints.** Hospital release cycles are 6–12 weeks; the provider cannot force simultaneous upgrades; every rejected request must be auditable (who sent what, when); Arabic patient names must round-trip UTF-8 intact.

**Solution approach.** Publish `/v2/triage` with strict pydantic contract (single timestamp format, `extra="forbid"`); keep `/v1` alive with per-vendor adapters that normalise and *warn*; per-vendor API keys → per-vendor error dashboards; `Sunset` header + weekly conformance report to each vendor; contract tests shared with vendors as a public test suite (Module 4 tie-in).

**Discussion questions.** (1) Strict-reject vs normalise-and-warn during migration — where's the line in a safety-critical system? (2) Should the error envelope include the offending value when it may contain PII? (3) Design the conformance report: which 5 metrics per vendor?

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| p50 / p99 latency `/v1/predict` | Performance | ≤ 15 ms / ≤ 50 ms (local) | `hey`, response-time header |
| Throughput @ c=25 | Performance | ≥ 1,000 req/s | `hey` |
| First-request latency (cold) | Reliability | ≤ 50 ms (post warm-up) | curl timing |
| Non-2xx under load | Reliability | 0 (valid traffic) | `hey` summary |
| Invalid-input rejection rate | Reliability | 100% of malformed corpus → 4xx | validation test corpus (40 cases) |
| Contract coverage | Code quality | 100% routes with `response_model` | ruff custom check / review |
| OpenAPI completeness | Code quality | All fields described + examples | `/docs` review checklist |

**Example benchmark table:**

| Configuration | p50 | p99 | RPS | non-2xx |
|---|---|---|---|---|
| `async def` route (bug) | 210 ms | 2,400 ms | 118 | 0.4% timeouts |
| `def` route | 9 ms | 38 ms | 1,410 | 0 |
| `def` + 4 uvicorn workers | 8 ms | 24 ms | 4,050 | 0 |

## Required Visuals and Training Assets

### Diagrams
1. **API request–response flow** — *Purpose:* one image of the whole path. *Elements:* client → middleware (trace id) → validation (pydantic wall icon) → DI provider → FraudScorer → model adapter → response with headers; side lanes for 422 and 503 exits. *Style:* horizontal swim-lane, colour-coded happy path vs error exits. *Designer note:* show the 422 exiting *before* the scorer — validation as firewall.
2. **Liveness vs readiness state diagram** — *Elements:* container states (starting → loading model → ready → serving → draining) with which endpoint returns what in each state; orchestrator actions annotated. *Style:* state machine with traffic-light colours.
3. **Versioning timeline** — *Elements:* /v1 and /v2 lanes over time, deprecation window, Sunset header event, traffic curves shifting. *Style:* Gantt-like strip.
4. **Sync vs async serving decision tree** — *Elements:* latency thresholds branching into sync / 202+job / streaming. *Style:* simple flowchart, 6 nodes.

### Images
1. **OpenAPI `/docs` screenshot** with `POST /v1/predict` expanded — *why:* participants verify their UI matches; *content:* schema with constraints visible, example filled, 200/422/503 documented.
2. **Terminal screenshot of `hey` output** — *why:* reference numbers for lab; *content:* latency histogram + RPS from the reference solution.
3. **422 response in HTTPie/curl** — *why:* show field-level error quality; *content:* response naming `amount_sar` constraint violation.
4. **VS Code screenshot: route + schema side by side** — *why:* reinforce contract/domain separation; *content:* `schemas.py` and `routes.py` split view with `to_domain()` highlighted.

### Simulations
1. **Model-not-ready storm** — *Setup:* start API with `MODEL_PATH` pointing to a 60-second-delayed network mount (script provided); send traffic immediately. *Expected:* `/ready` 503 until load completes; `/v1/predict` returns envelope with Retry-After; no 500s. *Learning objective:* readiness protects consumers during startup.
2. **API timeout under event-loop blocking** — *Setup:* branch `sim-async-block` (async route). *Expected:* p99 explodes at c≥20; `X-Response-Time-Ms` reveals queuing. *Learning objective:* concurrency model of FastAPI; diagnosing with load tools.
3. **Schema-probing attack replay** — *Setup:* script fires 25 malformed/probing payloads (SQL-ish strings, huge arrays, unknown fields). *Expected:* all rejected 4xx, zero reach the scorer (assert via log grep). *Learning objective:* validation as security control.

### Interactive Activities
- **Contract-design workshop (15 min):** groups design the batch endpoint contract (limits, partial-failure semantics: 200-with-item-errors vs 207) then defend choices.
- **Peer API review:** pairs exercise each other's `/docs` and file one issue against the contract checklist.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `sample.json` + `payloads/valid/*.json` | Course repo | JSON | 20 files | Manual + load testing |
| `payloads/malformed/*.json` | Course repo (crafted) | JSON | 40 files | Validation & security exercise |
| `hey` load profile | Course repo script | shell | — | Reproducible benchmarks |

### Demo Requirements
- **Instructor demo:** from empty route file to working `/v1/predict` via `/docs` in 10 minutes, narrating each decision; then live demo of the async trap with `hey` (rehearsed).
- **Student demo:** one pair presents their 422 corpus results; one pair presents load-test numbers vs reference.
- **Expected outputs:** all participants have `BENCHMARKS.md` v1 committed by end of Day 2 H1.

---

# Module 3 — Docker and Containerised Services

## Module Overview

**Purpose.** "It works on my machine" is fatal for AI services because they couple code to heavyweight, version-sensitive numerical stacks. Containers freeze the entire runtime — OS libraries, Python, BLAS, model dependencies — into an immutable, shippable artefact. This module teaches image building as an engineering discipline: layer caching, multi-stage builds, size and security hygiene, compose-based local orchestration, and container-level health.

**Business relevance.** Containers are the deployment currency of every serious platform — on-prem OpenShift in Saudi banks, managed Kubernetes in STC/ Aramco-scale clouds, or serverless container platforms. An AI team that hands over a clean image with a healthcheck integrates in days; a team that hands over "a conda env and a README" integrates in months. Image size and startup time directly translate into autoscaling cost and incident recovery speed.

**Industry use cases.**
- Computer-vision quality-inspection service deployed to factory edge boxes — image must be < 1 GB and start < 10 s on modest hardware.
- Fraud scorer autoscaling during salary-day traffic spikes: container startup time bounds scale-out reaction.
- A hospital deploys the same triage image, byte-identical, in two isolated networks — reproducibility as compliance evidence.

**Expected competencies.** Write multi-stage Dockerfiles for Python ML services, control build context and caching, run non-root, wire healthchecks, compose multi-service dev stacks, and measure image size/startup/latency.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Explain images, layers, containers, registries, and the build cache | LO2 |
| 3.2 | Author a multi-stage Dockerfile for the fraud service (slim, non-root, healthchecked) | LO2 |
| 3.3 | Use `.dockerignore` and layer ordering to achieve < 30 s warm rebuilds | LO2 |
| 3.4 | Orchestrate service + dependencies locally with docker compose | LO2 |
| 3.5 | Benchmark image size, startup time, and containerised latency | LO2, LO6 |

## Technical Content

### 1. Mental model: images, layers, containers

An **image** is a stack of read-only filesystem layers plus metadata (env, entrypoint, exposed ports). A **container** is an image plus a thin writable layer and a process. A **registry** stores and distributes images by content digest — `fraud-service@sha256:…` is immutable truth; tags (`:1.4.2`, `:latest`) are movable pointers. Production systems pin digests or immutable tags; `latest` in production is an anti-pattern because "what is running?" becomes unanswerable.

**Layer caching is the economics of Docker.** Each Dockerfile instruction creates a layer; a layer rebuilds only if its inputs (the instruction + the files it copies + all previous layers) changed. Therefore the golden ordering rule for Python services:

1. copy dependency manifests only → install dependencies (slow, rarely changes)
2. copy source code (fast, changes every commit)
3. copy models/assets as their own layer (changes on retrain, not on code change)

Violating this (COPY . . before pip install) forces a full dependency reinstall on every code edit — the single most common Dockerfile mistake, and it turns 25-second rebuilds into 8-minute rebuilds.

### 2. Multi-stage builds for ML

ML images bloat: compilers, build headers, pip caches, test files. Multi-stage builds separate the *build* environment from the *runtime* environment:

- **Stage 1 (builder):** full toolchain; resolve and install dependencies into a virtualenv or wheels directory.
- **Stage 2 (runtime):** `python:3.12-slim`; copy only the virtualenv and `src/`; no compilers, no pip cache, no tests.

Typical result for the fraud service: 2.4 GB naive → **410 MB** multi-stage slim. For GPU services the same pattern applies with CUDA base images, and the size stakes are 10×.

Size matters operationally, not aesthetically: pull time on cold nodes (autoscaling latency), registry storage cost, attack surface (every binary in the image is a CVE candidate — scanners like `trivy` report per-layer).

### 3. Runtime hygiene

- **Non-root user.** Create `appuser`; `USER appuser` before CMD. Root-in-container escapes are the first thing any security review flags.
- **Deterministic installs.** `pip install --no-cache-dir -r requirements.lock` (or `uv sync --frozen`). Lock files inside images = reproducible images.
- **Model artefacts:** three patterns with trade-offs — (a) *baked into the image* (simple, immutable, image per model version — course default); (b) *volume-mounted* (fast iteration, but image no longer self-contained); (c) *pulled at startup from a registry* (decouples model and code release — requires readiness gating; production pattern for large models). Teach (a), demonstrate (b) in compose, describe (c) as the bridge to MLOps modules.
- **`HEALTHCHECK`** hitting `/ready` (not `/health`) so `docker ps` and compose dependencies reflect actual serviceability.
- **Signals:** run uvicorn as PID 1 via exec-form CMD so SIGTERM reaches it and graceful shutdown works; demonstrate `docker stop` timing with/without exec form.
- **ENV discipline:** configuration enters as environment variables (12-factor); never bake secrets into layers — `docker history` exposes them forever (live demo).

### 4. docker compose for the dev stack

Compose is the local production simulator: the fraud service + Redis feature cache + a mock downstream consumer, one command. Key concepts: service definitions, healthcheck-gated `depends_on: condition: service_healthy`, named volumes, networks, `env_file`, and profile-based optional services (e.g., `--profile loadtest` adds a hey container). Compose is also the contract for "how do I run this thing?" — a new joiner types `docker compose up` and has the full stack.

### 5. Common mistakes & production considerations

1. `COPY . .` before dependency install (cache destruction).
2. No `.dockerignore` → 1.2 GB build context including `.git`, datasets, venvs; slow builds and accidental secret inclusion.
3. `latest` tags in deployment manifests.
4. conda inside containers when pip suffices — doubles size and build time for typical serving deps.
5. Healthcheck hitting `/health` (liveness) and masking not-ready containers.
6. Baking `.env` files or AWS keys into images (`docker history` demo makes this visceral).
7. Ignoring platform: Apple-Silicon participants must build `--platform linux/amd64` for x86 targets or use multi-arch builds; surface this early — it derails labs otherwise.

Production: image scanning (trivy) in CI (Module 5 wires it); read-only root filesystem where possible; resource limits (`--memory`, `--cpus`) and the OOM-kill behaviour of memory-hungry inference; log to stdout/stderr only (Module 6).

## Code Examples

### Production Dockerfile (multi-stage, non-root, healthchecked)

```dockerfile
# ---------- Stage 1: builder ----------
FROM python:3.12-slim AS builder

# System deps needed only to BUILD wheels (never ship these)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 1) Dependency layer: changes rarely => cached across code edits
COPY requirements.lock .
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.lock

# 2) Source layer: changes every commit, cheap to rebuild
COPY pyproject.toml README.md ./
COPY src/ src/
RUN /opt/venv/bin/pip install --no-cache-dir --no-deps .

# ---------- Stage 2: runtime ----------
FROM python:3.12-slim AS runtime

# Non-root user: first thing any security review checks
RUN useradd --create-home --uid 10001 appuser

# curl only for the container healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/venv /opt/venv

# 3) Model layer: separate from code so a retrain doesn't invalidate src cache
COPY models/fraud_xgb_v3.joblib /models/fraud_xgb_v3.joblib

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    MODEL_PATH=/models/fraud_xgb_v3.joblib

USER appuser
EXPOSE 8000

# Readiness-based healthcheck: /ready, not /health
HEALTHCHECK --interval=10s --timeout=3s --start-period=20s --retries=3 \
    CMD curl -fsS http://localhost:8000/v1/ready || exit 1

# Exec form => uvicorn is PID 1 => receives SIGTERM => graceful shutdown
CMD ["uvicorn", "fraud_service.api.app:create_app", "--factory", \
     "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
```

### .dockerignore

```gitignore
# Build context hygiene: what Docker never needs to see
.git
.venv
__pycache__/
*.pyc
tests/
data/
notebooks/
.env            # CRITICAL: secrets must never enter the build context
*.md
!README.md
.github/
.pytest_cache
.ruff_cache
```

### docker-compose.yml (dev stack)

```yaml
services:
  fraud-api:
    build:
      context: .
      dockerfile: Dockerfile
    image: fraud-service:dev
    ports:
      - "8000:8000"
    env_file: configs/dev.env          # non-secret dev config
    environment:
      REDIS_URL: redis://feature-cache:6379/0
    depends_on:
      feature-cache:
        condition: service_healthy     # gate on REAL readiness, not "started"
    healthcheck:
      test: ["CMD", "curl", "-fsS", "http://localhost:8000/v1/ready"]
      interval: 10s
      timeout: 3s
      start_period: 20s
      retries: 3
    deploy:
      resources:
        limits:
          memory: 512M                 # discover OOM behaviour in dev, not prod

  feature-cache:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 2s
      retries: 5
    volumes:
      - cache-data:/data

  loadtest:                            # optional: docker compose --profile loadtest up
    profiles: ["loadtest"]
    image: williamyeh/hey
    command: ["-n", "2000", "-c", "25", "-m", "POST",
              "-D", "/payloads/sample.json", "-T", "application/json",
              "http://fraud-api:8000/v1/predict"]
    volumes:
      - ./payloads:/payloads:ro
    depends_on:
      fraud-api:
        condition: service_healthy

volumes:
  cache-data:
```

### Makefile additions

```makefile
IMAGE := fraud-service
TAG   := $(shell git rev-parse --short HEAD)

image:                        ## Build production image tagged with git SHA
	docker build -t $(IMAGE):$(TAG) -t $(IMAGE):dev .

image-size: image             ## Report image size (course benchmark)
	docker images $(IMAGE):$(TAG) --format "{{.Repository}}:{{.Tag}} {{.Size}}"

up:                           ## Full dev stack
	docker compose up --build -d && docker compose ps

smoke: up                     ## End-to-end smoke test against the container
	sleep 2 && curl -fsS localhost:8000/v1/ready \
	&& curl -fsS localhost:8000/v1/predict -d @payloads/sample.json \
	     -H "content-type: application/json" | python -m json.tool
```

## Hands-on Lab 3 — Containerise the Fraud Service

| | |
|---|---|
| **Objective** | Produce a slim, non-root, healthchecked image and a compose stack; measure size, startup, and containerised latency |
| **Duration** | 50 minutes |
| **Setup** | Lab 2 solution; Docker Desktop/Colima running; `git checkout lab3-start` |

**Tasks**
1. *(5 min)* Write `.dockerignore` first; run `docker build` with a deliberate `COPY . .` naive Dockerfile (provided) and record build time + image size.
2. *(15 min)* Author the multi-stage Dockerfile per template; build; record size (`make image-size`).
3. *(5 min)* Prove cache discipline: edit one line in `routes.py`, rebuild, confirm rebuild < 30 s and dependency layer cache-hit.
4. *(10 min)* Write `docker-compose.yml` with Redis + healthcheck gating; `make up`; verify `docker compose ps` shows `healthy`.
5. *(10 min)* Run `make smoke`; then `docker compose --profile loadtest up loadtest` and compare p99 vs bare-metal Lab 2 numbers in `BENCHMARKS.md`.
6. *(5 min)* Measure startup: `docker events` or timing script `scripts/startup_time.sh`; record time-to-ready. Commit.

**Expected outputs**
```
naive image:      2.41 GB, build 6m12s
multi-stage:      412 MB,  cold build 3m05s, warm rebuild 22s
time-to-ready:    6.8 s (start_period covers model load)
container p99:    41 ms  (vs 38 ms bare-metal — overhead ≈ nil)
docker compose ps: fraud-api (healthy), feature-cache (healthy)
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Build context "sending 1.2 GB" | Missing `.dockerignore` | Add it; rebuild; compare |
| `exec format error` on run | Apple Silicon image on x86 or vice versa | `docker build --platform linux/amd64` or run natively |
| Container `unhealthy` | Healthcheck hits `/ready` before model loads | Increase `start-period`; check logs `docker logs` |
| `PermissionError` writing logs | Non-root user + baked path | Log to stdout only (Module 6 rule) |
| OOM-killed under load test | 512M limit + 2 workers | Discuss memory per worker; raise limit or drop to 1 worker — this is a *feature* of the lab |

**Instructor notes.** The naive-vs-multi-stage size delta is the module's money shot — have every pair post their two numbers to the shared board. The OOM under memory limit is seeded intentionally for at least the pairs that keep 2 workers; use it to teach memory sizing = model size × workers + overhead. Fast finishers: add `trivy image` scan and triage the top CVE.

## Mini Exercises

**Quiz.** (1) Why does `COPY . .` before `pip install` destroy caching? (2) What does exec-form CMD change about signals? (3) Healthcheck: `/health` or `/ready`, and why? (4) Name two reasons image size matters operationally. (5) Where do secrets enter a container correctly? → runtime env/secret store, never build args or layers.

**Debugging exercise.** Branch `sim-secret-leak`: a `.env` was COPY'd into an intermediate layer then "deleted". Participants use `docker history` + `docker save | tar` to prove the secret is still extractable, then fix with `.dockerignore` + runtime env.

**Code-review exercise.** Review a Dockerfile PR: `FROM python:latest`, root user, `pip install` without lock, ADD of a URL, healthcheck via `ps aux | grep uvicorn`. Five findings expected.

**Discussion.** Bake the model vs pull at startup for a 6 GB LLM checkpoint — walk through autoscaling, rollback, and registry-cost implications.

## Case Study — Computer-Vision Inspection at a Jubail Manufacturing Plant

**Scenario.** A defect-detection CNN must run on 14 edge servers inside a plant network with no internet, 4-hour maintenance windows, and a 30-minute cellular backhaul for updates.

**Business context.** Each false-negative batch costs ~SAR 40k in downstream rework; each hour of line stoppage costs more. IT mandates that updates be atomic and reversible.

**Technical challenge.** Current deployment is "SSH + git pull + conda env update" — 40 minutes per box, frequently divergent environments, no rollback. Move to image-based deployment within the constraints.

**Constraints.** 1.9 GB CUDA runtime baseline; 30-min transfer window (≈ 900 MB budget over the link); no external registry reachable from the plant; operators are technicians, not engineers.

**Solution approach.** Multi-stage CUDA image with aggressive pruning (strip dev toolchain, ship ONNX runtime instead of full PyTorch → 780 MB); in-plant registry mirror seeded during maintenance windows; digest-pinned deploys via compose file swap; rollback = re-point tag to previous digest (seconds); healthcheck-gated cutover script; model baked into image (pattern a) because atomicity beats flexibility here.

**Discussion questions.** (1) Why does ONNX runtime beat "just prune PyTorch" for the size budget? (2) Design the rollback runbook a technician can execute at 02:00. (3) What breaks if someone deploys `:latest` here? (4) When would pattern (c) (pull-at-start) become the right choice despite the constraints?

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| Image size (runtime stage) | Deployment | ≤ 450 MB | `docker images` |
| Cold build / warm rebuild | Deployment | ≤ 4 min / ≤ 30 s | CI timings, stopwatch |
| Container time-to-ready | Deployment | ≤ 10 s | startup script / events |
| Containerised p99 latency | Performance | ≤ 1.15 × bare-metal | hey via compose |
| Memory at steady load | Scalability | ≤ 512 MB (1 worker) | `docker stats` |
| High/critical CVEs | Reliability | 0 high in final image | `trivy image` |
| Non-root verified | Reliability | `whoami` = appuser | exec check in CI |

**Example benchmark table:**

| Image variant | Size | Cold build | Warm rebuild | Time-to-ready | p99 |
|---|---|---|---|---|---|
| Naive single-stage | 2.41 GB | 6m12s | 5m40s | 9.1 s | 43 ms |
| Multi-stage slim | 412 MB | 3m05s | 22 s | 6.8 s | 41 ms |
| + ONNX (stretch) | 264 MB | 2m20s | 19 s | 4.2 s | 33 ms |

## Required Visuals and Training Assets

### Diagrams
1. **Container lifecycle diagram** — *Purpose:* shared vocabulary for build→ship→run. *Elements:* Dockerfile → image (layer stack drawn as slices) → registry (digest) → container (writable layer + process) → stopped/removed; cache arrows on the build side. *Style:* left-to-right pipeline with an exploded layer-stack inset. *Designer note:* label the three course layers (deps/src/model) in distinct colours reused from Module 1 palette.
2. **Multi-stage build flow** — *Elements:* builder stage box (toolchain icons) with only `/opt/venv` arrow crossing to runtime stage box; crossed-out items (compilers, caches, tests) left behind. *Style:* two rooms with a narrow door; "what crosses the door" annotated.
3. **Layer-cache decision chart** — *Elements:* Dockerfile instructions as rows; "changed? → rebuild from here" arrows. *Style:* table-flow hybrid, printable.
4. **Compose dev-stack topology** — *Elements:* fraud-api, redis, loadtest profile, network boundary, healthcheck gates on dependency edges, volume cylinder. *Style:* standard container topology icons.

### Images
1. **Docker Desktop / `docker images` screenshot** showing naive vs multi-stage sizes side by side — *why:* the before/after anchor; *content:* both tags with sizes visible.
2. **Terminal screenshot of a warm rebuild** — *why:* cache-hit literacy; *content:* `CACHED` lines on dependency layers, rebuild total < 30 s.
3. **`docker compose ps` screenshot** — *why:* healthy-state reference; *content:* both services `(healthy)`.
4. **`docker history` screenshot on the leaked-secret image** — *why:* makes secret-in-layer risk concrete; *content:* layer with `.env` COPY visible.
5. **`docker stats` under load** — *why:* memory sizing discussion; *content:* fraud-api at ~430MiB/512MiB during load test.

### Simulations
1. **Container crash-loop** — *Setup:* run image with `MODEL_PATH=/models/missing.joblib`. *Expected:* fail-fast exit, compose restart policy loops, `docker compose ps` shows restarting; logs show clean fatal message. *Learning objective:* fail-fast + orchestrator restart beats limping.
2. **OOM kill under load** — *Setup:* 512M limit, 2 workers, loadtest profile. *Expected:* worker killed (exit 137), latency spike, recovery. *Learning objective:* memory limits, exit codes, sizing formula.
3. **Unhealthy dependency gating** — *Setup:* stop redis mid-run (`docker compose stop feature-cache`). *Expected:* fraud-api stays up (cache optional, degraded flag true) — connects to M2 degrade-vs-fail design. *Learning objective:* blast-radius thinking at the container level.

### Interactive Activities
- **Dockerfile golf (15 min):** pairs get the naive Dockerfile and compete for smallest working image; leaderboard on the shared board; winners explain their cuts.
- **Troubleshooting workshop:** rotate three broken-container stations (bad platform, bad healthcheck, secret leak); 7 minutes per station, written diagnosis required.

### Datasets
Same fraud artefacts as M1/M2, plus `payloads/` corpus; no new datasets — reinforces the golden thread.

### Demo Requirements
- **Instructor demo:** live multi-stage build with running commentary of cache hits; `docker stop` graceful-shutdown timing with shell-form vs exec-form CMD.
- **Student demo:** two pairs present their `BENCHMARKS.md` container-vs-bare-metal table.
- **Expected outputs:** every participant has image + compose stack passing `make smoke` before Day 2 H4.

---

# Module 4 — Testing Strategies for ML Code

## Module Overview

**Purpose.** ML systems fail differently from ordinary software: they can be *wrong while running perfectly*. This module builds a testing practice that catches both classic defects (broken code) and ML-specific defects (broken behaviour): unit tests for logic, integration tests for the API surface, and model-behaviour tests (invariance, directional expectation, golden files) for the model itself — all in pytest, all runnable in CI.

**Business relevance.** Untested AI services turn every deploy into a bet. Behavioural test suites are increasingly demanded in model-risk reviews (banking model governance, health AI audits): they are executable documentation of what the model is *supposed* to do. Teams with real test pyramids ship daily; teams without ship quarterly, fearfully.

**Industry use cases.**
- Fraud model upgrade v3→v4: behavioural suite proves score monotonicity in amount and stability under merchant-name casing before any traffic shift.
- Customer-support LLM router: golden-file tests pin routing decisions for 200 canonical utterances across prompt changes.
- Medical triage API: contract tests shared with EMR vendors (Module 2 case study) run in both parties' CI.

**Expected competencies.** Participants can structure a pytest suite (unit/integration/behavioural), use fixtures and dependency overrides, write invariance and directional tests, manage golden files, measure coverage meaningfully, and know what *not* to test.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Structure the ML testing pyramid and place a given test correctly | LO3 |
| 4.2 | Write unit tests for domain and service layers using test doubles | LO3, LO5 |
| 4.3 | Write API integration tests with httpx + dependency overrides | LO3, LO1 |
| 4.4 | Implement invariance, directional, and golden-file model tests | LO3 |
| 4.5 | Interpret coverage reports and set defensible thresholds | LO3, LO6 |

## Technical Content

### 1. The ML testing pyramid

| Level | Question answered | Speed | Fraud-service examples |
|---|---|---|---|
| **Unit** | Is my logic right? | ms | `decide()` policy bands; `to_features()` output; schema validators |
| **Integration** | Do the pieces talk correctly? | ~100 ms | POST /v1/predict returns contract-shaped JSON; 422 corpus; readiness behaviour |
| **Model-behaviour** | Does the model act as intended? | s | monotonicity in amount; casing invariance; golden 5k scores; performance floor on holdout |
| **(E2E/smoke)** | Does the shipped artefact work? | s–min | `make smoke` against the built container (Module 3/5) |

Two rules of placement: test a thing at the *lowest* level that can catch its failure; and the suite that runs on every commit must finish in minutes — heavyweight retraining evaluations belong to scheduled jobs, not the commit gate.

**What not to unit test:** the ML framework itself (sklearn's math), pydantic's validation engine, or exact float equality on probabilities (use tolerances / golden files with `pytest.approx`).

### 2. Unit testing the layers (payoff of Module 1)

Because `FraudScorer` depends on a `Model` protocol, unit tests are trivial:

- `ConstantModel(p)` double drives every policy branch without touching sklearn.
- Domain functions are pure — property-style tests (e.g., every probability in [0,1] maps to exactly one decision; decision boundaries are inclusive as specified) cost minutes and document business rules.
- Feature logic gets *table-driven* tests: input transaction → expected feature dict, including the nasty cases (midnight hours, Arabic merchant strings, amount = 0.01).

### 3. Integration testing the API

`TestClient`/`httpx.AsyncClient` against `create_app()` with `dependency_overrides[get_scorer]` injecting a fake — no model file, no network, ~50 ms per test:

- Contract tests: response shape, headers (`X-Trace-Id`), status codes for the malformed corpus (reuse `payloads/malformed/` from M2 — 40 assertions in one parametrised test).
- Readiness tests: app factory started *without* scorer → `/ready` 503, `/v1/predict` 503 + Retry-After.
- Error-envelope test: forced exception → 500 body matches `ErrorEnvelope`, no stack trace text present.

One *real-model* integration test (marked `@pytest.mark.slow`) loads the actual joblib artefact and scores one known row — this is the training/serving-skew tripwire.

### 4. Model-behaviour testing (the ML-specific art)

- **Invariance tests:** prediction must not change under transformations that are semantically neutral — merchant category casing/whitespace, transaction_id value, customer_id hashing. Each invariance encodes a fairness/robustness claim; make the class list them for the fraud domain and debate them (does *channel* invariance make sense? No — that's signal, not noise. This debate is the learning).
- **Directional expectation tests:** all else equal, a 100× amount increase must not *decrease* fraud probability; 3 a.m. vs 3 p.m. must move it the direction risk officers expect. Tolerance-based, not exact.
- **Golden-file tests:** score the 5k reference set, compare to `golden_scores_v3.csv` within `atol=1e-6`; any diff = skew or unintended model change. Golden files are versioned *with* the model artefact; regenerating them is a deliberate, reviewed act (`make regen-golden` + PR).
- **Performance-floor tests:** AUC on the frozen holdout ≥ 0.92; runs in the `slow` marker set / nightly, not per-commit.
- **Contract with the future:** when v4 arrives, the behavioural suite is the acceptance gate — Module 5 wires exactly this into CI.

### 5. Fixtures, markers, and suite architecture

- `conftest.py` provides: `app` (factory with overrides), `client`, `constant_model`, `sample_txn`, and a session-scoped `real_model` for slow tests.
- Markers: `unit`, `integration`, `behavioural`, `slow`; CI runs `-m "not slow"` per commit and everything nightly.
- Coverage: `pytest-cov` with **branch coverage**, threshold 80% on `src/fraud_service/{domain,service,api}` — *exclude* the adapters' thin I/O lines rather than gaming the number; coverage is a smoke detector, not a KPI. A 100% target produces assert-free theatre tests; teach reading the *uncovered lines report* instead of the percentage.

### 6. Common mistakes & production considerations

1. Tests that re-implement the code under test (tautological asserts).
2. Loading the real model in every test module (60 s suites) — fixtures + doubles fix this.
3. Random test data without seeding → flaky failures that erode trust in the suite.
4. Golden files regenerated casually "to make CI green" — the tripwire disabled.
5. Asserting exact floats across BLAS/platform variations — use `pytest.approx`.
6. No negative-path tests: the 422/503 behaviour is *contract*, test it like one.

Production: flaky-test quarantine policy; test-data governance (synthetic only in repo — real PII never enters git); test time budget as a tracked metric (suite > 5 min per commit rots discipline).

## Code Examples

### conftest.py — the suite's composition root

```python
# tests/conftest.py
"""Shared fixtures. Mirrors the app's composition root, but wires FAKES."""
from datetime import datetime, timezone

import pytest
from fastapi.testclient import TestClient

from fraud_service.api.app import create_app
from fraud_service.api.routes import get_scorer
from fraud_service.domain.entities import FeatureVector, RawScore, Transaction
from fraud_service.service.scorer import FraudScorer


class ConstantModel:
    """Test double: returns a fixed probability. Implements the Model protocol."""
    def __init__(self, p: float, version: str = "test-1"):
        self._p, self.model_version = p, version

    def predict_proba(self, features: FeatureVector) -> RawScore:
        return RawScore(value=self._p)


@pytest.fixture
def sample_txn() -> Transaction:
    return Transaction(
        transaction_id="TXN-TEST-0001", amount_sar=250.0, channel="ecom",
        merchant_category="electronics", customer_id="CUST-77",
        timestamp=datetime(2026, 7, 5, 3, 30, tzinfo=timezone.utc))


@pytest.fixture
def client_factory():
    """Build a TestClient with an injected scorer — the DI payoff."""
    def _make(probability: float = 0.10, threshold: float = 0.85) -> TestClient:
        app = create_app()
        scorer = FraudScorer(model=ConstantModel(probability),
                             block_threshold=threshold)
        app.dependency_overrides[get_scorer] = lambda: scorer
        return TestClient(app, raise_server_exceptions=False)
    return _make


@pytest.fixture(scope="session")
def real_model():
    """Session-scoped: load the true artefact ONCE for slow/behavioural tests."""
    from pathlib import Path
    from fraud_service.adapters.sklearn_model import SklearnModel
    return SklearnModel.load(Path("models/fraud_xgb_v3.joblib"))
```

### Unit tests — policy and features

```python
# tests/unit/test_policies.py
import pytest
from fraud_service.domain.entities import Decision, RawScore
from fraud_service.domain.policies import decide

@pytest.mark.unit
@pytest.mark.parametrize("p, expected", [
    (0.849999, Decision.REVIEW),   # just under block => review band
    (0.85,     Decision.BLOCK),    # boundary is inclusive — documented rule
    (0.699999, Decision.ALLOW),    # just under review band
    (0.70,     Decision.REVIEW),
    (0.0,      Decision.ALLOW),
    (1.0,      Decision.BLOCK),
])
def test_decision_bands(p, expected):
    assert decide(RawScore(value=p), block_threshold=0.85) is expected
```

```python
# tests/unit/test_features.py
import pytest

@pytest.mark.unit
def test_feature_names_are_stable(sample_txn):
    """Feature-name drift IS training/serving skew. Freeze the contract."""
    assert set(sample_txn.to_features().values) == {
        "amount_log", "channel", "mcc", "hour_of_day", "is_night"}

@pytest.mark.unit
def test_night_flag(sample_txn):
    assert sample_txn.to_features().values["is_night"] == 1   # 03:30 is night

@pytest.mark.unit
def test_mcc_normalised_from_messy_input(sample_txn):
    txn = sample_txn.model_copy(update={"merchant_category": " electronics "})
    assert txn.to_features().values["mcc"] == "ELECTRONICS"
```

### Integration tests — the API contract

```python
# tests/integration/test_predict_api.py
import json, pathlib, pytest

MALFORMED = sorted(pathlib.Path("payloads/malformed").glob("*.json"))

@pytest.mark.integration
def test_predict_contract(client_factory, sample_txn):
    client = client_factory(probability=0.93)          # forces BLOCK
    r = client.post("/v1/predict",
                    json=json.loads(sample_txn.model_dump_json()))
    assert r.status_code == 200
    body = r.json()
    assert body["decision"] == "block"
    assert 0 <= body["fraud_probability"] <= 1
    assert r.headers["X-Trace-Id"]                      # tracing is contract too

@pytest.mark.integration
@pytest.mark.parametrize("payload_file", MALFORMED, ids=lambda p: p.stem)
def test_malformed_corpus_rejected(client_factory, payload_file):
    """40 crafted bad payloads: every one must die at the validation wall."""
    client = client_factory()
    r = client.post("/v1/predict", content=payload_file.read_bytes(),
                    headers={"content-type": "application/json"})
    assert 400 <= r.status_code < 500, payload_file.name

@pytest.mark.integration
def test_no_stack_trace_in_500(client_factory, monkeypatch, sample_txn):
    client = client_factory()
    from fraud_service.service.scorer import FraudScorer
    monkeypatch.setattr(FraudScorer, "score",
                        lambda self, t: 1/0)            # force a crash
    r = client.post("/v1/predict",
                    json=json.loads(sample_txn.model_dump_json()))
    assert r.status_code == 500
    assert "ZeroDivisionError" not in r.text            # envelope only
    assert r.json()["error"]["code"] == "INTERNAL_ERROR"
```

### Model-behaviour tests

```python
# tests/behavioural/test_model_behaviour.py
import pandas as pd
import pytest
from fraud_service.domain.entities import Transaction

pytestmark = [pytest.mark.behavioural, pytest.mark.slow]


def _score(model, txn: Transaction) -> float:
    return model.predict_proba(txn.to_features()).value


def test_invariance_to_merchant_casing(real_model, sample_txn):
    """Casing is noise, not signal. Fairness/robustness claim as a test."""
    a = _score(real_model, sample_txn)
    b = _score(real_model, sample_txn.model_copy(
        update={"merchant_category": "ELECTRONICS"}))
    assert a == pytest.approx(b, abs=1e-9)


def test_directional_amount(real_model, sample_txn):
    """All else equal, much larger amount must not LOWER fraud probability."""
    small = _score(real_model, sample_txn.model_copy(update={"amount_sar": 50.0}))
    large = _score(real_model, sample_txn.model_copy(update={"amount_sar": 50_000.0}))
    assert large >= small - 1e-6


def test_golden_scores(real_model):
    """The skew tripwire: 5k reference rows must reproduce exactly (tolerance)."""
    ref = pd.read_csv("data/golden_scores_v3.csv")
    for row in ref.itertuples():
        txn = Transaction(
            transaction_id=row.transaction_id, amount_sar=row.amount_sar,
            channel=row.channel, merchant_category=row.mcc,
            customer_id=row.customer_id, timestamp=row.timestamp)
        assert _score(real_model, txn) == pytest.approx(row.score, abs=1e-6), \
            f"skew detected at {row.transaction_id}"
```

### pytest configuration (pyproject excerpt)

```toml
[tool.pytest.ini_options]
addopts = "-q --strict-markers --cov=fraud_service --cov-branch --cov-report=term-missing"
markers = [
  "unit: fast, no I/O",
  "integration: app-level via TestClient",
  "behavioural: exercises the real model artefact",
  "slow: excluded from the per-commit gate",
]
testpaths = ["tests"]

[tool.coverage.report]
fail_under = 80
exclude_also = ["if TYPE_CHECKING:", "raise NotImplementedError"]
```

## Hands-on Lab 4 — Build the Test Suite

| | |
|---|---|
| **Objective** | Deliver a three-level pytest suite: ≥ 80% branch coverage on domain/service/api, malformed-corpus green, behavioural suite green against the real artefact |
| **Duration** | 50 minutes |
| **Setup** | Lab 3 solution; `pip install pytest pytest-cov httpx`; `git checkout lab4-start` (contains failing skeletons) |

**Tasks**
1. *(10 min)* Implement `conftest.py` fixtures (`ConstantModel`, `client_factory`).
2. *(10 min)* Complete the parametrised policy-band unit tests; run `pytest -m unit` (target < 1 s).
3. *(10 min)* Implement the malformed-corpus integration test + no-stack-trace test.
4. *(10 min)* Implement casing-invariance + amount-directional + golden-file tests; run `pytest -m "behavioural"`.
5. *(5 min)* Run full suite with coverage; read the `term-missing` report; add ONE test chosen specifically to close the most meaningful gap (not the easiest).
6. *(5 min)* Commit `test: three-level suite with behavioural tripwires`; record suite timing in `BENCHMARKS.md`.

**Expected outputs**
```
pytest -m "not slow"   → 47 passed in 3.8s, coverage 84% (branch)
pytest -m slow         → 4 passed in 21.5s   (golden file: 5,000 rows OK)
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Golden test fails on ~600 rows | Participant "improved" a feature in Lab 1 | Perfect teachable skew moment — diff features vs reference solution |
| Suite takes 90 s | Real model loaded per-test | Session-scope the fixture; verify with `--durations=10` |
| Coverage stuck at 71% | Error-envelope branch untested | The `monkeypatch` 500 test covers it — point to term-missing line numbers |
| `TestClient` raises instead of returning 500 | `raise_server_exceptions` default | Pass `raise_server_exceptions=False` (already in fixture) |

**Instructor notes.** Seed 2–3 repos with the Lab 1 feature deviation so the golden test genuinely fails somewhere in the room — a real red is worth an hour of slides. Close the hour with the "what would this suite have caught?" retrospective against the Module 1 bank story.

## Mini Exercises

**Quiz.** (1) Place these in the pyramid: threshold bands / 422 corpus / AUC floor / casing invariance. (2) Why session-scope the real-model fixture? (3) When is regenerating a golden file legitimate, and what must accompany it? (4) Branch vs line coverage — what does branch add? (5) Why is `channel` NOT a valid invariance?

**Debugging exercise.** Branch `sim-flaky`: a test uses `datetime.now()` making `is_night` time-of-day dependent. Participants must identify and fix with a frozen timestamp — then generalise the rule (no unseeded randomness/clock in tests).

**Code-review exercise.** Review a PR with a tautological test (`assert decide(...) == decide(...)`), an exact-float assert, and a test importing a private function. Three findings + suggested rewrites.

**Discussion.** Your v4 model improves AUC but fails the amount-directional test on 2% of cases. Ship, block, or renegotiate the test? Who decides — engineering or risk?

## Case Study — Customer-Support LLM Router Regression

**Scenario.** A Saudi telecom's support assistant routes utterances to 14 intent handlers using an LLM + rules hybrid. A prompt "improvement" silently re-routed 8% of billing-dispute messages to the FAQ handler; CSAT dropped for two weeks before detection.

**Business context.** 60k conversations/day; regulator requires complaint-handling SLAs; every mis-route is a delayed complaint.

**Technical challenge.** LLM outputs are non-deterministic and prompt-sensitive; classic asserts don't fit. Build a regression net that catches routing drift pre-deploy.

**Constraints.** No customer text may enter the repo (PII) — synthetic canonical utterances only; suite must run < 5 min in CI using a pinned small model / recorded responses; Arabic and English utterances both in scope.

**Solution approach.** Golden routing file: 300 synthetic canonical utterances (AR/EN) × expected handler; temperature 0 + pinned model version for the gate; tolerance policy (≥ 98% match required, diffs reported by intent); recorded-response mode (VCR-style) for fast CI, live mode nightly; every prompt change requires golden-diff review in the PR — the diff *is* the review artefact.

**Discussion questions.** (1) What belongs in the golden set for bilingual routing — and who owns adding cases? (2) 98% threshold: too strict, too loose? What data decides? (3) How does this pattern transfer back to the fraud service's v4 upgrade?

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| Per-commit suite time | Performance | ≤ 5 min (course: ≤ 30 s) | pytest `--durations`, CI timer |
| Branch coverage (domain/service/api) | Code quality | ≥ 80% | pytest-cov |
| Malformed-corpus pass rate | Reliability | 40/40 rejected | parametrised test |
| Golden-file drift | Reliability | 0 rows > 1e-6 | behavioural suite |
| Flaky-test rate | Reliability | 0 over 20 CI runs | CI history |
| Behavioural tests per model claim | Code quality | ≥ 1 test per documented claim | review checklist |

**Example benchmark table:**

| Suite slice | Tests | Time | Coverage contribution |
|---|---|---|---|
| unit | 28 | 0.9 s | domain 96%, service 91% |
| integration | 15 | 2.9 s | api 88% |
| behavioural (slow) | 4 | 21.5 s | n/a (model claims: 3/3 covered) |

## Required Visuals and Training Assets

### Diagrams
1. **ML testing pyramid** — *Purpose:* placement instinct. *Elements:* four layers with per-layer example test names from the fraud service, speed axis, "runs when" annotations (per-commit vs nightly). *Style:* classic pyramid, course palette.
2. **DI override flow in tests** — *Elements:* `create_app()` → `dependency_overrides[get_scorer]` → `ConstantModel`; mirrored against the prod wiring diagram from M1. *Style:* side-by-side prod vs test wiring.
3. **Golden-file lifecycle** — *Elements:* model v3 + golden v3 pair → proposed change → red diff → review → regenerate + version bump. *Style:* circular workflow with a human-review gate icon.
4. **Behavioural-test taxonomy** — *Elements:* invariance / directional / golden / performance-floor boxes with one fraud example each and "encodes which claim" captions. *Style:* quadrant card.

### Images
1. **pytest terminal output** (green run with markers + timing) — *why:* expected-state reference; *content:* 47 passed, marker breakdown, 3.8 s.
2. **Coverage `term-missing` screenshot** — *why:* teach reading uncovered lines, not the percentage; *content:* report with two red line ranges highlighted.
3. **A real golden-file failure screenshot** — *why:* what skew looks like; *content:* assertion diff naming a transaction id and both scores.
4. **CI test summary on GitHub PR** — *why:* connect to Module 5; *content:* checks panel with test job green, coverage comment.

### Simulations
1. **Seeded skew (golden red)** — *Setup:* instructor pushes branch changing `log1p`→`log10`. *Expected:* golden test fails with ~12% rows; unit/integration stay green. *Learning objective:* only behavioural tests catch silent skew.
2. **Broken test vs broken code** — *Setup:* branch where the *test* asserts the wrong boundary (0.85 → REVIEW). *Expected:* participants must decide which is wrong using the policy doc. *Learning objective:* tests are claims; claims need sources.
3. **Flaky clock test** — *Setup:* branch `sim-flaky` (above). *Expected:* passes at 10:00 class, fails after 18:00 (or via `libfaketime`). *Learning objective:* determinism discipline.

### Interactive Activities
- **Test-writing kata (pairs, 10 min):** given three bug reports, write the test that would have caught each — before seeing any fix.
- **Peer review of test PRs:** exchange Lab 4 branches; each pair must find one tautological or low-value test and propose a replacement.
- **"Ship or block" debate (10 min):** the v4 directional-failure scenario; two groups argue, instructor arbitrates with the model-governance lens.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `payloads/malformed/*` | Course repo | JSON | 40 files | Integration corpus (reused from M2) |
| `golden_scores_v3.csv` | Reference solution output | CSV | 5,000 rows | Golden-file tests |
| `holdout_eval.csv` | Synthetic, frozen | CSV | 10,000 rows | AUC floor (nightly) |

### Demo Requirements
- **Instructor demo:** live TDD of one policy test → one invariance test; then trigger the seeded skew and let the golden test catch it on the projector.
- **Student demo:** one pair walks through their chosen "most meaningful coverage gap" test and why.
- **Expected outputs:** all repos green on `-m "not slow"` before Day 3 begins — it becomes the CI baseline.

---

# Module 5 — CI/CD Automation with GitHub Actions

## Module Overview

**Purpose.** A pipeline is the team's automated definition of "good enough to ship." This module turns the practices of Modules 1–4 into gates that run on every change: lint, type-check, test, build the image, smoke-test the image — and ship it to a registry only when everything is green. Participants leave with a working GitHub Actions pipeline on their own repository.

**Business relevance.** Deployment frequency and change-failure rate (DORA metrics) separate high-performing engineering organisations from the rest. For AI teams the stakes are higher: a model or feature change that skips validation can silently corrupt business decisions at scale. CI is also where governance evidence is produced automatically — every merged PR carries its test log, image digest, and scan report, which is exactly what enterprise audit and national cybersecurity (ECC) controls ask for.

**Industry use cases.**
- Fraud service: merge to `main` → validated image pushed with git-SHA tag → deployment module (SDA-AIE-211) picks it up.
- LLM app team: golden-routing suite (M4 case study) as a required PR check; prompt changes physically cannot merge without a reviewed golden diff.
- Vision service at the plant (M3 case study): CI produces the digest-pinned compose file that technicians deploy.

**Expected competencies.** Author multi-job workflows with caching, understand triggers and contexts, enforce quality gates via branch protection, build/push images from CI with proper tagging, and debug failed runs efficiently.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Explain CI vs CD and the anatomy of a GitHub Actions workflow | LO4 |
| 5.2 | Implement a lint → type → test pipeline with dependency caching | LO4, LO6 |
| 5.3 | Build, smoke-test, and push a Docker image from CI with SHA tagging | LO4, LO2 |
| 5.4 | Enforce gates with branch protection and required checks | LO4, LO6 |
| 5.5 | Diagnose failed pipeline runs from logs and artefacts | LO4 |

## Technical Content

### 1. Pipeline anatomy and philosophy

**CI** answers "is this change safe to integrate?" on every push/PR. **CD** answers "is this artefact safe to release?" and either delivers it to a registry (continuous delivery — this course) or all the way to production (continuous deployment — SDA-AIE-211's business). The unit of truth between them is the **immutable image digest**: CI's last act is producing it; CD's first act is consuming it. Nothing built on a laptop ever ships.

GitHub Actions vocabulary, taught against a real run: **workflow** (YAML in `.github/workflows/`) → triggered by **events** (`push`, `pull_request`, `schedule`, `workflow_dispatch`) → runs **jobs** (isolated VMs) → each job runs **steps** (shell or reusable **actions**). Jobs run in parallel unless `needs:` orders them. **Contexts** (`github.sha`, `secrets.*`, `matrix.*`) parameterise everything.

Design principles for AI pipelines:
- **Fail fast, fail cheap:** ruff (seconds) before pytest (minutes) before docker build (minutes). Order gates by cost.
- **The commit gate must be < 10 min** or engineers stop waiting for it; move `slow`/behavioural-heavy suites to `schedule:` (nightly) and PR-label triggers.
- **Reproducibility:** pin action versions (`actions/checkout@v4`, better: full SHA for third-party actions), pin Python, use lock files. An unpinned pipeline is a supply-chain door.
- **Artefacts as evidence:** upload coverage reports, image scan results, and golden diffs — the PR becomes its own audit file.

### 2. Caching and speed engineering

- `actions/setup-python` with `cache: pip` keyed on the lock file → dependency install drops from ~90 s to ~8 s.
- Docker layer caching in CI via buildx `cache-from/cache-to: type=gha` — the M3 layer-ordering discipline is what makes this effective; the two modules are one lesson in two parts.
- Split jobs so the cheap gates report in ~1 min even while tests run: `lint` and `test` in parallel, `image` gated by `needs: [lint, test]`.

### 3. The AI-specific gates

Beyond the standard trio (lint/type/test):
1. **Behavioural gate:** `pytest -m behavioural` with the real artefact — needs the model file in CI: small artefacts via Git LFS; large via authenticated download step from a model registry (course uses LFS, the trade-off is discussed).
2. **Container smoke test:** run the built image in the job, wait for `/ready`, POST one prediction, assert contract fields — catches "works in venv, broken in image" (missing system lib, wrong path, bad CMD).
3. **Image scan:** `trivy` action failing on HIGH/CRITICAL — with a documented, expiring ignore file for accepted risks (`.trivyignore` + expiry comments), not a blanket skip.
4. **Golden-diff artifact:** on behavioural failure, upload the diff CSV so the reviewer sees *which rows* moved without rerunning anything.

### 4. Branch protection: making gates real

A pipeline without branch protection is decoration. On `main`: require PRs, require status checks `lint`, `test`, `image-smoke` to pass, require one review, forbid force-push. Result: the *repository* enforces the definition of done — new team members inherit discipline from infrastructure, not tribal memory. Discuss trade-offs: hotfix path (`workflow_dispatch` + admin bypass with logged justification), and why "temporarily disabling checks" is how the M4 telecom incident happened.

### 5. Secrets and permissions in CI

- Registry credentials via `secrets.GITHUB_TOKEN` with `permissions: packages: write` (GHCR) — no long-lived PATs.
- `permissions:` block minimal by default (`contents: read`); widen per job, not per workflow.
- Never `echo` secrets; Actions masks known secrets but not derived strings. Fork PRs don't get secrets — hence the image-push job runs only on `push` to `main`, never on `pull_request` (this asymmetry trips everyone once; teach it explicitly).

### 6. Common mistakes & production considerations

1. One mega-job (no parallelism, no fast feedback, one flaky step reruns everything).
2. `pip install` unpinned in CI → the pipeline that "randomly" breaks on dependency releases.
3. Running the full slow suite per-commit → 25-min gate → engineers merge with `--no-verify` culture.
4. Pushing `:latest` from CI (M3 lesson recurs).
5. Secrets in workflow files or committed `.env` (M6 will formalise).
6. Ignoring the difference between `pull_request` (untrusted fork context) and `push` events.

Production: runner strategy for enterprises (self-hosted runners inside the network for registry/model-store access — common in Saudi banks where GitHub-hosted runners can't reach internal systems); concurrency groups to cancel superseded runs; required-workflow policies at the org level; cost visibility (minutes per merge as a tracked number).

## Code Examples

### The course pipeline — `.github/workflows/ci.yml`

```yaml
name: ci

on:
  pull_request:                 # gates for every PR
  push:
    branches: [main]            # main additionally builds & pushes the image
  workflow_dispatch:            # manual runs for demos/hotfix rebuilds

permissions:
  contents: read                # least privilege by default

concurrency:
  group: ci-${{ github.ref }}   # cancel superseded runs on the same branch
  cancel-in-progress: true

env:
  PYTHON_VERSION: "3.12"
  IMAGE: ghcr.io/${{ github.repository }}

jobs:
  lint:                         # cheapest gate first: seconds, not minutes
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: pip
          cache-dependency-path: requirements.lock
      - run: pip install ruff mypy
      - name: Ruff (style + import rules incl. layer contracts)
        run: ruff check src tests
      - name: Mypy (type-check the seams)
        run: mypy src/fraud_service --strict

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          lfs: true             # model artefact for behavioural tests
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: pip
          cache-dependency-path: requirements.lock
      - run: pip install -r requirements.lock && pip install -e . pytest pytest-cov httpx
      - name: Fast suite (per-commit gate)
        run: pytest -m "not slow" --cov-fail-under=80
      - name: Behavioural gate (real artefact)
        run: pytest -m "behavioural and not slow" -q
      - name: Upload coverage report
        if: always()            # evidence even on failure
        uses: actions/upload-artifact@v4
        with: {name: coverage, path: htmlcov/}

  image-smoke:                  # build once, prove the ARTEFACT works
    runs-on: ubuntu-latest
    needs: [lint, test]
    steps:
      - uses: actions/checkout@v4
        with: {lfs: true}
      - uses: docker/setup-buildx-action@v3
      - name: Build (GHA layer cache)
        uses: docker/build-push-action@v6
        with:
          context: .
          load: true                          # local load for smoke test
          tags: ${{ env.IMAGE }}:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
      - name: Smoke test the container
        run: |
          docker run -d --name svc -p 8000:8000 ${{ env.IMAGE }}:${{ github.sha }}
          for i in $(seq 1 30); do
            curl -fsS localhost:8000/v1/ready && break || sleep 2
          done
          curl -fsS localhost:8000/v1/predict \
               -H "content-type: application/json" -d @payloads/sample.json \
            | python -c "import json,sys; b=json.load(sys.stdin); \
                         assert 0<=b['fraud_probability']<=1; \
                         assert b['model_version']; print('smoke OK', b['decision'])"
          docker logs svc --tail 5
      - name: Scan image (fail on HIGH/CRITICAL)
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.IMAGE }}:${{ github.sha }}
          severity: HIGH,CRITICAL
          exit-code: "1"

  publish:                      # delivery: only on main, never on PRs
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    needs: [image-smoke]
    permissions:
      contents: read
      packages: write           # scoped token for GHCR push
    steps:
      - uses: actions/checkout@v4
        with: {lfs: true}
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - name: Build and push (SHA + semver-ish channel tag)
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: |
            ${{ env.IMAGE }}:${{ github.sha }}
            ${{ env.IMAGE }}:main
          cache-from: type=gha
```

### Nightly deep validation — `.github/workflows/nightly.yml`

```yaml
name: nightly
on:
  schedule:
    - cron: "0 1 * * *"         # 04:00 AST — off-hours for the team
  workflow_dispatch:

jobs:
  full-suite:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: {lfs: true}
      - uses: actions/setup-python@v5
        with: {python-version: "3.12", cache: pip}
      - run: pip install -r requirements.lock && pip install -e . pytest
      - name: Everything, including slow behavioural + AUC floor
        run: pytest -m "" --durations=15
      - name: Upload golden diff on failure (reviewer evidence)
        if: failure()
        uses: actions/upload-artifact@v4
        with: {name: golden-diff, path: reports/golden_diff.csv}
```

### Layer-contract enforcement (ties M1 to CI)

```toml
# pyproject.toml — import-linter contract run inside the lint job
[tool.importlinter]
root_package = "fraud_service"

[[tool.importlinter.contracts]]
name = "Clean architecture layers"
type = "layers"
layers = [
    "fraud_service.api",
    "fraud_service.adapters",
    "fraud_service.service",
    "fraud_service.domain",
]
# domain imports nothing above it; violations fail CI, not code review
```

## Hands-on Lab 5 — Build the Pipeline

| | |
|---|---|
| **Objective** | Working ci.yml on the participant's own GitHub repo: parallel lint+test, image smoke, publish-on-main to GHCR; branch protection turned on; one deliberately broken PR diagnosed and fixed |
| **Duration** | 50 minutes |
| **Setup** | Personal GitHub account; Lab 4 repo pushed; GHCR enabled; `git checkout lab5-start` |

**Tasks**
1. *(10 min)* Add `ci.yml` lint + test jobs; push; watch the run; fix anything red (most participants hit a lock-file or LFS miss — intended).
2. *(10 min)* Add `image-smoke` job; confirm buildx cache makes the second run ≥ 3× faster (compare timings in the Actions UI).
3. *(10 min)* Add `publish` job; merge to `main`; verify image on GHCR with SHA tag; `docker pull` it and run `make smoke` against the *pulled* image.
4. *(10 min)* Enable branch protection (required checks: lint, test, image-smoke; 1 review). Open the provided `bad-pr` branch (contains a layer violation + a golden-breaking change) as a PR — observe it blocked; read logs; download the golden-diff artefact.
5. *(10 min)* Fix the PR properly (not by weakening tests); merge green. Record pipeline timings in `BENCHMARKS.md`.

**Expected outputs**
```
PR checks: lint ✓ (58s)  test ✓ (2m41s)  image-smoke ✓ (3m12s)
main push: + publish ✓ → ghcr.io/<user>/fraud-service:<sha>
bad-pr: lint ✗ (import-linter: api -> domain violation) ; test ✗ (golden diff 612 rows)
second run with cache: image-smoke 1m02s
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Behavioural tests: model file missing in CI | LFS not checked out | `with: lfs: true` on checkout |
| `publish` skipped on PR | The `if:` condition | Correct behaviour — teach the fork-secrets asymmetry |
| GHCR push 403 | Missing `packages: write` permission | Add job-level permissions block |
| Smoke test flaps | No readiness wait loop | The retry loop is the fix; discuss polling vs fixed sleeps |
| Runs queue forever | Org runner limits | Use `concurrency` cancel; explain runner pools |

**Instructor notes.** The blocked `bad-pr` is the emotional core of Day 3: the repo defends itself. Make one participant try to merge it in the UI and screenshot the greyed-out button for the class. Fast finishers: add the trivy step and triage one finding, or add a `workflow_dispatch` input to override coverage threshold with logged reason (governed escape hatch).

## Mini Exercises

**Quiz.** (1) Why does `publish` run only on push-to-main? (2) Order these gates and justify: docker build, ruff, pytest-fast, trivy. (3) What does `concurrency.cancel-in-progress` save? (4) Where do fork PRs differ from branch PRs? (5) What makes an image "the same one" that passed CI? → the digest.

**Debugging exercise.** A provided failing run log (screenshot set): test job green locally, red in CI with `ImportError: fraud_service`. Root cause: missing `pip install -e .` — participants must find it from the log alone in < 5 min.

**Code-review exercise.** Review a teammate's ci.yml: unpinned third-party action, secrets echoed into a debug step, slow suite on every PR, `:latest` push. Four findings.

**Discussion.** Your bank's security team forbids GitHub-hosted runners from touching the internal model registry. Redesign the pipeline: which jobs move to self-hosted runners, and what new risks appear?

## Case Study — Fraud Model v4 Rollout Gate

**Scenario.** The fraud data-science team delivers model v4 (better AUC, new gradient-boosting library). The change arrives as a PR: new artefact via LFS, updated lock file, threshold retuned from 0.85 → 0.82.

**Business context.** SAMA-style model governance requires documented evidence that behaviour changes were validated before production exposure. The release must be reviewable by a risk officer who does not read Python.

**Technical challenge.** The PR triggers: golden-file failure (expected — new model), directional tests pass, casing invariance *fails on 3 rows*, image size grows 220 MB (new library), and the smoke test passes. Decide what ships.

**Constraints.** Rollout window is Sunday 05:00; risk sign-off needs the evidence pack 48 h earlier; rollback must be single-command (digest re-pin); the previous model must stay warm for shadow comparison (SDA-AIE-211 preview).

**Solution approach.** Golden failure handled by the *governed regeneration* path: regenerate goldens in the PR, attach the diff CSV artefact + notebook summary as the risk evidence pack. The 3-row invariance failure blocks: investigation shows the new library's category encoder is case-sensitive — fixed in the feature adapter, not by deleting the test. Image growth triaged with `dive`; the new library's GPU extras excluded. Merge produces digest; deployment module consumes it.

**Discussion questions.** (1) Who has authority to regenerate golden files, and what artefacts must the PR carry? (2) Was blocking on 3/5,000 invariance rows proportionate? Construct the counter-argument. (3) Design the one-page CI evidence pack a risk officer actually reads. (4) Threshold change 0.85→0.82: code, config, or governance decision — and where does it get tested?

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| PR gate wall-clock | Performance | ≤ 10 min (course ≤ 6) | Actions UI |
| CI pass rate on main | Reliability | ≥ 95% (7-day) | Actions insights |
| Cache hit ratio (deps/layers) | Performance | ≥ 80% of runs | run logs |
| Time-to-diagnose a red run | Operability | ≤ 10 min (exercise) | lab timing |
| Image publish → pullable | Deployment | 100% digest-pinned, 0 `:latest` | registry audit |
| Flaky rerun rate | Reliability | < 2% of runs | Actions rerun stats |
| High/critical CVEs shipped | Reliability | 0 | trivy gate |

**Example benchmark table:**

| Run | lint | test | image-smoke | total (parallel) | cache |
|---|---|---|---|---|---|
| Cold (first) | 1m10s | 3m55s | 5m40s | 6m48s | miss |
| Warm PR | 0m52s | 2m41s | 1m02s | 3m20s | hit |
| bad-pr (blocked) | 0m49s ✗ | 2m45s ✗ | skipped | 2m58s | hit |

## Required Visuals and Training Assets

### Diagrams
1. **CI/CD pipeline flow** — *Purpose:* the module's anchor. *Elements:* PR event → parallel lint/test lanes → image-smoke → (main only) publish → registry digest → arrow labelled "consumed by SDA-AIE-211"; red exit paths at each gate with artefact icons (coverage, golden diff, scan report). *Style:* horizontal flow, gate icons as turnstiles, course palette. *Designer note:* visually distinguish PR-triggered vs main-only segments (dashed vs solid).
2. **Gate-cost pyramid** — *Elements:* gates ordered by cost/time with per-gate duration labels; "fail here = cheap, fail there = expensive". *Style:* funnel.
3. **Branch-protection decision map** — *Elements:* PR → required checks → review → merge; bypass path with audit-log icon. *Style:* flowchart with a locked-gate motif.
4. **Runner topology for enterprise** — *Elements:* GitHub cloud, self-hosted runners inside corporate network boundary, model registry/internal registry reachable only from inside. *Style:* network-zone diagram (relevant to Saudi enterprise deployments).

### Images
1. **Actions run summary screenshot (all green)** — *why:* target state; *content:* four jobs with timings matching the benchmark table.
2. **Blocked PR screenshot** — *why:* the payoff image; *content:* red required checks + greyed merge button + review requirement.
3. **Failing log excerpt screenshot** — *why:* log-reading skill; *content:* import-linter violation line highlighted.
4. **GHCR package page screenshot** — *why:* artefact traceability; *content:* SHA tag + digest visible.
5. **Golden-diff artefact download screenshot** — *why:* evidence-pack habit; *content:* artefact list on the failed run.

### Simulations
1. **Broken-tests PR (`bad-pr`)** — *Setup:* provided branch with layer violation + feature change. *Expected:* blocked merge; artefacts explain why. *Learning objective:* gates as enforced definition-of-done.
2. **Failed deployment (publish outage)** — *Setup:* revoke `packages: write` on a fork of the repo; merge to main. *Expected:* pipeline green through smoke, publish fails 403; participants must read permissions error and fix. *Learning objective:* least-privilege debugging.
3. **Flaky smoke test** — *Setup:* remove the readiness wait loop. *Expected:* intermittent failures across reruns; participants must identify race and restore polling. *Learning objective:* determinism in pipelines, same principle as M4's clock test.

### Interactive Activities
- **Pipeline archaeology (15 min):** groups receive three anonymised real-world ci.yml files (one good, two flawed) and rank them with justification.
- **Peer review:** exchange repos; audit each other's branch-protection settings against a 6-point checklist.

### Datasets
No new datasets; the pipeline consumes M1–M4 artefacts (model via LFS, golden CSV, malformed corpus) — by design, to demonstrate artefact flow through CI.

### Demo Requirements
- **Instructor demo:** push a one-line change live; narrate the run in real time; then attempt to merge `bad-pr` and fail publicly.
- **Student demo:** each pair shows their green main-branch run + GHCR digest by end of Hour 2.
- **Expected outputs:** everyone enters the capstone with a working pipeline — capstone grading *reads the CI history*.

---

# Module 6 — Configuration, Secrets, and Logging Practices

## Module Overview

**Purpose.** Three quiet disciplines separate operable services from mysterious ones: configuration that is typed, validated and environment-driven; secrets that never touch git or image layers; and logs that are structured events a machine can query, not prose a human must grep. This module hardens the fraud service in all three dimensions and completes the capstone architecture.

**Business relevance.** Most real incidents are configuration incidents (wrong threshold in prod, staging model in production, missing env var discovered at 02:00). Secret leakage is an existential risk — a leaked key in a git history is a breach disclosure, and under Saudi PDPL and ECC controls it is also a regulatory event. Structured logs are what make the difference between a 10-minute incident and a 4-hour one; they are also the substrate for the observability module (LLMOps track) later.

**Industry use cases.**
- The same fraud image promoted dev → staging → prod with *only* environment changing — the 12-factor promise realised.
- Trace-id-correlated logs joining API gateway, fraud service, and case-management system during a dispute investigation.
- Model-version fields in every log line enabling per-version error attribution during a canary (SDA-AIE-211 dependency).

**Expected competencies.** Typed settings with pydantic-settings and fail-fast validation; layered config without secret leakage; JSON logging with trace/model correlation fields; secret-hygiene practices including scanning and rotation basics.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Implement typed, validated configuration with pydantic-settings | LO5 |
| 6.2 | Layer configuration (defaults < file < env) and keep one image across environments | LO5, LO2 |
| 6.3 | Keep secrets out of git, images, and logs; scan and respond to leaks | LO5, LO6 |
| 6.4 | Emit structured JSON logs with trace_id and model_version correlation | LO5, LO1 |
| 6.5 | Decide what to log at which level, including what must never be logged | LO5, LO6 |

## Technical Content

### 1. Configuration as a typed contract

Configuration errors deserve the same defence as bad API input: a typed model, validated at startup, failing fast with a readable error. pydantic-settings gives exactly that:

- Every knob has a **type, default (or explicit requiredness), description, and validation rule** — `Settings()` at startup either returns a fully valid object or crashes with a field-by-field report (which the orchestrator surfaces immediately, instead of a 500 three hours later).
- **Precedence:** defaults in code < `.env`/config file < environment variables. Environment wins because that is what dev/staging/prod vary.
- **One image, many environments** (12-factor): the image from Module 3/5 is promoted unchanged; only env differs. Anything else destroys the CI guarantee ("we tested *that* image").
- Config belongs in **one module**; `os.environ` calls sprinkled through the codebase are unreviewable and untestable (Module 1's mistake #5 formally resolved).
- **What is config vs code vs data?** Threshold: config (risk-owned, changes without deploy — but changes are audited). Feature names: code (they version with the model). Model path: config. Decision-band width: code unless product owns it. Teach the question, not just answers.

### 2. Secrets: the non-negotiables

A secret is anything whose disclosure grants access: API keys, DB passwords, registry tokens, signed URLs.

- **Never in git** — including "just for now", including private repos (forks, laptops, backups multiply exposure). `.env` is in `.gitignore` from repo birth (M1) and in `.dockerignore` (M3).
- **Never in images** — layers are archives; `docker history` reads them (M3 simulation proved it).
- **Never in logs** — the most common leak channel in practice; the logging setup masks known secret fields defensively.
- Delivery at runtime: environment variables injected by the platform (compose `env_file` for dev; CI `secrets.*`; vault/secret-manager in production — described conceptually, implemented in later modules).
- **Detection:** `gitleaks` in CI (add to Module 5 pipeline as stretch); pre-commit hook locally.
- **Response drill:** a leaked secret is *rotated first*, then history-cleaned — deleting the commit does not un-leak it. This ordering is the exam question people fail in real life.
- pydantic-settings `SecretStr` type: value is masked in reprs and accidental prints; `.get_secret_value()` makes every intentional use grep-able in review.

### 3. Structured logging for AI services

Logs are events, not sentences. JSON lines with stable field names turn "grep and hope" into queries:

- **Always-on fields:** timestamp, level, event name, `trace_id`, `model_version`, `git_sha`. The first two correlation fields were planted in Modules 2 and 1 respectively; here they pay off: one trace id joins the gateway log, the API log, and the scoring event; one model version splits an error-rate graph during rollout.
- **Event design:** `prediction_served` with `decision`, `probability_bucket` (bucketed! raw score + customer id together may be sensitive), `latency_ms`; `model_loaded` with version + seconds; `validation_rejected` with field names (never values — PII).
- **Levels with intent:** DEBUG (development detail, off in prod), INFO (business events), WARNING (degraded but serving — e.g., feature cache miss fallback), ERROR (request failed), CRITICAL (service cannot serve). Alert rules attach to WARNING+; if everything is INFO, nothing is monitorable.
- **What must never be logged:** national IDs, card numbers, full request bodies, raw feature vectors containing personal attributes, secrets. Under PDPL, logs *are* personal-data processing — retention and access controls apply to them too.
- **stdout only** (12-factor): the container platform owns shipping/rotation; file handlers inside containers create the M3 permission bug and un-shippable logs.
- Libraries: stdlib `logging` + `python-json-logger`, or `structlog` (course uses structlog for binding context). Uvicorn access logs are redundant once the middleware logs requests — disable duplication deliberately.

### 4. Common mistakes & production considerations

1. `print()` debugging left in production code (unleveled, unstructured, unbuffered surprises).
2. Logging full payloads "temporarily" during an incident — the temporary PII lake.
3. Config classes read lazily deep in call stacks → failures surface far from cause; read once at composition root, pass explicitly.
4. Same log level everywhere → either silence or noise.
5. Secrets in compose files committed "because it's just dev" — dev secrets become prod secrets via copy-paste.
6. Timezone-naive timestamps (log in UTC, render locally; incidents cross midnight).

Production: log volume costs money — sampling DEBUG/INFO under load; correlation with metrics/traces (OpenTelemetry — later module); audit-grade events (threshold changes, golden regeneration) logged immutably; log retention policy aligned with PDPL and sector rules.

## Code Examples

### Typed settings

```python
# src/fraud_service/config.py
"""All configuration in ONE place, typed and validated.
Reading os.environ anywhere else in the codebase is a review-blocking offence."""
from pathlib import Path
from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="FRAUD_",          # FRAUD_MODEL_PATH, FRAUD_LOG_LEVEL ...
        env_file=".env",              # dev convenience; real envs use real env vars
        env_file_encoding="utf-8",
        extra="forbid",               # unknown env vars with our prefix = typo = crash
    )

    # --- model ---
    model_path: Path = Field(description="Path to joblib bundle")
    block_threshold: float = Field(0.85, ge=0.5, le=0.99,
                                   description="Risk-approved block threshold")

    # --- service ---
    log_level: str = Field("INFO")
    git_sha: str = Field("dev", description="Injected by CI at build time")

    # --- dependencies ---
    redis_url: str = Field("redis://localhost:6379/0")
    registry_token: SecretStr | None = Field(
        None, description="Only needed when pulling models at startup")

    @field_validator("model_path")
    @classmethod
    def model_file_must_exist(cls, v: Path) -> Path:
        if not v.exists():
            # Fail HERE, at startup, with a message an operator understands —
            # not with a 500 on the first request.
            raise ValueError(f"model artefact not found: {v}")
        return v

    @field_validator("log_level")
    @classmethod
    def valid_level(cls, v: str) -> str:
        allowed = {"DEBUG", "INFO", "WARNING", "ERROR"}
        if v.upper() not in allowed:
            raise ValueError(f"log_level must be one of {allowed}")
        return v.upper()
```

### settings.example.env (committed) vs .env (never committed)

```bash
# configs/settings.example.env — COMMITTED. Documents every knob, no real values.
FRAUD_MODEL_PATH=/models/fraud_xgb_v3.joblib
FRAUD_BLOCK_THRESHOLD=0.85
FRAUD_LOG_LEVEL=INFO
FRAUD_REDIS_URL=redis://feature-cache:6379/0
# FRAUD_REGISTRY_TOKEN=          # <- set only via platform secret store
```

### Structured logging setup

```python
# src/fraud_service/logging_setup.py
"""JSON logs to stdout. The platform owns shipping and retention."""
import logging
import sys

import structlog


SENSITIVE_KEYS = {"password", "token", "secret", "authorization",
                  "customer_id_raw", "national_id", "card_number"}


def _mask_sensitive(logger, method, event_dict):
    """Defensive masking: even if someone logs a secret, it leaves masked."""
    for key in list(event_dict):
        if key.lower() in SENSITIVE_KEYS:
            event_dict[key] = "***MASKED***"
    return event_dict


def configure_logging(level: str = "INFO") -> None:
    logging.basicConfig(stream=sys.stdout, level=level, format="%(message)s")
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,   # trace_id binding
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso", utc=True),  # always UTC
            _mask_sensitive,
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, level)),
    )


def get_logger(name: str):
    return structlog.get_logger(name)
```

### Request logging middleware (completes Module 2's stub)

```python
# addition to src/fraud_service/api/app.py middleware
import structlog

@app.middleware("http")
async def request_logging(request: Request, call_next):
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(
        trace_id=request.state.trace_id,          # set by trace middleware
        path=request.url.path,
        method=request.method,
    )
    t0 = time.perf_counter()
    response = await call_next(request)
    log.info("http_request",
             status=response.status_code,
             latency_ms=round((time.perf_counter() - t0) * 1000, 1))
    return response
```

```python
# scoring event inside the route (note what is bucketed / absent)
log.info("prediction_served",
         decision=score.decision.value,
         probability_bucket=round(score.probability, 1),  # 0.0–1.0 in 0.1 steps
         model_version=score.model_version,
         latency_ms=elapsed_ms)
# ABSENT by design: customer_id, amount, raw feature values
```

### Example log lines (what participants should see)

```json
{"event":"model_loaded","version":"v3.2.0","seconds":0.41,"level":"info","timestamp":"2026-07-05T06:12:03.412Z"}
{"event":"http_request","trace_id":"a1b2c3d4e5f60718","path":"/v1/predict","method":"POST","status":200,"latency_ms":9.4,"level":"info","timestamp":"2026-07-05T06:12:41.220Z"}
{"event":"prediction_served","decision":"allow","probability_bucket":0.0,"model_version":"v3.2.0","latency_ms":8.1,"trace_id":"a1b2c3d4e5f60718","level":"info","timestamp":"2026-07-05T06:12:41.221Z"}
{"event":"validation_rejected","fields":["amount_sar"],"trace_id":"9c8d7e6f5a403122","level":"warning","timestamp":"2026-07-05T06:13:02.077Z"}
```

## Hands-on Lab 6 — Harden Config, Secrets, and Logs

| | |
|---|---|
| **Objective** | Replace ad-hoc config with typed Settings; prove fail-fast; convert logs to correlated JSON; run a secret-leak drill |
| **Duration** | 35 minutes (within Day 3 Hour 3) |
| **Setup** | Lab 5 solution; `pip install pydantic-settings structlog`; `git checkout lab6-start` |

**Tasks**
1. *(10 min)* Implement `Settings` with the validators; wire into lifespan; delete every scattered `os.environ` read (there are three planted — find them with `grep -rn "os.environ" src/`).
2. *(5 min)* Fail-fast demo: `FRAUD_MODEL_PATH=/nope docker compose up` → capture the crisp startup error; contrast with the old first-request 500.
3. *(10 min)* Wire `logging_setup` + request middleware + `prediction_served` event; run a load burst; pipe logs through `jq 'select(.event=="prediction_served") | .latency_ms'` to compute p50 from logs alone.
4. *(5 min)* Secret drill: the starter branch has `FRAUD_REGISTRY_TOKEN=ghp_XXXX` committed in `configs/dev.env`. Detect with `gitleaks detect`; write the two-step response in `INCIDENT.md` (rotate first, then clean history); fix delivery via env.
5. *(5 min)* Confirm masking: intentionally `log.info("debug", token=settings.registry_token)` → verify `***MASKED***` in output; remove the line; commit.

**Expected outputs**
```
Startup with bad path: ValidationError: model artefact not found: /nope  (exit 1, container restarts)
jq over 2000 requests → p50 ≈ 9ms from logs alone
gitleaks: 1 leak detected (configs/dev.env:12) → INCIDENT.md written → history cleaned
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Settings ignores env var | Missing `FRAUD_` prefix | Check `env_prefix`; `extra="forbid"` will catch typos |
| Logs interleaved/duplicated | uvicorn access log + middleware both on | Disable uvicorn access log (`--no-access-log`) |
| `trace_id` missing in scoring event | Contextvars not bound before route | Middleware order: trace → logging → routes |
| jq shows nothing | Logs not valid JSON (stray prints) | Find the `print()` (planted); replace with logger |

**Instructor notes.** The fail-fast contrast (step 2) and the jq-analytics moment (step 3) are the two demos that land hardest — do them on the projector even if pairs are ahead. Emphasise during the drill: rotation *before* history cleanup, and why the leaked token is considered burned forever.

## Mini Exercises

**Quiz.** (1) Precedence order of config sources and why env wins. (2) What does `SecretStr` actually protect against? (3) Name three fields that must never appear in logs for this service. (4) Why stdout-only logging in containers? (5) A secret was committed and force-push-removed — is the incident over? → No: rotate; history exists in clones/forks/reflog.

**Debugging exercise.** Branch `sim-config-drift`: staging behaves differently from dev; cause is `FRAUD_BLOCK_THRESHOLD=0.65` set in a forgotten compose override file. Participants must locate the effective config (`docker compose config`) and propose the guard (log the *effective* non-secret settings at startup — one line, huge payoff).

**Code-review exercise.** Review a PR that logs the full request body at INFO "for debugging", reads `os.environ["THRESHOLD"]` inside the route, and prints the settings object (leaking a token pre-SecretStr). Three findings, with PDPL angle articulated.

**Discussion.** The risk team wants threshold changes without redeploy; platform team wants immutable config. Design the compromise (config service? env + restart? audited runtime endpoint?) and its audit trail.

## Case Study — LLM Application Gateway Key Leak

**Scenario.** A Saudi enterprise's internal LLM gateway (routes staff prompts to external and on-prem models) commits its provider API key to a private repo. Eight months later the repo is open-sourced after a "secrets sweep" that missed git history. The key is scraped within hours; six figures of fraudulent usage accrue over a weekend.

**Business context.** Beyond the direct cost: the key had access to fine-tuned models containing internal terminology; disclosure triggers data-protection review under PDPL; procurement freezes the provider relationship pending investigation.

**Technical challenge.** Reconstruct the leak timeline, contain, and re-architect secret handling so the class of incident is impossible, not just this instance.

**Constraints.** The gateway serves 4,000 staff — downtime window is minutes, not hours; keys for three providers rotate on different mechanisms; history rewrite of a now-public repo cannot un-publish clones.

**Solution approach.** Immediate: rotate all provider keys (not just the leaked one — assume lateral discovery), enable provider-side spend limits and IP allowlists. Structural: secrets move to platform secret store injected as env at deploy; `SecretStr` + masking processor in the gateway; gitleaks as a required CI check *and* org-level push protection; quarterly secret-inventory review; log audit confirms keys never entered logs (masking already in place — the one control that held).

**Discussion questions.** (1) Why rotate *all* keys? (2) Which control in this module would have prevented the incident outright, and which would only have shortened it? (3) Write the five-line incident-comms message to staff. (4) Spend limits and allowlists are provider-side controls — why do client-side controls still matter?

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| Startup failure clarity | Reliability | Bad config → non-zero exit + field-named error < 3 s | fail-fast demo |
| Effective-config startup log | Operability | 100% of non-secret settings logged once | log inspection |
| Log parse rate | Operability | 100% lines valid JSON | `jq` over load-test output |
| Trace-id propagation | Operability | 100% of requests correlated end-to-end | grep by trace id |
| Secrets in git/image/logs | Reliability | 0 (gitleaks + history + docker history + log grep) | drill checklist |
| Log overhead | Performance | p99 delta ≤ 2 ms with logging on | hey before/after |
| PII fields in logs | Compliance | 0 against the forbidden-field list | review checklist |

**Example benchmark table:**

| Configuration | p99 | Log lines/req | Parse errors | Secrets found |
|---|---|---|---|---|
| Before M6 (prints, ad-hoc env) | 38 ms | 0–3 unstructured | n/a | 1 (planted) |
| After M6 | 39 ms | 2 structured | 0 | 0 |

## Required Visuals and Training Assets

### Diagrams
1. **Configuration precedence ladder** — *Elements:* defaults < example file < .env < environment, with "who sets it where" per environment (dev laptop / compose / CI / prod platform); one-image-three-environments motif. *Style:* ladder/stack with environment columns.
2. **Secret lifecycle** — *Elements:* creation → storage (vault icon) → injection (env at runtime) → use (SecretStr) → rotation → revocation; red X paths into git, image layers, logs. *Style:* lifecycle loop with forbidden-path callouts.
3. **Log correlation flow** — *Elements:* one trace_id flowing through gateway → API middleware → scoring event → (future) case system; a jq query box showing the join. *Style:* sequence-style with the JSON field highlighted at each hop.
4. **Log-level decision tree** — *Elements:* "is service degraded? can it serve? is action required now?" branching to levels with fraud-service example events on each leaf. *Style:* compact flowchart, printable.

### Images
1. **Fail-fast startup error screenshot** — *why:* the module's before/after anchor; *content:* ValidationError naming `model_path`, container exit, restart loop in compose ps.
2. **jq analytics terminal screenshot** — *why:* logs-as-data mindset; *content:* the p50 computation pipeline and result.
3. **gitleaks detection screenshot** — *why:* tool literacy; *content:* finding with file/line, rule id.
4. **Masked-secret log line screenshot** — *why:* proof the last line of defence works; *content:* `"token":"***MASKED***"` in context.

### Simulations
1. **Config-drift incident** — *Setup:* branch `sim-config-drift` (hidden compose override). *Expected:* staging mis-scores; found via `docker compose config`; guard added. *Learning objective:* effective-config visibility.
2. **Secret-leak drill** — *Setup:* planted token in history. *Expected:* detection → rotation-first response → history clean → CI guard added. *Learning objective:* correct incident ordering under time pressure.
3. **Log-volume flood** — *Setup:* set DEBUG in "prod" compose and run load test. *Expected:* 40× log volume, latency +6 ms, disk chatter; participants set INFO + sampling note. *Learning objective:* logging has a cost curve.

### Interactive Activities
- **"Log or not?" card game (10 min):** 14 candidate fields (raw score, bucketed score, national id, merchant category, latency, full prompt text…) — teams sort into log / mask / never, defend against PDPL and debugging needs.
- **Config-review pairs:** exchange repos; verify example-env completeness and grep for stray `os.environ`.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `logs_sample.jsonl` | Generated by reference solution under load | JSONL | 10k lines | jq exercises without running load |
| Forbidden-fields list | Course handout (PDPL-aligned) | MD table | 1 page | Logging review checklist |

### Demo Requirements
- **Instructor demo:** fail-fast startup vs legacy late-500 side by side; live jq session answering "what was p99 for blocked decisions in the last run?" from logs alone.
- **Student demo:** one pair presents their INCIDENT.md from the secret drill.
- **Expected outputs:** hardened service ready for capstone integration in the same hour.

---

# Final Capstone Project

## Title: Containerized AI Model Service Production Pipeline

## Project Scenario

You are the newly assigned production engineer for **"Raqib" (رقيب)**, the fraud-scoring capability of a Saudi digital-payments provider. The data-science team hands you a trained model artefact and a feature specification. Your mandate: deliver a production-grade scoring service that the platform team can deploy — a service they can trust because *its repository proves its own quality*. Everything you built in Labs 1–6 is a component; the capstone is the integration plus your own extensions.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Clean architecture (LO5):** src-layout; domain/service/adapters/api layers; import-linter contract green; model behind a protocol.
2. **FastAPI service (LO1):** `POST /v1/predict` with strict pydantic contract (`extra="forbid"`); error envelope with stable codes; `/v1/health` + `/v1/ready` with correct semantics; trace-id + model-version headers; warm-up at startup.
3. **Containerisation (LO2):** multi-stage Dockerfile ≤ 500 MB; non-root; healthcheck on `/ready`; exec-form CMD; `.dockerignore`; compose stack with Redis and healthcheck-gated dependencies; warm rebuild ≤ 30 s.
4. **Testing (LO3):** unit + integration + behavioural suites; ≥ 80% branch coverage on domain/service/api; malformed corpus 40/40 rejected; golden-file + ≥ 1 invariance + ≥ 1 directional test; suite (fast) ≤ 60 s.
5. **CI/CD (LO4):** GitHub Actions with parallel lint/test, image build + container smoke test, publish-to-GHCR on main with SHA tag; branch protection with required checks; green history (≥ 5 meaningful commits through the pipeline).
6. **Config/secrets/logging (LO5/LO6):** pydantic-settings with fail-fast validation; no secrets in git/image/logs (gitleaks clean); structured JSON logs with trace_id + model_version; `prediction_served` event with bucketed probability.
7. **Code quality (LO6):** ruff + mypy clean; README runbook (run, test, build, configure — a stranger succeeds in 10 minutes); `BENCHMARKS.md` with real measured numbers.

**One extension (choose at least one):**
- Batch endpoint `POST /v1/predict:batch` (≤ 256 items, partial-failure semantics, tested)
- Model hot-reload: `POST /admin/reload` gated by admin token, with readiness handling and a test
- trivy gate in CI with triaged `.trivyignore`
- Prometheus-style `/metrics` endpoint (request count, latency histogram)
- Golden-regeneration workflow: `make regen-golden` + PR template with evidence checklist

## Architecture (target state)

```
GitHub repo ──PR──> Actions: lint ─┐
                     test ─────────┼──> image-smoke ──main──> GHCR (sha-tagged)
                                   │        │
                       coverage/golden-diff artifacts
Local/dev:  docker compose up  → fraud-api (healthy) + feature-cache (healthy)
Runtime:    client → /v1/predict → validation wall → scorer → model adapter → JSON logs (trace_id, model_version)
```

## Deliverables

1. GitHub repository URL (public or instructor-shared) with full history
2. Green CI run on `main` + GHCR image pullable by digest
3. `README.md` runbook + `BENCHMARKS.md` with the five course benchmark tables filled from *your* runs
4. 5-minute demo: clone-to-running via compose, one valid + one malformed request, one behavioural test explained, CI walkthrough
5. `DECISIONS.md`: five one-paragraph engineering decisions with rationale (e.g., bake-vs-pull model, threshold placement)

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: Labs 1–2 integrated, API green locally | End Day 2 H1 | instructor spot-check |
| M-B: containerised + tested (Labs 3–4) | End Day 2 | `make smoke` + suite green |
| M-C: pipeline live (Lab 5) | Day 3 H2 | blocked bad-PR screenshot |
| M-D: hardened + extension (Lab 6 + choice) | Day 3 H4 | full checklist self-audit |
| M-E: demo + submission | Day 3 H5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Architecture & code quality | 20 | Layers clean, contract enforced in CI, idiomatic; reviewer finds nothing structural | Minor leakage (schema reuse, one stray import) | God-modules, framework types in domain, lint failures |
| API design & correctness | 15 | Full contract incl. error envelope, readiness semantics, headers; malformed corpus 40/40 | Contract mostly right; 1–2 corpus failures or missing Retry-After | Raw outputs, wrong status codes, no readiness |
| Containerisation | 15 | ≤ 500 MB, non-root, healthcheck, cache-disciplined, compose healthy-gated | Works but oversized or root or weak healthcheck | No multi-stage, secrets in context, broken compose |
| Testing | 20 | Three levels present and meaningful; coverage ≥ 80%; golden+invariance+directional; fast suite ≤ 60 s | Coverage 70–80% or behavioural thin | Coverage theatre, no behavioural tests |
| CI/CD | 15 | Parallel gates, smoke, publish, protection on; green history; failure artefacts | Pipeline works; protection partial or no smoke | No pipeline / red main / laptop-built image |
| Config, secrets, logging | 10 | Fail-fast settings; gitleaks clean; correlated JSON logs; PDPL-clean fields | Minor gaps (one stray env read, noisy levels) | Secrets committed or unstructured prints |
| Demo & decisions doc | 5 | Crisp demo; DECISIONS.md shows trade-off literacy | Demo works, rationale thin | Cannot run own repo cold |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the repository evidence first* (CI history, protection settings, commit hygiene), demo second — the point of the course is that the repo speaks.
- Anti-pattern flags that cap a criterion at 70%: regenerated goldens without justification; coverage inflated by asserting nothing; `:latest` deploy tags; force-pushed green.
- Verify one behavioural claim live: ask the participant to break casing invariance and show the red.

## Bonus Tasks (for early finishers / distinction seekers)

1. Multi-arch build (amd64+arm64) with buildx in CI
2. `sim-skew` reproduction: introduce skew, show which gate catches it, write the 10-line postmortem
3. Structured error taxonomy: full `code` catalogue in an `errors.md` published from OpenAPI metadata
4. Load-test job in CI (`--profile loadtest`) with regression threshold on p99

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** In clean architecture, which layer may import sklearn? → adapters only.
**Q2.** Why src-layout over flat package? → tests/CI/container import the installed package; kills path-dependent bugs.
**Q3.** Correct status code + header for "model loading, retry shortly"? → 503 + Retry-After.
**Q4.** Why must CPU-bound inference routes be plain `def` in FastAPI? → async would block the event loop; thread pool handles def.
**Q5.** `extra="forbid"` on request models defends against what two things? → silent typos and probing/unknown fields.
**Q6.** Liveness vs readiness — which restarts the container, which gates traffic? → liveness restarts; readiness gates.
**Q7.** Order these Dockerfile steps for cache efficiency: COPY src / install deps / COPY lockfile → lockfile, deps, src.
**Q8.** Two operational reasons image size matters → autoscale pull latency; CVE surface (also registry cost).
**Q9.** Why exec-form CMD? → PID 1 signal delivery → graceful shutdown.
**Q10.** Where do secrets correctly enter a container? → runtime environment/secret store — never layers/args.
**Q11.** Name the three ML-specific test types and one example each. → invariance (casing), directional (amount↑), golden file (5k scores).
**Q12.** When is regenerating a golden file legitimate? → deliberate model/feature change, reviewed PR, diff attached, version bumped.
**Q13.** Why branch coverage over line coverage? → asserts both sides of conditionals are exercised.
**Q14.** Why does the publish job run only on push-to-main? → PRs (esp. forks) are untrusted; secrets unavailable/undeserved.
**Q15.** What uniquely identifies "the image CI tested"? → the digest.
**Q16.** First action after discovering a committed secret? → rotate it (history cleanup second).
**Q17.** Config precedence and why env wins → defaults < file < env; env is what varies per environment with one image.
**Q18.** Three fields forbidden in fraud-service logs → national id/customer raw id, card number, raw request body (also secrets).
**Q19.** What two log fields make cross-service incident correlation possible? → trace_id, model_version (+timestamp).
**Q20.** DORA metric most directly improved by this course's practices? → change failure rate (also deployment frequency).

## Practical Assessments

**PA-1 (30 min, Day 2):** Given a broken repo (failing healthcheck, async-blocked route, missing .dockerignore), produce a green `make smoke`. Scored on: diagnosis notes (40%), fixes (40%), verification evidence (20%).

**PA-2 (30 min, Day 3):** Given a PR with a golden-file failure and a layer violation, triage: what may merge, what must change, write the review. Scored against the model review (rubric: correctness of triage 50%, review tone/actionability 30%, governance reasoning 20%).

**PA-3:** Capstone (rubric above) — 40% of course grade. Labs completion + PA-1/PA-2 — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (6 labs) | 30% | checkpoint commits + expected outputs |
| PA-1 + PA-2 | 20% | artefacts + notes |
| Quiz | 10% | 10-question selection |
| Capstone | 40% | rubric, repo-first |

Badge issuance (Engineering badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical golden diffs across repos are checked).

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone course org repos; push checkpoint tags (`lab1-start` … `lab6-start`, `bad-pr`, all `sim-*` branches)
- [ ] Regenerate `fraud_xgb_v3.joblib` + `golden_scores_v3.csv` against the pinned sklearn version; verify behavioural suite green
- [ ] Dry-run all 6 labs end-to-end on a clean machine **and** on Codespaces fallback
- [ ] Verify GHCR pushes work under the classroom org (test account)
- [ ] Print A4 posters: architecture rings, project tree, pipeline flow, log-level tree
- [ ] Load the malformed-payload corpus and `logs_sample.jsonl` into the shared drive
- [ ] Prepare the shared leaderboard (image sizes, benchmark numbers)
- [ ] Confirm classroom network allows github.com, ghcr.io, pypi (or mirror configured) — in restricted environments pre-pull base images to a local registry

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + git + a GitHub account with SSH or PAT auth
- [ ] Docker Desktop (WSL2 on Windows) or Colima; verify `docker run hello-world`
- [ ] VS Code + Python + Docker extensions (or preferred IDE)
- [ ] `pip install fastapi[standard] uvicorn pydantic-settings structlog pytest pytest-cov httpx ruff mypy`
- [ ] `hey`, `jq`, `gitleaks` binaries (provided in course bundle for offline install)
- [ ] Clone course repo; run `make doctor` (provided script validates all of the above and prints ✓/✗)

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| WSL2/Docker not enabled on Windows | High | Pre-session email + first-hour floater support; Codespaces fallback |
| Apple Silicon vs amd64 images | High | Teach `--platform` early in M3; multi-arch is a bonus topic |
| Corporate proxy blocks pip/GHCR | Medium | Local PyPI mirror + pre-pulled base images; document proxy envs |
| Git LFS quota/misses in CI | Medium | `with: lfs: true`; keep artefact ≤ 5 MB by design |
| Participants "improve" features mid-course, breaking goldens | Medium | It's a feature — route to the skew lesson; reference solution tags rescue |
| pytest import errors (src-layout) | Medium | `pip install -e .`; the M1 lesson, revisited deliberately |
| Fear of Docker/YAML among DS-background participants | Medium | Pairing strategy; emphasise templates-then-understanding sequencing |
| Slow laptops on docker build | Low | Buildx cache; pair on the stronger machine; Codespaces |

## Timing Recommendations

- Protect Lab 3 and Lab 5 at full length; compress M6 theory (it lands through the lab) if behind.
- If a cohort is strong: pull the trivy gate and batch endpoint into main scope on Day 3.
- If a cohort is weak: drop Lab 5 task 4's fix-the-PR to a guided demo; never drop the *blocked PR observation* — it is the course's thesis made visible.
- Hard rule: capstone assembly (Day 3 H4) must start on time; cut discussion, not build time.

## Discussion Prompts (use during transitions)

1. "What is the most expensive line of code you've seen in a notebook that reached production?"
2. "Your model is right 94% of the time. Your service is up 99.9% of the time. Which number does the customer feel — and which does this course change?"
3. "Who should own the block threshold — data science, engineering, or risk? What does your answer imply about where it lives?"
4. "If the repo is the audit evidence, what does *your* current repo testify about your team?"
5. "Which of the six practices would have caught your last production incident earliest?"

## Wrap-up (Day 3 final 15 minutes)

- Map each mandatory capstone requirement to the module that taught it (one slide).
- Forward pointer: SDA-AIE-211 consumes *exactly* the GHCR digest produced today (deployment, canary, monitoring); SDA-AIE-216 builds on the logging/config substrate for observability.
- Collect: repo URLs, BENCHMARKS.md, DECISIONS.md; issue badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.12, FastAPI ≥ 0.110, pydantic v2, pytest ≥ 8. Verify pinned versions in the course lock file before each delivery.*




