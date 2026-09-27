from _draw import *
import pandas as pd, json
D = "/home/claude/course_assets/data/"
print("Module 1-2 figures:")

# ---------------------------------------------------------------- 1. two worlds
def f_two_worlds():
    fig, ax = canvas(A, (0, 100), (0, 50))
    label(ax, 50, 47, "One user. Two worlds. You only ever get to visit one.",
          fs=10.5, color=NAVY, bold=True)
    node(ax, 50, 37, "user i", r=5.2, color=NAVY, fs=8.5)
    # treated world
    box(ax, 6, 8, 38, 22, "", fc="#EAF5FC", ec=BLUE, lw=1.6)
    chip(ax, 12, 25, 26, 3.6, "WORLD 1  ·  treated", color=BLUE, fs=8)
    label(ax, 25, 20.5, "gets the guided uploader", fs=9, color=NAVY)
    label(ax, 25, 15.5, "$Y_i(1) = 1$", fs=14, color=BLUE, bold=True)
    label(ax, 25, 11, "completes the service", fs=8, color=SLATE, style="italic")
    # control world
    box(ax, 56, 8, 38, 22, "", fc="#FDF1E9", ec=ORANGE, lw=1.6)
    chip(ax, 62, 25, 26, 3.6, "WORLD 0  ·  not treated", color=ORANGE, fs=8)
    label(ax, 75, 20.5, "keeps the old uploader", fs=9, color=NAVY)
    label(ax, 75, 15.5, "$Y_i(0) = 0$", fs=14, color=ORANGE, bold=True)
    label(ax, 75, 11, "abandons the service", fs=8, color=SLATE, style="italic")
    arrow(ax, (46, 34), (28, 30.5), color=BLUE, lw=2.0, rad=0.18)
    arrow(ax, (54, 34), (72, 30.5), color=ORANGE, lw=2.0, rad=-0.18)
    # the cut, drawn in two segments so it never runs through the labels
    for y0, y1 in [(24.5, 31.5), (10.5, 13.5)]:
        ax.plot([50, 50], [y0, y1], color=RED, lw=2.0, ls=(0, (4.5, 3.5)), zorder=1)
    # the effect, in a white plate that sits over the cut
    box(ax, 38.5, 14.5, 23, 9.5, "", fc="white", ec="white", lw=0)
    label(ax, 50, 21, r"$\tau_i = Y_i(1) - Y_i(0)$", fs=12.5, color=NAVY, bold=True)
    label(ax, 50, 16.8, "the individual\ntreatment effect", fs=8, color=SLATE)
    label(ax, 50, 7.2, "only ONE world is ever observed", fs=9, color=RED, bold=True)
    bilingual(ax, 50, 2.6, "the counterfactual is missing by construction",
              "النواتج المحتملة", fs=8)
    save(fig, "m1_two_worlds")

# ------------------------------------------------- 2. bias decomposition
def f_bias_decomposition():
    fig, ax = plt.subplots(figsize=A)
    truth = json.load(open(D + "GROUND_TRUTH.json"))["module1_potential_outcomes"]
    att, bias = truth["true_ATE"] * 100, truth["selection_bias_term"] * 100
    naive = att + bias
    ax.barh([1], [att], color=TEAL, height=0.42, label="ATT — the real effect")
    ax.barh([1], [bias], left=[att], color=RED, height=0.42, alpha=0.85,
            label="selection bias — who chose the feature")
    ax.barh([0], [att], color=TEAL, height=0.42)
    ax.text(att / 2, 1, f"{att:.1f} pp", ha="center", va="center", color="white",
            fontweight="bold", fontsize=11)
    ax.text(att + bias / 2, 1, f"+{bias:.1f} pp", ha="center", va="center",
            color="white", fontweight="bold", fontsize=11)
    ax.text(att / 2, 0, f"{att:.1f} pp", ha="center", va="center", color="white",
            fontweight="bold", fontsize=11)
    ax.text(naive + 0.6, 1, f"naive estimate = {naive:.1f} pp", va="center",
            fontsize=10, color=NAVY, fontweight="bold")
    ax.text(att + 0.6, 0, f"randomised estimate = {att:.1f} pp", va="center",
            fontsize=10, color=NAVY, fontweight="bold")
    ax.set_yticks([1, 0])
    ax.set_yticklabels(["Users who\nopted in", "Users assigned\nby a coin flip"],
                       fontsize=9.5)
    ax.set_xlabel("Estimated effect on completion rate (percentage points)")
    ax.set_title("The same feature, measured two ways")
    ax.set_xlim(0, 27); ax.grid(axis="y", visible=False)
    ax.legend(loc="upper right", fontsize=8.5, bbox_to_anchor=(1.0, 1.02))
    ax.text(13.5, -0.78, r"$E[Y|T{=}1] - E[Y|T{=}0]\;=\;$ATT$\;+\;$"
            r"$(E[Y(0)|T{=}1]-E[Y(0)|T{=}0])$",
            ha="center", fontsize=10.5, color=SLATE)
    ax.text(13.5, -1.10, "naive difference  =  the real effect  +  selection bias",
            ha="center", fontsize=9, color=MUTED, style="italic")
    ax.set_ylim(-1.35, 1.75)
    save(fig, "m1_bias_decomposition")

