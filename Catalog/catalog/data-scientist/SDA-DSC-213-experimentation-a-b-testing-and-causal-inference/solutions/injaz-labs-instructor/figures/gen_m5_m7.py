from _draw import *
import sys; sys.path.insert(0, "/home/claude/course_assets")
import pandas as pd, networkx as nx
from causal_utils.quasi import (estimate_propensity, match_nearest, did_twfe,
                                event_study, iv_2sls)
from causal_utils.graphs import InjazDAG, injaz_uploader_dag, draw_dag
from causal_utils.analysis import two_proportion_test
D = "/home/claude/course_assets/data/"
print("Module 5-7 figures:")

# ------------------------------------------------- 17. ladder of evidence
def f_ladder():
    fig, ax = canvas(A, (0, 100), (0, 50))
    label(ax, 50, 47.5, "Every rung down buys convenience with a stronger assumption",
          fs=9.8, color=NAVY, bold=True)
    rungs = [
        (38, TEAL,  "Randomised experiment (A/B)", "assumes: nothing. Balance is manufactured."),
        (30.5, BLUE, "Natural experiment / IV",    "assumes: the instrument affects Y only through T"),
        (23,  PURPLE,"Difference-in-differences",  "assumes: parallel trends absent the programme"),
        (15.5, ORANGE,"Matching / weighting",      "assumes: no unmeasured confounders"),
        (8,   RED,   "Naive comparison",           "assumes: the groups were already comparable"),
    ]
    for y, c, name, ass in rungs:
        box(ax, 8, y - 2.6, 4, 5.2, "", fc=c, ec=c, radius=0.6)
        label(ax, 15, y + 1.1, name, fs=9.5, color=NAVY, bold=True, ha="left")
        label(ax, 15, y - 1.6, ass, fs=8, color=SLATE, ha="left", style="italic")
    ax.annotate("", xy=(4.5, 40), xytext=(4.5, 6),
                arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=2.2))
    label(ax, 2.0, 23, "CREDIBILITY", fs=8.5, color=MUTED, bold=True, rot=90)
    label(ax, 50, 2.4,
          "You do not get to skip the assumption. You only get to choose which one you must defend.",
          fs=8.8, color=NAVY, bold=True)
    save(fig, "m5_ladder_of_evidence")

# ------------------------------------------------- 18. propensity overlap
def f_overlap():
    u = pd.read_csv(D + "injaz_users.csv")
    cov = ["age", "device_age_years", "digital_literacy_score", "prior_sessions",
           "prior_completion_rate", "region"]
    e = estimate_propensity(u, "enrolled_training", cov)
    fig, ax = plt.subplots(figsize=A)
    bins = np.linspace(0, 1, 46)
    t, c = e[u.enrolled_training == 1], e[u.enrolled_training == 0]
    ax.hist(c, bins=bins, density=True, color=SLATE, alpha=0.62, label="not enrolled")
    ax.hist(t, bins=bins, density=True, color=BLUE, alpha=0.62, label="enrolled")
    lo, hi = max(t.min(), c.min()), min(t.max(), c.max())
    ax.axvspan(lo, hi, color=TEAL, alpha=0.10)
    ax.axvline(lo, color=TEAL, lw=1.4, ls="--"); ax.axvline(hi, color=TEAL, lw=1.4, ls="--")
    ax.text((lo + hi) / 2, ax.get_ylim()[1] * 0.93, "COMMON SUPPORT\nmatching is possible here",
            ha="center", fontsize=9, color=TEAL, fontweight="bold")
    ax.set_xlabel("Estimated propensity to enrol,  ê(x) = P(enrol | X)")
    ax.set_ylabel("Density")
    ax.set_title("Overlap is the go/no-go check — read it before you match")
    ax.legend(loc="upper right")
    save(fig, "m5_propensity_overlap")

