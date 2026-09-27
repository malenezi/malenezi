"""
Quasi-experimental estimators: propensity scores, matching, IPW,
difference-in-differences, event studies, instrumental variables,
and sensitivity analysis.
Module 5 — When You Cannot Randomise.

Every estimator here buys identification with an ASSUMPTION rather than a
coin flip. Each function's docstring names the assumption it is spending and
what would break it, because that sentence -- not the point estimate -- is
what a reviewer will ask you for.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from .assignment import balance_table

__all__ = [
    "estimate_propensity", "match_nearest", "MatchResult", "ipw_ate",
    "did_twfe", "DiDResult", "event_study", "iv_2sls", "IVResult",
    "rosenbaum_bounds", "placebo_outcome_test", "random_common_cause_test",
    "subset_refutation",
]


# ------------------------------------------------------- propensity scores

def estimate_propensity(df: pd.DataFrame, treatment: str,
                        covariates: list[str], trim: float = 0.01) -> pd.Series:
    """P(T=1 | X) by logistic regression on standardised covariates.

    The propensity model is NOT judged by its AUC. A model that predicts
    treatment perfectly is a disaster: it means there is no overlap, and no
    treated unit has a comparable control. Judge it by the BALANCE it buys
    (see `match_nearest`) and by the overlap of the two score distributions.
    """
    X = pd.get_dummies(df[covariates], drop_first=True).astype(float)
    Xs = StandardScaler().fit_transform(X)
    lr = LogisticRegression(max_iter=2000, C=1.0)
    lr.fit(Xs, df[treatment].astype(int))
    e = lr.predict_proba(Xs)[:, 1]
    return pd.Series(np.clip(e, trim, 1 - trim), index=df.index, name="propensity")


@dataclass
class MatchResult:
    att: float
    se: float
    ci_low: float
    ci_high: float
    n_treated_matched: int
    n_treated_total: int
    caliper: float
    matched: pd.DataFrame
    balance_before: pd.DataFrame
    balance_after: pd.DataFrame

    @property
    def worst_smd_after(self) -> float:
        return float(self.balance_after["abs_smd"].max())

    def __repr__(self) -> str:
        return (
            "Propensity-score matching (ATT)\n"
            f"  ATT            : {100*self.att:+.2f} pp "
            f"[{100*self.ci_low:+.2f}, {100*self.ci_high:+.2f}]\n"
            f"  matched treated: {self.n_treated_matched:,} / "
            f"{self.n_treated_total:,} (caliper {self.caliper})\n"
            f"  worst |SMD| before -> after: "
            f"{self.balance_before['abs_smd'].max():.3f} -> "
            f"{self.worst_smd_after:.3f}"
        )


def match_nearest(df: pd.DataFrame, treatment: str, outcome: str,
                  covariates: list[str], caliper: float = 0.05,
                  with_replacement: bool = True, alpha: float = 0.05,
                  propensity: pd.Series | None = None) -> MatchResult:
    """Nearest-neighbour matching on the propensity score, estimating the ATT.

    ASSUMPTION SPENT — unconfoundedness given X: among users with the same
    propensity score, enrolling is as good as random. Nothing in the data can
    verify this. What CAN be checked, and must be reported, is (a) overlap,
    (b) post-matching balance, and (c) how strong a hidden confounder would
    have to be to overturn the result (`rosenbaum_bounds`).

    Unmatched treated units are DROPPED and counted. If many are dropped, the
    estimand has quietly changed to 'the ATT among matchable treated units'
    and the memo must say so.
    """
    d = df[[treatment, outcome] + covariates].dropna().copy()
    e = estimate_propensity(d, treatment, covariates) if propensity is None \
        else propensity.loc[d.index]
    d["_ps"] = e

    bal_before = balance_table(d.assign(_g=np.where(d[treatment] == 1, "treatment", "control")),
                               "_g", covariates)

    treated = d[d[treatment] == 1]
    control = d[d[treatment] == 0].sort_values("_ps")
    c_ps = control["_ps"].to_numpy()
    c_idx = control.index.to_numpy()

    pairs, used = [], set()
    for ti, ps in treated["_ps"].items():
        j = np.searchsorted(c_ps, ps)
        best, best_d = None, np.inf
        for k in range(max(0, j - 25), min(len(c_ps), j + 25)):
            if (not with_replacement) and c_idx[k] in used:
                continue
            dist = abs(c_ps[k] - ps)
            if dist < best_d:
                best, best_d = k, dist
        if best is not None and best_d <= caliper:
            pairs.append((ti, c_idx[best], best_d))
            used.add(c_idx[best])

    if not pairs:
        raise RuntimeError("No matches within the caliper — check overlap.")

    ti_idx = [p[0] for p in pairs]
    ci_idx = [p[1] for p in pairs]
    y_t = d.loc[ti_idx, outcome].to_numpy(dtype=float)
    y_c = d.loc[ci_idx, outcome].to_numpy(dtype=float)
    diff = y_t - y_c
    att = float(diff.mean())
    se = float(diff.std(ddof=1) / np.sqrt(len(diff)))   # paired SE
    crit = stats.norm.ppf(1 - alpha / 2)

    matched = pd.concat([
        d.loc[ti_idx].assign(_pair=range(len(pairs)), _role="treated"),
        d.loc[ci_idx].assign(_pair=range(len(pairs)), _role="control"),
    ])
    bal_after = balance_table(
        matched.assign(_g=np.where(matched["_role"] == "treated", "treatment", "control")),
        "_g", covariates)

    return MatchResult(att, se, att - crit * se, att + crit * se,
                       len(pairs), int(len(treated)), caliper,
                       matched, bal_before, bal_after)


def ipw_ate(df: pd.DataFrame, treatment: str, outcome: str,
            covariates: list[str], stabilised: bool = True,
            alpha: float = 0.05) -> dict:
    """Inverse-probability weighting: reweight the sample so treated and
    control look alike on X, then take the difference in weighted means.

    Uses every unit rather than discarding unmatched ones, at the cost of
    being sensitive to extreme weights. Always inspect the maximum weight:
    if one unit carries 5% of the estimate, the estimate is that unit.
    """
    d = df[[treatment, outcome] + covariates].dropna().copy()
    e = estimate_propensity(d, treatment, covariates).to_numpy()
    t = d[treatment].to_numpy(dtype=float)
    y = d[outcome].to_numpy(dtype=float)
    w = t / e + (1 - t) / (1 - e)
    if stabilised:
        w = np.where(t == 1, t * t.mean() / e, (1 - t) * (1 - t.mean()) / (1 - e))
    m1 = np.average(y[t == 1], weights=w[t == 1])
    m0 = np.average(y[t == 0], weights=w[t == 0])
    ate = float(m1 - m0)
    # Sandwich-free approximation: weighted regression gives a usable SE
    res = sm.WLS(y, sm.add_constant(t), weights=w).fit(cov_type="HC3")
    se = float(res.bse[1])
    crit = stats.norm.ppf(1 - alpha / 2)
    return {"ate": ate, "se": se, "ci_low": ate - crit*se, "ci_high": ate + crit*se,
            "max_weight_share": float(w.max() / w.sum()),
            "effective_sample_size": float(w.sum() ** 2 / (w ** 2).sum())}


# ------------------------------------------------- difference-in-differences

@dataclass
class DiDResult:
    att: float
    se: float
    ci_low: float
    ci_high: float
    p_value: float
    n_obs: int
    n_units: int
    model: object = field(repr=False, default=None)

    def __repr__(self) -> str:
        return ("Difference-in-differences (TWFE)\n"
                f"  ATT : {100*self.att:+.2f} pp "
                f"[{100*self.ci_low:+.2f}, {100*self.ci_high:+.2f}]\n"
                f"  se  : {self.se:.5f}   p = {self.p_value:.4g}\n"
                f"  {self.n_obs:,} observations across {self.n_units} units")


def did_twfe(panel: pd.DataFrame, outcome: str, unit: str, time: str,
             treated_post: str, alpha: float = 0.05,
             cluster_by_unit: bool = True) -> DiDResult:
    """Two-way fixed-effects difference-in-differences.

    ASSUMPTION SPENT — parallel trends: absent the programme, treated and
    control units' outcomes would have moved in parallel. Untestable for the
    post period by construction. What you CAN do, and must, is show the
    pre-period was parallel (`event_study`).

    WARNING for staggered rollouts: with variation in treatment TIMING and
    effects that change over time, the TWFE coefficient is a weighted average
    of 2x2 comparisons that can include already-treated units as 'controls',
    and some weights can be negative. Report TWFE, then check it against a
    cohort-aware estimator (Callaway-Sant'Anna, Sun-Abraham) before you
    defend the number.

    Standard errors are clustered on the unit by default: outcomes within a
    region are correlated across months, and pretending otherwise produces a
    confidence interval that is far too narrow.
    """
    d = panel[[outcome, unit, time, treated_post]].dropna().copy()
    model = smf.ols(f"{outcome} ~ {treated_post} + C({unit}) + C({time})", data=d)
    if cluster_by_unit:
        res = model.fit(cov_type="cluster", cov_kwds={"groups": d[unit]})
    else:
        res = model.fit(cov_type="HC3")
    est, se = float(res.params[treated_post]), float(res.bse[treated_post])
    crit = stats.norm.ppf(1 - alpha / 2)
    return DiDResult(est, se, est - crit*se, est + crit*se,
                     float(res.pvalues[treated_post]), len(d),
                     int(d[unit].nunique()), res)


def event_study(panel: pd.DataFrame, outcome: str, unit: str, time: str,
                rel_time: str, baseline: int = -1, window=(-6, 8),
                alpha: float = 0.05) -> pd.DataFrame:
    """Coefficients by time relative to activation — the parallel-trends exhibit.

    Read it in this order:
      1. Are the PRE-period coefficients flat and centred on zero? If not,
         parallel trends is already contradicted and the DiD number is not
         a causal estimate, whatever its p-value.
      2. Does the effect appear AT activation, not before it?
      3. Does it persist, ramp, or decay? That shapes the scaling decision
         as much as the average does.

    Never-treated units contribute to identification but have no relative
    time; they are pooled into the omitted baseline.
    """
    d = panel.copy()
    d[rel_time] = pd.to_numeric(d[rel_time], errors="coerce")
    lo, hi = window
    d["_rel"] = d[rel_time].clip(lo, hi)
    d["_rel"] = d["_rel"].fillna(baseline)         # never-treated -> baseline
    d["_rel"] = d["_rel"].astype(int)

    res = smf.ols(
        f"{outcome} ~ C(_rel, Treatment(reference={baseline})) + C({unit}) + C({time})",
        data=d).fit(cov_type="cluster", cov_kwds={"groups": d[unit]})

    crit = stats.norm.ppf(1 - alpha / 2)
    rows = [{"rel_time": baseline, "coef": 0.0, "se": 0.0,
             "ci_low": 0.0, "ci_high": 0.0, "is_baseline": True,
             "period": "pre"}]
    for term in res.params.index:
        if not term.startswith("C(_rel"):
            continue
        r = int(term.split("T.")[-1].rstrip("]"))
        b, s = float(res.params[term]), float(res.bse[term])
        rows.append({"rel_time": r, "coef": b, "se": s,
                     "ci_low": b - crit*s, "ci_high": b + crit*s,
                     "is_baseline": False, "period": "pre" if r < 0 else "post"})
    return pd.DataFrame(rows).sort_values("rel_time").reset_index(drop=True)


# ------------------------------------------------- instrumental variables

@dataclass
class IVResult:
    late: float
    se: float
    ci_low: float
    ci_high: float
    first_stage_coef: float
    first_stage_F: float
    ols_estimate: float

    @property
    def weak(self) -> bool:
        return self.first_stage_F < 10

    def __repr__(self) -> str:
        flag = "  *** WEAK INSTRUMENT (F < 10) ***" if self.weak else ""
        return ("Instrumental variables (2SLS)\n"
                f"  LATE          : {100*self.late:+.2f} pp "
                f"[{100*self.ci_low:+.2f}, {100*self.ci_high:+.2f}]\n"
                f"  OLS (biased)  : {100*self.ols_estimate:+.2f} pp\n"
                f"  first stage   : coef {self.first_stage_coef:+.4f}   "
                f"F = {self.first_stage_F:,.1f}{flag}")


def iv_2sls(df: pd.DataFrame, outcome: str, endogenous: str, instrument: str,
            exog: list[str] | None = None, alpha: float = 0.05) -> IVResult:
    """Two-stage least squares with correct (second-stage-corrected) SEs.

    THREE CONDITIONS, and a defence is needed for each:
      1. RELEVANCE   — the instrument moves the treatment. Testable: first-
                       stage F > 10 (and really > 30 for comfort).
      2. EXCLUSION   — the instrument affects the outcome ONLY through the
                       treatment. NOT testable. This is where instruments die.
      3. INDEPENDENCE— the instrument is as-good-as-randomly assigned with
                       respect to unobservables.

    What you recover is the LATE: the effect among COMPLIERS -- units whose
    treatment status the instrument actually changed. That is a different
    population from the ATE, and the memo must name it.
    """
    exog = exog or []
    d = df[[outcome, endogenous, instrument] + exog].dropna().copy()
    Xe = pd.get_dummies(d[exog], drop_first=True).astype(float) if exog else pd.DataFrame(index=d.index)

    # First stage
    Z = sm.add_constant(pd.concat([d[[instrument]], Xe], axis=1).astype(float))
    fs = sm.OLS(d[endogenous].astype(float), Z).fit(cov_type="HC3")
    d_hat = fs.fittedvalues
    F = float(fs.tvalues[instrument] ** 2)

    # Second stage with the fitted treatment
    X2 = sm.add_constant(pd.concat([pd.Series(d_hat, name=endogenous), Xe], axis=1).astype(float))
    ss = sm.OLS(d[outcome].astype(float), X2).fit()
    beta = float(ss.params[endogenous])

    # Correct the residual variance: use ACTUAL, not fitted, treatment
    Xa = sm.add_constant(pd.concat([d[[endogenous]], Xe], axis=1).astype(float))
    resid = d[outcome].to_numpy(float) - Xa.to_numpy(float) @ ss.params.to_numpy(float)
    sigma2 = (resid ** 2).sum() / (len(d) - X2.shape[1])
    XtX_inv = np.linalg.pinv(X2.to_numpy(float).T @ X2.to_numpy(float))
    pos = list(X2.columns).index(endogenous)
    se = float(np.sqrt(sigma2 * XtX_inv[pos, pos]))

    ols = sm.OLS(d[outcome].astype(float), Xa).fit(cov_type="HC3")
    crit = stats.norm.ppf(1 - alpha / 2)
    return IVResult(beta, se, beta - crit*se, beta + crit*se,
                    float(fs.params[instrument]), F,
                    float(ols.params[endogenous]))


# --------------------------------------------------- sensitivity / refutation

def rosenbaum_bounds(matched: pd.DataFrame, outcome: str, role_col: str = "_role",
                     pair_col: str = "_pair",
                     gammas=(1.0, 1.1, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0)) -> pd.DataFrame:
    """How strong would a hidden confounder have to be to overturn the result?

    Gamma is the odds ratio by which an unobserved variable could change a
    unit's odds of being treated. Gamma = 1 is the unconfoundedness
    assumption. The reported number is the upper-bound p-value at each Gamma.

    Read the output as one sentence for the memo: 'the conclusion survives an
    unmeasured confounder that changes the odds of enrolling by up to
    Gamma-star; a confounder stronger than that would overturn it.' If
    Gamma-star is 1.1, the finding is fragile and should be presented as such.
    """
    w = matched.pivot_table(index=pair_col, columns=role_col, values=outcome,
                            aggfunc="first")
    if not {"treated", "control"} <= set(w.columns):
        raise ValueError("matched frame must contain 'treated' and 'control' roles")
    d = (w["treated"] - w["control"]).dropna()
    d = d[d != 0]                       # discordant pairs only (McNemar-style)
    n = len(d)
    s = int((d > 0).sum())
    rows = []
    for gmm in gammas:
        p_plus = gmm / (1 + gmm)
        p_upper = float(stats.binom.sf(s - 1, n, p_plus))
        p_lower = float(stats.binom.sf(s - 1, n, 1 / (1 + gmm)))
        rows.append({"gamma": gmm, "p_upper_bound": p_upper,
                     "p_lower_bound": p_lower,
                     "still_significant_at_05": p_upper < 0.05})
    return pd.DataFrame(rows)


def placebo_outcome_test(df: pd.DataFrame, treatment: str, placebo_outcome: str,
                         covariates: list[str]) -> dict:
    """Re-run the analysis on an outcome the treatment CANNOT have caused.
    A non-zero 'effect' means the design, not the treatment, is producing
    the number."""
    res = smf.ols(
        f"{placebo_outcome} ~ {treatment} + " +
        " + ".join(c if pd.api.types.is_numeric_dtype(df[c]) else f"C({c})"
                   for c in covariates),
        data=df).fit(cov_type="HC3")
    return {"placebo_effect": float(res.params[treatment]),
            "p_value": float(res.pvalues[treatment]),
            "passes": bool(res.pvalues[treatment] > 0.05)}


def random_common_cause_test(df: pd.DataFrame, treatment: str, outcome: str,
                             covariates: list[str], n_sims: int = 20,
                             seed: int = 213) -> dict:
    """Add an irrelevant random covariate and re-estimate. A stable estimate
    is weak but necessary evidence that the model is not chasing noise."""
    g = np.random.default_rng(seed)
    base = smf.ols(f"{outcome} ~ {treatment} + " + " + ".join(
        c if pd.api.types.is_numeric_dtype(df[c]) else f"C({c})" for c in covariates),
        data=df).fit()
    ests = []
    for _ in range(n_sims):
        d = df.copy()
        d["_rcc"] = g.normal(size=len(d))
        r = smf.ols(f"{outcome} ~ {treatment} + _rcc + " + " + ".join(
            c if pd.api.types.is_numeric_dtype(df[c]) else f"C({c})" for c in covariates),
            data=d).fit()
        ests.append(float(r.params[treatment]))
    base_est = float(base.params[treatment])
    return {"original": base_est, "mean_with_random_cause": float(np.mean(ests)),
            "max_abs_shift": float(np.max(np.abs(np.array(ests) - base_est))),
            "passes": bool(np.max(np.abs(np.array(ests) - base_est)) < 0.1 * abs(base_est) + 1e-4)}


def subset_refutation(df: pd.DataFrame, treatment: str, outcome: str,
                      covariates: list[str], frac: float = 0.7,
                      n_sims: int = 20, seed: int = 213) -> dict:
    """Re-estimate on random subsets. A conclusion that only exists in the
    full sample is a conclusion about one slice of it."""
    g = np.random.default_rng(seed)
    rhs = " + ".join(c if pd.api.types.is_numeric_dtype(df[c]) else f"C({c})"
                     for c in covariates)
    ests = []
    for _ in range(n_sims):
        d = df.sample(frac=frac, random_state=int(g.integers(1e6)))
        ests.append(float(smf.ols(f"{outcome} ~ {treatment} + {rhs}", data=d)
                          .fit().params[treatment]))
    full = float(smf.ols(f"{outcome} ~ {treatment} + {rhs}", data=df)
                 .fit().params[treatment])
    return {"original": full, "subset_mean": float(np.mean(ests)),
            "subset_sd": float(np.std(ests, ddof=1)),
            "passes": bool(abs(np.mean(ests) - full) < 0.15 * abs(full) + 1e-4)}
