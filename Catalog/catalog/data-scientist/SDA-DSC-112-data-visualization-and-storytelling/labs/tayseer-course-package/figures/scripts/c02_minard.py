"""Minard 1869 — six variables in one image, recreated from HistData Minard.troops/cities/temp."""
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from canon_style import *

tr = pd.read_csv("Minard.troops.csv"); ci = pd.read_csv("Minard.cities.csv"); te = pd.read_csv("Minard.temp.csv")
TAN, BLACK = "#D9B382", "#2B2B2B"

fig = plt.figure(figsize=(W, H))
gs = fig.add_gridspec(2, 1, height_ratios=[2.3, 1], hspace=0.17)
axm = fig.add_subplot(gs[0]); axt = fig.add_subplot(gs[1], sharex=axm)

SCALE = 0.58 / 340000.0      # degrees of latitude per man
for (grp, dirn), g in tr.groupby(["group", "direction"], sort=False):
    g = g.reset_index(drop=True)
    x, y, s = g.long.values, g.lat.values, g.survivors.values
    hw = s * SCALE / 2
    axm.fill_between(x, y - hw, y + hw, color=TAN if dirn == "A" else BLACK,
                     lw=0, zorder=3 if dirn == "A" else 4)

for _, c in ci.iterrows():
    axm.plot(c.long, c.lat, "o", ms=2.4, color="#7A5C2E", zorder=6)
    axm.text(c.long, c.lat + 0.20, c.city, fontsize=7.2, color="#5A4520",
             ha="center", va="bottom", zorder=7)

axm.annotate("422,000 men cross the Niemen", xy=(24.0, 54.9), xytext=(23.45, 56.75),
             fontsize=9, fontweight="bold", color="#7A5C2E",
             arrowprops=dict(arrowstyle="-", color="#7A5C2E", lw=1.0))
axm.annotate("100,000 reach Moscow", xy=(37.6, 55.8), xytext=(34.9, 56.85),
             fontsize=9, fontweight="bold", color="#7A5C2E",
             arrowprops=dict(arrowstyle="-", color="#7A5C2E", lw=1.0))
axm.annotate("10,000 return", xy=(24.6, 54.25), xytext=(23.45, 53.35),
             fontsize=9, fontweight="bold", color=BLACK,
             arrowprops=dict(arrowstyle="-", color=BLACK, lw=1.0))
axm.annotate("Berezina crossing", xy=(28.5, 54.15), xytext=(29.2, 53.25),
             fontsize=8, color=NAVY,
             arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.9))
axm.set_ylim(52.9, 57.15); axm.set_xlim(23.2, 38.4)
axm.set_xticks([]); axm.set_yticks([]); despine(axm, keep=())
head(axm, "six variables, one image, no legend",
     "Minard, 1869 — Carte figurative des pertes successives de l'Armée Française", dy=0.02)
axm.text(0.995, 0.02, "band width = men   ·   tan = advance, black = retreat   ·   x, y = longitude, latitude   ·   temperature below, aligned by longitude",
         transform=axm.transAxes, fontsize=8, color=GREY, ha="right", va="bottom")

# ---- temperature, aligned by longitude ----------------------------------
axt.plot(te.long, te.temp, color=NAVY, lw=1.6, marker="o", ms=3.5, zorder=3)
KEY = {0: "0° Ré\n18 Oct", 3: "−9° Ré (−11.3 °C)\n9 Nov", 4: "−21° Ré (−26.3 °C)\n14 Nov",
       7: "−30° Ré (−37.5 °C)\n6 Dec — the coldest", 8: "−26° Ré (−32.5 °C)\n7 Dec"}
for i, r in te.reset_index(drop=True).iterrows():
    if i not in KEY: continue
    up = i in (3, 8)
    axt.annotate(KEY[i], xy=(r.long, r.temp), xytext=(0, 11 if up else -10),
                 textcoords="offset points", fontsize=7, color=INK if i != 7 else ORANGE,
                 fontweight="normal" if i != 7 else "bold",
                 ha="center", va="bottom" if up else "top")
axt.set_ylim(-44, 12); axt.set_xlim(23.2, 38.4)
axt.set_yticks([0, -10, -20, -30]); axt.set_yticklabels(["0", "−10", "−20", "−30"])
axt.set_ylabel("Degrees Réaumur", fontsize=8)
axt.set_xticks([]); despine(axt, keep=("left",))
axt.grid(axis="y", color=LIGHT, lw=0.6); axt.set_axisbelow(True)
axt.text(0.0, 1.02, "TEMPERATURE ON THE RETREAT — the units trap: the scale is Réaumur, so °C = °Ré × 1.25 and the minimum is −37.5 °C, not −30",
         transform=axt.transAxes, fontsize=8, color=ORANGE, fontweight="bold", ha="left", va="bottom")

footnote(fig, "Recreated from HistData Minard.troops / Minard.cities / Minard.temp (the standard tabulated transcription of Minard's drawn band widths).  "
              "340,000 + 60,000 + 22,000 = 422,000 in;  4,000 + 6,000 = 10,000 out.  "
              "Documented flaws: the retreat leg is drawn displaced southward (Minard rejected 'the tyranny of precise geographical position'); the straight taper from Vilnius to Vitebsk hides the campaign's worst losses; and the retreat band briefly thickens near long. 26.4.")
fig.subplots_adjust(top=0.845, bottom=0.05, left=0.045, right=0.995)
save(fig, "canon_02_minard")
