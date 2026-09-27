"""Module 8/final capstone — `/healthz` (liveness) and `/readyz` (readiness).

TEACHING POINT: liveness and readiness answer DIFFERENT questions.
`/healthz` asks "is the process alive at all" — it must be nearly free
and never depend on anything external, or a slow dependency turns into a
false "the whole service is down". `/readyz` asks "can this instance
actually serve a request right now" — it DOES check dependencies (seed
data on disk, the vector store, the four MCP servers, which model mode is
configured), because a process that is alive but has no data to read is
not ready, and a deploy/rollback decision (`deployment/runbook.md`) reads
`/readyz`, not `/healthz`.

Both are plain functions returning `schemas.HealthStatus` so they can be
called directly (a unit test, `scripts/selfcheck.py`, the stdlib HTTP
fallback) with no web framework at all; `service/api.py` exposes them as
routes when FastAPI is available.

Dependency-free (Layer A): stdlib + `rafeeq.core.config` only. MCP
reachability is checked by IMPORTING `mcp_servers.*` (they import-guard
`mcp` themselves, per SPEC §1) rather than opening a real stdio
connection — this module never spawns a subprocess.
"""
from __future__ import annotations

from typing import Any

from rafeeq.core.config import (
    CUSTOMERS_SEED_PATH,
    ORDERS_SEED_PATH,
    PAYMENTS_SEED_PATH,
    TICKETS_EVAL_PATH,
    get_settings,
)
from rafeeq.service.schemas import HealthStatus


def liveness() -> HealthStatus:
    """`/healthz` — the process can answer at all. No I/O, no imports of
    anything that could itself be unhealthy; this must stay cheap enough
    to poll every few seconds without adding load."""
    return HealthStatus(status="ok", checks={"process": "alive"})


def _check_data_files() -> tuple[bool, dict[str, Any]]:
    files = {
        "customers_seed": CUSTOMERS_SEED_PATH,
        "orders_seed": ORDERS_SEED_PATH,
        "payments_seed": PAYMENTS_SEED_PATH,
        "tickets_eval": TICKETS_EVAL_PATH,
    }
    detail: dict[str, Any] = {}
    ok = True
    for name, path in files.items():
        exists = path.exists()
        detail[name] = "present" if exists else "MISSING"
        ok = ok and exists
    return ok, detail


def _check_vector_store() -> tuple[bool, str]:
    try:
        from rafeeq.memory.vector_store import get_store

        get_store("readiness_probe")  # constructs/loads the collection; no network in stub/simple mode
        return True, "ok"
    except Exception as exc:  # noqa: BLE001 - readiness must report, never raise
        return False, f"{type(exc).__name__}: {exc}"


def _check_mcp_servers() -> tuple[bool, dict[str, str]]:
    """Import each MCP server module (they import-guard `mcp` itself) —
    a real deployment additionally pings each server's stdio process; in
    stub/offline mode (the default, SPEC §1) this is the honest
    equivalent of "reachable": the server code is present and importable,
    and `rafeeq.tools.mcp_client.load_tools_local()` is the fallback
    transport the agent actually uses in that mode."""
    servers = ("orders_server", "logistics_server", "billing_server", "customer_server")
    detail: dict[str, str] = {}
    ok = True
    for name in servers:
        try:
            __import__(f"mcp_servers.{name}")
            detail[name] = "importable"
        except Exception as exc:  # noqa: BLE001 - readiness must report, never raise
            detail[name] = f"MISSING: {type(exc).__name__}: {exc}"
            ok = False
    return ok, detail


def readiness() -> HealthStatus:
    """`/readyz` — can this instance serve `/v1/resolve` right now.
    Checks: seed data on disk, the vector store constructs, the four MCP
    server modules import, and reports which model mode is active (not a
    pass/fail on its own — `stub`/`replay` are valid, intentional modes;
    `live` with no API key is the one combination worth flagging)."""
    settings = get_settings()
    data_ok, data_detail = _check_data_files()
    vector_ok, vector_detail = _check_vector_store()
    mcp_ok, mcp_detail = _check_mcp_servers()

    model_mode_ok = True
    model_mode_detail = settings.model_mode
    if settings.model_mode == "live" and not settings.openai_api_key:
        model_mode_ok = False
        model_mode_detail = "live mode configured but OPENAI_API_KEY is not set"

    checks = {
        "data_files": data_detail,
        "vector_store": vector_detail,
        "mcp_servers": mcp_detail,
        "model_mode": model_mode_detail,
        "vector_mode": settings.vector_mode,
        "embed_mode": settings.embed_mode,
    }
    overall_ok = data_ok and vector_ok and mcp_ok and model_mode_ok
    status = "ok" if overall_ok else ("degraded" if (data_ok and mcp_ok) else "down")
    return HealthStatus(status=status, checks=checks)
