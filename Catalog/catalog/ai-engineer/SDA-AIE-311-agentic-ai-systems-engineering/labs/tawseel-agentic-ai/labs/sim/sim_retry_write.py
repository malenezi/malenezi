#!/usr/bin/env python3
"""sim_retry_write — Module 9, `labs/lab09`.

Symptom:    A timeout on `issue_refund` triggers a SECOND, real refund —
            the customer is paid twice.
Root cause: A naive retry wrapper retries ANY tool on failure, including
            writes, without checking whether the tool is idempotent-safe
            to retry. Worse: retrying with a FRESH idempotency key each
            attempt (a common real mistake) defeats even the tool's own
            replay protection.
Fix:        `rafeeq.observability.retry.call_with_retry` reads
            `rafeeq.tools.registry.IDEMPOTENT` and has NO retry branch at
            all for a write tool — it is called exactly once, whatever
            it raises propagates immediately. Not an optimisation: the
            branch that would retry a write does not exist in its
            control flow for that tool_name.

Run: `PYTHONPATH=src python3 labs/sim/sim_retry_write.py`
"""
from __future__ import annotations

import sys
import uuid
from pathlib import Path
from typing import Any, Callable

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.errors import TransientToolError
from rafeeq.observability.retry import RetryLedger, call_with_retry
from rafeeq.tools.billing import get_payment_impl, issue_refund_impl

ORDER_ID = "TW-2026-23560"
ORDER_ID_2 = "TW-2026-16382"  # real seeded order with enough refundable balance
AMOUNT_SAR = 50.0  # inside AUTO_REFUND_LIMIT_SAR, so nothing else blocks it


def naive_retry(fn: Callable[..., Any], *args: Any, retries: int = 2) -> Any:
    """THE ANTI-PATTERN: retries ANY exception, on ANY tool, generating a
    FRESH idempotency key each attempt (the mistake that defeats even
    `issue_refund_impl`'s own replay protection)."""
    last_exc: Exception | None = None
    for _ in range(retries + 1):
        try:
            return fn(*args, uuid.uuid4().hex)  # a NEW idempotency key every attempt
        except TransientToolError as exc:  # noqa: BLE001 - deliberately broad, this IS the bug
            last_exc = exc
            continue
    raise last_exc  # type: ignore[misc]


def flaky_issue_refund(order_id: str, amount_sar: float, reason: str, idempotency_key: str) -> dict:
    """Simulates a network timeout AFTER the write already landed on the
    backend — the real-world scenario that makes naive retry dangerous:
    the caller sees an exception and assumes nothing happened. Stashes
    every underlying result on `.last_result` (demo-only introspection —
    the "gateway" this stands in for would not normally expose that to a
    caller that just saw it time out)."""
    result = issue_refund_impl(order_id, amount_sar, reason, idempotency_key)
    flaky_issue_refund.last_result = result  # type: ignore[attr-defined]
    if flaky_issue_refund.calls == 0:  # type: ignore[attr-defined]
        flaky_issue_refund.calls += 1  # type: ignore[attr-defined]
        raise TransientToolError("simulated timeout waiting for the gateway's ack")
    return result


def main() -> int:
    print(f"-- broken: naive_retry(flaky_issue_refund) on order {ORDER_ID} --")
    flaky_issue_refund.calls = 0  # type: ignore[attr-defined]
    naive_result = naive_retry(flaky_issue_refund, ORDER_ID, AMOUNT_SAR, "sim_retry_write_demo")
    total_after_naive = naive_result.get("total_refunded_sar", 0.0)
    double_refund = total_after_naive >= (2 * AMOUNT_SAR) - 0.01
    print(f"  final call's total_refunded_sar on this order: {total_after_naive} SAR "
          f"(one request for {AMOUNT_SAR} SAR)")
    print(f"  the customer was refunded TWICE (naive retry re-sent the write with a FRESH "
          f"idempotency key after a 'failure' that had already succeeded): {double_refund}\n")

    print("-- fixed: the SAME flaky call through call_with_retry --")
    ledger = RetryLedger()
    flaky_issue_refund.calls = 0  # type: ignore[attr-defined]
    raised = False
    try:
        call_with_retry("issue_refund", flaky_issue_refund, ORDER_ID_2, AMOUNT_SAR,
                         "sim_retry_write_fixed_demo", "sim-retry-write-fixed-key", ledger=ledger)
    except TransientToolError:
        raised = True  # the write tool's own exception propagates — no silent retry
    payment_id = flaky_issue_refund.last_result["payment_id"]  # type: ignore[attr-defined]
    payment = get_payment_impl(payment_id)
    refunds_on_this_key = [r for r in payment["refunds"] if r.get("idempotency_key") == "sim-retry-write-fixed-key"]
    single_refund = len(refunds_on_this_key) == 1
    never_retried = ledger.retry_count("issue_refund") == 0
    print(f"  refunds recorded under this ONE idempotency key: {len(refunds_on_this_key)}")
    print(f"  exception propagated instead of being silently retried: {raised}")
    print(f"  issue_refund retried 0 times: {never_retried} ({ledger.summary()})")
    print(f"  refunded exactly once, even though the caller 'saw' a failure: {single_refund}\n")

    ok = double_refund and raised and never_retried and single_refund
    print("FAILURE DEMONSTRATED (double refund) AND FIX PROVEN (write tool never retried)" if ok
          else "DEMO DID NOT REPRODUCE THE EXPECTED CONTRAST (unexpected)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
