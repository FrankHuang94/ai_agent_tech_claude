"""Section 03 — Memory systems charts."""
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

# --- Chart 1: latency vs persistence, size=cost ---
df = pd.read_csv(os.path.join(DATA, "03_memory_tradeoffs.csv"))
fig, ax = plt.subplots(figsize=(11, 7))
sizes = (df["cost_score"] ** 2) * 12
colors = [PALETTE[i] for i in range(len(df))]
ax.scatter(df["retrieval_latency_ms"], df["persistence_score"], s=sizes,
           c=colors, edgecolors="white", linewidths=1.4, alpha=0.9, zorder=3)
for _, r in df.iterrows():
    ax.annotate(r["approach"], (r["retrieval_latency_ms"], r["persistence_score"]),
                fontsize=8.6, color=INK, ha="center",
                xytext=(0, np.sqrt((r["cost_score"]**2)*12)/2 + 7), textcoords="offset points")
ax.set_xlabel("Retrieval latency (ms, lower = better)  →")
ax.set_ylabel("Persistence (1 = ephemeral → 10 = durable)")
ax.set_xlim(-15, 175); ax.set_ylim(0, 10.5)
ax.set_title("Agent memory approaches: latency vs. persistence", loc="left", pad=26)
ax.text(0, 1.03, "Bubble size = relative cost/operational overhead (larger = more expensive to run)",
        transform=ax.transAxes, fontsize=10, color=MUTED)
fig.text(0.01, 0.005, "Source: internal assessment + vendor docs, July 2026. Scores are relative, not absolute.",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "03_memory_tradeoffs.png"))

# --- Chart 2: DMR benchmark accuracy ---
b = pd.read_csv(os.path.join(DATA, "03_memory_benchmarks.csv")).sort_values("dmr_accuracy")
fig, ax = plt.subplots(figsize=(10, 6))
is_baseline = b["notes"].str.contains("window|vector", case=False)
bar_colors = [MUTED if bl else PALETTE[2] for bl in (b["architecture"].str.contains("no external|naive"))]
ax.barh(b["system"], b["dmr_accuracy"], color=bar_colors, edgecolor="white")
for i, v in enumerate(b["dmr_accuracy"]):
    ax.text(v + 0.3, i, f"{v:.1f}%", va="center", fontsize=9, color=INK)
ax.set_xlim(70, 100)
ax.set_xlabel("Deep Memory Retrieval accuracy (%)")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.set_title("Memory-system recall vs. baselines", loc="left", pad=24)
ax.text(0, 1.02, "Green = dedicated memory system; grey = no-memory / naive-RAG baseline. Vendor-reported (inferred).",
        transform=ax.transAxes, fontsize=9.5, color=MUTED)
fig.text(0.01, 0.005, "Source: vendor-reported DMR/LOCOMO-style figures, 2026. Cross-vendor comparability is imperfect.",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "03_memory_benchmarks.png"))