# ---------------------------------------------------- 19. DiD two lines
def f_did_lines():
    p = pd.read_csv(D + "injaz_regions_panel.csv")
    p["activation_month"] = pd.to_numeric(p["activation_month"], errors="coerce")
    w1 = p[p.activation_month == 10]
    never = p[p.activation_month.isna()]
    t = w1.groupby("period").completion_rate.mean() * 100
    c = never.groupby("period").completion_rate.mean() * 100
    shift = t.loc[:9].mean() - c.loc[:9].mean()
    cf = c + shift                                    # the counterfactual
    fig, ax = plt.subplots(figsize=A)
    ax.plot(t.index, t.values, "-o", color=BLUE, ms=4, lw=2.2, label="treated regions")
    ax.plot(c.index, c.values, "-o", color=SLATE, ms=4, lw=2.2, label="never-treated regions")
    ax.plot(cf.index[9:], cf.values[9:], "--", color=ORANGE, lw=2.2,
            label="counterfactual for the treated")
    ax.axvline(10, color=NAVY, lw=1.4, ls=":")
    ax.text(10.25, t.min() + 0.2, "reminders switched on", fontsize=8.5, color=NAVY, rotation=90)
    x_end = t.index.max()
    ax.annotate("", xy=(x_end, t.iloc[-1]), xytext=(x_end, cf.iloc[-1]),
                arrowprops=dict(arrowstyle="<->", color=TEAL, lw=2.2))
    ax.text(x_end - 0.5, (t.iloc[-1] + cf.iloc[-1]) / 2, "DiD estimate",
            fontsize=9.5, color=TEAL, fontweight="bold", ha="right", va="center")
    ax.set_xlabel("Month"); ax.set_ylabel("Completion rate (%)")
    ax.set_title("The control group's TREND, not its level, is what you borrow")
    ax.legend(loc="upper left", fontsize=8.5)
    save(fig, "m5_did_two_lines")

# ------------------------------------------------------ 19b. event study
def f_event_study():
    fig, axes = plt.subplots(1, 2, figsize=B, sharey=True)
    for ax, f, ttl, col in [
        (axes[0], "injaz_regions_panel.csv", "Parallel trends HOLD — the estimate is credible", TEAL),
        (axes[1], "injaz_regions_panel_pretrend.csv", "Parallel trends FAIL — the estimate is not causal", RED)]:
        p = pd.read_csv(D + f)
        es = event_study(p, "completion_rate", "region", "period",
                         "months_since_activation", window=(-6, 8))
        pre = es[es.rel_time < 0]; post = es[es.rel_time >= 0]
        ax.axhline(0, color=MUTED, lw=1.2); ax.axvline(-0.5, color=NAVY, lw=1.4, ls=":")
        for sub, c in [(pre, col if col == RED else SLATE), (post, BLUE)]:
            ax.errorbar(sub.rel_time, sub.coef * 100,
                        yerr=[(sub.coef - sub.ci_low) * 100, (sub.ci_high - sub.coef) * 100],
                        fmt="o", color=c, ms=5, lw=1.6, capsize=3)
        ax.set_title(ttl, fontsize=10, color=col)
        ax.set_xlabel("Months since activation")
        ax.axvspan(-6.6, -0.5, color=col, alpha=0.06)
    axes[0].set_ylabel("Effect on completion rate (pp)")
    axes[0].text(-3.3, 3.6, "pre-period\nflat = good", fontsize=8.5, color=SLATE, ha="center")
    axes[1].text(-3.3, 3.6, "pre-period\nalready rising", fontsize=8.5, color=RED,
                 ha="center", fontweight="bold")
    fig.suptitle("The event study is where a difference-in-differences earns — or loses — the room",
                 fontsize=11, y=1.03, color=NAVY, fontweight="bold")
    save(fig, "m5_event_study")

