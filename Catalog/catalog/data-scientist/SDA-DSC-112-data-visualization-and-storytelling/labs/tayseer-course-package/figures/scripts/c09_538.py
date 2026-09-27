"""FiveThirtyEight-style uncertainty displays — the distribution instead of the estimate,
   and frequency framing instead of a bare percentage."""
import numpy as np, matplotlib.pyplot as plt
from canon_style import *

rng = np.random.default_rng(2020)
ev = np.clip(np.round(rng.normal(302, 56, 40000)), 80, 500).astype(int)   # simulated electoral votes
pwin = (ev >= 270).mean()

fig = plt.figure(figsize=(W, H))
gs = fig.add_gridspec(1, 3, width_ratios=[1.25, 1.15, 0.85], wspace=0.24)
axh = fig.add_subplot(gs[0]); axq = fig.add_subplot(gs[1]); axt = fig.add_subplot(gs[2])

# ---- 1. the full distribution -------------------------------------------
bins = np.arange(ev.min(), ev.max()+4, 4)
n, b, patches = axh.hist(ev, bins=bins, lw=0)
for p, left in zip(patches, b[:-1]):
    p.set_facecolor(BLUE if left >= 270 else "#E3C3AE")
axh.axvline(270, color=NAVY, lw=1.6)
axh.text(274, axh.get_ylim()[1]*0.93, "270 to win", fontsize=8, color=NAVY, fontweight="bold")
axh.set_xlabel("Electoral votes in each of 40,000 simulated elections")
axh.set_ylabel("Simulations")
despine(axh); axh.grid(axis="y", color=LIGHT, lw=0.6); axh.set_axisbelow(True)
head(axh, "show the distribution, not the estimate",
     "Every outcome the model thinks is possible", dy=0.03)

# ---- 2. quantile dotplot of the same thing ------------------------------
K = 50
qs = np.quantile(ev, (np.arange(K) + 0.5) / K)
edges = np.linspace(qs.min(), qs.max(), 26)
idx = np.clip(np.digitize(qs, edges) - 1, 0, len(edges)-2)
xs, ys, cs = [], [], []
for i in range(len(edges)-1):
    inb = qs[idx == i]
    for k, _ in enumerate(inb):
        c = (edges[i] + edges[i+1]) / 2
        xs.append(c); ys.append(k + 0.5); cs.append(BLUE if c >= 270 else "#E3C3AE")
axq.scatter(xs, ys, s=58, c=cs, edgecolor="white", lw=0.7, zorder=3)
axq.axvline(270, color=NAVY, lw=1.6)
nwin = int(round(pwin*K))
axq.set_xlabel("Electoral votes — 50 dots, each 1 outcome in 50")
axq.set_ylabel("Count"); axq.set_ylim(0, max(ys)+2)
despine(axq); axq.grid(axis="y", color=LIGHT, lw=0.6); axq.set_axisbelow(True)
axq.text(0.62, 0.95, f"{nwin} of these 50 dots\nare to the right of 270.\nYou can count them.",
         transform=axq.transAxes, fontsize=8.5, color=NAVY, fontweight="bold",
         va="top", linespacing=1.5, ha="left")
head(axq, "…then let people count it", "The same forecast as a quantile dotplot", ORANGE, dy=0.03)

# ---- 3. framing -----------------------------------------------------------
axt.axis("off")
axt.add_patch(plt.Rectangle((0.0, 0.56), 1.0, 0.40, transform=axt.transAxes,
                            facecolor="#FBECEC", edgecolor=RED, lw=1.0))
axt.text(0.05, 0.895, "PROBABILITY FRAMING", transform=axt.transAxes, fontsize=8,
         color=RED, fontweight="bold")
axt.text(0.05, 0.80, f"“{pwin*100:.0f}% chance of winning”", transform=axt.transAxes,
         fontsize=12, color=NAVY, fontweight="bold")
axt.text(0.05, 0.70, "Read by most audiences as\n“going to win”. In 2016 the least\nconfident mainstream forecast —\n29% for Trump — was the one\ncalled wrong.",
         transform=axt.transAxes, fontsize=8, color=INK, va="top", linespacing=1.5)
axt.add_patch(plt.Rectangle((0.0, 0.06), 1.0, 0.40, transform=axt.transAxes,
                            facecolor="#E9F5EC", edgecolor=GREEN, lw=1.0))
axt.text(0.05, 0.395, "FREQUENCY FRAMING", transform=axt.transAxes, fontsize=8,
         color=GREEN, fontweight="bold")
axt.text(0.05, 0.30, f"“Wins {nwin} times in 50”", transform=axt.transAxes,
         fontsize=12, color=NAVY, fontweight="bold")
axt.text(0.05, 0.20, "Countable, and it makes the\nlosing outcomes visible. This is\nwhat the dotplot draws.",
         transform=axt.transAxes, fontsize=8, color=INK, va="top", linespacing=1.5)

footnote(fig, "A reconstruction of the TECHNIQUES, with simulated numbers — not a reproduction of any published forecast. "
              "FiveThirtyEight was shut down on 5 March 2025 and its archive now redirects away from fivethirtyeight.com, so every 538 link must go through web.archive.org; the successors are Nate Silver's Silver Bulletin and G. Elliott Morris's Strength in Numbers. "
              "Quantile dotplots: Kay, Kola, Hullman & Munson, CHI 2016; Fernandes et al., CHI 2018 — 50-dot quantile dotplots produced transit decisions at 97% of optimal expected payoff and were more consistent than the control. "
              "Hypothetical outcome plots: Hullman, Resnick & Adar, PLOS ONE 2015.")
fig.subplots_adjust(top=0.82, bottom=0.14, left=0.05, right=0.995)
save(fig, "canon_09_538_uncertainty")
