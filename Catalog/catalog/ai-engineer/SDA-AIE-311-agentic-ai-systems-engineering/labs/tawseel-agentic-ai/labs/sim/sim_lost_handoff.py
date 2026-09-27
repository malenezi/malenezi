#!/usr/bin/env python3
"""sim_lost_handoff — Module 6, `labs/lab06`.

Symptom:    A specialist runs, produces a correct result, and the
            customer still gets an empty answer.
Root cause: The delegate node invokes the specialist but never writes
            its result back into shared state before control returns to
            the supervisor — the specialist's work is discarded.
Fix:        Every delegation MUST write the specialist's result back
            into state (`last_result`, and a message) before the
            supervisor is asked to decide again —
            `rafeeq.orchestration.delegate.make_delegate`'s real
            contract (Module 6 §3), reproduced here without needing
            `langgraph` since the real closure is Layer B.

Run: `PYTHONPATH=src python3 labs/sim/sim_lost_handoff.py`
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Callable

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.tools.logistics import track_shipment_impl

ORDER_ID = "TW-2026-16382"


def broken_delegate(specialist_fn: Callable[[dict], Any], state: dict) -> dict:
    """THE ANTI-PATTERN: calls the specialist, discards the result."""
    specialist_fn({"order_id": state["order_id"]})  # ran — result thrown away
    return {}  # nothing written back: `last_result` and `messages` untouched


def fixed_delegate(specialist_fn: Callable[[dict], Any], state: dict) -> dict:
    """THE FIX: the specialist's result is ALWAYS written back — the
    mandatory write-back contract `delegate.py`'s docstring names."""
    result = specialist_fn({"order_id": state["order_id"]})
    reply = f"Order {state['order_id']}: {result.get('status', 'unknown')}."
    return {"last_result": result, "messages": [("ai", reply)]}


def main() -> int:
    specialist_fn = lambda payload: track_shipment_impl(payload["order_id"])  # noqa: E731

    state = {"order_id": ORDER_ID, "last_result": None, "messages": []}

    print("-- broken: delegate discards the specialist's result --")
    update = broken_delegate(specialist_fn, state)
    customer_got_empty_answer = not update.get("messages") and update.get("last_result") is None
    print(f"  write-back: {update}")
    print(f"  the specialist RAN (real track_shipment_impl call happened) but the "
          f"customer gets nothing back: {customer_got_empty_answer}\n")

    print("-- fixed: delegate writes the result back --")
    update = fixed_delegate(specialist_fn, state)
    customer_got_answer = bool(update.get("messages")) and update.get("last_result") is not None
    print(f"  write-back: {update}")
    print(f"  the customer now gets a real answer: {customer_got_answer}\n")

    ok = customer_got_empty_answer and customer_got_answer
    print("FAILURE DEMONSTRATED (lost handoff) AND FIX PROVEN (write-back contract)" if ok
          else "DEMO DID NOT REPRODUCE THE EXPECTED CONTRAST (unexpected)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