# ------------------------------------------------------- 20. IV as a valve
def f_iv():
    fig, ax = canvas(A, (0, 100), (0, 50))
    label(ax, 50, 47, "An instrument is a source of variation the confounder cannot reach",
          fs=9.8, color=NAVY, bold=True)
    node(ax, 13, 24, "distance to\nthe office\n(Z)", r=9, color=TEAL, fs=7.5)
    node(ax, 45, 24, "files\nonline\n(T)", r=9, color=BLUE, fs=8)
    node(ax, 80, 24, "completes\nservice\n(Y)", r=9.5, color=ORANGE, fs=8)
    node(ax, 62.5, 42, "motivation\n(unobserved)", r=8.5, color=PURPLE, fs=7)
    arrow(ax, (22.5, 24), (35.5, 24), color=TEAL, lw=2.6)
    arrow(ax, (54.5, 24), (70, 24), color=BLUE, lw=2.6)
    arrow(ax, (57, 36), (48, 31.5), color=PURPLE, lw=2.2, ls=(0, (4, 3)))
    arrow(ax, (68.5, 36), (78, 32), color=PURPLE, lw=2.2, ls=(0, (4, 3)))
    label(ax, 29, 27.5, "1 · RELEVANCE\nF = 2,340", fs=8, color=TEAL, bold=True)
    label(ax, 62, 27.5, "the causal\nquestion", fs=8, color=BLUE)
    label(ax, 62.5, 33, "confounds both — this is\nwhy OLS is biased", fs=7.5, color=PURPLE)
    # the blocked direct path
    arrow(ax, (16, 15), (76, 15), color=MUTED, lw=2.0, ls=(0, (5, 4)), rad=-0.20)
    ax.plot([46], [8.6], marker="X", ms=17, color=RED, zorder=6)
    label(ax, 46, 4.4, "2 · EXCLUSION — distance must not affect completion any other way\n"
                       "(NOT testable: this is the assumption you defend in the memo)",
          fs=8.2, color=RED, bold=True)
    save(fig, "m5_iv_valve")

# ------------------------------------------------- 21. the three junctions
def f_junctions():
    fig, axes = plt.subplots(1, 3, figsize=B)
    specs = [
        ("CHAIN     A → B → C", [(10, 25), (50, 25), (90, 25)],
         [(0, 1), (1, 2)], PURPLE,
         "B is a MEDIATOR.\nOpen by default.\nConditioning on B BLOCKS\nthe causal path — never do it."),
        ("FORK     A ← B → C", [(10, 12), (50, 38), (90, 12)],
         [(1, 0), (1, 2)], ORANGE,
         "B is a CONFOUNDER.\nOpen by default.\nConditioning on B BLOCKS\nthe spurious path — do it."),
        ("COLLIDER     A → B ← C", [(10, 38), (50, 12), (90, 38)],
         [(0, 1), (2, 1)], TEAL,
         "B is a COLLIDER.\nBLOCKED by default.\nConditioning on B OPENS\na spurious path — never do it."),
    ]
    for ax, (ttl, pos, edges, col, note) in zip(axes, specs):
        ax.set_xlim(-8, 108); ax.set_ylim(-30, 52); ax.axis("off")
        names = ["A", "B", "C"]
        cols = [SLATE, col, SLATE]
        for (x, y), n, c in zip(pos, names, cols):
            node(ax, x, y, n, r=8, color=c, fs=11)
        for i, j in edges:
            arrow(ax, pos[i], pos[j], color=MUTED, lw=2.2)
        ax.set_title(ttl, fontsize=10.5, color=NAVY, pad=8)
        ax.text(50, -12, note, ha="center", va="center", fontsize=8.3, color=NAVY,
                linespacing=1.6,
                bbox=dict(boxstyle="round,pad=0.55", facecolor=PANEL, edgecolor="none"))
    fig.suptitle("Three junctions. Learn these and d-separation is just bookkeeping.",
                 fontsize=11.5, y=1.02, color=NAVY, fontweight="bold")
    save(fig, "m6_three_junctions")

