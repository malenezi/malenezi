from _draw import *
import sys; sys.path.insert(0, "/home/claude/course_assets")
import pandas as pd
from scipy import stats
from causal_utils.power import (sample_size_proportions, power_for_n, mde_for_n,
                                cuped_adjust)
from causal_utils.analysis import peeking_simulation
D = "/home/claude/course_assets/data/"
print("Module 3-4 figures:")

# ------------------------------------------------- 9. four-way trade-off
def f_tradeoff():
    fig, ax = canvas(A, (0, 100), (0, 50))
    label(ax, 50, 47, "Four quantities, one equation. Fix three and the fourth is decided.",
          fs=10, color=NAVY, bold=True)
    specs = [(16, BLUE, "α", "significance\nlevel", "how often you cry\nwolf on a null"),
             (38, PURPLE, "1−β", "power", "how often you catch\na real effect"),
             (60, ORANGE, "δ", "MDE", "the smallest effect\nworth detecting"),
             (82, TEAL, "n", "sample size", "what it costs you\nin traffic and days")]
    for x, c, sym, name, desc in specs:
        node(ax, x, 31, sym, r=8.5, color=c, fs=15)
        label(ax, x, 19.5, name.upper(), fs=9, color=c, bold=True)
        label(ax, x, 14, desc, fs=7.8, color=SLATE)
    for x0, x1 in [(16, 38), (38, 60), (60, 82)]:
        arrow(ax, (x0 + 9.5, 31), (x1 - 9.5, 31), color=MUTED, lw=1.6,
              style="<|-|>", ms=10)
    box(ax, 12, 2.5, 76, 8,
        r"$n \;\propto\; \dfrac{(z_{\alpha/2} + z_{\beta})^2 \, \sigma^2}{\delta^2}$"
        "        halve the MDE  →  4× the sample",
        fc=PANEL, ec=PANEL, tc=NAVY, fs=11)
    save(fig, "m3_four_way_tradeoff")

# -------------------------------------------------- 10. Type I / Type II
def f_type_i_ii():
    fig = plt.figure(figsize=A)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.25], wspace=0.28)
    ax0 = fig.add_subplot(gs[0]); ax0.axis("off")
    ax0.set_xlim(-2, 50); ax0.set_ylim(0, 46)
    label(ax0, 24, 44, "The 2×2 you must be able to draw from memory",
          fs=9.5, color=NAVY, bold=True)
    label(ax0, 16, 34.5, "no effect\nexists", fs=8, color=SLATE, bold=True)
    label(ax0, 35, 34.5, "an effect\nexists", fs=8, color=SLATE, bold=True)
    label(ax0, 5.0, 25, "you\nreject", fs=8, color=SLATE, bold=True, rot=90)
    label(ax0, 5.0, 11, "you do\nnot reject", fs=8, color=SLATE, bold=True, rot=90)
    cells = [(9, 19, RED, "Type I error\nα = 0.05", "false positive"),
             (28, 19, TEAL, "correct\nPOWER = 1−β", "true positive"),
             (9, 5, TEAL, "correct", "true negative"),
             (28, 5, ORANGE, "Type II error\nβ = 0.20", "false negative")]
    for x, y, c, t, sub in cells:
        box(ax0, x, y, 14, 12, "", fc=c, ec=c, radius=1.0)
        ax0.text(x + 7, y + 7.4, t, ha="center", va="center", color="white",
                 fontsize=8, fontweight="bold", zorder=4)
        ax0.text(x + 7, y + 3.0, sub, ha="center", va="center", color="white",
                 fontsize=7, zorder=4, style="italic")

    ax = fig.add_subplot(gs[1])
    x = np.linspace(-4, 8, 700)
    h0, h1 = stats.norm.pdf(x, 0, 1), stats.norm.pdf(x, 2.8, 1)
    crit = 1.96
    ax.plot(x, h0, color=SLATE, lw=2); ax.plot(x, h1, color=BLUE, lw=2)
    ax.fill_between(x, 0, h0, where=x >= crit, color=RED, alpha=0.55)
    ax.fill_between(x, 0, h1, where=x < crit, color=ORANGE, alpha=0.45)
    ax.axvline(crit, color=NAVY, lw=1.4, ls="--")
    ax.text(crit + 0.12, 0.40, "critical value", fontsize=8, color=NAVY, rotation=90,
            va="top")
    ax.text(-1.6, 0.30, "H₀\nno effect", fontsize=8.5, color=SLATE, ha="center")
    ax.text(4.4, 0.30, "H₁\nreal effect", fontsize=8.5, color=BLUE, ha="center")
    ax.annotate("α", xy=(2.4, 0.018), xytext=(3.4, 0.10), fontsize=11, color=RED,
                fontweight="bold", arrowprops=dict(arrowstyle="->", color=RED))
    ax.annotate("β", xy=(1.3, 0.035), xytext=(0.1, 0.13), fontsize=11, color=ORANGE,
                fontweight="bold", arrowprops=dict(arrowstyle="->", color=ORANGE))
    ax.set_yticks([]); ax.set_xlabel("Observed effect (standard errors)")
    ax.set_title("Move the line and you trade one error for the other", fontsize=10)
    save(fig, "m3_type_i_ii")

