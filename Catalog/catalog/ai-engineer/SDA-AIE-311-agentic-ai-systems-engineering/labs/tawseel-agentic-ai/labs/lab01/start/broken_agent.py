#!/usr/bin/env python3
"""Lab 1, Task 1 — the runaway agent. RUN THIS FIRST, then kill it.

This is what an "agent" looks like before Module 1's lesson lands: a
`while True:` wrapped around a chat call, with no termination condition
at all. It is wired against `rafeeq.core.llm.get_model()` — the default
`StubChatModel` (SPEC §2) — so it costs nothing and needs no API key, but
it is exactly as unbounded as a real one calling a real frontier model:
nothing here ever stops it.

Run it:

    PYTHONPATH=src python3 labs/lab01/start/broken_agent.py

Watch the call counter climb, then press Ctrl-C. That is the Module 1
case study ("The Runaway Refund Agent at a Gulf E-commerce Platform") in
miniature: a "confused customer" message the loop can never resolve,
120+ silent calls, no audit trail — because there is no state to audit,
only a growing list of messages nobody ever inspects.

Find the three `# SMELL` comments below before you write a single line
of `RafeeqState`/`graph.py` — Task 2 and 3 exist to remove exactly these
three.
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.llm import get_model  # Layer A: the stub model, zero cost, zero keys

# A "confused customer" message: no order id, no recognisable intent — the
# kind of input StubChatModel answers with a generic bilingual greeting
# and NO tool call, forever, because nothing about the conversation ever
# changes turn to turn in this broken version.
CONFUSED_CUSTOMER_MESSAGE = "مش عارف, بس ساعدني لو سمحت"  # "I don't know, just help me please"


def run_forever() -> None:
    model = get_model()

    # SMELL: state is a bare, untyped list of messages — no step_count, no
    # resolution flag, nothing an auditor (or a router!) can inspect to
    # answer "why did this run do what it did". Compare to Module 1's
    # `RafeeqState` TypedDict, which is the entire point of Task 2.
    messages: list[tuple[str, str]] = [("human", CONFUSED_CUSTOMER_MESSAGE)]

    call_count = 0
    # SMELL: no step budget. There is no MAX_STEPS, no cost cap, no
    # wall-clock timeout — nothing bounds this loop on any of the three
    # axes Module 1 §4 requires (steps, cost, wall-clock time). It will
    # run until the process is killed, exactly like the incident this
    # lab's case study describes.
    while True:
        reply = model.invoke(messages)
        call_count += 1
        print(f"[call {call_count:>4}] model says: {reply.content!r}  tool_calls={reply.tool_calls}")

        # SMELL: the model's own "I am done" signal (no tool_calls, a
        # final answer) is never read. A real termination condition checks
        # `route(state)`-style logic EVERY iteration; this loop just always
        # goes around again regardless of what the model replied — "the
        # model decides when it's done" is not even wired up here, let
        # alone trusted as sufficient (Module 1's Mini-Exercise Q5).
        messages = messages  # (nothing about the conversation ever advances)


if __name__ == "__main__":
    try:
        run_forever()
    except KeyboardInterrupt:
        print("\nKilled with Ctrl-C. That is the ONLY thing that stopped this agent — "
              "no code in this file ever would have. Now go build the bounded version.")
        raise SystemExit(130)