# ----------------------------------------------- 22. backdoor on the DAG
def f_backdoor():
    # Short display labels so nothing overflows a node
    NICE = {"age": "age", "digital_literacy": "digital\nliteracy",
            "device_age": "device\nage", "uses_uploader": "uses\nuploader",
            "support_calls": "support\ncalls", "completed": "completed",
            "region": "region", "service_complexity": "service\ncomplexity"}
    g0 = injaz_uploader_dag()
    dag = InjazDAG(g0)
    adj = {NICE[a] for a in dag.minimal_adjustment_set()}
    g = nx.relabel_nodes(g0, NICE)
    T, Y = NICE["uses_uploader"], NICE["completed"]
    pos = {NICE["age"]: (0.07, 0.92), NICE["digital_literacy"]: (0.33, 0.88),
           NICE["device_age"]: (0.07, 0.48), NICE["uses_uploader"]: (0.33, 0.13),
           NICE["support_calls"]: (0.63, 0.13), NICE["completed"]: (0.90, 0.50),
           NICE["region"]: (0.63, 0.88), NICE["service_complexity"]: (0.88, 0.90)}

    fig, ax = plt.subplots(figsize=A)
    NS = 3300
    nx.draw_networkx_edges(g, pos, ax=ax, edge_color=MUTED, width=1.5,
                           arrowsize=15, node_size=NS)
    # backdoor paths (adjust for these)
    for e in [(NICE["digital_literacy"], T), (NICE["digital_literacy"], Y),
              (NICE["device_age"], T), (NICE["device_age"], Y)]:
        nx.draw_networkx_edges(g, pos, ax=ax, edgelist=[e], edge_color=TEAL,
                               width=2.6, style="dashed", arrowsize=16, node_size=NS)
    # the mediator route
    for e in [(T, NICE["support_calls"]), (NICE["support_calls"], Y)]:
        nx.draw_networkx_edges(g, pos, ax=ax, edgelist=[e], edge_color=RED,
                               width=2.2, arrowsize=16, node_size=NS)
    # the effect of interest
    nx.draw_networkx_edges(g, pos, ax=ax, edgelist=[(T, Y)], edge_color=ORANGE,
                           width=3.4, arrowsize=20, node_size=NS)

    colors = [BLUE if n == T else ORANGE if n == Y else TEAL if n in adj else SLATE
              for n in g.nodes]
    nx.draw_networkx_nodes(g, pos, ax=ax, node_color=colors, node_size=NS,
                           edgecolors="white", linewidths=2)
    nx.draw_networkx_labels(g, pos, ax=ax, font_size=7.2, font_color="white")

    ax.text(0.02, 0.06, "TEAL = the backdoor set\nADJUST FOR THESE TWO", fontsize=8.5,
            color=TEAL, fontweight="bold", ha="left", va="center")
    ax.text(0.685, 0.335, "the effect of interest", fontsize=8, color=ORANGE,
            fontweight="bold", ha="center", rotation=13)
    ax.text(0.48, -0.055, "MEDIATOR — adjusting for support_calls "
            "erases part of the very effect being measured",
            fontsize=8, color=RED, ha="center", fontweight="bold")
    ax.set_title("Backdoor criterion: the adjustment set is derived, not debated",
                 fontsize=10.5)
    ax.set_xlim(-0.04, 1.02); ax.set_ylim(-0.12, 1.03); ax.axis("off")
    save(fig, "m6_backdoor_dag")

# ------------------------------------------------- 23. collider scatter
def f_collider():
    d = pd.read_parquet(D + "collider_sim.parquet").sample(4000, random_state=3)
    fig, axes = plt.subplots(1, 2, figsize=A, sharex=True, sharey=True)
    for ax, sub, ttl, col in [
        (axes[0], d, "Everyone", SLATE),
        (axes[1], d[d.completed == 1], "Only users who COMPLETED", RED)]:
        ax.scatter(sub.digital_literacy, sub.service_simplicity, s=7, alpha=0.30,
                   color=col, edgecolors="none")
        r = np.corrcoef(sub.digital_literacy, sub.service_simplicity)[0, 1]
        b = np.polyfit(sub.digital_literacy, sub.service_simplicity, 1)
        xr = np.linspace(0.05, 0.98, 10)
        ax.plot(xr, np.polyval(b, xr), color=col, lw=2.8)
        ax.set_title(f"{ttl}\ncorrelation = {r:+.3f}", fontsize=10, color=col)
        ax.set_xlabel("Digital literacy")
    axes[0].set_ylabel("Service simplicity")
    fig.suptitle("Nothing changed in the world — only which rows you looked at",
                 fontsize=11, y=1.02, color=NAVY, fontweight="bold")
    save(fig, "m6_collider_scatter")