# ------------------------------------------------------- 11. MDE vs n
def f_mde_vs_n():
    mdes = np.linspace(0.003, 0.05, 200)
    ns = [sample_size_proportions(0.55, m) for m in mdes]
    fig, ax = plt.subplots(figsize=A)
    ax.plot(mdes * 100, ns, color=BLUE, lw=2.6)
    for m, c, col in [(0.02, "1×", TEAL), (0.01, "4×", ORANGE), (0.005, "16×", RED)]:
        n = sample_size_proportions(0.55, m)
        ax.plot([m * 100], [n], "o", color=col, ms=9, markeredgecolor="white",
                markeredgewidth=1.5, zorder=5)
        ax.annotate(f"{m*100:.1f} pp\n{n:,}/arm\n{c} the cost",
                    xy=(m * 100, n), xytext=(m * 100 + 0.55, n + 14000),
                    fontsize=8.5, color=col, fontweight="bold",
                    arrowprops=dict(arrowstyle="-", color=col, lw=1.2))
    ax.set_xlabel("Minimum detectable effect (percentage points)")
    ax.set_ylabel("Required sample size per arm")
    ax.set_title("Ambition is quadratic: halving the MDE quadruples the cost")
    ax.set_ylim(0, 175000); ax.set_xlim(0, 5.2)
    ax.yaxis.set_major_formatter(lambda v, p: f"{v/1000:.0f}k")
    save(fig, "m3_mde_vs_n")

# -------------------------------------------------- 12. run-length pipeline
def f_run_length():
    fig, ax = canvas(B, (0, 121), (0, 34))
    label(ax, 60, 31.5, "From a statistic to a date in the delivery plan",
          fs=10.5, color=NAVY, bold=True)
    steps = [(2, "n per arm\n\n9,669", BLUE),
             (25, "× arms\n\n2 arms\n= 19,338", PURPLE),
             (48, "÷ daily eligible\n× trigger rate\n\n13,351 × 62%\n= 8,255/day", ORANGE),
             (71, "= days\n\n2.3 days", TEAL),
             (94, "max(·, whole weeks)\n\nRUN 7 DAYS", NAVY)]
    for i, (x, t, c) in enumerate(steps):
        solid = i == len(steps) - 1
        box(ax, x, 9, 21, 15, t,
            fc=c if solid else "white", ec=c, tc="white" if solid else NAVY,
            fs=8.5, bold=solid, lw=1.8)
        if i < len(steps) - 1:
            arrow(ax, (x + 21.5, 16.5), (x + 22.6, 16.5), lw=2.2, color=MUTED)
    label(ax, 60, 4.5,
          "The floor is not superstition: weekday and weekend users are different "
          "people, so a partial week samples a biased slice.",
          fs=8.8, color=RED, bold=True)
    save(fig, "m3_run_length_pipeline")

