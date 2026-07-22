"""Section 02 — Orchestration framework charts."""
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

# --- Chart 1: GitHub stars over time (approx) ---
df = pd.read_csv(os.path.join(DATA, "02_framework_stars.csv"))
fig, ax = plt.subplots(figsize=(11, 6.5))
cols = ["LangChain", "LlamaIndex", "AutoGen", "CrewAI", "LangGraph", "PydanticAI", "GoogleADK"]
for i, c in enumerate(cols):
    series = df[c].replace(0, np.nan)
    ax.plot(df["quarter"], series, marker="o", markersize=4, lw=2.2,
            color=PALETTE[i], label=c)
    # label last point
    last = series.dropna().iloc[-1]
    ax.text(len(df) - 0.9, last, f" {c} ({last:.0f}k)", fontsize=8.5,
            color=PALETTE[i], va="center")
ax.set_ylabel("GitHub stars (thousands, approx.)")
ax.set_xlabel("")
ax.set_xlim(0, len(df) + 1.6)
ax.set_title("Orchestration framework traction (GitHub stars)", loc="left", pad=24)
ax.text(0, 1.02, "Approximate; star counts vary by source and reflect community size, not revenue or production use",
        transform=ax.transAxes, fontsize=9.5, color=MUTED)
ax.legend(ncol=4, loc="upper left", fontsize=8.5)
fig.text(0.01, 0.005, "Source: framework GitHub repos, multiple 2026 snapshots (inferred, approximate).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "02_framework_stars.png"))

# --- Chart 2: Funding raised by independent framework companies ---
f = pd.read_csv(os.path.join(DATA, "02_framework_funding.csv"))
f = f[f["total_funding_musd"] > 0].sort_values("total_funding_musd")
fig, ax = plt.subplots(figsize=(10, 5.5))
bars = ax.barh(f["company"], f["total_funding_musd"], color=PALETTE[0], edgecolor="white")
for i, (v, s) in enumerate(zip(f["total_funding_musd"], f["latest_stage"])):
    ax.text(v + 3, i, f"${v:.0f}M  ({s})", va="center", fontsize=9, color=INK)
ax.set_xlim(0, 320)
ax.set_xlabel("Total disclosed funding (US$ millions)")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.set_title("Independent orchestration-framework funding", loc="left", pad=24)
ax.text(0, 1.03, "Vendor-owned frameworks (MS Agent Framework, OpenAI/Google SDKs) omitted — funded internally",
        transform=ax.transAxes, fontsize=9.5, color=MUTED)
fig.text(0.01, 0.005, "Source: press reports 2025–2026 (inferred). LangChain: $125M Series B, Oct 2025, $1.25B valuation.",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "02_framework_funding.png"))
