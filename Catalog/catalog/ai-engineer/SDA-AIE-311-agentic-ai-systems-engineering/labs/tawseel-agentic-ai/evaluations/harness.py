"""Module 9 (evaluation layer) — the cross-module harness.

This is the SAME harness reused Day 1 through Day 5 of the course: it runs
any target (a rule-based stub, a LangGraph monolith, a supervisor + spec-
ialist system, or a replay of recorded transcripts — see `targets.py`)
over `data/tickets_eval.jsonl` (120 bilingual, labelled tickets — SPEC
§3/§4), grades every ticket, and writes a timestamped JSON report plus a
markdown summary under `reports/`.

TEACHING POINT (LangSmith principle, SPEC §6): a production trace that
went wrong should become a regression test, not a one-off bug fix. This
harness's `--baseline`/`--gate` pair is the smallest version of that idea
that can run entirely offline: freeze today's metrics as a baseline
report, and any later run that regresses beyond tolerance fails CI
(`--gate` exits non-zero) instead of merging silently.

Grading reuses `evaluations/oracles.py` verbatim by normalising each
ticket into the same pseudo-scenario shape TawseelBench scenarios already
have (`ticket_to_pseudo_scenario`) — ONE set of oracles, ONE metrics
module, for both benchmarks (see `metrics.py`'s own docstring on this).

CLI:
    python -m evaluations.harness --target stub
    python -m evaluations.harness --target stub --tag multi_domain
    python -m evaluations.harness --target stub --out reports/eval_stub.json
    python -m evaluations.harness --target stub --baseline reports/eval_stub_baseline.json --gate
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
TICKETS_PATH = REPO_ROOT / "data" / "tickets_eval.jsonl"
REPORTS_DIR = REPO_ROOT / "reports"

# Same sys.path convention as tawseelbench/runner.py and scripts/selfcheck.py
# — importable regardless of how/where this module is invoked from.
for _p in (REPO_ROOT / "src", REPO_ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
del _p

# Metrics that regress when they go UP are compared the opposite way round
# from metrics that regress when they go DOWN — see `_check_gate`.
_LOWER_IS_BETTER = {
    "unsafe_action_rate", "retry_failure_rate", "avg_tool_calls_per_task",
    "avg_tokens_in_per_task", "avg_tokens_out_per_task", "avg_cost_usd_per_task",
    "avg_cost_sar_equivalent_per_task", "p50_latency_s", "p95_latency_s",
    "attack_success_rate",
}
_GATED_METRICS = (
    "task_success_rate", "policy_compliance_rate", "correct_tool_call_rate",
    "unsafe_action_rate", "attack_success_rate",
)
DEFAULT_TOLERANCE = 0.02  # 2 percentage points, per metric, before --gate trips


def load_tickets() -> list[dict[str, Any]]:
    tickets: list[dict[str, Any]] = []
    with TICKETS_PATH.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                tickets.append(json.loads(line))
    return tickets


def filter_tickets(tickets: list[dict[str, Any]], *, difficulty: str | None = None,
                    intent: str | None = None, tag: str | None = None,
                    locale: str | None = None, ticket_id: str | None = None) -> list[dict[str, Any]]:
    out = tickets
    if ticket_id:
        out = [t for t in out if t["ticket_id"] == ticket_id]
    if difficulty:
        out = [t for t in out if t["difficulty"] == difficulty]
    if intent:
        out = [t for t in out if t["intent"] == intent]
    if tag:
        out = [t for t in out if tag in t.get("tags", [])]
    if locale:
        out = [t for t in out if t["locale"] == locale]
    return out


def ticket_to_pseudo_scenario(ticket: dict[str, Any]) -> dict[str, Any]:
    """Normalise one `tickets_eval.jsonl` row into the same scenario shape
    `evaluations/oracles.py` grades TawseelBench scenarios against, so the
    exact same 13 oracles apply here with zero special-casing.

    Deliberately NOT populated: `expected_state_transition.tool_sequence`.
    `expected.tools` in this fixture is an unordered "these must be
    called" set (SPEC §4's ticket shape), not an ordered sequence — filling
    it in here would make `tool_selection_correct` fail on any ticket
    whose target legitimately calls a grounding tool (e.g. `get_order`)
    before the tool the fixture happens to name first. `required_tools_called`
    (an unordered subset check) is the oracle this fixture is actually
    shaped for."""
    expected = ticket.get("expected", {}) or {}
    return {
        "id": ticket["ticket_id"],
        "title": ticket.get("text", "")[:80],
        "locale": ticket.get("locale", "en"),
        "difficulty": ticket.get("difficulty", "medium"),
        "domains": [],
        "intent": ticket.get("intent"),
        "tags": ticket.get("tags", []),
        "customer_request": {
            "text": ticket["text"], "locale": ticket.get("locale", "en"),
            "customer_id": ticket.get("customer_id"), "order_id": ticket.get("order_id"),
        },
        "applicable_policy": {"policy_ids": [], "policy_version": ""},
        "expected_state_transition": {},
        "pass_fail_criteria": {
            "must_call_tools": expected.get("tools", []) or [],
            "must_not_mention": expected.get("must_not", []) or [],
            "language_must_match_customer": True,
            "escalation_required": expected.get("resolution") == "escalated",
        },
        "notes_for_instructor": "",
    }


def run_ticket(ticket: dict[str, Any], target) -> dict[str, Any]:
    """Run ONE ticket against `target` and grade it. Unlike TawseelBench
    scenarios, tickets carry no `environment_state` patch — they run
    directly against the live seed data (read-only questions) or, for
    write intents (refund/reschedule), against whatever state the seed
    already has for that order. Store state is restored afterwards so
    running the harness never leaves side effects for the next ticket or
    the next run."""
    from evaluations import oracles
    from evaluations.statediff import diff_snapshots
    from evaluations.targets import Task, TargetUnavailable
    from rafeeq.adapters.store import store

    store.ensure_loaded()
    before = store.snapshot()
    try:
        task = Task(
            id=ticket["ticket_id"], text=ticket["text"], locale=ticket.get("locale", "en"),
            customer_id=ticket.get("customer_id"), order_id=ticket.get("order_id"),
            intent_hint=ticket.get("intent"),
        )
        error: str | None = None
        try:
            result = target(task)
            transcript = result.to_dict()
        except TargetUnavailable:
            # A missing dependency (e.g. langgraph) is an ENVIRONMENT
            # problem, not a per-ticket grading failure — let it propagate
            # so the caller (the CLI, dashboard.py, ...) can report it
            # once, clearly, instead of every ticket silently "failing".
            raise
        except Exception as exc:  # noqa: BLE001 - a target crash is a FAILED ticket, not a harness crash
            error = f"{type(exc).__name__}: {exc}"
            transcript = {
                "task_id": ticket["ticket_id"], "reply_text": "", "reply_locale": ticket.get("locale", "en"),
                "tool_calls": [], "specialist": None, "handoffs": 0, "steps": 0, "escalated": False,
                "escalation_reason": None, "refused": False, "clarifying_question": False,
                "tokens_in": 0, "tokens_out": 0, "cost_usd": 0.0, "latency_s": 0.0, "error": error,
            }
        after = store.snapshot()
        store_diff = diff_snapshots(before, after)
    finally:
        store.restore(before)

    scenario = ticket_to_pseudo_scenario(ticket)
    oracle_results = oracles.evaluate_scenario(scenario, after, transcript, store_diff)
    passed = oracles.overall_passed(oracle_results) and not transcript.get("error")

    return {
        "scenario_id": ticket["ticket_id"], "title": scenario["title"], "family": "tickets_eval",
        "difficulty": ticket.get("difficulty"), "locale": ticket.get("locale"),
        "tags": ticket.get("tags", []), "passed": passed,
        "transcript": transcript, "scenario": scenario,
        "oracle_results": {k: v.to_dict() for k, v in oracle_results.items()},
        "store_diff": store_diff,
    }


def run_harness(tickets: list[dict[str, Any]], target) -> list[dict[str, Any]]:
    return [run_ticket(t, target) for t in tickets]


def _print_summary(results: list[dict[str, Any]], target_name: str) -> None:
    from evaluations.metrics import Metrics, render_table

    m = Metrics.from_results(results)
    print(render_table(m, title=f"harness — {target_name} over {len(results)} ticket(s)"))
    failed = [r for r in results if not r["passed"]]
    print()
    if failed:
        print(f"### {len(failed)} failing ticket(s)")
        for r in failed:
            reasons = [f"{k}: {v['detail']}" for k, v in r["oracle_results"].items() if not v["passed"]]
            print(f"- {r['scenario_id']} ({r['difficulty']}, {r['locale']}): {'; '.join(reasons) or r['transcript'].get('error')}")


def _write_report(results: list[dict[str, Any]], target_name: str, out_path: Path) -> dict[str, Any]:
    from evaluations.metrics import Metrics

    m = Metrics.from_results(results)
    report = {
        "target": target_name,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "n_tickets": len(results),
        "metrics": m.to_dict(),
        "results": results,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    md_path = out_path.with_suffix(".md")
    from evaluations.metrics import render_table
    md_path.write_text(render_table(m, title=f"harness — {target_name}"), encoding="utf-8")
    return report


def _check_gate(current: dict[str, float], baseline: dict[str, float],
                 tolerance: float = DEFAULT_TOLERANCE) -> list[str]:
    """Compare `current` metrics against a `baseline` report's metrics.
    Returns a list of human-readable regression messages (empty == no
    regression beyond `tolerance` on any gated metric). A metric missing
    from either side (e.g. `attack_success_rate` is None when a run has
    no security-tagged tasks) is skipped, not treated as a regression."""
    problems: list[str] = []
    for name in _GATED_METRICS:
        cur, base = current.get(name), baseline.get(name)
        if cur is None or base is None:
            continue
        delta = cur - base
        regressed = (delta < -tolerance) if name not in _LOWER_IS_BETTER else (delta > tolerance)
        if regressed:
            problems.append(f"{name}: baseline={base:.3f} current={cur:.3f} delta={delta:+.3f} (tolerance={tolerance})")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the cross-module harness over tickets_eval.jsonl.")
    parser.add_argument("--target", default="stub", help="stub | monolith | supervisor | recorded:<path>")
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], default=None)
    parser.add_argument("--intent", default=None)
    parser.add_argument("--tag", default=None)
    parser.add_argument("--locale", choices=["ar", "en"], default=None)
    parser.add_argument("--id", dest="ticket_id", default=None)
    parser.add_argument("--out", default=None, help="write the full JSON+markdown report here (default: reports/eval_<target>_<ts>.json)")
    parser.add_argument("--baseline", default=None, help="path to a prior report's JSON; enables comparison output")
    parser.add_argument("--gate", action="store_true", help="exit non-zero if any gated metric regresses beyond --tolerance vs --baseline")
    parser.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    args = parser.parse_args(argv)

    from evaluations.targets import get_target

    tickets = load_tickets()
    tickets = filter_tickets(tickets, difficulty=args.difficulty, intent=args.intent,
                              tag=args.tag, locale=args.locale, ticket_id=args.ticket_id)
    if not tickets:
        print("No tickets matched the given filters.")
        return 1

    try:
        target = get_target(args.target)
    except Exception as exc:  # noqa: BLE001
        print(f"Could not construct target {args.target!r}: {exc}")
        return 1

    results = run_harness(tickets, target)
    _print_summary(results, args.target)

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = Path(args.out) if args.out else REPORTS_DIR / f"eval_{args.target.replace(':', '_')}_{ts}.json"
    report = _write_report(results, args.target, out_path)
    print(f"\nwrote {out_path} (+ {out_path.with_suffix('.md').name})")

    if args.baseline:
        baseline_report = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
        problems = _check_gate(report["metrics"], baseline_report.get("metrics", {}), args.tolerance)
        if problems:
            print(f"\n### REGRESSION GATE: {len(problems)} metric(s) regressed vs {args.baseline}")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"\nREGRESSION GATE: no regression vs {args.baseline} (tolerance={args.tolerance}).")
        if args.gate and problems:
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
