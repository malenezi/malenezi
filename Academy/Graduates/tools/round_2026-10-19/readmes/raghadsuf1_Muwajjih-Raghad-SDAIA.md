# Muwajjih — AI Government Complaint Triage

Muwajjih is a production-oriented AI service that receives a short municipal/government complaint and returns the most likely department plus a normal/urgent priority. It is deliberately designed to demonstrate the SDA-AIE-113 engineering practices: clean architecture, strict FastAPI contracts, model lifecycle control, Docker/Compose, a three-level test pyramid, behavioural model tests, CI/CD, typed configuration, secrets hygiene, and trace-correlated JSON logging.

## 10-minute runbook

### 1. Install

```bash
python -m venv .venv
source .venv/bin/activate
make install
```

### 2. Run the full local stack

```bash
make up
docker compose ps
```

Expected: `muwajjih-api` and `feature-cache` are `healthy`.

### 3. Smoke the service

```bash
make smoke
```

### 4. Run the fast gate

```bash
make lint
make typecheck
make arch
make test
```

### 5. Run the behavioural suite

```bash
make test-slow
```

### 6. Inspect the API

Open `/docs` on the running service. The primary endpoint is:

```text
POST /v1/predict
```

Example request:

```json
{
  "complaint_id": "MWJ-DEMO-001",
  "text": "هناك حريق قرب مدرسة"
}
```

Muwajjih returns an envelope with `trace_id`, decision data, model version and reason codes.

## Architecture

```text
FastAPI API
    |
    v
Service / TriageScorer ----> Model Protocol <---- sklearn adapter
    |
    v
Domain policies
    |
    +---- Cache Protocol <---- Redis adapter
```

The domain and service layers do not import FastAPI, sklearn or Redis. The concrete model is injected through a Protocol. The emergency-priority rule is deterministic business policy applied after model inference.

## Behavioural claims

- **Invariance:** casing and whitespace are noise and must not change the decision.
- **Directional:** adding an explicit emergency signal must not lower the priority; policy promotes it to `urgent`.
- **Golden:** `models/golden_scores_v1.csv` is versioned with the model artifact and is deliberately regenerated only with `make regen-golden`.

## Extension

The project includes a bounded batch endpoint, `POST /v1/predictions:batch`, capped at 32 items. This is intentionally bounded and documented so it cannot become an unbounded self-inflicted load vector.

## Security / operational notes

- No secrets are committed; `.env` is ignored and only non-secret configuration is documented in `configs/settings.example.env`.
- Runtime uses a non-root `appuser`.
- Docker readiness targets `/v1/ready`.
- The image is built with a multi-stage Dockerfile and `linux/amd64` in Compose for the course's Apple Silicon/x86 compatibility path.
- CI publishes only immutable commit-SHA tags to GHCR; no `:latest` tag is used.

## Training Program

This project was completed as part of the SDA-AIE-113 — Software Engineering Practices for AI Systems training program at SDAIA Academy, under the supervision of Abdullah Khalid AlShahrani.

The portfolio demonstrates the practical application of software engineering practices for AI systems — building a production-style AI/ML service through clean architecture, a well-defined API contract, containerization, a layered automated testing suite, a CI/CD pipeline with branch protection, and safe configuration, secrets, and logging management.

Official SDAIA Academy GitHub: https://github.com/SDAIAAcademy
