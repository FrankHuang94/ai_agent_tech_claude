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
tracks = {"MCP": PALETTE[0], "A2A": PALETTE[2], "ACP/AGNTCY": PALETTE[3], "Payments": PALETTE[4], "AAIF": PALETTE[5]}
tracky = {"AAIF": 5, "MCP": 4, "A2A": 3, "ACP/AGNTCY": 2, "Payments": 1}
fig, ax = plt.subplots(figsize=(15, 7))
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
ax.set_ylim(0.3, 6.3)
ax.set_xlim(-0.6, len(df) + 1.2)
ax.grid(axis="y", visible=False)
ax.set_title("Agent-standards timeline: rapid consolidation under the Linux Foundation", loc="left", pad=24)
ax.text(0, 1.015, "MCP (tools) and A2A (agent-to-agent) both reached neutral LF governance within ~1 year; since Aug 2026 both sit in the Agentic AI Foundation",
        transform=ax.transAxes, fontsize=9.4, color=MUTED)
fig.text(0.01, -0.03, "Source: standards announcements Nov 2024 to Oct 2026 (official; dates to month; registry count from third-party/community indexes).", fontsize=8, color=MUTED)
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
ax.text(0, 1.03, "Bubble size = likelihood of becoming/remaining the consolidated standard for its layer. MCP leads; A2A closes the gap after joining AAIF.",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: internal assessment, November 2026 (analyst judgment). IBM ACP merged into A2A (Aug 2025); AP2 now at FIDO Alliance, x402 at LF x402 Foundation.", fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "15_standards_comparison.png"))
