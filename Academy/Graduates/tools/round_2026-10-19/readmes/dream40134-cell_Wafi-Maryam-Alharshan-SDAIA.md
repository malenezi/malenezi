# Wafi — IT Helpdesk Ticket Triage

Classifies an incoming IT support ticket into `{team, urgency}` so it can be
routed automatically. Built for the SDA-AIE-113 capstone.

## Quickstart (< 10 minutes)

```bash
git clone <your-repo-url>
cd wafi
make install        # editable install + dev deps
make test           # unit + integration + behavioural, coverage gate 80%
```

## Run the service

```bash
docker compose up --build
```

This starts `wafi` on `http://localhost:8000` alongside a `redis` supporting
service. `wafi` waits for redis to report healthy before starting.
Configuration is passed via `WAFI_*` environment variables in
`docker-compose.yml` — see `.env.example` for the full list if running
without Docker.

## Try it

```bash
# valid request
curl -X POST http://localhost:8000/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "my vpn keeps dropping every few minutes"}'

# malformed request (unknown field -> 422)
curl -X POST http://localhost:8000/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "hello", "not_a_real_field": true}'

curl http://localhost:8000/health   # liveness
curl http://localhost:8000/ready    # readiness
```

## Architecture

```
src/wafi/
  domain/     pure business rules — no imports from any other layer
  service/    use-case orchestration, depends on domain + the classifier Protocol
  adapters/   concrete classifier + idempotency cache, implement Protocols via DI
  api/        FastAPI endpoints, config, logging — wires everything together at startup
```

The layering is enforced automatically by `import-linter` (`make lint`) —
`domain` cannot import from `service`, `adapters`, or `api`; the layers
contract in `pyproject.toml` enforces the full stack order.

The model is swappable: `wafi.adapters.classifier_protocol.TicketClassifier`
is the interface; `KeywordClassifier` is the current implementation, injected
into `TriageService` at startup (`src/wafi/api/app.py`).

## Testing

| Level | Location | What it proves |
|---|---|---|
| Unit | `tests/unit/` | domain policy + classifier logic in isolation |
| Integration | `tests/integration/` | the real FastAPI app, via `TestClient` |
| Behavioural — invariance | `tests/behavioral/test_invariance.py` | an outage phrase **always** forces `urgent` |
| Behavioural — directional | `tests/behavioral/test_directional.py` | more affected users never **lowers** urgency |
| Behavioural — golden | `tests/behavioral/test_golden.py` + `golden/golden_cases.json` | live output matches a frozen reference set |

Fast gate (unit + behavioural, no Docker) finishes in well under 60s:
`make test-fast`.

## Extension: idempotency cache

An identical ticket (same text + `affected_users`) submitted twice returns
the same decision without being re-classified. Backed by Redis
(`RedisIdempotencyCache`), injected into `TriageService` the same way the
classifier is (constructor DI). Falls back to a no-op `NullCache` if
`REDIS_URL` isn't set, and fails open (logs a warning, treats as a
cache miss) if Redis is unreachable — a caching layer going down must never
take ticket triage down with it.

Try it (with `docker compose up`, which sets `REDIS_URL` for you):
```bash
curl -X POST http://localhost:8000/v1/predict -H "Content-Type: application/json" \
  -d '{"text": "my vpn keeps dropping"}'
# run the exact same request again -> same team/urgency, and the response's
# "rationale" field will say "served from idempotency cache"
```

Tested in `tests/unit/test_triage_service_cache.py` (fake in-memory cache —
proves a cache hit skips the classifier) and
`tests/behavioral/test_idempotency_cache.py` (the real `RedisIdempotencyCache`
against `fakeredis`, no live Redis needed to run the test suite).

## Config, secrets & logging

Typed settings (`src/wafi/api/config.py`, `pydantic-settings`) fail fast:
an invalid `WAFI_LOG_LEVEL` or an unrecognized `WAFI_*` variable crashes the
process at startup instead of being silently ignored (`extra="forbid"`).
See `.env.example` for the full list — copy it to `.env` for local runs;
`.env` itself is gitignored and no real secret is ever committed.

Logs are structured JSON, one object per line, each correlated with the
request's `trace_id` (also returned in the `x-trace-id` response header and
the `/v1/predict` response body). Ticket text itself is never logged — only
its length and the resulting `team`/`urgency` — to avoid leaking personal
data a reporter may have included in the ticket.

## Repo docs

- `DECISIONS.md` — five engineering decisions with rationale
- `BENCHMARKS.md` — fill in with numbers from your own machine




## Acknowledgments

This project was completed as part of the SDA-AIE-113 — Software Engineering
Practices for AI Systems training program at SDAIA Academy, under the
supervision of Abdullah Khalid AlShahrani.

The portfolio demonstrates the practical application of software engineering
practices for AI systems — building a production-style AI/ML service through
clean architecture, a well-defined API contract, containerization, a layered
automated testing suite, a CI/CD pipeline with branch protection, and safe
configuration, secrets, and logging management.

Official SDAIA Academy GitHub: https://github.com/SDAIAAcademy

## About This Project — MLOps Engineering Perspective

This capstone was built and delivered end-to-end in an MLOps engineering
role, covering the full lifecycle of shipping a production-style AI service
rather than just its model logic:

- **Clean architecture** — the codebase is split into `domain`, `service`,
  `adapters`, and `api` layers, with dependency direction enforced
  automatically by `import-linter` contracts in `pyproject.toml`, so the
  business rules never depend on infrastructure or framework code.
- **Swappable model interface** — the classifier sits behind the
  `TicketClassifier` Protocol, so the current rule-based `KeywordClassifier`
  can be replaced by a trained model later without touching `service/` or
  `api/`.
- **API contract & containerization** — a versioned FastAPI contract
  (`/v1/predict`, `/health`, `/ready`) packaged into a Docker image, with a
  `docker-compose.yml` that health-gates the app against its Redis
  dependency before routing traffic.
- **Layered automated testing** — unit, integration, and behavioural test
  suites (including invariance, directional, and golden-set tests) enforce
  an 80% coverage gate and run automatically on every change.
- **CI/CD with branch protection** — a GitHub Actions pipeline (lint, test,
  image-smoke, publish) gates every merge to `main`, backed by required
  status checks and mandatory review before merging.
- **Safe configuration, secrets & logging** — typed, fail-fast settings
  (`pydantic-settings`, `extra="forbid"`), structured JSON logs correlated
  by `trace_id`, and secret-scanning discipline to keep credentials out of
  the codebase entirely.

Together these practices reflect the day-to-day responsibilities of an
MLOps engineer: not just building a model, but making it reliable,
observable, testable, and safely deployable in a real engineering
workflow — which is the core objective of the SDA-AIE-113 course.
