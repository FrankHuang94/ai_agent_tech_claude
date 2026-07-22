"""Section 05 — Planning & reasoning charts."""
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

# --- Chart 1: benchmark saturation over time ---
df = pd.read_csv(os.path.join(DATA, "05_reasoning_trends.csv"))
fig, ax = plt.subplots(figsize=(11.5, 6.8))
cols = [("MMLU", "MMLU (older, saturated)"),
        ("GPQA_Diamond", "GPQA-Diamond (PhD science)"),
        ("AIME", "AIME (competition math)"),
        ("ARC_AGI_2", "ARC-AGI-2 (abstract)"),
        ("HLE", "Humanity's Last Exam")]
for i, (c, lab) in enumerate(cols):
    series = df[c].replace(0, np.nan)
    ax.plot(df["period"], series, marker="o", markersize=4.5, lw=2.4, color=PALETTE[i], label=lab)
    last = series.dropna().iloc[-1]
    ax.text(len(df) - 0.9, last, f" {last:.0f}", fontsize=9, color=PALETTE[i], va="center")
ax.axhline(88, color=MUTED, lw=0.9, ls="--", alpha=0.7)
ax.text(0.1, 89.3, "≈ human-expert band", fontsize=8.5, color=MUTED)
ax.set_ylabel("Benchmark score (%)")
ax.set_ylim(0, 103)
ax.set_xlim(0, len(df) + 0.6)
ax.legend(loc="center left", fontsize=8.7)
ax.set_title("Reasoning benchmarks saturate on arrival", loc="left", pad=24)
ax.text(0, 1.02, "Each harder benchmark is built to escape saturation, and each is climbed within ~2 years",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: aggregated public leaderboards 2023–2026 (inferred/approximate; illustrative of the arc).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "05_reasoning_trends.png"))

# --- Chart 2: test-time compute scaling ---
d = pd.read_csv(os.path.join(DATA, "05_ttc_scaling.csv"))
fig, ax = plt.subplots(figsize=(10.5, 6.3))
ax.plot(d["reasoning_tokens"], d["accuracy_hard_task"], marker="o", lw=2.6, color=PALETTE[4])
ax.fill_between(d["reasoning_tokens"], d["accuracy_hard_task"], alpha=0.08, color=PALETTE[4])
ax.set_xscale("log", base=2)
ax.set_xticks(d["reasoning_tokens"])
ax.set_xticklabels([f"{t//1024}k" if t>=1024 else str(t) for t in d["reasoning_tokens"]])
ax.set_xlabel("Reasoning ('thinking') tokens per problem (log scale)")
ax.set_ylabel("Accuracy on hard task (%)")
ax.set_ylim(20, 92)
ax.set_title("Test-time compute: more thinking buys accuracy, with diminishing returns", loc="left", pad=24)
ax.text(0, 1.02, "The 2025–2026 scaling axis: spend inference compute on reasoning rather than only scaling training",
        transform=ax.transAxes, fontsize=9.5, color=MUTED)
fig.text(0.01, 0.005, "Source: illustrative of published inference-scaling curves (inferred). Shape, not exact values.",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "05_ttc_scaling.png"))
