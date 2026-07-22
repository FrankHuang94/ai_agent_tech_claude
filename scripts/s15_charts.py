"""Section 15 — Standards & interoperability charts."""
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

# --- Chart 1: standards timeline ---
df = pd.read_csv(os.path.join(DATA, "15_standards_timeline.csv"))
tracks = {"MCP": PALETTE[0], "A2A": PALETTE[2], "ACP": PALETTE[3], "Payments": PALETTE[4]}
tracky = {"MCP": 4, "A2A": 3, "ACP": 2, "Payments": 1}
fig, ax = plt.subplots(figsize=(13, 6.5))
x = np.arange(len(df))
for i, r in df.iterrows():
    y = tracky[r["track"]]
    ax.scatter(i, y, s=130, color=tracks[r["track"]], zorder=3, edgecolors="white", linewidths=1.3)
    ax.annotate(r["milestone"], (i, y), fontsize=7.8, color=INK, rotation=30, ha="left", va="bottom",
                xytext=(2, 6), textcoords="offset points")
# connect track lines
for t, yv in tracky.items():
    idx = [i for i, r in df.iterrows() if r["track"] == t]
    if len(idx) > 1:
        ax.plot(idx, [yv]*len(idx), color=tracks[t], lw=1.6, alpha=0.4, zorder=1)
ax.set_yticks(list(tracky.values())); ax.set_yticklabels(list(tracky.keys()))
ax.set_xticks(x); ax.set_xticklabels(df["date"], rotation=45, ha="right", fontsize=8)
ax.set_ylim(0.3, 5)
ax.grid(axis="y", visible=False)
ax.set_title("Agent-standards timeline: rapid consolidation under the Linux Foundation", loc="left", pad=30)
ax.text(0, 1.06, "MCP (tools) and A2A (agent-to-agent) both moved to neutral LF governance within ~1 year of launch",
        transform=ax.transAxes, fontsize=9.4, color=MUTED)
fig.text(0.01, 0.005, "Source: standards announcements 2024–2026 (official; dates approximate).", fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "15_standards_timeline.png"))

# --- Chart 2: standards comparison bubble ---
d = pd.read_csv(os.path.join(DATA, "15_standards_comparison.csv"))
fig, ax = plt.subplots(figsize=(11, 7))
sizes = (d["consolidation_likelihood"]**2)*11
colors = [PALETTE[i%len(PALETTE)] for i in range(len(d))]
ax.scatter(d["adoption"], d["governance_score"], s=sizes, c=colors, edgecolors="white", linewidths=1.4, alpha=0.9, zorder=3)
for _, r in d.iterrows():
    ax.annotate(f"{r['standard']}\n({r['layer']})", (r["adoption"], r["governance_score"]), fontsize=8.0, color=INK, ha="center",
                xytext=(0, np.sqrt((r['consolidation_likelihood']**2)*11)/2+8), textcoords="offset points")
ax.set_xlabel("Adoption (1 = proposed → 10 = ubiquitous)")
ax.set_ylabel("Governance maturity (neutral, community-governed)")
ax.set_xlim(0, 10.5); ax.set_ylim(2, 10.5)
ax.set_title("Agent standards: adoption vs. governance maturity", loc="left", pad=26)
ax.text(0, 1.03, "Bubble size = likelihood of becoming/remaining the consolidated standard for its layer. MCP leads decisively.",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: internal assessment, July 2026 (analyst judgment).", fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "15_standards_comparison.png"))
