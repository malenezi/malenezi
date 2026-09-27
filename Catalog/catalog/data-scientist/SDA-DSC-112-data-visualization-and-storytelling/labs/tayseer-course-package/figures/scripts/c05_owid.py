"""Our World in Data — what a grapher chart does that a default chart does not:
   direct labelling, an annotated argument, a stated source and a reuse licence."""
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from canon_style import *

o = pd.read_csv("owid_covid-19-data_master_public_data_cases_deaths_full_data.csv",
                parse_dates=["date"], low_memory=False)
pop = (pd.read_csv("owid_population_latest.csv").set_index("entity")["population"])
sel = ["Saudi Arabia", "United Arab Emirates", "Egypt", "Jordan", "Kuwait", "Oman"]
o = o[o.location.isin(sel) & (o.date <= "2022-12-31")].copy()
o["dpm"] = o.total_deaths / o.location.map(pop) * 1e6
piv = (o.pivot_table(index="date", columns="location", values="dpm")
         .ffill().resample("W").last())
HI, MUT = {"Saudi Arabia": TEAL}, "#CFD6E4"

fig, (axa, axb) = plt.subplots(1, 2, figsize=(W, H), gridspec_kw={"wspace": 0.22})

# ---- A: the default a tool gives you ------------------------------------
for c in piv.columns:
    axa.plot(piv.index, piv[c], lw=1.6, label=c)
axa.legend(fontsize=7.5, loc="upper left", ncol=2)
axa.set_ylabel("Cumulative COVID-19 deaths per million")
axa.grid(color=LIGHT, lw=0.6); axa.set_axisbelow(True); despine(axa)
head(axa, "what the tool gives you by default",
     "Six countries, a legend, and no argument", GREY, dy=0.03)

# ---- B: the same data, grapher-style ------------------------------------
ends = {c: piv[c].dropna().iloc[-1] for c in piv.columns}
placed = []
for c, v in sorted(ends.items(), key=lambda kv: -kv[1]):
    hl = c in HI
    axb.plot(piv.index, piv[c], lw=2.4 if hl else 1.2,
             color=HI.get(c, MUT), zorder=4 if hl else 2)
    y = v
    while any(abs(y - p) < 62 for p in placed):      # simple de-overlap
        y -= 22
    placed.append(y)
    axb.annotate(f"  {c}", (piv.index[-1], v), xytext=(piv.index[-1], y),
                 fontsize=7.8, color=NAVY if hl else GREY,
                 fontweight="bold" if hl else "normal", va="center",
                 annotation_clip=False,
                 arrowprops=dict(arrowstyle="-", color="#DDE2EC", lw=0.7))
ksa = piv["Saudi Arabia"]
axb.annotate("Saudi Arabia ends the period at "
             f"{ksa.iloc[-1]:.0f} deaths per million —\nthe lowest of the six, and roughly a quarter of the highest",
             xy=(ksa.index[-1], ksa.iloc[-1]), xytext=(pd.Timestamp("2020-05-01"), 1080),
             fontsize=8.5, color=NAVY, fontweight="bold",
             arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
axb.set_ylabel("Cumulative COVID-19 deaths per million")
axb.set_xlim(piv.index[0], pd.Timestamp("2023-11-01"))
axb.grid(color=LIGHT, lw=0.6); axb.set_axisbelow(True); despine(axb)
axb.text(0.0, -0.20, "Data: Our World in Data / Global Change Data Lab  ·  Licensed CC BY  ·  ourworldindata.org",
         transform=axb.transAxes, fontsize=7, color=GREY)
head(axb, "what our world in data does instead",
     "Direct labels, one accent, the argument written on the chart", dy=0.03)

footnote(fig, "Both panels plot the identical series from the Our World in Data COVID-19 repository (cases_deaths/full_data.csv, weekly resample). "
              "Nothing was added to the data between the panels — only the design. "
              "OWID's charts, articles and their own data are CC BY, so a training course may reproduce them with attribution; third-party data inside a grapher chart keeps the third party's licence. "
              "Note the Grapher SOURCE CODE is no longer MIT — you may study it, not fork it.")
fig.subplots_adjust(top=0.80, bottom=0.16, left=0.055, right=0.90)
save(fig, "canon_05_owid")
