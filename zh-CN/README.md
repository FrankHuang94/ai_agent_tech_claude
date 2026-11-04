# AI 智能体核心技术 — 结构化技术参考

> **说明：** 本文为英文原文 [`README.md`](../README.md) 的简体中文参考译文，仅供参考；如有出入，以英文原文为准。
> 本目录（`zh-CN/`）收录全部 17 个章节的中文参考译文；图表、CSV 数据与脚本未翻译，仍沿用英文原版（位于仓库根目录的 `assets/` 与 `scripts/`）。

这是一份关于自主 AI 智能体背后核心技术的结构化技术与竞争格局参考：涵盖架构分层、各层的工程挑战、路线图方向，以及截至
**2026 年 11 月**（在最初的 2026 年 7 月快照基础上更新）的竞争与标准格局。

这是一份**内部技术参考**，而非产品路线图或某一家公司的战略文件。全文按技术类别组织，每个类别一个 Markdown 文件，并配有生成的图表（matplotlib）和由 GitHub 原生渲染的 Mermaid 图。每一项竞争性论断都标注了置信度和交付成熟度标签（参见[方法论](sections/17-appendix-glossary-methodology.md)）。

> **初版生成日期：** 2026-07-22（原始快照）· **最近更新：** 2026-11-04
> **范围：** 15 个技术类别 + 执行摘要 + 主数据库 + 附录（共 17 个文件）
> **篇幅：** 英文原文各章节合计约 130,000 词
> **主数据库：** 15 个类别下去重后的 178 家公司/实体（[CSV](../assets/data/master_competitive_database.csv)，字段说明见[中文版 SCHEMA](assets/data/SCHEMA.md)）
> **可视化：** 34 张生成图表 + 每个章节中的原生 Mermaid 图
> **English original:** [`../README.md`](../README.md)

---

## 2026 年 11 月更新

所有章节都补充了 2026 年 7 月下旬至 11 月初的新进展。§02–§15 的每一章开头新增了带日期、附来源链接的 **“2026 年 7 月以来的变化”** 日志，结尾新增 **“参考来源（2026 年 11 月更新）”** 列表；过时的论断已就地修订，竞争格局表和路线图已更新，受影响的图表已重新生成，主数据库由 149 个实体扩充至 178 个。要点如下（详细内容与置信度标签见 §01）：

- 新一代前沿模型（Claude 5.x、GPT-6、Gemini 4）使推理成为“始终开启”的默认能力；SWE-bench Verified 已趋于饱和（约 95–97%），正在让位于 Terminal-Bench 4.0 等更难的基准测试。
- MCP 的 `2026-07-28` 规范使协议核心变为无状态；A2A 于 2026 年 8 月加入 Linux 基金会旗下的 Agentic AI Foundation（AAIF），与 MCP 同属一个中立机构。更正：IBM 的 ACP 早在 2025 年就已并入 A2A。
- 整合浪潮波及“脚手架”层：SpaceX 收购了 Cursor（600 亿美元），Microsoft 归档了 AutoGen；评估/可观测性、智能体安全以及非人类身份（NHI）领域的初创公司，纷纷被数据平台、安全与身份领域的既有厂商以及模型实验室收购。
- 提示注入、评估以及长程规划，仍是智能体最容易出问题的三大环节。

---

## 如何阅读本文

每个章节都会为每一项技术论断区分三种交付状态：

- **shipped-reliable（已发布且可靠）**——已正式发布（GA）、有文档、被第三方用于生产环境。
- **demoed-brittle（已演示但脆弱）**——已公开展示或处于预览阶段；在精心设定的条件下可用，存在已知的可靠性缺口。
- **research-only（仅限研究）**——论文、原型或内部演示；并非受支持的产品。

路线图与能力类论断还额外标注了**置信度**：
`official`（官方：厂商公告/文档）、`inferred`（推断：论文/招聘信息/演讲）或
`speculative`（推测）。完整方法论见第 17 章。

---

## 目录

