# 主竞争数据库 — 字段说明（Schema）

> **说明：** 本文为英文原文 [`assets/data/SCHEMA.md`](../../../assets/data/SCHEMA.md) 的简体中文参考译文，仅供参考；如有出入，以英文原文为准。数据文件本身（[`master_competitive_database.csv`](../../../assets/data/master_competitive_database.csv)）未翻译，列名与取值均保持英文。

`master_competitive_database.csv` 是支撑**第 16 章**的汇总参考数据。第 01–15 章中出现的公司条目经去重后全部汇入此文件。

## 字段

| 字段 | 说明 | 允许的取值 / 格式 |
|---|---|---|
| `company` | 组织或产品名称。当产品名与母公司名差异较大时，优先使用产品名（例如 `LangChain` 旗下的 `LangGraph`）。 | 自由文本 |
| `category` | 主要技术类别，与章节对应。 | 下列 15 个类别标识之一 |
| `maturity` | 旗舰智能体能力的交付成熟度。 | `shipped-reliable`、`demoed-brittle`、`research-only` |
| `funding_stage` | 公司已知的最近一轮融资阶段。 | `bootstrapped`、`seed`、`series-a`、`series-b`、`series-c`、`series-d+`、`public`、`subsidiary`、`open-source-project`、`research-lab`、`unknown`（部分历史行还使用 `series-e`、`series-e+`、`series-f`） |
| `key_backers` | 主要投资方、母公司或所属机构。 | 以分号分隔 |
| `differentiator` | 一句话概括的差异化定位。 | 自由文本 |
| `main_competitors` | 最接近的 2–4 个竞争对手。 | 以分号分隔 |
| `source_confidence` | 依据第 17 章方法论给出的论断置信度。 | `official`（厂商公告/文档）、`inferred`（论文/招聘信息/演讲）、`speculative`（推测） |

## 类别标识

`orchestration`（编排）、`memory`（记忆）、`tool-use`（工具使用）、`planning-reasoning`（规划与推理）、`multi-agent`（多智能体）、
`retrieval`（检索）、`computer-use`（计算机使用）、`coding`（编码）、`voice-multimodal`（语音与多模态）、`eval-observability`（评估与可观测性）、
`guardrails-security`（护栏与安全）、`identity-auth`（身份与认证）、`enterprise-platform`（企业平台）、`standards`（标准）、
`infrastructure`（基础设施）。

## 成熟度定义

- **shipped-reliable（已发布且可靠）**——已正式发布（GA）、有文档、被第三方用于生产环境；在其声明的适用范围内表现可预期。
- **demoed-brittle（已演示但脆弱）**——已公开展示或处于预览/测试阶段；在精心设定的条件下可用，但超出这些条件时存在已知的可靠性缺口。
- **research-only（仅限研究）**——论文、原型或内部演示；并非受支持的产品。

同一行理论上可能涉及多个类别；第 16 章说明了去重规则（每家公司 × 主要类别仅保留一行）。截至 2026 年 11 月更新，数据库共 178 行。
