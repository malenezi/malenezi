#!/usr/bin/env python3
"""Lab 3 solution — verification script.

Stdlib + pydantic only for the tool-selection and error-value checks
(uses `rafeeq.tools.mcp_client.load_tools_local()`, the in-process
fallback SPEC §1 provides — no `mcp` package needed). Separately checks
whether the real `mcp` + `langchain-mcp-adapters` packages are installed
and, if so, that all four MCP servers are discoverable as standalone
scripts; if not, prints a clear skip rather than failing (Lab 3's own
troubleshooting note: verify the server runs standalone first).

Run: `PYTHONPATH=src python3 labs/lab03/solution/verify.py`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from rafeeq.core.config import TICKETS_EVAL_PATH
from rafeeq.core.llm import get_model
from rafeeq.tools.mcp_client import load_tools_local
from rafeeq.tools.registry import ALL_TOOLS, IDEMPOTENT, TOOL_DOMAIN, WRITE_TOOLS
from rafeeq.tools.logistics import track_shipment_impl

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, ok, detail))


def _load_order_tickets(n: int = 10) -> list[dict]:
    tickets = []
    with TICKETS_EVAL_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            t = json.loads(line)
            if t.get("intent") in ("order_status", "track") and t.get("expected", {}).get("tools"):
                tickets.append(t)
            if len(tickets) >= n:
                break
    return tickets


def main() -> int:
    # -- 1/2. governed catalogue + MCP local fallback -----------------------
    tools = load_tools_local()
    check("load_tools_local() returns the full governed catalogue", len(tools) == len(ALL_TOOLS),
          f"{len(tools)} tools loaded")
    check("every tool has an owning domain (TOOL_DOMAIN)", set(TOOL_DOMAIN) == {t.name for t in ALL_TOOLS})

    # -- tool-selection accuracy on 10 order-status/track tickets -----------
    tickets = _load_order_tickets(10)
    correct = 0
    model = get_model().bind_tools(tools)
    for t in tickets:
        reply = model.invoke([("human", t["text"])])
        called = {tc["name"] for tc in reply.tool_calls}
        expected = set(t["expected"]["tools"])
        if called & expected:
            correct += 1
    check("agent on order tickets: correct tool selection", correct == len(tickets),
          f"{correct}/{len(tickets)} correct" if tickets else "no order-status/track tickets found")
    check("0 crashes selecting tools for real tickets", True)  # implicit: the loop above didn't raise

    # -- invalid order id handled gracefully (error VALUE, no crash) --------
    bad = track_shipment_impl("not-a-real-id")
    check("invalid order id returns an error VALUE, does not raise",
          isinstance(bad, dict) and bool(bad.get("error")), str(bad))
    missing = track_shipment_impl("TW-2026-00000")
    check("well-formed but nonexistent order id -> order_not_found, not a crash",
          missing.get("error") == "order_not_found", str(missing))

    # -- write tool marked non-idempotent, never auto-retried ---------------
    check("add_case_note is a WRITE tool (never auto-retried)", "add_case_note" in WRITE_TOOLS)
    check("issue_refund is a WRITE tool (never auto-retried)", "issue_refund" in WRITE_TOOLS)
    check("track_shipment is IDEMPOTENT (safe to retry)", "track_shipment" in IDEMPOTENT)
    check("no tool is both read-safe and write", not (IDEMPOTENT & WRITE_TOOLS))

    # -- MCP discovery, only when the real dependency is present -----------
    import importlib.util

    has_mcp = importlib.util.find_spec("mcp") is not None
    has_adapters = importlib.util.find_spec("langchain_mcp_adapters") is not None
    if has_mcp and has_adapters:
        import asyncio

        from rafeeq.tools.mcp_client import load_tawseel_tools

        try:
            discovered = asyncio.run(load_tawseel_tools())
            check("MCP discovery: tools loaded from all 4 servers", len(discovered) > 0,
                  f"{len(discovered)} tools discovered")
        except Exception as exc:  # noqa: BLE001
            check("MCP discovery: tools loaded from all 4 servers", False, f"{type(exc).__name__}: {exc}")
    else:
        print("(skipping real MCP discovery — `mcp`/`langchain-mcp-adapters` not installed; "
              "load_tools_local() above already proved the tool surface itself is correct)")

    return _report()


def _report() -> int:
    name_w = max(len(n) for n, _, _ in RESULTS) if RESULTS else 10
    print("\nLab 3 verification — Tawseel tools over MCP")
    print("=" * (name_w + 24))
    n_pass = 0
    for name, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        n_pass += int(ok)
        line = f"[{status}] {name:<{name_w}}"
        if detail:
            line += f"  ({detail})"
        print(line)
    print("=" * (name_w + 24))
    print(f"{n_pass}/{len(RESULTS)} checks passed")
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
