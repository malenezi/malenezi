# MLOps: Model Deployment and Automation
## عمليات تعلم الآلة: نشر النماذج والأتمتة

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | MLOps: Model Deployment and Automation |
| **Arabic Title** | عمليات تعلم الآلة: نشر النماذج والأتمتة |
| **Code** | SDA-AIE-216 |
| **Level** | Specialist |
| **Duration** | 5 days × 5 learning hours = **25 hours** |
| **Audience** | AI engineers responsible for production ML systems |
| **Prerequisites** | SDA-AIE-113; SDA-AIE-111 |
| **Assessment** | Labs; deployed pipeline project |
| **Stackability** | MLOps badge · Prerequisite for LLMOps and reliability modules · Next: SDA-AIE-312 |
| **Tools & Platforms** | MLflow · DVC · Airflow/Prefect · Docker · Kubernetes (basics) · Evidently |

## Course Description

A comprehensive module on operationalising machine learning. Participants build reproducible training pipelines, register and version models and data, deploy scalable serving endpoints, and automate retraining with monitoring for drift. The module establishes the MLOps backbone that Expert-level reliability and LLMOps modules extend.

The course is built around a single evolving artefact: **"Tayyār" (تيّار)** — a short-term **electricity load-forecasting platform** for a fictional national grid operator (the "National Grid Operations Center", NGOC). Participants inherit a data-scientist's notebook that predicts next-hour and day-ahead megawatt (MW) demand per operating area, and turn it into a governed MLOps system: experiments tracked in MLflow, data and features versioned with DVC, a training pipeline orchestrated in Airflow/Prefect, models registered and promoted through stages, served as batch and online endpoints, monitored for drift with Evidently, and released via canary/blue-green/shadow strategies with one-command rollback. Every lab produces a component of the final capstone, so by Day 5 each participant owns a working, reproducible, monitored, automatically-retraining forecasting platform — the same shape of system they will harden for reliability in later Expert modules.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Design end-to-end MLOps architectures spanning training, serving, and monitoring
2. **LO2** — Implement reproducible pipelines with data and model versioning
3. **LO3** — Deploy models as scalable, containerised inference services
4. **LO4** — Develop automated retraining and CI/CD/CT workflows
5. **LO5** — Implement monitoring for data drift, concept drift, and performance decay
6. **LO6** — Evaluate deployment strategies including canary, blue-green, and shadow releases

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | From notebook to tracked, registered models | M1: MLOps Maturity & System Architecture · M2: Experiment Tracking & Model Registry | 50% | 50% | Target-state architecture diagram + MLflow tracking server logging Tayyār runs; best model registered as `tayyar-load-forecaster@Staging` |
| **Day 2** | Reproducible data and automated training | M3: Data Versioning & Feature Stores · M4: Pipeline Orchestration & Automation | 40% | 60% | DVC-versioned dataset + feature module; Airflow/Prefect DAG that ingests → featurises → trains → evaluates → registers |
| **Day 3** | Serve it at scale | M5: Model Serving — Batch, Online, Streaming · M6: Drift Detection & Monitoring (start) | 40% | 60% | Containerised online forecast API + day-ahead batch job; first Evidently drift report |
| **Day 4** | Watch it, and release it safely | M6: Drift Detection & Monitoring · M7: Release Strategies & Rollback | 35% | 65% | Monitoring dashboard + drift-triggered retraining hook; canary + shadow deployment with automated rollback gate |
| **Day 5** | Integrate the platform | Capstone assembly · Demos · Assessment | 15% | 85% | Full Tayyār MLOps platform demo + submission |

## Hour-by-Hour Breakdown

### Day 1 — From Notebook to Tracked, Registered Models

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why ML projects stall at "it worked in the notebook"** + course kickoff + the Tayyār brief | Recognise the gap between a trained model and an operated system; place a team on the MLOps maturity model | Interactive lecture + incident-story discussion | 80/20 |
| 2 | **MLOps maturity & target architecture** (M1) | Maturity levels 0–2; the training/serving/monitoring planes; components and their contracts | Lecture + architecture whiteboarding | 70/30 |
| 3 | **Lab 1 — Assess & architect Tayyār** | Score the handed-over notebook on the maturity rubric; draft the target-state architecture and component inventory | Guided lab (pairs) | 20/80 |
| 4 | **Experiment tracking & the model registry** (M2) | Params/metrics/artefacts; runs vs experiments; registry stages; reproducibility metadata | Lecture + live MLflow demo | 60/40 |
| 5 | **Lab 2a — Instrument training with MLflow** | Wrap the Tayyār training script with autolog + manual logging; compare runs in the UI | Guided lab (pairs) | 10/90 |

### Day 2 — Reproducible Data and Automated Training

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Lab 2b — Register & promote a model** | Register the best run; add a model signature + input example; transition to `Staging` with a description | Lab + micro-lecture | 20/80 |
| 2 | **Data & feature versioning** (M3) | Why git fails for data; DVC remotes & pipelines; training/serving skew; feature stores (offline/online) | Lecture + live DVC demo | 60/40 |
| 3 | **Lab 3 — Version the data & build the feature module** | `dvc add` the load dataset, push to a remote; build the shared `features.py`; materialise offline features | Guided lab | 15/85 |
| 4 | **Pipeline orchestration & automation** (M4) | DAGs, tasks, schedules, retries, idempotency; CT (continuous training); when to trigger a retrain | Lecture + DAG walkthrough | 60/40 |
| 5 | **Lab 4 — Build the training DAG** | Author an Airflow/Prefect flow: ingest → validate → featurise → train → evaluate → register; run it end-to-end | Guided lab | 10/90 |

### Day 3 — Serve It at Scale

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Serving patterns: batch, online, streaming** (M5) | Latency/throughput/freshness trade-offs; loading from the registry; batch vs online vs streaming decision rule | Lecture + pattern comparison | 60/40 |
| 2 | **Lab 5a — Online forecast API + day-ahead batch job** | FastAPI endpoint loading `@Staging` from the registry; containerise; a batch scorer writing day-ahead forecasts | Guided lab | 10/90 |
| 3 | **Lab 5b — Scale & containerise; K8s basics** | Multi-worker image; readiness gating on model load; a `Deployment`+`Service` manifest walkthrough | Lab + micro-lecture | 30/70 |
| 4 | **Why models decay: drift taxonomy** (M6) | Data drift vs concept drift vs performance decay; detection statistics; monitoring the Tayyār feed | Lecture + Evidently demo | 65/35 |
| 5 | **Lab 6a — First drift report** | Generate an Evidently data-drift + regression-performance report on a shifted week of load data | Guided lab | 15/85 |

### Day 4 — Watch It, and Release It Safely

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Monitoring in production** (M6) | Metrics/logs/alerts; drift thresholds; wiring drift → retraining trigger; the monitoring feedback loop | Lecture + dashboard walkthrough | 55/45 |
| 2 | **Lab 6b — Drift-triggered retraining hook** | Turn the drift report into a scheduled monitoring job that opens a retraining trigger when MAPE decays | Guided lab | 15/85 |
| 3 | **Release strategies & rollback** (M7) | Canary, blue-green, shadow; traffic splitting; automated promotion gates; rollback = registry re-point | Lecture + strategy comparison | 60/40 |
| 4 | **Lab 7 — Ship v2 by canary + shadow with a rollback gate** | Deploy a candidate forecaster in shadow, compare MAPE live, canary 10% → 100% with an automated regression rollback | Guided lab | 10/90 |
| 5 | **Capstone kickoff + integration** | Integrate all components; complete capstone checklist; peer architecture review round | Project work | 10/90 |

### Day 5 — Integrate the Platform

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Capstone assembly I** | Wire tracking → data/feature versioning → orchestration → registry into one reproducible flow | Project work | 0/100 |
| 2 | **Capstone assembly II** | Serving + monitoring + release strategy + rollback; fill `BENCHMARKS.md` with measured numbers | Project work | 0/100 |
| 3 | **Capstone hardening + dry run** | End-to-end run: retrain → register → shadow → canary → monitor; rehearse the demo | Project work | 10/90 |
| 4 | **Capstone demos** | 8-minute demos; rubric-based peer + instructor scoring | Presentations | 10/90 |
| 5 | **Assessment + wrap-up** | Quiz; path to SDA-AIE-312 and LLMOps/reliability modules; badge logistics | Assessment + discussion | 30/70 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module evolves the same **Tayyār** load-forecasting platform. Never introduce a throwaway example project — always advance `tayyar-load-forecaster`. This is what makes the Day-5 capstone achievable: participants assemble, they do not build from scratch.
- **Pace control:** Labs 4 (orchestration) and 7 (release strategies) are the most overrun-prone. Publish checkpoint commits (`lab1-start`, `lab2-solution`, `lab4-start`, …) and pre-seeded MLflow/DVC state in the course repository so stragglers can fast-forward: `git checkout lab4-start && dvc pull`.
- **Infrastructure strategy:** primary = a docker-compose "MLOps stack" (MLflow server + MinIO artefact store + Postgres backend + Airflow/Prefect + a local registry) provided as `make platform-up`; fallback = a hosted classroom stack. Kubernetes is taught at the "basics" depth the catalogue specifies — manifests are read and applied against a local `kind`/`minikube` cluster, not authored from a blank file. Verify both the week before delivery.
- **Pairing:** rotate pairs each day. Pair a strong-MLOps/infra participant with a strong-modelling participant; the skill transfer is the point. Data scientists fear YAML and Docker; engineers under-respect drift — the pairing dissolves both.
- **Language:** deliver in English or Arabic; keep all code, identifiers, commit messages, and MLflow run names in English (production convention in Saudi enterprise environments — mixed-language logs and artefact names break grep- and API-based tooling).
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day-5 is deliberately light on new theory — it is build-and-demo time.
- **Assessment logistics:** the deployed-pipeline project is graded **repo-first** (MLflow run history, DVC lineage, DAG runs, CI logs, release evidence) and demo-second. Collect repository URLs and MLflow experiment links at the end of Day 4 Hour 5 so lineage can be verified before demos begin.
- **Compute honesty:** the Tayyār model is deliberately small (a LightGBM regressor on tabular data) so that a full retrain runs in seconds on a laptop. This keeps the focus on *operations*, not GPU wrangling — call this out so participants generalise the patterns to heavier models rather than assuming MLOps means small models.

---

# Module 1 — MLOps Maturity Model and System Architecture

## Module Overview

**Purpose.** Before touching a tool, a team must know *what* they are building and *how far* they have to go. This module gives participants a shared vocabulary — the MLOps maturity model — and a reference architecture that separates the three planes of an ML system (training, serving, monitoring) into components with explicit contracts. Every later module implements one of these components; this module is the map they are read against.

**Business relevance.** Saudi enterprises and government entities are moving en masse from ML proofs-of-concept to operated services under Vision 2030 digital-transformation mandates. The gap between "a model exists" and "a model is safely operated" is precisely the MLOps maturity gap, and it is where most budget is silently lost: models that cannot be reproduced, retrained, or rolled back become liabilities the moment their author leaves. A maturity assessment turns a vague "we do AI" into a concrete, funded roadmap.

**Industry use cases.**
- A national grid operator must forecast electricity demand hour-ahead and day-ahead across four operating areas; a wrong forecast means either paying for spun-up reserve generation or risking load-shedding — both expensive — so the *reliability of the operations around the model* matters as much as the model's accuracy.
- A bank's credit-decision model must be reproducible on demand for a regulator: "show me exactly the data, features, and code that produced this decision on this date." Only a mature MLOps architecture can answer that.
- A logistics platform retrains demand models weekly; without orchestration and monitoring, each retrain is a manual, error-prone event that quietly drifts the business.

**Expected competencies.** After this module a participant can place a team on the maturity model with evidence, draw the target-state architecture for an ML system, name each component's responsibility and contract, and defend an incremental adoption roadmap rather than a big-bang rewrite.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Assess an ML team/project against the MLOps maturity model with concrete evidence | LO1 |
| 1.2 | Draw the reference architecture: training, serving, and monitoring planes | LO1 |
| 1.3 | Name each component's responsibility and the contracts (artefacts) that flow between them | LO1 |
| 1.4 | Distinguish CI, CD, and CT (continuous training) and where each lives in the architecture | LO1, LO4 |
| 1.5 | Propose an incremental maturity roadmap for a given team and constraints | LO1 |

## Technical Content

### 1. What MLOps actually is (and is not)

MLOps is the practice of operating machine-learning systems reliably and reproducibly — the intersection of ML, software engineering, and operations. It is emphatically **not** "a tool", and installing MLflow does not make a team mature. Frame it in class as three disciplines fused:

- **Reproducibility:** any prediction can be traced back to the exact data, features, code, and model that produced it, and any model can be rebuilt from source.
- **Automation:** the path from "new data or new code" to "a validated, deployed model" runs with minimal human toil and maximal human *judgement* at the gates.
- **Observability:** the system reports its own health — data quality, drift, and predictive performance — so decay is caught by instruments, not by angry stakeholders.

The distinguishing feature of ML systems versus ordinary software: **there are three things that change, not one.** Traditional software changes when *code* changes. ML systems change when **code**, **data**, or **the world the data describes** changes. This is why ML needs its own operations discipline — and why "CI/CD" alone is insufficient; ML adds **CT (continuous training)**.

### 2. The MLOps maturity model

The course uses a compact three-level model (aligned with the widely-used Google/Microsoft formulations; the exact number of levels varies by source — teach the *progression*, not the numbering):

| Level | Name | Training | Deployment | Monitoring | Typical symptom |
|---|---|---|---|---|---|
| **0** | Manual / notebook | Ad-hoc in a notebook, run by hand | Manual hand-off of a pickle file; "throw it over the wall" | None, or a dashboard nobody watches | "Only Aisha can retrain it, and she's on leave" |
| **1** | ML pipeline automation | An orchestrated, parameterised pipeline; experiments tracked | Automated model delivery to a registry; deployment still gated by a human | Data + performance monitoring; drift alerts | "We can retrain reliably, but releasing is still a project" |
| **2** | CI/CD/CT automation | Retraining triggered by schedule, code change, or drift | Automated pipeline builds, tests, and deploys models with progressive delivery | Closed loop: monitoring *triggers* retraining | "New data flows to a safely-released model with humans at the gates, not the controls" |

**Assessment is evidence-based, not aspirational.** A team is at the level it can *demonstrate under audit*, not the level of its best intentions. Ask for the artefact: "Show me the pipeline run that produced the current production model." No artefact ⇒ not that level. This is the single most useful habit to instil in this module.

**Tayyār today (the starting point).** The handed-over Tayyār project is a textbook Level 0: one `forecast.ipynb`, a CSV emailed monthly, a `model.pkl` copied to a server by hand, and a MAPE number nobody can reproduce because the training/test split used `random_state=None`. The course's arc is Tayyār's journey from Level 0 to Level 2.

### 3. The reference architecture: three planes

Draw this once and refer to it for five days. An MLOps system has three planes that share artefacts through **stores**:

```
                         ┌─────────────────────────────────────────┐
   ┌── DATA PLANE ───────┤  Sources → Ingestion → Validation →      │
   │                     │  Feature Engineering → Feature Store     │
   │                     └───────────────┬─────────────────────────┘
   │                                     │ (features)
   │   ┌── TRAINING PLANE ───────────────▼─────────────────────────┐
   │   │  Orchestrated pipeline: train → evaluate → register       │
   │   │  Experiment Tracking (params/metrics)  ── Model Registry  │
   │   └───────────────┬───────────────────────────┬──────────────┘
   │                   │ (registered model)         │
   │   ┌── SERVING PLANE▼──────────────────┐        │ (versions/stages)
   │   │  Batch job · Online API · Stream   │◄───────┘
   │   └───────────────┬───────────────────┘
   │                   │ (predictions + inputs)
   │   ┌── MONITORING PLANE▼───────────────────────────────────────┐
   └──►│  Drift detection · Performance decay · Alerts ── feeds ────┼──► back to Training (CT)
       └───────────────────────────────────────────────────────────┘
```

The **contracts** (what flows between planes) are the important part — components can be swapped freely if contracts hold:

| Contract (artefact) | Producer | Consumer | Carries |
|---|---|---|---|
| **Versioned dataset** | Data plane (DVC) | Training plane | Immutable data snapshot + hash |
| **Feature set** | Feature store | Training + Serving | Same feature logic offline & online (skew defence) |
| **Registered model version** | Training plane (registry) | Serving plane | Artefact + signature + stage + lineage |
| **Prediction log** | Serving plane | Monitoring plane | Inputs, outputs, model version, timestamp |
| **Drift/decay signal** | Monitoring plane | Training plane | Trigger + evidence for retraining |

### 4. CI, CD, and CT — three automations, not one

- **CI (Continuous Integration):** validate *code and pipeline* changes — lint, type-check, unit-test the feature logic and pipeline components, test that the pipeline *assembles*. (Foreshadows the CI a prerequisite course, SDA-AIE-113, already covered.)
- **CD (Continuous Delivery):** deliver a *validated model artefact* to the registry and a *validated image* to a registry — and, at higher maturity, progressively release it (Module 7).
- **CT (Continuous Training):** the ML-specific axis — automatically *retrain* the model when triggered by a schedule, new data, code change, or a drift signal, then run it through CD. CT is what closes the monitoring→training loop and is the defining capability of Level 2.

The three compose: a drift signal (monitoring) triggers CT (retrain + evaluate + register), whose output triggers CD (test + release the new version by canary). Humans approve at gates; machines do the toil.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Everything that affects a prediction is versioned:* data (DVC), features (module version), code (git SHA), model (registry version), environment (image digest), config (env snapshot). A prediction is reproducible only if all six are pinned.
- *Stores are the integration points:* planes talk through the feature store, model registry, and prediction log — never by importing each other's internals. This is clean architecture at the system scale.
- *Automate the toil, gate the judgement:* automate retraining, testing, and packaging; keep a human decision at "promote to production" until monitoring earns the team's trust.
- *Start where the pain is:* the highest-ROI first step is almost always **experiment tracking + a registry** (you cannot manage what you cannot see), not a Kubernetes cluster.

**Common mistakes**
1. Buying a platform before writing down the target architecture — tool-led adoption produces expensive Level-0 systems with a Level-2 invoice.
2. Treating MLOps as "DevOps for models" and forgetting the *data* and *retraining* axes entirely.
3. No prediction logging, so monitoring is impossible and the CT loop can never close.
4. Reproducibility theatre: a registry entry with no data version or code SHA — it looks governed but cannot actually be rebuilt.
5. Big-bang rewrites: freezing delivery to "do MLOps properly" instead of maturing incrementally around a live service.
6. Conflating *model version* (an artefact in the registry) with *deployment* (which version is receiving traffic) — Module 7 depends on keeping these separate.

**Production considerations**
- On-call engineers navigate this architecture at 03:00 during a load-forecast miss on a peak-demand day; predictability of the component layout beats cleverness.
- In Saudi regulated and critical-infrastructure settings, *auditability* is a first-class requirement: the lineage from prediction → model version → data version → code SHA is compliance evidence, not a nicety.
- Plan for two model consumers from day one: the day-ahead **batch** forecast and the near-real-time **online** correction. If both consume the same registered model through the same feature logic, the architecture is right (Module 5 proves it).

### 6. Real-world example walkthrough

Narrate this (5 minutes, no slides): a utility deployed a load-forecasting model that was excellent in backtest. Six months later a new tranche of rooftop-solar capacity changed the *shape* of afternoon demand (concept drift), summer temperatures ran hotter than the training years (data drift), and the model — retrained by hand only "when someone remembered" — silently over-forecast midday load. The control room paid for reserve generation it did not need for weeks before anyone connected the forecast error to the cost line. The postmortem's first action was not "better model"; it was **"tracked experiments + versioned data + drift monitoring + scheduled retraining with safe release."** This course is that action item, generalised — and Tayyār is that utility.

## Code Examples

### The Tayyār maturity self-assessment (a runnable checklist)

```python
# tools/maturity_audit.py
"""Evidence-based MLOps maturity audit for the Tayyar platform.

Run it against a repo; it does not ASK if you do a thing, it CHECKS for the
artefact that proves you do. 'Aspirational yes' is not a passing answer.
"""
from __future__ import annotations
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Check:
    name: str
    passed: bool
    evidence: str


def _exists(*paths: str) -> bool:
    return any(Path(p).exists() for p in paths)


def audit(repo: Path) -> list[Check]:
    checks: list[Check] = []

    # Level 1 signals
    checks.append(Check(
        "Experiments tracked",
        _exists("mlruns", "mlflow.db") or _has_mlflow_calls(repo),
        "MLflow tracking store or logging calls present"))
    checks.append(Check(
        "Data versioned",
        _exists(".dvc", "data/grid_load_hourly.csv.dvc"),
        "DVC metadata files present"))
    checks.append(Check(
        "Model registered (not a loose pickle)",
        _registry_has_model("tayyar-load-forecaster"),
        "Registry contains named model with versions"))
    checks.append(Check(
        "Training is an orchestrated pipeline",
        _exists("dags/train_tayyar.py", "flows/train_tayyar.py"),
        "Airflow DAG or Prefect flow defines the training pipeline"))

    # Level 2 signals
    checks.append(Check(
        "Predictions are logged for monitoring",
        _exists("monitoring/prediction_log.parquet") or _logs_predictions(repo),
        "Serving layer persists inputs+outputs+model_version"))
    checks.append(Check(
        "Drift monitoring runs on a schedule",
        _exists("dags/monitor_tayyar.py", "flows/monitor_tayyar.py"),
        "Scheduled Evidently monitoring job exists"))
    checks.append(Check(
        "Retraining can be triggered by drift",
        _drift_triggers_training(repo),
        "Monitoring job can open a retraining trigger"))

    return checks


def level(checks: list[Check]) -> int:
    names = {c.name for c in checks if c.passed}
    level1 = {"Experiments tracked", "Data versioned",
              "Model registered (not a loose pickle)",
              "Training is an orchestrated pipeline"}
    level2 = {"Predictions are logged for monitoring",
              "Drift monitoring runs on a schedule",
              "Retraining can be triggered by drift"}
    if level1 | level2 <= names:
        return 2
    if level1 <= names:
        return 1
    return 0


# --- stubs the participants implement in Lab 1 (return False initially) ---
def _has_mlflow_calls(repo: Path) -> bool: ...
def _registry_has_model(name: str) -> bool: ...
def _logs_predictions(repo: Path) -> bool: ...
def _drift_triggers_training(repo: Path) -> bool: ...


if __name__ == "__main__":
    results = audit(Path("."))
    for c in results:
        print(f"[{'x' if c.passed else ' '}] {c.name:45s} — {c.evidence}")
    print(f"\nAssessed maturity level: {level(results)}")
```

### The architecture as a machine-readable component inventory

```yaml
# architecture/tayyar_components.yaml
# The target-state component inventory. Each later module implements one row.
# 'contract_out' is what this component produces for others to consume.
platform: tayyar
operating_areas: [CENTRAL, WESTERN, EASTERN, SOUTHERN]

components:
  - name: ingestion
    plane: data
    tool: python + Airflow
    responsibility: Pull hourly load + weather readings per operating area
    contract_out: raw_load_hourly (partitioned by date)

  - name: data_versioning
    plane: data
    tool: DVC
    responsibility: Snapshot and hash each dataset revision
    contract_out: grid_load_hourly.csv.dvc (immutable pointer)

  - name: feature_store
    plane: data
    tool: feature module + parquet (offline) / Redis (online)
    responsibility: Single source of feature logic, offline & online
    contract_out: feature_set@version (skew-free)

  - name: experiment_tracking
    plane: training
    tool: MLflow Tracking
    responsibility: Record params, metrics, artefacts per run
    contract_out: run_id with full metadata

  - name: model_registry
    plane: training
    tool: MLflow Model Registry
    responsibility: Version, stage, and lineage models
    contract_out: tayyar-load-forecaster@{Staging,Production}

  - name: orchestration
    plane: training
    tool: Airflow / Prefect
    responsibility: Run ingest→featurise→train→evaluate→register on schedule/trigger
    contract_out: pipeline_run (idempotent, retryable)

  - name: serving_online
    plane: serving
    tool: FastAPI + Docker (+ K8s basics)
    responsibility: Low-latency next-hour forecast per area
    contract_out: forecast_response + prediction_log

  - name: serving_batch
    plane: serving
    tool: scheduled container job
    responsibility: Day-ahead 24h forecast per area
    contract_out: day_ahead_forecast.parquet + prediction_log

  - name: monitoring
    plane: monitoring
    tool: Evidently
    responsibility: Detect data/concept drift + MAPE decay; alert; trigger CT
    contract_out: drift_report + retraining_trigger

  - name: release_controller
    plane: serving
    tool: canary/shadow logic + registry stages
    responsibility: Progressive delivery with automated rollback
    contract_out: promotion_decision (with evidence)
```