# ---------------------------------------------- 3. confounding triangle
def f_confounding_triangle():
    fig, ax = canvas(A, (0, 100), (0, 50))
    node(ax, 50, 39, "digital\nliteracy", r=9, color=PURPLE, fs=8.5)
    node(ax, 18, 13, "uses the\nuploader", r=9.5, color=BLUE, fs=8.5)
    node(ax, 82, 13, "completes\nthe service", r=9.5, color=ORANGE, fs=8.5)
    arrow(ax, (43, 32), (25, 21), color=PURPLE, lw=2.4)
    arrow(ax, (57, 32), (75, 21), color=PURPLE, lw=2.4)
    arrow(ax, (28, 13), (72, 13), color=BLUE, lw=2.4)
    label(ax, 28, 27, "drives\nadoption", fs=8, color=PURPLE, rot=-38)
    label(ax, 72, 27, "drives\ncompletion", fs=8, color=PURPLE, rot=38)
    label(ax, 50, 8.5, "the effect we want to measure", fs=8.5, color=BLUE, bold=True)
    box(ax, 6, 40, 30, 8, "the confounder\nis the ONLY thing\nboth arrows share",
        fc=PANEL, ec=PANEL, fs=8, tc=SLATE)
    label(ax, 50, 2.0,
          "Literacy opens a BACKDOOR path. Until it is blocked, the blue arrow "
          "is not what you are measuring.",
          fs=8.5, color=NAVY)
    save(fig, "m1_confounding_triangle")

# ------------------------------------------------ 4. bias does not shrink
def f_bias_vs_n():
    df = pd.read_parquet(D + "simulated_potential_outcomes.parquet")
    truth = json.load(open(D + "GROUND_TRUTH.json"))["module1_potential_outcomes"]
    rng = np.random.default_rng(7)
    # Average many resamples at each n: one draw per n is noise, and the point
    # of the chart is the systematic gap, not the wobble.
    ns = np.unique(np.logspace(2, np.log10(len(df)), 22).astype(int))
    REPS = 40
    self_, rand_, self_lo, self_hi = [], [], [], []
    for n in ns:
        a, b = [], []
        for _ in range(REPS):
            smp = df.sample(n, random_state=int(rng.integers(1e6)))
            t = smp.treated_self_selected
            a.append(100 * (smp.y_observed_self_selected[t == 1].mean()
                            - smp.y_observed_self_selected[t == 0].mean()))
            r = smp.treated_randomised
            b.append(100 * (smp.y_observed_randomised[r == 1].mean()
                            - smp.y_observed_randomised[r == 0].mean()))
        self_.append(np.nanmean(a)); rand_.append(np.nanmean(b))
        self_lo.append(np.nanpercentile(a, 10)); self_hi.append(np.nanpercentile(a, 90))
    fig, ax = plt.subplots(figsize=A)
    ax.fill_between(ns, self_lo, self_hi, color=RED, alpha=0.13)
    ax.semilogx(ns, self_, "-o", color=RED, ms=4, lw=2.2, label="self-selected (opt-in)")
    ax.semilogx(ns, rand_, "-o", color=TEAL, ms=4, lw=2.2, label="randomised (coin flip)")
    ax.axhline(truth["true_ATE"] * 100, color=NAVY, ls="--", lw=1.4)
    ax.text(ns[2], truth["true_ATE"] * 100 + 1.4, "the truth: +5.0 pp",
            fontsize=9, color=NAVY, fontweight="bold")
    ax.annotate("", xy=(ns[-2], 19.3), xytext=(ns[-2], 5.0),
                arrowprops=dict(arrowstyle="<->", color=SLATE, lw=1.4))
    ax.text(ns[-2] * 0.80, 12.5, "the gap never closes", rotation=90, ha="right",
            va="center", fontsize=9.5, color=SLATE, fontweight="bold")
    ax.set_xlabel("Sample size (log scale)")
    ax.set_ylabel("Estimated effect (percentage points)")
    ax.set_title("More data buys precision, never a fix for bias")
    ax.legend(loc="center left", bbox_to_anchor=(0.03, 0.42))
    ax.set_ylim(-2, 27)
    save(fig, "m1_bias_vs_n")

