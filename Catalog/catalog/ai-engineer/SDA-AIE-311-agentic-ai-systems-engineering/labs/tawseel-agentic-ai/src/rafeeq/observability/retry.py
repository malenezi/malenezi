"""Module 9 — bounded retry, keyed off idempotency, with a proof ledger.

Transient failures (a tool timeout, a rate-limit) deserve a bounded retry
with backoff — but ONLY for idempotent operations. `call_with_retry` reads
`rafeeq.tools.registry.IDEMPOTENT` (Module 3's read/write split, not a
second hand-maintained list) to decide: a read tool (`track_shipment`) is
retried on `TransientToolError`; a write tool (`issue_refund`) is called
EXACTLY ONCE, full stop — retrying a write is the double-refund incident
(M1/M3) reborn.

`RetryLedger` exists so that claim is not just asserted in a docstring: it
records every attempt, so the capstone (and `tests/security` / CI) can
PROVE `issue_refund` was retried zero times by reading the ledger back,
not by re-reading this file's logic and hoping.

Dependency-free (Layer A): stdlib (`time`, `dataclasses`) +
`rafeeq.tools.registry.IDEMPOTENT` + `rafeeq.core.errors.TransientToolError`.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from threading import Lock
from typing import Any, Callable, TypeVar

from rafeeq.core.errors import TransientToolError
from rafeeq.tools.registry import IDEMPOTENT

T = TypeVar("T")


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Attempt:
    tool_name: str
    attempt_no: int          # 1-indexed
    ts: str
    outcome: str              # "success" | "transient_error" | "raised" | "gave_up"
    idempotent: bool
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return dict(self.__dict__)


@dataclass
class RetryLedger:
    """Every attempt made through `call_with_retry`, in order. This is the
    capstone's evidence artefact: `assert_never_retried("issue_refund")`
    reads THIS, not the retry function's source code."""

    attempts: list[Attempt] = field(default_factory=list)
    _lock: Lock = field(default_factory=Lock, repr=False, compare=False)

    def record(self, tool_name: str, attempt_no: int, outcome: str, idempotent: bool,
               error: str | None = None) -> Attempt:
        attempt = Attempt(tool_name=tool_name, attempt_no=attempt_no, ts=_now_iso(),
                           outcome=outcome, idempotent=idempotent, error=error)
        with self._lock:
            self.attempts.append(attempt)
        return attempt

    def attempts_for(self, tool_name: str) -> list[Attempt]:
        return [a for a in self.attempts if a.tool_name == tool_name]

    def retry_count(self, tool_name: str) -> int:
        """Number of attempts BEYOND the first for `tool_name` — the
        number that must be 0 for any write tool."""
        return max(0, len(self.attempts_for(tool_name)) - 1)

    def assert_never_retried(self, tool_name: str) -> None:
        """Raise `AssertionError` if `tool_name` was ever called more than
        once through this ledger. The capstone's proof obligation
        ("issue_refund retried 0 times") made a one-liner."""
        n = self.retry_count(tool_name)
        assert n == 0, f"{tool_name} was retried {n} time(s) — write tools must be retried 0 times"

    def to_dict(self) -> dict[str, Any]:
        return {"attempts": [a.to_dict() for a in self.attempts]}

    def summary(self) -> str:
        by_tool: dict[str, int] = {}
        for a in self.attempts:
            by_tool[a.tool_name] = by_tool.get(a.tool_name, 0) + 1
        lines = ["RetryLedger summary:"]
        for tool, n in sorted(by_tool.items()):
            retries = self.retry_count(tool)
            lines.append(f"  {tool}: {n} attempt(s), {retries} retr{'y' if retries == 1 else 'ies'}")
        return "\n".join(lines)


# A process-wide default ledger — convenient for scripts/labs/tests that
# do not thread an explicit one through. Real request handling
# (`service/api.py`) should create one per run so a run's ledger can ship
# alongside its trace, but the default exists so `call_with_retry` is
# usable stand-alone without ceremony.
DEFAULT_LEDGER = RetryLedger()


def call_with_retry(tool_name: str, fn: Callable[..., T], *args: Any, retries: int = 2,
                     base: float = 0.5, ledger: RetryLedger | None = None,
                     sleep: Callable[[float], None] | None = None, **kwargs: Any) -> T:
    """Call `fn(*args, **kwargs)`, retrying with exponential backoff ONLY
    if `tool_name in IDEMPOTENT` and the call raises `TransientToolError`.

    A WRITE tool (`tool_name not in IDEMPOTENT`) is called EXACTLY ONCE —
    no try/except loop at all — whatever it raises propagates immediately.
    This is not an optimisation, it is the safety property: the branch
    that would retry a write simply does not exist in this function's
    control flow for that tool_name, so there is no flag to forget to set.

    `sleep` is injectable (defaults to `time.sleep`) so tests can assert
    backoff behaviour without a real wall-clock delay.
    """
    ledger = ledger if ledger is not None else DEFAULT_LEDGER
    do_sleep = sleep or time.sleep
    idempotent = tool_name in IDEMPOTENT

    if not idempotent:
        # NEVER retry a write tool (SPEC §7 mistake #4 / M9 mistake #4).
        try:
            result = fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001 - record then re-raise, never swallow
            ledger.record(tool_name, 1, "raised", idempotent=False, error=f"{type(exc).__name__}: {exc}")
            raise
        ledger.record(tool_name, 1, "success", idempotent=False)
        return result

    last_error: TransientToolError | None = None
    for attempt in range(1, retries + 2):  # first try + `retries` retries
        try:
            result = fn(*args, **kwargs)
        except TransientToolError as exc:
            last_error = exc
            ledger.record(tool_name, attempt, "transient_error", idempotent=True, error=str(exc))
            if attempt == retries + 1:
                ledger.record(tool_name, attempt, "gave_up", idempotent=True, error=str(exc))
                raise
            do_sleep(base * (2 ** (attempt - 1)))
            continue
        except Exception as exc:  # noqa: BLE001 - non-transient: record and stop, no retry
            ledger.record(tool_name, attempt, "raised", idempotent=True, error=f"{type(exc).__name__}: {exc}")
            raise
        ledger.record(tool_name, attempt, "success", idempotent=True)
        return result

    # Unreachable (the loop above always returns or raises), but keeps the
    # type checker honest about `call_with_retry`'s return type.
    assert last_error is not None  # pragma: no cover
    raise last_error
