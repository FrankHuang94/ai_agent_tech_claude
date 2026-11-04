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
    last = i == len(df) - 1
    # stagger labels on the flat 2025-12 -> 2026-02 segment so they don't collide
    dy = -28 if (i > 0 and df["best_score"].iloc[i] == df["best_score"].iloc[i-1]) else -14
    ax.annotate(r["milestone"], (r["date"], r["best_score"]),
                fontsize=7.6, color=MUTED, ha="right" if last else "left", rotation=0,
                va="center" if last else "baseline",
                xytext=(-12, 0) if last else (8, dy), textcoords="offset points")
ax.set_ylabel("OSWorld success rate (%)")
ax.set_ylim(0, 95)
ax.set_xlim(-0.3, len(df)-0.2)
ax.set_title("Computer-use on OSWorld: 12% → 85% in two years", loc="left", pad=24)
ax.text(0, 1.02, "Short-horizon desktop computer-use crossed the human baseline in late 2025; vendors moved to long-horizon OSWorld 2.x after mid-2026",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: OSWorld / OSWorld-Verified reports 2024–2026; Fable 5 figure provider-reported (inferred; approximate).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "08_osworld_timeline.png"))

# --- Chart 2: long-horizon partial credit vs full completion (the horizon cliff) ---
d = pd.read_csv(os.path.join(DATA, "08_horizon_gap.csv"))
fig, ax = plt.subplots(figsize=(11.5, 6.6))
y = np.arange(len(d)); h = 0.38
labels = [f"{s_}  ({dt}, {n})" for s_, dt, n in zip(d["system"], d["date"], d["note"])]
ax.barh(y - h/2, d["long_partial"], height=h, color=PALETTE[0], label="Long-horizon partial credit (checkpoints met)")
ax.barh(y + h/2, d["long_binary"].fillna(0), height=h, color=PALETTE[1], label="Long-horizon full completion (binary)")
for yi, v in zip(y - h/2, d["long_partial"]):
    ax.text(v + 0.8, yi, f"{v:.1f}", va="center", fontsize=8.5, color=INK)
for yi, v in zip(y + h/2, d["long_binary"]):
    if pd.isna(v):
        ax.text(0.8, yi, "binary not reported", va="center", fontsize=8, color=MUTED, style="italic")
    else:
        ax.text(v + 0.8, yi, f"{v:.1f}", va="center", fontsize=8.5, color=INK)
ax.axvline(85, color=PALETTE[2], lw=1.4, ls="--")
ax.text(84.2, 0.985, "Best short-horizon\n(OSWorld-Verified) ~85%", fontsize=8.5,
        color=PALETTE[2], ha="right", va="top", transform=ax.get_xaxis_transform())
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9); ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("OSWorld 2.0 score (%), ~1.6-hour median tasks")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.legend(loc="lower right", bbox_to_anchor=(0.83, 0.0), fontsize=9)
ax.set_title("The horizon cliff: partial credit climbs, full completion lags", loc="left", pad=24)
ax.text(0, 1.02, "Where reported, full-task completion stays ~13–21% while partial credit rose from ~50% to ~78% (Jun–Sep 2026)",
        transform=ax.transAxes, fontsize=9.2, color=MUTED)
fig.text(0.01, 0.005, "Source: OSWorld 2.0 paper (arXiv 2606.29537), Yutori/Steel leaderboards, vendor reports, Jun–Sep 2026 "
         "(inferred; harness/budget vary; OSWorld 2.1 scores excluded as non-comparable).", fontsize=7.6, color=MUTED)
save(fig, os.path.join(OUT, "08_horizon_gap.png"))
