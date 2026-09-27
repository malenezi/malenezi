"""Lab 9 solution — Tasks 3b/4 glue, filled in (mirrors
`start/optimise_retry_task.py`'s TODOs, not a copy-paste of it: this is
the completed version `solution/verify.py` actually imports and runs)."""
from __future__ import annotations

from typing import Any

from rafeeq.core.errors import TransientToolError
from rafeeq.observability.optimise import CacheStats, cached_policy, route_model_name
from rafeeq.observability.retry import RetryLedger, call_with_retry
from rafeeq.tools.billing import issue_refund_impl
from rafeeq.tools.logistics import track_shipment_impl


def reply_model_for(intent: str | None, confidence: float) -> str:
    return route_model_name(intent, confidence)


def cached_policy_lookup(question: str, locale: str, stats: CacheStats) -> str:
    return cached_policy(question, locale, stats=stats)


def make_flaky(fn, fail_times: int = 1):
    calls = {"n": 0}

    def wrapped(*args: Any, **kwargs: Any) -> Any:
        calls["n"] += 1
        if calls["n"] <= fail_times:
            raise TransientToolError(f"simulated transient failure #{calls['n']}")
        return fn(*args, **kwargs)

    wrapped.calls = calls
    return wrapped


def retry_read_tool_once_flaky(order_id: str, ledger: RetryLedger) -> dict:
    flaky = make_flaky(track_shipment_impl, fail_times=1)
    return call_with_retry("track_shipment", flaky, order_id, ledger=ledger, sleep=lambda s: None)


def call_write_tool_never_retried(order_id: str, amount_sar: float, ledger: RetryLedger) -> dict:
    return call_with_retry(
        "issue_refund", issue_refund_impl, order_id, amount_sar,
        "lab9_retry_task", "lab9-retry-demo-key", ledger=ledger,
    )


def call_write_tool_that_would_fail(order_id: str, ledger: RetryLedger) -> None:
    """Task 4's counter-proof: even a WRITE call that FAILS is attempted
    exactly once, never retried — the flaky wrapper here always raises,
    and `call_with_retry` for a non-idempotent tool has no retry branch
    to catch it in the first place."""
    flaky_refund = make_flaky(issue_refund_impl, fail_times=99)  # always fails
    call_with_retry(
        "issue_refund", flaky_refund, order_id, 20.0, "lab9_retry_fail_demo",
        "lab9-retry-fail-demo-key", ledger=ledger,
    )
