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
fig.text(0.01, 0.005, "Source: internal assessment + vendor docs, July 2026 (reviewed Nov 2026, unchanged). Scores are relative, not absolute.",
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
fig.text(0.01, 0.005, "Source: vendor-reported DMR figures, mid-2026 (DMR largely superseded by LoCoMo/LongMemEval/BEAM by Nov 2026). Imperfect comparability.",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "03_memory_benchmarks.png"))

# --- Chart 3 (Nov 2026 update): saturated LoCoMo/LongMemEval vs BEAM headroom ---
n = pd.read_csv(os.path.join(DATA, "03_memory_benchmarks_2026.csv"))
benches = list(dict.fromkeys(n["benchmark"]))
systems = list(dict.fromkeys(n["system"]))
fig, ax = plt.subplots(figsize=(11, 6))
w = 0.8 / len(systems)
x = np.arange(len(benches))
sys_colors = {s_: (MUTED if "old" in s_ else PALETTE[i]) for i, s_ in enumerate(systems)}
for j, s_ in enumerate(systems):
    sub = n[n["system"] == s_].set_index("benchmark")
    vals = [sub["score"].get(b_, np.nan) for b_ in benches]
    xs = x - 0.4 + w / 2 + j * w
    ax.bar(xs, vals, width=w * 0.95, color=sys_colors[s_], edgecolor="white", label=s_)
    for xi, v in zip(xs, vals):
        if not np.isnan(v):
            ax.text(xi, v + 1, f"{v:.1f}", ha="center", fontsize=8.5, color=INK)
ax.axhline(90, color=MUTED, lw=1, ls="--")
ax.text(1.5, 91.0, "~90: saturation zone", fontsize=8.5, color=MUTED, ha="center")
ax.set_xticks(x); ax.set_xticklabels(benches)
ax.set_ylim(0, 105)
ax.set_ylabel("Reported accuracy (%)")
ax.grid(axis="y"); ax.grid(axis="x", visible=False)
ax.legend(loc="upper right", fontsize=8.5)
ax.set_title("Memory benchmarks, Nov 2026: recall suites saturate, BEAM shows headroom", loc="left", pad=24)
ax.text(0, 1.02, "Vendor-reported; LoCoMo answer key under independent audit (~6.4% score-corrupting errors). Directional only.",
        transform=ax.transAxes, fontsize=9.5, color=MUTED)
fig.text(0.01, 0.005, "Source: Mem0 PyPI README (official, vendor); Vectorize Hindsight AMB manifesto, Mar 2026 (inferred).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "03_memory_benchmarks_2026.png"))