# --------------------------------------- 24. identification verdict flow
def f_identification_flow():
    fig, ax = canvas(B, (0, 121), (0, 38))
    label(ax, 60, 36, "The professional answer is one of four — and one of them is 'no'",
          fs=10.5, color=NAVY, bold=True)
    box(ax, 2, 14, 20, 11, "Draw the DAG.\nCan the backdoor\npaths be blocked?",
        fc=NAVY, ec=NAVY, tc="white", fs=8.5, bold=True)
    rail = 30.5
    ax.plot([22, 22], [19.5, rail], color=MUTED, lw=1.8)
    ax.plot([22, 104.5], [rail, rail], color=MUTED, lw=1.8)
    branches = [
        (26, TEAL, "YES — all measured",
         "ADJUST\nregression, matching, IPW\non the backdoor set"),
        (58, BLUE, "NO — but a valid instrument exists",
         "INSTRUMENT\n2SLS; report the LATE\nand defend exclusion"),
        (90, ORANGE, "NO — but a full mediator is measured",
         "FRONTDOOR\nrare in practice;\ncheck no direct path"),
    ]
    for x, c, q, a in branches:
        cx = x + 14.5
        arrow(ax, (cx, rail), (cx, 26.6), color=c, lw=2.0)
        box(ax, x, 20.5, 29, 6, q, fc="white", ec=c, tc=NAVY, fs=8.2, lw=1.8)
        arrow(ax, (cx, 20), (cx, 18.4), color=c, lw=2.0)
        box(ax, x, 8.5, 29, 10, a, fc=c, ec=c, tc="white", fs=8.2)
    box(ax, 26, 1.0, 93, 6,
        "NONE OF THE ABOVE  →  NOT IDENTIFIABLE.  Say so, name the variable you would need, "
        "and propose the design that would get it.",
        fc="#FBE9E7", ec=RED, tc=RED, fs=8.5, bold=True, lw=1.8)
    save(fig, "m6_identification_flow")

# ------------------------------------------ 25. method-selection flowchart
def f_method_selection():
    fig, ax = canvas(B, (0, 121), (0, 40))
    label(ax, 60, 38, "Method selection is itself a causal decision — make it before you touch data",
          fs=10.5, color=NAVY, bold=True)
    qs = [(2,  "Can you\nrandomise\ngoing forward?", BLUE),
          (26, "Did it turn on at\ndifferent times in\ndifferent units?", PURPLE),
          (50, "Is there a valid\ninstrument?", TEAL),
          (74, "Are all confounders\nMEASURED?", ORANGE)]
    for x, q, c in qs:
        box(ax, x, 20, 21, 11, q, fc="white", ec=c, tc=NAVY, fs=8.2, lw=1.8)
    for x in (23, 47, 71):
        arrow(ax, (x, 25.5), (x + 2.6, 25.5), lw=1.8)
        label(ax, x + 1.3, 28.2, "no", fs=7.5, color=MUTED)
    answers = [(2, "A/B TEST\nthe gold standard", BLUE),
               (26, "DIFFERENCE-IN-\nDIFFERENCES\n+ event study", PURPLE),
               (50, "INSTRUMENTAL\nVARIABLES\nreport the LATE", TEAL),
               (74, "MATCHING / IPW\n+ sensitivity analysis", ORANGE)]
    for x, a, c in answers:
        arrow(ax, (x + 10.5, 19.5), (x + 10.5, 16.5), color=c, lw=2.0)
        box(ax, x, 6, 21, 10, a, fc=c, ec=c, tc="white", fs=8.2, bold=True)
        label(ax, x + 10.5, 17.8, "yes", fs=7.5, color=c, bold=True)
    arrow(ax, (95, 25.5), (97.6, 25.5), lw=1.8)
    box(ax, 98, 6, 21, 25,
        "NOT IDENTIFIABLE\n\nName the missing\nvariable. Propose the\ndesign that would\n"
        "measure it. Do not\nship a number you\ncannot defend.",
        fc="#FBE9E7", ec=RED, tc=RED, fs=8.2, lw=1.8, bold=True)
    save(fig, "m7_method_selection")

