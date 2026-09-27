"""The shared evaluation harness — one function, every model, same folds.

Every number on the course scoreboard comes from evaluate() on the shared
CV object, or it does not go on the scoreboard. That is what keeps model
comparisons legal across pairs and across days.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_validate

RANDOM_STATE = 42
CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
SCORING = {"pr_auc": "average_precision", "roc_auc": "roc_auc", "recall": "recall"}


def evaluate(pipeline, X, y, name: str) -> pd.Series:
    """Cross-validate a FULL pipeline (preprocessing refits per fold — M3's guarantee)."""
    res = cross_validate(pipeline, X, y, cv=CV, scoring=SCORING, n_jobs=-1)
    row = {f"{m}_mean": res[f"test_{m}"].mean() for m in SCORING}
    row |= {f"{m}_std": res[f"test_{m}"].std() for m in SCORING}
    return pd.Series(row, name=name).round(3)


def recall_at_budget(y_true, proba, budget: float = 0.20) -> float:
    """Recall among the top `budget` share of customers ranked by predicted risk.

    The framing-canvas metric: the CRM voucher budget covers 20% of the base.
    """
    y_true = np.asarray(y_true)
    proba = np.asarray(proba)
    n = int(budget * len(y_true))
    top = np.argsort(-proba)[:n]
    return float(y_true[top].sum() / y_true.sum())


def precision_at_budget(y_true, proba, budget: float = 0.20) -> float:
    y_true = np.asarray(y_true)
    proba = np.asarray(proba)
    n = int(budget * len(y_true))
    top = np.argsort(-proba)[:n]
    return float(y_true[top].mean())


def shuffled_label_test(pipeline, X, y, cv=None, seed: int = RANDOM_STATE) -> float:
    """If shuffled labels score above chance, something leaks.

    Returns mean PR-AUC under label permutation; honest ⇒ ≈ base rate (0.14).
    """
    from sklearn.model_selection import cross_val_score
    rng = np.random.default_rng(seed)
    y_shuffled = pd.Series(rng.permutation(np.asarray(y)), index=X.index)
    return float(cross_val_score(pipeline, X, y_shuffled, cv=cv or CV,
                                 scoring="average_precision", n_jobs=-1).mean())
