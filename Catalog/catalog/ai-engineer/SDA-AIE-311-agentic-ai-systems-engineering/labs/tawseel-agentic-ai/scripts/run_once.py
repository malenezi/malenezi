#!/usr/bin/env python3
"""Module 1 — drive the compiled Lab 1 graph once.

The instructor package's own worked example (Module 1, "Running one
bounded task"), wired to run from a clean checkout:

    PYTHONPATH=src python3 scripts/run_once.py
    PYTHONPATH=src python3 scripts/run_once.py --text "I need a refund" --locale en

`recursion_limit` is the HARD backstop even if a routing bug would
otherwise loop forever (Module 1's own troubleshooting row: `route`
without a budget branch raises `GraphRecursionError` — see
`labs/sim/sim_no_terminate.py`).

This script needs `langgraph` + `langchain-core` (Layer B, SPEC §1) — not
installed in the build/CI sandbox this repo was authored in. It still
IMPORTS cleanly under plain python3 (only `main()` touches the
dependency), and prints a clear next step instead of a bare traceback
when the dependency is missing, exactly like every other Layer-B entry
point in this repo (`core.graph._require_langgraph`).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run Rafeeq's Lab 1 core loop once.")
    parser.add_argument("--text", default="أين طلبي رقم TW-2026-88120؟",
                         help="the customer message (default: the package's Arabic order-status example)")
    parser.add_argument("--customer-id", default="CUST-4471")
    parser.add_argument("--locale", default="ar", choices=["ar", "en"])
    args = parser.parse_args(argv)

    try:
        from langchain_core.messages import HumanMessage
        from rafeeq.core.graph import build_graph, MISSING_DEP_HINT, LANGGRAPH_AVAILABLE
    except ImportError as exc:
        print(f"ImportError: {exc}\n\n"
              "run_once.py needs `langgraph` + `langchain-core` to compile and run the "
              "graph (SPEC §1, Layer B). Install with:\n"
              "    pip install langgraph langchain-core langchain-openai\n"
              "Until then, exercise the SAME termination logic offline with:\n"
              "    PYTHONPATH=src python3 -m pytest tests/unit/test_termination.py -q\n"
              "or the stdlib mirror:\n"
              "    PYTHONPATH=src python3 tests/unit/run_without_pytest.py")
        return 1

    if not LANGGRAPH_AVAILABLE:  # pragma: no cover - defensive, matches core.graph's own guard
        print(MISSING_DEP_HINT)
        return 1

    from rafeeq.core.state import new_state

    agent = build_graph()
    initial = new_state(
        messages=[HumanMessage(content=args.text)],
        customer_id=args.customer_id,
        locale=args.locale,
    )
    final = agent.invoke(initial, config={"recursion_limit": 12})
    print(final["messages"][-1].content, "| steps:", final["step_count"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
