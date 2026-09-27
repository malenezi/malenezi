#!/usr/bin/env python3
"""Preflight check for the Rafeeq course repo — `make doctor`.

Verifies, in order: the Python version, which optional (Layer-B, SPEC §1)
dependencies are present, whether the generated data files exist and are
internally consistent (delegates to `scripts/selfcheck.py`'s checks),
which runtime modes are active (`RAFEEQ_MODEL_MODE` / `RAFEEQ_VECTOR_MODE`
/ `RAFEEQ_EMBED_MODE`), whether the model gateway is reachable (skipped
entirely when running offline — no network call is ever made unless
`RAFEEQ_MODEL_MODE=live`), and whether Docker is on PATH. It closes with a
one-line verdict per lab: which labs run today with nothing installed
beyond `pydantic`, and which need an extra `pip install` before their
Hands-on Lab can be completed end to end.

Dependency-free by design (stdlib only) so it can be the very FIRST thing
a participant runs on a clean checkout, before anything else in
`requirements.txt` is even considered. `python3 scripts/doctor.py` (or
`make doctor`) from the repo root.
"""
from __future__ import annotations

import importlib.util
import os
import shutil
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

MIN_PYTHON = (3, 11)

# module name -> (pip package name, why it matters)
OPTIONAL_DEPS: dict[str, tuple[str, str]] = {
    "langgraph": ("langgraph", "compiled graphs (Labs 1/2/5/6/7 build_*() functions)"),
    "langchain_core": ("langchain-core", "message types + @tool decorator the graph layer uses"),
    "langchain_openai": ("langchain-openai", "RAFEEQ_MODEL_MODE=live only"),
    "mcp": ("mcp", "real MCP servers over stdio (Lab 3)"),
    "langchain_mcp_adapters": ("langchain-mcp-adapters", "MultiServerMCPClient (Lab 3)"),
    "qdrant_client": ("qdrant-client", "RAFEEQ_VECTOR_MODE=qdrant only (Lab 4 works offline without it)"),
    "psycopg": ("psycopg[binary]", "Postgres checkpointer (capstone only; SQLite is the lab default)"),
    "fastapi": ("fastapi", "`make serve` with real HTTP routes (a stdlib fallback server always works)"),
    "pytest": ("pytest", "pytest-style test files; every one has a stdlib run_without_pytest.py mirror"),
}

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    RESULTS.append((name, ok, detail))
    return ok


def _has_module(name: str) -> bool:
    try:
        return importlib.util.find_spec(name) is not None
    except (ImportError, ValueError):
        return False


