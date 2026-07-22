"""Section 17 — Appendix charts (confidence & maturity taxonomy)."""
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

# --- Chart: maturity x confidence composition of the database ---
fig, ax = plt.subplots(figsize=(10.5, 6))
mats = ["shipped-reliable", "demoed-brittle", "research-only"]
confs = ["official", "inferred"]
confcolor = {"official": PALETTE[2], "inferred": PALETTE[3]}
bottom = np.zeros(len(mats))
for c in confs:
    vals = [len(df[(df.maturity == m) & (df.source_confidence == c)]) for m in mats]
    ax.bar([m.replace("-", "-\n") for m in mats], vals, bottom=bottom, label=c, color=confcolor[c], edgecolor="white", width=0.55)
    for i, v in enumerate(vals):
        if v > 0:
            ax.text(i, bottom[i] + v/2, str(v), ha="center", va="center", color="white", fontsize=10)
    bottom += vals
ax.set_ylabel("Number of database entities")
ax.legend(title="Source confidence", loc="upper right")
ax.set_title("How the master database's claims are labeled", loc="left", pad=24)
ax.text(0, 1.02, "Maturity of the product (x) split by source confidence of the claim (color). Most claims are official & shipped.",
        transform=ax.transAxes, fontsize=9.4, color=MUTED)
fig.text(0.01, 0.005, "Source: this document's master competitive database, July 2026.", fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "17_confidence_maturity.png"))
