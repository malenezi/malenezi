"""Module 1/8 — Rafeeq error types.

TEACHING POINT: errors are RETURN VALUES, not just exceptions to catch and
discard. A tool or node that swallows an error and continues on a stale or
empty observation is the "swallowed tool error" anti-pattern from Module 1
(mistake #5) — it lets the loop confidently produce a wrong answer instead
of surfacing the failure into state where a router can act on it. The
exception classes below exist for genuine control flow (raise, catch,
abort); `as_error_value` exists so a tool can instead *return* a small,
serialisable error object that flows through state like any other
observation and gets logged, retried, or shown to the customer.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class RafeeqError(Exception):
    """Base class for every Rafeeq-specific error. Never raise bare
    Exception in this codebase — callers pattern-match on subclasses."""

    code: str = "rafeeq_error"

    def __init__(self, message: str, **detail: Any) -> None:
        super().__init__(message)
        self.message = message
        self.detail = detail

    def to_dict(self) -> dict[str, Any]:
        return as_error_value(self.code, message=self.message, **self.detail)


class TransientToolError(RafeeqError):
    """A tool failed in a way that is plausibly retryable (timeout, rate
    limit, flaky backend). Callers should retry with backoff (M9) before
    giving up — retrying is safe because the underlying action did not
    necessarily take effect."""

    code = "transient_tool_error"


class ToolError(RafeeqError):
    """A tool failed in a way that is NOT retryable (bad input, not found,
    business-rule violation). Retrying will not help; surface it to the
    caller/customer instead."""

    code = "tool_error"


class BudgetExceeded(RafeeqError):
    """Raised by RunBudget when a step / cost / wall-clock ceiling is hit.
    This is the Module 1 "bounded by construction" contract made concrete:
    a run MUST escalate, not silently keep looping, when this fires."""

    code = "budget_exceeded"


class NotAuthorised(RafeeqError):
    """Raised by security/authz checks (M8) when an action is outside the
    caller's permission boundary — e.g. an autonomous refund above the
    human-approval threshold, or a prohibited action from the action-risk
    matrix (change_customer_identity, override_fraud_flag, delete_order)."""

    code = "not_authorised"


def as_error_value(code: str, **detail: Any) -> dict[str, Any]:
    """Build a small, JSON-serialisable error object suitable for returning
    from a tool call or node instead of raising. Every field is stable and
    cheap to log; `ts` makes errors orderable in a trace without needing a
    tracing backend (M9 wires the real thing; this keeps Layer A usable
    stand-alone).

    Usage:
        return as_error_value("order_not_found", order_id=order_id)
    """
    return {
        "error": True,
        "code": code,
        "ts": datetime.now(timezone.utc).isoformat(),
        "detail": detail,
    }
