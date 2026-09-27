#!/usr/bin/env python3
"""Module 1/3 — Layer-A self-check.

Stdlib-only. Imports every Layer-A module, loads the generated data, and
asserts referential integrity end to end: every order's customer exists,
every payment's order exists, every eval ticket's order exists and its
`expected` block matches the ACTUAL seed state (not just "is well-formed").
Run this after `python3 data/generate.py` and before trusting the data for
labs, the eval harness, or TawseelBench.

Usage: `python3 scripts/selfcheck.py` (from anywhere; paths are resolved
via `rafeeq.core.config`).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(condition), detail))


def main() -> int:
    # -- 1. import every Layer-A module -----------------------------------
    try:
        from rafeeq.core import budget, config, embeddings, errors, llm, state  # noqa: F401
        from rafeeq.adapters import billing, crm, logistics, oms, store as store_mod  # noqa: F401
        from rafeeq.memory import vector_store  # noqa: F401
        check("import: core.config", True)
        check("import: core.state", True)
        check("import: core.llm", True)
        check("import: core.embeddings", True)
        check("import: core.budget", True)
        check("import: core.errors", True)
        check("import: adapters.store/oms/logistics/crm/billing", True)
        check("import: memory.vector_store", True)
    except Exception as exc:  # noqa: BLE001 - report, don't crash the report
        check("import: Layer-A modules", False, f"{type(exc).__name__}: {exc}")
        _report()
        return 1

    from rafeeq.core.config import (
        AUTO_REFUND_LIMIT_SAR, REFUND_LIMIT_SAR,
        CUSTOMERS_SEED_PATH, ORDERS_SEED_PATH, PAYMENTS_SEED_PATH,
        DELIVERY_EVENTS_PATH, TICKETS_EVAL_PATH, ROUTING_EVAL_PATH,
    )

    # -- 2. load data straight from disk (independent of the store's own
    #    loader, so this genuinely checks the FILES, not the adapter code) --
    def load_json(path: Path) -> list[dict]:
        if not path.exists():
            return []
        return json.loads(path.read_text(encoding="utf-8"))

    def load_jsonl(path: Path) -> list[dict]:
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

    customers = load_json(CUSTOMERS_SEED_PATH)
    orders = load_json(ORDERS_SEED_PATH)
    payments = load_json(PAYMENTS_SEED_PATH)
    events = load_jsonl(DELIVERY_EVENTS_PATH)
    tickets = load_jsonl(TICKETS_EVAL_PATH)
    routing = load_jsonl(ROUTING_EVAL_PATH)

    check("data files present", all([customers, orders, payments, events, tickets, routing]),
          f"customers={len(customers)} orders={len(orders)} payments={len(payments)} "
          f"events={len(events)} tickets={len(tickets)} routing={len(routing)}")

    customer_ids = {c["customer_id"] for c in customers}
    order_ids = {o["order_id"] for o in orders}
    orders_by_id = {o["order_id"]: o for o in orders}

    # -- 3. referential integrity -------------------------------------------
    orphan_orders = [o["order_id"] for o in orders if o["customer_id"] not in customer_ids]
    check("every order's customer exists", not orphan_orders, f"{len(orphan_orders)} orphaned orders")

    orphan_payments = [p["payment_id"] for p in payments if p["order_id"] not in order_ids]
    check("every payment's order exists", not orphan_payments, f"{len(orphan_payments)} orphaned payments")

    n_payments_per_order: dict[str, int] = {}
    for p in payments:
        n_payments_per_order[p["order_id"]] = n_payments_per_order.get(p["order_id"], 0) + 1
    multi_payment_orders = [oid for oid, n in n_payments_per_order.items() if n != 1]
    check("exactly one payment per order", not multi_payment_orders, f"{len(multi_payment_orders)} orders without exactly 1 payment")

    orphan_events = {e["order_id"] for e in events if e["order_id"] not in order_ids}
    check("every delivery event's order exists", not orphan_events, f"{len(orphan_events)} orphaned event order_ids")

    orphan_ticket_orders = [t["ticket_id"] for t in tickets if t.get("order_id") and t["order_id"] not in order_ids]
    check("every eval ticket's order exists (when set)", not orphan_ticket_orders,
          f"{len(orphan_ticket_orders)} tickets reference a missing order")

    orphan_routing_orders = [t["ticket_id"] for t in routing if t.get("order_id") and t["order_id"] not in order_ids]
    check("every routing ticket's order exists", not orphan_routing_orders,
          f"{len(orphan_routing_orders)} routing tickets reference a missing order")

    # -- 4. eval ticket `expected` must be TRUE of the seed state -----------
    bad_refund_tickets = []
    bad_reschedule_tickets = []
    bad_specialist_tickets = []
    for t in tickets:
        order = orders_by_id.get(t.get("order_id"))
        expected = t.get("expected", {})
        intent = t.get("intent")

        if intent == "refund" and order is not None:
            amount = order["amount_sar"]
            expected_resolution = "escalated" if amount > REFUND_LIMIT_SAR else "resolved"
            if expected["resolution"] != expected_resolution:
                bad_refund_tickets.append(t["ticket_id"])

        if intent == "reschedule" and order is not None:
            reschedulable = order["status"] not in ("delivered", "exception")
            if reschedulable and expected["resolution"] != "resolved":
                bad_reschedule_tickets.append(t["ticket_id"])
            if not reschedulable and expected["resolution"] != "escalated":
                bad_reschedule_tickets.append(t["ticket_id"])

        if intent in ("order_status", "track") and expected.get("specialist") != "logistics":
            bad_specialist_tickets.append(t["ticket_id"])
        if intent == "refund" and expected.get("specialist") != "billing":
            bad_specialist_tickets.append(t["ticket_id"])

        if order is not None and expected.get("must_mention") and order["order_id"] not in expected["must_mention"]:
            if t.get("order_id") == order["order_id"]:
                bad_specialist_tickets.append(t["ticket_id"])  # order_id should be mentionable

    check("refund tickets: expected.resolution matches order amount vs REFUND_LIMIT_SAR",
          not bad_refund_tickets, f"mismatches: {bad_refund_tickets[:10]}")
    check("reschedule tickets: expected.resolution matches order status reschedulability",
          not bad_reschedule_tickets, f"mismatches: {bad_reschedule_tickets[:10]}")
    check("intent -> specialist mapping is internally consistent",
          not bad_specialist_tickets, f"mismatches: {bad_specialist_tickets[:10]}")

    # -- 5. policy constants sanity ------------------------------------------
    check("AUTO_REFUND_LIMIT_SAR < REFUND_LIMIT_SAR", AUTO_REFUND_LIMIT_SAR < REFUND_LIMIT_SAR,
          f"{AUTO_REFUND_LIMIT_SAR} vs {REFUND_LIMIT_SAR}")

    # -- 6. policy documents ----------------------------------------------
    from rafeeq.core.config import POLICIES_DIR, POLICIES_SUPERSEDED_DIR
    policy_names = [
        "refund_eligibility", "delivery_sla", "rescheduling",
        "lost_or_damaged", "data_privacy_pdpl", "escalation",
    ]
    missing_policies = []
    for name in policy_names:
        for locale in ("en", "ar"):
            p = POLICIES_DIR / locale / f"{name}.md"
            if not p.exists():
                missing_policies.append(str(p))
    check("all 6 policies present in en/ and ar/", not missing_policies, f"missing: {missing_policies}")

    superseded_missing = [
        str(POLICIES_SUPERSEDED_DIR / loc / "refund_eligibility.md")
        for loc in ("en", "ar")
        if not (POLICIES_SUPERSEDED_DIR / loc / "refund_eligibility.md").exists()
    ]
    check("superseded refund_eligibility (2026.1) present in en/ and ar/",
          not superseded_missing, f"missing: {superseded_missing}")

    if not superseded_missing:
        superseded_text = (POLICIES_SUPERSEDED_DIR / "en" / "refund_eligibility.md").read_text(encoding="utf-8")
        current_text = (POLICIES_DIR / "en" / "refund_eligibility.md").read_text(encoding="utf-8")
        check("superseded policy states a DIFFERENT threshold (300 SAR) than current (500 SAR)",
              "300 SAR" in superseded_text and "500 SAR" in current_text and "300 SAR" not in current_text)

    # -- 7. adapters + vector store smoke test (via the actual store) -------
    try:
        store_mod.store.reset()
        counts = store_mod.store.counts()
        check("adapters.store loads and counts match files",
              counts["customers"] == len(customers) and counts["orders"] == len(orders),
              f"store counts: {counts}")

        from rafeeq.adapters.billing import BillingClient
        bill = BillingClient()
        sample_order = next(o for o in orders if not o["refunded"] and o["amount_sar"] < AUTO_REFUND_LIMIT_SAR)
        r1 = bill.issue_refund(sample_order["order_id"], sample_order["amount_sar"], "selfcheck", "selfcheck-key-1")
        r2 = bill.issue_refund(sample_order["order_id"], sample_order["amount_sar"], "selfcheck", "selfcheck-key-1")
        check("billing.issue_refund is idempotent by key", r2["idempotent_replay"] is True and r1["amount_sar"] == r2["amount_sar"])
        store_mod.store.reset()

        from rafeeq.memory.vector_store import Document, SimpleVectorStore
        vs = SimpleVectorStore("selfcheck")
        vs.add_documents([
            Document("refund policy note for a customer", {"customer_id": "A"}),
            Document("سياسة استرداد لعميل آخر", {"customer_id": "B"}),
        ])
        scoped = vs.similarity_search("refund", k=5, filter={"customer_id": "A"})
        check("SimpleVectorStore filters before ranking (no cross-customer leakage)",
              all(d.metadata["customer_id"] == "A" for d in scoped))
    except Exception as exc:  # noqa: BLE001
        check("adapters + vector store smoke test", False, f"{type(exc).__name__}: {exc}")

    return _report()


def _report() -> int:
    name_w = max(len(n) for n, _, _ in RESULTS) if RESULTS else 10
    print("\nRafeeq Layer-A self-check")
    print("=" * (name_w + 20))
    n_pass = 0
    for name, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        n_pass += int(ok)
        line = f"[{status}] {name:<{name_w}}"
        if detail:
            line += f"  ({detail})"
        print(line)
    print("=" * (name_w + 20))
    print(f"{n_pass}/{len(RESULTS)} checks passed")
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
