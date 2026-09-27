"""
From estimate to decision: frozen analysis plans, decision plots, memos.
Module 7 — Experimentation Case Study.

The last mile is where good analysis dies. A correct estimate delivered as a
p-value to a director who needed a range and a recommendation has failed.
"""
from __future__ import annotations

import json
import textwrap
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone

import numpy as np

__all__ = ["AnalysisPlan", "freeze_plan", "decision_plot", "forest_plot",
           "decision_memo"]


# ------------------------------------------------------- the frozen plan

@dataclass
class AnalysisPlan:
    """Everything you must commit to BEFORE looking at outcomes.

    The freeze is the whole point. Metrics chosen after seeing the data are
    not metrics, they are conclusions with a p-value stapled on. Write this
    object, hash it, commit the hash, and put the hash in the memo.
    """
    experiment_name: str
    decision: str
    randomisation_unit: str
    oec: str
    guardrails: list[str]
    trigger_definition: str
    unit_of_analysis: str
    mde: float
    alpha: float = 0.05
    power: float = 0.80
    planned_n_per_arm: int | None = None
    planned_run_days: int | None = None
    correction_family: str = "bonferroni for guardrails; none for the OEC"
    stopping_rule: str = "fixed horizon; no interim stopping for significance"
    practical_threshold: float = 0.01
    frozen_at: str | None = None
    plan_hash: str | None = None

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True)


def freeze_plan(plan: AnalysisPlan) -> AnalysisPlan:
    """Stamp and hash the plan. Run this BEFORE the analysis cell, and put
    `plan.plan_hash` in the memo so a reader can verify nothing moved."""
    import hashlib
    plan.frozen_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    body = json.dumps({k: v for k, v in asdict(plan).items()
                       if k != "plan_hash"}, sort_keys=True)
    plan.plan_hash = hashlib.sha256(body.encode()).hexdigest()[:16]
    print(f"Analysis plan FROZEN at {plan.frozen_at}\n  hash: {plan.plan_hash}")
    return plan


# ------------------------------------------------------------- the visuals

def decision_plot(estimates, threshold: float = 0.01, ax=None,
                  title: str = "Effect vs the decision threshold",
                  xlabel: str = "Effect on completion rate (percentage points)"):
    """The single chart a decision-maker needs.

    `estimates` is a list of objects with .label, .estimate, .ci_low, .ci_high
    (any EffectEstimate / DiDResult works, or a dict with those keys).

    Three reference marks do the work: zero (is there an effect at all),
    the threshold (is it big enough to be worth it), and the interval
    (how sure are we). A point estimate alone answers none of these.
    """
    import matplotlib.pyplot as plt
    from .style import NAVY, BLUE, ORANGE, TEAL, SLATE, MUTED, PANEL, GREEN, RED

    def unpack(e):
        if isinstance(e, dict):
            return e["label"], e["estimate"], e["ci_low"], e["ci_high"]
        return (getattr(e, "label", getattr(e, "name", "effect")),
                getattr(e, "estimate", getattr(e, "att", None)),
                e.ci_low, e.ci_high)

    rows = [unpack(e) for e in estimates]
    n = len(rows)
    if ax is None:
        _, ax = plt.subplots(figsize=(9, 0.72 * n + 1.9))

    span = max(r[3] for r in rows) * 100 - min(r[2] for r in rows) * 100
    pad_label = 0.045 * max(span, 1.0) + 0.12

    ax.axvspan(threshold * 100, max(1e-9, threshold * 100) + 100, color=GREEN,
               alpha=0.06, zorder=0)
    ax.axvline(0, color=MUTED, lw=1.2, zorder=1)
    ax.axvline(threshold * 100, color=ORANGE, lw=1.6, ls="--", zorder=1,
               label=f"ship threshold ({threshold*100:.1f} pp)")

    for i, (label, est, lo, hi) in enumerate(rows):
        y = n - 1 - i
        clears = lo * 100 > threshold * 100
        col = TEAL if clears else (BLUE if lo > 0 else SLATE)
        ax.plot([lo * 100, hi * 100], [y, y], color=col, lw=3.4,
                solid_capstyle="round", zorder=3)
        ax.plot([est * 100], [y], "o", color=col, ms=10, zorder=4,
                markeredgecolor="white", markeredgewidth=1.6)
        ax.text(hi * 100 + pad_label, y,
                f"{est*100:+.2f} pp   [{lo*100:+.2f}, {hi*100:+.2f}]",
                va="center", ha="left", fontsize=9, color=NAVY)

    ax.set_yticks(range(n))
    ax.set_yticklabels([r[0] for r in rows][::-1])
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.legend(loc="lower right")
    ax.grid(axis="y", visible=False)
    lo_all = min(r[2] for r in rows) * 100
    hi_all = max(r[3] for r in rows) * 100
    pad = 0.18 * (hi_all - lo_all + 1e-9)
    ax.set_xlim(min(lo_all, -0.2) - pad, hi_all + pad * 4.0)
    ax.set_ylim(-0.75, n - 0.25)
    return ax


