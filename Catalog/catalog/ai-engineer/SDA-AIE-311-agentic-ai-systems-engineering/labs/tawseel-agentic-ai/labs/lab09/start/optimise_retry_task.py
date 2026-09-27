"""Lab 9, Tasks 3/4 — cut cost with caching + model routing, then add a
bounded retry that a write tool can never enter.

Fill in the TODOs. `rafeeq.observability.optimise` and `.retry` already
implement every mechanism; you are choosing WHEN to call them.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.errors import TransientToolError
from rafeeq.observability.optimise import CacheStats, cached_policy, route_model_name
from rafeeq.observability.retry import RetryLedger, call_with_retry
from rafeeq.tools.billing import issue_refund_impl
from rafeeq.tools.logistics import track_shipment_impl


def reply_model_for(intent: str | None, confidence: float) -> str:
    """TODO(lab 9.3a): return the model NAME the reply-composition span
    should use for a ticket with this (intent, confidence) — just
    `route_model_name(intent, confidence)`. Order-status/track intents at
    high confidence should come back cheap; everything else, frontier."""
    raise NotImplementedError("TODO(lab 9.3a): implement reply_model_for")


def cached_policy_lookup(question: str, locale: str, stats: CacheStats) -> str:
    """TODO(lab 9.3b): return `cached_policy(question, locale, stats=stats)`
    — the scoped, versioned cache (question, locale, policy_version). Pass
    the SAME `stats` object across a whole ticket batch so its hit_rate
    reflects the batch, not just one call."""
    raise NotImplementedError("TODO(lab 9.3b): implement cached_policy_lookup")


def make_flaky(fn, fail_times: int = 1):
    """Test double: wraps `fn` so it raises `TransientToolError` on its
    first `fail_times` call(s), then delegates normally. Already
    implemented — used by Task 4, not something you need to fill in."""
    calls = {"n": 0}

    def wrapped(*args: Any, **kwargs: Any) -> Any:
        calls["n"] += 1
        if calls["n"] <= fail_times:
            raise TransientToolError(f"simulated transient failure #{calls['n']}")
        return fn(*args, **kwargs)

    wrapped.calls = calls
    return wrapped


def retry_read_tool_once_flaky(order_id: str, ledger: RetryLedger) -> dict:
    """TODO(lab 9.4a): `track_shipment` is in `IDEMPOTENT` (a read). Wrap
    `track_shipment_impl` with `make_flaky(track_shipment_impl,
    fail_times=1)` and call it through `call_with_retry("track_shipment",
    flaky_fn, order_id, ledger=ledger, sleep=lambda s: None)` (inject a
    no-op sleep so the lab does not actually wait on backoff). Return the
    result — it should SUCCEED (the retry covers the one flaky attempt)."""
    raise NotImplementedError("TODO(lab 9.4a): implement retry_read_tool_once_flaky")


def call_write_tool_never_retried(order_id: str, amount_sar: float, ledger: RetryLedger) -> dict:
    """TODO(lab 9.4b): `issue_refund` is NOT in `IDEMPOTENT` — call it
    through `call_with_retry("issue_refund", issue_refund_impl, order_id,
    amount_sar, "lab9_retry_task", "lab9-retry-demo-key", ledger=ledger)`
    exactly once. After this call, `ledger.retry_count("issue_refund")`
    MUST be 0 — that is the safety property Task 4 proves, not a
    coincidence of this specific call."""
    raise NotImplementedError("TODO(lab 9.4b): implement call_write_tool_never_retried")
