"""Section 13 — Agent identity & authentication charts."""
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

# --- Chart 1: standards adoption status (lollipop) ---
df = pd.read_csv(os.path.join(DATA, "13_standards_adoption.csv")).sort_values("maturity_score")
statuscolor = {"adopted": PALETTE[2], "emerging": PALETTE[3], "proposed": PALETTE[1]}
colors = [statuscolor[s] for s in df["status"]]
fig, ax = plt.subplots(figsize=(11, 7))
y = range(len(df))
ax.hlines(y, 0, df["maturity_score"], color=colors, lw=2.5, alpha=0.5)
ax.scatter(df["maturity_score"], y, color=colors, s=130, zorder=3, edgecolors="white", linewidths=1.3)
ax.set_yticks(list(y)); ax.set_yticklabels([f"{r['standard']}  ·  {r['domain']}" for _, r in df.iterrows()], fontsize=9)
for i, (v) in enumerate(df["maturity_score"]):
    ax.text(v + 0.15, i, f"{v}", va="center", fontsize=9, color=INK)
ax.set_xlim(0, 10)
ax.set_xlabel("Adoption maturity  (0 = proposed → 10 = ubiquitous)")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
handles = [plt.Line2D([0],[0], marker="o", color="w", markerfacecolor=statuscolor[k], markersize=10) for k in statuscolor]
ax.legend(handles, list(statuscolor.keys()), loc="lower right")
ax.set_title("Agent identity & payment standards: adoption status", loc="left", pad=24)
ax.text(0, 1.02, "Reused web-auth standards (OAuth 2.1, OIDC) are adopted; agent-native identity and payments are still emerging/proposed",
        transform=ax.transAxes, fontsize=9.0, color=MUTED)
fig.text(0.01, 0.005, "Source: standards bodies / vendor announcements, July 2026 (existence official; maturity is analyst judgment).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "13_standards_adoption.png"))

# --- Chart 2: payment protocols ---
d = pd.read_csv(os.path.join(DATA, "13_payment_protocols.csv")).sort_values("maturity")
fig, ax = plt.subplots(figsize=(11, 5.5))
ax.barh(range(len(d)), d["maturity"], color=PALETTE[4], edgecolor="white")
ax.set_yticks(range(len(d)))
ax.set_yticklabels([f"{r['protocol']}\n({r['backer']})" for _, r in d.iterrows()], fontsize=8.5)
for i, (m, mech) in enumerate(zip(d["maturity"], d["mechanism"])):
    ax.text(m + 0.06, i, mech, va="center", fontsize=8.3, color=MUTED)
ax.set_xlim(0, 8)
ax.set_xlabel("Maturity (0 = proposed → 10 = adopted)")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.set_title("Agentic payment protocols: a contested new layer", loc="left", pad=24)
ax.text(0, 1.03, "Card networks, platforms, and crypto all racing to be how agents pay — none yet dominant",
        transform=ax.transAxes, fontsize=9.4, color=MUTED)
fig.text(0.01, 0.005, "Source: vendor announcements 2025–2026 (official for existence; maturity analyst judgment).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "13_payment_protocols.png"))
