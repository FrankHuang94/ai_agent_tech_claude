"""Section 07 — Retrieval / knowledge grounding charts."""
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

# --- Chart 1: latency vs accuracy, size=cost ---
df = pd.read_csv(os.path.join(DATA, "07_retrieval_tradeoffs.csv"))
fig, ax = plt.subplots(figsize=(11, 7))
sizes = (df["cost_score"] ** 2) * 11
colors = [PALETTE[i] for i in range(len(df))]
ax.scatter(df["latency_ms"], df["answer_quality"], s=sizes, c=colors,
           edgecolors="white", linewidths=1.4, alpha=0.9, zorder=3)
for _, r in df.iterrows():
    ax.annotate(r["approach"], (r["latency_ms"], r["answer_quality"]),
                fontsize=8.5, color=INK, ha="center",
                xytext=(0, np.sqrt((r["cost_score"]**2)*11)/2 + 7), textcoords="offset points")
ax.set_xlabel("Retrieval latency (ms, log)  →  slower")
ax.set_ylabel("Answer quality (RAGAS-style, %)")
ax.set_xscale("log")
ax.set_xticks([40,70,140,220,350,600,900])
ax.set_xticklabels([40,70,140,220,350,600,900])
ax.set_ylim(55, 92)
ax.set_title("Retrieval strategies: latency vs. answer quality", loc="left", pad=26)
ax.text(0, 1.03, "Bubble size = relative cost/complexity. Agentic multi-hop is best quality but slowest & priciest.",
        transform=ax.transAxes, fontsize=10, color=MUTED)
fig.text(0.01, 0.005, "Source: internal synthesis of published RAG-pipeline results, 2026 (inferred; illustrative).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "07_retrieval_tradeoffs.png"))

# --- Chart 2: pipeline quality staircase ---
d = pd.read_csv(os.path.join(DATA, "07_pipeline_quality.csv"))
fig, ax = plt.subplots(figsize=(10.5, 6))
colors2 = plt.cm.Blues(np.linspace(0.45, 0.9, len(d)))
bars = ax.bar(range(len(d)), d["ragas_score"], color=colors2, edgecolor="white", width=0.66)
ax.set_xticks(range(len(d))); ax.set_xticklabels(d["stage"], rotation=18, ha="right", fontsize=9)
for i, v in enumerate(d["ragas_score"]):
    ax.text(i, v + 0.6, f"{v}", ha="center", fontsize=9.5, color=INK)
ax.set_ylim(50, 95)
ax.set_ylabel("Answer quality (RAGAS-style, %)")
ax.set_title("Retrieval quality compounds as you add pipeline stages", loc="left", pad=24)
ax.text(0, 1.02, "Each stage — hybrid, rerank, query rewriting, agentic iteration — adds measurable quality",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: illustrative of reported hybrid-search + rerank gains (~15–30% over naive vector), 2026 (inferred).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "07_pipeline_quality.png"))