## Hands-on Lab 1 — Assess and Architect the Tayyār Platform

| | |
|---|---|
| **Objective** | Score the handed-over Tayyār notebook against the maturity model with evidence, then produce the target-state architecture and a machine-readable component inventory + adoption roadmap |
| **Duration** | 50 minutes |
| **Setup** | Course repo cloned, `git checkout lab1-start`; the starter contains `forecast.ipynb` (deliberately Level 0) and `tools/maturity_audit.py` with stubbed checks |

**Instructions & tasks**

1. *(8 min)* Run `forecast.ipynb` top-to-bottom; list every reproducibility hazard flagged with `# SMELL` (unseeded split, emailed CSV, `model.pkl` written to a hard-coded path, MAPE printed but not stored, features computed inline).
2. *(7 min)* Run `python tools/maturity_audit.py`; record the current level (expect **0**). Note which checks fail and *why the evidence is absent*.
3. *(15 min)* Draft the **target-state architecture** on the provided canvas: place the three planes, the five stores/contracts, and label which module of this course will implement each component. Use the reference diagram as a starting skeleton, not a copy.
4. *(10 min)* Complete `architecture/tayyar_components.yaml` for your target state (fill any `responsibility`/`contract_out` you would change); validate it parses (`python -c "import yaml,sys; yaml.safe_load(open('architecture/tayyar_components.yaml'))"`).
5. *(7 min)* Write a 5-line **roadmap** in `ROADMAP.md`: order the components by ROI-per-effort for Tayyār, starting from Level 0. Defend your *first* step in one sentence.
6. *(3 min)* Commit with message `docs: maturity assessment + target architecture for tayyar`.

**Expected output**
```
$ python tools/maturity_audit.py
[ ] Experiments tracked                              — MLflow tracking store or logging calls present
[ ] Data versioned                                   — DVC metadata files present
[ ] Model registered (not a loose pickle)            — Registry contains named model with versions
[ ] Training is an orchestrated pipeline             — Airflow DAG or Prefect flow defines the pipeline
[ ] Predictions are logged for monitoring            — Serving layer persists inputs+outputs+model_version
[ ] Drift monitoring runs on a schedule              — Scheduled Evidently monitoring job exists
[ ] Retraining can be triggered by drift             — Monitoring job can open a retraining trigger

Assessed maturity level: 0
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Notebook won't run (missing lightgbm) | Starter env incomplete | `pip install -r requirements.lock`; the point is to *read* it, not perfect it |
| `yaml.safe_load` errors | Tab indentation in YAML | YAML forbids tabs; convert to spaces; discuss why config formats matter |
| Team argues Level 1 "because we sort of track things" | No artefact | Audit rule: no artefact ⇒ not that level; make them point to the evidence |
| Roadmap starts with Kubernetes | Tool-led thinking | Redirect: highest ROI from Level 0 is tracking + registry, not a cluster |

**Instructor notes.** The starter notebook contains exactly the reproducibility hazards named in the content section — walk the room and check who catches the unseeded split (it is the one with real audit consequences). This lab produces the *contract* the rest of the course fulfils: keep the target-architecture canvas visible on the wall all five days and physically tick each component as its module lands. Fast finishers: have them implement one of the stubbed `maturity_audit.py` checks (e.g. `_registry_has_model`) — a perfect bridge to Module 2.

## Mini Exercises

**Quiz (5 questions)**
1. The three things that change in an ML system (vs one in ordinary software)? → **code, data, and the world (the data-generating process)**.
2. What single artefact proves a team is at "Level 1 — pipeline automation"? → **an orchestrated pipeline run that produced the current model** (a registry entry with lineage).
3. Define CT and how it differs from CD. → CT retrains the *model* on trigger; CD delivers/releases a validated *artefact*. CT feeds CD.
4. Name the six things that must be versioned to reproduce a prediction. → data, features, code, model, environment, config.
5. True/False: installing MLflow raises a team's maturity level. → **False** — maturity is demonstrated capability, not installed tools.

**Debugging exercise.** Give participants a "Level 2" claim with a registry entry whose lineage points to `data: latest` and `code: (unknown)`. They must explain why this is *reproducibility theatre* and what minimum metadata would make it real.

**Architecture-review exercise.** Provide a mis-drawn architecture where the monitoring plane reads directly from the training database and the serving layer imports the training feature code by relative path. Each pair writes ≥4 contract violations and redraws the offending edges through stores.

**Discussion questions.**
- Your leadership wants "MLOps" and has budget for one hire or one platform. Which, and why, for a Level-0 team?
- Who owns the decision to promote a Tayyār model to production — data science, engineering, or grid operations? What does your answer imply about where the promotion gate lives?

## Case Study — From Notebook to Operated Service at a Regional Water Utility

**Scenario.** "Namaa Water", a regional Saudi water utility, built a pump-energy optimisation model that reduced pumping cost 9% in a pilot. Eighteen months later the model is quietly *increasing* cost in two of five districts, and nobody noticed for a full billing quarter.

**Business context.** The pilot's success got the data scientist promoted and moved to a new team. The model runs as a cron job invoking a notebook-exported script on a single VM; there is no tracking, no versioning, and no monitoring. Energy is one of the utility's top-three cost lines.

**Technical challenge.** Diagnose *why* the model degraded (was it data drift from new pumps, concept drift from a tariff change, or a silent code edit?) — and the team **cannot answer**, because nothing was tracked, versioned, or logged. The real deliverable is not a fix; it is a maturity roadmap that makes the *next* degradation diagnosable.

**Constraints.** Two engineers, neither the original author; the model artefact cannot be retrained until the input data is trusted (6-week data-quality review); the utility's regulator now wants quarterly evidence of model governance; production changes require a change-advisory board sign-off.

**Solution approach (facilitate, don't lecture).** (1) Stop the bleeding: add prediction logging *around* the existing model — zero model change, immediate observability. (2) Version the data with DVC and pin the current code SHA so the *current* behaviour is at least reproducible. (3) Stand up tracking + a registry so the next retrain is comparable. (4) Add drift + performance monitoring against the logged predictions. (5) Only then automate retraining. Each step ships independently; none requires freezing the service.

**Discussion questions.**
1. Why is prediction logging the correct *first* step even before versioning?
2. Which maturity step would have made the original degradation diagnosable in days instead of a quarter?
3. The regulator wants "governance evidence." Map three maturity artefacts to three governance questions.
4. Argue for/against retraining before the 6-week data-quality review completes.

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Maturity level of the *plan* (not yet the system) | Governance | Documented Level-2 target with roadmap | `ROADMAP.md` review |
| Component inventory completeness | Architecture | 10/10 components with responsibility + contract | `tayyar_components.yaml` review |
| Reproducibility hazards identified in starter | Diagnosis | ≥ 5 of 6 seeded smells found | Lab checklist |
| Contracts correctly placed between planes | Architecture | 5/5 store contracts drawn | Canvas review |
| Roadmap first-step ROI defensible | Governance | First step = tracking/registry (not infra) | Discussion |

**Example benchmark table (filled during lab):**

| Snapshot | Assessed level | Tracked | Versioned data | Registered model | Monitored |
|---|---|---|---|---|---|
| Tayyār as handed over | 0 | no | no | no (loose `model.pkl`) | no |
| Tayyār target (this course) | 2 | MLflow | DVC | registry w/ stages | Evidently + CT loop |

## Required Visuals and Training Assets

### Diagrams
1. **The three-plane reference architecture** — *Purpose:* the anchor image for the whole course. *Elements:* Data / Training / Serving / Monitoring planes as horizontal bands; the five store-contracts as labelled arrows; a dashed feedback arrow from Monitoring back to Training marked "CT". *Style:* flat vector, four-colour palette (one per plane), English labels with Arabic subtitles. *Designer description:* "Four stacked horizontal bands with component boxes; bold labelled arrows for artefacts flowing down and one curved dashed arrow looping monitoring back to training."
2. **MLOps maturity ladder** — *Purpose:* memorable placement tool. *Elements:* three rungs (0/1/2) with the training/deployment/monitoring column for each and a "typical symptom" quote per rung. *Style:* ascending staircase, printable A4.
3. **CI / CD / CT triad** — *Purpose:* disambiguate the three automations. *Elements:* three interlocking loops with what each validates and how CT→CD→release chains. *Style:* Venn-plus-flow hybrid.
4. **Reproducibility "six pins"** — *Purpose:* make reproducibility concrete. *Elements:* a prediction at the centre with six pinned inputs (data/features/code/model/env/config) radiating out. *Style:* hub-and-spoke.

### Images (screenshots)
1. **Maturity-audit terminal output** (all unchecked, Level 0) — *why:* the honest starting point; *content:* the seven checks failing with evidence strings.
2. **The deliberately-messy `forecast.ipynb`** with `# SMELL` annotations visible — *why:* participants hunt these in Lab 1; *content:* unseeded split, hard-coded path, printed-not-stored MAPE.
3. **The completed architecture canvas photo** — *why:* target-state reference on the wall; *content:* filled three-plane diagram with module labels.
4. **`tayyar_components.yaml` in an editor** — *why:* the machine-readable contract; *content:* the component inventory with `contract_out` fields highlighted.

### Simulations
1. **The unreproducible model** — *Setup:* branch `sim-unreproducible` trains twice with `random_state=None` and different row order. *Expected behaviour:* two "same" runs produce different MAPE and different `model.pkl` hashes. *Learning objective:* without pinning, "the model" is not a single thing.
2. **The silent degradation** — *Setup:* provided a logged-vs-actual load series where MAPE quietly climbs over eight weeks. *Expected behaviour:* the trend is invisible day-to-day and obvious only when charted. *Learning objective:* decay is gradual; you need instruments, not vibes.

### Interactive Activities
- **Maturity card-sort (15 min):** 18 capability cards (e.g. "retrain by hand", "registry with stages", "drift alerts") sorted onto the 0/1/2 ladder; each pair defends one borderline card.
- **"Where does this belong?" plane game (10 min):** 14 component cards (feature store, canary controller, Evidently job, DVC remote…) placed onto the four-plane canvas; class challenges one placement.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `grid_load_hourly.csv` | Synthetic, generated by course tooling (realistic KSA load shape: summer AC peak, Ramadan evening shift, Hajj spike; MW load + temp/humidity/calendar) | CSV | ~35,000 rows (4 areas × 2 years hourly) | The golden-thread dataset; reused in every module |
| `forecast.ipynb` | Course team (deliberately Level 0) | Jupyter | 1 notebook | Lab 1 assessment target |
| `tayyar_components.yaml` (template) | Course team | YAML | 1 file | Architecture inventory scaffold |

### Demo Requirements
- **Instructor demo:** live maturity audit of the starter repo, then a 5-minute whiteboard build of the three-plane architecture — narrate each contract as you draw its arrow.
- **Student demo:** two pairs present their target architecture and defend their *first* roadmap step to the class.
- **Expected outputs:** every participant has a committed `ROADMAP.md` + completed `tayyar_components.yaml` and a level-0 audit baseline.

---

# Module 2 — Experiment Tracking and Model Registry

## Module Overview

**Purpose.** You cannot manage what you cannot see. This module gives Tayyār an institutional memory: every training run's parameters, metrics, and artefacts recorded and comparable, and every model that matters versioned in a registry with stages, a signature, and lineage. This is the highest-ROI first step out of Level 0, and the substrate every later module reads from.

**Business relevance.** In regulated Saudi sectors — critical infrastructure, banking (SAMA), health (SFDA-adjacent) — a model is not "done" when it scores well; it is done when the organisation can answer *"which exact model is in production, who approved it, on what data, and how does it compare to the last three candidates?"* under audit. Experiment tracking and a registry turn that from a fire drill into a link. They also end the most common source of wasted effort: re-running experiments nobody recorded, and shipping a model that was worse than one tried last month.

**Industry use cases.**
- A grid operator compares fourteen forecasting candidates (feature sets, horizons, gradient-boosting hyperparameters) and must justify the chosen one to an operations committee with a single comparison view.
- A bank's model-risk function requires that every production credit model be reproducible from its registry entry alone — data version, code SHA, and metrics attached.
- A retail forecasting team runs a nightly retrain; the registry's "champion vs challenger" staging is what lets them auto-promote only when the challenger beats the champion.

**Expected competencies.** Participants can instrument a training script with autolog + deliberate manual logging, organise runs into experiments, compare runs to pick a champion, register a model with a signature and input example, and transition it through registry stages with descriptions and lineage.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Distinguish runs, experiments, parameters, metrics, and artefacts | LO2 |
| 2.2 | Instrument the Tayyār training script with MLflow autolog + manual logging | LO2, LO1 |
| 2.3 | Compare runs and select a champion with defensible criteria | LO2 |
| 2.4 | Register a model with a signature, input example, and lineage metadata | LO2 |
| 2.5 | Transition models across stages (None → Staging → Production) with governance | LO2, LO1 |

## Technical Content

### 1. The vocabulary: runs, experiments, artefacts

- **Experiment:** a named bucket for runs that answer one question ("day-ahead-forecast-tuning"). Tayyār gets one experiment per modelling question, not one per person.
- **Run:** a single execution of training code, identified by a `run_id`. It records **parameters** (inputs you chose: learning rate, feature set, horizon), **metrics** (outputs you measured: MAPE, RMSE, training time), **artefacts** (files produced: the model, plots, the feature list), and **tags** (free metadata: git SHA, data version, author).
- **The reproducibility contract:** a run is only useful later if it captures *enough to rebuild it*. The non-negotiable tags for Tayyār: `git_sha`, `data_version` (the DVC hash from Module 3), `feature_set_version`, and `python_env` (a lockfile hash). A metric without these tags is a number without a source.

### 2. Autolog first, then log with intent

MLflow's `autolog()` captures framework params, metrics, and the model automatically for supported libraries (sklearn, LightGBM, XGBoost, PyTorch…). Turn it on first — it removes 80% of the boilerplate — then add the *domain* logging autolog cannot know:

- **Business metric:** MAPE per operating area and a weighted overall MAPE — autolog logs the loss, but "MAPE on the Western area during summer peak" is the number the operations committee cares about.
- **Data + code lineage tags** (above): the metadata that makes the run auditable.
- **Domain artefacts:** the per-horizon error plot, the feature-importance chart, the exact `feature_list.json`, and a small `error_by_hour.csv` — evidence a reviewer reads without rerunning anything.
- **Input example + signature** (see §4): so the registered model self-documents its expected input schema.

Rule to teach: **autolog for completeness, manual logging for judgement.** Autolog answers "what did the framework do?"; you answer "what does the business need to see?"

### 3. Comparing runs and choosing a champion

The MLflow UI's run comparison (parallel-coordinates + table) is where a champion is chosen — but the *criterion* is an engineering decision, not "lowest MAPE":

- Choose against the **business objective**, not the loss: day-ahead MAPE ≤ 3.0% overall *and* ≤ 3.5% on every operating area (a model great on average but terrible on the Southern area is unacceptable — you cannot under-forecast one region into load-shedding).
- Prefer the **simpler, faster** model when metrics tie within noise — smaller models retrain and serve cheaper (Module 5).
- Beware **leakage-inflated** metrics: a suspiciously good run is guilty until proven innocent (did a future-timestamp feature leak in?). Tracking makes this auditable.
- Record *why* you chose: a `selection_reason` tag on the champion run is future-you's gift.

### 4. Signatures, input examples, and the flavour system

A registered model must self-describe its I/O or it becomes a liability at serving time:

