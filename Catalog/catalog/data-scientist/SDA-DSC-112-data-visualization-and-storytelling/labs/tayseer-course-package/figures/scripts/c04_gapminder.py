"""Gapminder — the animated bubble chart, and the Robertson et al. (2008) finding
   that the same data as small multiples is faster AND more accurate for analysis."""
import pandas as pd, numpy as np, matplotlib.pyplot as plt
import plotly.express as px
from canon_style import *

g = px.data.gapminder()
CONT = {"Africa": ORANGE, "Americas": GREEN, "Asia": BLUE, "Europe": PURPLE, "Oceania": TEAL}

fig = plt.figure(figsize=(W, H))
gs = fig.add_gridspec(1, 2, width_ratios=[1.05, 1.25], wspace=0.20)
axb = fig.add_subplot(gs[0]); gsr = gs[1].subgridspec(2, 3, wspace=0.12, hspace=0.38)

# ---- LEFT: one frame of the animation -----------------------------------
d = g[g.year == 2007]
axb.scatter(d.gdpPercap, d.lifeExp, s=d["pop"]/2.2e5, alpha=0.55, lw=0.6,
            edgecolor="white", c=[CONT[c] for c in d.continent], zorder=3)
axb.set_xscale("log"); axb.set_xlim(200, 60000); axb.set_ylim(35, 85)
axb.set_xlabel("Income per person (GDP per capita, PPP $, log scale)")
axb.set_ylabel("Life expectancy at birth (years)")
axb.set_xticks([300, 1000, 3000, 10000, 30000])
axb.set_xticklabels(["300", "1k", "3k", "10k", "30k"])
despine(axb); axb.grid(color=LIGHT, lw=0.6); axb.set_axisbelow(True)
axb.text(0.965, 0.07, "2007", transform=axb.transAxes, fontsize=44, color="#E4E8F1",
         ha="right", va="bottom", fontweight="bold", zorder=1)
for lab, x, y, ha in [("China", 4959, 73.0, "center"), ("India", 2452, 64.7, "center"),
                      ("United States", 42951, 78.2, "right"), ("Japan", 31656, 82.6, "right"), ("Nigeria", 2014, 46.9, "center")]:
    axb.annotate(lab, (x, y), xytext=(0, 13), textcoords="offset points",
                 fontsize=7.5, color=INK, ha=ha)
hs = [plt.Line2D([], [], marker="o", ls="", ms=6, color=c, label=k) for k, c in CONT.items()]
axb.legend(handles=hs, fontsize=7.5, loc="upper left", ncol=2, handletextpad=0.3, columnspacing=0.9)
head(axb, "one frame of the animation",
     "Gapminder, 2007 — one frame of a 55-year animation", dy=0.03)

# ---- RIGHT: the same data as small multiples ----------------------------
agg = (g.assign(gdp=g.gdpPercap*g["pop"])
         .groupby(["continent", "year"]).apply(
            lambda x: pd.Series({"life": np.average(x.lifeExp, weights=x["pop"]),
                                 "inc": x.gdp.sum()/x["pop"].sum()}), include_groups=False)
         .reset_index())
order = ["Africa", "Americas", "Asia", "Europe", "Oceania"]
axes = []
for i, cont in enumerate(order):
    ax = fig.add_subplot(gsr[i//3, i % 3]); axes.append(ax)
    sub = agg[agg.continent == cont]
    for other in order:
        o = agg[agg.continent == other]
        ax.plot(o.year, o.life, color="#E1E5EE", lw=1.0, zorder=1)
    ax.plot(sub.year, sub.life, color=CONT[cont], lw=2.0, zorder=3)
    ax.set_ylim(28, 82); ax.set_xlim(1952, 2007)
    ax.set_title(cont, fontsize=8.5, color=NAVY, fontweight="bold", pad=3)
    despine(ax, keep=("left", "bottom") if i % 3 == 0 else ("bottom",))
    ax.set_xticks([1960, 1990]); ax.tick_params(labelsize=6.5)
    if i % 3: ax.set_yticks([])
    else: ax.set_yticks([40, 60, 80])
axn = fig.add_subplot(gsr[1, 2]); axn.axis("off")
axn.text(0, 0.98, "Robertson et al., IEEE TVCG 2008\nEffectiveness of Animation in Trend Visualization",
         fontsize=7.4, color=NAVY, fontweight="bold", va="top")
axn.text(0, 0.60, "For ANALYSIS, mean time on task:\n"
                  "   small multiples   45.7 s\n"
                  "   traces                55.0 s\n"
                  "   animation           83.1 s\n"
                  "and small multiples were significantly\nmore accurate (p < .001).\n\n"
                  "For PRESENTATION the order reverses:\nanimation 15.8 s, small multiples 25.3 s.",
         fontsize=7.0, color=INK, va="top", linespacing=1.5)
fig.text(0.548, 0.935, "THE SAME DATA, FOR A DIFFERENT JOB", fontsize=7.5, color=ORANGE, fontweight="bold")
fig.text(0.548, 0.875, "Population-weighted life expectancy, as small multiples", fontsize=11.5, color=NAVY, fontweight="bold")

footnote(fig, "Left: rendered from the Gapminder dataset shipped with plotly.express (1,704 rows, 142 countries, 1952–2007). "
              "Right: the same series as small multiples, each panel against all five in grey. "
              "The teaching point is not that animation is bad — it is that Rosling's chart is a PRESENTATION artefact whose attention is carried by a narrator. "
              "Take the narrator away and comparison becomes a change-blindness problem: the viewer must hold earlier positions in working memory, and cannot compare two non-adjacent years at all.")
fig.subplots_adjust(top=0.80, bottom=0.12, left=0.045, right=0.995)
save(fig, "canon_04_gapminder")
