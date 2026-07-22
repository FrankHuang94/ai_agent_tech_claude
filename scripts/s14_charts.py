"""Section 14 — Enterprise agent platform charts."""
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

# --- Chart 1: market growth ---
df = pd.read_csv(os.path.join(DATA, "14_market_growth.csv"))
fig, ax = plt.subplots(figsize=(10.5, 6.2))
colors = plt.cm.Blues(np.linspace(0.5, 0.95, len(df)))
ax.bar(df["year"].astype(str), df["market_size_busd"], color=colors, edgecolor="white", width=0.62)
for i, v in enumerate(df["market_size_busd"]):
    ax.text(i, v + 0.7, f"${v:.1f}B", ha="center", fontsize=9.5, color=INK)
ax.set_ylabel("AI agents market size (US$ billions)")
ax.set_ylim(0, 58)
ax.set_title("Enterprise AI agent market: $7.8B (2025) → $52.6B (2030)", loc="left", pad=24)
ax.text(0, 1.02, "~46% CAGR — from pilot budgets to production commitments; the enterprise-platform land-grab",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: market projection cited mid-2026 (inferred; single-source estimate, treat as directional).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "14_market_growth.png"))

# --- Chart 2: platform positioning ---
d = pd.read_csv(os.path.join(DATA, "14_platform_positioning.csv"))
fig, ax = plt.subplots(figsize=(11, 7.5))
sizes = (d["adoption"]**2)*10
ax.scatter(d["openness"], d["breadth"], s=sizes, c=[PALETTE[i%len(PALETTE)] for i in range(len(d))],
           edgecolors="white", linewidths=1.4, alpha=0.9, zorder=3)
for _, r in d.iterrows():
    ax.annotate(r["platform"], (r["openness"], r["breadth"]), fontsize=8.4, color=INK, ha="center",
                xytext=(0, np.sqrt((r["adoption"]**2)*10)/2+7), textcoords="offset points")
ax.axvline(4.5, color=MUTED, lw=0.8, ls="--", alpha=0.6)
ax.set_xlabel("Openness  (1 = proprietary ecosystem-locked → 10 = open/cross-platform)")
ax.set_ylabel("Capability breadth  (narrow → broad)")
ax.set_xlim(0.5, 8); ax.set_ylim(3, 9)
ax.text(1, 8.6, "Ecosystem-anchored\n(ride the incumbent's data/apps)", fontsize=8.8, color=MUTED)
ax.text(6.6, 3.4, "Open / cross-platform", fontsize=8.8, color=MUTED, ha="right")
ax.set_title("Enterprise agent platforms: openness vs. breadth", loc="left", pad=26)
ax.text(0, 1.03, "Bubble size = relative enterprise adoption. Incumbents anchor on their data/app moat; openness is the counter-bet.",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: internal assessment, July 2026 (analyst judgment; adoption approximate).", fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "14_platform_positioning.png"))
