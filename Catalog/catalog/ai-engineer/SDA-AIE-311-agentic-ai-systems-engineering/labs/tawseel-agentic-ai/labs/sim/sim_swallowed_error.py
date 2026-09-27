#!/usr/bin/env python3
"""sim_swallowed_error — Module 1 (errors are values) / Module 7 (flow
gates need populated state), `labs/lab01` and `labs/lab07`.

Symptom:    A refund flow silently "approves" a refund for an order that
            could not even be loaded.
Root cause: An order-lookup failure is swallowed and defaulted instead of
            failed closed — `amount = 0.0` on error looks, to every
            downstream gate, exactly like "a legitimate order worth
            nothing", which routes to `auto_approve` instead of refusing.
Fix:        `rafeeq.flows.refund_flow.load_order` fails CLOSED: on error
            it sets `amount: None` (never `0.0`) and carries
            `order_error` in state, so `amount_gate` reading `state.get(
            "amount") or 0.0` still lands on the auto-approve band ONLY
            if a caller ignores `order_error` first — the real fix is
            `eligibility_gate`/the caller checking `order_error` before
            any amount gate runs at all, exactly what
            `labs/lab07/start/refund_flow_task.py` asks you to wire.

Run: `PYTHONPATH=src python3 labs/sim/sim_swallowed_error.py`
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Literal

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import AUTO_REFUND_LIMIT_SAR
from rafeeq.flows.refund_flow import amount_gate, load_order
from rafeeq.tools.orders import get_order_impl

UNKNOWN_ORDER = "TW-2026-99999"  # well-formed id, does not exist


def broken_load_order(state: dict) -> dict:
    """THE ANTI-PATTERN: on a lookup failure, silently default `amount`
    to 0.0 instead of `None` and drop `order_error` entirely — "no order"
    becomes indistinguishable from "an order worth nothing"."""
    order = get_order_impl(state["order_id"])
    if order.get("error"):
        return {"amount": 0.0, "sla_breached": False, "already_refunded": False}  # swallowed!
    return {"amount": order["amount_sar"], "sla_breached": order["sla_breached"],
            "already_refunded": order["refunded"]}


def main() -> int:
    print(f"-- broken: load_order silently defaults amount=0.0 on a lookup failure "
          f"--  order={UNKNOWN_ORDER!r} (does not exist)")
    broken_state = broken_load_order({"order_id": UNKNOWN_ORDER})
    print(f"  state after broken load_order: {broken_state}")
    broken_decision = amount_gate(broken_state)
    wrongly_approved = broken_decision == "auto_approve"
    print(f"  amount_gate({{'amount': 0.0}}) -> {broken_decision!r} — an order that "
          f"DOES NOT EXIST routes to the FULLY AUTONOMOUS band "
          f"(<= {AUTO_REFUND_LIMIT_SAR} SAR): {wrongly_approved}\n")

    print("-- fixed: the real load_order fails closed --")
    fixed_state = load_order({"order_id": UNKNOWN_ORDER})
    print(f"  state after the real load_order: {fixed_state}")
    error_is_visible = fixed_state.get("order_error") is not None and fixed_state.get("amount") is None
    print(f"  order_error is carried in state and amount is None (never a fake 0.0): "
          f"{error_is_visible}")
    print("  a caller checking order_error BEFORE any amount gate — exactly what "
          "labs/lab07 wires — refuses to proceed at all, instead of silently approving.\n")

    ok = wrongly_approved and error_is_visible
    print("FAILURE DEMONSTRATED (swallowed error auto-approves) AND FIX PROVEN "
          "(fails closed, error stays visible)" if ok
          else "DEMO DID NOT REPRODUCE THE EXPECTED CONTRAST (unexpected)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
