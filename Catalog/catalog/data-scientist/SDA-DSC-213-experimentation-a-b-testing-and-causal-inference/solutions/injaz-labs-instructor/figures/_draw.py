"""Shared schematic-drawing helpers in the SDAIA deck style."""
import sys
sys.path.insert(0, "/home/claude/course_assets")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
from matplotlib.lines import Line2D
import numpy as np
from causal_utils.style import (use_sdaia_style, NAVY, BLUE, PURPLE, ORANGE,
                                TEAL, SKY, SLATE, MUTED, PANEL, RED, GREEN)

use_sdaia_style()
OUT = "/home/claude/course_assets/figures"

# Two slide layouts (inches), matching the deck's content geometry
A = (8.60, 4.35)     # figure + right insight panel
B = (12.09, 3.95)    # full-width figure + bottom insight strip


def canvas(size=A, xlim=(0, 100), ylim=(0, 50)):
    fig, ax = plt.subplots(figsize=size)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.axis("off")
    ax.set_facecolor("white")
    return fig, ax


def box(ax, x, y, w, h, text, fc=PANEL, ec=None, tc=NAVY, fs=9, bold=False,
        radius=1.4, lw=1.4, align="center", pad=1.2):
    ec = ec if ec is not None else fc
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0,rounding_size={radius}",
                       facecolor=fc, edgecolor=ec, linewidth=lw, zorder=2)
    ax.add_patch(p)
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=fs, color=tc, zorder=3,
                fontweight="bold" if bold else "normal", linespacing=1.45)
    return p


def chip(ax, x, y, w, h, label, color=BLUE, fs=8.5):
    """A solid coloured pill with white text."""
    return box(ax, x, y, w, h, label, fc=color, ec=color, tc="white",
               fs=fs, bold=True)


def arrow(ax, xy1, xy2, color=MUTED, lw=1.8, style="-|>", ls="-",
          rad=0.0, zorder=1, ms=12):
    a = FancyArrowPatch(xy1, xy2, arrowstyle=style, color=color,
                        linewidth=lw, linestyle=ls, mutation_scale=ms,
                        connectionstyle=f"arc3,rad={rad}", zorder=zorder,
                        shrinkA=2, shrinkB=4)
    ax.add_patch(a)
    return a


def label(ax, x, y, text, fs=8.5, color=SLATE, ha="center", va="center",
          bold=False, style="normal", rot=0):
    return ax.text(x, y, text, fontsize=fs, color=color, ha=ha, va=va,
                   fontweight="bold" if bold else "normal",
                   fontstyle=style, rotation=rot, zorder=4, linespacing=1.45)


def node(ax, x, y, text, r=6.0, color=SLATE, fs=8, tc="white"):
    c = Circle((x, y), r, facecolor=color, edgecolor="white", linewidth=2,
               zorder=3)
    ax.add_patch(c)
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=tc,
            zorder=4, fontweight="bold", linespacing=1.2)
    return c


def save(fig, name):
    path = f"{OUT}/{name}.png"
    fig.savefig(path, dpi=200, bbox_inches="tight", pad_inches=0.06,
                facecolor="white")
    plt.close(fig)
    print("  ", name)
    return path


# ---------------------------------------------------------------- Arabic
import arabic_reshaper
from bidi.algorithm import get_display

AR_FONT = {"fontname": "DejaVu Sans"}


def ar(text: str) -> str:
    """Reshape + bidi-order an Arabic string so matplotlib renders it correctly.
    Always pair with **AR_FONT (Carlito has no Arabic coverage)."""
    return get_display(arabic_reshaper.reshape(text))


def bilingual(ax, x, y, en, arabic, fs=8.5, color=MUTED, ha="center"):
    """One line of English, one of Arabic, stacked — for key-term callouts."""
    ax.text(x, y + 1.6, en, fontsize=fs, color=color, ha=ha, va="center", zorder=4)
    ax.text(x, y - 1.6, ar(arabic), fontsize=fs, color=color, ha=ha, va="center",
            zorder=4, **AR_FONT)
