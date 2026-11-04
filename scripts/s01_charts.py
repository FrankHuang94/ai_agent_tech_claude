"""Section 01 — Executive Summary charts."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from chartstyle import apply_style, save, PALETTE, INK, MUTED

apply_style()
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "..", "assets", "data")
OUT = os.path.join(HERE, "..", "assets", "charts")

df = pd.read_csv(os.path.join(DATA, "01_category_maturity.csv"))

# --- Chart 1: Maturity vs contestedness bubble map ---
fig, ax = plt.subplots(figsize=(11, 7.5))
x = df["maturity_score"]
y = df["contestedness"]
sizes = (df["bottleneck_severity"] ** 2) * 7

# color by bottleneck severity (sequential)
colors = plt.cm.YlOrRd((df["bottleneck_severity"] - 3) / (9.5 - 3))
sc = ax.scatter(x, y, s=sizes, c=colors, edgecolors="white", linewidths=1.3, alpha=0.9, zorder=3)

# Manual label placement (dx, dy in points, ha) for layers whose bubbles sit close together.
LABEL_POS = {
    "Orchestration frameworks": (0, 12, "center"),
    "Coding agents": (0, -20, "center"),
    "Voice & multimodal": (0, 14, "center"),
    "Infrastructure / runtime": (0, -24, "center"),
    "Retrieval / grounding": (14, -2, "left"),
    "Planning & reasoning": (-16, -6, "right"),
    "Multi-agent coordination": (0, 16, "center"),
    "Memory systems": (14, 8, "left"),
    "Identity & auth": (-20, 0, "right"),
    "Guardrails & security": (0, -30, "center"),
    "Computer-use / browser": (-16, -4, "right"),
    "Evaluation & observability": (16, -4, "left"),
    "Standards & interop": (14, -4, "left"),
}
for _, r in df.iterrows():
    radius = np.sqrt((r["bottleneck_severity"]**2)*7)/2
    dx, dy, ha = LABEL_POS.get(r["category"], (0, radius + 6, "center"))
    if r["category"] in LABEL_POS and abs(dy) > 0 and dx == 0:
        dy = (radius + 4) if dy > 0 else -(radius + 12)
    ax.annotate(r["category"], (r["maturity_score"], r["contestedness"]),
                fontsize=8.5, color=INK, ha=ha, va="center" if dx else "baseline",
                xytext=(dx, dy), textcoords="offset points")

ax.axvline(5.5, color=MUTED, lw=0.8, ls="--", alpha=0.6)
ax.axhline(6.0, color=MUTED, lw=0.8, ls="--", alpha=0.6)
ax.text(9.7, 2.2, "Commoditizing\n(mature, settled)", fontsize=9, color=MUTED, ha="right")
ax.text(1.6, 9.4, "Standards fights\n(immature, contested)", fontsize=9, color=MUTED, ha="left")
ax.set_xlim(1, 10); ax.set_ylim(1.5, 10)
ax.set_xlabel("Delivery maturity  (1 = research-only  →  10 = commoditized)")
ax.set_ylabel("Contestedness  (1 = settled  →  10 = active standards fight)")
ax.set_title("AI agent stack: maturity vs. contestedness by layer", loc="left", pad=26)
ax.text(0, 1.03, "Bubble size = bottleneck severity (larger = bigger drag on end-to-end agent reliability)",
        transform=ax.transAxes, fontsize=10, color=MUTED)
fig.text(0.01, 0.005, "Source: internal assessment, November 2026 (revised from July 2026). Scores are analyst judgment, not measured metrics.",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "01_maturity_contestedness.png"))

# --- Chart 2: Bottleneck severity ranked bar ---
fig, ax = plt.subplots(figsize=(10, 7))
d2 = df.sort_values("bottleneck_severity")
bar_colors = plt.cm.YlOrRd((d2["bottleneck_severity"] - 3) / (9.5 - 3))
ax.barh(d2["category"], d2["bottleneck_severity"], color=bar_colors, edgecolor="white")
for i, v in enumerate(d2["bottleneck_severity"]):
    ax.text(v + 0.1, i, f"{v:.1f}", va="center", fontsize=9, color=INK)
ax.set_xlim(0, 10)
ax.set_xlabel("Bottleneck severity (drag on end-to-end reliability, 1–10)")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.set_title("Where the agent stack breaks (November 2026)", loc="left", pad=24)
ax.text(0, 1.02, "Higher = this layer is the more common cause of end-to-end agent failure",
        transform=ax.transAxes, fontsize=10, color=MUTED)
save(fig, os.path.join(OUT, "01_bottleneck_severity.png"))