# ------------------------------------------------- 5. experiment anatomy
def f_experiment_anatomy():
    fig, ax = canvas(B, (0, 121), (0, 40))
    box(ax, 2, 12, 17, 15, "Eligible\nuser pool\n\n200,000", fc=PANEL, tc=NAVY, fs=9)
    label(ax, 10.5, 8.5, "unit of\nRANDOMISATION", fs=7.5, color=BLUE, bold=True)
    arrow(ax, (19.5, 19.5), (28, 19.5), lw=2.2)
    label(ax, 23.7, 22.5, "hash(salt,\nuser_id)", fs=7.5, color=SLATE)
    chip(ax, 28, 21.5, 20, 7.5, "CONTROL   50%\nold uploader", color=SLATE, fs=8.5)
    chip(ax, 28, 10.5, 20, 7.5, "TREATMENT   50%\nguided uploader", color=BLUE, fs=8.5)
    arrow(ax, (48.5, 25), (57, 22), lw=2.0)
    arrow(ax, (48.5, 14), (57, 18), lw=2.0)
    box(ax, 57, 12, 17, 15, "TRIGGER\n\nreached the\nupload step\n\n62%", fc="#FDF1E9",
        ec=ORANGE, tc=NAVY, fs=8.5)
    label(ax, 65.5, 8.5, "unit of\nANALYSIS", fs=7.5, color=ORANGE, bold=True)
    arrow(ax, (74.5, 19.5), (82, 19.5), lw=2.2)
    chip(ax, 82, 22, 37, 7, "OEC   ·   service completion rate", color=TEAL, fs=9)
    box(ax, 82, 10, 37, 10.5,
        "GUARDRAILS  ·  must not get worse\n"
        "support contacts   ·   error rate\n"
        "session duration   ·   drop-off",
        fc=PANEL, ec=MUTED, tc=NAVY, fs=8)
    label(ax, 60, 35.5, "Every experiment is these six decisions, made before any data arrives",
          fs=10.5, color=NAVY, bold=True)
    ax.text(60, 2.5, ar("وحدة العشوائية · وحدة التحليل · المقياس الرئيسي · مقاييس الحماية"),
            fontsize=9, color=MUTED, ha="center", va="center", **AR_FONT)
    save(fig, "m2_experiment_anatomy")

# --------------------------------------------- 6. randomisation unit tree
def f_unit_tree():
    fig, ax = canvas(B, (0, 121), (0, 40))
    label(ax, 60, 37.5, "Choosing the randomisation unit is a causal decision, not a convenience",
          fs=10.5, color=NAVY, bold=True)
    box(ax, 2, 17, 18, 9, "Start:\nwhat is the\nrandomisation unit?", fc=NAVY, ec=NAVY,
        tc="white", fs=8.5, bold=True)
    qs = [
        (24, "Do units\ninterfere with\neach other?", TEAL),
        (48, "Do users\nreturn across\nsessions?", PURPLE),
        (72, "Enough units\nfor adequate\npower?", ORANGE),
    ]
    for x, q, c in qs:
        box(ax, x, 17, 18, 9, q, fc="white", ec=c, tc=NAVY, fs=8, lw=1.8)
    for x in (20, 44, 68):
        arrow(ax, (x, 21.5), (x + 4, 21.5), lw=2.0)
    outs = [
        (24, 4.5, "YES → cluster or\nswitchback design", TEAL),
        (48, 4.5, "YES → randomise\nthe USER", PURPLE),
        (72, 4.5, "NO → switchback,\nor accept a\nbigger MDE", ORANGE),
    ]
    for x, y, t, c in outs:
        arrow(ax, (x + 9, 16.5), (x + 9, 12.5), color=c, lw=2.0)
        box(ax, x - 1, y, 20, 8, t, fc=c, ec=c, tc="white", fs=8, bold=True)
    arrow(ax, (90, 21.5), (94, 21.5), lw=2.0)
    box(ax, 94, 15.5, 25, 12,
        "YES → randomise the\nSESSION only if users\nnever return and\nnothing leaks\n"
        "(rarely true)", fc=PANEL, ec=MUTED, tc=NAVY, fs=8)
    label(ax, 60, 1.2,
          "Default to the USER. Session-level randomisation is the most common "
          "silent design error in industry.",
          fs=8.5, color=RED, bold=True)
    save(fig, "m2_randomisation_unit_tree")

