# Master Competitive Database — Schema

`master_competitive_database.csv` is the consolidated reference artifact backing
**Section 16**. Every section (01–15) feeds deduplicated company entries into it.

## Columns

| Column | Description | Allowed values / format |
|---|---|---|
| `company` | Organization or product name. Product name preferred when it differs materially from the parent org (e.g. `LangGraph` under `LangChain`). | Free text |
| `category` | Primary technical category, matching a section. | One of the 15 category slugs below |
| `maturity` | Delivery maturity of the flagship agent capability. | `shipped-reliable`, `demoed-brittle`, `research-only` |
| `funding_stage` | Most recent known financing stage of the company. | `bootstrapped`, `seed`, `series-a`, `series-b`, `series-c`, `series-d+`, `public`, `subsidiary`, `open-source-project`, `research-lab`, `unknown` |
| `key_backers` | Notable investors, parent company, or institutional home. | Semicolon-separated |
| `differentiator` | One-line distinguishing angle. | Free text |
| `main_competitors` | Closest 2–4 competitors. | Semicolon-separated |
| `source_confidence` | Confidence in the claim per the methodology in Section 17. | `official` (vendor announcement/docs), `inferred` (papers/job posts/talks), `speculative` |

## Category slugs

`orchestration`, `memory`, `tool-use`, `planning-reasoning`, `multi-agent`,
`retrieval`, `computer-use`, `coding`, `voice-multimodal`, `eval-observability`,
`guardrails-security`, `identity-auth`, `enterprise-platform`, `standards`,
`infrastructure`.

## Maturity definitions

- **shipped-reliable** — Generally available, documented, used in production by
  third parties; behaves predictably within a stated envelope.
- **demoed-brittle** — Publicly shown or in preview/beta; works in curated
  conditions but with known reliability gaps outside them.
- **research-only** — Paper, prototype, or internal demo; not a supported product.

Rows may legitimately appear in more than one category; Section 16 documents the
deduplication rule (one row per company × primary category).
