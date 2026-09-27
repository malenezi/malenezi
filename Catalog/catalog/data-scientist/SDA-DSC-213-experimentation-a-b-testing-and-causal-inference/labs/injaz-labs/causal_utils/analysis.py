"""
Correct effect estimation, variance, sequential peeking, and multiple testing.
Module 4 — Analysis Pitfalls: Peeking and Multiple Testing.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

__all__ = [
    "EffectEstimate", "two_proportion_test", "regression_effect",
    "delta_method_ratio", "peeking_simulation", "correct_pvalues",
    "always_valid_bound", "practical_significance_verdict",
]


@dataclass
class EffectEstimate:
    label: str
    estimate: float
    se: float
    ci_low: float
    ci_high: float
    p_value: float
    n_treatment: int
    n_control: int
    method: str

    def as_pp(self) -> str:
        return (f"{100*self.estimate:+.2f} pp "
                f"[{100*self.ci_low:+.2f}, {100*self.ci_high:+.2f}]")

    def __repr__(self) -> str:
        return (f"{self.label} ({self.method})\n"
                f"  effect : {self.as_pp()}   (95% CI)\n"
                f"  se     : {self.se:.5f}    p = {self.p_value:.4g}\n"
                f"  n      : treatment {self.n_treatment:,} / "
                f"control {self.n_control:,}")


def two_proportion_test(df: pd.DataFrame, outcome: str, group: str,
                        treated_label="treatment", alpha: float = 0.05,
                        label: str | None = None) -> EffectEstimate:
    """Unpooled-variance difference in proportions with a Wald interval.

    Note the deliberate asymmetry: the p-value uses the POOLED variance (the
    null says the two rates are equal, so pooling is right under H0), while
    the confidence interval uses the UNPOOLED variance (we are no longer
    assuming the null). Textbooks gloss over this; reviewers do not.
    """
    t = df.loc[df[group] == treated_label, outcome].dropna()
    c = df.loc[df[group] != treated_label, outcome].dropna()
    n1, n0 = len(t), len(c)
    p1, p0 = t.mean(), c.mean()
    diff = p1 - p0

    p_pool = (t.sum() + c.sum()) / (n1 + n0)
    se_pool = np.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n0))
    z = diff / se_pool
    pval = 2 * stats.norm.sf(abs(z))

    se_unpool = np.sqrt(p1 * (1 - p1) / n1 + p0 * (1 - p0) / n0)
    crit = stats.norm.ppf(1 - alpha / 2)
    return EffectEstimate(label or outcome, float(diff), float(se_unpool),
                          float(diff - crit * se_unpool),
                          float(diff + crit * se_unpool), float(pval),
                          n1, n0, "two-proportion z-test")


def regression_effect(df: pd.DataFrame, outcome: str, treatment: str,
                      covariates: list[str] | None = None,
                      cluster: str | None = None, cov_type: str = "HC3",
                      alpha: float = 0.05,
                      label: str | None = None) -> EffectEstimate:
    """OLS effect with robust (HC3) or cluster-robust standard errors.

    Two independent reasons to run the regression rather than the raw
    difference:
      * covariates measured BEFORE assignment reduce residual variance and
        therefore tighten the interval (they cannot bias a randomised
        comparison);
      * if the randomisation unit is coarser than the analysis row -- users
        randomised, sessions analysed -- the rows are not independent and a
        naive standard error is too small. Pass `cluster` and the interval
        widens to something honest.

    Never put a POST-treatment variable in `covariates`. That is Module 6's
    mediator trap and it will quietly destroy the estimate.
    """
    cols = [outcome, treatment] + (covariates or []) + ([cluster] if cluster else [])
    d = df[list(dict.fromkeys(cols))].dropna().copy()
    rhs = f"C({treatment})"
    if covariates:
        rhs += " + " + " + ".join(
            c if pd.api.types.is_numeric_dtype(d[c]) else f"C({c})"
            for c in covariates)
    model = smf.ols(f"{outcome} ~ {rhs}", data=d)
    if cluster:
        res = model.fit(cov_type="cluster", cov_kwds={"groups": d[cluster]})
        method = f"OLS + cluster-robust SE ({cluster})"
    else:
        res = model.fit(cov_type=cov_type)
        method = f"OLS + {cov_type} robust SE"

    term = next(t for t in res.params.index if t.startswith(f"C({treatment})"))
    est, se = float(res.params[term]), float(res.bse[term])
    crit = stats.norm.ppf(1 - alpha / 2)
    lvl = term.split("T.")[-1].rstrip("]")
    return EffectEstimate(label or outcome, est, se, est - crit * se,
                          est + crit * se, float(res.pvalues[term]),
                          int((d[treatment] == lvl).sum()),
                          int((d[treatment] != lvl).sum()), method)


def delta_method_ratio(numerator, denominator, group, treated_label="treatment",
                       alpha: float = 0.05, label: str = "ratio metric"
                       ) -> EffectEstimate:
    """Effect on a RATIO metric (e.g. completions per session) where the
    denominator is itself random.

    Treating a ratio as if the denominator were fixed understates the variance.
    The delta method propagates both:
        Var(X/Y) ~ (1/mu_y^2) Var(X) + (mu_x^2/mu_y^4) Var(Y)
                   - 2 (mu_x/mu_y^3) Cov(X, Y)
    """
    def ratio_and_var(x, y):
        n = len(x)
        mx, my = x.mean(), y.mean()
        vx, vy = x.var(ddof=1), y.var(ddof=1)
        cxy = np.cov(x, y, ddof=1)[0, 1]
        r = mx / my
        var = (vx / my**2 + mx**2 * vy / my**4 - 2 * mx * cxy / my**3) / n
        return r, var

    m = np.asarray(group) == treated_label
    num, den = np.asarray(numerator, float), np.asarray(denominator, float)
    r1, v1 = ratio_and_var(num[m], den[m])
    r0, v0 = ratio_and_var(num[~m], den[~m])
    diff, se = r1 - r0, np.sqrt(v1 + v0)
    crit = stats.norm.ppf(1 - alpha / 2)
    return EffectEstimate(label, float(diff), float(se), float(diff - crit*se),
                          float(diff + crit*se),
                          float(2 * stats.norm.sf(abs(diff / se))),
                          int(m.sum()), int((~m).sum()), "delta method")


def peeking_simulation(n_looks_grid=(1, 2, 5, 10, 20), n_per_arm: int = 5_000,
                       p: float = 0.55, n_experiments: int = 2_000,
                       alpha: float = 0.05, seed: int = 213) -> pd.DataFrame:
    """Simulate optional stopping under a TRUE NULL and count false positives.

    Every experiment here has zero effect. Any 'significant' result is a false
    positive. The only thing that changes across rows is how often you looked.
    """
    g = np.random.default_rng(seed)
    max_looks = max(n_looks_grid)
    rows = []
    a = g.binomial(1, p, size=(n_experiments, n_per_arm))
    b = g.binomial(1, p, size=(n_experiments, n_per_arm))
    ca, cb = np.cumsum(a, axis=1), np.cumsum(b, axis=1)

    for n_looks in n_looks_grid:
        idx = np.linspace(n_per_arm / n_looks, n_per_arm, n_looks).astype(int) - 1
        sig = np.zeros(n_experiments, dtype=bool)
        for i in idx:
            n = i + 1
            p1, p0 = ca[:, i] / n, cb[:, i] / n
            pp = (ca[:, i] + cb[:, i]) / (2 * n)
            se = np.sqrt(np.clip(pp * (1 - pp) * 2 / n, 1e-12, None))
            sig |= np.abs((p1 - p0) / se) > stats.norm.ppf(1 - alpha / 2)
        rows.append({"n_looks": n_looks,
                     "false_positive_rate": float(sig.mean()),
                     "inflation_vs_nominal": float(sig.mean() / alpha)})
    return pd.DataFrame(rows)


def correct_pvalues(pvalues, labels=None, method: str = "bh",
                    alpha: float = 0.05) -> pd.DataFrame:
    """Bonferroni (FWER) or Benjamini-Hochberg (FDR) correction.

    Choosing the family is a design decision, not a computation:
      * one pre-registered OEC            -> no correction;
      * a guardrail family (3-6 metrics)  -> Bonferroni, you want to be sure
                                             none is broken;
      * an exploratory sweep (segments)   -> BH, you can tolerate some false
                                             discoveries in a hypothesis list.
    """
    p = np.asarray(pvalues, dtype=float)
    labels = list(labels) if labels is not None else [f"test_{i+1}" for i in range(len(p))]
    m = len(p)
    if method.lower() in ("bonferroni", "bonf"):
        adj = np.minimum(p * m, 1.0)
    elif method.lower() in ("bh", "fdr"):
        order = np.argsort(p)
        ranked = p[order] * m / (np.arange(m) + 1)
        ranked = np.minimum.accumulate(ranked[::-1])[::-1]
        adj = np.empty(m); adj[order] = np.minimum(ranked, 1.0)
    else:
        raise ValueError("method must be 'bonferroni' or 'bh'")
    return pd.DataFrame({"metric": labels, "p_raw": p, "p_adjusted": adj,
                         "reject": adj < alpha, "family_size": m,
                         "method": method.upper()}).sort_values("p_raw")


def always_valid_bound(n, alpha: float = 0.05, rho: float = 1000.0) -> np.ndarray:
    """Mixture-sequential-probability-ratio confidence-sequence half-width
    multiplier -- a threshold you may look at as often as you like.

    The price of continuous monitoring is a wider interval early on. That is
    the honest trade: you cannot get unlimited looks for free.
    """
    n = np.asarray(n, dtype=float)
    return np.sqrt(2 * (n + rho) / n**2 * np.log(np.sqrt((n + rho) / rho) / alpha))


def practical_significance_verdict(est: EffectEstimate, threshold: float,
                                   metric_name: str = "effect") -> str:
    """Map a confidence interval onto a decision, not a p-value onto a verdict.

    Four cases, and only one of them is 'ship'.
    """
    lo, hi = est.ci_low, est.ci_high
    t = threshold
    if lo > t:
        v = "SHIP"
        why = f"the whole interval clears the {100*t:.1f} pp threshold"
    elif hi < 0:
        v = "STOP / ROLL BACK"
        why = "the whole interval is negative — this is a harm, not a null"
    elif lo > 0 and hi < t:
        v = "HOLD — real but too small"
        why = (f"positive and significant, but the whole interval sits below "
               f"the {100*t:.1f} pp threshold that justifies the build cost")
    elif lo > 0:
        v = "HOLD — extend or accept the risk"
        why = (f"significantly positive, but the interval straddles the "
               f"{100*t:.1f} pp threshold, so the data cannot yet tell you "
               f"whether the effect is worth shipping")
    else:
        v = "INCONCLUSIVE"
        why = ("the interval contains zero; report what effect sizes are "
               "still compatible with the data, not 'no effect'")
    return (f"{metric_name}: {est.as_pp()}  vs threshold {100*t:+.1f} pp\n"
            f"  VERDICT: {v}\n  because {why}.")