# ------------------------------------------------------ 7. interference
def f_interference():
    fig, ax = canvas(A, (0, 100), (0, 50))
    label(ax, 50, 47, "SUTVA fails when one unit's treatment changes another unit's outcome",
          fs=9.5, color=NAVY, bold=True)
    # panel 1: shared device
    box(ax, 3, 6, 45, 34, "", fc=PANEL, ec=PANEL)
    chip(ax, 8, 34, 25, 3.6, "SPILLOVER", color=PURPLE, fs=8)
    node(ax, 17, 24, "user A\nTREATED", r=7.5, color=BLUE, fs=7)
    node(ax, 36, 24, "user B\nCONTROL", r=7.5, color=SLATE, fs=7)
    arrow(ax, (24, 24), (28, 24), color=RED, lw=2.2, ls=(0, (3, 2)))
    label(ax, 26, 28.5, "shows\nthem", fs=7, color=RED)
    box(ax, 10, 9, 32, 7, "one household, one device\nthe control user sees the new flow",
        fc="white", ec=MUTED, tc=NAVY, fs=7.5)
    # panel 2: cannibalisation
    box(ax, 52, 6, 45, 34, "", fc=PANEL, ec=PANEL)
    chip(ax, 57, 34, 25, 3.6, "CANNIBALISATION", color=ORANGE, fs=8)
    for i, x in enumerate([61, 70, 79, 88]):
        c = BLUE if i < 3 else SLATE
        box(ax, x - 3.4, 22, 6.8, 8, "", fc=c, ec=c)
    label(ax, 74.5, 18.5, "a finite pool of same-day appointment slots", fs=7.5, color=NAVY)
    label(ax, 74.5, 32, "treated users book faster and take them all",
          fs=7.5, color=NAVY)
    box(ax, 59, 9, 32, 7, "the control group looks worse\nbecause treatment took the supply",
        fc="white", ec=MUTED, tc=NAVY, fs=7.5)
    label(ax, 50, 2.2,
          "In both panels the measured 'effect' is partly the control group getting worse.",
          fs=8.5, color=RED, bold=True)
    save(fig, "m2_interference")

# ---------------------------------------------------- 8. SRM diagnostic
def f_srm():
    import sys; sys.path.insert(0, "/home/claude/course_assets")
    from causal_utils.assignment import srm_check
    clean = pd.read_csv(D + "injaz_experiment_results.csv", usecols=["variant"])
    brok = pd.read_csv(D + "injaz_experiment_results_srm_broken.csv", usecols=["variant"])
    rc, rb = srm_check(clean["variant"]), srm_check(brok["variant"])
    fig, axes = plt.subplots(1, 2, figsize=A, sharey=True)
    for ax, r, ttl in zip(axes, (rc, rb), ("Clean experiment", "3% of one arm lost")):
        arms = list(r.observed)
        x = np.arange(len(arms))
        ax.bar(x - 0.19, [r.expected[a] for a in arms], 0.36, color=MUTED,
               label="expected")
        ax.bar(x + 0.19, [r.observed[a] for a in arms], 0.36,
               color=TEAL if r.passed else RED, label="observed")
        ax.set_xticks(x); ax.set_xticklabels(arms)
        ax.set_title(ttl, fontsize=11)
        ax.text(0.5, 0.93, f"$\\chi^2$ = {r.chi2:,.1f}   p = {r.p_value:.2g}",
                transform=ax.transAxes, ha="center", fontsize=9.5, color=NAVY)
        if not r.passed:
            ax.text(0.5, 0.55, "INVALID", transform=ax.transAxes, ha="center",
                    va="center", fontsize=26, color=RED, alpha=0.30,
                    fontweight="bold", rotation=12)
        else:
            ax.text(0.5, 0.55, "PASS", transform=ax.transAxes, ha="center",
                    va="center", fontsize=26, color=TEAL, alpha=0.28,
                    fontweight="bold", rotation=12)
    axes[0].set_ylabel("Users assigned"); axes[0].legend(loc="lower center", ncol=2)
    axes[0].set_ylim(0, 46000)
    fig.suptitle("Sample-Ratio Mismatch: a 1.5% drift is fatal, not cosmetic",
                 fontsize=11.5, y=1.02, color=NAVY, fontweight="bold")
    save(fig, "m2_srm_diagnostic")


for f in [f_two_worlds, f_bias_decomposition, f_confounding_triangle, f_bias_vs_n,
          f_experiment_anatomy, f_unit_tree, f_interference, f_srm]:
    f()
