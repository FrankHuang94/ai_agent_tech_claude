"""Section 16 — Master database summary charts."""
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

df = pd.read_csv(os.path.join(DATA, "master_competitive_database.csv"))
print("total companies:", len(df))

# --- Chart 1: company count by category ---
cat_labels = {
    "orchestration":"Orchestration","memory":"Memory","tool-use":"Tool use",
    "planning-reasoning":"Planning & reasoning","multi-agent":"Multi-agent",
    "retrieval":"Retrieval","computer-use":"Computer-use","coding":"Coding",
    "voice-multimodal":"Voice & multimodal","eval-observability":"Eval & observability",
    "guardrails-security":"Guardrails & security","identity-auth":"Identity & auth",
    "enterprise-platform":"Enterprise platforms","standards":"Standards","infrastructure":"Infrastructure",
}
counts = df["category"].value_counts()
counts = counts.reindex([c for c in cat_labels if c in counts.index])
fig, ax = plt.subplots(figsize=(11, 7))
colors = plt.cm.viridis(np.linspace(0.15, 0.9, len(counts)))
ax.barh([cat_labels[c] for c in counts.index], counts.values, color=colors, edgecolor="white")
for i, v in enumerate(counts.values):
    ax.text(v + 0.15, i, str(v), va="center", fontsize=9.5, color=INK)
ax.invert_yaxis()
ax.set_xlabel("Number of companies/entities in database")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.set_title(f"Master database: {len(df)} entities across 15 categories", loc="left", pad=24)
ax.text(0, 1.02, "Company count by primary category (deduplicated). Dense categories = active, contested markets.",
        transform=ax.transAxes, fontsize=9.6, color=MUTED)
fig.text(0.01, 0.005, "Source: this document's master competitive database, July 2026.", fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "16_count_by_category.png"))

# --- Chart 2: funding stage distribution ---
stage_order = ["seed","series-a","series-b","series-c","series-d+","series-e+","series-f","public","subsidiary","open-source-project","research-lab","bootstrapped","unknown"]
stage_label = {"seed":"Seed","series-a":"Series A","series-b":"Series B","series-c":"Series C",
    "series-d+":"Series D+","series-e+":"Series E+","series-f":"Series F","public":"Public",
    "subsidiary":"Big-tech subsidiary","open-source-project":"OSS / standard","research-lab":"Research lab",
    "bootstrapped":"Bootstrapped","unknown":"Unknown"}
sc = df["funding_stage"].value_counts()
sc = sc.reindex([s for s in stage_order if s in sc.index])
fig, ax = plt.subplots(figsize=(11, 6.3))
# color: startups blue-ish, big-tech grey, oss green
def scol(s):
    if s in ("subsidiary","public"): return PALETTE[8]
    if s in ("open-source-project","research-lab"): return PALETTE[2]
    return PALETTE[0]
colors = [scol(s) for s in sc.index]
ax.bar([stage_label[s] for s in sc.index], sc.values, color=colors, edgecolor="white", width=0.68)
for i, v in enumerate(sc.values):
    ax.text(i, v + 0.3, str(v), ha="center", fontsize=9.3, color=INK)
ax.set_ylabel("Number of entities")
ax.set_xticklabels([stage_label[s] for s in sc.index], rotation=35, ha="right", fontsize=8.6)
ax.set_title("Master database: funding-stage distribution", loc="left", pad=24)
ax.text(0, 1.02, "Blue = independent startup stages · grey = big-tech (public/subsidiary) · green = OSS/standard/lab",
        transform=ax.transAxes, fontsize=9.3, color=MUTED)
fig.text(0.01, 0.005, "Source: this document's master competitive database, July 2026 (stages inferred where unconfirmed).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "16_funding_distribution.png"))
