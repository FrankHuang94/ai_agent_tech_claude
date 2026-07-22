"""Section 06 — Multi-agent coordination charts."""
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

# --- Chart 1: capability coverage heatmap ---
df = pd.read_csv(os.path.join(DATA, "06_protocol_coverage.csv")).set_index("protocol")
fig, ax = plt.subplots(figsize=(10.5, 6))
data = df.values
im = ax.imshow(data, cmap="Blues", vmin=0, vmax=3, aspect="auto")
ax.set_xticks(range(len(df.columns))); ax.set_xticklabels(df.columns, rotation=25, ha="right")
ax.set_yticks(range(len(df.index))); ax.set_yticklabels(df.index)
labels = {0: "—", 1: "partial", 2: "good", 3: "core"}
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        v = data[i, j]
        ax.text(j, i, labels[v], ha="center", va="center",
                color="white" if v >= 2 else INK, fontsize=8.5)
ax.set_title("Agent-protocol capability coverage", loc="left", pad=26)
ax.text(0, 1.05, "Which interop layer each protocol addresses — they are complementary, not competing head-to-head",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
ax.grid(False)
fig.text(0.01, 0.005, "Source: protocol specs, July 2026 (official for existence; coverage rating is analyst judgment).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "06_protocol_coverage.png"))

# --- Chart 2: adoption over time ---
a = pd.read_csv(os.path.join(DATA, "06_protocol_adoption.csv"))
fig, ax = plt.subplots(figsize=(11, 6.3))
for i, (c, lab) in enumerate([("MCP_orgs", "MCP (tools/context)"),
                              ("A2A_orgs", "A2A (agent-to-agent)"),
                              ("ACP_orgs", "ACP / AGNTCY")]):
    s = a[c].replace(0, np.nan)
    ax.plot(a["quarter"], s, marker="o", markersize=5, lw=2.6, color=PALETTE[i], label=lab)
    last = s.dropna().iloc[-1]
    ax.text(len(a)-0.9, last, f" {last:.0f}", fontsize=9, color=PALETTE[i], va="center")
ax.set_ylabel("Supporting organizations / partners (approx.)")
ax.set_xlim(0, len(a)+0.8)
ax.legend(loc="upper left")
ax.set_title("Agent-protocol adoption: supporting organizations over time", loc="left", pad=24)
ax.text(0, 1.02, "MCP (tool layer) leads; A2A (agent layer) follows ~1 year behind; both now under the Linux Foundation",
        transform=ax.transAxes, fontsize=9.4, color=MUTED)
fig.text(0.01, 0.005, "Source: Linux Foundation / vendor announcements 2024–2026 (approximate; partner counts vary by source).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "06_protocol_adoption.png"))
