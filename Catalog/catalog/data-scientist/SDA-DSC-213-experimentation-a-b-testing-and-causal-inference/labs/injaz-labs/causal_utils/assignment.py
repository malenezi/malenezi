"""
Assignment, sample-ratio mismatch, and covariate balance.
Module 2 — Experiment Design and Randomisation.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from scipy import stats

__all__ = [
    "hash_assign", "srm_check", "SRMResult",
    "standardised_mean_difference", "balance_table",
]


# ---------------------------------------------------------------- assignment

def hash_assign(unit_ids, salt: str, weights=(0.5, 0.5),
                arm_names=("control", "treatment")) -> np.ndarray:
    """Deterministic, stateless bucketing of units into arms.

    Why hashing rather than a random draw: the assignment must be reproducible
    from the unit id alone, identical in the analysis pipeline and in the
    serving layer, and stable if the same user returns tomorrow. Change the
    salt and you get a fresh, independent randomisation -- which is exactly
    what you want for the next experiment, and exactly what you must NOT do
    mid-flight.

    Parameters
    ----------
    unit_ids : array-like — the randomisation unit (user_id, region, ...).
    salt     : str        — experiment identifier. One salt per experiment.
    weights  : tuple      — allocation shares; must sum to 1.
    arm_names: tuple      — arm labels, same length as weights.
    """
    weights = np.asarray(weights, dtype=float)
    if not np.isclose(weights.sum(), 1.0):
        raise ValueError(f"weights must sum to 1, got {weights.sum()}")
    if len(weights) != len(arm_names):
        raise ValueError("weights and arm_names must be the same length")

    edges = np.cumsum(weights)
    out = np.empty(len(unit_ids), dtype=object)
    for i, uid in enumerate(np.asarray(unit_ids)):
        digest = hashlib.md5(f"{salt}:{uid}".encode()).hexdigest()
        # First 8 hex chars -> a uniform draw in [0, 1)
        u = int(digest[:8], 16) / 0xFFFFFFFF
        out[i] = arm_names[int(np.searchsorted(edges, u, side="right"))]
    return out


# ----------------------------------------------------------------------- SRM

@dataclass
class SRMResult:
    observed: dict
    expected: dict
    chi2: float
    p_value: float
    passed: bool

    def __repr__(self) -> str:
        verdict = "PASS" if self.passed else "*** SRM — EXPERIMENT INVALID ***"
        lines = [f"Sample Ratio Mismatch check: {verdict}",
                 f"  chi2 = {self.chi2:,.2f}   p = {self.p_value:.3g}"]
        for arm in self.observed:
            o, e = self.observed[arm], self.expected[arm]
            lines.append(f"  {arm:<12} observed {o:>8,}   expected {e:>10,.0f} "
                         f"  ({100 * (o / e - 1):+.2f}%)")
        return "\n".join(lines)


def srm_check(variant: pd.Series, expected_weights: dict | None = None,
              alpha: float = 0.001) -> SRMResult:
    """Chi-square test that arm sizes match the planned allocation.

    A failed SRM does not mean 'adjust and continue'. It means some units were
    lost or misassigned non-randomly, so the comparison is no longer a
    randomised one. The correct response is to find the bug and rerun.

    alpha defaults to 0.001, not 0.05: with millions of units, tiny harmless
    deviations trip a 5% threshold, and a real SRM is usually catastrophic
    enough to blow past 0.001 anyway.
    """
    counts = variant.value_counts()
    arms = list(counts.index)
    if expected_weights is None:
        expected_weights = {a: 1 / len(arms) for a in arms}
    total = counts.sum()
    exp = np.array([expected_weights[a] * total for a in arms])
    obs = counts.reindex(arms).to_numpy(dtype=float)
    chi2 = float(((obs - exp) ** 2 / exp).sum())
    p = float(stats.chi2.sf(chi2, df=len(arms) - 1))
    return SRMResult(
        observed={a: int(o) for a, o in zip(arms, obs)},
        expected={a: float(e) for a, e in zip(arms, exp)},
        chi2=chi2, p_value=p, passed=bool(p >= alpha),
    )


# ------------------------------------------------------------------- balance

def standardised_mean_difference(x: pd.Series, group: pd.Series,
                                 treated_label) -> float:
    """SMD = (mean_t - mean_c) / pooled sd. Scale-free, so |SMD| < 0.1 is the
    conventional 'balanced' threshold for any covariate."""
    t = pd.to_numeric(x[group == treated_label], errors="coerce").dropna()
    c = pd.to_numeric(x[group != treated_label], errors="coerce").dropna()
    if len(t) < 2 or len(c) < 2:
        return np.nan
    pooled = np.sqrt((t.var(ddof=1) + c.var(ddof=1)) / 2)
    if pooled == 0:
        return 0.0
    return float((t.mean() - c.mean()) / pooled)


def balance_table(df: pd.DataFrame, group_col: str, covariates: list[str],
                  treated_label="treatment", threshold: float = 0.10) -> pd.DataFrame:
    """One row per covariate: group means, SMD, and a pass flag.

    Categorical covariates are expanded into one indicator per level, because
    'region is balanced' is not a single number -- each region must be.
    """
    rows = []
    for col in covariates:
        s = df[col]
        if not pd.api.types.is_numeric_dtype(s):
            for level in sorted(s.dropna().unique()):
                ind = (s == level).astype(float)
                rows.append(_balance_row(f"{col}={level}", ind, df[group_col],
                                         treated_label, threshold))
        else:
            rows.append(_balance_row(col, s, df[group_col], treated_label, threshold))
    out = pd.DataFrame(rows)
    return out.sort_values("abs_smd", ascending=False).reset_index(drop=True)


def _balance_row(name, series, group, treated_label, threshold):
    smd = standardised_mean_difference(series, group, treated_label)
    t = pd.to_numeric(series[group == treated_label], errors="coerce")
    c = pd.to_numeric(series[group != treated_label], errors="coerce")
    return {
        "covariate": name,
        "mean_treatment": float(t.mean()),
        "mean_control": float(c.mean()),
        "smd": smd,
        "abs_smd": abs(smd),
        "balanced": bool(abs(smd) < threshold),
    }
