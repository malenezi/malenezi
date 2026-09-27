"""SDAIA Academy plotting style — matches the course deck exactly."""
from __future__ import annotations
import matplotlib as mpl
import matplotlib.pyplot as plt

NAVY   = "#16233F"
BLUE   = "#3FA9E0"
PURPLE = "#5A5BA6"
ORANGE = "#EA7B38"
TEAL   = "#3E9B90"
SKY    = "#70C8F2"
SLATE  = "#566581"
MUTED  = "#8A98AE"
PANEL  = "#F4F7FB"
RED    = "#C0392B"
GREEN  = "#2E8B57"

SEQUENCE = [BLUE, ORANGE, PURPLE, TEAL, SKY, SLATE]


def use_sdaia_style(base_size: int = 11) -> None:
    """Apply the deck palette and typography to every subsequent figure."""
    mpl.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": MUTED,
        "axes.linewidth": 0.9,
        "axes.labelcolor": NAVY,
        "axes.titlecolor": NAVY,
        "axes.titlesize": base_size + 3,
        "axes.titleweight": "bold",
        "axes.labelsize": base_size,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": "#E3E9F2",
        "grid.linewidth": 0.8,
        "xtick.color": SLATE,
        "ytick.color": SLATE,
        "xtick.labelsize": base_size - 1,
        "ytick.labelsize": base_size - 1,
        "text.color": NAVY,
        "legend.frameon": False,
        "legend.fontsize": base_size - 1,
        "font.family": "sans-serif",
        "font.sans-serif": ["Carlito", "Calibri", "DejaVu Sans"],
        "axes.prop_cycle": mpl.cycler(color=SEQUENCE),
        "figure.dpi": 110,
        "savefig.dpi": 220,
        "savefig.bbox": "tight",
    })
