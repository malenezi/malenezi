"""Module 8/9 — the security event log.

TEACHING POINT: a guardrail that trips silently taught nobody anything.
Every guardrail trip, authz denial, or red-team finding in this repo
routes through `log_security_event` so it lands in one durable, greppable
place (`reports/security_events.jsonl`) that a SOC/CI job can tail — this
is the M8 "log every guardrail trip and escalation as a security event"
production rule made concrete.

Dependency-free (Layer A): stdlib only (`json`, `logging`, `dataclasses`,
`pathlib`) — every other security module imports this LAZILY (inside a
function, wrapped in `except Exception`) so a logging failure can never
block an authorisation decision or a guardrail verdict (see
`security/authz.py::_log_denial` for the pattern this module is written
to support).

`authz.py` was written first and already guesses at this module's shape
(`log_authz_denial` or `log_event`, called either with kwargs or with a
single positional decision object) — this module supplies BOTH so that
guess resolves cleanly without editing `authz.py`.
"""
from __future__ import annotations

import json
import logging
import threading
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rafeeq.core.config import REPO_ROOT

REPORTS_DIR = REPO_ROOT / "reports"
SECURITY_EVENTS_PATH = REPORTS_DIR / "security_events.jsonl"

SEVERITIES = ("low", "medium", "high", "critical")

_logger = logging.getLogger("rafeeq.security")
_write_lock = threading.Lock()


@dataclass(frozen=True)
class SecurityEvent:
    """One row of the security event log. `kind` is a short machine key
    (e.g. `blocked_over_limit_refund`, `authz_denial`, `injection_flagged`,
    `pii_masked`, `red_team_finding`); `detail` is a small JSON-serialisable
    dict giving the concrete facts (tool name, args, customer id, pattern
    matched) — never free text a human would have to re-parse."""

    ts: str
    kind: str
    severity: str
    detail: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _normalise_severity(severity: str) -> str:
    s = (severity or "medium").strip().lower()
    return s if s in SEVERITIES else "medium"


def log_security_event(kind: str, detail: dict[str, Any] | None = None, severity: str = "medium") -> SecurityEvent:
    """Record ONE security event: structured JSONL append to
    `reports/security_events.jsonl` PLUS a stdlib `logging` line (so it
    shows up in console/CI logs even before anyone greps the file).

    Never raises: a security event that cannot be persisted must not take
    down the guardrail/authz call that is reporting it — on any I/O
    failure this degrades to logging-only and returns the event anyway.
    """
    event = SecurityEvent(
        ts=datetime.now(timezone.utc).isoformat(),
        kind=kind,
        severity=_normalise_severity(severity),
        detail=dict(detail or {}),
    )

    log_fn = {
        "low": _logger.info, "medium": _logger.warning,
        "high": _logger.error, "critical": _logger.critical,
    }[event.severity]
    log_fn("security_event kind=%s severity=%s detail=%s", event.kind, event.severity, event.detail)

    try:
        with _write_lock:
            REPORTS_DIR.mkdir(parents=True, exist_ok=True)
            with SECURITY_EVENTS_PATH.open("a", encoding="utf-8") as f:
                f.write(json.dumps(event.to_dict(), ensure_ascii=False) + "\n")
    except OSError:  # noqa: BLE001 - persistence must never break the caller
        _logger.exception("failed to persist security event to %s", SECURITY_EVENTS_PATH)

    return event


def log_authz_denial(**kwargs: Any) -> SecurityEvent:
    """Shape `security/authz.py::_log_denial` already calls by keyword
    (`event="authz_denial"`, plus decision fields) — adapt it onto
    `log_security_event` without requiring authz.py to change."""
    kwargs = dict(kwargs)
    kwargs.pop("event", None)
    reason = kwargs.get("reason", "")
    severity = "high" if reason in ("prohibited_action", "cross_customer_denied") else "medium"
    return log_security_event("authz_denial", kwargs, severity=severity)


def log_event(*args: Any, **kwargs: Any) -> SecurityEvent:
    """Loose-signature fallback so any caller guessing at this module's
    entry point (`log_fn(decision)` positional, or arbitrary kwargs)
    still lands a row instead of raising `TypeError`. Prefer
    `log_security_event` for new call sites."""
    if args and hasattr(args[0], "__dict__") and not kwargs:
        obj = args[0]
        detail = {k: v for k, v in vars(obj).items() if k not in ("severity",)}
        severity = getattr(obj, "severity", "medium")
        kind = detail.pop("reason", None) or detail.pop("kind", None) or type(obj).__name__
        return log_security_event(str(kind), detail, severity=str(severity))
    kind = kwargs.pop("kind", None) or kwargs.pop("event", None) or (str(args[0]) if args else "event")
    severity = kwargs.pop("severity", "medium")
    return log_security_event(str(kind), kwargs, severity=severity)


def read_events(kind: str | None = None, severity: str | None = None, limit: int | None = None) -> list[SecurityEvent]:
    """Read back `reports/security_events.jsonl`, optionally filtered by
    `kind`/`severity`, most-recent-last (file order). Used by the red-team
    suite's oracles (did THIS run trip a security event?) and by
    `tests/security/*` to assert a guardrail actually logged. Returns an
    empty list if the file does not exist yet — a fresh checkout has no
    security history, that is not an error."""
    if not SECURITY_EVENTS_PATH.exists():
        return []
    events: list[SecurityEvent] = []
    with SECURITY_EVENTS_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if kind is not None and row.get("kind") != kind:
                continue
            if severity is not None and row.get("severity") != severity:
                continue
            events.append(SecurityEvent(
                ts=row.get("ts", ""), kind=row.get("kind", ""),
                severity=row.get("severity", "medium"), detail=row.get("detail", {}),
            ))
    if limit is not None:
        events = events[-limit:]
    return events


def clear_events() -> None:
    """Test helper: truncate the security event log. Never call from
    production code — only from test setUp/tearDown so red-team/guardrail
    tests can assert against a clean log without cross-test pollution."""
    try:
        if SECURITY_EVENTS_PATH.exists():
            SECURITY_EVENTS_PATH.unlink()
    except OSError:
        pass