- **Signature:** the input/output schema (column names + dtypes). MLflow infers it from an example; it is what lets the serving layer validate inputs and what catches training/serving skew at the boundary.
- **Input example:** a small sample row logged with the model; it makes the registry entry testable and documents the exact expected shape (crucial for Tayyār's feature columns).
- **Flavours:** MLflow stores a model in one or more "flavours" (e.g. `python_function` + `lightgbm`). The `pyfunc` flavour is the universal serving contract — Module 5 loads the model as a `pyfunc` so the serving code never imports LightGBM directly (clean architecture at the artefact level).

### 5. The model registry and staged promotion

The registry turns a good run into a governed asset:

- **Registered model:** a named entity (`tayyar-load-forecaster`) with numbered **versions**. A version points to a run and its artefacts.
- **Stages / aliases:** `None → Staging → Production → Archived` (classic stages) or the newer **alias** model (`@champion`, `@production`). Teach both; note MLflow is moving from stages to aliases + tags — use whichever the classroom server version supports, and explain the direction of travel.
- **Promotion is a governed transition:** moving a version to Production is a decision with an owner, a reason, and a record. This is where "who approved this model?" gets its answer. Rollback (Module 7) is just re-pointing the alias to the previous version — seconds, not a rebuild.
- **Lineage:** from a Production model version you can reach its run → params/metrics → data version → code SHA. That chain *is* the audit evidence.

### 6. Common mistakes & production considerations

1. Logging metrics but not lineage tags — pretty dashboards you cannot reproduce from.
2. One experiment for everything (or one per person) — comparison becomes impossible; organise by *question*.
3. Registering the model but not its signature/input example — the serving team reverse-engineers the schema from Slack messages.
4. Treating `Production` stage as a label anyone can set — no owner, no reason, no audit; promotion must be gated.
5. Storing artefacts on a laptop's local `mlruns/` — use a shared tracking server + object store (MinIO/S3) so the team and CI see the same runs.
6. Logging the *training data itself* as an artefact (huge, and it belongs in DVC) — log the data *version*, not the data.

Production: a central tracking server backed by a database + object store (the course `make platform-up` provides MLflow + Postgres + MinIO); access control on who can promote to Production; retention on old runs; and — for critical infrastructure — immutable audit of every stage transition. In restricted Saudi networks the tracking server and artefact store live *inside* the network boundary; participants should never assume public SaaS tracking.

## Code Examples

### Instrumented training with autolog + intentional logging

```python
# src/load_forecast/training/train.py
"""Train the Tayyar day-ahead load forecaster with full MLflow tracking.

Design: autolog for completeness, manual logging for the numbers the grid
operations committee actually reads, plus lineage tags for auditability.
"""
from __future__ import annotations
import json
import subprocess
from pathlib import Path

import lightgbm as lgb
import mlflow
import mlflow.lightgbm
import numpy as np
import pandas as pd
from mlflow.models import infer_signature
from sklearn.metrics import mean_absolute_percentage_error

from load_forecast.features import build_features, FEATURE_SET_VERSION

AREAS = ["CENTRAL", "WESTERN", "EASTERN", "SOUTHERN"]


def _git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"]).decode().strip()
    except Exception:
        return "unknown"


def train(data_path: Path, params: dict, data_version: str) -> str:
    df = pd.read_csv(data_path, parse_dates=["timestamp"])
    X, y = build_features(df)                      # SHARED feature logic (M3)

    # Time-based split: NEVER shuffle a time series (leakage!)
    split = df["timestamp"].quantile(0.8)
    train_mask = df["timestamp"] <= split
    Xtr, ytr = X[train_mask], y[train_mask]
    Xte, yte = X[~train_mask], y[~train_mask]

    mlflow.set_experiment("tayyar-day-ahead-forecast")
    mlflow.lightgbm.autolog(log_input_examples=False, log_models=False)

    with mlflow.start_run(run_name=f"lgbm-{_git_sha()}") as run:
        model = lgb.LGBMRegressor(**params)
        model.fit(Xtr, ytr,
                  eval_set=[(Xte, yte)],
                  callbacks=[lgb.early_stopping(50, verbose=False)])

        # --- manual logging: the BUSINESS metrics autolog cannot know ---
        pred = model.predict(Xte)
        overall_mape = float(mean_absolute_percentage_error(yte, pred))
        mlflow.log_metric("mape_overall", overall_mape)

        worst_area_mape = 0.0
        for area in AREAS:
            m = df.loc[~train_mask, "operating_area"] == area
            if m.any():
                area_mape = float(mean_absolute_percentage_error(
                    yte[m.values], pred[m.values]))
                mlflow.log_metric(f"mape_{area}", area_mape)
                worst_area_mape = max(worst_area_mape, area_mape)
        mlflow.log_metric("mape_worst_area", worst_area_mape)

        # --- lineage tags: what makes this run auditable & reproducible ---
        mlflow.set_tags({
            "git_sha": _git_sha(),
            "data_version": data_version,             # DVC hash (Module 3)
            "feature_set_version": FEATURE_SET_VERSION,
            "horizon": "day_ahead_24h",
        })

        # --- signature + input example: the model self-documents its I/O ---
        signature = infer_signature(Xte, pred)
        input_example = Xte.iloc[:2]
        mlflow.lightgbm.log_model(
            model, name="model",
            signature=signature, input_example=input_example)

        # --- domain artefacts a reviewer reads without rerunning ---
        Path("feature_list.json").write_text(json.dumps(list(X.columns)))
        mlflow.log_artifact("feature_list.json")

        print(f"run_id={run.info.run_id} mape={overall_mape:.4f} "
              f"worst_area={worst_area_mape:.4f}")
        return run.info.run_id
```

### Choosing the champion programmatically (governed selection)

```python
# src/load_forecast/training/select_champion.py
"""Pick the champion by the BUSINESS criterion, not raw loss, and record why."""
import mlflow
from mlflow.tracking import MlflowClient

OVERALL_CEILING = 0.030       # day-ahead MAPE must be <= 3.0% overall
PER_AREA_CEILING = 0.035      # ... and <= 3.5% on EVERY operating area


def pick_champion(experiment_name: str) -> str:
    client = MlflowClient()
    exp = client.get_experiment_by_name(experiment_name)
    runs = mlflow.search_runs([exp.experiment_id],
                              order_by=["metrics.mape_overall ASC"])

    eligible = runs[
        (runs["metrics.mape_overall"] <= OVERALL_CEILING)
        & (runs["metrics.mape_worst_area"] <= PER_AREA_CEILING)
    ]
    if eligible.empty:
        raise SystemExit("No run meets the operations SLA; do not promote.")

    champion = eligible.iloc[0]                     # best overall among eligible
    run_id = champion["run_id"]
    client.set_tag(run_id, "selection_reason",
                   f"Best overall MAPE among runs meeting per-area SLA "
                   f"(overall={champion['metrics.mape_overall']:.4f}, "
                   f"worst_area={champion['metrics.mape_worst_area']:.4f})")
    print(f"Champion: {run_id}")
    return run_id
```

### Register and stage with lineage

```python
# src/load_forecast/training/register.py
"""Register the champion and transition it to Staging with governance metadata."""
from mlflow.tracking import MlflowClient

MODEL_NAME = "tayyar-load-forecaster"


def register_and_stage(run_id: str, note: str) -> int:
    client = MlflowClient()
    src = f"runs:/{run_id}/model"
    mv = client.create_model_version(
        name=MODEL_NAME, source=src, run_id=run_id)

    # Newer MLflow: use aliases + tags instead of deprecated stages.
    client.set_registered_model_alias(MODEL_NAME, "staging", mv.version)
    client.set_model_version_tag(MODEL_NAME, mv.version, "approved_by", "unset")
    client.update_model_version(MODEL_NAME, mv.version, description=note)
    print(f"Registered {MODEL_NAME} v{mv.version} -> @staging")
    return int(mv.version)
```

## Hands-on Lab 2 — Instrument, Compare, and Register the Forecaster

| | |
|---|---|
| **Objective** | Turn the untracked Tayyār training script into a fully-tracked, comparable, registered model: MLflow-instrumented, champion selected by SLA, registered with signature + lineage, promoted to `@staging` |
| **Duration** | 2 × 50 min (Day 1 H5 + Day 2 H1) |
| **Setup** | `make platform-up` (MLflow + Postgres + MinIO), `git checkout lab2-start`, `pip install mlflow lightgbm scikit-learn` |

**Part A tasks (50 min)**
1. *(10 min)* Point the script at the tracking server (`MLFLOW_TRACKING_URI`); add `mlflow.lightgbm.autolog()`; run once; confirm the run appears in the UI.
2. *(15 min)* Add manual logging: `mape_overall`, `mape_<AREA>` for all four areas, `mape_worst_area`, and the four lineage tags.
3. *(15 min)* Sweep three hyperparameter sets (provided) as three runs; open the UI comparison view; identify the best-overall and the best-worst-area — note they may differ.
4. *(10 min)* Add the signature + input example to the logged model; verify the registry-ready artefact in the UI ("Schema" tab populated).

**Part B tasks (50 min)**
1. *(10 min)* Implement `pick_champion` with the SLA ceilings; run it; read the printed `selection_reason`.
2. *(15 min)* Register the champion as `tayyar-load-forecaster`; add a description; set the `@staging` alias.
3. *(10 min)* Verify lineage: from the registered version in the UI, click through to run → metrics → tags; confirm you can reach `git_sha` and `data_version`.
4. *(10 min)* Load the staged model back as `pyfunc` and predict on the input example — proving the artefact is self-serving (bridge to Module 5).
5. *(5 min)* Commit: `feat(training): mlflow tracking, champion selection, registry promotion`.

**Expected outputs**
```
$ python -m load_forecast.training.train ...
run_id=8f3a1c...  mape=0.0271  worst_area=0.0329

$ python -m load_forecast.training.select_champion
Champion: 8f3a1c...

$ python -m load_forecast.training.register
Registered tayyar-load-forecaster v1 -> @staging

MLflow UI: 3 runs in 'tayyar-day-ahead-forecast'; v1 aliased @staging;
Schema tab shows 11 input columns; lineage reaches git_sha + data_version.
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Runs land in `mlruns/` not the server | `MLFLOW_TRACKING_URI` unset | Export it (`http://localhost:5000`); confirm in run's "source" |
| Artefacts fail to upload | MinIO/S3 creds not set | Set `MLFLOW_S3_ENDPOINT_URL` + keys from `platform.env` |
| Best-overall model fails a region | Averaged metric hides a bad area | This is the lesson — the SLA per-area ceiling exists for exactly this |
| Signature inference errors | Non-numeric/object columns | Cast categoricals per the feature spec; discuss serving-time dtype contracts |
| `create_model_version` "run not found" | Wrong tracking URI at register time | Register against the same server that holds the run |

**Instructor notes.** The highest-value teachable moment is the divergence in Part A step 3: the model with the best overall MAPE is *not* the one with the best worst-area MAPE. Let a pair pick the overall-best, then reveal the Southern-area failure — this is why the SLA and the registry's comparison view exist. Keep every pair's champion `run_id` posted; Module 3 attaches a data version to it, and Module 4 automates the whole chain.

## Mini Exercises

**Quiz.** (1) Difference between a *parameter* and a *metric*? → param = chosen input; metric = measured output. (2) Name the four lineage tags Tayyār runs must carry. → git_sha, data_version, feature_set_version, python_env. (3) Why log the data *version* not the data? → data belongs in DVC; artefact stores bloat and duplicate. (4) What does a model *signature* buy the serving team? → validated I/O schema; skew defence at the boundary. (5) Rollback in registry terms? → re-point the production alias to the previous version.

**Debugging exercise.** Branch `sim-leak`: a run shows MAPE 0.4% (suspiciously perfect). Participants must discover a `load_next_hour` feature leaked the target and explain why tracking made it *catchable* (compare against realistic runs) rather than shipped.

**Code-review exercise.** Review a PR that logs metrics but no tags, registers with `stage="Production"` directly (skipping staging), and stores the full training CSV as an artefact. Three findings + the governance argument for each.

**Discussion.** Your challenger beats the champion on overall MAPE by 0.1% but is 3× slower to retrain and serve. Promote or not? Who decides, and what tag records the decision?

## Case Study — Fourteen Forecasters and No Memory at a Distribution Company

**Scenario.** A Saudi electricity distribution company's analytics team spent a quarter building "the best" load forecaster. Four data scientists tried fourteen approaches on shared laptops; when leadership asked "which one won and why?", nobody could reconstruct the comparison — results lived in scattered notebooks and one contested spreadsheet.

**Business context.** A SAR 2M reserve-generation contract decision hinged on the forecast's accuracy claim; procurement needed defensible evidence, not "trust us".

**Technical challenge.** Reconstruct a defensible comparison *after the fact*, then make the next quarter's work auditable by construction.

**Constraints.** No shared tracking server existed; three of the fourteen experiments could not be re-run at all (lost preprocessing); the regulator wanted per-region accuracy, not just overall; the winning model had to be reproducible six months later for a rate case.

**Solution approach.** Stand up a shared MLflow server + MinIO; re-run the eleven reproducible experiments under tracking with lineage tags; log per-area MAPE as first-class metrics; register the champion with signature + `selection_reason`; write the three unreproducible ones off explicitly (and add a policy: no result counts unless tracked). The registry entry becomes the procurement evidence.

**Discussion questions.** (1) What minimum metadata would have saved the three lost experiments? (2) Overall vs per-region metric — which does the regulator care about and why? (3) How does a registry entry become procurement/audit evidence? (4) Design the one-screen comparison a non-technical committee can read.

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| Runs with complete lineage tags | Reproducibility | 100% (4/4 tags) | MLflow tag audit |
| Champion meets operations SLA | Correctness | overall ≤ 3.0% AND worst-area ≤ 3.5% | tracked metrics |
| Registered model has signature + example | Governance | 100% | registry Schema tab |
| Time to answer "which model is in Staging + why" | Operability | < 1 min | live UI navigation |
| Reproducible from registry entry alone | Reproducibility | Yes (reach data + code from version) | lineage click-through |
| Champion selection is recorded | Governance | `selection_reason` tag present | tag inspection |

**Example benchmark table:**

| Run | mape_overall | mape_worst_area | retrain time | eligible? | note |
|---|---|---|---|---|---|
| lgbm-baseline | 3.4% | 4.1% (Southern) | 4 s | no | fails per-area SLA |
| lgbm-tuned-A | 2.7% | 3.3% | 6 s | yes | **champion** |
| lgbm-tuned-B | 2.6% | 3.9% (Southern) | 9 s | no | best overall but fails a region |

## Required Visuals and Training Assets

### Diagrams
1. **Run anatomy** — *Purpose:* fix the vocabulary. *Elements:* a run box exploded into params / metrics / artefacts / tags, with Tayyār examples in each. *Style:* labelled exploded box.
2. **Tracking → registry → serving flow** — *Elements:* experiment (many runs) → champion selection gate → registered model (versions + stages/aliases) → arrow to serving (loads `@production`). *Style:* left-to-right pipeline with a human-gate icon at promotion.
3. **Lineage chain** — *Elements:* Production model version → run → metrics/params → data version (DVC) → code SHA (git); the whole chain highlighted as "audit evidence". *Style:* linked-nodes chain.
4. **Champion-vs-challenger staging** — *Elements:* `@champion` and `@challenger` aliases on two versions; auto-promotion rule when challenger wins. *Style:* two-lane comparison with a gate.

### Images
1. **MLflow run-comparison screenshot** (parallel coordinates) — *why:* how a champion is chosen; *content:* three runs, per-area MAPE columns, the divergence highlighted.
2. **Registered model page** with versions + `@staging` alias + description — *why:* the governed asset; *content:* version list, alias badge, lineage link.
3. **Model "Schema" tab** showing the inferred signature — *why:* the self-documenting I/O contract; *content:* 11 input columns with dtypes.
4. **Lineage click-through** from version to `git_sha` tag — *why:* reproducibility proof; *content:* the tag panel of the source run.

### Simulations
1. **Metrics without lineage** — *Setup:* branch logging metrics but no tags. *Expected:* a beautiful dashboard that cannot answer "on what data/code?". *Learning objective:* dashboards ≠ reproducibility.
2. **Leakage caught by comparison** — *Setup:* branch `sim-leak` (target leaked into a feature). *Expected:* an implausibly perfect run stands out against realistic ones. *Learning objective:* tracking makes leakage auditable.
3. **Averaged-metric trap** — *Setup:* a model with great overall MAPE but a failing Southern area. *Expected:* the per-area metric exposes it. *Learning objective:* choose against the business criterion.

### Interactive Activities
- **Champion debate (15 min):** groups get a comparison table and must nominate + defend a champion under the SLA; two groups will disagree on the overall-vs-per-area trade-off.
- **Metadata scavenger hunt:** pairs pick a random registered version and race to reach its data version and code SHA; slowest lineage = most improvement to make.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `grid_load_hourly.csv` | Golden-thread dataset (from M1) | CSV | ~35k rows | Training input; reused |
| `hparam_grid.yaml` | Course repo | YAML | 3 configs | The Part-A sweep |
| Pre-seeded `mlruns` (optional) | Course team | MLflow store | ~10 runs | Comparison-UI practice without waiting |

### Demo Requirements
- **Instructor demo:** live-instrument one training run from zero tracking to a registered, staged, signed model in under 10 minutes, narrating each logged field.
- **Student demo:** one pair walks the class through their champion selection and defends it against the per-area SLA.
- **Expected outputs:** every participant has `tayyar-load-forecaster@staging` v1 with full lineage before Day 2 Hour 2.

---

# Module 3 — Data Versioning and Feature Stores

## Module Overview

**Purpose.** A model is a function of its data and features; if those are not versioned, the model is not reproducible no matter how good the code hygiene. This module makes Tayyār's data an immutable, hashed, shareable artefact with DVC, and makes its features a single source of truth shared by training and serving — the primary defence against the most expensive silent bug in ML, training/serving skew.

**Business relevance.** "Show me exactly the data that produced this forecast on 2026-07-01" is a question critical-infrastructure and financial regulators in Saudi Arabia do ask. Git cannot answer it for gigabyte datasets; DVC can. And when a forecast is wrong and costs real reserve-generation money, the first diagnostic question — "did the features change between training and serving?" — can only be answered *no* if a feature store guarantees it. Feature reuse also compounds: a well-built feature store turns each new model from a data-plumbing project into a modelling project.

**Industry use cases.**
- A grid operator must reproduce a disputed day-ahead forecast for a settlement review months later — only a pinned data version + pinned feature logic makes that possible.
- A bank computes "customer 90-day average balance" in fourteen models; a feature store computes it once, consistently, offline for training and online for serving.
- A retail forecaster's "is_promotion_active" feature was computed with pandas in training and a hand-written SQL in serving; they diverged, and the model silently degraded — the exact skew a shared feature module prevents.

**Expected competencies.** Participants can version a dataset with DVC and push it to a remote, wire a DVC pipeline stage, build a single shared feature module imported by both training and serving, materialise offline features, and articulate the offline/online consistency requirement of a feature store.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Version a dataset with DVC and push/pull it from a remote | LO2 |
| 3.2 | Explain why git is wrong for data and how DVC content-addresses it | LO2 |
| 3.3 | Build one shared feature module used by both training and serving | LO2 |
| 3.4 | Materialise offline features and describe the online counterpart | LO2 |
| 3.5 | Diagnose and prevent training/serving skew | LO2, LO5 |

## Technical Content

### 1. Why git fails for data, and what DVC does

Git is built for text diffs of small files. Datasets break it: a 500 MB CSV bloats the repo permanently (git keeps every version's full blob), diffs are meaningless, and clones become punishing. **DVC** solves this by content-addressing:

- `dvc add data/grid_load_hourly.csv` computes the file's hash, moves the file into a local cache, and writes a tiny `grid_load_hourly.csv.dvc` **pointer file** (containing the hash) that *is* committed to git.
- The real bytes live in a **remote** (S3/MinIO/GCS/SSH) that `dvc push` uploads to and `dvc pull` fetches from — keyed by hash, so identical data is stored once (deduplication).
- git now versions a 100-byte pointer; the data version is the hash. `git checkout <old-commit> && dvc pull` reconstructs the *exact* dataset that commit used. **This is the `data_version` tag Module 2's runs logged.**

The mental model to teach: **git tracks the pointer, DVC tracks the bytes, the hash is the version.** A run's `data_version` tag is the DVC hash — that is the link that makes a forecast reproducible.

### 2. DVC pipelines and data lineage

Beyond versioning files, DVC can define a **pipeline** (`dvc.yaml`) of stages with dependencies and outputs — a lightweight, data-aware make:

- Each stage declares `deps` (inputs), `cmd` (what to run), and `outs` (produced artefacts, themselves DVC-tracked).
- DVC hashes deps and outs; `dvc repro` re-runs only stages whose inputs changed — reproducible, cached data transformations.
- This gives **data lineage**: raw → validated → featurised, each step versioned and reproducible. (Module 4's Airflow/Prefect orchestrates *when* pipelines run across a cluster on a schedule; DVC pipelines make the *data transformation* itself reproducible and cache-efficient. They compose — DVC for data lineage, the orchestrator for scheduling and operational concerns.)

### 3. The feature module: one source of truth

The single most important skew-defence in this course: **feature logic lives in exactly one module, imported by both training and serving.** For Tayyār:

- Calendar features (hour, day-of-week, `is_ramadan`, `is_hajj`, `is_holiday`), weather features (temperature, humidity, lags), and load lags (`load_lag_1h`, `load_lag_24h`, `load_lag_168h`) are all defined in `features.py`.
- Training imports it to build the training matrix; the serving API imports the *same* function to featurise an incoming request. If a feature's definition changes, both sides change together, and the `feature_set_version` (logged as a tag in Module 2) bumps.
- Rule: **no feature is ever computed twice.** The moment a serving path re-implements a training feature "for speed", skew is born.

### 4. Offline vs online: the two halves of a feature store

A feature store serves the same feature values in two access patterns:

| | Offline store | Online store |
|---|---|---|
| **Consumer** | Training + batch scoring | Real-time online API |
| **Access** | High-throughput, latency-tolerant | Low-latency point lookups |
| **Backend** | Parquet / warehouse | Redis / key-value |
| **Tayyār example** | Two years of hourly features for training | The last 168 hours of load lags for the next-hour forecast |
| **Consistency requirement** | — | **Same values as offline for the same entity/time** |

The defining property of a feature store is **offline/online consistency**: the `load_lag_24h` a model trained on offline must equal the `load_lag_24h` it is served online. This course builds a *lightweight* feature store (shared feature module + parquet offline + Redis online) to teach the pattern without a heavyweight platform; the concepts transfer directly to Feast, Tecton, or a cloud-native store.

**Point-in-time correctness** (teach the trap, even if lightly implemented): when building training features, you must use only data *available at the prediction time* — joining "yesterday's actual load" into a feature for a forecast that had to be made before yesterday closed is leakage. Time-series features are landmines for this; Tayyār's lags are built with explicit time offsets to stay honest.

### 5. Data validation as a first-class stage

Before data is featurised it must be validated — a bad feed silently corrupts every downstream model:

- **Schema checks:** expected columns, dtypes, and the four operating areas present.
- **Range checks:** `load_mw > 0`, `temp_c` within physical bounds for KSA (-5 to 55 °C), no future timestamps.
- **Freshness/completeness:** no gaps in the hourly index (a missing hour breaks lag features), no duplicated timestamps per area.
- Tools: `pandas`-based assertions, or `pandera`/Great Expectations for declarative schemas. Validation failures *stop the pipeline* (Module 4) rather than training on garbage — fail loud, fail early.

### 6. Common mistakes & production considerations

1. Committing the CSV to git "just this once" — the repo carries it forever; use DVC from data birth.
2. Re-implementing a training feature in the serving code — the classic skew source.
3. No data validation — training silently proceeds on a corrupt or shifted feed.
4. Ignoring point-in-time correctness in time-series features — leakage that looks like brilliance.
5. Storing the DVC remote on a laptop — the team and CI cannot pull; use a shared remote (MinIO/S3).
6. Feature logic that reads config or the clock nondeterministically — features must be pure functions of their inputs (testable, cacheable).

Production: the DVC remote and feature online-store live inside the network boundary in restricted Saudi environments; access control and PDPL retention apply to feature data (a feature can be personal data); large feature sets use a warehouse/lakehouse, but the *contract* — one definition, offline/online consistent, validated, versioned — is identical to the course's lightweight version.

## Code Examples

### The shared feature module (imported by BOTH training and serving)

```python
# src/load_forecast/features.py
"""SINGLE source of truth for Tayyar features.

Imported by training (offline, whole dataframe) AND serving (online, one
request). Never re-implement a feature elsewhere: that is training/serving skew.
Pure functions only — no clock, no config, no I/O.
"""
from __future__ import annotations
import pandas as pd

# Bump this when feature LOGIC changes; it is logged as a run tag (Module 2).
FEATURE_SET_VERSION = "v2"

FEATURE_COLUMNS = [
    "hour", "dow", "is_weekend", "is_ramadan", "is_hajj", "is_holiday",
    "temp_c", "humidity", "load_lag_1h", "load_lag_24h", "load_lag_168h",
]
TARGET = "load_mw"


def build_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Offline path: featurise a full history dataframe for training.

    Assumes df is sorted by (operating_area, timestamp) with an hourly index.
    """
    df = df.sort_values(["operating_area", "timestamp"]).copy()
    feats = _calendar(df)
    feats = _weather(df, feats)
    feats = _load_lags(df, feats)                    # point-in-time safe lags
    feats = feats.dropna(subset=["load_lag_168h"])   # drop warm-up rows
    X = feats[FEATURE_COLUMNS]
    y = df.loc[X.index, TARGET]
    return X, y


def build_features_online(recent: pd.DataFrame, now: pd.Timestamp,
                          weather_forecast: dict) -> pd.DataFrame:
    """Online path: featurise ONE next-hour request for ONE area.

    `recent` = last >=168h of actuals for the area; `weather_forecast` = the
    forecast temp/humidity for the target hour. Reuses the SAME helpers.
    """
    row = {
        "hour": now.hour,
        "dow": now.dayofweek,
        "is_weekend": int(now.dayofweek >= 5),        # Fri/Sat in KSA calendar
        "is_ramadan": int(_is_ramadan(now)),
        "is_hajj": int(_is_hajj(now)),
        "is_holiday": int(_is_holiday(now)),
        "temp_c": weather_forecast["temp_c"],
        "humidity": weather_forecast["humidity"],
        "load_lag_1h": _lag(recent, now, hours=1),
        "load_lag_24h": _lag(recent, now, hours=24),
        "load_lag_168h": _lag(recent, now, hours=168),
    }
    return pd.DataFrame([row])[FEATURE_COLUMNS]


def _calendar(df: pd.DataFrame) -> pd.DataFrame:
    ts = df["timestamp"]
    return pd.DataFrame({
        "hour": ts.dt.hour, "dow": ts.dt.dayofweek,
        "is_weekend": (ts.dt.dayofweek >= 5).astype(int),
        "is_ramadan": ts.map(_is_ramadan).astype(int),
        "is_hajj": ts.map(_is_hajj).astype(int),
        "is_holiday": ts.map(_is_holiday).astype(int),
    }, index=df.index)


def _weather(df, feats):
    feats["temp_c"] = df["temp_c"]
    feats["humidity"] = df["humidity"]
    return feats


def _load_lags(df, feats):
    # groupby area so lags never cross operating areas
    g = df.groupby("operating_area")["load_mw"]
    feats["load_lag_1h"] = g.shift(1)
    feats["load_lag_24h"] = g.shift(24)
    feats["load_lag_168h"] = g.shift(168)            # one week ago, same hour
    return feats


def _lag(recent: pd.DataFrame, now: pd.Timestamp, hours: int) -> float:
    target = now - pd.Timedelta(hours=hours)
    hit = recent.loc[recent["timestamp"] == target, "load_mw"]
    if hit.empty:
        raise ValueError(f"missing lag-{hours}h actual at {target}")
    return float(hit.iloc[0])


# Calendar helpers (Hijri-aware); stubbed here, provided in course repo.
def _is_ramadan(ts) -> bool: ...
def _is_hajj(ts) -> bool: ...
def _is_holiday(ts) -> bool: ...
```

### DVC: version the data and define a pipeline

```bash
# One-time: initialise DVC and configure a shared MinIO remote
dvc init
dvc remote add -d minio s3://tayyar-data
dvc remote modify minio endpointurl http://localhost:9000

# Version the raw dataset: bytes -> cache, pointer -> git
dvc add data/grid_load_hourly.csv
git add data/grid_load_hourly.csv.dvc data/.gitignore
git commit -m "data: version grid_load_hourly v1 (2 years, 4 areas)"
dvc push                                  # bytes to the remote

# Print the data version (the hash that runs tag as data_version)
dvc get-url data/grid_load_hourly.csv.dvc 2>/dev/null || \
  python -c "import yaml;print(yaml.safe_load(open('data/grid_load_hourly.csv.dvc'))['outs'][0]['md5'])"
```

```yaml
# dvc.yaml — a reproducible data pipeline (validate -> featurise)
stages:
  validate:
    cmd: python -m load_forecast.data.validate data/grid_load_hourly.csv
    deps:
      - data/grid_load_hourly.csv
      - src/load_forecast/data/validate.py
    outs:
      - data/validated.flag

  featurise:
    cmd: python -m load_forecast.data.materialise data/grid_load_hourly.csv data/features_offline.parquet
    deps:
      - data/validated.flag
      - src/load_forecast/features.py
      - src/load_forecast/data/materialise.py
    outs:
      - data/features_offline.parquet          # DVC-tracked offline feature store
```

### Data validation stage (stops the pipeline on bad data)

```python
# src/load_forecast/data/validate.py
"""Validate the load feed BEFORE it can corrupt a model. Fail loud."""
import sys
import pandas as pd

AREAS = {"CENTRAL", "WESTERN", "EASTERN", "SOUTHERN"}


def validate(path: str) -> None:
    df = pd.read_csv(path, parse_dates=["timestamp"])
    problems: list[str] = []

    expected = {"timestamp", "operating_area", "load_mw", "temp_c", "humidity"}
    missing = expected - set(df.columns)
    if missing:
        problems.append(f"missing columns: {missing}")

    if set(df["operating_area"].unique()) != AREAS:
        problems.append(f"unexpected areas: {set(df['operating_area'].unique())}")

    if (df["load_mw"] <= 0).any():
        problems.append("non-positive load_mw present")
    if not df["temp_c"].between(-5, 55).all():
        problems.append("temp_c outside physical KSA bounds (-5..55C)")
    if (df["timestamp"] > pd.Timestamp.utcnow()).any():
        problems.append("future timestamps present (possible feed error)")

    # completeness: no missing hours per area (lags depend on it)
    for area, g in df.groupby("operating_area"):
        idx = pd.date_range(g["timestamp"].min(), g["timestamp"].max(), freq="h")
        if len(idx) != g["timestamp"].nunique():
            problems.append(f"gaps in hourly index for {area}")

    if problems:
        print("DATA VALIDATION FAILED:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)                              # stops dvc repro / the DAG

    open("data/validated.flag", "w").write("ok")
    print(f"validation passed: {len(df):,} rows, {df['operating_area'].nunique()} areas")


if __name__ == "__main__":
    validate(sys.argv[1])
```

## Hands-on Lab 3 — Version the Data and Build the Feature Store

| | |
|---|---|
| **Objective** | Put `grid_load_hourly.csv` under DVC with a shared remote; build the single shared `features.py`; materialise the offline feature parquet via a DVC pipeline; prove training and serving compute identical features |
| **Duration** | 50 minutes |
| **Setup** | `make platform-up` (MinIO running), Lab 2 solution, `git checkout lab3-start`, `pip install dvc[s3] pandas pyarrow` |

**Tasks**
1. *(8 min)* `dvc init`; add the MinIO remote; `dvc add` the dataset; commit the pointer; `dvc push`. Print and record the `data_version` hash.
2. *(12 min)* Complete `features.py`: implement the three load-lag features and the calendar features; ensure `build_features` and `build_features_online` call the *same* helpers.
3. *(10 min)* Write a skew test: featurise one row via the offline path and via the online path; assert every feature column is bit-identical (`tests/test_no_skew.py`).
4. *(10 min)* Implement `validate.py` checks; add the `validate` + `featurise` stages to `dvc.yaml`; run `dvc repro`; confirm `features_offline.parquet` is produced and DVC-tracked.
5. *(5 min)* Re-run `dvc repro` unchanged → confirm all stages report "cached" (nothing re-runs). Edit one line in `features.py` → confirm only `featurise` re-runs.
6. *(5 min)* Update the Module-2 training run's `data_version` tag to the real DVC hash; commit `feat(data): dvc versioning + shared feature store + validation`.

**Expected outputs**
```
$ dvc add data/grid_load_hourly.csv && dvc push
data_version (md5): 7c1e9a4f2b...  (bytes pushed to minio)

$ pytest tests/test_no_skew.py -q
1 passed   # offline and online features identical

$ dvc repro
Running stage 'validate': validation passed: 35,040 rows, 4 areas
Running stage 'featurise': wrote data/features_offline.parquet (34,368 rows)

$ dvc repro           # second run
Stage 'validate' didn't change, skipping
Stage 'featurise' didn't change, skipping
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| `dvc push` fails auth | MinIO creds unset | Export `AWS_ACCESS_KEY_ID/SECRET` from `platform.env` |
| Skew test fails on `is_weekend` | Online path used `>=6` (Sun) not `>=5` | KSA weekend = Fri/Sat (dow 4/5 depending on convention); align both paths |
| `dvc repro` re-runs everything | `outs`/`deps` misdeclared | Ensure `features.py` is a dep of `featurise`; check the flag file |
| Lag feature all-NaN | Data not sorted by (area, timestamp) | Sort before `groupby.shift`; discuss why order matters |
| Validation passes on gapped data | Completeness check skipped | The per-area date_range check is the fix; seed a gap to prove it |

**Instructor notes.** The skew test is the emotional core: seed 2–3 repos where the online path subtly differs (e.g. `is_ramadan` computed from Gregorian month) so the test genuinely fails somewhere in the room — a real red beats a slide. When `dvc repro` correctly re-runs *only* `featurise` after a feature edit, pause and connect it to Module 4: this cache-awareness is what makes automated retraining cheap.

## Mini Exercises

**Quiz.** (1) What does git commit when you `dvc add` a file? → the tiny `.dvc` pointer (hash), not the bytes. (2) Where do the bytes go? → the DVC cache, then the remote on `dvc push`. (3) Why is one shared feature module the skew defence? → training and serving compute identical values by construction. (4) Offline vs online store — one consumer each. → training/batch vs real-time API. (5) What is point-in-time correctness? → using only data available at prediction time; no future leakage.

**Debugging exercise.** Branch `sim-skew-online`: serving computes `load_lag_24h` from a rolling mean instead of the exact 24h-ago value. The skew test catches it; participants fix by reusing the shared helper and explain why "approximately equal" is not acceptable for a versioned feature.

**Code-review exercise.** Review a PR that commits a 480 MB CSV to git, computes `is_holiday` inline in the training script (not in `features.py`), and skips validation. Three findings + the reproducibility/skew argument.

**Discussion.** Your online store must serve `load_lag_168h` (a week of history) at 20 ms. Where does that data live and how is it kept consistent with the offline parquet used for training?

## Case Study — The Feature That Was Computed Twice at a Retail Forecaster

**Scenario.** A Saudi grocery chain forecasts store-level demand to optimise inventory. Training computed `days_since_last_promo` in a pandas pipeline; the serving service, built by a different team six months later, computed it with a hand-written SQL query. The two disagreed on the boundary (inclusive vs exclusive of the promo end date) — a one-day difference that shifted demand forecasts enough to over-stock perishables during Ramadan.

**Business context.** Perishable waste is a direct cost and a sustainability KPI; the divergence cost an estimated SAR 1.3M in spoilage over one Ramadan before the skew was found.

**Technical challenge.** Prove the skew exists, quantify it, and re-architect so the class of bug is impossible — without freezing either the training or serving team.

**Constraints.** Two teams, two languages (Python training, SQL serving); the serving path had a latency budget that "justified" the reimplementation; historical forecasts had to remain reproducible for the waste audit.

**Solution approach.** Build one feature definition as the source of truth; the online path reads *materialised* feature values from a store rather than recomputing (satisfying latency without reimplementation); a shared skew test runs in both teams' CI comparing offline and online values on a shared entity sample; the boundary rule is written down once and versioned. Historical reproducibility is restored by DVC-versioning the training data and pinning the feature-set version to each past model.

**Discussion questions.** (1) Why did the latency argument *not* justify reimplementation — what alternative meets latency without skew? (2) How do you quantify the business cost of a one-day feature boundary error? (3) Where does the skew test live so both teams cannot bypass it? (4) How does DVC restore reproducibility of the *past* forecasts under audit?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Dataset under version control | Reproducibility | 100% (git tracks pointer, bytes in remote) | `dvc status`, remote listing |
| Offline/online feature parity | Correctness | 0 differing columns | skew test |
| DVC pipeline cache-hit on no-change | Efficiency | 100% stages skipped | `dvc repro` output |
| Data validation coverage | Reliability | schema + range + completeness all enforced | `validate.py` review |
| Feature logic duplicated | Code quality | 0 (single module) | grep/review |
| Run traceable to exact data version | Reproducibility | 100% (data_version tag = DVC hash) | MLflow tag audit |

**Example benchmark table:**

| Snapshot | Data in git | Data version resolvable | Skew test | Validation | Offline features |
|---|---|---|---|---|---|
| Tayyār before M3 | 480 MB CSV in git | no (no hash) | n/a | none | recomputed ad hoc |
| Tayyār after M3 | 100-byte pointer | yes (DVC md5) | pass | schema+range+completeness | parquet, DVC-tracked |

## Required Visuals and Training Assets

### Diagrams
1. **DVC content-addressing flow** — *Purpose:* demystify DVC. *Elements:* CSV → hash → cache; pointer `.dvc` → git; bytes → remote; `dvc pull` reconstructs. *Style:* split showing git-lane (pointer) vs DVC-lane (bytes) with the hash linking them.
2. **Training/serving skew (before/after)** — *Purpose:* motivate the shared module. *Elements:* "before" = two divergent feature boxes with a warning; "after" = one `features.py` imported by both paths. *Style:* before/after split panel (reuse M-course palette).
3. **Offline vs online feature store** — *Elements:* one feature definition feeding a parquet (offline, training) and a Redis (online, serving), with a "must be consistent" bar linking them. *Style:* two-lane with a consistency clamp.
4. **Data pipeline lineage** — *Elements:* raw → validate → featurise as DVC stages with hashes; `dvc repro` re-running only changed stages. *Style:* staged pipeline with cache badges.

### Images
1. **`.dvc` pointer file + `dvc status`** — *why:* the pointer-not-bytes mental model; *content:* the tiny YAML hash and a clean status.
2. **MinIO bucket screenshot** with hashed objects — *why:* where the bytes live; *content:* content-addressed blobs under `tayyar-data`.
3. **Skew test failure/pass screenshot** — *why:* the core proof; *content:* pytest output for `test_no_skew`.
4. **`dvc repro` cached run** — *why:* cache-awareness; *content:* "didn't change, skipping" lines.

### Simulations
1. **Git-bloat regret** — *Setup:* branch that committed the CSV to git. *Expected:* clone time and `.git` size balloon; history cannot be un-fattened easily. *Learning objective:* use DVC from data birth.
2. **Silent online skew** — *Setup:* branch `sim-skew-online` (rolling-mean lag). *Expected:* skew test red; forecasts drift subtly with no error. *Learning objective:* skew is silent; only shared code/tests catch it.
3. **Bad-feed guard** — *Setup:* inject a gap + a negative load into the CSV. *Expected:* `validate` stops the pipeline with named problems. *Learning objective:* validation as a gate, not a suggestion.

### Interactive Activities
- **Feature-store card sort (10 min):** 12 features sorted into offline-only / online-needed / both, with the latency + freshness justification.
- **Point-in-time hunt (15 min):** given six candidate features, pairs flag which risk future leakage and rewrite the time offsets.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `grid_load_hourly.csv` | Golden-thread dataset | CSV | ~35k rows | DVC-versioned source |
| `features_offline.parquet` | Produced by the `featurise` stage | Parquet | ~34k rows | Offline feature store; training input |
| `bad_feed.csv` | Course team (gaps + bad values) | CSV | small | Validation simulation |

### Demo Requirements
- **Instructor demo:** live `dvc add`/`push`, then a two-line edit to `features.py` and `dvc repro` showing selective re-run; then a live skew test going red then green.
- **Student demo:** one pair shows their skew test and explains the boundary bug it would catch.
- **Expected outputs:** every participant has DVC-versioned data (pushed), a passing skew test, and a materialised offline feature parquet before Day 2 Hour 4.

---

# Module 4 — Pipeline Orchestration and Automation

## Module Overview

**Purpose.** Modules 2 and 3 gave Tayyār tracked experiments and versioned data; this module removes the human from the *toil* of running training. Participants author an orchestrated pipeline — ingest → validate → featurise → train → evaluate → register — that runs on a schedule or a trigger, retries transient failures, and is idempotent. This is the "ML pipeline automation" that defines Level 1 and the machinery that continuous training (CT) rides on.

**Business relevance.** A manual retrain is a manual incident: someone remembers, finds the right data, runs the right script, and hopes. For a load forecaster that must track a shifting summer, a manual cadence means the model is stale exactly when accuracy matters most. Orchestration turns retraining into infrastructure — scheduled, monitored, retryable, auditable — which is what lets a small Saudi ML team operate many models without heroics, and what gives auditors a run history to inspect.

**Industry use cases.**
- A grid operator retrains the load forecaster weekly and after any validated data-quality fix; the orchestrator guarantees the retrain ran, on the right data, with a recorded outcome.
- A bank's nightly risk-model pipeline must be idempotent (a re-run after a 2 a.m. failure must not double-count) and must page on failure with a diagnosable log.
- A telecom's churn pipeline fans out per-region training tasks in parallel and gates registration on an evaluation task — exactly the DAG shape Tayyār uses.

**Expected competencies.** Participants can model a training workflow as a DAG of idempotent tasks, configure schedules/triggers/retries, pass data between tasks via the versioned stores (not by smuggling large objects), gate model registration on an evaluation task, and diagnose a failed run from the orchestrator UI and logs.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Model a training workflow as a DAG of tasks with dependencies | LO4 |
| 4.2 | Configure schedules, triggers, retries, and idempotency | LO4 |
| 4.3 | Gate model registration on an automated evaluation task | LO4, LO2 |
| 4.4 | Distinguish CI, CD, and CT and place the pipeline in the CT loop | LO4 |
| 4.5 | Diagnose a failed pipeline run from the orchestrator UI and logs | LO4 |

## Technical Content

### 1. DAGs, tasks, and why orchestration exists

An orchestrator (Airflow, Prefect, Dagster…) runs a **DAG** — a directed acyclic graph of **tasks** — handling scheduling, dependency ordering, retries, parallelism, logging, and alerting so you do not hand-roll a fragile cron chain. The core vocabulary:

- **Task:** a unit of work (e.g. `validate_data`). Should be *idempotent* (safe to re-run) and *single-purpose*.
- **Dependency:** `featurise >> train >> evaluate >> register` — the edges of the DAG; a task runs only after its upstreams succeed.
- **Schedule:** cron-like cadence (`@weekly`) or event/trigger-based.
- **Run (DAG run):** one execution for a logical date; the orchestrator tracks its state and history — the audit trail Level 1 requires.

Airflow vs Prefect (teach the choice, not dogma): Airflow is the incumbent, config-as-DAG, strong scheduling and enterprise footprint (common in Saudi banks); Prefect is Pythonic, dynamic, lighter to start. The *concepts* — DAG, task, retry, schedule, idempotency — are identical. The course provides both a `dags/train_tayyar.py` (Airflow) and a `flows/train_tayyar.py` (Prefect); pick per classroom infrastructure.

### 2. Idempotency and passing data the right way

Two rules separate robust pipelines from flaky ones:

- **Idempotency:** re-running a task (after a retry or a manual backfill) must not corrupt state. Write to a *deterministic, run-scoped* location and overwrite, don't append; register by *content*, not by "append a new version every time regardless". A pipeline you cannot safely re-run is a pipeline you cannot operate.
- **Pass references, not payloads:** tasks should exchange *pointers* (a DVC data version, an MLflow `run_id`, a parquet path) — never push a 300 MB dataframe through the orchestrator's metadata backend (Airflow XCom / Prefect results). The stores from Modules 2–3 *are* the inter-task channel. This keeps the orchestrator light and the lineage explicit.

### 3. The Tayyār training DAG

The canonical pipeline every participant builds:

```
ingest ─► validate ─► featurise ─┬─► train ─► evaluate ─► register(if SLA met)
                                 │
        (validate FAILS ⇒ stop, alert, no training on bad data)
```

- **ingest:** pull the latest hourly load+weather (in the course, refresh the DVC-tracked CSV).
- **validate:** the Module-3 checks; failure short-circuits the DAG (no training on garbage).
- **featurise:** materialise the offline feature parquet via the shared `features.py`.
- **train:** the Module-2 tracked training; emits an MLflow `run_id`.
- **evaluate:** compute the operations SLA (overall + per-area MAPE) on a holdout; this is the **automated gate**.
- **register:** only if the SLA is met *and* the challenger beats the current champion — otherwise the DAG succeeds but *records* "candidate rejected, no promotion" (a legitimate, logged outcome).

### 4. Scheduling, triggers, and CT

The pipeline becomes *continuous training* when its trigger is automated:

- **Schedule:** `@weekly` keeps Tayyār fresh against gradual seasonal shift.
- **Data trigger:** a validated new data drop (e.g. a corrected feed) triggers a retrain.
- **Drift trigger:** the Module-6 monitoring job opens a retraining trigger when MAPE decays — this is the closed loop that defines Level 2. The DAG exposes a `workflow_dispatch`-style manual/API trigger so monitoring can fire it.
- **Guardrail:** automated *training* is safe; automated *promotion to production* stays gated by the evaluation SLA and (for Tayyār) a human ops approval until monitoring earns trust. Automate the toil, gate the judgement.

### 5. Reliability: retries, alerting, SLAs

- **Retries with backoff** for transient failures (a flaky data pull); but *not* infinite retries on a deterministic failure (bad data will fail every time — alert, don't loop).
- **Alerting:** on failure, page the owning team with the run link and the failing task's log — not a bare "DAG failed" email.
- **SLA/timeout:** a training task that normally takes 2 minutes but runs 30 is a symptom; set timeouts so a hung task fails loudly.
- **Observability:** the orchestrator UI is the operability surface — task duration trends, failure rates, and the Gantt view are where you diagnose "why is Thursday's retrain slow?".

### 6. Common mistakes & production considerations

1. One giant task that does everything — no retry granularity, no parallelism, no diagnosability. Split by responsibility.
2. Pushing large dataframes through XCom/results — the metadata DB bloats and slows; pass references.
3. Non-idempotent tasks — a re-run double-registers or corrupts; write deterministically.
4. No evaluation gate — the pipeline auto-registers a worse model because "it ran".
5. Infinite retries on deterministic failures — the pipeline "self-heals" by spinning forever on bad data.
6. Secrets in the DAG file — use the orchestrator's connections/secrets backend (ties to Module 6's discipline).
7. Confusing DVC pipelines with the orchestrator — DVC makes the *data transformation* reproducible and cache-efficient; the orchestrator schedules, retries, parallelises, and alerts across the cluster. Use both: the DAG's `featurise` task can invoke `dvc repro`.

Production: enterprise runners inside the network boundary (Saudi banks and critical infrastructure rarely reach public schedulers); backfills for reprocessing history; concurrency limits so a retrain does not starve the cluster; cost visibility (compute-minutes per retrain as a tracked number); and clear ownership so a 2 a.m. failure pages a human who can act.

## Code Examples

### The training DAG (Airflow)

```python
# dags/train_tayyar.py
"""Airflow DAG: ingest -> validate -> featurise -> train -> evaluate -> register.

Tasks pass REFERENCES (data version, run_id) via XCom, never dataframes.
Registration is GATED on the evaluation SLA.
"""
from __future__ import annotations
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator

from load_forecast.data.validate import validate
from load_forecast.data.materialise import materialise
from load_forecast.training.train import train
from load_forecast.training.evaluate import evaluate_sla
from load_forecast.training.register import register_and_stage

DATA_PATH = "data/grid_load_hourly.csv"
FEATURES_PATH = "data/features_offline.parquet"

default_args = {
    "owner": "mlops-tayyar",
    "retries": 2,
    "retry_delay": timedelta(minutes=1),      # backoff for TRANSIENT failures
    "retry_exponential_backoff": True,
    "execution_timeout": timedelta(minutes=15),
}


def _ingest(**ctx):
    # In prod: pull latest hourly feed. In course: refresh + return DVC version.
    import subprocess
    subprocess.check_call(["dvc", "pull", f"{DATA_PATH}.dvc"])
    version = subprocess.check_output(
        ["dvc", "get-url", f"{DATA_PATH}.dvc"]).decode().strip() or "v1"
    ctx["ti"].xcom_push(key="data_version", value=version)


def _validate(**_):
    validate(DATA_PATH)                        # exits non-zero => task fails


def _featurise(**_):
    materialise(DATA_PATH, FEATURES_PATH)      # shared features.py (M3)


def _train(**ctx):
    data_version = ctx["ti"].xcom_pull(key="data_version")
    params = {"n_estimators": 800, "learning_rate": 0.05, "num_leaves": 64}
    run_id = train(DATA_PATH, params, data_version=data_version)
    ctx["ti"].xcom_push(key="run_id", value=run_id)


def _evaluate_branch(**ctx):
    run_id = ctx["ti"].xcom_pull(key="run_id")
    passed = evaluate_sla(run_id)              # overall<=3.0% AND worst-area<=3.5%
    return "register" if passed else "reject_candidate"


def _register(**ctx):
    run_id = ctx["ti"].xcom_pull(key="run_id")
    register_and_stage(run_id, note="Auto-registered by weekly CT pipeline")


with DAG(
    dag_id="train_tayyar",
    schedule="@weekly",                        # CT cadence; also API-triggerable
    start_date=datetime(2026, 1, 1),
    catchup=False,
    default_args=default_args,
    tags=["tayyar", "training", "ct"],
) as dag:
    ingest = PythonOperator(task_id="ingest", python_callable=_ingest)
    validate_t = PythonOperator(task_id="validate", python_callable=_validate)
    featurise = PythonOperator(task_id="featurise", python_callable=_featurise)
    train_t = PythonOperator(task_id="train", python_callable=_train)
    gate = BranchPythonOperator(task_id="evaluate", python_callable=_evaluate_branch)
    register = PythonOperator(task_id="register", python_callable=_register)
    reject = EmptyOperator(task_id="reject_candidate")   # logged non-promotion

    ingest >> validate_t >> featurise >> train_t >> gate >> [register, reject]
```

### The same pipeline in Prefect (for classrooms using Prefect)

```python
# flows/train_tayyar.py
"""Prefect flow: same DAG, Pythonic dynamic style. Pick ONE orchestrator."""
from prefect import flow, task, get_run_logger

from load_forecast.data.validate import validate
from load_forecast.data.materialise import materialise
from load_forecast.training.train import train
from load_forecast.training.evaluate import evaluate_sla
from load_forecast.training.register import register_and_stage


@task(retries=2, retry_delay_seconds=60)
def ingest() -> str:
    import subprocess
    subprocess.check_call(["dvc", "pull", "data/grid_load_hourly.csv.dvc"])
    return "v1"


@task
def validate_step():
    validate("data/grid_load_hourly.csv")


@task
def featurise_step():
    materialise("data/grid_load_hourly.csv", "data/features_offline.parquet")


@task
def train_step(data_version: str) -> str:
    return train("data/grid_load_hourly.csv",
                 {"n_estimators": 800, "learning_rate": 0.05, "num_leaves": 64},
                 data_version=data_version)


@flow(name="train_tayyar", log_prints=True)
def train_tayyar():
    log = get_run_logger()
    data_version = ingest()
    validate_step()
    featurise_step()
    run_id = train_step(data_version)
    if evaluate_sla(run_id):
        register_and_stage(run_id, note="Auto-registered by Prefect CT flow")
        log.info("candidate PROMOTED to @staging")
    else:
        log.warning("candidate REJECTED: fails operations SLA; no promotion")


if __name__ == "__main__":
    train_tayyar()
```

### The evaluation gate (the automated SLA check)

```python
# src/load_forecast/training/evaluate.py
"""The automated gate: a run is promotable only if it meets the operations SLA
AND beats the incumbent champion. Returns a bool the DAG branches on."""
import mlflow
from mlflow.tracking import MlflowClient

MODEL_NAME = "tayyar-load-forecaster"
OVERALL_CEILING = 0.030
PER_AREA_CEILING = 0.035


def evaluate_sla(run_id: str) -> bool:
    client = MlflowClient()
    m = client.get_run(run_id).data.metrics
    meets_sla = (m["mape_overall"] <= OVERALL_CEILING
                 and m["mape_worst_area"] <= PER_AREA_CEILING)
    if not meets_sla:
        return False

    # Beat the incumbent, if any (champion-vs-challenger).
    try:
        champ = client.get_model_version_by_alias(MODEL_NAME, "production")
        champ_mape = client.get_run(champ.run_id).data.metrics["mape_overall"]
        return m["mape_overall"] <= champ_mape         # tie -> keep incumbent? no, allow
    except Exception:
        return True                                    # no incumbent yet
```

## Hands-on Lab 4 — Build the Training DAG

| | |
|---|---|
| **Objective** | Author and run the Tayyār training pipeline end-to-end in Airflow (or Prefect): ingest → validate → featurise → train → evaluate → register, with retries, an SLA gate, and reference-passing between tasks |
| **Duration** | 50 minutes |
| **Setup** | `make platform-up` (orchestrator + MLflow + MinIO), Lab 3 solution, `git checkout lab4-start` |

**Tasks**
1. *(8 min)* Wire the DAG skeleton: five tasks with the correct dependency edges; trigger a manual run; watch it in the UI.
2. *(10 min)* Implement reference-passing: `ingest` pushes `data_version`; `train` pulls it and pushes `run_id`; confirm no dataframe crosses XCom/results.
3. *(10 min)* Implement the `evaluate` gate as a branch: promote on SLA-pass, route to `reject_candidate` on fail. Test both paths by tweaking the SLA ceiling.
4. *(8 min)* Break `validate` on purpose (feed the `bad_feed.csv`); confirm the DAG stops at `validate`, `train` never runs, and the failure is diagnosable from the task log.
5. *(8 min)* Add retries + a timeout; simulate a transient ingest failure (provided flaky flag) and watch a retry succeed; contrast with the deterministic validate failure that correctly does *not* self-heal.
6. *(6 min)* Set the schedule to `@weekly`; confirm the next run is scheduled; commit `feat(orchestration): tayyar CT training DAG with SLA gate`.

**Expected outputs**
```
DAG run (green):  ingest ✓ validate ✓ featurise ✓ train ✓ evaluate ✓ → register ✓
                  MLflow: new run + tayyar-load-forecaster v2 @staging

Bad-feed run:     ingest ✓ validate ✗ (non-positive load_mw) → train SKIPPED
                  alert fired with task-log link; no model registered

Rejected candidate: ... evaluate → reject_candidate (worst-area MAPE 3.8% > 3.5%)
                    DAG SUCCEEDS, logs "no promotion"
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| XCom "object too large" | Pushing a dataframe | Push the parquet path / run_id instead |
| `register` runs after a bad `validate` | Missing branch/short-circuit | Use the branch operator; validate must gate |
| DAG re-run double-registers | Non-idempotent register | Register by content / guard duplicate; overwrite run-scoped outs |
| Transient failure not retried | Retries unset on the task | Set `retries` + backoff at task/default level |
| Infinite retries on bad data | Retrying a deterministic failure | Distinguish transient vs deterministic; alert, don't loop |

**Instructor notes.** The two failure demos are the lesson: (a) `validate` failing on bad data and correctly stopping the DAG, and (b) a *rejected candidate* where the DAG *succeeds* but promotes nothing. Participants instinctively think "green = new model shipped" — break that instinct here, because Module 7's release safety depends on it. Fast finishers: wire an API/`workflow_dispatch` trigger so Module 6's monitoring job can fire this DAG (previews the CT loop).

## Mini Exercises

**Quiz.** (1) What makes a task idempotent and why does it matter? → safe to re-run; retries/backfills won't corrupt. (2) Why pass references not payloads between tasks? → keeps the metadata backend light; lineage explicit. (3) Where is the promotion gate in the DAG? → the `evaluate` task, before `register`. (4) Transient vs deterministic failure — different handling? → retry transient; alert on deterministic. (5) What turns this pipeline into CT? → an automated trigger (schedule/data/drift).

**Debugging exercise.** A DAG "succeeds" nightly but the model never improves. Root cause: `evaluate` always returns True (SLA ceilings set to 1.0). Participants must find the disabled gate and restore the real ceilings — and discuss how a too-loose gate is worse than no gate (false confidence).

**Code-review exercise.** Review a DAG PR with one mega-task, a hard-coded secret, a dataframe in XCom, and `retries=100`. Four findings + the operability argument.

**Discussion.** Your bank forbids the scheduler from reaching the internal model registry. Which tasks move to self-hosted runners inside the boundary, and what new failure modes appear?

## Case Study — The 2 a.m. Retrain Nobody Could Diagnose

**Scenario.** A Saudi logistics firm's demand-forecast retrain ran nightly via a chain of cron jobs and a shell script. One night it silently produced a broken model; the on-call engineer got a "job failed" text with no context, spent three hours reconstructing which step failed, and discovered a transient S3 hiccup that a retry would have healed.

**Business context.** The broken model skewed next-day vehicle allocation; the cost of the outage plus the three-hour diagnosis dwarfed the effort of proper orchestration.

**Technical challenge.** Replace the cron chain with an orchestrated DAG that retries transient failures, alerts with context, is idempotent under re-run, and exposes a diagnosable run history.

**Constraints.** The team is three engineers; the pipeline touches an internal registry unreachable from public runners; historical nightly runs must remain auditable for a client SLA; no budget for a heavyweight managed platform initially.

**Solution approach.** Model the cron steps as DAG tasks; add retries+backoff for the S3/transient steps and *no* retries for deterministic validation; alert with the failing task's log link; make the register step idempotent; run on a self-hosted worker inside the boundary; keep the DAG-run history as the SLA audit trail. Start with the lighter orchestrator, migrate later if scale demands.

**Discussion questions.** (1) Which of the failures in the story would retries have healed, and which would they have masked dangerously? (2) What single piece of context in the alert would have saved the three hours? (3) How does DAG-run history satisfy the client SLA audit? (4) When is a cron chain actually fine, and when is it negligence?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Pipeline runs end-to-end unattended | Automation | 100% (green run, no manual steps) | DAG run history |
| Registration gated on SLA | Governance | Auto-register only if SLA met + beats champion | branch logic + logs |
| Bad data stops the pipeline | Reliability | `validate` failure short-circuits training | forced-failure run |
| Transient failure auto-heals | Reliability | retry succeeds within 2 attempts | flaky-ingest run |
| Data passed as references only | Code quality | 0 dataframes in XCom/results | DAG review |
| Failed-run time-to-diagnose | Operability | ≤ 10 min from UI + logs | lab timing |

**Example benchmark table:**

| Run type | Outcome | Registered? | Notes |
|---|---|---|---|
| Normal weekly | green | yes (v2 @staging) | SLA met, beats champion |
| Bad feed | validate ✗ | no | training skipped, alert with context |
| Rejected candidate | green (branch → reject) | no | worst-area MAPE 3.8% > 3.5% ceiling |
| Transient ingest hiccup | green after 1 retry | yes | backoff healed S3 blip |

## Required Visuals and Training Assets

### Diagrams
1. **The Tayyār training DAG** — *Purpose:* the module anchor. *Elements:* the five tasks with edges; the `evaluate` branch splitting to `register` vs `reject_candidate`; the `validate`-fail short-circuit; a trigger badge (schedule/data/drift). *Style:* left-to-right DAG with a diamond gate.
2. **CI/CD/CT loop** — *Elements:* code change → CI; model artefact → CD; drift/schedule → CT (this DAG) → back into CD. *Style:* three interlocking loops (reuse M1's triad, now concrete).
3. **References-not-payloads** — *Elements:* tasks exchanging small pointers (data_version, run_id, parquet path) while the big artefacts live in DVC/MLflow stores. *Style:* thin arrows (pointers) vs a crossed-out fat arrow (dataframe).
4. **Retry decision tree** — *Elements:* failure → transient? retry+backoff : alert (no loop). *Style:* compact flowchart.

### Images
1. **Airflow/Prefect graph view (green run)** — *why:* the operability surface; *content:* all tasks green, the branch visible.
2. **Failed-task log with context** — *why:* diagnosability; *content:* `validate` failure naming the bad column + a run link.
3. **Gantt / duration view** — *why:* spotting slow tasks; *content:* task durations across a week of runs.
4. **Scheduled next-run panel** — *why:* CT cadence made real; *content:* `@weekly` with the next execution date.

### Simulations
1. **Bad-data short-circuit** — *Setup:* feed `bad_feed.csv`. *Expected:* DAG stops at `validate`; training never runs. *Learning objective:* validation gates training.
2. **Transient vs deterministic failure** — *Setup:* a flaky-ingest flag (fails once) vs a bad feed (fails always). *Expected:* the first heals on retry; the second must alert, not loop. *Learning objective:* retry semantics.
3. **The disabled gate** — *Setup:* SLA ceilings set to 1.0. *Expected:* every candidate "passes"; a worse model gets promoted. *Learning objective:* a too-loose gate manufactures false confidence.

### Interactive Activities
- **DAG design charrette (15 min):** given a new model's requirements, pairs draw the task graph and mark idempotency + gate points; defend one edge.
- **Alert-writing kata (10 min):** rewrite three useless "job failed" alerts into context-rich, actionable ones.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `grid_load_hourly.csv` (DVC) | Golden thread | CSV | ~35k rows | Pipeline input |
| `bad_feed.csv` | Course team | CSV | small | Validate short-circuit sim |
| `flaky_flag` | Course script | file | — | Transient-failure retry sim |

### Demo Requirements
- **Instructor demo:** trigger a live DAG run end-to-end; then force a bad-feed failure and read the contextful alert; then show a rejected-candidate green run that promotes nothing.
- **Student demo:** one pair walks their branch logic and the two "green but different" outcomes (promoted vs rejected).
- **Expected outputs:** every participant has a green end-to-end DAG run producing a registered `@staging` model before Day 3 begins.

---

# Module 5 — Model Serving: Batch, Online, and Streaming

## Module Overview

**Purpose.** A registered model that nobody can call is a museum piece. This module turns `tayyar-load-forecaster@Staging` into two live consumers of the *same* registered artefact: a **day-ahead batch job** that writes a 24-hour forecast per operating area every night, and a **low-latency online API** that answers a next-hour forecast on demand. Participants load the model from the registry (never from a loose pickle), featurise requests through the *same* `features.py` from Module 3, containerise the service, and read a Kubernetes `Deployment` manifest at the "basics" depth the catalogue specifies. Streaming is taught as the third pattern on the latency/freshness spectrum so participants can place a workload correctly, not so they build a Kafka cluster from scratch.

**Business relevance.** The grid operations center consumes forecasts in two rhythms: the day-ahead unit-commitment meeting needs a full 24-hour curve per area by 18:00 the night before (batch), and the real-time balancing desk wants a next-hour correction on demand as weather and load surprise the plan (online). A single model, served two ways, keeps the two rhythms consistent — the balancing desk and the commitment meeting must never argue over *which* forecast is "the" forecast. Getting serving wrong is where MLOps effort visibly pays or fails: an endpoint that 500s at the evening peak, or a batch job that silently skips the Southern area, is an operations incident, not a modelling footnote.

**Industry use cases.**
- A grid operator serves the same forecaster as an overnight batch (day-ahead planning) and an online API (intraday balancing) — proving one registered model, one feature module, two access patterns.
- A payments provider scores transactions online at 30 ms p99 for authorisation, and re-scores the day's transactions in a nightly batch for investigation queues — same model, two SLAs.
- A ride-hailing platform consumes a demand model as a stream: each new trip event updates a rolling feature and emits a fresh surge multiplier within seconds — the streaming end of the spectrum.

**Expected competencies.** After this module a participant can choose batch vs online vs streaming from latency/throughput/freshness requirements, load a model by registry alias as a `pyfunc`, build a FastAPI online endpoint that featurises through the shared module and logs every prediction, write an idempotent day-ahead batch scorer, containerise the service with a readiness gate on model load, and read/apply a basic Kubernetes `Deployment`+`Service` manifest.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Choose batch, online, or streaming from latency/throughput/freshness requirements | LO3, LO1 |
| 5.2 | Load a model from the registry by alias as a `pyfunc` (no loose pickles) | LO3, LO2 |
| 5.3 | Build an online forecast API that featurises via the shared module and logs predictions | LO3, LO5 |
| 5.4 | Write an idempotent day-ahead batch scorer writing per-area forecasts | LO3 |
| 5.5 | Containerise the service with a readiness gate on model load | LO3 |
| 5.6 | Read and apply a basic Kubernetes Deployment + Service manifest | LO3 |

## Technical Content

### 1. The serving spectrum: batch, online, streaming

The three patterns are points on a spectrum of *how fresh must the prediction be, and how is it requested*:

| | Batch | Online (request/response) | Streaming |
|---|---|---|---|
| **Trigger** | Schedule (e.g. nightly) | Synchronous request | Continuous event flow |
| **Latency** | Minutes–hours (irrelevant per-item) | Milliseconds (p99 matters) | Seconds (near-real-time) |
| **Throughput** | Very high (whole population) | Per-request | High, sustained |
| **Freshness** | As of last run | On demand, now | As events arrive |
| **Tayyār use** | Day-ahead 24h curve per area | Next-hour on-demand correction | (Illustrative) live meter feed re-forecast |
| **Cost shape** | Cheap per prediction, bursty compute | Always-on capacity | Always-on stream infra |

**The decision rule to teach:** start from the *consumer's* need. If a human or system reads predictions on a cadence and can tolerate staleness until the next run → **batch** (cheapest, simplest, most robust). If a caller needs a prediction *for a specific input, now* → **online**. If predictions must react to a continuous event flow within seconds → **streaming**. Most teams over-reach for online/streaming when batch would serve; the first architectural question is always "can this be a batch job?" Tayyār needs both batch (day-ahead) and online (intraday) because it has two genuinely different consumers — that is the justification, not fashion.

### 2. Load from the registry, never from a pickle

Both serving paths load the model the *same* way — by registry URI, resolved through an alias, as a framework-agnostic `pyfunc`:

- **`models:/tayyar-load-forecaster@Staging`** (or `@Production`) is the address. The serving code asks the registry for "whatever version is currently aliased Staging" — it does not hard-code a version number or a file path. This is what makes **rollback a re-point** (Module 7): change the alias, and every serving replica loads the new version on its next refresh.
- **`mlflow.pyfunc.load_model(uri)`** returns a uniform object with a `.predict(DataFrame)` method regardless of the underlying flavour (LightGBM here). The serving code never imports `lightgbm` — clean architecture at the artefact boundary (Module 2's flavour lesson made operational).
- **Load once, at startup**, not per request. Model load is expensive (deserialise + warm); do it during application startup and gate readiness on its success (§5). A model reloaded per request is a self-inflicted latency and memory incident.

### 3. The online forecast API

The online service answers `POST /v1/forecast/next-hour` for one operating area:

- **Strict input contract:** a pydantic model with `extra="forbid"` — an unknown field is a client bug or a probe, not something to silently ignore. The request carries the area, the target hour, and the weather forecast for that hour; the recent-load history is fetched from the online feature store (Redis), not sent by the client.
- **Featurise through the shared module:** the endpoint calls `build_features_online(...)` from Module 3 — the *exact* function training used. This is the skew defence made live: the online path cannot drift from training because it runs training's code.
- **Signature validation at the boundary:** the model's signature (Module 2) validates the feature frame's schema before `predict`; a dtype or column mismatch fails loud with a 422, not a silent wrong answer.
- **Log every prediction:** inputs + output + `model_version` + `trace_id` + timestamp go to the prediction log — this is the *contract the monitoring plane consumes* (Module 6). A serving layer that does not log predictions makes drift detection impossible; prediction logging is not optional instrumentation, it is the CT loop's raw material.
- **Model-version + trace-id response headers:** every response says which model produced it, so an operator can correlate a bad forecast to a registry version instantly.

### 4. The day-ahead batch scorer

The batch job runs nightly and writes a 24-hour forecast per area:

- **Idempotent by run date:** it writes `day_ahead_forecast/date=2026-07-01/forecast.parquet` — a deterministic, partitioned, overwrite-safe location. Re-running the job for the same date reproduces the same file (given the same model + data), never appends duplicates. This is the Module-4 idempotency rule applied to serving output.
- **Same model, same features:** it loads `models:/tayyar-load-forecaster@Production` and featurises through `features.py`. Batch and online *cannot* disagree because they share the model and the feature code.
- **Also logs predictions:** the batch writes to the same prediction-log contract so monitoring sees both paths. A forecast is a forecast whether it came from the API or the batch — monitoring should not care which produced it.
- **Robust to partial failure:** if one area's feature history is incomplete, the job records that area as failed *and continues* the others, rather than aborting the whole night's forecast — a missing Southern history must not blank the Central curve.

### 5. Containerisation and the readiness gate

The service is packaged as a container that does not accept traffic until the model is loaded:

- **`/health` (liveness) vs `/ready` (readiness):** liveness answers "is the process alive?" (restart if not); readiness answers "can it serve a correct forecast *right now*?" — which is **false until the model has loaded from the registry**. Wiring readiness to model-load state is the single most important serving-reliability habit: it stops the orchestrator routing traffic to a replica whose model is still deserialising.
- **Warm-up at startup:** load the model and run one throwaway prediction during startup so the first real request is not the one that pays the JIT/warm cost.
- **Multi-worker for throughput:** run several workers behind the ASGI server; because the model is loaded per worker at startup, memory scales with workers — a real capacity-planning conversation, not an afterthought.
- **Small, non-root image:** a slim base, non-root user, and a healthcheck on `/ready` — the containerisation discipline from the prerequisite course (SDA-AIE-113), now serving a model.

### 6. Kubernetes at "basics" depth, and common mistakes

Kubernetes is taught *read-and-apply*, not authored-from-blank (the catalogue's "basics"):

- A `Deployment` runs N replicas of the image; a `Service` gives them one stable address; a **readiness probe** on `/ready` is what makes rolling updates safe — K8s only sends traffic to replicas that report ready, so a replica whose model failed to load never receives a request. This is the platform-level version of §5's gate and the mechanism Module 7's canary rides on.
- Participants apply a provided manifest against a local `kind`/`minikube` cluster and observe a rolling update; they do not hand-author production manifests.

**Common mistakes**
1. Loading the model per request instead of at startup — latency and memory catastrophe.
2. Re-implementing features in the serving code "for speed" — the training/serving skew Module 3 forbade, reborn at the serving layer.
3. Readiness that returns 200 before the model is loaded — traffic hits a not-ready replica and 500s during every deploy.
4. Not logging predictions — monitoring (Module 6) and the CT loop become impossible.
5. Hard-coding a model *version* or file path instead of an alias — rollback stops being a re-point and becomes a redeploy.
6. Serving online what should be batch — paying always-on cost and complexity for predictions a nightly job would deliver.
7. Batch job that aborts the whole run on one area's bad data — a partial-failure policy is mandatory.

**Production considerations.** In restricted Saudi networks the model registry and image registry live inside the boundary; the serving image pulls the model from the internal MLflow, never a public endpoint. Autoscaling online replicas on the evening-peak load curve, capacity-planning worker memory against model size, and a graceful-shutdown path (exec-form entrypoint, drain in-flight requests) are the operational realities. Batch jobs run as scheduled container jobs (the orchestrator of Module 4 can trigger them) with the same lineage discipline: every forecast row carries the `model_version` that produced it.

## Code Examples

### The online forecast API (loads from registry, featurises via shared module, logs predictions)

```python
# src/load_forecast/serving/api.py
"""Tayyar online next-hour forecast API.

Loads the model from the REGISTRY by alias at startup (never a pickle path),
featurises through the SHARED features module (skew defence), validates against
the model signature, and LOGS every prediction for the monitoring plane (M6).
"""
from __future__ import annotations
import os
import uuid
from contextlib import asynccontextmanager
from datetime import datetime

import mlflow.pyfunc
import pandas as pd
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

from load_forecast.features import build_features_online
from load_forecast.serving.feature_client import recent_load        # Redis online store
from load_forecast.serving.prediction_log import log_prediction

MODEL_URI = os.environ.get("MODEL_URI", "models:/tayyar-load-forecaster@Production")
AREAS = {"CENTRAL", "WESTERN", "EASTERN", "SOUTHERN"}

_state: dict = {"model": None, "model_version": None, "ready": False}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load ONCE at startup; warm it; only then flip readiness true.
    model = mlflow.pyfunc.load_model(MODEL_URI)
    _state["model"] = model
    _state["model_version"] = model.metadata.run_id[:8]
    _warm(model)                                   # first predict pays the warm cost
    _state["ready"] = True
    yield
    _state["ready"] = False                        # drain on shutdown


app = FastAPI(title="tayyar-forecast", lifespan=lifespan)


class ForecastRequest(BaseModel):
    model_config = {"extra": "forbid"}             # unknown field => client bug/probe
    operating_area: str
    target_hour: datetime
    temp_c: float = Field(ge=-5, le=55)            # KSA physical bounds
    humidity: float = Field(ge=0, le=100)


class ForecastResponse(BaseModel):
    operating_area: str
    target_hour: datetime
    load_mw: float
    model_version: str


@app.get("/health")           # liveness: is the process up?
def health():
    return {"status": "alive"}


@app.get("/ready")            # readiness: is the MODEL loaded? gates traffic.
def ready(response: Response):
    if not _state["ready"]:
        response.status_code = 503
        return {"status": "loading_model"}
    return {"status": "ready", "model_version": _state["model_version"]}


@app.post("/v1/forecast/next-hour", response_model=ForecastResponse)
def forecast(req: ForecastRequest, response: Response):
    if not _state["ready"]:
        raise HTTPException(503, "model not loaded")
    if req.operating_area not in AREAS:
        raise HTTPException(422, f"unknown operating_area: {req.operating_area}")

    trace_id = str(uuid.uuid4())
    # Online feature history from the store — NOT sent by the client.
    recent = recent_load(req.operating_area, before=req.target_hour, hours=168)
    # SHARED feature logic: identical to training => no skew.
    X = build_features_online(
        recent, now=req.target_hour,
        weather_forecast={"temp_c": req.temp_c, "humidity": req.humidity})

    try:
        yhat = float(_state["model"].predict(X)[0])   # signature validates schema
    except Exception as exc:                            # dtype/column mismatch => 422
        raise HTTPException(422, f"feature/signature mismatch: {exc}") from exc

    log_prediction(                                     # the M6 monitoring contract
        trace_id=trace_id, operating_area=req.operating_area,
        target_hour=req.target_hour, features=X.iloc[0].to_dict(),
        prediction=yhat, model_version=_state["model_version"])

    response.headers["X-Model-Version"] = _state["model_version"]
    response.headers["X-Trace-Id"] = trace_id
    return ForecastResponse(operating_area=req.operating_area,
                            target_hour=req.target_hour,
                            load_mw=round(yhat, 2),
                            model_version=_state["model_version"])


def _warm(model) -> None:
    dummy = pd.DataFrame([{c: 0.0 for c in
                           ["hour", "dow", "is_weekend", "is_ramadan", "is_hajj",
                            "is_holiday", "temp_c", "humidity",
                            "load_lag_1h", "load_lag_24h", "load_lag_168h"]}])
    try:
        model.predict(dummy)
    except Exception:
        pass                                            # warm-up only; ignore result
```

### The idempotent day-ahead batch scorer

```python
# src/load_forecast/serving/batch.py
"""Day-ahead batch scorer: 24h forecast per operating area, written to a
DETERMINISTIC partitioned path (idempotent), logging predictions like the API.

Partial-failure policy: one area's bad history must NOT blank the others.
"""
from __future__ import annotations
from datetime import datetime, timedelta
from pathlib import Path

import mlflow.pyfunc
import pandas as pd

from load_forecast.features import build_features_online
from load_forecast.serving.feature_client import recent_load
from load_forecast.serving.prediction_log import log_prediction

AREAS = ["CENTRAL", "WESTERN", "EASTERN", "SOUTHERN"]
MODEL_URI = "models:/tayyar-load-forecaster@Production"


def score_day_ahead(target_date: datetime, out_root: str = "day_ahead_forecast") -> Path:
    model = mlflow.pyfunc.load_model(MODEL_URI)
    version = model.metadata.run_id[:8]
    rows, failures = [], []

    for area in AREAS:
        try:
            for h in range(24):                        # 24 hourly forecasts
                target = target_date.replace(hour=0) + timedelta(hours=h)
                recent = recent_load(area, before=target, hours=168)
                wx = _weather_forecast(area, target)   # provided day-ahead weather
                X = build_features_online(recent, now=target, weather_forecast=wx)
                yhat = float(model.predict(X)[0])
                rows.append({"operating_area": area, "target_hour": target,
                             "load_mw": round(yhat, 2), "model_version": version})
                log_prediction(trace_id=f"batch-{area}-{target:%Y%m%d%H}",
                               operating_area=area, target_hour=target,
                               features=X.iloc[0].to_dict(), prediction=yhat,
                               model_version=version)
        except Exception as exc:                        # continue other areas
            failures.append((area, str(exc)))

    # Deterministic, overwrite-safe location => idempotent re-runs.
    out = Path(out_root) / f"date={target_date:%Y-%m-%d}"
    out.mkdir(parents=True, exist_ok=True)
    dst = out / "forecast.parquet"
    pd.DataFrame(rows).to_parquet(dst, index=False)     # overwrite, never append

    if failures:
        print(f"PARTIAL: {len(failures)} area(s) failed: {failures}")
    print(f"wrote {len(rows)} forecasts (model v{version}) -> {dst}")
    return dst
```

### Kubernetes Deployment + Service (read-and-apply, "basics" depth)

```yaml
# k8s/tayyar-forecast.yaml — applied against a local kind/minikube cluster.
# The readiness probe on /ready is what makes rolling updates safe:
# K8s routes traffic ONLY to replicas whose model has finished loading.
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tayyar-forecast
  labels: {app: tayyar-forecast}
spec:
  replicas: 3
  selector:
    matchLabels: {app: tayyar-forecast}
  template:
    metadata:
      labels: {app: tayyar-forecast}
    spec:
      containers:
        - name: api
          image: registry.internal/tayyar-forecast:2.3.0     # digest-pinned in prod
          ports: [{containerPort: 8000}]
          env:
            - name: MODEL_URI
              value: "models:/tayyar-load-forecaster@Production"
            - name: MLFLOW_TRACKING_URI
              value: "http://mlflow.mlops.svc:5000"           # inside the boundary
          readinessProbe:                                     # gates traffic on model load
            httpGet: {path: /ready, port: 8000}
            initialDelaySeconds: 5
            periodSeconds: 5
            failureThreshold: 3
          livenessProbe:                                      # restarts a hung process
            httpGet: {path: /health, port: 8000}
            initialDelaySeconds: 10
            periodSeconds: 15
          resources:
            requests: {cpu: "250m", memory: "512Mi"}
            limits:   {cpu: "1",    memory: "1Gi"}
---
apiVersion: v1
kind: Service
metadata:
  name: tayyar-forecast
spec:
  selector: {app: tayyar-forecast}
  ports: [{port: 80, targetPort: 8000}]
```

## Hands-on Lab 5 — Serve the Forecaster Online and as a Day-Ahead Batch

| | |
|---|---|
| **Objective** | Stand up the online next-hour API (loading `@Staging` from the registry, featurising via the shared module, logging predictions), containerise it with a readiness gate, and run the idempotent day-ahead batch scorer; then apply the K8s manifest and watch a safe rolling update |
| **Duration** | 2 × 50 min (Day 3 H2 + H3) |
| **Setup** | `make platform-up` (MLflow + MinIO + Redis), Lab 4 solution, `git checkout lab5-start`, `pip install "fastapi[standard]" uvicorn mlflow redis pyarrow`, a local `kind`/`minikube` cluster for Part B |

**Part A tasks (50 min)**
1. *(8 min)* Wire `lifespan` to load `models:/tayyar-load-forecaster@Staging` at startup; confirm `/ready` returns 503 until load completes then 200 with the model version.
2. *(12 min)* Implement `/v1/forecast/next-hour`: featurise via `build_features_online`, predict, and set the `X-Model-Version` + `X-Trace-Id` headers. Send one valid request and read the headers.
3. *(10 min)* Implement `log_prediction` (append to `monitoring/prediction_log.parquet`); send five requests; confirm the log has five rows with `model_version` and features — this is Module 6's input.
4. *(10 min)* Implement the day-ahead batch scorer; run it for a date; confirm `day_ahead_forecast/date=.../forecast.parquet` has 96 rows (4 areas × 24h). Re-run the same date and confirm the file is *overwritten*, not duplicated (idempotency).
5. *(10 min)* Break one area's history (delete Southern from the online store) and re-run batch; confirm it records a partial failure and *still* writes the other three areas' 72 rows.

**Part B tasks (50 min)**
1. *(12 min)* Write/inspect the multi-stage Dockerfile; build the image; run the container; confirm the healthcheck flips healthy only *after* the model loads (readiness gate).
2. *(10 min)* Run a small load test (`hey`/`ab`, 200 requests, concurrency 10); record p50/p99 latency in `BENCHMARKS.md`. Note the first-request latency vs warmed latency.
3. *(15 min)* Apply `k8s/tayyar-forecast.yaml` to the local cluster; watch three replicas become Ready; `kubectl rollout status`. Deliberately set a bad `MODEL_URI` on a new revision and observe K8s *not* routing traffic to the never-ready replicas (the probe's job).
4. *(8 min)* Commit `feat(serving): online API + day-ahead batch + k8s manifest`.
5. *(5 min)* Discuss: worker count × model memory = pod memory request — fill the capacity number.

**Expected outputs**
```
$ curl localhost:8000/ready
{"status":"loading_model"}         # then, ~2s later:
{"status":"ready","model_version":"8f3a1c.."}

$ curl -sD - -X POST localhost:8000/v1/forecast/next-hour -d '{...}' | grep X-
X-Model-Version: 8f3a1c..
X-Trace-Id: 2f9c...-...

$ python -m load_forecast.serving.batch 2026-07-01
wrote 96 forecasts (model v8f3a1c) -> day_ahead_forecast/date=2026-07-01/forecast.parquet
$ python -m load_forecast.serving.batch 2026-07-01     # re-run
wrote 96 forecasts ... (file OVERWRITTEN, still 96 rows)   # idempotent

$ kubectl get pods -l app=tayyar-forecast
NAME                     READY   STATUS
tayyar-forecast-...-a    1/1     Running
tayyar-forecast-...-b    1/1     Running
tayyar-forecast-...-c    1/1     Running
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| `/ready` never turns 200 | Model URI/alias wrong or registry unreachable | Check `MODEL_URI` + `MLFLOW_TRACKING_URI`; alias exists? |
| First request slow, rest fast | No warm-up | Add the startup warm predict; the peak's first call must not pay it |
| 422 on a valid-looking request | Feature dtype/column mismatch vs signature | Reuse `build_features_online`; do not hand-build the frame |
| Batch appends duplicate rows on re-run | Non-deterministic path / append mode | Write to `date=<d>/forecast.parquet` and overwrite |
| Whole batch aborts on one area | No partial-failure handling | Wrap per-area loop in try/except; record + continue |
| K8s pods stuck `0/1 Ready` | Readiness probe failing (model not loading) | `kubectl logs`; fix `MODEL_URI`; the probe is doing its job |

**Instructor notes.** The emotional beat of Part B step 3 is watching Kubernetes *refuse* to route traffic to a replica whose model never loaded — that is the readiness gate earning its keep, and it is the exact mechanism Module 7's canary depends on. Keep every pair's prediction log growing; Module 6 reads it directly. Fast finishers: add a `POST /v1/forecast/batch` that scores several areas in one request (partial-failure semantics), previewing capstone extension scope.

## Mini Exercises

**Quiz.** (1) The three serving patterns and the freshness each offers? → batch (as-of-last-run), online (on-demand now), streaming (seconds). (2) Why load the model by alias, not version/path? → makes rollback a re-point; replicas pick up the new version on refresh. (3) Liveness vs readiness for a model server? → liveness restarts a dead process; readiness gates traffic until the model is loaded. (4) Why must serving featurise through `features.py`? → identical to training → no skew. (5) What makes the batch scorer idempotent? → deterministic partitioned path + overwrite, not append.

**Debugging exercise.** Branch `sim-serving-skew`: the API re-implements `is_weekend` inline (dow>=6) instead of calling the shared helper (dow>=5). Forecasts are subtly wrong on Fridays. Participants find that serving bypassed `features.py` and fix by routing through the shared function — reconnecting to Module 3's skew lesson at the serving layer.

**Code-review exercise.** Review a serving PR that loads the model per request, returns 200 from `/ready` immediately, and does not log predictions. Three findings + the reliability/monitoring argument for each.

**Discussion.** Your intraday balancing desk wants next-hour forecasts every 5 minutes as new meter data lands. Is that online or streaming, and what changes in the feature-freshness pipeline? Where is the batch day-ahead still the right tool?

## Case Study — The Endpoint That Died at the Evening Peak

**Scenario.** A Saudi utility's first online load-forecast API worked flawlessly in testing and for three weeks in production — then browned out every evening at 20:00, exactly when the operations desk needed it most, returning 500s for four minutes during the autoscale event.

**Business context.** The 20:00 window is peak-demand ramp; a forecast outage there forces the balancing desk back to a manual heuristic, and a bad manual call means paying for spun-up reserve generation. The outage was invisible in average-latency dashboards because it was brief and periodic.

**Technical challenge.** Diagnose why new replicas — spun up by the autoscaler to handle the evening surge — served errors for their first ~90 seconds, and fix it without over-provisioning always-on capacity.

**Constraints.** Compute budget forbids running peak capacity 24/7; the model is 40 MB and takes ~2 s to load and warm; the balancing desk's SLA is p99 < 200 ms with no error spikes; the fix must survive future model-size growth.

**Solution approach (facilitate).** The autoscaler added replicas that reported *ready* before their model finished loading, so the load balancer sent them traffic during the 2-second load window → 500s. The fix is the readiness gate: `/ready` returns 503 until the model is loaded *and* warmed; K8s then withholds traffic until the replica is genuinely ready. Add a startup warm-up predict so the first real request does not pay the JIT cost, and set the autoscaler to scale *ahead* of the evening ramp (predictive, using the very load curve the model forecasts — a satisfying loop). No always-on over-provisioning required.

**Discussion questions.** (1) Why did average-latency dashboards hide a peak-time outage — what metric would have surfaced it? (2) Why is readiness (not liveness) the correct gate here? (3) How does warm-up differ from readiness, and why do you need both? (4) Design the autoscaling trigger — what makes the load forecaster itself a good scaling signal?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Online p99 latency (warmed) | Performance | < 200 ms | load test (`hey`) |
| First-request penalty | Performance | < 2× warmed p50 | warm vs cold timing |
| Readiness correctness | Reliability | `/ready` 503 until model loaded, then 200 | probe observation |
| Prediction logging coverage | Observability | 100% of predictions logged (API + batch) | prediction-log row count |
| Batch idempotency | Correctness | Re-run same date → identical row count, overwritten | double-run diff |
| Batch partial-failure resilience | Reliability | One area fails → others still written | fault-injection run |
| Serving/training feature parity | Correctness | 0 skew (shared module) | skew test at serving layer |

**Example benchmark table (filled during lab):**

| Path | Predictions | p50 | p99 | Model load gate | Predictions logged |
|---|---|---|---|---|---|
| Online API (cold first req) | 1 | 190 ms | — | 503 → 200 after 2.1 s | yes |
| Online API (warmed) | 200 | 22 ms | 140 ms | ready | yes |
| Day-ahead batch (4 areas × 24h) | 96 | — | — | n/a | yes |
| Batch, Southern history broken | 72 | — | — | n/a | yes (partial, logged failure) |

## Required Visuals and Training Assets

### Diagrams
1. **The serving spectrum** — *Purpose:* the placement tool. *Elements:* a horizontal axis (freshness/latency) with batch, online, streaming plotted; Tayyār's day-ahead (batch) and next-hour (online) pinned; cost/throughput annotations. *Style:* labelled spectrum with two Tayyār pins.
2. **One model, two consumers** — *Purpose:* prove the single-artefact discipline. *Elements:* the registry `@Production` version feeding both the batch job and the online API through the same `features.py`; both writing the same prediction-log contract. *Style:* single source fanning to two paths, converging on the log.
3. **Readiness gate lifecycle** — *Purpose:* fix liveness vs readiness. *Elements:* replica states (starting → loading model → warming → ready), `/ready` returning 503 then 200, load balancer withholding then sending traffic. *Style:* state machine with a traffic-gate icon.
4. **K8s rolling update with readiness** — *Elements:* old replicas draining as new replicas pass readiness; a never-ready (bad-model) replica shown receiving no traffic. *Style:* rolling-update timeline.

### Images
1. **`/ready` transition** (503 → 200) in a terminal — *why:* the gate made visible; *content:* the two curl responses with the model version.
2. **Response headers** showing `X-Model-Version` + `X-Trace-Id` — *why:* correlation to a registry version; *content:* the header block.
3. **`day_ahead_forecast/date=.../forecast.parquet`** listing — *why:* idempotent partitioned output; *content:* the partition path and 96 rows.
4. **`kubectl get pods` all Ready** + a bad-model replica `0/1` — *why:* the probe withholding traffic; *content:* the pod list with the not-ready replica.

### Simulations
1. **Cold-replica 500 storm** — *Setup:* readiness returns 200 immediately (gate disabled). *Expected:* new replicas 500 during model load. *Learning objective:* readiness must gate on model load.
2. **Serving-layer skew** — *Setup:* branch `sim-serving-skew` (inline `is_weekend`). *Expected:* Friday forecasts drift; serving skew test red. *Learning objective:* serving must route through `features.py`.
3. **Batch double-run** — *Setup:* run the day-ahead job twice for one date. *Expected:* idempotent overwrite (not duplicated rows). *Learning objective:* deterministic partitioned output.

### Interactive Activities
- **Pattern-placement game (10 min):** 10 workloads (fraud auth, nightly churn scoring, live surge pricing, day-ahead load…) placed on the batch/online/streaming spectrum with a one-line justification.
- **Readiness role-play (10 min):** volunteers act as load balancer, replica, and model-loader; the class calls out when traffic may flow — dramatising the gate.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `grid_load_hourly.csv` (DVC) | Golden thread | CSV | ~35k rows | Feature history source |
| Online store seed (Redis) | Course tooling (last 168h per area) | Redis dump | small | Online-path lag lookups |
| `weather_day_ahead.csv` | Course team (day-ahead forecast temps) | CSV | small | Batch scorer weather input |

### Demo Requirements
- **Instructor demo:** live-load the model into the API, show `/ready` gating, fire one request and read the headers, then run the batch and re-run it to show idempotency; finish by applying the K8s manifest and rolling out a bad-model revision to watch the probe withhold traffic.
- **Student demo:** one pair shows their prediction log filling from both the API and the batch — the single contract Module 6 will consume.
- **Expected outputs:** every participant has a containerised online API (readiness-gated), a day-ahead batch parquet, and a growing prediction log before Day 3 Hour 4.

---

# Module 6 — Drift Detection and Monitoring

## Module Overview

**Purpose.** A deployed model is a decaying asset: the world it learned drifts away from the world it now predicts. This module gives Tayyār eyes. Participants generate Evidently reports over the prediction log from Module 5, distinguish **data drift** (inputs shift) from **concept drift** (the input→output relationship shifts) from **performance decay** (MAPE climbs), set thresholds that page a human, and wire a drift signal to *open a retraining trigger* on the Module-4 DAG — closing the monitoring→training loop that defines Level 2 maturity.

**Business relevance.** Tayyār's world shifts constantly: a heatwave hotter than any training year (data drift), a wave of rooftop-solar capacity reshaping afternoon demand (concept drift), Ramadan and Hajj moving the evening peak. Undetected, these silently inflate forecast error and cost real reserve-generation money — exactly the six-months-of-silent-over-forecast story from Module 1. Monitoring converts "we found out when the finance team asked about the reserve bill" into "the instruments paged us in week one." In regulated Saudi critical infrastructure, *demonstrable* monitoring is also governance evidence: you must show that you would *know* if the model degraded.

**Industry use cases.**
- A grid operator monitors per-area MAPE and input distributions; a heatwave trips a data-drift alert before the forecast error becomes a reserve-cost line.
- A bank watches its credit model for population shift (new customer segments) and score-distribution drift, feeding a mandated quarterly model-risk review.
- A retail forecaster's monitoring catches a supplier data-format change (a silent schema drift) that would otherwise have poisoned the next retrain.

**Expected competencies.** Participants can generate Evidently data-drift and regression-performance reports on the prediction log, interpret drift statistics and read the difference between the three decay types, set actionable thresholds (not noisy ones), schedule monitoring as a job, and wire a drift/decay signal to trigger the Module-4 retraining DAG.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Distinguish data drift, concept drift, and performance decay with evidence | LO5 |
| 6.2 | Generate Evidently data-drift + regression-performance reports on the prediction log | LO5 |
| 6.3 | Set actionable drift/decay thresholds and alerts (signal over noise) | LO5 |
| 6.4 | Schedule monitoring as a recurring job producing a durable report | LO5, LO4 |
| 6.5 | Wire a drift/decay signal to trigger retraining (close the CT loop) | LO5, LO4 |

## Technical Content

### 1. The three ways a model decays

Precision here prevents the wrong fix:

| | What shifts | Tayyār example | Detect with | Right response |
|---|---|---|---|---|
| **Data drift** | Input distribution P(X) | Summer runs 4 °C hotter than any training year | Compare feature distributions (reference vs current) | Often retrain on recent data |
| **Concept drift** | Relationship P(y\|X) | Rooftop solar reshapes afternoon demand for the *same* weather | Performance drop *without* obvious input drift | Retrain; possibly re-feature/re-model |
| **Performance decay** | Realised error (the outcome) | Day-ahead MAPE climbs 2.7% → 3.6% over eight weeks | Compare predictions to *actuals* once known | Investigate which drift caused it; retrain |

The key teaching point: **data drift is a leading indicator you can measure immediately** (you have the inputs now); **performance decay is the lagging ground truth** (you must wait for actual load to be observed). Concept drift is the sneaky one — inputs look normal, but the model is wrong, so you catch it through performance, not input, monitoring. Tayyār monitors *both* input distributions (fast, leading) and MAPE-vs-actuals (slow, definitive).

### 2. Reference vs current: the comparison at the heart of drift

All drift detection is a comparison of a **reference** window (what the model expects — typically the training distribution or a healthy recent baseline) against a **current** window (recent production data):

- For **data drift**, per feature: is the current distribution statistically different from reference? Evidently picks a test per column type (e.g. Kolmogorov–Smirnov for numeric, population-stability index / chi-square for categorical) and reports a per-column drift flag plus a dataset-level drift share.
- For **performance**, once actuals arrive: compute MAPE/RMSE on the current window and compare to the reference/SLA.
- **Windowing matters:** too short a window is noisy (a hot afternoon is not climate change); too long masks a real shift. Tayyār uses a rolling 7-day current window against the training reference for inputs, and a rolling 14-day window for MAPE decay.

### 3. Evidently: reports and tests

Evidently produces two complementary things:

- **Reports** — rich, human-readable HTML (distribution overlays, drift scores per column, performance plots) for a human to *investigate*. This is what an analyst opens after an alert.
- **Tests / test suites** — programmatic pass/fail checks (e.g. "dataset drift share < 0.3", "MAPE ≤ 0.035") that a *scheduled job* evaluates to decide whether to alert or trigger. Reports are for humans; tests are for automation. Tayyār's monitoring job runs the test suite and emits the HTML report as an artefact for the human who responds.

### 4. Thresholds: signal, not noise

A monitor that cries wolf is turned off, and a turned-off monitor is worse than none (false confidence). Threshold discipline:

- **Base thresholds on cost, not statistics alone.** A statistically-significant drift that does not move MAPE beyond the operations SLA is often *not* actionable — alert on *decay that matters* (MAPE breaching the 3.5% per-area ceiling), and treat input drift as an early *watch* signal, not an immediate page.
- **Use hysteresis / persistence:** require the breach to persist (e.g. MAPE above ceiling for 3 consecutive days) before paging, so one anomalous day does not trigger a retrain.
- **Tier the response:** input drift → log + dashboard; sustained performance decay → open a retraining trigger; SLA breach with ops impact → page a human. Not every signal is a page.

### 5. Closing the loop: monitoring triggers retraining

This is the Level-2 capability and the course's climax-before-capstone:

- The scheduled monitoring job evaluates the test suite over the recent prediction log + observed actuals.
- On a *sustained* decay breach, it does **not** silently retrain and promote — it **opens a retraining trigger** (fires the Module-4 DAG via its API/`workflow_dispatch` entry point) with the *evidence* attached (the drift report, the decayed metric). The DAG then retrains, evaluates against the SLA gate, and registers a challenger *if* it beats the incumbent — with promotion still human-gated (Module 7).
- **Automate the detection and the trigger; keep judgement at promotion.** The loop closes without a human noticing the decay, but a human still approves the new champion into production until monitoring earns full trust.

### 6. Common mistakes & production considerations

1. Monitoring only inputs (data drift) and never actuals — you miss concept drift entirely (inputs look fine, model is wrong).
2. Monitoring only performance and never inputs — you find out late (performance is lagging) and cannot pre-empt.
3. Thresholds set on statistical significance alone — noisy pages, then a silenced monitor.
4. No reference window discipline — comparing against a drifting baseline hides slow decay.
5. Auto-retrain-and-promote on any drift — a bad-data drift retrains on garbage and ships it; the SLA gate + human promotion must remain.
6. Not persisting reports — an alert with no investigable artefact wastes the responder's time.
7. Forgetting the actuals-arrival delay — day-ahead MAPE can only be computed *after* the load is observed; the monitoring schedule must account for this lag.

**Production considerations.** Prediction logs and monitoring reports live inside the network boundary; feature values may be personal data (PDPL) and carry retention rules. Monitoring must itself be reliable (a monitoring job that silently dies is a hidden Level-0 regression) — monitor the monitor. In critical infrastructure, the *evidence trail* from "MAPE decayed → drift report → retraining trigger → new champion" is auditable governance, not just engineering hygiene.

## Code Examples

### The monitoring job: Evidently report + test suite over the prediction log

```python
# src/load_forecast/monitoring/monitor.py
"""Scheduled Tayyar monitoring: compare a CURRENT window of production
predictions/actuals against a REFERENCE, emit an HTML report for humans and a
pass/fail test result for automation. On sustained decay, open a retrain trigger.
"""
from __future__ import annotations
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, RegressionPreset
from evidently.test_suite import TestSuite
from evidently.tests import TestShareOfDriftedColumns, TestValueMAPE

from load_forecast.monitoring.trigger import open_retraining_trigger

FEATURES = ["hour", "dow", "is_weekend", "is_ramadan", "is_hajj", "is_holiday",
            "temp_c", "humidity", "load_lag_1h", "load_lag_24h", "load_lag_168h"]
PER_AREA_CEILING = 0.035
DRIFT_SHARE_WATCH = 0.30


def _windows(log: pd.DataFrame, ref_days=90, cur_days=14):
    cutoff = log["target_hour"].max() - timedelta(days=cur_days)
    ref = log[log["target_hour"] <= cutoff].tail(ref_days * 24 * 4)
    cur = log[log["target_hour"] > cutoff]
    return ref, cur


def run_monitoring(log_path="monitoring/prediction_log.parquet",
                   out_dir="monitoring/reports") -> dict:
    log = pd.read_parquet(log_path)
    log = log.dropna(subset=["actual_mw"])          # only rows with observed actuals
    ref, cur = _windows(log)

    mapping = ColumnMapping(prediction="prediction", target="actual_mw",
                            numerical_features=FEATURES)

    # --- human-readable report (data drift + regression performance) ---
    report = Report(metrics=[DataDriftPreset(), RegressionPreset()])
    report.run(reference_data=ref, current_data=cur, column_mapping=mapping)
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    report_path = out / f"drift_{datetime.utcnow():%Y%m%d}.html"
    report.save_html(str(report_path))

    # --- machine-readable tests (drives automation) ---
    suite = TestSuite(tests=[
        TestShareOfDriftedColumns(lt=DRIFT_SHARE_WATCH),   # input drift WATCH
        TestValueMAPE(lte=PER_AREA_CEILING),               # performance DECAY page
    ])
    suite.run(reference_data=ref, current_data=cur, column_mapping=mapping)
    results = suite.as_dict()
    mape_test = next(t for t in results["tests"] if "MAPE" in t["name"])
    decayed = mape_test["status"] != "SUCCESS"

    print(f"report -> {report_path} | MAPE test: {mape_test['status']}")
    return {"report": str(report_path), "decayed": decayed,
            "tests": results["summary"]}
```

### Sustained-decay logic and opening the retraining trigger

```python
# src/load_forecast/monitoring/trigger.py
"""Persistence + tiered response: input drift => watch; SUSTAINED MAPE decay =>
open a retraining trigger (fires the Module-4 DAG) with evidence attached.
Never auto-promote — the SLA gate + human approval stay in the loop.
"""
from __future__ import annotations
import json
from pathlib import Path

import requests

AIRFLOW_TRIGGER = "http://airflow:8080/api/v1/dags/train_tayyar/dagRuns"
STATE = Path("monitoring/decay_streak.json")
REQUIRED_CONSECUTIVE = 3                      # hysteresis: 3 days before paging


def record_and_maybe_trigger(decayed: bool, evidence: dict) -> bool:
    streak = json.loads(STATE.read_text())["streak"] if STATE.exists() else 0
    streak = streak + 1 if decayed else 0
    STATE.write_text(json.dumps({"streak": streak}))

    if streak >= REQUIRED_CONSECUTIVE:
        open_retraining_trigger(evidence)      # fire CT with the drift report
        STATE.write_text(json.dumps({"streak": 0}))   # reset after firing
        return True
    if decayed:
        print(f"decay observed (streak={streak}/{REQUIRED_CONSECUTIVE}); watching")
    return False


def open_retraining_trigger(evidence: dict) -> None:
    """Fire the Module-4 DAG with evidence — retrain, DON'T auto-promote."""
    payload = {"conf": {"trigger": "drift", "evidence": evidence}}
    resp = requests.post(AIRFLOW_TRIGGER, json=payload, timeout=10)
    resp.raise_for_status()
    print(f"retraining trigger opened for train_tayyar: {evidence.get('report')}")
```

### Scheduling the monitor (the loop made continuous)

```python
# dags/monitor_tayyar.py
"""Airflow DAG: run monitoring daily; on SUSTAINED decay, trigger train_tayyar.
Accounts for the actuals-arrival lag: day-ahead MAPE is computed once the load
for the forecast hour has been observed (>= 1 day later)."""
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from load_forecast.monitoring.monitor import run_monitoring
from load_forecast.monitoring.trigger import record_and_maybe_trigger


def _monitor(**_):
    result = run_monitoring()
    fired = record_and_maybe_trigger(result["decayed"], evidence=result)
    print("retraining triggered" if fired else "no trigger (within tolerance)")


with DAG(
    dag_id="monitor_tayyar",
    schedule="@daily",                        # actuals lag => daily, not hourly
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["tayyar", "monitoring", "ct-loop"],
) as dag:
    PythonOperator(task_id="monitor", python_callable=_monitor)
```

## Hands-on Lab 6 — Detect Drift and Close the Retraining Loop

| | |
|---|---|
| **Objective** | Generate an Evidently data-drift + regression-performance report on a shifted week of Tayyār data, set an actionable threshold, schedule the monitor, and wire a sustained-decay signal to trigger the Module-4 retraining DAG |
| **Duration** | 2 × 50 min (Day 3 H5 + Day 4 H2) |
| **Setup** | `make platform-up`, Lab 5 prediction log, `git checkout lab6-start`, `pip install evidently`, provided `shifted_week.csv` (a heatwave + solar-reshaped week) |

**Part A tasks (Day 3 H5, 50 min)**
1. *(10 min)* Build a reference (healthy) window and a current window from the prediction log; run `DataDriftPreset()`; open the HTML report; identify which features drifted (expect `temp_c` and the afternoon load lags).
2. *(12 min)* Add `RegressionPreset()` with the actuals joined; read the current-window MAPE and compare to the 3.5% per-area ceiling.
3. *(10 min)* Feed the `shifted_week.csv` (heatwave) as the current window; confirm `temp_c` drift flags *and* MAPE climbs — a data-drift-driven decay.
4. *(10 min)* Feed a solar-reshaped week where inputs look normal but afternoon MAPE climbs; observe *performance* decay with little input drift — concept drift. Name the difference out loud.
5. *(8 min)* Convert the report into a `TestSuite` with `TestShareOfDriftedColumns` + `TestValueMAPE`; get a machine-readable pass/fail.

**Part B tasks (Day 4 H2, 50 min)**
1. *(12 min)* Implement the sustained-decay logic (3-day streak) in `trigger.py`; simulate three consecutive decayed days and confirm it fires exactly once, then resets.
2. *(10 min)* Implement `open_retraining_trigger` to POST to the `train_tayyar` DAG's trigger endpoint with the evidence; confirm a new DAG run appears with `conf.trigger == "drift"`.
3. *(10 min)* Schedule `monitor_tayyar` `@daily`; run it; confirm it produces a dated HTML report artefact and evaluates the tests.
4. *(10 min)* End-to-end: shift the data → monitor detects decay over 3 days → trigger fires → `train_tayyar` retrains → SLA gate evaluates the challenger. Observe the *closed loop* (promotion still pending human/Module 7).
5. *(8 min)* Commit `feat(monitoring): evidently drift + sustained-decay retraining trigger`.

**Expected outputs**
```
$ python -m load_forecast.monitoring.monitor
report -> monitoring/reports/drift_20260703.html | MAPE test: FAIL

# 3 consecutive decayed days:
decay observed (streak=1/3); watching
decay observed (streak=2/3); watching
retraining trigger opened for train_tayyar: monitoring/reports/drift_20260703.html

$ # Airflow: a new train_tayyar run, conf={"trigger":"drift", ...}
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| MAPE test errors (no target) | Actuals not joined | Join observed `actual_mw` before RegressionPreset; drop rows without actuals |
| Everything flags as drift | Reference window too small/stale | Use a healthy 90-day reference; discuss window discipline |
| Trigger fires every single day | No hysteresis | Add the 3-day streak; one hot day is not climate change |
| DAG trigger 403/401 | Airflow API auth | Set the API token/basic-auth from `platform.env` |
| Decay never detected | Threshold too loose (ceiling 1.0) | Restore the real 3.5% ceiling — the Module-4 disabled-gate lesson, again |

**Instructor notes.** The pedagogical peak is Part A steps 3 vs 4: a heatwave shows *input drift + decay* (you can see it coming in the inputs), while the solar-reshape shows *decay with clean inputs* (concept drift — invisible to input monitoring). Make the room articulate why you need *both* input and performance monitoring. Part B's closed loop is the Level-2 moment — connect the trigger firing back to Module 1's maturity ladder physically on the wall. Fast finishers: add a per-area drift breakdown so the Southern area's decay is visible independently.

## Mini Exercises

**Quiz.** (1) Data vs concept drift — which shows in the inputs? → data drift shifts P(X) (visible in inputs); concept drift shifts P(y|X) (invisible in inputs, visible in performance). (2) Why monitor both inputs and actuals? → inputs are leading (fast), actuals are lagging (definitive); each catches what the other misses. (3) Why hysteresis on the retrain trigger? → one anomalous day is not decay; require persistence. (4) Reports vs tests in Evidently? → reports for human investigation, tests for automation pass/fail. (5) What does the monitoring job do on sustained decay — retrain and promote? → No: open a retraining trigger; SLA gate + human still gate promotion.

**Debugging exercise.** Branch `sim-noisy-monitor`: the trigger fires on any single-day input drift, retraining nightly on noise. Participants add cost-based thresholding + hysteresis and explain why a noisy monitor gets silenced (false confidence) — worse than none.

**Code-review exercise.** Review a monitoring PR that (a) monitors only input drift, never actuals, (b) auto-promotes the retrained model, and (c) never persists the report. Three findings + the governance argument.

**Discussion.** Your day-ahead forecast's actuals only arrive a day later, and hour-ahead's arrive within the hour. How does the actuals-arrival lag change each one's monitoring schedule and alert latency?

## Case Study — The Heatwave the Model Never Saw

**Scenario.** A Saudi grid operator's load forecaster, trained on three temperate years, met an unprecedented July heatwave: sustained 49 °C for ten days. The model under-forecast the AC-driven load surge, the balancing desk trusted it, and the operator scrambled expensive reserve generation mid-crisis.

**Business context.** Reserve generation bought under emergency conditions is the most expensive electricity there is; the ten-day miss cost more than the entire year's MLOps tooling budget. Leadership's question afterward: "why didn't we *know* the model was out of its depth?"

**Technical challenge.** Build monitoring that would have *paged* on day one of the heatwave — before the forecast error became a reserve-cost crisis — distinguishing "inputs are outside training range" (measurable immediately) from "the forecast is wrong" (measurable only after the load is observed).

**Constraints.** Day-ahead actuals lag by a day; the operator cannot wait for MAPE to confirm decay when the inputs are already visibly extreme; false alarms during normal summer heat would get the monitor ignored; the fix must produce audit evidence for the post-incident regulator review.

**Solution approach.** Two-tier monitoring: an *input-drift watch* on `temp_c` (leading indicator) flags the moment temperatures exceed the training range — an immediate "model operating out of distribution" warning, day one of the heatwave; and a *performance* monitor on MAPE-vs-actuals (lagging, definitive) that confirms and quantifies the decay a day later. Sustained decay opens a retraining trigger on recent hot-weather data; promotion stays human-gated given crisis conditions. The drift report becomes the regulator's evidence that the operator now *would* know.

**Discussion questions.** (1) Which tier would have paged on day one, and why couldn't performance monitoring alone do that? (2) How do you set the `temp_c` watch so normal summer heat does not cry wolf but an unprecedented heatwave does? (3) Should the operator auto-promote a heatwave-retrained model mid-crisis? Argue both sides. (4) How does the drift report function as regulatory evidence?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Data-drift detection on shifted week | Detection | `temp_c` + afternoon lags flagged | Evidently report |
| Performance decay detection | Detection | MAPE breach caught within window | MAPE test |
| Concept-drift caught via performance | Detection | Solar-reshape decay flagged despite clean inputs | Report comparison |
| Alert signal-to-noise | Reliability | 0 pages on single-day anomalies (hysteresis) | streak logic test |
| Loop closure | Automation | Sustained decay → DAG trigger fires once | end-to-end run |
| Report durability | Governance | Dated HTML artefact persisted per run | reports directory |

**Example benchmark table:**

| Scenario | temp_c drift | Dataset drift share | Current MAPE | Decay? | Action |
|---|---|---|---|---|---|
| Healthy week | no | 0.05 | 2.7% | no | none |
| Heatwave week | yes | 0.36 | 3.9% | yes | watch (input) → trigger (sustained) |
| Solar-reshaped week | no | 0.08 | 3.7% | yes | performance trigger (concept drift) |
| One anomalous day | slight | 0.31 | 3.6% | 1-day | watch only (hysteresis holds) |

## Required Visuals and Training Assets

### Diagrams
1. **The three decays** — *Purpose:* the disambiguation anchor. *Elements:* three panels — data drift (input histograms shift), concept drift (same inputs, relationship changes), performance decay (MAPE line climbs); leading vs lagging labels. *Style:* three side-by-side panels with a leading/lagging axis.
2. **Reference vs current windows** — *Elements:* a rolling current window compared against a reference baseline; the drift test between them; window-size trade-off annotation. *Style:* sliding-window timeline.
3. **The closed CT loop** — *Purpose:* the Level-2 image. *Elements:* serving → prediction log → monitor → (sustained decay) → retraining trigger → train DAG → SLA gate → registry → back to serving; human gate at promotion highlighted. *Style:* full loop reusing M1's palette, now fully instantiated.
4. **Tiered response ladder** — *Elements:* input drift → dashboard/watch; sustained decay → trigger; SLA breach with ops impact → page. *Style:* escalation ladder.

### Images
1. **Evidently data-drift report** — *why:* what an analyst opens post-alert; *content:* the `temp_c` distribution overlay with a drift flag.
2. **Evidently regression-performance report** — *why:* MAPE decay made visible; *content:* predicted-vs-actual and the error trend.
3. **Test-suite pass/fail output** — *why:* the automation surface; *content:* drift-share PASS, MAPE FAIL.
4. **Triggered `train_tayyar` run with `conf.trigger=drift`** — *why:* the loop closing; *content:* the Airflow run detail showing the drift evidence.

### Simulations
1. **Heatwave (data drift)** — *Setup:* `shifted_week.csv` with extreme `temp_c`. *Expected:* input drift flags + MAPE climbs. *Learning objective:* leading indicator on inputs.
2. **Solar reshape (concept drift)** — *Setup:* afternoon load relationship changed, inputs normal. *Expected:* MAPE decays with clean input drift. *Learning objective:* need performance monitoring, not just input.
3. **Noisy monitor** — *Setup:* trigger with no hysteresis. *Expected:* nightly retrains on single-day noise. *Learning objective:* signal over noise; hysteresis + cost thresholds.

### Interactive Activities
- **Drift-type diagnosis (15 min):** groups get four report snapshots and must label each data / concept / performance and prescribe the response.
- **Threshold-setting debate (10 min):** two groups propose a `temp_c` watch threshold — too tight cries wolf, too loose misses the heatwave; the class negotiates the cost-based middle.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `prediction_log.parquet` | Produced by Module-5 serving | Parquet | grows | Monitoring input (predictions + actuals) |
| `shifted_week.csv` | Course team (heatwave) | CSV | small | Data-drift simulation |
| `solar_reshaped_week.csv` | Course team (concept drift) | CSV | small | Concept-drift simulation |

### Demo Requirements
- **Instructor demo:** live-generate a drift report on a healthy week (green), then swap in the heatwave week and watch `temp_c` drift + MAPE climb; then wire the sustained-decay trigger and fire the retraining DAG on screen.
- **Student demo:** one pair shows their heatwave-vs-solar comparison and names why one is data drift and the other concept drift.
- **Expected outputs:** every participant has a scheduled monitoring job producing a durable drift report and a working sustained-decay retraining trigger before Day 4 Hour 3.

---

# Module 7 — Release Strategies and Rollback

## Module Overview

**Purpose.** Module 6 can now produce a *challenger* — a retrained `tayyar-load-forecaster` that beats the incumbent on the SLA. This module answers the last operational question: **how do you put it into production without betting the grid on it?** Participants implement the three progressive-delivery strategies — **shadow** (run the candidate alongside, serve nothing from it, compare live), **canary** (send it a small slice of real traffic, ramp on evidence), and **blue-green** (two full environments, switch atomically) — with an *automated promotion gate* and, crucially, **one-command rollback that is just a registry alias re-point**. This is the difference between "we shipped a model" and "we shipped a model safely, and could undo it in seconds."

**Business relevance.** For a load forecaster feeding grid operations, a bad release is not a cosmetic bug — an over-forecasting v2 pushed straight to 100% traffic means real reserve-generation spend, or worse. Progressive delivery lets the operator *learn from production* (the only place the real distribution lives) while risking only a sliver of traffic, and roll back the instant the candidate underperforms. In Saudi critical infrastructure, "we can undo any model change in under a minute, with evidence of why" is both an operational necessity and a governance requirement. This module is why Modules 2's registry aliases and Module 5's alias-based loading were built the way they were.

**Industry use cases.**
- A grid operator shadow-tests every challenger against live traffic for a week (serving nothing from it) before canarying 10% → 100%, with an automated MAPE-regression rollback gate.
- A payments provider blue-green-switches its fraud model so a bad release is a one-flag revert, and canaries score-threshold changes on 1% of traffic.
- A recommender team runs permanent shadow deployments of experimental models to gather production metrics with zero user risk.

**Expected competencies.** Participants can choose shadow/canary/blue-green from risk and observability requirements, implement traffic splitting driven by registry aliases, define an automated promotion gate on live metrics, execute a one-command rollback by alias re-point, and design the human-gated approval that guards production promotion.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Compare canary, blue-green, and shadow releases by risk/observability trade-off | LO6 |
| 7.2 | Implement traffic splitting driven by registry aliases | LO6, LO3 |
| 7.3 | Define an automated promotion gate on live production metrics | LO6, LO5 |
| 7.4 | Execute a one-command rollback as a registry alias re-point | LO6, LO2 |
| 7.5 | Design the human-gated approval guarding production promotion | LO6, LO1 |

## Technical Content

### 1. Why progressive delivery for models (not just code)

Traditional CD wisdom — never big-bang a release — applies doubly to models, because a model's correctness *depends on the production data distribution you cannot fully see in test*. A model that aced the offline SLA can still underperform on live traffic (a subtle skew, an unseen regime). Progressive delivery treats production as the final, irreplaceable test environment — but with a *small blast radius* and a *fast undo*. The three strategies trade off how much risk you take to learn how much:

| Strategy | Traffic to candidate | Risk | What you learn | Rollback |
|---|---|---|---|---|
| **Shadow** | 0% served (runs in parallel, output discarded) | None to users | Live behaviour vs incumbent, zero risk | N/A (nothing served) |
| **Canary** | Small slice (1–10%), ramped | Bounded to the slice | Real served performance on real users | Re-point alias / stop ramp |
| **Blue-green** | 0% then 100% (atomic switch) | All-or-nothing at switch | Full-environment validation pre-switch | Flip back to blue |

### 2. Shadow deployment: risk-free live comparison

Shadow is the safest and the natural *first* stage for Tayyār:

- The candidate model receives a *copy* of every real request, produces a forecast, and **logs it — but the served answer still comes from the incumbent**. Users/operations see only the current production model.
- You accumulate a live, apples-to-apples comparison: for the same inputs, incumbent MAPE vs candidate MAPE, on the *real* production distribution, with *zero* risk.
- After a shadow window (Tayyār: one week, to see a full weekly load cycle), you have evidence to justify — or refuse — a canary. Shadow is how you earn the right to canary.

### 3. Canary: bounded-risk ramp on evidence

Canary sends a *small* fraction of real traffic to the candidate and ramps only if it keeps winning:

- Start at 10%: the release controller routes 10% of forecast requests to the candidate (`@candidate` alias), 90% to the incumbent (`@production`). Both log predictions tagged with their model version.
- **Automated promotion gate:** at each step, compare candidate vs incumbent MAPE on the canary slice over a window; ramp 10% → 25% → 50% → 100% *only while the candidate is non-inferior*. Any regression beyond tolerance halts the ramp and triggers rollback.
- **Ramp on evidence, not a timer alone:** a timer says "an hour passed"; the gate says "and the candidate is still winning." Both matter — enough time to see a real signal, and a metric that clears the bar.

### 4. Blue-green: atomic switch with instant revert

Blue-green keeps two full environments — blue (current) and green (candidate) — and switches all traffic at once:

- Green is deployed and validated (readiness, smoke, shadow) while blue serves 100%. The **switch** re-points the router (or the `@production` alias) from blue to green atomically.
- **Rollback is flipping back to blue** — instant, because blue is still running. This is the fastest full-revert, at the cost of running two environments.
- For Tayyār, blue-green suits an *infrastructure* change (new serving image, new K8s version) more than a model swap; canary+shadow suits *model* changes where you want graduated exposure. Teach the fit, not a favourite.

### 5. Rollback = a registry alias re-point (the payoff)

The course's architecture makes rollback trivial, and this is the moment it pays off:

- Because serving loads `models:/tayyar-load-forecaster@Production` (Module 5) and promotion is an *alias transition* (Module 2), **rollback is re-pointing `@Production` to the previous version** — a single API call, seconds, no rebuild, no redeploy. Serving replicas pick up the previous version on their next model refresh.
- Contrast the Level-0 alternative: finding the old `model.pkl`, hoping it is the right one, copying it to a server, restarting — minutes-to-hours under incident pressure, with no certainty. The whole course's discipline (registry, aliases, alias-based loading) exists to make this one operation instant and certain.
- **Record the rollback:** every alias transition has an owner, a reason, and a timestamp — the rollback itself is audit evidence ("reverted v3→v2 at 20:14, reason: canary MAPE regression on Southern area").

### 6. Automated gates, human judgement, and common mistakes

The governing principle from Module 1, now fully realised: **automate the toil, gate the judgement.**

- *Automate:* traffic splitting, metric comparison on the canary slice, the non-inferiority test, and the *rollback* (a regression should auto-revert without waiting for a human at 03:00).
- *Gate with a human:* the *initial* promotion to production traffic and the ramp to 100% stay human-approved for Tayyār until monitoring earns trust — grid operations must own the decision that their forecast source changed.

**Common mistakes**
1. Big-bang model swaps straight to 100% — the exact risk progressive delivery removes.
2. Canary with no automated gate — "ship it and watch" is not a gate; define the metric and the tolerance up front.
3. Ramping on a timer alone with no metric — time passing is not evidence of quality.
4. Rollback that requires a rebuild/redeploy — if rollback is not seconds, the architecture is wrong (you built loose pickles, not aliases).
5. Comparing candidate and incumbent on *different* traffic — the canary slice must be comparable (or shadow, which sees identical inputs).
6. No record of the promotion/rollback decision — you lose the audit trail exactly when (post-incident) you need it most.
7. Confusing model *version* with *deployment* — the whole module depends on keeping "which version exists" (registry) separate from "which version gets traffic" (alias/router), the distinction Module 1 flagged.

**Production considerations.** In Saudi critical infrastructure the promotion gate is a change-advisory checkpoint; the automated rollback still exists but a human owns forward promotion. Traffic splitting can live at the app layer (the release controller here), a service mesh, or the model server; the *pattern* is identical. Guard against alias thrash (rapid re-points confusing replicas) with a minimum dwell time. And keep the incumbent warm during any canary so rollback is truly instant.

## Code Examples

### The release controller: alias-driven traffic split + shadow

```python
# src/load_forecast/serving/release.py
"""Release controller: routes forecast traffic across incumbent/candidate by
registry ALIAS, supports SHADOW (candidate runs, output discarded) and CANARY
(candidate serves a fraction), and logs both for the promotion gate.
"""
from __future__ import annotations
import os
import random

import mlflow.pyfunc

from load_forecast.serving.prediction_log import log_prediction

MODEL = "tayyar-load-forecaster"


class ReleaseController:
    def __init__(self, canary_pct: int = 0, shadow: bool = False):
        self.canary_pct = canary_pct               # 0..100 of traffic to candidate
        self.shadow = shadow
        self.incumbent = mlflow.pyfunc.load_model(f"models:/{MODEL}@Production")
        self.candidate = self._maybe_load("candidate")

    def _maybe_load(self, alias: str):
        try:
            return mlflow.pyfunc.load_model(f"models:/{MODEL}@{alias}")
        except Exception:
            return None                            # no candidate deployed

    def forecast(self, X, area: str, hour, trace_id: str) -> float:
        inc_pred = float(self.incumbent.predict(X)[0])
        inc_ver = self.incumbent.metadata.run_id[:8]

        # SHADOW: candidate runs and is LOGGED, but incumbent's answer is served.
        if self.candidate is not None and (self.shadow or self._route_to_candidate()):
            cand_pred = float(self.candidate.predict(X)[0])
            cand_ver = self.candidate.metadata.run_id[:8]
            log_prediction(trace_id=f"{trace_id}-cand", operating_area=area,
                           target_hour=hour, features=X.iloc[0].to_dict(),
                           prediction=cand_pred, model_version=cand_ver,
                           role="candidate")
            if not self.shadow:                    # CANARY: actually serve candidate
                log_prediction(trace_id=trace_id, operating_area=area,
                               target_hour=hour, features=X.iloc[0].to_dict(),
                               prediction=cand_pred, model_version=cand_ver,
                               role="served")
                return cand_pred

        log_prediction(trace_id=trace_id, operating_area=area, target_hour=hour,
                       features=X.iloc[0].to_dict(), prediction=inc_pred,
                       model_version=inc_ver, role="served")
        return inc_pred

    def _route_to_candidate(self) -> bool:
        return self.candidate is not None and random.randint(1, 100) <= self.canary_pct
```

### The automated promotion gate (non-inferiority on live traffic)

```python
# src/load_forecast/serving/promotion_gate.py
"""Compare candidate vs incumbent on LIVE logged predictions+actuals. Ramp the
canary only while the candidate is non-inferior; regress => signal rollback.
"""
from __future__ import annotations
import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error as mape

TOLERANCE = 0.002            # candidate may be at most 0.2pp worse before halting
RAMP = {10: 25, 25: 50, 50: 100}


def evaluate_canary(log_path="monitoring/prediction_log.parquet",
                    current_pct: int = 10) -> dict:
    log = pd.read_parquet(log_path).dropna(subset=["actual_mw"])
    recent = log[log["target_hour"] >= log["target_hour"].max() - pd.Timedelta("2D")]

    inc = recent[recent["role"] == "served"]                      # incumbent-served
    cand = recent[recent["role"] == "candidate"]                  # shadow/canary log
    if cand.empty:
        return {"decision": "hold", "reason": "no candidate traffic yet"}

    inc_mape = mape(inc["actual_mw"], inc["prediction"])
    cand_mape = mape(cand["actual_mw"], cand["prediction"])

    if cand_mape <= inc_mape + TOLERANCE:                         # non-inferior
        nxt = RAMP.get(current_pct, 100)
        return {"decision": "ramp", "to_pct": nxt,
                "inc_mape": round(inc_mape, 4), "cand_mape": round(cand_mape, 4)}
    return {"decision": "rollback",
            "reason": f"candidate MAPE {cand_mape:.4f} > incumbent "
                      f"{inc_mape:.4f} + tol", "inc_mape": round(inc_mape, 4),
            "cand_mape": round(cand_mape, 4)}
```

### One-command rollback (alias re-point) — the payoff

```python
# src/load_forecast/serving/rollback.py
"""Rollback == re-point the @Production alias to the previous version. Seconds,
no rebuild, no redeploy. Every transition is recorded (owner, reason, time)."""
from __future__ import annotations
import sys
from datetime import datetime, timezone

from mlflow.tracking import MlflowClient

MODEL = "tayyar-load-forecaster"


def rollback(reason: str, owner: str = "on-call") -> int:
    client = MlflowClient()
    current = client.get_model_version_by_alias(MODEL, "production")
    versions = sorted((int(v.version) for v in client.search_model_versions(
        f"name='{MODEL}'")), reverse=True)
    prev = next(v for v in versions if v < int(current.version))

    client.set_registered_model_alias(MODEL, "production", prev)   # THE re-point
    client.set_model_version_tag(MODEL, prev, "rollback_reason", reason)
    client.set_model_version_tag(MODEL, prev, "rollback_owner", owner)
    client.set_model_version_tag(MODEL, prev, "rollback_at",
                                 datetime.now(timezone.utc).isoformat())
    print(f"ROLLED BACK @production: v{current.version} -> v{prev} ({reason})")
    return prev


if __name__ == "__main__":                       # `python -m ...rollback "why"`
    rollback(reason=sys.argv[1] if len(sys.argv) > 1 else "manual rollback")
```

## Hands-on Lab 7 — Ship v2 by Shadow + Canary with an Automated Rollback Gate

| | |
|---|---|
| **Objective** | Deploy the retrained candidate in shadow (compare live, serve nothing from it), then canary 10% → 100% behind an automated non-inferiority gate, and execute a one-command rollback when a deliberately-regressed candidate fails — proving rollback is an alias re-point |
| **Duration** | 50 minutes |
| **Setup** | `make platform-up`, Lab 6 challenger registered, `git checkout lab7-start`; a candidate model aliased `@candidate` and the incumbent `@Production` |

**Tasks**
1. *(8 min)* Deploy the candidate in **shadow** (`shadow=True`): send live-shaped traffic; confirm the served answer always comes from the incumbent while the candidate's forecasts are logged with `role="candidate"`. Verify users are at zero risk.
2. *(10 min)* Run the promotion gate over the shadow window; read incumbent vs candidate MAPE; decide (evidence-based) whether the candidate has earned a canary.
3. *(10 min)* Switch to **canary at 10%**; confirm ~10% of served predictions carry the candidate version; run the gate → observe a `ramp` decision to 25% when the candidate is non-inferior. Ramp through 25 → 50 → 100.
4. *(10 min)* Deploy a *deliberately regressed* candidate (`@candidate` pointing at a worse model); canary it; confirm the gate returns `rollback` (candidate MAPE > incumbent + tolerance).
5. *(7 min)* Execute `python -m load_forecast.serving.rollback "canary MAPE regression"`; confirm `@Production` re-points to the previous version in **one command, in seconds**, with the reason/owner/time tags recorded. Confirm serving replicas load the reverted version on refresh.
6. *(5 min)* Commit `feat(release): shadow+canary with automated non-inferiority gate and alias rollback`.

**Expected outputs**
```
# Shadow:
served=incumbent(v2)  shadow_logged=candidate(v3)   # users unaffected

# Canary gate (good candidate):
{"decision":"ramp","to_pct":25,"inc_mape":0.0271,"cand_mape":0.0263}
... ramps 10 -> 25 -> 50 -> 100

# Canary gate (regressed candidate):
{"decision":"rollback","reason":"candidate MAPE 0.0388 > incumbent 0.0271 + tol"}

$ python -m load_forecast.serving.rollback "canary MAPE regression"
ROLLED BACK @production: v3 -> v2 (canary MAPE regression)   # seconds, no redeploy
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Shadow serves candidate answers | `shadow` flag not gating the return | In shadow, log candidate but always return incumbent |
| Canary % looks wrong | Randomness over too few requests | Send more traffic; law of large numbers; or use a hash-based split |
| Gate always says `ramp` | Tolerance too loose / no actuals | Restore tolerance; join actuals before MAPE |
| Rollback "no previous version" | Only one version exists | Register ≥ 2 versions; rollback needs a prior to point to |
| Replicas keep serving rolled-back-from version | Model not refreshed | Re-point alias + trigger replica model refresh/restart; discuss dwell time |

**Instructor notes.** The whole course lands in step 5: rollback is *one command, seconds, no rebuild*, because every earlier module built toward alias-based loading and registry promotion. Make participants feel the contrast — ask "how would you roll back the Level-0 Tayyār from Module 1?" (find the pickle, hope, copy, restart) versus this one re-point. The regressed-candidate rollback (step 4→5) is the emotional payoff of the five days; do not rush it. Fast finishers: add a minimum dwell time to prevent alias thrash, and auto-fire the rollback from the gate's `rollback` decision (fully automated revert).

## Mini Exercises

**Quiz.** (1) Shadow vs canary — which serves candidate answers to users? → canary serves a slice; shadow serves none. (2) Why ramp a canary on a metric, not just a timer? → time passing is not evidence of quality; the gate proves non-inferiority. (3) In this architecture, what *is* a rollback? → re-pointing the `@Production` alias to the previous version — seconds, no redeploy. (4) Model version vs deployment — why keep them separate? → registry tracks which versions exist; the alias/router tracks which gets traffic; Module 7 depends on the split. (5) Which change suits blue-green over canary? → an infra/environment change you want to switch atomically, vs a model change you want to expose gradually.

**Debugging exercise.** Branch `sim-timer-canary`: the ramp advances purely on elapsed time with no metric check; a regressed candidate ramps to 100% because "an hour passed." Participants add the non-inferiority gate and explain why time alone is not evidence.

**Code-review exercise.** Review a release PR that swaps the model straight to 100%, has no rollback path other than a rebuild, and compares candidate to incumbent on different time windows. Three findings + the safe-release argument.

**Discussion.** Grid operations insists on approving every forward promotion to production traffic, but wants rollback fully automated. Draw the gate: which transitions are machine-automatic and which are human-gated, and why is that the right split for critical infrastructure?

## Case Study — The Canary That Saved the Southern Area

**Scenario.** A Saudi grid operator retrained its forecaster after a strong offline improvement (overall MAPE 2.9% → 2.6%). The old process would have swapped it to production. The new process shadow-tested it for a week, then canaried at 10% — and the automated gate refused to ramp.

**Business context.** The candidate's *overall* MAPE was genuinely better, but on live Southern-area traffic it was materially *worse* (3.9% vs the incumbent's 3.3%) — a regime the offline holdout under-represented. Under-forecasting the Southern area risks load-shedding; the averaged offline metric had hidden it, exactly as Module 2 warned.

**Technical challenge.** Catch a per-area regression that a better *overall* offline metric masked, using live production evidence, before it reached full traffic — and revert instantly when it surfaced.

**Constraints.** The candidate looked better by the headline number; leadership was keen to ship the improvement; the Southern regression only appeared on live traffic, not the offline holdout; any revert had to be instant and evidence-backed for the change record.

**Solution approach.** Shadow first (a week, zero risk) surfaced the Southern gap in live comparison; the canary gate's *per-area* non-inferiority check refused to ramp past 10% and auto-signalled rollback; the one-command alias re-point reverted to the incumbent in seconds, with the reason ("Southern-area MAPE regression on live traffic") recorded for the CAB. The candidate went back for re-featuring on Southern-area data — the loop, working as designed. The averaged-metric trap from Module 2 was caught by live progressive delivery, not offline testing.

**Discussion questions.** (1) Why did the offline SLA pass but the canary gate fail — what did live traffic reveal? (2) Why is shadow the right *first* stage here rather than jumping to canary? (3) How does the per-area gate connect back to Module 2's champion-selection lesson? (4) What does the recorded rollback reason give the change-advisory board?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Rollback time | Operability | < 60 s (alias re-point, no rebuild) | timed rollback |
| Shadow risk to users | Safety | 0% (candidate serves nothing) | served-role audit |
| Canary blast radius | Safety | ≤ 10% at first step | traffic split check |
| Promotion gate on live metric | Governance | Ramp only if non-inferior; regress → rollback | gate decisions |
| Per-area regression caught | Correctness | Southern regression halts ramp | canary run |
| Every transition recorded | Governance | owner + reason + timestamp on each re-point | alias tag audit |

**Example benchmark table:**

| Stage | Candidate traffic | Overall MAPE (cand) | Worst-area (cand) | Gate decision | Rollback time |
|---|---|---|---|---|---|
| Shadow (1 week) | 0% | 2.6% | 3.9% (Southern) | hold — investigate | — |
| Canary 10% (good cand) | 10% | 2.63% | 3.3% | ramp → 25% | — |
| Canary 10% (regressed cand) | 10% | 2.6% | 3.9% (Southern) | rollback | 12 s |
| Post-rollback | 0% | — | incumbent restored (2.71%/3.3%) | stable | — |

## Required Visuals and Training Assets

### Diagrams
1. **Three release strategies** — *Purpose:* the choosing tool. *Elements:* shadow (copy in, output discarded), canary (10%→100% ramp), blue-green (atomic switch) side by side with risk/rollback annotations. *Style:* three-panel comparison.
2. **Alias-driven traffic split** — *Elements:* `@Production` and `@candidate` aliases; the release controller routing a fraction; both logging with a `role` tag. *Style:* router diagram with alias badges.
3. **The promotion gate + auto-rollback** — *Elements:* canary metric compared to incumbent; non-inferior → ramp; regression → rollback (alias re-point). *Style:* decision loop with a rollback branch.
4. **Rollback = re-point** — *Purpose:* the payoff image. *Elements:* the `@Production` alias arrow moving from v3 back to v2 in one motion; "seconds, no rebuild" callout; contrasted with the Level-0 pickle-hunt. *Style:* before/after alias arrow with a stopwatch.

### Images
1. **Shadow log** showing `role=served` (incumbent) + `role=candidate` on the same trace — *why:* zero-risk comparison; *content:* two log rows, same inputs, both versions.
2. **Canary ramp decisions** in a terminal — *why:* evidence-based ramp; *content:* the `ramp` JSON decisions climbing 10→100.
3. **Gate `rollback` decision** on a regressed candidate — *why:* the gate refusing to ramp; *content:* the rollback JSON with both MAPEs.
4. **Rollback alias re-point** with reason/owner tags — *why:* the seconds-not-hours payoff; *content:* the one-command output + the recorded tags.

### Simulations
1. **Timer-only canary** — *Setup:* `sim-timer-canary` ramps on time with no gate. *Expected:* a regressed candidate reaches 100%. *Learning objective:* ramp on evidence, not a clock.
2. **Per-area regression on live traffic** — *Setup:* candidate better overall, worse on Southern. *Expected:* the per-area gate halts and rolls back. *Learning objective:* live progressive delivery catches what offline averages hide.
3. **Rollback race** — *Setup:* two versions, live traffic, a regression. *Expected:* one-command alias re-point restores service in seconds. *Learning objective:* architecture makes rollback trivial.

### Interactive Activities
- **Strategy-fit sort (10 min):** 8 changes (new model, new serving image, threshold tweak, K8s upgrade…) sorted onto shadow/canary/blue-green with justification.
- **Gate-design workshop (15 min):** pairs write the non-inferiority rule (metric, window, tolerance, per-area check) for a given SLA and defend the tolerance.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `prediction_log.parquet` (with `role`) | Module-5/7 serving | Parquet | grows | Gate comparison (served vs candidate) |
| Candidate model `@candidate` | Module-6 retrain | Registry | 1 version | The thing being released |
| Regressed candidate | Course team | Registry | 1 version | Rollback simulation |

### Demo Requirements
- **Instructor demo:** shadow a candidate (show users unaffected), canary it with the gate ramping, then swap in a regressed candidate and execute the one-command rollback live — timing it under a minute to land the payoff.
- **Student demo:** one pair walks their gate's `ramp` vs `rollback` decisions and executes a rollback, stating the recorded reason.
- **Expected outputs:** every participant has shadowed, canaried, and rolled back a candidate via alias re-point, with every transition recorded, before the capstone.

---

# Final Capstone Project

## Title: The Tayyār MLOps Platform — Reproducible, Monitored, Safely-Released Load Forecasting

*(Covers Topic 8 — "MLOps platform project": the integration of every module into one operated platform.)*

## Project Scenario

You are the MLOps engineer for **Tayyār (تيّار)**, the short-term electricity load-forecasting platform of the National Grid Operations Center (NGOC). On Day 1 you inherited a Level-0 notebook (`forecast.ipynb`), an emailed CSV, and a `model.pkl` copied to a server by hand. Over five days you have built, one lab at a time, every component of a governed MLOps system. The capstone is **not new work — it is the integration**: wire your tracked experiments, versioned data and features, orchestrated training, registry, serving, monitoring, and release machinery into *one reproducible, monitored, automatically-retraining, safely-released platform*, and prove — repo-first — that it operates at MLOps Level 2. NGOC will trust the platform because *its repository, run history, and lineage prove their own quality*.

## Requirements

**Mandatory (maps to the grading rubric):**

1. **Reproducible training (LO1, LO2):** MLflow tracking with the four lineage tags on every run (`git_sha`, `data_version`, `feature_set_version`, `python_env`); DVC-versioned `grid_load_hourly.csv` pushed to the shared remote; the single shared `features.py` imported by training and serving; a passing skew test.
2. **Registry & governance (LO2):** `tayyar-load-forecaster` registered with signature + input example; champion selected by the operations SLA (overall ≤ 3.0%, worst-area ≤ 3.5%) with a recorded `selection_reason`; staged/aliased promotion; lineage reachable from a version to its data + code.
3. **Orchestrated CT (LO4):** an Airflow/Prefect `train_tayyar` pipeline (ingest → validate → featurise → train → evaluate → register) that is idempotent, retries transient failures, gates registration on the SLA, and is API-triggerable; bad data short-circuits it.
4. **Serving, two ways (LO3):** a containerised online next-hour API (registry-alias load, readiness-gated on model load, prediction logging, `X-Model-Version` header) *and* an idempotent day-ahead batch scorer; a readable K8s `Deployment`+`Service` applied to a local cluster.
5. **Monitoring & the closed loop (LO5):** a scheduled Evidently monitoring job producing durable drift + regression reports over the prediction log; a *sustained-decay* (hysteresis) trigger that fires `train_tayyar` with evidence attached — the closed CT loop.
6. **Safe release & rollback (LO6):** shadow → canary (10% → 100%) behind an automated non-inferiority gate (incl. per-area check); one-command rollback as an alias re-point, with owner/reason/timestamp recorded.
7. **Operability (all LOs):** `README.md` runbook (`make platform-up`, retrain, serve, monitor, release, rollback — a stranger succeeds in 15 minutes); `BENCHMARKS.md` filled with *your own measured numbers* from the six per-module benchmark tables; `DECISIONS.md` with five engineering-decision paragraphs.

**One extension (choose at least one):**
- **Feature store online path:** materialise `load_lag_*` into Redis and serve the online API from it (not the CSV), with an offline/online consistency check.
- **Fully-automated rollback:** wire the promotion gate's `rollback` decision to fire `rollback.py` automatically, with a minimum-dwell guard against alias thrash.
- **Per-area canary gate:** ramp only if *every* operating area is non-inferior (the Southern-area lesson, automated).
- **Cost/compute tracking:** log compute-minutes-per-retrain as an MLflow metric and chart the CT cost over a month.
- **Blue-green for the serving image:** a green environment for an image/K8s change with an atomic switch and one-flag revert.

## Architecture (target state)

```
 DATA:     grid_load_hourly.csv ──DVC──> remote (hash = data_version)
                     │                         │
 TRAIN:   Airflow/Prefect train_tayyar: ingest→validate→featurise→train→evaluate(SLA gate)→register
                     │  MLflow tracking (lineage tags) ── Model Registry (@Staging/@Production/@candidate)
                     ▼
 SERVE:   online API (readiness-gated) ─┐        day-ahead batch (idempotent) ─┐
                     │  release controller (shadow / canary via aliases)        │
                     ▼                                                          ▼
 LOG:                └────────────► prediction_log.parquet (inputs+preds+model_version+actuals) ◄─┘
                                              │
 MONITOR: Evidently monitor_tayyar (@daily) → drift + MAPE reports → sustained decay → TRIGGER train_tayyar
                                              │
 RELEASE: challenger → shadow → canary(gate) → promote(@Production)  |  regression → rollback(alias re-point, <60s)
```

## Deliverables

1. Git repository URL (instructor-shared) with full history and the checkpoint commits.
2. MLflow experiment link: `tayyar-load-forecaster` registered, aliased, with lineage reachable to data + code.
3. A green end-to-end run recording: retrain (triggered) → SLA gate → register → shadow → canary → promote, plus one demonstrated rollback.
4. `README.md` runbook + `BENCHMARKS.md` (six tables filled from *your* runs) + `DECISIONS.md`.
5. 8-minute demo: `make platform-up`, one online forecast (show the model-version header), a drift report, a canary ramp, and a one-command rollback.

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: Tracking + registry + DVC + skew test integrated | End Day 2 H1 | instructor spot-check of lineage |
| M-B: `train_tayyar` DAG green end-to-end, SLA-gated | End Day 2 | triggered run + registered `@Staging` |
| M-C: Online API + batch + K8s applied | Day 3 H3 | readiness gate demo + batch parquet |
| M-D: Monitoring + closed retraining loop | Day 4 H2 | drift report + trigger fires DAG |
| M-E: Shadow + canary + rollback | Day 4 H4 | timed rollback < 60 s |
| M-F: Assembly + demo + submission | Day 5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Reproducibility & lineage | 18 | All runs carry 4 tags; DVC data resolvable; skew test green; a version traces to exact data+code | Minor gaps (one tag missing, occasional) | Loose pickle, untracked data, no lineage |
| Registry & governance | 14 | Signature + SLA champion + `selection_reason` + governed alias transitions | Registered but weak selection/record | Direct-to-production, no signature, no reason |
| Orchestrated CT | 16 | Idempotent SLA-gated DAG, transient-retry, bad-data short-circuit, API-triggerable | Works but a gap (no gate branch or non-idempotent) | Cron chain / mega-task / no gate |
| Serving (online + batch) | 16 | Alias-load, readiness-gated, logging, header; idempotent partial-failure batch; K8s applied | One path weak (no readiness gate or non-idempotent batch) | Per-request load, no logging, no readiness |
| Monitoring & closed loop | 16 | Data+concept+performance monitoring; hysteresis trigger fires CT with evidence | Detects drift but loop not closed or noisy | Input-only or no scheduled monitoring |
| Release & rollback | 14 | Shadow→canary with automated gate (per-area) + < 60 s alias rollback recorded | Canary works but weak gate or slow rollback | Big-bang swap, rebuild-to-rollback |
| Runbook, benchmarks, decisions | 6 | Stranger runs it in 15 min; real numbers; trade-off literacy | Works, rationale thin | Cannot run own repo cold |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade **repo-first**: MLflow run history, DVC lineage, DAG-run history, monitoring reports, and release/rollback evidence *before* the demo. The whole course's thesis is that the repository proves its own quality.
- Anti-pattern flags that cap a criterion at 70%: a registry entry whose lineage points to `data: latest`; an evaluation gate with ceilings set to 1.0 (disabled gate); a rollback that requires a rebuild; a canary that ramps on a timer with no metric; predictions not logged (monitoring impossible).
- Verify one claim live: ask the participant to point `@Production` at a regressed version and roll it back — time it, and read the recorded reason tag.

## Bonus Tasks (for early finishers / distinction seekers)

1. **Chaos drill:** kill a serving replica mid-canary; show K8s + readiness keep service correct.
2. **Reproduce a forecast under audit:** given a past prediction's `model_version`, rebuild the exact data + code + model and reproduce the number.
3. **Cost-of-CT chart:** compute-minutes per retrain over simulated weeks; argue the schedule-vs-drift trigger trade-off.
4. **Skew hunt:** introduce a serving-layer skew; show which test/monitor catches it; write a 10-line postmortem.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** The three things that change in an ML system vs one in ordinary software? → code, data, and the world (the data-generating process).
**Q2.** What single artefact proves a team is at Level 1? → an orchestrated pipeline run (with lineage) that produced the current model.
**Q3.** Define CT and how it differs from CD. → CT retrains the model on a trigger; CD delivers/releases a validated artefact; CT feeds CD.
**Q4.** Name the four lineage tags every Tayyār run must carry. → git_sha, data_version, feature_set_version, python_env.
**Q5.** Why log the data *version* not the data itself? → data belongs in DVC; artefact stores bloat and duplicate; the version is the link.
**Q6.** What does a model *signature* buy the serving team? → a validated I/O schema — skew defence and fail-loud at the boundary.
**Q7.** What does git commit when you `dvc add` a file, and where do the bytes go? → the tiny `.dvc` pointer (hash) to git; the bytes to the DVC cache then the remote on `dvc push`.
**Q8.** Why is one shared feature module the skew defence? → training and serving compute identical values by construction.
**Q9.** What is point-in-time correctness? → building features from only the data available at prediction time (no future leakage).
**Q10.** Why pass references, not payloads, between orchestrator tasks? → keeps the metadata backend light and the lineage explicit; the stores are the channel.
**Q11.** Where is the promotion gate in the training DAG, and what does it check? → the `evaluate` task before `register`; the operations SLA (and beats-incumbent).
**Q12.** Transient vs deterministic failure — different handling? → retry (backoff) transient; alert (don't loop) on deterministic.
**Q13.** The three serving patterns and the freshness each offers? → batch (as-of-last-run), online (on-demand now), streaming (seconds).
**Q14.** Liveness vs readiness for a model server? → liveness restarts a dead process; readiness gates traffic until the model is loaded.
**Q15.** Why load a model by alias, not version or path? → makes rollback a re-point; replicas pick up the new version on refresh.
**Q16.** Data drift vs concept drift — which is visible in the inputs? → data drift shifts P(X) (visible); concept drift shifts P(y|X) (invisible in inputs, visible in performance).
**Q17.** Why monitor both inputs and actuals? → inputs are leading (fast), actuals are lagging (definitive); each catches what the other misses.
**Q18.** Why hysteresis on a retraining trigger? → one anomalous day is not decay; require persistence to avoid retraining on noise.
**Q19.** Shadow vs canary — which serves candidate answers to users? → canary serves a slice; shadow serves none (logs only).
**Q20.** In this architecture, what *is* a rollback and how long should it take? → re-pointing the `@Production` alias to the previous version; seconds, no rebuild.

## Practical Assessments

**PA-1 (30 min, Day 2):** Given a broken `train_tayyar` DAG (a dataframe in XCom, the SLA gate disabled at ceiling 1.0, `retries=100` on a deterministic validation), diagnose and fix to a green, correctly-gated run. Scored on: diagnosis notes (40%), fixes (40%), verification evidence — a rejected-candidate green run (20%).

**PA-2 (30 min, Day 4):** Given a monitoring + release scenario (a heatwave drift report and a candidate that is better overall but worse on the Southern area), triage: does it trigger a retrain? Should the candidate be promoted? Write the decision and execute a rollback. Scored against the model answer (triage correctness 50%, governance reasoning 30%, evidence/record quality 20%).

**PA-3:** Capstone (rubric above) — 40% of the course grade. Labs completion + PA-1/PA-2 + quiz — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (Labs 1–7) | 30% | checkpoint commits + expected outputs (MLflow/DVC/DAG/reports) |
| PA-1 + PA-2 | 20% | artefacts + diagnosis/decision notes |
| Quiz | 10% | 10-question selection |
| Capstone | 40% | rubric, repo-first (run history + lineage + release evidence) |

Badge issuance (MLOps badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical DVC hashes / MLflow run copies across repos are checked). The capstone is the prerequisite evidence for SDA-AIE-312 and the LLMOps/reliability modules.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone the course org repo; push checkpoint tags (`lab1-start` … `lab7-start`) and pre-seeded MLflow/DVC state so stragglers can `git checkout lab4-start && dvc pull`.
- [ ] Bring up the `make platform-up` stack (MLflow + Postgres + MinIO + Airflow/Prefect + Redis + a local registry) on a clean machine **and** verify the hosted classroom-stack fallback.
- [ ] Regenerate `grid_load_hourly.csv` (2 years × 4 areas, with the KSA summer/Ramadan/Hajj load shape) and the `shifted_week.csv` / `solar_reshaped_week.csv` drift fixtures; verify the seeded MAPE numbers still hold.
- [ ] Dry-run all 7 labs end-to-end, timing Labs 4 (orchestration) and 7 (release) — the two overrun-prone sessions.
- [ ] Stand up a local `kind`/`minikube` cluster and confirm `kubectl apply -f k8s/tayyar-forecast.yaml` rolls out; test the bad-`MODEL_URI` not-ready demo.
- [ ] Seed 2–3 repos with deliberate serving/feature skew so the Module-3/5 skew tests genuinely go red in the room.
- [ ] Print A4 posters: the three-plane architecture, the maturity ladder, the training DAG, the closed CT loop, the three release strategies.
- [ ] Confirm the classroom network reaches (or mirrors) the internal MLflow/MinIO/registry; in restricted environments pre-pull base images to the local registry.
- [ ] Prepare the shared leaderboard (per-area MAPE, rollback times, image sizes).

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + git + a working `docker` (`docker run hello-world`) and `docker compose`.
- [ ] `pip install mlflow lightgbm scikit-learn "dvc[s3]" pandas pyarrow "fastapi[standard]" uvicorn redis evidently apache-airflow` (or `prefect`).
- [ ] A local Kubernetes: `kind` or `minikube` + `kubectl`; verify `kubectl get nodes`.
- [ ] `hey`/`ab`, `jq`, and `make` available.
- [ ] Clone the course repo; run `make doctor` (validates all of the above and prints ✓/✗) and `make platform-up` once to pre-pull images.

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| Runs land in local `mlruns/` not the server | High | Export `MLFLOW_TRACKING_URI`; confirm in the run source; check MinIO creds |
| Docker/WSL2 not enabled on Windows | High | Pre-session email + first-hour floater support; hosted-stack fallback |
| DVC push auth failures to MinIO | Medium | Export `AWS_ACCESS_KEY_ID/SECRET` + `MLFLOW_S3_ENDPOINT_URL` from `platform.env` |
| Skew test passes when it shouldn't | Medium | KSA weekend/Hijri edge cases; route both paths through `features.py` — the lesson |
| DAG re-run double-registers | Medium | Non-idempotent register; write run-scoped, register by content |
| `/ready` never turns 200 | Medium | Wrong `MODEL_URI`/alias or registry unreachable; check inside-boundary URI |
| Evidently "no target" errors | Medium | Join observed `actual_mw` before RegressionPreset; drop rows without actuals |
| Canary % looks wrong on few requests | Low | Law of large numbers — send more traffic, or hash-based split |
| K8s pods stuck `0/1 Ready` | Low | The readiness probe doing its job; `kubectl logs`; fix the model URI |

## Timing Recommendations

- Protect **Lab 4 (orchestration)** and **Lab 7 (release)** at full length — they overrun most. Publish checkpoint commits + pre-seeded state so stragglers fast-forward rather than fall behind.
- Compress **M6 theory** (it lands through the lab) if behind; never cut the closed-loop demo — it is the Level-2 moment.
- Day 5 is deliberately light on new theory: it is assembly-and-demo time. Start capstone assembly (Day 4 H5 / Day 5 H1) *on time*; cut discussion, not build time.
- Keep the Day-1 architecture canvas on the wall all five days and physically tick each component as its module lands — the capstone is visibly "assemble", not "build from scratch".

## Discussion Prompts (use during transitions)

1. "How would you roll back the Level-0 Tayyār from Day 1 — and how long would it take under a peak-demand incident?"
2. "Your model is 2.6% MAPE overall and 3.9% on the Southern area. Which number does grid operations feel — and which does the SLA protect?"
3. "Who owns the decision to promote a forecaster to production — data science, engineering, or grid operations? Where does that put the promotion gate?"
4. "If the repository is the audit evidence, what does *your* current repo testify about your team's maturity level?"
5. "Which of the seven components would have caught your last production incident earliest?"

## Wrap-up (Day 5 final 15 minutes)

- Map each capstone requirement back to the module (and lab) that taught it — one slide; the capstone is the assembly of seven components, not new work.
- Re-walk the maturity ladder: Tayyār went from Level 0 (notebook, emailed CSV, hand-copied pickle) to Level 2 (tracked, versioned, orchestrated, served, monitored, safely-released with a closed CT loop) over five days.
- Forward pointers: **SDA-AIE-312** and the LLMOps/reliability modules consume *exactly* this platform — they harden the same shape of system for reliability and extend it to LLM operations; the capstone repo + registered model are the prerequisite evidence.
- Collect: repository URLs, MLflow experiment links, `BENCHMARKS.md`, `DECISIONS.md`; issue MLOps-badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.12, MLflow ≥ 2.9, DVC ≥ 3, Airflow ≥ 2.8 / Prefect ≥ 2.14, FastAPI ≥ 0.110, pydantic v2, Evidently ≥ 0.4, and LightGBM ≥ 4. Verify pinned versions in the course lock file before each delivery, and confirm the `make platform-up` stack and the local Kubernetes cluster the week before delivery.*





