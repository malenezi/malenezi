"""
Power, minimum detectable effect, sample sizing, run length, and CUPED.
Module 3 — Power Analysis and Sample Sizing.

Everything here is written closed-form first so participants can see the
machinery, with a statsmodels cross-check available in the labs. If the two
disagree, one of them is wrong and you must find out which -- that is the
exercise.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import stats

__all__ = [
    "sample_size_proportions", "sample_size_means", "power_for_n",
    "mde_for_n", "RunLengthPlan", "run_length", "cuped_adjust", "CupedResult",
]


def _z(alpha: float, power: float, two_sided: bool = True):
    z_a = stats.norm.ppf(1 - alpha / (2 if two_sided else 1))
    z_b = stats.norm.ppf(power)
    return z_a, z_b


# ------------------------------------------------------------------- sizing

def sample_size_proportions(p_baseline: float, mde_absolute: float,
                            alpha: float = 0.05, power: float = 0.80,
                            two_sided: bool = True, ratio: float = 1.0) -> int:
    """Required sample size PER ARM for a difference in proportions.

    n = (z_{a/2} sqrt(2 p_bar q_bar) + z_b sqrt(p1 q1 + p2 q2))^2 / delta^2

    `ratio` = n_control / n_treatment, for unequal allocation.
    Returns the TREATMENT arm size; multiply by `ratio` for control.
    """
    if mde_absolute <= 0:
        raise ValueError("mde_absolute must be > 0")
    p1, p2 = p_baseline, p_baseline + mde_absolute
    if not (0 < p2 < 1):
        raise ValueError(f"baseline + MDE = {p2:.3f} is outside (0, 1)")
    z_a, z_b = _z(alpha, power, two_sided)
    p_bar = (p1 + p2) / 2          # pooled rate under the alternative
    term = (z_a * np.sqrt((1 + 1 / ratio) * p_bar * (1 - p_bar))
            + z_b * np.sqrt(p1 * (1 - p1) / ratio + p2 * (1 - p2)))
    return int(np.ceil(term ** 2 / mde_absolute ** 2))


def sample_size_means(sd: float, mde_absolute: float, alpha: float = 0.05,
                      power: float = 0.80, two_sided: bool = True) -> int:
    """Required sample size PER ARM for a difference in means.
    n = 2 sd^2 (z_{a/2} + z_b)^2 / delta^2"""
    z_a, z_b = _z(alpha, power, two_sided)
    return int(np.ceil(2 * sd ** 2 * (z_a + z_b) ** 2 / mde_absolute ** 2))


def power_for_n(n_per_arm: int, p_baseline: float, effect_absolute: float,
                alpha: float = 0.05, two_sided: bool = True) -> float:
    """Probability of detecting `effect_absolute` with `n_per_arm` per arm.

    Power is not a property of an experiment. It is a property of an
    experiment *against a specific effect size*. 'This test is 80% powered'
    is an incomplete sentence.
    """
    p1, p2 = p_baseline, p_baseline + effect_absolute
    se = np.sqrt(p1 * (1 - p1) / n_per_arm + p2 * (1 - p2) / n_per_arm)
    z_a = stats.norm.ppf(1 - alpha / (2 if two_sided else 1))
    return float(stats.norm.cdf(abs(effect_absolute) / se - z_a))


def mde_for_n(n_per_arm: int, p_baseline: float, alpha: float = 0.05,
              power: float = 0.80, two_sided: bool = True) -> float:
    """The smallest effect this sample can reliably detect.

    Ask this BEFORE running, not after a null result. 'We found no effect'
    and 'we could never have found this effect' are different sentences.
    """
    z_a, z_b = _z(alpha, power, two_sided)
    se_unit = np.sqrt(2 * p_baseline * (1 - p_baseline) / n_per_arm)
    return float((z_a + z_b) * se_unit)


# --------------------------------------------------------------- run length

@dataclass
class RunLengthPlan:
    n_per_arm: int
    n_arms: int
    total_units_needed: int
    daily_eligible: float
    trigger_rate: float
    daily_usable: float
    days_required: int
    days_recommended: int
    floor_days: int

    def __repr__(self) -> str:
        return (
            "Run-length plan\n"
            f"  required per arm      : {self.n_per_arm:,}\n"
            f"  arms                  : {self.n_arms}\n"
            f"  total units needed    : {self.total_units_needed:,}\n"
            f"  daily eligible        : {self.daily_eligible:,.0f}\n"
            f"  trigger rate          : {self.trigger_rate:.1%}\n"
            f"  daily usable units    : {self.daily_usable:,.0f}\n"
            f"  days by arithmetic    : {self.days_required}\n"
            f"  weekly-cycle floor    : {self.floor_days}\n"
            f"  ==> RUN FOR           : {self.days_recommended} days"
        )


def run_length(n_per_arm: int, daily_eligible: float, trigger_rate: float,
               n_arms: int = 2, floor_days: int = 7) -> RunLengthPlan:
    """Turn a sample size into a calendar commitment.

    Three things bite teams here, all of them handled below:
      1. n is PER ARM -- multiply by the number of arms;
      2. not every eligible user reaches the changed step (trigger rate);
      3. a whole number of weeks is a floor, because weekday and weekend
         users are different people. Stopping on a Thursday because the
         maths said 5.2 days samples a biased slice of your population.
    """
    total = n_per_arm * n_arms
    usable = daily_eligible * trigger_rate
    days = int(np.ceil(total / usable))
    recommended = max(days, floor_days)
    if recommended % 7:
        recommended += 7 - (recommended % 7)      # round up to whole weeks
    return RunLengthPlan(n_per_arm, n_arms, total, daily_eligible, trigger_rate,
                         usable, days, recommended, floor_days)


# ------------------------------------------------------------------- CUPED

@dataclass
class CupedResult:
    theta: float
    variance_before: float
    variance_after: float
    variance_reduction: float
    correlation: float
    effective_n_multiplier: float
    y_adjusted: np.ndarray

    def __repr__(self) -> str:
        return (
            "CUPED variance reduction\n"
            f"  corr(pre, post)      : {self.correlation:.3f}\n"
            f"  theta                : {self.theta:.4f}\n"
            f"  variance before/after: {self.variance_before:.5f} -> "
            f"{self.variance_after:.5f}\n"
            f"  variance reduction   : {self.variance_reduction:.1%}\n"
            f"  equivalent to        : {self.effective_n_multiplier:.2f}x the sample"
        )


def cuped_adjust(y, x_pre) -> CupedResult:
    """Controlled-experiment Using Pre-Experiment Data.

    Y_cuped = Y - theta (X_pre - mean(X_pre)),  theta = cov(Y, X)/var(X)

    The adjustment is UNBIASED for the treatment effect provided X_pre is
    measured before assignment and therefore cannot be affected by treatment.
    That single condition is the whole safety argument: never CUPED on a
    post-treatment covariate.

    Variance falls by rho^2, so a covariate correlated 0.4 with the outcome
    buys ~16% -- worth roughly a 16% shorter experiment, for free.
    """
    y = np.asarray(y, dtype=float)
    x = np.asarray(x_pre, dtype=float)
    mask = ~(np.isnan(y) | np.isnan(x))
    y, x = y[mask], x[mask]
    theta = float(np.cov(y, x, ddof=1)[0, 1] / np.var(x, ddof=1))
    y_adj = y - theta * (x - x.mean())
    v0, v1 = float(np.var(y, ddof=1)), float(np.var(y_adj, ddof=1))
    rho = float(np.corrcoef(y, x)[0, 1])
    return CupedResult(theta, v0, v1, 1 - v1 / v0, rho, v0 / v1, y_adj)
