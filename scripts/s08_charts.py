"""Section 08 — Computer-use / browser agent charts."""
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

# --- Chart 1: OSWorld over time ---
df = pd.read_csv(os.path.join(DATA, "08_osworld_timeline.csv"))
fig, ax = plt.subplots(figsize=(11.5, 6.8))
ax.plot(df["date"], df["best_score"], marker="o", markersize=7, lw=2.8, color=PALETTE[0], zorder=3)
ax.axhline(72.4, color=PALETTE[1], lw=1.4, ls="--")
ax.text(0.05, 74, "Human baseline (72.4%)", fontsize=9, color=PALETTE[1])
for _, r in df.iterrows():
    ax.annotate(f"{r['best_score']:.0f}", (r["date"], r["best_score"]),
                fontsize=9, color=INK, ha="center", xytext=(0, 9), textcoords="offset points")
# milestone labels
for i, r in df.iterrows():
    ax.annotate(r["milestone"], (r["date"], r["best_score"]),
                fontsize=7.6, color=MUTED, ha="left", rotation=0,
                xytext=(8, -14), textcoords="offset points")
ax.set_ylabel("OSWorld success rate (%)")
ax.set_ylim(0, 95)
ax.set_xlim(-0.3, len(df)-0.2)
ax.set_title("Computer-use on OSWorld: 12% → 84% in two years", loc="left", pad=24)
ax.text(0, 1.02, "Short-horizon desktop computer-use crossed the human baseline in late 2025 and kept climbing",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: OSWorld / OSWorld-Verified reports 2024–2026 (inferred; approximate).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "08_osworld_timeline.png"))

# --- Chart 2: short vs long horizon gap ---
d = pd.read_csv(os.path.join(DATA, "08_horizon_gap.csv"))
fig, ax = plt.subplots(figsize=(11, 6.3))
y = np.arange(len(d)); h = 0.38
ax.barh(y + h/2, d["short_horizon"], height=h, color=PALETTE[2], label="Short-horizon (OSWorld-Verified)")
ax.barh(y - h/2, d["long_horizon"], height=h, color=PALETTE[1], label="Long-horizon (OSWorld 2.0, ~1.6h tasks)")
for yi, v in zip(y + h/2, d["short_horizon"]):
    ax.text(v + 0.8, yi, f"{v:.0f}", va="center", fontsize=8.5, color=INK)
for yi, v in zip(y - h/2, d["long_horizon"]):
    ax.text(v + 0.8, yi, f"{v:.0f}", va="center", fontsize=8.5, color=INK)
ax.set_yticks(y); ax.set_yticklabels(d["system"]); ax.invert_yaxis()
ax.set_xlim(0, 95)
ax.set_xlabel("Task success rate (%)")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.legend(loc="lower right")
ax.set_title("The horizon cliff: short tasks nearly solved, long tasks barely started", loc="left", pad=24)
ax.text(0, 1.02, "Every system collapses from ~70–84% on short tasks to ~13–21% on multi-hour long-horizon tasks",
        transform=ax.transAxes, fontsize=9.4, color=MUTED)
fig.text(0.01, 0.005, "Source: OSWorld-Verified vs OSWorld 2.0, 2026 (inferred; long-horizon values illustrative).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "08_horizon_gap.png"))
