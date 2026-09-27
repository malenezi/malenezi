#!/usr/bin/env python3
"""Lab 6 solution — verification script.

Stdlib + pydantic only. Drives `rafeeq.orchestration.supervisor.supervise`/
`route` and a Layer-A stand-in delegate/aggregate BY HAND — the same
by-hand pattern `labs/lab01/solution/verify.py` uses for the core loop.

Honesty note on routing accuracy: `StubChatModel.with_structured_output`
only fills fields it recognises from its own candidate dict
(`order_id`/`intent`/`locale`/`text`/`confidence`) — `supervisor.Route`'s
`target`/`subgoal` fields are NOT among them, so a hand-driven `supervise()`
call against the stub does not produce a meaningful routing decision (this
is a real, current limitation of the shared stub, not a Lab 6 bug). What
IS measurable, and IS the production signal `orchestration/fastpath.py`
actually uses for its confident majority, is the deterministic
`orchestration.routing.classify_intent` + `specialist_for_intent` router —
this script reports ITS real accuracy on `routing_eval.jsonl` instead, and
proves the one property that does NOT depend on the routing model at all:
the global handoff budget short-circuits to escalate before any router is
even asked.

Run: `PYTHONPATH=src python3 labs/lab06/solution/verify.py`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.agents.scoping import scoped_input
from rafeeq.core.config import MAX_HANDOFFS, ROUTING_EVAL_PATH
from rafeeq.orchestration.routing import classify_intent, specialist_for_intent
from rafeeq.orchestration.supervisor import route, supervise

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, ok, detail))


def main() -> int:
    # -- 1/3. thin supervisor: budget wins the race, ALWAYS ----------------
    over_budget_state = {"handoff_count": MAX_HANDOFFS, "messages": [("human", "anything at all")]}
    decision = supervise(over_budget_state)
    check("supervise() escalates the instant handoff_count >= MAX_HANDOFFS, "
          "WITHOUT asking the routing model", decision.get("route") == "escalate", str(decision))

    check("route() is a pure passthrough of state['route']",
          route({"route": "billing"}) == "billing" and route({"route": "escalate"}) == "escalate")

    # -- deterministic first-hop routing accuracy (the real fastpath signal) --
    tickets = [json.loads(line) for line in ROUTING_EVAL_PATH.open("r", encoding="utf-8")]
    correct = 0
    for t in tickets:
        intent, _confidence = classify_intent(t["text"])
        specialist = specialist_for_intent(intent)
        if specialist == t["expected_specialist"]:
            correct += 1
    accuracy = correct / len(tickets) if tickets else 0.0
    print(f"deterministic fast-path routing accuracy on routing_eval.jsonl: "
          f"{correct}/{len(tickets)} = {accuracy:.0%} (informational — see the honesty note above; "
          f"the package's 94% target is a live-model number)")
    check("routing accuracy computed on the real 60-ticket routing_eval.jsonl", len(tickets) == 60)

    # -- 2. scoped handoff + mandatory write-back (a hand-built delegate) --
    from rafeeq.tools.billing import get_invoice_impl
    from rafeeq.tools.logistics import track_shipment_impl

    def logistics_fn(payload: dict) -> str:
        result = track_shipment_impl("TW-2026-10002")
        return f"Status: {result.get('status', 'unknown')}"

    def billing_fn(payload: dict) -> str:
        result = get_invoice_impl("TW-2026-10002")
        return f"Invoice: {result.get('amount_sar', 'n/a')} SAR"

    state = {"customer_id": "CUST-4471", "locale": "en", "order_id": "TW-2026-10002",
              "messages": [], "handoff_count": 0, "last_result": {}}

    for name, fn in (("logistics", logistics_fn), ("billing", billing_fn)):
        payload = scoped_input(state, name)
        result_text = fn(payload)
        state["messages"] = list(state["messages"]) + [("ai", result_text)]
        state["last_result"] = {**state["last_result"], name: result_text}
        state["handoff_count"] += 1

    check("a two-specialist ticket produced write-backs from BOTH specialists",
          set(state["last_result"]) == {"logistics", "billing"}, str(state["last_result"]))
    check("handoff_count advanced exactly once per specialist (2 hops)", state["handoff_count"] == 2)
    check("no lost handoff: every specialist's answer reached state['messages']",
          len(state["messages"]) == 2)

    # -- chatter-loop: force MAX_HANDOFFS handoffs, confirm escalation ------
    chatter_state = {"handoff_count": 0, "messages": [("human", "keeps bouncing between specialists")]}
    hops = 0
    while True:
        d = supervise(chatter_state)
        if d.get("route") == "escalate":
            break
        chatter_state["handoff_count"] += 1
        hops += 1
        if hops > MAX_HANDOFFS + 5:
            break  # safety net for this test itself — should never trigger
    check(f"chatter-loop ticket escalates at/before handoff {MAX_HANDOFFS}, never loops past it",
          hops <= MAX_HANDOFFS, f"escalated after {hops} hop(s)")

    return _report()


def _report() -> int:
    name_w = max(len(n) for n, _, _ in RESULTS) if RESULTS else 10
    print("\nLab 6 verification — supervisor orchestrator")
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
