# AI Agent Core Technologies — Structured Technical Reference

A structured technical and competitive reference on the core technologies behind
autonomous AI agents: the architecture layers, the engineering challenges at each
layer, the roadmap direction, and the competitive/standards landscape as of
**July 2026**.

This is an **internal technical reference**, not a product roadmap or a single
company's strategy document. It is organized as one Markdown file per technical
category, backed by generated charts (matplotlib) and native GitHub-rendered
Mermaid diagrams. Every competitive claim is tagged with a confidence level and a
delivery-maturity label (see [methodology](sections/17-appendix-glossary-methodology.md)).

> **Generation date:** 2026-07-22
> **Scope:** 15 technical categories + executive summary + master database + appendix
> **Total length:** 100,000+ words across all section files

---

## How to read this

Every section distinguishes three delivery states for every technology claim:

- **shipped-reliable** — generally available, documented, used in production by third parties.
- **demoed-brittle** — shown publicly or in preview; works in curated conditions, known reliability gaps.
- **research-only** — paper, prototype, or internal demo; not a supported product.

Roadmap and capability claims additionally carry a **confidence level**:
`official` (vendor announcement/docs), `inferred` (papers/job posts/talks), or
`speculative`. The full methodology is in Section 17.

---

## Table of contents

| # | Section | Focus |
|---|---|---|
| 01 | [Executive Summary](sections/01-exec-summary.md) | Cross-category challenge map; which layers are solved, bottlenecked, or contested |
| 02 | [Agent Orchestration Frameworks](sections/02-orchestration-frameworks.md) | LangGraph, CrewAI, AutoGen, LlamaIndex; graph vs. linear execution; state management |
| 03 | [Memory Systems](sections/03-memory-systems.md) | Short-term context, long-term/episodic memory, vector/graph/hybrid stores |
| 04 | [Tool Use and Function Calling](sections/04-tool-use-function-calling.md) | Schema standards, tool-selection reliability, structured output, error recovery |
| 05 | [Planning and Reasoning](sections/05-planning-reasoning.md) | ReAct, tree search, reflection, long-horizon decomposition |
| 06 | [Multi-Agent Coordination](sections/06-multi-agent-coordination.md) | MCP, A2A, delegation and role specialization, coordination failure modes |
| 07 | [Retrieval and Knowledge Grounding](sections/07-retrieval-knowledge-grounding.md) | Agentic RAG, knowledge freshness, hybrid retrieval |
| 08 | [Computer-Use and Browser Agents](sections/08-computer-use-browser-agents.md) | Screen understanding, action reliability, sandboxing |
| 09 | [Coding Agents](sections/09-coding-agents.md) | Autonomous dev agents, execution safety, human-in-the-loop review |
| 10 | [Voice and Multimodal Agents](sections/10-voice-multimodal-agents.md) | Real-time voice architecture, multimodal I/O, latency |
| 11 | [Evaluation and Observability](sections/11-evaluation-observability.md) | Benchmarks and their limits, tracing, production monitoring, regression detection |
| 12 | [Guardrails, Safety, and Security](sections/12-guardrails-safety-security.md) | Prompt injection, exfiltration, permissioning, sandboxing |
| 13 | [Agent Identity and Authentication](sections/13-agent-identity-authentication.md) | OAuth-for-agents, delegated credentials, agentic payments |
| 14 | [Enterprise Agent Platforms](sections/14-enterprise-agent-platforms.md) | Agentforce, Copilot Studio, ServiceNow, vertical platforms |
| 15 | [Standards and Interoperability](sections/15-standards-interoperability.md) | MCP/A2A status, consolidation path, historical analogues |
| 16 | [Master Competitive Database](sections/16-master-competitive-database.md) | Consolidated 100+ company table; CSV export; summary charts |
| 17 | [Appendix: Glossary and Methodology](sections/17-appendix-glossary-methodology.md) | Terms; confidence-level methodology |

---

## Repository structure

```
.
├── README.md                     # this file
├── sections/                     # one markdown file per section (01–17)
├── assets/
│   ├── charts/                   # generated chart images (PNG) referenced by sections
│   └── data/                     # CSV/JSON backing each chart + master database
│       ├── master_competitive_database.csv
│       └── SCHEMA.md
└── scripts/                      # Python chart generators + shared chart style
    └── chartstyle.py
```

## Regenerating charts

All charts are generated from data in `assets/data/`. Each section's charts have a
corresponding script in `scripts/`. To regenerate:

```bash
pip install matplotlib pandas numpy
python3 scripts/<section>_charts.py
```

## Caveats

This is a fast-moving field; competitive data is a **July 2026 snapshot** and will
age. Funding stages, adopter lists, and standards status change monthly. Where a
claim could not be verified to an official source, it is tagged `inferred` or
`speculative` and should be treated accordingly.
