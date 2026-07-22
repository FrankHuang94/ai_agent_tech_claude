"""Section 04 — Tool use / function calling charts."""
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

# --- Chart 1: tau-bench grouped bar ---
df = pd.read_csv(os.path.join(DATA, "04_taubench.csv"))
fig, ax = plt.subplots(figsize=(11, 6.5))
y = np.arange(len(df))
h = 0.38
ax.barh(y + h/2, df["tau_retail"], height=h, color=PALETTE[0], label="τ-bench retail")
ax.barh(y - h/2, df["tau_airline"], height=h, color=PALETTE[3], label="τ-bench airline")
for yi, v in zip(y + h/2, df["tau_retail"]):
    ax.text(v + 0.6, yi, f"{v:.0f}", va="center", fontsize=8.5, color=INK)
for yi, v in zip(y - h/2, df["tau_airline"]):
    ax.text(v + 0.6, yi, f"{v:.0f}", va="center", fontsize=8.5, color=INK)
ax.set_yticks(y); ax.set_yticklabels(df["model"])
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("Multi-turn tool-use success (%)")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.legend(loc="lower right")
ax.set_title("Multi-turn tool use: τ-bench retail vs. airline", loc="left", pad=24)
ax.text(0, 1.02, "Airline (harder: stricter policy, more steps) trails retail across all models — reliability is task-dependent",
        transform=ax.transAxes, fontsize=9.3, color=MUTED)
fig.text(0.01, 0.005, "Source: τ-bench figures, 2026 (approximate/illustrative; anchored to published Sonnet 4.5 results).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "04_taubench.png"))

# --- Chart 2: tool-count degradation ---
d = pd.read_csv(os.path.join(DATA, "04_toolcount_degradation.csv"))
fig, ax = plt.subplots(figsize=(10.5, 6.5))
ax.plot(d["num_tools"], d["naive_flat"], marker="o", lw=2.4, color=PALETTE[1], label="Naive: all tools in prompt")
ax.plot(d["num_tools"], d["with_retrieval"], marker="s", lw=2.4, color=PALETTE[2], label="Tool retrieval (RAG over tools)")
ax.plot(d["num_tools"], d["with_namespacing"], marker="^", lw=2.4, color=PALETTE[0], label="Namespacing + hierarchical selection")
ax.set_xscale("log")
ax.set_xticks(d["num_tools"]); ax.set_xticklabels(d["num_tools"])
ax.set_xlabel("Number of available tools (log scale)")
ax.set_ylabel("Correct tool-selection rate (%)")
ax.set_ylim(25, 100)
ax.legend(loc="lower left")
ax.set_title("The many-tools problem: selection accuracy degrades with tool count", loc="left", pad=24)
ax.text(0, 1.02, "Flat prompts collapse past ~50 tools; retrieval and namespacing keep selection viable at scale",
        transform=ax.transAxes, fontsize=9.5, color=MUTED)
fig.text(0.01, 0.005, "Source: illustrative synthesis of published tool-selection degradation patterns (inferred).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "04_toolcount_degradation.png"))
