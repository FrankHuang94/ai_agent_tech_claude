"""Section 12 — Guardrails, safety & security charts."""
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

# --- Chart 1: injection defense residual risk ---
df = pd.read_csv(os.path.join(DATA, "12_injection_defenses.csv"))
fig, ax = plt.subplots(figsize=(11, 6.5))
colors = plt.cm.RdYlGn_r(df["attack_success_rate"] / 90)
bars = ax.barh(range(len(df)), df["attack_success_rate"], color=colors, edgecolor="white")
ax.set_yticks(range(len(df))); ax.set_yticklabels(df["defense"])
ax.invert_yaxis()
for i, (v, n) in enumerate(zip(df["attack_success_rate"], df["note"])):
    ax.text(v + 1, i, f"{v}%", va="center", fontsize=9, color=INK)
ax.set_xlim(0, 95)
ax.set_xlabel("Prompt-injection attack success rate (%, lower = safer)")
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.set_title("No single defense stops prompt injection; layers reduce but never eliminate it", loc="left", pad=24)
ax.text(0, 1.02, "Defense-in-depth drives residual risk down toward — but not to — zero. There is no robust single fix.",
        transform=ax.transAxes, fontsize=9.4, color=MUTED)
fig.text(0.01, 0.005, "Source: illustrative synthesis of published injection-defense evaluations, 2026 (inferred).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "12_injection_defenses.png"))

# --- Chart 2: incident/vuln trend + acquisitions ---
d = pd.read_csv(os.path.join(DATA, "12_incident_trend.csv"))
fig, ax = plt.subplots(figsize=(11, 6.3))
ax.bar(range(len(d)), d["disclosed_ai_vulns"], color=PALETTE[1], width=0.6, label="Disclosed AI/LLM vulnerabilities")
ax.set_xticks(range(len(d))); ax.set_xticklabels(d["period"])
ax.set_ylabel("Disclosed AI/LLM vulnerabilities (approx.)")
for i, v in enumerate(d["disclosed_ai_vulns"]):
    ax.text(i, v + 8, str(v), ha="center", fontsize=9, color=INK)
ax2 = ax.twinx()
ax2.plot(range(len(d)), d["cumulative_acquisitions"], marker="o", lw=2.6, color=PALETTE[4], label="Cumulative major AI-security acquisitions")
ax2.set_ylabel("Cumulative major acquisitions", color=PALETTE[4])
ax2.set_ylim(0, 9); ax2.grid(False)
ax2.tick_params(axis="y", colors=PALETTE[4])
ax.set_title("AI/agent security: rising vulnerabilities and a consolidating market", loc="left", pad=24)
ax.text(0, 1.02, "Vulnerability disclosures climb as agents gain the ability to act; incumbents acquire the startups (Lakera, Protect AI, Robust Intelligence)",
        transform=ax.transAxes, fontsize=8.8, color=MUTED)
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9)
fig.text(0.01, 0.005, "Source: illustrative of OWASP/CVE trends and public acquisitions 2023–2026 (inferred; approximate).",
         fontsize=8, color=MUTED)
save(fig, os.path.join(OUT, "12_incident_trend.png"))