def forest_plot(estimates, ax=None, title="Triangulation across methods",
                xlabel="Estimated effect (percentage points)"):
    """Several methods, several assumption sets, one picture.

    Convergence across methods that fail in DIFFERENT ways is real evidence.
    Convergence across three variants of the same method is not.
    """
    import matplotlib.pyplot as plt
    from .style import NAVY, BLUE, ORANGE, PURPLE, TEAL, MUTED
    cols = [BLUE, ORANGE, PURPLE, TEAL, NAVY]
    rows = [(getattr(e, "label", e.get("label") if isinstance(e, dict) else "?"),
             getattr(e, "estimate", getattr(e, "att", None)) if not isinstance(e, dict) else e["estimate"],
             e["ci_low"] if isinstance(e, dict) else e.ci_low,
             e["ci_high"] if isinstance(e, dict) else e.ci_high) for e in estimates]
    n = len(rows)
    if ax is None:
        _, ax = plt.subplots(figsize=(8.5, 1.0 * n + 2))
    ax.axvline(0, color=MUTED, lw=1.2)
    for i, (label, est, lo, hi) in enumerate(rows):
        y = n - 1 - i
        c = cols[i % len(cols)]
        ax.plot([lo*100, hi*100], [y, y], color=c, lw=3.2, solid_capstyle="round")
        ax.plot([est*100], [y], "D", color=c, ms=8, markeredgecolor="white")
    ax.set_yticks(range(n)); ax.set_yticklabels([r[0] for r in rows][::-1])
    ax.set_xlabel(xlabel); ax.set_title(title); ax.grid(axis="y", visible=False)
    return ax


# --------------------------------------------------------------- the memo

def decision_memo(title: str, decision: str, estimates: dict,
                  threshold: float, recommendation: str,
                  assumptions: list[str], risks: list[str],
                  what_would_change_this: list[str],
                  plan: AnalysisPlan | None = None,
                  audience: str = "Injaz Product & Policy Committee") -> str:
    """Render the one-page decision memo.

    `estimates` maps a business-readable name -> an object with .estimate,
    .ci_low, .ci_high. Everything is reported in percentage points, in
    business units, with the interval. No p-values reach this page: a
    director cannot act on 0.032, they can act on 'between +1.3 and +3.1
    points, and we need at least +1.0'.
    """
    def line(name, e):
        est = getattr(e, "estimate", getattr(e, "att", None))
        return (f"  - {name}: {est*100:+.2f} pp "
                f"(95% CI {e.ci_low*100:+.2f} to {e.ci_high*100:+.2f})")

    w = lambda items: "\n".join(f"  {i}. {t}" for i, t in enumerate(items, 1))
    stamp = plan.plan_hash if plan else "not recorded"
    frozen = plan.frozen_at if plan else "not recorded"

    return textwrap.dedent(f"""\
        ================================================================
        DECISION MEMO — {title}
        To: {audience}
        Date: {datetime.now().strftime('%Y-%m-%d')}
        Analysis plan frozen: {frozen}  (hash {stamp})
        ================================================================

        DECISION REQUESTED
        {decision}

        RECOMMENDATION
        {recommendation}

        WHAT WE MEASURED   (threshold for action: {threshold*100:+.1f} pp)
        """) + "\n".join(line(k, v) for k, v in estimates.items()) + textwrap.dedent(f"""

        WHAT WE ASSUMED   (each of these, if wrong, changes the answer)
        {w(assumptions)}

        RISKS AND LIMITS
        {w(risks)}

        WHAT WOULD CHANGE THIS
        {w(what_would_change_this)}

        ================================================================
        """)
