"""TawseelBench — the runner.

Loads scenarios, applies each one's `environment_state` as a patch over the
real seed data via `rafeeq.adapters.store.store.snapshot()`/`restore()` (so
scenarios never leak state into one another — the same guarantee
`store.py`'s own docstring promises), invokes the target under test, grades
the transcript through every oracle in `evaluations/oracles.py`, and
reports per-scenario + per-family + aggregate results.

CLI:
    python -m evaluations.tawseelbench.runner --target stub
    python -m evaluations.tawseelbench.runner --target stub --family security
    python -m evaluations.tawseelbench.runner --target stub --difficulty hard
    python -m evaluations.tawseelbench.runner --target stub --id TB-025
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
SCEN_DIR = Path(__file__).resolve().parent / "scenarios"
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.json"

# Match the convention scripts/selfcheck.py uses: make `rafeeq` (src/) and
# `evaluations` (repo root) importable regardless of how/where this module
# is invoked from, without requiring the caller to set PYTHONPATH first.
for _p in (REPO_ROOT / "src", REPO_ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
del _p

FAMILIES = ["orders", "logistics", "billing", "multi_domain", "security", "policy_edge"]


def load_schema() -> dict[str, Any]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def load_scenarios(family: str | None = None) -> list[dict[str, Any]]:
    """Load every scenario JSON file, optionally restricted to one family
    (the scenarios/<family>/ subdirectory name). Sorted by id so runs are
    deterministic and diffable."""
    families = [family] if family else FAMILIES
    scenarios: list[dict[str, Any]] = []
    for fam in families:
        fam_dir = SCEN_DIR / fam
        if not fam_dir.is_dir():
            continue
        for path in sorted(fam_dir.glob("TB-*.json")):
            scenarios.append(json.loads(path.read_text(encoding="utf-8")))
    scenarios.sort(key=lambda s: s["id"])
    return scenarios


def filter_scenarios(scenarios: list[dict[str, Any]], *, difficulty: str | None = None,
                      scenario_id: str | None = None, tag: str | None = None,
                      locale: str | None = None) -> list[dict[str, Any]]:
    out = scenarios
    if scenario_id:
        out = [s for s in out if s["id"] == scenario_id]
    if difficulty:
        out = [s for s in out if s["difficulty"] == difficulty]
    if tag:
        out = [s for s in out if tag in s.get("tags", [])]
    if locale:
        out = [s for s in out if s["locale"] == locale]
    return out


def apply_environment_state(store: Any, environment_state: dict[str, Any]) -> None:
    """Deep-merge a scenario's `environment_state.patch` onto the live
    store. Record-level sections (`orders`/`customers`/`payments`) MERGE
    field-by-field into the existing seed record (so a scenario only needs
    to state the fields it changes); `events_by_order`/`tickets_by_customer`
    REPLACE the target order/customer's full list (there is no sane
    field-level merge for a list); `refund_ledger` sets entries by key."""
    store.ensure_loaded()
    patch = environment_state.get("patch", {}) or {}
    for section in ("orders", "customers", "payments"):
        section_target: dict[str, dict] = getattr(store, section)
        for record_id, fields in patch.get(section, {}).items():
            if record_id in section_target:
                section_target[record_id].update(fields)
            else:  # pragma: no cover - scenarios are expected to patch existing records only
                section_target[record_id] = dict(fields)
    for order_id, events in patch.get("events_by_order", {}).items():
        store.events_by_order[order_id] = events
    for customer_id, tickets in patch.get("tickets_by_customer", {}).items():
        store.tickets_by_customer[customer_id] = tickets
    for key, record in patch.get("refund_ledger", {}).items():
        store.refund_ledger[key] = record


def run_scenario(scenario: dict[str, Any], target) -> dict[str, Any]:
    """Run ONE scenario against `target` and grade it. Returns a result
    record: {"scenario_id", "family", "passed", "transcript",
    "oracle_results", "store_diff"}. Store state is always restored, even
    if the target raises."""
    from evaluations import oracles
    from evaluations.statediff import diff_snapshots
    from evaluations.targets import Task, TargetUnavailable
    from rafeeq.adapters.store import store

    store.ensure_loaded()
    before = store.snapshot()
    try:
        apply_environment_state(store, scenario["environment_state"])
        req = scenario["customer_request"]
        task = Task(
            id=scenario["id"], text=req["text"], locale=req.get("locale", "en"),
            customer_id=req.get("customer_id"), order_id=req.get("order_id"),
            intent_hint=scenario.get("intent"),
        )
        error: str | None = None
        try:
            result = target(task)
            transcript = result.to_dict()
        except TargetUnavailable:
            # A missing dependency (e.g. langgraph) is an ENVIRONMENT
            # problem, not a per-scenario grading failure — propagate it
            # so the caller can report it once, clearly.
            raise
        except Exception as exc:  # noqa: BLE001 - a target crash is a FAILED scenario, not a runner crash
            error = f"{type(exc).__name__}: {exc}"
            transcript = {
                "task_id": scenario["id"], "reply_text": "", "reply_locale": req.get("locale", "en"),
                "tool_calls": [], "specialist": None, "handoffs": 0, "steps": 0, "escalated": False,
                "escalation_reason": None, "refused": False, "clarifying_question": False,
                "tokens_in": 0, "tokens_out": 0, "cost_usd": 0.0, "latency_s": 0.0, "error": error,
            }
        after = store.snapshot()
        store_diff = diff_snapshots(before, after)
    finally:
        store.restore(before)

    oracle_results = oracles.evaluate_scenario(scenario, after, transcript, store_diff)
    passed = oracles.overall_passed(oracle_results) and not transcript.get("error")

    n = int(scenario["id"][3:])
    family = ("orders" if n <= 6 else "logistics" if n <= 15 else "billing" if n <= 24
              else "multi_domain" if n <= 36 else "security" if n <= 50 else "policy_edge")

    return {
        "scenario_id": scenario["id"], "title": scenario["title"], "family": family,
        "difficulty": scenario["difficulty"], "locale": scenario["locale"],
        "tags": scenario.get("tags", []), "passed": passed,
        "transcript": transcript, "scenario": scenario,
        "oracle_results": {k: v.to_dict() for k, v in oracle_results.items()},
        "store_diff": store_diff,
    }


def run_bench(scenarios: list[dict[str, Any]], target) -> list[dict[str, Any]]:
    return [run_scenario(s, target) for s in scenarios]


def validate_all_scenarios() -> list[str]:
    """Validate every scenario file against schema.json. Returns a list of
    "<id>: <error>" strings (empty == every scenario is valid)."""
    from evaluations.tawseelbench.validate import validate_scenario

    schema = load_schema()
    problems: list[str] = []
    for scenario in load_scenarios():
        for err in validate_scenario(scenario, schema):
            problems.append(f"{scenario['id']}: {err}")
    return problems


def _print_summary(results: list[dict[str, Any]]) -> None:
    from evaluations.metrics import Metrics, render_family_table, render_table

    overall = Metrics.from_results(results)
    print(render_table(overall, title=f"TawseelBench — {len(results)} scenario(s)"))
    print()
    by_family: dict[str, list[dict[str, Any]]] = {}
    for r in results:
        by_family.setdefault(r["family"], []).append(r)
    family_metrics = {fam: Metrics.from_results(rs) for fam, rs in by_family.items()}
    print(render_family_table(family_metrics))
    print()
    failed = [r for r in results if not r["passed"]]
    if failed:
        print(f"### {len(failed)} failing scenario(s)")
        for r in failed:
            reasons = [f"{k}: {v['detail']}" for k, v in r["oracle_results"].items() if not v["passed"]]
            print(f"- {r['scenario_id']} ({r['family']}, {r['difficulty']}): {'; '.join(reasons) or r['transcript'].get('error')}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run TawseelBench against a target.")
    parser.add_argument("--target", default="stub", help="stub | monolith | supervisor | recorded:<path>")
    parser.add_argument("--family", choices=FAMILIES, default=None)
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], default=None)
    parser.add_argument("--tag", default=None)
    parser.add_argument("--locale", choices=["ar", "en"], default=None)
    parser.add_argument("--id", dest="scenario_id", default=None)
    parser.add_argument("--validate-only", action="store_true", help="only validate scenarios against schema.json")
    parser.add_argument("--out", default=None, help="write full JSON results to this path")
    args = parser.parse_args(argv)

    if args.validate_only:
        problems = validate_all_scenarios()
        if problems:
            print(f"{len(problems)} schema validation error(s):")
            for p in problems:
                print(f"  {p}")
            return 1
        print(f"All {len(load_scenarios())} scenarios validate against schema.json.")
        return 0

    from evaluations.targets import get_target

    scenarios = load_scenarios(args.family)
    scenarios = filter_scenarios(scenarios, difficulty=args.difficulty, scenario_id=args.scenario_id,
                                  tag=args.tag, locale=args.locale)
    if not scenarios:
        print("No scenarios matched the given filters.")
        return 1

    try:
        target = get_target(args.target)
    except Exception as exc:  # noqa: BLE001
        print(f"Could not construct target {args.target!r}: {exc}")
        return 1

    results = run_bench(scenarios, target)
    _print_summary(results)

    if args.out:
        Path(args.out).write_text(json.dumps(results, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        print(f"\nwrote {args.out}")

    return 0 if all(r["passed"] for r in results) else 0  # non-zero reserved for --gate in harness.py


if __name__ == "__main__":
    raise SystemExit(main())
