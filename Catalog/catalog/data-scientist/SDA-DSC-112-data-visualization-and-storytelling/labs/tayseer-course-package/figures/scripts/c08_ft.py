"""FT / John Burn-Murdoch — days since the 100th case, log scale, doubling guides;
   and the Romano et al. (2020) finding that the same chart misleads a general audience."""
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from canon_style import *

j = pd.read_csv("CSSEGISandData_COVID-19_master_csse_covid_19_data_csse_covid_19_time_series_time_series_covid19_confirmed_global.csv")
j = j.groupby("Country/Region").sum(numeric_only=True).drop(columns=["Lat", "Long"])
j.columns = pd.to_datetime(j.columns)
SEL = {"Italy": NAVY, "Spain": ORANGE, "US": PURPLE, "United Kingdom": BLUE,
       "Korea, South": TEAL, "Japan": GREEN}

def aligned(c, thresh=100, days=40):
    s = j.loc[c]; s = s[s >= thresh]
    return np.arange(min(len(s), days)), s.values[:days]

fig, (axl, axr) = plt.subplots(1, 2, figsize=(W, H), gridspec_kw={"wspace": 0.20})

YMAX = 2.5e5
for ax, logscale in ((axl, True), (axr, False)):
    for dbl, lab in ((2, "doubles\nevery 2 days"), (3, "every\n3 days"), (7, "every\nweek")):
        t = np.arange(0, 46); ax.plot(t, 100 * 2 ** (t / dbl), color="#E1E5EE", lw=0.9, zorder=1)
        if logscale:
            xx = dbl * np.log2(YMAX / 100)            # where the guide exits the top
            ax.text(xx + 0.5, YMAX * 0.99, lab, fontsize=6.6, color=MUTED,
                    va="top", ha="left", linespacing=1.3)
    for c, col in SEL.items():
        x, y = aligned(c)
        keep = y <= YMAX * 0.985
        ax.plot(x[keep], y[keep], color=col, lw=2.0, zorder=3)
        xi, yi = x[keep][-1], y[keep][-1]
        ax.annotate(f"  {c}", (xi, yi), fontsize=7.8, color=col,
                    fontweight="bold", va="center", annotation_clip=False)
    if logscale:
        ax.set_yscale("log"); ax.set_ylim(90, YMAX); ax.set_xlim(0, 47)
        ax.set_yticks([100, 1000, 10000, 100000])
        ax.set_yticklabels(["100", "1,000", "10,000", "100,000"])
    else:
        ax.set_ylim(0, YMAX); ax.set_xlim(0, 47)
        ax.set_yticks([0, 50000, 100000, 150000, 200000])
        ax.set_yticklabels(["0", "50k", "100k", "150k", "200k"])
    ax.set_xlabel("Days since the 100th confirmed case")
    ax.set_ylabel("Cumulative confirmed cases")
    despine(ax); ax.grid(axis="y", color=LIGHT, lw=0.6); ax.set_axisbelow(True)

axl.text(0.035, 0.30, "On a log scale the SLOPE is the growth rate,\nso the reader's task becomes comparing slopes\nagainst the doubling-time guides.",
         transform=axl.transAxes, fontsize=8.2, color=INK, va="top", linespacing=1.5,
         bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=2))
axr.text(0.035, 0.985, "On a linear scale the same reader sees magnitude\nand danger — and every country not yet in crisis\nis squashed into the bottom-left corner.",
         transform=axr.transAxes, fontsize=8.2, color=INK, va="top", linespacing=1.5)
head(axl, "march 2020  ·  the chart that taught the world to read exponentials",
     "Log scale — correct for the analytic task", dy=0.03)
head(axr, "romano et al., health economics 2020", "Linear — correct for the audience task", ORANGE, dy=0.03)

footnote(fig, "Built from the Johns Hopkins CSSE global confirmed-case series, aligned on each country's 100th case — Burn-Murdoch's design, first published 11 March 2020, made in R/ggplot2. "
              "Romano, Sotis, Dominioni & Guidi (Health Economics 29(11), 1482–1494) found that showing COVID deaths on a log scale left people with a LESS accurate understanding of the pandemic's development and shifted their policy preferences, and recommended a linear scale as the default for general audiences. "
              "The honest lesson: the same well-designed chart is right or misleading depending on which question the reader brought to it. Ask that question before choosing the scale.")
fig.subplots_adjust(top=0.82, bottom=0.14, left=0.055, right=0.915)
save(fig, "canon_08_ft_log")
