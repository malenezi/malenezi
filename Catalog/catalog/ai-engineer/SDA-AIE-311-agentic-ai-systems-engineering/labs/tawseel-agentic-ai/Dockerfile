# Module 9/final capstone — the Rafeeq service image.
#
# One image serves BOTH deployment shapes docker-compose.yml wires up:
#   - `full` profile: RAFEEQ_MODEL_MODE=live/replay against real Qdrant/
#     Postgres/MCP servers (this image's `requirements.txt` install brings
#     in langgraph/fastapi/uvicorn/qdrant-client — Layer B, SPEC §1 — none
#     of which are available in the training-build sandbox this repo was
#     authored in, but ARE real, installable packages for a deployed
#     container).
#   - `labs` profile: RAFEEQ_MODEL_MODE=stub, no external services at all
#     — the same image, same entrypoint, different env (docs/OFFLINE_MODE.md).
#
# Multi-stage so the runtime image never carries pip's build cache or
# compiler toolchain.

FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /app

FROM base AS deps
COPY requirements.txt requirements-dev.txt* ./
RUN pip install --no-cache-dir -r requirements.txt

FROM deps AS runtime
COPY . .
# A non-root user: the container never needs root, and a compromised
# process (a landed injection, a dependency CVE) should not have it.
RUN useradd --create-home --uid 10001 rafeeq && chown -R rafeeq:rafeeq /app
USER rafeeq

ENV PYTHONPATH=/app/src \
    RAFEEQ_MODEL_MODE=stub \
    RAFEEQ_VECTOR_MODE=simple \
    RAFEEQ_EMBED_MODE=hashing \
    RAFEEQ_HOST=0.0.0.0 \
    RAFEEQ_PORT=8000

EXPOSE 8000

HEALTHCHECK --interval=15s --timeout=5s --start-period=10s --retries=3 \
    CMD python3 -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/healthz', timeout=3).status == 200 else 1)"

# `service/api.py::main()` picks FastAPI+uvicorn when installed, else the
# stdlib http.server fallback — the SAME entrypoint serves either
# deployment shape (SPEC's "genuinely runs anywhere").
CMD ["python3", "-m", "rafeeq.service.api"]
