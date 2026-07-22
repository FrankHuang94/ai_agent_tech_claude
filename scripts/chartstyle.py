"""Shared matplotlib styling for all charts in the AI Agent Tech database.

Import and call `apply_style()` at the top of every chart script so the whole
repository reads as one visual system. Palette is brand-neutral and chosen for
categorical distinctness and reasonable contrast on a white background.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

# Categorical palette (colorblind-aware, distinct at a glance)
PALETTE = [
    "#2563eb",  # blue
    "#dc2626",  # red
    "#16a34a",  # green
    "#d97706",  # amber
    "#7c3aed",  # violet
    "#0891b2",  # cyan
    "#db2777",  # pink
    "#65a30d",  # lime
    "#475569",  # slate
    "#ea580c",  # orange
]

# Sequential (single-hue) for ordered magnitudes
SEQUENTIAL = ["#dbeafe", "#93c5fd", "#60a5fa", "#3b82f6", "#2563eb", "#1d4ed8", "#1e3a8a"]

INK = "#1f2937"
MUTED = "#6b7280"
GRID = "#e5e7eb"


def apply_style():
    plt.rcParams.update({
        "figure.dpi": 130,
        "savefig.dpi": 130,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "font.size": 11,
        "font.family": "DejaVu Sans",
        "axes.edgecolor": GRID,
        "axes.linewidth": 1.0,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.titlecolor": INK,
        "axes.labelcolor": INK,
        "axes.labelsize": 11,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "text.color": INK,
        "legend.frameon": False,
        "legend.fontsize": 10,
    })


def finish(ax, title=None, subtitle=None, source=None):
    """Apply title/subtitle/source annotations consistently."""
    if title:
        ax.set_title(title, loc="left", pad=18 if subtitle else 10)
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes, fontsize=10.5,
                color=MUTED, ha="left", va="bottom")
    if source:
        ax.figure.text(0.01, 0.005, source, fontsize=8, color=MUTED, ha="left")


def save(fig, path):
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print("wrote", path)
