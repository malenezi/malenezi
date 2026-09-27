
"""story/qa_prep.py — the Q&A preparation matrix.

Every answer has the same three beats: ACKNOWLEDGE, answer BRIEFLY, then BRIDGE back
to the Big Idea. Two master rules: bridge after every answer, and never bluff a number.

The bank ships as data (`qa_bank.csv`, 12 committee questions), so the matrix is built
from the real bank rather than invented at the desk.
"""
from __future__ import annotations

import pandas as pd

TECHNIQUE = {
    "Clarifying": "Answer briefly, return to the arc.",
    "Hostile": "Separate the number from the recommendation; acknowledge, route to "
               "appendix, hold the thread.",
    "Data is wrong": "Concede the figure if it is arguable, show the recommendation "
                     "survives the lower estimate, reconcile in the appendix.",
    "Off-topic": "Acknowledge, park it, redirect to the decision on the table.",
    "Unknown": "Say you do not have it, commit to a date. Never bluff a number.",
}

REQUIRED_TYPES = {"Hostile", "Data is wrong"}


def build_matrix(qa_bank: pd.DataFrame, min_rows: int = 4,
                 likelihood: tuple[str, ...] = ("High", "Medium")) -> pd.DataFrame:
    """Select the questions worth rehearsing and attach the technique to each."""
    m = qa_bank[qa_bank.likelihood.isin(likelihood)].copy()
    m["technique"] = m.question_type.map(TECHNIQUE).fillna(TECHNIQUE["Clarifying"])
    m = m[["qa_id", "question_type", "technique", "question", "model_answer",
           "bridge_back_to_big_idea", "appendix_reference", "likelihood"]]
    assert len(m) >= min_rows, f"rehearse at least {min_rows} questions"
    missing = REQUIRED_TYPES - set(m.question_type)
    assert not missing, f"the matrix must include: {missing}"
    return m.reset_index(drop=True)


def drill(matrix: pd.DataFrame, n: int | None = None) -> None:
    """Print the matrix as a rehearsal drill: acknowledge -> answer -> bridge."""
    rows = matrix if n is None else matrix.head(n)
    for i, item in enumerate(rows.itertuples(), 1):
        print(f"Q{i} [{item.question_type}] {item.question}")
        print(f"   technique : {item.technique}")
        print(f"   answer    : {item.model_answer}")
        print(f"   ->bridge  : ...{item.bridge_back_to_big_idea}")
        print(f"   appendix  : {item.appendix_reference}\n")


def unprepared_bridge(question: str, big_idea_clause: str) -> str:
    """Round 2 asks an UNPREPARED question. The shape of the answer is still fixed."""
    return (f"Acknowledge: \"That is a fair question.\"  "
            f"Answer briefly and honestly — if you do not know, say so and commit to a "
            f"date.  Bridge: \"...which is exactly why {big_idea_clause}\"")