def main() -> int:
    print("Rafeeq doctor — preflight for the course repo\n" + "=" * 60)

    # -- 1. Python version --------------------------------------------------
    py_ok = sys.version_info[:2] >= MIN_PYTHON
    check("Python >= 3.11", py_ok, f"found {sys.version.split()[0]}")

    # -- 2. Optional (Layer-B) dependencies ----------------------------------
    present: dict[str, bool] = {}
    print("\nOptional dependencies (Layer B, SPEC §1 — none required for Layer-A labs):")
    for mod, (pip_name, why) in OPTIONAL_DEPS.items():
        found = _has_module(mod)
        present[mod] = found
        mark = "present" if found else "absent "
        print(f"  [{mark}] {mod:<24} (pip install {pip_name}) — {why}")
    check("optional deps surveyed", True, f"{sum(present.values())}/{len(present)} present")

    # -- 3. Data files present + consistent (delegates to selfcheck) --------
    try:
        from rafeeq.core.config import (
            CUSTOMERS_SEED_PATH, ORDERS_SEED_PATH, PAYMENTS_SEED_PATH,
            DELIVERY_EVENTS_PATH, TICKETS_EVAL_PATH, ROUTING_EVAL_PATH, POLICIES_DIR,
        )
        data_files = {
            "customers_seed.json": CUSTOMERS_SEED_PATH,
            "orders_seed.json": ORDERS_SEED_PATH,
            "payments_seed.json": PAYMENTS_SEED_PATH,
            "delivery_events.jsonl": DELIVERY_EVENTS_PATH,
            "tickets_eval.jsonl": TICKETS_EVAL_PATH,
            "routing_eval.jsonl": ROUTING_EVAL_PATH,
        }
        missing = [name for name, p in data_files.items() if not p.exists()]
        check("data files generated", not missing,
              "all present" if not missing else f"missing: {missing} — run `make data`")
        check("policies/ present (en + ar)", (POLICIES_DIR / "en").exists() and (POLICIES_DIR / "ar").exists())

        if not missing:
            import subprocess

            result = subprocess.run(
                [sys.executable, str(_REPO_ROOT / "scripts" / "selfcheck.py")],
                capture_output=True, text=True, cwd=str(_REPO_ROOT),
            )
            check("scripts/selfcheck.py (data referential integrity)", result.returncode == 0,
                  "all checks passed" if result.returncode == 0 else "selfcheck reported a failure — run it directly for detail")
    except Exception as exc:  # noqa: BLE001
        check("data files generated", False, f"{type(exc).__name__}: {exc}")

    # -- 4. Runtime modes -----------------------------------------------------
    try:
        from rafeeq.core.config import get_settings

        settings = get_settings()
        print(f"\nRuntime modes (env-driven, offline-safe defaults — docs/OFFLINE_MODE.md):")
        print(f"  RAFEEQ_MODEL_MODE  = {settings.model_mode}")
        print(f"  RAFEEQ_VECTOR_MODE = {settings.vector_mode}")
        print(f"  RAFEEQ_EMBED_MODE  = {settings.embed_mode}")
        check("runtime modes readable", True, f"offline={settings.is_offline()}")

        # -- 5. Gateway reachability — ONLY when live mode is actually configured.
        if settings.model_mode == "live":
            import urllib.request

            url = settings.openai_base_url or "https://api.openai.com/v1/models"
            try:
                urllib.request.urlopen(url, timeout=3)  # noqa: S310 - deliberate, user opted into live mode
                check("model gateway reachable", True, url)
            except Exception as exc:  # noqa: BLE001
                check("model gateway reachable", False, f"{url}: {exc}")
        else:
            check("model gateway reachability", True, "skipped — RAFEEQ_MODEL_MODE is not 'live', no network call made")
    except Exception as exc:  # noqa: BLE001
        check("runtime modes readable", False, f"{type(exc).__name__}: {exc}")

    # -- 6. Docker presence (only needed for the `full` compose profile) ----
    docker_path = shutil.which("docker")
    check("Docker on PATH", docker_path is not None,
          docker_path or "not found — the `labs` compose profile and every offline Make target need no Docker at all")

    # -- 7. Verdict ------------------------------------------------------------
    offline_labs = "1, 2, 4, 7, 8, 9"
    graph_needed_labs = "5, 6 (specialist/supervisor `build_*()` graphs need `langgraph`)"
    mcp_needed_labs = "3 (real MCP server subprocesses need `mcp` + `langchain-mcp-adapters`)"
    print("\n" + "=" * 60)
    print("Verdict")
    print("=" * 60)
    print(f"You can run labs {offline_labs} fully offline right now — every task's")
    print("`verify.py` is stdlib-runnable and every start/solution module import-guards")
    print("the Layer-B graph layer (SPEC §1).")
    if not present["langgraph"]:
        print(f"Lab {graph_needed_labs} — `pip install langgraph langchain-core` first.")
    else:
        print("Labs 5, 6 — langgraph is present; their graphs will build.")
    if not (present["mcp"] and present["langchain_mcp_adapters"]):
        print(f"Lab {mcp_needed_labs} — `pip install mcp langchain-mcp-adapters` first "
              "(tool logic itself is already testable offline via `load_tools_local()`).")
    else:
        print("Lab 3 — mcp + langchain-mcp-adapters are present; real MCP servers will run.")

    return _report()


def _report() -> int:
    name_w = max(len(n) for n, _, _ in RESULTS) if RESULTS else 10
    print("\n" + "-" * 60)
    n_pass = 0
    for name, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        n_pass += int(ok)
        line = f"[{status}] {name:<{name_w}}"
        if detail:
            line += f"  ({detail})"
        print(line)
    print("-" * 60)
    print(f"{n_pass}/{len(RESULTS)} checks passed")
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
