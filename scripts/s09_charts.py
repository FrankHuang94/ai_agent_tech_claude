"""Section 09 — Coding agent charts."""
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

# --- Chart 1: SWE-bench over time ---
df = pd.read_csv(os.path.join(DATA, "09_swebench_timeline.csv"))
fig, ax = plt.subplots(figsize=(11.5, 6.8))
ax.plot(df["date"], df["swebench_verified"], marker="o", markersize=7, lw=2.8, color=PALETTE[2], zorder=3)
ax.fill_between(range(len(df)), df["swebench_verified"], alpha=0.08, color=PALETTE[2])
for _, r in df.iterrows():
    ax.annotate(f"{r['swebench_verified']:.0f}%", (r["date"], r["swebench_verified"]),
                fontsize=9.5, color=INK, ha="center", xytext=(0, 9), textcoords="offset points")
for i, r in df.iterrows():
    ax.annotate(r["milestone"], (r["date"], r["swebench_verified"]),
                fontsize=7.6, color=MUTED, ha="left", xytext=(8, -13), textcoords="offset points")
ax.set_ylabel("SWE-bench Verified (%)")
ax.set_ylim(0, 100)
ax.set_xlim(-0.3, len(df)-0.1)
ax.set_title("Coding agents on SWE-bench Verified: 4% → 90% in under three years", loc="left", pad=24)
ax.text(0, 1.02, "Autonomous fixing of real GitHub issues — the clearest 'shipped and reliable' agent vertical",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: SWE-bench Verified leaderboard 2023–2026 (inferred; approximate, harness-dependent).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "09_swebench_timeline.png"))

# --- Chart 2: agent scores bar ---
d = pd.read_csv(os.path.join(DATA, "09_agent_scores.csv")).sort_values("swebench_verified")
cmap = {"frontier": PALETTE[4], "shipped": PALETTE[0], "open": PALETTE[2], "autonomous": PALETTE[3]}
colors = [cmap[c] for c in d["category"]]
fig, ax = plt.subplots(figsize=(11, 6))
ax.barh(d["agent"], d["swebench_verified"], color=colors, edgecolor="white")
for i, v in enumerate(d["swebench_verified"]):
    ax.text(v + 0.7, i, f"{v:.1f}%", va="center", fontsize=9, color=INK)
ax.set_xlim(0, 102)
ax.set_xlabel("SWE-bench Verified (%)")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
handles = [plt.Rectangle((0,0),1,1,color=cmap[k]) for k in cmap]
ax.legend(handles, [k for k in cmap], loc="lower right", title=None, ncol=2, fontsize=9)
ax.set_title("Coding agents by benchmark score, mid-2026", loc="left", pad=24)
ax.text(0, 1.02, "Widely-available agents cluster 80–88%; frontier configs reach ~95%; autonomous end-to-end agents trail",
        transform=ax.transAxes, fontsize=9.3, color=MUTED)
fig.text(0.01, 0.005, "Source: SWE-bench Verified reports, 2026 (inferred; scores are harness- and scaffold-dependent).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "09_agent_scores.png"))