# ------------------------------------------------------- 12b. CUPED
def f_cuped():
    e = pd.read_csv(D + "injaz_experiment_results.csv")
    e = e[e.triggered == 1]
    r = cuped_adjust(e.completed, e.prior_completion_rate)
    fig, ax = plt.subplots(figsize=A)
    bars = ax.bar(["Raw outcome", "CUPED-adjusted"],
                  [r.variance_before, r.variance_after],
                  color=[SLATE, TEAL], width=0.45)
    for b, v in zip(bars, [r.variance_before, r.variance_after]):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.004, f"{v:.4f}",
                ha="center", fontsize=10, color=NAVY, fontweight="bold")
    ax.annotate("", xy=(1, r.variance_after), xytext=(1, r.variance_before),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=2))
    ax.text(1.12, (r.variance_before + r.variance_after) / 2,
            f"−{r.variance_reduction:.1%} variance\n= {r.effective_n_multiplier:.2f}× the sample\n"
            f"for free",
            fontsize=9.5, color=ORANGE, fontweight="bold", va="center")
    ax.set_ylabel("Variance of the outcome")
    ax.set_title(f"CUPED on real Injaz data — ρ(pre, post) = {r.correlation:.2f}, "
                 f"so variance falls by ρ² = {r.correlation**2:.1%}", fontsize=10.5)
    ax.set_ylim(0, 0.30); ax.set_xlim(-0.6, 2.0)
    save(fig, "m3_cuped_variance")