| # | 章节 | 重点 |
|---|---|---|
| 01 | [执行摘要](sections/01-exec-summary.md) | 跨类别挑战地图；哪些层已解决、处于瓶颈或仍有争议 |
| 02 | [智能体编排框架](sections/02-orchestration-frameworks.md) | LangGraph、CrewAI、AutoGen、LlamaIndex；图式执行与线性执行；状态管理 |
| 03 | [记忆系统](sections/03-memory-systems.md) | 短期上下文、长期/情景记忆、向量/图/混合存储 |
| 04 | [工具使用与函数调用](sections/04-tool-use-function-calling.md) | 模式（schema）标准、工具选择可靠性、结构化输出、错误恢复 |
| 05 | [规划与推理](sections/05-planning-reasoning.md) | ReAct、树搜索、反思、长程任务分解 |
| 06 | [多智能体协调](sections/06-multi-agent-coordination.md) | MCP、A2A、委派与角色分工、协调失效模式 |
| 07 | [检索与知识接地](sections/07-retrieval-knowledge-grounding.md) | 智能体式 RAG、知识新鲜度、混合检索 |
| 08 | [计算机使用与浏览器智能体](sections/08-computer-use-browser-agents.md) | 屏幕理解、操作可靠性、沙箱 |
| 09 | [编码智能体](sections/09-coding-agents.md) | 自主开发智能体、执行安全、人在回路的代码审查 |
| 10 | [语音与多模态智能体](sections/10-voice-multimodal-agents.md) | 实时语音架构、多模态输入输出、延迟 |
| 11 | [评估与可观测性](sections/11-evaluation-observability.md) | 基准测试及其局限、链路追踪、生产监控、回归检测 |
| 12 | [护栏、安全与防护](sections/12-guardrails-safety-security.md) | 提示注入、数据外泄、权限管理、沙箱 |
| 13 | [智能体身份与认证](sections/13-agent-identity-authentication.md) | 面向智能体的 OAuth、委托凭证、智能体支付 |
| 14 | [企业级智能体平台](sections/14-enterprise-agent-platforms.md) | Agentforce、Copilot Studio、ServiceNow、垂直行业平台 |
| 15 | [标准与互操作性](sections/15-standards-interoperability.md) | MCP/A2A 现状、整合路径、历史类比 |
| 16 | [主竞争数据库](sections/16-master-competitive-database.md) | 178 个实体的汇总表；CSV 导出；汇总图表 |
| 17 | [附录：术语表与方法论](sections/17-appendix-glossary-methodology.md) | 术语；置信度方法论 |

---

## 仓库结构

```
.
├── README.md                     # 英文版说明
├── sections/                     # 英文原文，每章一个 markdown 文件（01–17）
├── zh-CN/                        # 简体中文参考译文（本目录）
│   ├── README.md                 # 本文件
│   ├── sections/                 # 各章节中文译文（文件名与英文版一致）
│   └── assets/data/SCHEMA.md     # 主数据库字段说明（中文）
├── assets/
│   ├── charts/                   # 各章节引用的生成图表（PNG，英文）
│   └── data/                     # 支撑各图表的 CSV/JSON 数据 + 主数据库
│       ├── master_competitive_database.csv
│       └── SCHEMA.md
└── scripts/                      # Python 图表生成脚本 + 共享图表样式
    └── chartstyle.py
```

## 重新生成图表

所有图表均由 `assets/data/` 中的数据生成。每个章节的图表在 `scripts/` 中都有对应脚本。重新生成方法：

```bash
pip install matplotlib pandas numpy
```

```bash
python3 scripts/<section>_charts.py
```

## 注意事项

这是一个快速变化的领域；竞争数据是 **2026 年 11 月的快照**（对最初 2026 年 7 月快照的更新），会随时间过时。融资阶段、采用者名单以及标准状态每月都在变化。凡无法核实到官方来源的论断，均标注为 `inferred`（推断）或 `speculative`（推测），应据此审慎对待。在 2026 年 11 月的更新过程中，许多一手来源网站无法直接访问，因此有更大比例的新论断依赖二手报道，并标注了 `inferred`。

本目录中的简体中文译文仅供参考；如与英文原文不一致，以英文原文为准。图表未作翻译。
