"""Section 11 — Evaluation & observability charts."""
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

# --- Chart 1: platform capability heatmap ---
df = pd.read_csv(os.path.join(DATA, "11_platform_capabilities.csv")).set_index("platform")
fig, ax = plt.subplots(figsize=(10.5, 6))
data = df.values
im = ax.imshow(data, cmap="Greens", vmin=0, vmax=3, aspect="auto")
ax.set_xticks(range(len(df.columns))); ax.set_xticklabels(df.columns, rotation=25, ha="right")
ax.set_yticks(range(len(df.index))); ax.set_yticklabels(df.index)
labels = {0:"—",1:"basic",2:"good",3:"core"}
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        v = data[i,j]
        ax.text(j, i, labels[v], ha="center", va="center", color="white" if v>=2 else INK, fontsize=8.3)
ax.set_title("Agent eval/observability platform capabilities", loc="left", pad=26)
ax.text(0, 1.05, "The category is converging on unified trace + eval + monitoring; differentiation is self-host and guardrails",
        transform=ax.transAxes, fontsize=9.3, color=MUTED)
ax.grid(False)
fig.text(0.01, 0.005, "Source: vendor docs, July 2026 (existence official; ratings analyst judgment).", fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "11_platform_capabilities.png"))

# --- Chart 2: eval methods cost vs signal ---
d = pd.read_csv(os.path.join(DATA, "11_eval_methods.csv"))
fig, ax = plt.subplots(figsize=(11, 7))
sizes = (d["production_predictiveness"]**2)*11
colors = [PALETTE[i] for i in range(len(d))]
ax.scatter(d["cost_per_eval"], d["signal_quality"], s=sizes, c=colors, edgecolors="white", linewidths=1.4, alpha=0.9, zorder=3)
for _, r in d.iterrows():
    ax.annotate(r["method"], (r["cost_per_eval"], r["signal_quality"]), fontsize=8.6, color=INK, ha="center",
                xytext=(0, np.sqrt((r["production_predictiveness"]**2)*11)/2+7), textcoords="offset points")
ax.set_xlabel("Cost per evaluation  (1 = cheap → 10 = expensive)")
ax.set_ylabel("Signal quality  (how trustworthy the measurement)")
ax.set_xlim(0, 10.5); ax.set_ylim(2, 10)
ax.set_title("Agent evaluation methods: cost vs. signal quality", loc="left", pad=26)
ax.text(0, 1.03, "Bubble size = production-predictiveness. Cheap public benchmarks are the least production-predictive.",
        transform=ax.transAxes, fontsize=10, color=MUTED)
fig.text(0.01, 0.005, "Source: internal assessment, July 2026 (analyst judgment, not measured).", fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "11_eval_methods.png"))