# ------------------------------------------------------ 13. peeking
def f_peeking():
    df = peeking_simulation(n_looks_grid=(1, 2, 5, 10, 20), n_per_arm=4000,
                            n_experiments=3000)
    fig, ax = plt.subplots(figsize=A)
    x = np.arange(len(df))
    bars = ax.bar(x, df.false_positive_rate * 100, color=[TEAL] + [ORANGE]*2 + [RED]*2,
                  width=0.55)
    for b, v in zip(bars, df.false_positive_rate * 100):
        ax.text(b.get_x() + b.get_width()/2, v + 0.6, f"{v:.1f}%", ha="center",
                fontsize=10, color=NAVY, fontweight="bold")
    ax.axhline(5, color=NAVY, ls="--", lw=1.5)
    ax.text(len(df) - 0.45, 5.9, "the 5% you promised", fontsize=9, color=NAVY,
            ha="right", fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels([f"{k} look{'s' if k>1 else ''}" for k in df.n_looks])
    ax.set_ylabel("False-positive rate (%)")
    ax.set_title("Every experiment below has ZERO true effect. Only the looking changed.")
    ax.set_ylim(0, 30)
    save(fig, "m4_peeking_staircase")

# --------------------------------------------- 14. correction family flow
def f_correction_flow():
    fig, ax = canvas(B, (0, 121), (0, 38))
    label(ax, 60, 36, "Choosing the correction family is a design decision, not a computation",
          fs=10.5, color=NAVY, bold=True)
    box(ax, 2, 12.5, 19, 11, "How many\nhypotheses does\nthis test\nbelong to?",
        fc=NAVY, ec=NAVY, tc="white", fs=8.5, bold=True)

    cols = [(26, TEAL, "ONE pre-registered OEC",
             "NO CORRECTION\n\nyou promised one test,\nyou ran one test"),
            (58, ORANGE, "A GUARDRAIL family  (3–6 metrics)",
             "BONFERRONI  ·  control FWER\n\nany single broken guardrail\nblocks the launch"),
            (90, PURPLE, "An EXPLORATORY sweep  (segments)",
             "BENJAMINI–HOCHBERG  ·  control FDR\n\nyou want a shortlist to follow up,\nnot certainty on each")]

    # one rail out of the decision box, with a clean drop into each branch
    rail_y = 29.5
    ax.plot([21.5, 21.5], [18, rail_y], color=MUTED, lw=1.8, zorder=1)
    ax.plot([21.5, 104.5], [rail_y, rail_y], color=MUTED, lw=1.8, zorder=1)
    for x, c, q, a in cols:
        cx = x + 14.5
        arrow(ax, (cx, rail_y), (cx, 25.6), color=c, lw=2.0)
        box(ax, x, 19.5, 29, 6, q, fc="white", ec=c, tc=NAVY, fs=8.4, lw=1.8)
        arrow(ax, (cx, 19), (cx, 17.4), color=c, lw=2.0)
        box(ax, x, 5, 29, 12, a, fc=c, ec=c, tc="white", fs=8.4)
    label(ax, 60, 1.4,
          "Deciding this AFTER seeing the p-values is the same error as choosing "
          "the metric after seeing the data.",
          fs=8.8, color=RED, bold=True)
    save(fig, "m4_correction_family")

# ----------------------------------------- 15. unit-of-analysis mismatch
def f_unit_mismatch():
    fig, ax = canvas(A, (0, 100), (0, 50))
    label(ax, 50, 47.5, "Randomise users, analyse sessions, and your interval lies to you",
          fs=9.8, color=NAVY, bold=True)
    for i, ux in enumerate([10, 38, 66]):
        box(ax, ux, 22, 26, 17, "", fc=PANEL, ec=BLUE, lw=1.6)
        label(ax, ux + 13, 36, f"user {i+1}  ·  randomised ONCE", fs=8, color=BLUE, bold=True)
        for j in range(4):
            box(ax, ux + 2 + j * 5.8, 25, 4.8, 7, f"s{j+1}", fc=BLUE, ec=BLUE,
                tc="white", fs=7, radius=0.8)
    label(ax, 50, 18.5, "12 sessions — but only 3 independent draws of the treatment",
          fs=9, color=NAVY)
    box(ax, 8, 4, 39, 11,
        "NAIVE session-level SE\n\n0.00166\n\n'we are very sure'",
        fc="white", ec=RED, tc=RED, fs=8.5, lw=1.8)
    box(ax, 53, 4, 39, 11,
        "CLUSTERED by user\n\n0.00267   (1.61× wider)\n\nthe honest interval",
        fc=TEAL, ec=TEAL, tc="white", fs=8.5, lw=1.8)
    arrow(ax, (47.5, 9.5), (52.5, 9.5), color=MUTED, lw=2.2)
    save(fig, "m4_unit_of_analysis")

# ------------------------------------------------- 16. Simpson's paradox
def f_simpson():
    rng = np.random.default_rng(11)
    fig, ax = plt.subplots(figsize=A)
    groups = [("Low complexity\nservices", 0.30, 0.72, BLUE, 0.85),
              ("Medium complexity", 0.55, 0.52, PURPLE, 0.50),
              ("High complexity\nservices", 0.80, 0.30, ORANGE, 0.15)]
    xs_all, ys_all = [], []
    for name, xc, yc, col, w in groups:
        x = np.clip(rng.normal(xc, 0.055, 120), 0, 1)
        y = np.clip(yc + 0.42 * (x - xc) + rng.normal(0, 0.018, 120), 0, 1)
        ax.scatter(x, y, s=16, color=col, alpha=0.55, edgecolors="none")
        b = np.polyfit(x, y, 1)
        xr = np.linspace(x.min(), x.max(), 20)
        ax.plot(xr, np.polyval(b, xr), color=col, lw=2.6)
        ax.text(x.mean(), y.mean() + 0.075, name, fontsize=8, color=col,
                ha="center", fontweight="bold")
        xs_all.append(x); ys_all.append(y)
    X, Y = np.concatenate(xs_all), np.concatenate(ys_all)
    b = np.polyfit(X, Y, 1)
    xr = np.linspace(0.15, 0.95, 20)
    ax.plot(xr, np.polyval(b, xr), color=RED, lw=3.0, ls="--")
    ax.text(0.62, np.polyval(b, 0.62) - 0.09, "POOLED trend\n(the opposite sign)",
            color=RED, fontsize=9, fontweight="bold", ha="center")
    ax.set_xlabel("Share of users given the new uploader")
    ax.set_ylabel("Completion rate")
    ax.set_title("Every segment goes up. The aggregate goes down.")
    ax.set_ylim(0.15, 0.92)
    save(fig, "m4_simpsons_paradox")


for f in [f_tradeoff, f_type_i_ii, f_mde_vs_n, f_run_length, f_cuped,
          f_peeking, f_correction_flow, f_unit_mismatch, f_simpson]:
    f()
