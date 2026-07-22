"""Section 10 — Voice / multimodal agent charts."""
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

# --- Chart 1: latency budget cascade vs S2S (stacked) ---
df = pd.read_csv(os.path.join(DATA, "10_latency_budget.csv"))
comps = df[df["component"] != "Total"]
fig, ax = plt.subplots(figsize=(10.5, 6.3))
archs = ["cascade_ms", "speech_to_speech_ms"]
labels = ["Cascade\n(STT → LLM → TTS)", "Speech-to-speech\n(audio in → audio out)"]
bottoms = [0, 0]
colorset = [PALETTE[0], PALETTE[3], PALETTE[2], PALETTE[4], PALETTE[5]]
for i, (_, row) in enumerate(comps.iterrows()):
    vals = [row["cascade_ms"], row["speech_to_speech_ms"]]
    ax.bar(labels, vals, bottom=bottoms, label=row["component"], color=colorset[i % len(colorset)], edgecolor="white", width=0.5)
    for j, v in enumerate(vals):
        if v > 0:
            ax.text(j, bottoms[j] + v/2, f"{int(v)}", ha="center", va="center", fontsize=8.5, color="white")
    bottoms = [bottoms[0] + vals[0], bottoms[1] + vals[1]]
ax.axhline(900, color=PALETTE[1], lw=1.5, ls="--")
ax.text(1.3, 915, "900ms natural-conversation ceiling", fontsize=9, color=PALETTE[1], ha="right")
for j, tot in enumerate([760, 510]):
    ax.text(j, tot + 25, f"total {tot}ms", ha="center", fontsize=9.5, color=INK, fontweight="bold")
ax.set_ylabel("Latency (ms)")
ax.set_ylim(0, 1000)
ax.legend(loc="upper left", fontsize=8.6, ncol=2)
ax.set_title("Voice-agent latency budget: cascade vs. speech-to-speech", loc="left", pad=24)
ax.text(0, 1.02, "Speech-to-speech collapses STT+LLM+TTS into one model, cutting the latency floor",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: reported component latencies, 2026 (inferred; representative values).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "10_latency_budget.png"))

# --- Chart 2: platform latency ---
d = pd.read_csv(os.path.join(DATA, "10_platform_latency.csv")).sort_values("latency_ms")
colors = [PALETTE[4] if "speech-to-speech" in a else PALETTE[0] for a in d["approach"]]
fig, ax = plt.subplots(figsize=(10.5, 5.8))
ax.barh(d["platform"], d["latency_ms"], color=colors, edgecolor="white")
for i, v in enumerate(d["latency_ms"]):
    ax.text(v + 8, i, f"{v}ms", va="center", fontsize=9, color=INK)
ax.axvline(700, color=MUTED, lw=1.2, ls="--")
ax.text(705, 0.2, "700ms accepted", fontsize=8.5, color=MUTED)
ax.set_xlim(0, 950)
ax.set_xlabel("End-to-end voice round-trip latency (ms)")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.set_title("Voice platform end-to-end latency, 2026", loc="left", pad=24)
ax.text(0, 1.02, "Speech-to-speech (violet) leads on latency; orchestrated cascades trade latency for modularity/control",
        transform=ax.transAxes, fontsize=9.3, color=MUTED)
fig.text(0.01, 0.005, "Source: platform reports, 2026 (inferred; approximate, config-dependent).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "10_platform_latency.png"))
