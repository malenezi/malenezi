#!/usr/bin/env python3
"""Module 9/final capstone — the `sim-incident` brownout drill.

Runnable standalone (`python3 deployment/sim_env/scripts/sim_incident.py`)
or as the `sim-backends` compose service's `--serve` mode. Stdlib +
`rafeeq.observability.{retry,slo}` + `rafeeq.core.errors` only.

What it proves, end to end, with real measurements (not an assertion in
prose):

  1. baseline (brownout off): p95 latency is well under the SLO, and
     `slo.check_slos` reports no alert.
  2. inject a brownout (`sim_env.config.set_brownout(True, ...)`): repeat
     the same simulated read-tool calls through
     `observability.retry.call_with_retry` (so a transient failure is
     retried, exactly as `docs/OBSERVABILITY.md`'s retry-safety rule
     describes) and measure p95 latency again — this time it is worse,
     and the p95-latency alert FIRES.
  3. respond: turn the brownout back off, re-measure, and confirm the
     alert clears — the "watch the alert fire, respond" loop
     `deployment/runbook.md` walks an operator through.

Exit code is 0 only if every assertion above holds; CI/the runbook can
treat a nonzero exit as "the drill itself is broken", distinct from "the
alert didn't fire when it should have" (which raises `AssertionError`
with a message naming exactly which check failed).
"""
from __future__ import annotations

import argparse
import statistics
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_SIM_ENV_DIR = _HERE.parent          # deployment/sim_env
_DEPLOYMENT_DIR = _SIM_ENV_DIR.parent  # deployment
_REPO_ROOT = _DEPLOYMENT_DIR.parent    # repo root
_SRC = _REPO_ROOT / "src"

for _p in (_SRC, _DEPLOYMENT_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
del _p

from sim_env import config as sim_config  # noqa: E402 - after sys.path fixup

from rafeeq.core.errors import TransientToolError  # noqa: E402
from rafeeq.observability import slo  # noqa: E402
from rafeeq.observability.retry import RetryLedger, call_with_retry  # noqa: E402

N_CALLS = 12
READ_TOOL = "track_shipment"          # idempotent (tools.registry.IDEMPOTENT) — safe to retry
LATENCY_SLO = slo.SLOs()               # default targets (p95 <= 2.5s, etc — Module 9's own bench table


def _simulated_read(order_id: str) -> dict:
    """Stand-in for a real adapter read. Calls `sim_env.config.maybe_inject`
    first (the ONE line a real adapter would add to participate in this
    drill — see `config.py`'s module docstring), then returns instantly."""
    sim_config.maybe_inject(READ_TOOL)
    return {"order_id": order_id, "status": "in_transit"}


def _measure(n: int, ledger: RetryLedger) -> list[float]:
    latencies: list[float] = []
    for i in range(n):
        t0 = time.monotonic()
        try:
            call_with_retry(READ_TOOL, _simulated_read, f"TW-2026-{10000+i}",
                             retries=2, base=0.05, ledger=ledger)
        except TransientToolError:
            pass  # a call that exhausts retries still counts toward latency/error signals
        latencies.append(time.monotonic() - t0)
    return latencies


def _p95(values: list[float]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, round(0.95 * (len(ordered) - 1)))
    return ordered[idx]


def run_drill() -> int:
    print("== sim-incident: brownout drill ==\n")

    # -- 1. baseline -----------------------------------------------------
    sim_config.set_brownout(False)
    baseline_ledger = RetryLedger()
    baseline_latencies = _measure(N_CALLS, baseline_ledger)
    baseline_p95 = _p95(baseline_latencies)
    baseline_alerts = slo.check_slos({"p95_latency_s": baseline_p95}, LATENCY_SLO)
    print(f"baseline p95 latency: {baseline_p95:.3f}s  (SLO <= {LATENCY_SLO.p95_latency_s_max}s)")
    print(slo.render_alerts(baseline_alerts))
    assert not baseline_alerts, f"baseline should be SLO-green, got: {baseline_alerts}"

    # -- 2. inject the brownout -------------------------------------------
    sim_config.set_brownout(True, extra_latency_s=1.0, error_rate=0.6)
    brownout_ledger = RetryLedger()
    print("\n-- brownout injected: extra_latency_s=1.0 error_rate=0.6 --")
    brownout_latencies = _measure(N_CALLS, brownout_ledger)
    brownout_p95 = _p95(brownout_latencies)
    brownout_alerts = slo.check_slos({"p95_latency_s": brownout_p95}, LATENCY_SLO)
    print(f"\nbrownout p95 latency: {brownout_p95:.3f}s  (SLO <= {LATENCY_SLO.p95_latency_s_max}s)")
    print(f"retries observed: {brownout_ledger.retry_count(READ_TOOL)} "
          f"(across {len(brownout_ledger.attempts_for(READ_TOOL))} attempts, all on the idempotent read tool)")
    print(slo.render_alerts(brownout_alerts))
    assert brownout_p95 > baseline_p95, "brownout should measurably worsen p95 latency"
    assert any(a.metric == "p95_latency_s" for a in brownout_alerts), \
        "the p95-latency alert MUST fire during the brownout — it did not"

    # -- 3. respond: turn the brownout off, confirm recovery --------------
    sim_config.set_brownout(False)
    recovery_ledger = RetryLedger()
    recovery_latencies = _measure(N_CALLS, recovery_ledger)
    recovery_p95 = _p95(recovery_latencies)
    recovery_alerts = slo.check_slos({"p95_latency_s": recovery_p95}, LATENCY_SLO)
    print(f"\nrecovery p95 latency: {recovery_p95:.3f}s  (SLO <= {LATENCY_SLO.p95_latency_s_max}s)")
    print(slo.render_alerts(recovery_alerts))
    assert not recovery_alerts, f"recovery should clear the alert, got: {recovery_alerts}"

    print("\nsim-incident drill: PASSED "
          "(baseline green -> brownout alert fired -> recovery green).")
    return 0


def serve() -> None:
    """`sim-backends` compose service mode: write the (initially off)
    state file and idle, so `sim_env.config.load_state()` from another
    container (mounted on the same `sim_env_state` volume) has something
    to read, and the compose healthcheck (which just checks the file
    exists) can pass."""
    sim_config.save_state(sim_config.SimState())
    print(f"sim-backends: state file at {sim_config.state_path()} — idling.", file=sys.stderr)
    while True:
        time.sleep(3600)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--on", action="store_true", help="turn the brownout on and exit")
    parser.add_argument("--off", action="store_true", help="turn the brownout off and exit")
    parser.add_argument("--serve", action="store_true", help="run as the sim-backends compose service")
    args = parser.parse_args()

    if args.serve:
        serve()
        return 0
    if args.on:
        sim_config.set_brownout(True, extra_latency_s=1.5, error_rate=0.5)
        print(f"brownout ON: {sim_config.load_state()}")
        return 0
    if args.off:
        sim_config.set_brownout(False)
        print(f"brownout OFF: {sim_config.load_state()}")
        return 0

    try:
        return run_drill()
    except AssertionError as exc:
        print(f"\nsim-incident drill: FAILED — {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
