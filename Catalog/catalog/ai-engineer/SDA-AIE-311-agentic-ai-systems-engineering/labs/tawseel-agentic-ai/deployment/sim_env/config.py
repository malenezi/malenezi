"""Module 9/final capstone — the simulated Tawseel environment's fault
injection toggles.

This is a tiny, dependency-free, file-backed switch: `SimState.brownout`
plus its magnitude (`extra_latency_s`, `error_rate`). `scripts/sim_incident.py`
flips it; anything that wants to BEHAVE like a degraded backend calls
`maybe_inject(tool_name)` at the top of a read — it sleeps the injected
latency and, with probability `error_rate`, raises
`rafeeq.core.errors.TransientToolError` (a transient, retryable failure —
exactly the shape `observability.retry.call_with_retry` already knows how
to retry for idempotent tools, and exactly the shape a write tool must
NEVER be retried for).

Deliberately NOT wired into `src/rafeeq/adapters/*.py` by this module —
those adapters are owned by earlier modules (M1-M3) and this build's
scope is observability/service/deployment, not editing them. The wiring
point is exactly one line (`sim_env.config.maybe_inject(tool_name)` at
the top of an adapter's read method); `runbook.md`'s sim-incident drill
demonstrates the mechanism end to end against a stand-in flaky call
(`scripts/sim_incident.py`) rather than claiming every adapter already
calls it.

State lives in a JSON file (`SIM_ENV_CONFIG_PATH`, default
`deployment/sim_env/state/state.json`) rather than an env var or an
in-process global, ON PURPOSE: the drill in `runbook.md` flips it from
one process (the operator's shell / CI step) and a SEPARATE process (the
running service, or `scripts/sim_incident.py --serve` in compose) must
observe the change without a restart — the same reason a real feature
flag is never just an env var.
"""
from __future__ import annotations

import json
import os
import random
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent
DEFAULT_STATE_PATH = _HERE / "state" / "state.json"


@dataclass
class SimState:
    brownout: bool = False
    extra_latency_s: float = 0.0
    error_rate: float = 0.0   # fraction of injected calls that raise TransientToolError

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def state_path() -> Path:
    override = os.environ.get("SIM_ENV_CONFIG_PATH")
    return Path(override) if override else DEFAULT_STATE_PATH


def load_state() -> SimState:
    path = state_path()
    if not path.exists():
        return SimState()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return SimState(brownout=bool(data.get("brownout", False)),
                         extra_latency_s=float(data.get("extra_latency_s", 0.0)),
                         error_rate=float(data.get("error_rate", 0.0)))
    except (OSError, ValueError, json.JSONDecodeError):
        return SimState()


def save_state(state: SimState) -> None:
    path = state_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state.to_dict(), indent=2), encoding="utf-8")


def set_brownout(on: bool, extra_latency_s: float = 1.5, error_rate: float = 0.35) -> SimState:
    """Flip the brownout switch. `on=False` always resets magnitude to
    zero — there is no way to leave a stale nonzero latency/error-rate
    behind once the drill turns the brownout back off."""
    state = SimState(brownout=on, extra_latency_s=extra_latency_s if on else 0.0,
                      error_rate=error_rate if on else 0.0)
    save_state(state)
    return state


def maybe_inject(tool_name: str, state: SimState | None = None) -> None:
    """Call at the top of a read. A no-op (zero overhead beyond one file
    stat) when the brownout is off. When on: sleeps `extra_latency_s`
    (the latency signal `slo.py`'s p95 alert would see), then raises
    `TransientToolError` with probability `error_rate` (the reliability
    signal a tool-error-rate alert would see, and exactly the exception
    `observability.retry.call_with_retry` retries for idempotent tools)."""
    from rafeeq.core.errors import TransientToolError  # lazy: keep this module importable standalone

    state = state if state is not None else load_state()
    if not state.brownout:
        return
    if state.extra_latency_s:
        time.sleep(state.extra_latency_s)
    if state.error_rate and random.random() < state.error_rate:
        raise TransientToolError(f"simulated brownout: {tool_name}")