# ---------------------------------------------- 26. engagement pipeline
def f_engagement():
    fig, ax = canvas(B, (0, 121), (0, 30))
    label(ax, 60, 27.5, "The order is the method. Doing step 4 before step 3 is how analyses go wrong.",
          fs=10.5, color=NAVY, bold=True)
    steps = [("1 · FRAME", "what decision,\nwhat estimand?", SLATE),
             ("2 · DESIGN", "unit, OEC,\nguardrails", BLUE),
             ("3 · POWER", "n, MDE,\nrun length", PURPLE),
             ("4 · ANALYSE", "effect + honest\nvariance", ORANGE),
             ("5 · VALIDATE", "refute, sensitivity,\nguardrails", TEAL),
             ("6 · DECIDE", "memo with a\nrecommendation", NAVY)]
    w, gap = 17.5, 3.0
    for i, (t, sub, c) in enumerate(steps):
        x = 2 + i * (w + gap)
        box(ax, x, 7, w, 12, f"{t}\n\n{sub}", fc=c if i == 5 else "white", ec=c,
            tc="white" if i == 5 else NAVY, fs=8.2, lw=1.8, bold=(i == 5))
        if i < 5:
            arrow(ax, (x + w + 0.3, 13), (x + w + gap - 0.3, 13), lw=2.0)
    # the freeze gate between 3 and 4
    gx = 2 + 3 * (w + gap) - gap / 2
    ax.plot([gx, gx], [4.5, 21.5], color=RED, lw=2.4, ls=(0, (4, 3)), zorder=5)
    label(ax, gx, 22.8, "🔒 FREEZE THE PLAN", fs=8.5, color=RED, bold=True)
    label(ax, gx, 2.5, "nothing about the analysis may change after this line",
          fs=8, color=RED, bold=True)
    save(fig, "m7_engagement_pipeline")

# ------------------------------------------------- 27 + 28. decision plot
def f_decision():
    from causal_utils.reporting import decision_plot
    from causal_utils.analysis import regression_effect
    a = pd.read_csv(D + "injaz_autofill_ab.csv"); a = a[a.triggered == 1]
    au = regression_effect(a, "completed", "variant", ["prior_completion_rate"],
                           label="AI autofill  (A/B test)")
    p = pd.read_csv(D + "injaz_regions_panel.csv")
    dd = did_twfe(p, "completion_rate", "region", "period", "treated_post")
    dd.label = "Regional reminders  (DiD)"
    u = pd.read_csv(D + "injaz_users.csv")
    m = match_nearest(u, "enrolled_training", "completed",
                      ["age", "device_age_years", "digital_literacy_score",
                       "prior_sessions", "prior_completion_rate", "region"],
                      caliper=0.02)
    m.label = "Literacy training  (matching)"
    fig, ax = plt.subplots(figsize=A)
    decision_plot([au, dd, m], threshold=0.01, ax=ax,
                  title="Three interventions, one threshold, one page")
    ax.text(0.5, -0.30,
            "Autofill is significant yet its interval STRADDLES the threshold "
            "→ hold and extend, not ship.",
            transform=ax.transAxes, ha="center", fontsize=9, color=RED,
            fontweight="bold")
    save(fig, "m7_decision_plot")

    fig, ax = canvas(A, (0, 100), (0, 50))
    label(ax, 50, 47, "Reading a confidence interval as a decision", fs=10.5,
          color=NAVY, bold=True)
    zones = [(6, RED, "entirely\nbelow zero", "ROLL BACK\nthis is a harm"),
             (30, SLATE, "straddles\nzero", "INCONCLUSIVE\nsay what is still possible"),
             (54, ORANGE, "positive, straddles\nthe threshold", "HOLD / EXTEND\ncannot yet justify the build"),
             (78, TEAL, "entirely above\nthe threshold", "SHIP\nthe decision is made")]
    for x, c, top, bottom in zones:
        box(ax, x, 26, 18, 12, top, fc="white", ec=c, tc=NAVY, fs=8.5, lw=1.8)
        arrow(ax, (x + 9, 25.5), (x + 9, 21.5), color=c, lw=2.0)
        box(ax, x, 9, 18, 12, bottom, fc=c, ec=c, tc="white", fs=8.5, bold=True)
    label(ax, 50, 3.5,
          "A p-value cannot distinguish the middle two. That is why leadership never receives one.",
          fs=8.8, color=NAVY, bold=True)
    save(fig, "m7_uncertainty_to_decision")


for f in [f_ladder, f_overlap, f_did_lines, f_event_study, f_iv, f_junctions,
          f_backdoor, f_collider, f_identification_flow, f_method_selection,
          f_engagement, f_decision]:
    f()
