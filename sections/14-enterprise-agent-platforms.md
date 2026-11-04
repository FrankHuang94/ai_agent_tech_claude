# 14 — Enterprise Agent Platforms

*Where agents meet the enterprise. Agentforce, Copilot Studio, ServiceNow, and vertical
platforms — the packaging layer that turns agent technology into deployable business software.
Target: 6,500 words. Current as of November 2026 (snapshot of July 22, 2026, updated).*

---

## The packaging layer

Enterprise agent platforms are not a *technology* layer like the preceding sections — they are a
*packaging and distribution* layer that assembles the underlying technologies (orchestration §02,
memory §03, tools §04, retrieval §07, guardrails §12, identity §13) into deployable business
software for enterprises, sold by the vendors who already own the enterprise's data and workflows.
In the executive summary this layer scores **6.0/10 maturity, 7.0/10 contestedness** — reasonably
mature (the platforms ship and are adopted) but highly contested (every enterprise-software
incumbent is fighting to own it). The defining fact of 2026 is that **enterprise agentic AI moved
from pilot budgets to production commitments**, and the platform vendors are in a land-grab to be
where those production agents live.

It is worth being clear about what this layer *is not*: it is not where the hard agent technology
gets invented. Every capability an enterprise platform offers — reasoning, memory, tool use,
retrieval, guardrails — comes from the layers below, which the platform assembles rather than
originates. What the platform adds is the enterprise-grade *wrapper*: the data integration, the
governance, the low-code accessibility, the compliance, the support. That distinction matters because
it explains both why the incumbents (who own the data and relationships, not better agent tech) are
so well-positioned, and why the competitive battle here is fought over distribution and ecosystem
rather than over raw capability. This is a go-to-market layer as much as a technology layer — and in enterprise software, distribution
and trusted relationships have historically beaten superior technology more often than not, which is
the incumbents' deepest structural advantage here.

The scale is real, and it grew through 2026. Salesforce reported Agentforce ARR of **>$1.5B** in
Q2 FY27 (quarter ended Jul 31, 2026), up >240% YoY, and **~$3.9B** in combined Agentforce + Data 360
ARR. The Agentforce metric now also counts Slackbot and Headless 360, so it is not like-for-like
with the ~$800M fiscal-2026 figure or Q1 FY27's $1.2B. Agentforce also processed 3.2B "Agentic
Work Units" in that quarter *(official)*. Microsoft reported Copilot Studio at ~160,000
organizations and 400,000+ custom agents (early 2026). By October 2026 its **Agent 365** registry
held **50M+ agents**, up >30% QoQ *(official, earnings call)*. ServiceNow twice raised its 2026
AI-ACV target, from $1B to **$1.7B** *(official)*. On market size, one projection has the
enterprise AI-agent market growing from ~$7.8B (2025) toward ~$52.6B (2030) at a ~46% CAGR.
Gartner's much broader "software with agentic capabilities" envelope is reported at roughly
$200B for 2026 *(inferred; secondary reports of Gartner; not comparable)*. This is one of the
fastest-growing enterprise-software categories. The incumbents (Salesforce, Microsoft,
ServiceNow, Google, SAP, Amazon, Workday) are all racing to convert their existing enterprise
relationships into agent-platform revenue, and OpenAI's Frontier (Feb 2026) has joined them
from the model side.

![Enterprise AI agent market growth](../assets/charts/14_market_growth.png)

The market-size trajectory (treat the exact figures as directional single-source estimates)
captures the shift from experimentation to committed spend — and it is why every enterprise-software
vendor repositioned around "agents" over 2025–2026. The strategic question this section answers is
*how these platforms differ, who wins where, and the fundamental build-vs-buy and lock-in dynamics*.

---

## What changed since July 2026 (November 2026 update)

The July snapshot described a land-grab. Four months later, the land-grab is turning into a
**fight over the control plane**. Every major vendor now sells an agent *registry, governance
and observability* layer and tries to make it the place where *other vendors'* agents are
managed. Microsoft has Agent 365. ServiceNow has AI Control Tower, plus an "AI Passport" for
third-party agents. Salesforce now orchestrates third-party agents from AWS, Azure and Google.
Google has the Gemini Enterprise Agent Platform. At the same time, the incumbents opened up at
the *model* layer. Agentforce now offers Claude and the Bedrock model catalog, and Workday ships
Sana into Copilot, Gemini Enterprise, Slack and Claude. Revenue disclosures grew materially,
though metric definitions keep changing, which makes period-over-period comparison unreliable.
The log also picks up material February–July items the July snapshot missed. Tags follow §17:
*official* is a vendor announcement or filing, linked to the primary source where reachable and
otherwise to coverage of it; *inferred* is single-source or analyst-derived.

- **Jan 28, 2026 — Decagon raises a $250M Series D at a $4.5B valuation** (Coatue, Index)
  *(official; via Bloomberg)* —
  [Bloomberg](https://www.bloomberg.com/news/articles/2026-01-28/ai-customer-support-startup-decagon-valued-at-4-5-billion).
- **Feb 5, 2026 — OpenAI launches Frontier**, a platform for enterprises to build, deploy and
  manage agents. It launched in limited availability, with no public pricing *(official; via
  coverage)* —
  [Constellation Research](https://www.constellationr.com/insights/news/openai-launches-openai-frontier-aims-be-ai-agent-orchestrator).
- **Feb 2026 — Google reports 8M+ paid Gemini Enterprise seats across 2,800+ companies** (Q4 2025
  call) *(official; via coverage)* —
  [PYMNTS](https://www.pymnts.com/google/2026/alphabet-bets-185b-on-gemini-agentic-commerce-and-enterprise-ai/).
- **Apr 22, 2026 — Vertex AI becomes the Gemini Enterprise Agent Platform** (Google Cloud Next
  '26). Agent Engine becomes Agent Runtime, and Vertex AI Studio becomes Agent Studio *(official)* —
  [Google Cloud release notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes?hl=de).
- **May 1, 2026 — Microsoft Agent 365 reaches GA** at ~$15/user/month. **Microsoft 365 E7** ($99,
  bundling E5, Copilot and Agent 365) also launches *(official; via coverage)* —
  [The Register](https://www.theregister.com/2026/03/09/microsoft_adds_a_premium_tier/).
- **May 4, 2026 — Sierra raises a $950M Series E at $15.8B** (Tiger Global, GV) *(official)* —
  [SiliconANGLE](https://siliconangle.com/?p=746652).
- **May 2026 — ServiceNow Knowledge 2026 expands AI Control Tower** into a governance layer
  (discover, govern, secure, observe, measure) for AI across *any* system *(official)* —
  [ServiceNow](https://s205.q4cdn.com/916135447/files/doc_news/ServiceNow-expands-AI-Control-Tower-to-discover-observe-govern-secure-and-measure-AI-deployed-across-any-system-in-the-enterprise-2026.pdf).
- **Jun 17, 2026 — AWS Summit New York.** AgentCore adds runtime instances (persistent compute)
  and a managed web-search tool. AWS also launches AWS Context, a knowledge graph for agents
  *(official)* —
  [AWS News Blog](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/).
  Legacy Bedrock Agents was reportedly renamed "Agents Classic" and closed to new customers from
  Jul 30 *(inferred)* —
  [AWS Builder Center](https://builder.aws.com/content/3ItUUFljIPOutbUGruzDO3RX7Gw/amazon-bedrock-agentcore).
- **Aug 26, 2026 — Salesforce Q2 FY27.** Agentforce ARR >$1.5B on the broadened definition, and
  Agentforce + Data 360 ARR ~$3.9B. Agentforce processed 3.2B Agentic Work Units, up 97% QoQ
  *(official)* —
  [TechMarketView](https://www.techmarketview.com/ukhotviews/archive/2026/08/27/salesforce-q2-keeps-agentforce-growth-story-moving),
  [Pulse 2.0](https://pulse2.com/salesforce-net-income-jumps-87-as-agentforce-and-data-360-arr-surges-more-than-210-to-nearly-3-9-billion/).
- **Sep 15–17, 2026 — Dreamforce** brought 21 announcements. They include long-horizon agents
  (e.g. "Hunter" for outbound sales), **Koa**, a CRM reasoning model on NVIDIA Nemotron (pilot),
  and Agentforce Coworker. Claude becomes selectable in the Atlas Reasoning Engine, the full
  Bedrock model catalog is opened, and Agentforce can orchestrate third-party agents *(official
  list; details inferred from recaps)* —
  [Salesforce](https://www.salesforce.com/blog/dreamforce-2026-announcements/),
  [Cyntexa](https://cyntexa.com/blog/dreamforce-2026-highlights/).
- **Sep 2026 — AgentCore Evaluations adds TypeScript frameworks** and skill evaluators
  *(official)* —
  [AgentCore release notes](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.md).
- **Q3 2026 — SAP moves Joule agents to AI-Unit consumption billing** (reported at 0.02 AI Units
  per agent action). A DSAG user-group survey found only ~3% of SAP customers using SAP Business
  AI productively *(inferred)* —
  [Börse Express](https://www.boerse-express.com/news/articles/sap-aktie-nur-3-prozent-nutzen-joule-produktiv-903874).
- **Oct 13, 2026 — Workday Rising.** Sana becomes Workday's front door and is GA inside Gemini
  Enterprise, Microsoft Copilot, Teams and Slack, with Claude in early access. Workday also adds
  new autopilot agents and an Agent Harness *(official)* —
  [Workday](https://investor.workday.com/news-and-events/press-releases/news-details/2026/Workday-to-Bring-Sana-Everywhere-Employees-Work-Including-Claude-Gemini-Enterprise-Microsoft-Copilot-Slack-and-Teams/default.aspx).
- **Oct 28, 2026 — ServiceNow Q3.** The 2026 AI-ACV target rises to $1.7B, and agentic-AI
  consumption in production is up >13× YTD. ServiceNow also launches a Control Tower Alliance and
  an **AI Passport** for verifying first- and third-party agent scopes *(official)* —
  [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000092/erq3fy26.htm).
- **Oct 28, 2026 — Microsoft Q1 FY27.** The Agent 365 registry passes 50M agents (+30% QoQ), and
  E7 has "millions" of paid seats. Microsoft gave no new Copilot seat count; the July figure was
  >30M *(official, call)* —
  [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/),
  [UC Today](https://uctoday.com/microsoft-q1-copilot-usage-jumps-seat-count-goes-missing).
- **Upcoming — Microsoft Ignite, Nov 17–20, 2026** (San Francisco). No Ignite 2026 announcements
  existed at the time of writing *(official dates)* —
  [Moscone](https://moscone.com/events/microsoft-ignite-2026).

---

## The core value proposition, and its catch

Enterprise agent platforms sell a compelling proposition: **agents pre-integrated with your
enterprise data and workflows, buildable by non-developers, governed and secure, deployable in
weeks.** The value is real:

- **Data/workflow integration.** The platform's agents come pre-connected to the vendor's data and
  applications — Agentforce to Salesforce CRM data, Copilot Studio to Microsoft 365 and the Graph,
  ServiceNow agents to ITSM/workflow data, SAP Joule to SAP's business data. This integration is the
  hard part of enterprise agents, and the platform delivers it out of the box.
- **Low-code/no-code building.** Business users (not just developers) can build agents in a visual
  builder, dramatically widening who can deploy agents — the "citizen developer" model applied to
  agents.
- **Governance and security built in.** The platform provides the permissioning (§13), guardrails
  (§12), audit, and compliance that enterprises require, integrated with the vendor's existing
  identity and governance — a major value-add given how hard §12/§13 are to do yourself.
- **Fast time-to-production.** Pre-built templates and integration mean 4–6 weeks to production for
  common use cases, versus months of custom development.

**The catch is lock-in.** These platforms are deeply tied to the vendor's ecosystem — Agentforce is
most valuable if you're a Salesforce shop, Copilot Studio if you're a Microsoft shop — and the
convenience comes at the cost of dependence on that vendor's data model, pricing, and roadmap. This
is the central tension of the layer: **the same ecosystem integration that makes the platform
valuable makes it a lock-in vector**, and enterprises trade portability for time-to-value. It is the
classic enterprise-software bargain, now for agents.

---

## Platform architecture approaches

The enterprise platforms differ architecturally in ways that shape what they're good for. The
diagram contrasts the dominant approaches:

```mermaid
flowchart TB
    subgraph Anchor["Ecosystem-anchored platforms"]
        direction TB
        A1[Agentforce] --> AD[(Salesforce<br/>CRM data + Flow)]
        A2[Copilot Studio] --> AD2[(Microsoft 365<br/>Graph + Power Platform)]
        A3[ServiceNow agents] --> AD3[(Workflow data<br/>fabric + ITSM)]
        A4[SAP Joule] --> AD4[(SAP business<br/>data)]
    end
    subgraph Open["Open / cross-platform"]
        direction TB
        O1["Google Gemini Enterprise<br/>+ Agent Platform"] --> OD[(Cross-source<br/>enterprise search)]
        O2[AWS Bedrock AgentCore] --> OD2[(Model-agnostic<br/>agent runtime)]
        O3[OpenAI Frontier] --> OD3[(Model-vendor<br/>agent platform)]
    end
    subgraph Common["Shared underlying capabilities (§02–§13)"]
        ORCH[Orchestration] --- MEM[Memory]
        MEM --- TOOL[Tools/MCP]
        TOOL --- GOV[Governance/security]
    end
    Anchor --> Common
    Open --> Common

    classDef anchor fill:#dbeafe,stroke:#2563eb,color:#1e3a8a;
    classDef open fill:#dcfce7,stroke:#16a34a,color:#14532d;
    class A1,A2,A3,A4 anchor;
    class O1,O2,O3 open;
```

The fundamental split is **ecosystem-anchored vs. open/cross-platform**:

- **Ecosystem-anchored** (Agentforce, Copilot Studio, ServiceNow, SAP Joule, Workday) build agents
  *on top of the vendor's data/application moat*. Their power is the deep integration with data the
  enterprise already has in that vendor's system; their limit is that they're most valuable within
  that ecosystem. This is the dominant, highest-adoption approach because it leverages the
  incumbent's existing enterprise position.
- **Open/cross-platform** (Google Gemini Enterprise, formerly Agentspace, plus the Gemini
  Enterprise Agent Platform that replaced the Vertex AI brand in April 2026; AWS Bedrock
  AgentCore; and since February 2026 OpenAI Frontier) bet on being the agent layer *across* an
  enterprise's heterogeneous systems, not tied to one application vendor's data. Their power is
  neutrality: they work with any data or model. Their challenge is lacking the built-in data moat
  the anchored platforms have.

*Nov 2026 note:* the line between the two camps blurred in H2 2026. The anchored vendors now
present themselves as cross-platform *control planes*. Agentforce orchestrates third-party
agents from AWS, Azure and Google. ServiceNow's AI Control Tower governs AI "deployed across any
system," and Agent 365 registers agents built anywhere. They have also opened up their models:
Claude and Bedrock models run inside Agentforce, and Workday's Sana runs inside Copilot, Gemini
Enterprise and Claude *(official)*.

The positioning chart maps the platforms on openness vs. breadth, sized by adoption:

![Enterprise agent platforms: openness vs. breadth](../assets/charts/14_platform_positioning.png)

The high-adoption platforms cluster in the ecosystem-anchored (lower-openness) region, because
riding an incumbent's data/app moat is the winning near-term strategy — enterprises deploy agents
where their data and workflows already live. The open/cross-platform bet (Google, AWS) is the
counter-strategy for enterprises that want a neutral agent layer across systems. OpenAI Frontier,
added in the November 2026 update, sits here too as a model-vendor entrant. The counter-strategy
still fights the
incumbents' integration advantage. This mirrors the §02 orchestration dynamic one level up: the
platform is squeezed between the incumbent's data moat and the open-portability alternative.

---

## The major platforms

A closer look at the leading enterprise platforms and their distinct positions:

- **Salesforce Agentforce.** The customer-facing/CRM agent leader, deeply integrated with Salesforce
  data, Flow, and the Data Cloud. Strongest for customer service, sales, and marketing agents where
  the CRM data is the fuel. Agentforce ARR was >$1.5B as of Q2 FY27 (Aug 2026), on a definition
  that now includes Slackbot and Headless 360; it was ~$800M at FY26 year-end. Agentforce + Data
  360 ARR is ~$3.9B. Consumption-based pricing (Flex Credits) reflects the "agents do work, pay per
  work" model. Dreamforce 2026 (Sep) added long-horizon agents, the Koa CRM reasoning model
  (pilot), and Claude and Bedrock models as reasoning options, along with third-party agent
  orchestration *(official/inferred)*. Its bet: the CRM is where customer-facing agents belong,
  and Salesforce owns the CRM.
- **Microsoft Copilot Studio.** The broadest-reach platform by adoption (~160,000 orgs, 400,000+
  agents), riding Microsoft 365's ubiquity and the Power Platform's low-code base. Strongest for
  employee-facing productivity and internal-process agents integrated with the Microsoft Graph
  (email, docs, Teams). Bundled affordably ($30/user/mo with M365 Copilot). Since May 2026,
  **Agent 365** (GA; ~$15/user/mo standalone, or inside the $99 **M365 E7** suite) provides the
  registry, governance and observability control plane for agents built in Copilot Studio,
  Foundry or third-party frameworks. Its registry passed 50M agents by October 2026 *(official)*.
  Its bet: agents live where employees already work (Microsoft 365), and Microsoft owns that.
- **ServiceNow AI Agents.** The workflow/IT-and-employee-service leader, embedding agents into
  ServiceNow's workflow data fabric and ITSM/HR/customer workflows, with an AI Control Tower for
  governance (April 2026 restructuring embedded AI across tiers by default). Control Tower was
  expanded at Knowledge 2026 (May) to govern AI on *any* system, and gained an AI Passport and a
  Control Tower Alliance in October. The 2026 AI-ACV target was raised to $1.7B *(official)*.
  Strongest for IT/HR/employee-service automation where ServiceNow owns the workflow. Its bet:
  agents belong in the workflow layer, and ServiceNow owns enterprise workflow.
- **SAP Joule.** The SAP-native agent layer (Joule Assistants orchestrating agents across finance,
  supply chain, HR, CX), strongest for enterprises running SAP's business processes. Joule agents
  moved to AI-Unit consumption billing in Q3 2026. A 2026 DSAG survey found only ~3% of SAP
  customers using SAP Business AI productively, and 77% of AI users relying on non-SAP tools such
  as Copilot. That is a pointed reminder that owning the data does not guarantee owning the agent
  *(inferred)*. Its bet: agents belong against the ERP/business-process data SAP owns.
- **Google Gemini Enterprise (formerly Agentspace) + Gemini Enterprise Agent Platform.** The
  open/cross-platform bet: enterprise agents and search across an enterprise's heterogeneous data
  sources, model-flexible and A2A-native. In April 2026 Google folded Vertex AI's agent tooling
  into the Gemini Enterprise Agent Platform. Google reported 8M+ paid Gemini Enterprise seats in
  February 2026 *(official)*. Its bet: enterprises want a neutral agent layer across all their
  systems, not one tied to a single app vendor.
- **AWS Bedrock AgentCore.** The model-agnostic agent runtime/infrastructure bet: provide the
  managed runtime, memory, identity, and tools for enterprises to build and run agents on AWS with
  any model. 2026 additions include a GA harness, persistent runtime instances, managed web search
  and TypeScript evaluations. The older Bedrock Agents product is being wound down to "Classic"
  *(official/inferred)*. More infrastructure than packaged application; competes for the "build
  on our cloud" agent workloads.
- **OpenAI Frontier** *(new in this update)*. OpenAI launched Frontier in February 2026, a
  model-vendor platform for enterprises to build, deploy and manage agents. It was in limited
  availability with undisclosed pricing; named early users in coverage include State Farm, Uber
  and Oracle *(official launch; customer list inferred)*. Its bet: the frontier-model vendor can
  own the agent layer directly, bypassing both app incumbents and clouds.
- **Workday (Illuminate → Sana), Adobe, Atlassian Rovo, and other app-vendors** each build agents
  against their specific data (HR/finance for Workday, creative for Adobe, dev-collaboration for
  Atlassian). This is the "every enterprise app vendor adds agents against its own data" pattern.
  Workday has since rebuilt its front end around the acquired Sana and, as of October 2026,
  distributes Sana *into* rival surfaces: Copilot, Gemini Enterprise, Slack, Teams and Claude
  *(official)*.

The recurring logic: **every enterprise-software incumbent is turning its existing data/workflow moat
into an agent platform**, betting that agents will live where the relevant data already lives. This
is why the layer is so contested — it's not one market but the agentic re-fighting of *every*
enterprise-software category (CRM, productivity, ITSM, ERP, HR) simultaneously, with each incumbent
defending its turf by adding agents.

---

## The competitive landscape

### Competitive table — enterprise agent platforms

| Platform | Vendor | Maturity | Anchor / focus | Notable (confidence) | Differentiator | Competitors |
|---|---|---|---|---|---|---|
| **Agentforce** | Salesforce | shipped-reliable | CRM / customer-facing | >$1.5B Agentforce ARR (broadened definition), Q2 FY27 (official) | CRM data + customer-service agents; now multi-model (Claude, Bedrock) | Copilot Studio, ServiceNow |
| **Copilot Studio + Agent 365** | Microsoft | shipped-reliable | M365 / employee-facing | ~160k orgs (early 2026); Agent 365 GA May 2026, 50M+ registered agents (official) | M365 ubiquity + low-code reach + agent control plane | Agentforce, Google |
| **ServiceNow AI Agents** | ServiceNow | shipped-reliable | Workflow / IT-HR service | AI Control Tower + AI Passport; $1.7B 2026 AI-ACV target (official) | Workflow data fabric + cross-system governance | Copilot Studio, Agentforce |
| **SAP Joule** | SAP | shipped-reliable | ERP / business process | 30+ agents, 2,500+ Joule skills; AI-Unit billing (inferred) | SAP business-data-native agents | Microsoft, Workday |
| **Google Gemini Enterprise (ex-Agentspace) / Agent Platform** | Google | shipped-reliable | Cross-source / open | 8M+ paid seats (Feb 2026); Vertex AI → Agent Platform, Apr 2026 (official) | Neutral cross-system agent layer | Copilot Studio, AWS |
| **AWS Bedrock AgentCore** | Amazon | shipped-reliable | Model-agnostic runtime | Harness GA, runtime instances, Jun 2026 (official) | Build-your-own on AWS, any model | Google, Azure |
| **OpenAI Frontier** *(new)* | OpenAI | demoed-brittle | Model-vendor agent platform | Launched Feb 2026, limited availability (official) | Frontier-model vendor owning the agent layer | Google, AWS, Microsoft |
| **Workday Illuminate / Sana** | Workday | shipped-reliable | HR / finance | Sana as front door; ships into Copilot, Gemini, Claude, Oct 2026 (official) | HR/finance-data-native | SAP, Microsoft |
| **IBM watsonx Orchestrate** | IBM | shipped-reliable | Enterprise multi-agent | IBM ACP merged into A2A (Aug 2025); A2A-compatible (official) | Enterprise orchestration + governance | ServiceNow, Microsoft |
| **UiPath Agentic Automation** | UiPath | shipped-reliable | Back-office / RPA+agents | RPA install base (official) | Agent + deterministic RPA execution | Automation Anywhere, MS |
| **Kore.ai** | Kore.ai | shipped-reliable | CX / conversational | Enterprise CX agents (inferred) | Vendor-neutral CX agent platform | Agentforce, Sierra |
| **Atlassian Rovo** | Atlassian | shipped-reliable | Dev/collaboration | Rovo agents (official) | Agents across Atlassian tools | Microsoft, Glean |
| **Adobe (AEP Agent Orchestrator)** | Adobe | shipped-reliable | Marketing/creative | Adobe agents (official) | Marketing-data-native agents | Salesforce, Microsoft |
| **Sierra / Decagon** | Startups | shipped-reliable | CX (best-of-breed) | Sierra $15.8B (May 2026); Decagon $4.5B (Jan 2026) (official) | Vendor-neutral premium CX agents | Agentforce, Kore.ai |
| **Dust / Glean-agents** (Sana acquired by Workday) | Startups | shipped-reliable | Cross-app employee agents | Glean ~$300M ARR, May 2026 (inferred) | Neutral employee agent platforms | Copilot Studio, Gemini Enterprise |
| **Cohere North / vertical platforms** | Various | demoed→reliable | Vertical/regulated | (inferred) | Domain/regulated agent platforms | incumbents |

That is sixteen entries — well past ten. The structural read: **the layer is dominated by the
enterprise-software incumbents extending their moats, with a band of best-of-breed startups (Sierra,
Decagon for CX; Dust and Glean for cross-app employee agents, with Sana now absorbed by Workday)
betting that neutrality and quality
beat incumbent integration.** The incumbents' advantage is the data/workflow moat and existing
relationships; the startups' advantage is being cross-platform, best-of-breed, and not locked to one
vendor's ecosystem. Both bets are live, and the market is big enough for both — the incumbents win
the "agents against our data" workloads by default, while the startups win the "best agent regardless
of our software stack" and cross-system workloads.

---

## Build vs. buy: the central enterprise decision

The defining strategic question for enterprises in this layer is **build vs. buy** — build agents
custom on the framework layer (§02), or buy a platform. The trade-offs:

- **Buy (platform)** — faster time-to-value (weeks), built-in data integration and governance,
  low-code accessibility, vendor support — at the cost of lock-in, per-seat/consumption pricing that
  scales with usage, and constraint to the vendor's model and capabilities. Best when your use case
  fits the platform's ecosystem (you're a Salesforce shop building customer-service agents) and speed
  matters more than control.
- **Build (custom on frameworks)** — full control, portability, best-of-breed model/component choice,
  and no per-seat platform tax — at the cost of building the integration, governance, and security
  yourself (the hard parts), longer time-to-value, and needing engineering talent. Best when you need
  differentiation, control, portability, or a use case the platforms don't serve well.
- **Hybrid** — the common real answer: buy the platform for standard, ecosystem-fit use cases (fast,
  governed) and build custom for differentiated or cross-system needs. Most large enterprises do
  both.

The nuance that matters: **the platforms' consumption-based pricing changes the calculus at scale.**
The per-work pricing (Agentforce Flex Credits, consumption models) that makes platforms cheap to
start becomes expensive at high volume, at which point building custom (paying model costs directly)
can be cheaper — the classic "buy to start, build at scale" SaaS dynamic. So the build-vs-buy answer
often *changes over time*: buy to prove value fast, then evaluate building for the high-volume,
differentiated workloads where the platform tax and lock-in bite. The enterprises getting this right
treat it as a portfolio decision (buy some, build some) that evolves, not a one-time either/or.

---

## Enterprise realities: governance, integration, change management

What separates enterprise agent platforms from developer tools is that they must handle the *messy
realities* of enterprise deployment, which are as much organizational as technical:

- **Governance and compliance.** Enterprises need to control which agents can access what data, audit
  everything (§11), meet regulatory requirements (§12), and manage agent lifecycle (§13) — the AI
  Control Towers and governance layers the platforms emphasize. This governance is often the *reason*
  enterprises buy a platform rather than build, because doing it themselves is hard.
- **Integration with legacy systems.** Real enterprises run heterogeneous, often-legacy systems, and
  connecting agents to all of them (via connectors, MCP §04, or the platform's integration layer) is
  a major part of the value and the difficulty. The platforms' pre-built connectors are a key
  selling point.
- **Change management and adoption.** The hardest part of enterprise agent deployment is often *not*
  technical but organizational — getting employees to trust and use the agents, redesigning processes
  around them, and managing the workforce implications. Platforms increasingly bundle adoption
  tooling and best practices, because a deployed-but-unused agent delivers no value.
- **Reliability and the human-in-the-loop reality.** Enterprise agents, like all agents, hit the
  reliability limits of the underlying tech (§05, §08, §12), so production enterprise agents are
  mostly *semi-autonomous* — handling well-scoped tasks with human oversight and escalation, not
  fully autonomous operation. The platforms provide the human-in-the-loop and escalation machinery
  this requires.

The enterprise reality check: **an enterprise agent platform's value is as much in the governance,
integration, and adoption support as in the agent capability itself** — because the capability comes
from the shared underlying tech (§02–§13) that everyone has access to, while the *enterprise-grade
packaging* (governance, integration, compliance, support, change management) is what enterprises
actually pay for and can't easily build. This is why the incumbents, who have the enterprise
relationships and the governance/integration infrastructure, are well-positioned despite not having
better underlying agent tech than anyone else.

---

## The customer-experience agent battle

The single most contested enterprise agent use case is **customer experience (CX)** — support,
service, and sales agents — because it has clear ROI (replacing/augmenting expensive human support at
high volume) and touches the customer directly. It is worth examining because it shows the
incumbent-vs-best-of-breed dynamic sharply:

- **The incumbent play (Agentforce).** Salesforce bets that CX agents belong in the CRM, where the
  customer data, case history, and workflows already live — so Agentforce, deeply integrated with
  Salesforce Service Cloud, is the natural choice for the millions of enterprises already on
  Salesforce. The integration is the moat: your agent knows the customer because Salesforce already
  does.
- **The best-of-breed play (Sierra, Decagon).** Startups like Sierra (Bret Taylor) and Decagon bet
  that CX agents are hard enough — and important enough — to warrant a *specialized, best-in-class*
  platform, vendor-neutral and integrating with whatever CRM/systems the enterprise runs. Their pitch
  is superior agent quality and CX-specific depth, not incumbent convenience. Investors backed the
  pitch heavily in 2026. Decagon raised $250M at $4.5B in January, and Sierra raised $950M at
  $15.8B in May. Sierra reportedly reached $150M ARR by early 2026 *(inferred)*, still an order of
  magnitude below Agentforce's ARR.
- **The conversational-AI incumbents (Kore.ai, and the contact-center vendors — Genesys, NICE,
  Five9, and others adding agents).** The existing contact-center and conversational-AI vendors
  extend their platforms with agents, betting their contact-center integration and CX heritage win.

The CX battle illustrates the layer's central question: **does incumbent data integration
(Agentforce) beat best-of-breed quality (Sierra/Decagon) beat CX-specialist heritage (contact-center
vendors)?** The likely answer, as in most enterprise-software history, is *segmentation*: incumbents
win the "good-enough agent on our existing platform" majority by default, best-of-breed wins the
"CX is our differentiator, we want the best" premium segment, and specialists hold their niches. CX
is also where §10 (voice) intersects — many CX agents are voice agents — making it a convergence
point of enterprise platforms, voice, and the underlying agent tech. The volume and clarity of CX
ROI make it the beachhead use case for enterprise agents generally, which is why it's the most
crowded.

## Vertical and regulated-industry platforms

Beyond the horizontal platforms, a growing segment is **vertical-specific and regulated-industry
agent platforms** — agents built for the specific data, workflows, compliance, and domain knowledge
of a particular industry:

- **Healthcare.** Agents for clinical documentation, patient interaction, prior authorization, and
  administrative workflows, requiring HIPAA compliance, clinical accuracy, and integration with EHR
  systems (Epic, Cerner). The stakes (patient safety, regulation) and the domain specificity favor
  specialized platforms and deep domain partnerships.
- **Financial services.** Agents for compliance, fraud, customer service, and analysis, requiring
  the sector's stringent regulation, audit, and accuracy — and often on-prem/private deployment for
  data sensitivity. Both incumbents (with financial-services offerings) and specialists compete.
- **Legal.** Agents for contract analysis, research, and drafting (Harvey, and others), where domain
  accuracy, citation-faithfulness (§07), and professional-liability concerns demand
  specialization — one of the higher-value vertical agent markets.
- **Other verticals** — insurance, manufacturing, retail, government — each developing specialized
  agent platforms tuned to their data, workflows, and compliance.

The vertical dynamic: **regulated and specialized industries favor domain-specific platforms** (or
deeply-customized deployments of horizontal ones) because the domain knowledge, compliance, and
integration requirements are too specific for a generic platform to serve well. This creates space
for vertical specialists (Harvey in legal, healthcare-specific agent companies) alongside the
horizontal incumbents — the "vertical SaaS" pattern repeating for agents. The highest-value vertical
agents are often in domains where expert labor is expensive and the tasks are well-structured
(legal research, clinical documentation), which is the verifier/ROI logic (§09, §11) applied to
industry verticals.

## "Agent washing" and the hype-vs-reality gap

A neutral assessment must address the **hype-vs-reality gap** in enterprise agents, because
"agent washing" — rebranding existing automation or simple chatbots as "AI agents" — is rampant, and
enterprises struggle to separate genuine agentic capability from marketing:

- **The rebranding problem.** Every enterprise-software vendor now calls its features "agents,"
  whether they're genuinely agentic (autonomous, tool-using, reasoning) or just rebranded chatbots,
  RPA, or workflow automation. This makes the market hard to evaluate — "we have agents" means very
  different things across vendors.
- **The pilot-to-production gap.** Many enterprise agent initiatives are impressive pilots that
  struggle to reach reliable production, hitting the reliability limits (§05, §08, §12) that this
  document catalogs. The gap between "demoed in a pilot" and "reliable in production" is where much
  enterprise disappointment lives — the same demoed-brittle-vs-shipped-reliable distinction, at the
  enterprise-deployment level.
- **ROI skepticism.** As spend moved from pilot budgets to production commitments, enterprises
  increasingly demand *demonstrated ROI*, and some early deployments underdelivered — leading to a
  more sober, outcome-focused buying posture in 2026 than the 2024–2025 hype.

The reality-check framing: **enterprise agents are genuinely valuable for well-scoped,
high-ROI, tolerant-of-supervision use cases (CX triage, IT/HR service, document processing) and
oversold for autonomous, high-stakes, long-horizon work the underlying tech can't yet reliably do.**
The 2026 enterprise buyer is more discerning than the 2024 one — asking for proof, scoping realistically,
and distinguishing genuine agentic capability from agent-washed marketing. This maturing skepticism is
healthy and is pushing the market toward honest, outcome-focused deployment. The platforms that win
will be those delivering measurable ROI on realistic use cases, not those with the boldest autonomy
claims.

## Measuring enterprise agent ROI

As the market matures from hype to accountability, **measuring agent ROI** becomes central, and it's
harder than it looks — connecting to the evaluation bottleneck (§11) at the business level:

- **Cost displacement** — the clearest ROI: agents handling work that previously required human labor
  (support tickets deflected, documents processed, tasks automated), measured against the fully-loaded
  cost of the human alternative. Clearest where the task is high-volume and well-defined.
- **Productivity augmentation** — harder to measure: agents making humans more productive (a support
  rep handling more cases with agent assist, a developer shipping more with a coding agent §09). The
  productivity gain is real but diffuse and harder to attribute cleanly.
- **Quality and experience** — hardest: agents improving service quality, response time, or customer
  experience, which affect revenue/retention indirectly and are hard to isolate.
- **The measurement challenge.** Attributing business outcomes to agent deployment (vs. other
  factors), accounting for the full cost (platform fees, integration, oversight, failures), and
  measuring quality/experience gains is genuinely difficult — the §11 evaluation problem at the
  organizational level. Enterprises that measure rigorously make better deployment decisions; those
  that don't fall for agent-washing or over-invest in low-ROI use cases.

The practical guidance mirrors §11: **measure agent ROI rigorously on real business outcomes,
account for full costs including oversight and failures, and start with high-ROI well-defined use
cases where the value is measurable** — because the enterprises succeeding with agents are the ones
treating it as a measured business investment, not a hype-driven initiative. Cost displacement on
high-volume defined tasks is the safest starting ROI; the diffuse productivity and experience gains
are real but harder to bank on up front.

## A deployment maturity model

Enterprises adopting agents progress through a recognizable **maturity curve**, useful for situating
where an organization is:

1. **Experimentation.** Pilots and proofs of concept, exploring what agents can do — impressive
   demos, limited production. Most enterprises passed through this in 2024–2025.
2. **Point solutions.** Deploying agents for specific, well-scoped, high-ROI use cases (CX triage,
   IT service, document processing) in production with human oversight — the 2026 mainstream.
3. **Process integration.** Redesigning business processes *around* agents (not just adding agents to
   existing processes), with governance, monitoring, and change management — where the leading
   enterprises are heading.
4. **Agentic operations.** Fleets of governed, monitored agents integrated across the enterprise,
   with mature governance (AI Control Towers), human oversight where needed, and measured ROI — the
   aspirational near-future state, gated on the reliability/security/governance maturation this
   document tracks.

Most enterprises in 2026 are at stage 2 (point solutions in production) moving toward stage 3 —
which is why governance, integration, and change management (stage-3 concerns) are the platforms'
current emphasis. The progression is gated by the underlying tech (you can't reach agentic operations
while security §12 and reliability §05/§08 limit autonomy) and by organizational readiness (governance,
process redesign, workforce adaptation). Situating an enterprise on this curve clarifies what it
needs next — and the honest assessment is that stage 4 (broad agentic operations) remains
aspirational for most, gated by the same bottlenecks (security, evaluation, reliability, identity)
that gate the whole field.

## Enterprise platforms and the other layers

- **↔ Orchestration (§02).** Platforms are low-code orchestration for non-developers, built on the
  same graph/workflow substrate; they compete with code-first frameworks one abstraction level up.
- **↔ Security & Identity (§12, §13).** Governance, permissioning, and compliance are core platform
  value; the platforms package the hard §12/§13 work.
- **↔ Eval/observability (§11).** Enterprise platforms need production monitoring and governance
  (AI Control Towers) — §11 as an enterprise-governance requirement.
- **↔ Voice/CX (§10).** Customer-experience agents (Agentforce, Sierra, Decagon, Kore.ai) span this
  layer and the voice/multimodal layer.
- **↔ Standards (§15).** Enterprises want portability (avoid lock-in), driving demand for MCP/A2A
  support even within proprietary platforms — the standards are the enterprise's hedge against
  platform lock-in.

---

## Failure modes specific to enterprise platforms

1. **Lock-in regret.** Deep platform dependence becomes costly/constraining. Mitigate with
   standards (MCP/A2A) support and a portability strategy.
2. **Consumption-cost blowup.** Per-work pricing scales unexpectedly at volume. Mitigate with cost
   monitoring and build-vs-buy re-evaluation at scale.
3. **Integration gaps.** The platform doesn't connect well to a critical legacy system. Mitigate
   with connector/MCP evaluation before committing.
4. **Adoption failure.** Agents deployed but unused due to poor change management. Mitigate with
   adoption planning, not just technical deployment.
5. **Governance/compliance gaps.** The platform's governance doesn't meet a regulatory requirement.
   Mitigate with compliance evaluation up front.
6. **Over-promised autonomy.** Expecting full autonomy where the tech only supports semi-autonomous.
   Mitigate with realistic scoping and human-in-the-loop design.
7. **Capability ceiling.** The platform's low-code model can't express a needed complex behavior.
   Mitigate with hybrid build-on-frameworks for complex cases.

---

## System of record vs. system of action

A framing that clarifies the strategic stakes of this layer: the incumbents own the enterprise
**systems of record** (the databases of truth — CRM, ERP, ITSM, HR), and the agent era threatens to
introduce a new **system of action** — the agent layer that *does things* across those systems of
record. The strategic question is *who owns the system of action*, and it is existential for the
incumbents:

- **The incumbent bet** is that the system of action should live *with* the system of record — your
  CRM agent belongs in the CRM, your ERP agent in the ERP — so the incumbents extend their systems of
  record into systems of action, defending their position. This is why every incumbent is racing to
  add agents: to prevent a new agent layer from disintermediating them.
- **The disruptor bet** (Google Gemini Enterprise, OpenAI Frontier, best-of-breed startups, cross-app platforms) is that the
  system of action should be a *neutral layer above* the systems of record — an agent layer that
  orchestrates across all of them, owned by whoever provides the best cross-system agent experience.
  If this bet wins, the incumbents' systems of record become commoditized data sources *below* a new
  control layer — a strategic threat.
- **The stakes.** Whoever owns the system of action owns the primary interface through which work
  gets done, potentially relegating the systems of record to back-end data stores. This is why the
  incumbents are investing so heavily and defensively — they are protecting against being demoted from
  "where work happens" to "where data sits." It is the same disruption pattern that plays out in
  every platform shift, now for agents.

The likely outcome, given incumbent strength and enterprise inertia, is **contested coexistence**:
incumbents successfully extend into systems of action for workloads centered on their data (defending
their turf), while a neutral cross-system agent layer emerges for genuinely cross-system work and for
enterprises wanting vendor-neutrality. The incumbents mostly hold their ground but don't monopolize
the new layer. This framing explains the intensity of the land-grab: it's not just a new product
category, it's a potential re-ordering of who sits at the top of the enterprise-software stack, and
the incumbents are fighting to not be pushed down it.

## The workforce and organizational dimension

Enterprise agents raise workforce implications that shape adoption and can't be ignored in a complete
assessment:

- **Augmentation vs. displacement.** The dominant near-term pattern is *augmentation* — agents making
  workers more productive (handling routine work so humans focus on judgment/exceptions) rather than
  wholesale displacement. But the displacement concern is real for high-volume routine roles (Tier-1
  support, data entry), and it affects both the ethics and the internal politics of adoption.
- **Change management and trust.** Employees must trust and adopt agents for value to materialize, and
  fear (of displacement, of errors, of the unfamiliar) impedes adoption. Successful deployments invest
  heavily in change management — involving employees, demonstrating augmentation not replacement, and
  redesigning roles thoughtfully. The technical deployment is often easier than the human one.
- **New roles.** Agent deployment creates new roles — agent supervisors/reviewers (the human-in-the-
  loop, §02), agent operations, and the "manages a fleet of agents" role that coding (§09) previewed.
  The workforce shifts toward *directing and overseeing* agents rather than doing the routine work
  directly.
- **The organizational-readiness gate.** Beyond technology, enterprises must be *organizationally
  ready* — processes redesigned, governance in place, workforce prepared — which is often the binding
  constraint on how fast agents can be adopted, more than the technology. The maturity model above is
  as much organizational as technical.

The honest framing: **enterprise agent adoption is as much an organizational transformation as a
technology deployment**, and the platforms increasingly recognize this by bundling change-management,
adoption, and governance support. The enterprises succeeding treat agents as a socio-technical change
(people, process, and technology together), not a software rollout — and the workforce implications,
handled well (augmentation, reskilling, thoughtful role redesign) or poorly (fear, resistance, botched
displacement), substantially determine whether the deployment delivers value. This human dimension is
easy to underweight in a technology-focused analysis but is frequently the actual determinant of
enterprise agent success or failure.

## A brief history of enterprise agent platforms

The arc explains the current land-grab. **Before 2024**, enterprise "AI" meant predictive ML,
analytics, and simple chatbots/RPA — useful but not agentic, and mostly bought as point solutions or
built by data-science teams. There was no "agent platform" category. **2024** was the pivot: as
LLM agents proved capable, every enterprise-software incumbent scrambled to add agents — Salesforce
launched Agentforce, Microsoft repositioned Copilot Studio around agents, ServiceNow, SAP, and the
others followed. The category was born from incumbents defending their turf against the agent
disruption, and the initial wave was heavy on announcements and pilots.

**2025** was the buildout and hype peak: the platforms matured, adoption grew from pilots toward
production, best-of-breed startups (Sierra, Decagon, Glean) raised big on the neutral/premium bet,
and "agent" became the dominant enterprise-software marketing theme (with the attendant agent-washing).
The build-vs-buy and lock-in debates crystallized. **2026** is the current state: enterprise agents
moved decisively from pilot budgets to production commitments (the Agentforce ARR, Copilot Studio
adoption numbers), the market is large and fast-growing, the incumbents dominate via data moats while
best-of-breed holds niches, consumption/outcome pricing spread, and — importantly — a more sober,
ROI-focused, agent-washing-skeptical buyer emerged. The arc is the classic enterprise-software land-
grab compressed into ~two years: a new category, incumbents defending and disruptors attacking, hype
then sobering, converging toward measured production deployment. What's distinctive is the *speed* and
the *breadth* — it's not one category being disrupted but *every* enterprise-software category
simultaneously adding agents, which is why the layer is so crowded and contested. **Late 2026**
added three new features. The vendors moved from pure revenue to *usage* disclosures (Agentic Work
Units, registered agents, consumption multiples), and they keep redefining those metrics. A
control-plane race opened (Agent 365, AI Control Tower, Gemini Enterprise Agent Platform).
Frontier-model vendors entered directly, with OpenAI Frontier.

## Agent marketplaces and the ecosystem play

An emerging dimension of the platform battle is **agent marketplaces** — the platforms building
ecosystems where third parties (ISVs, partners, the enterprise's own teams) publish pre-built agents
that others can discover, buy, and deploy. This mirrors the app-store/app-exchange strategy that
made previous platforms sticky:

- **Salesforce's AgentExchange, Microsoft's agent marketplace, ServiceNow's store**, and others let
  partners distribute agents and let enterprises find pre-built agents for common use cases —
  extending the platform's value through an ecosystem and deepening lock-in (agents built for one
  marketplace don't trivially move).
- **The ecosystem flywheel.** A marketplace with many quality agents attracts more enterprises,
  which attracts more agent-builders, which attracts more enterprises — the classic platform
  flywheel, now for agents. The incumbents with existing partner ecosystems (Salesforce's ISV base,
  Microsoft's) have a head start replicating it for agents.
- **The standards tension.** Marketplaces are inherently platform-specific (deepening lock-in),
  which is in tension with the enterprise's standards-based portability desire — so the marketplaces
  increasingly support MCP/A2A to let marketplace agents interoperate, balancing ecosystem lock-in
  against portability demands.

The strategic point: **agent marketplaces are how the platforms convert a product into an
ecosystem**, extending value and stickiness beyond the platform's own agents to a whole third-party
economy — and the incumbents' existing partner ecosystems give them another advantage in building
them. Whether these marketplaces become genuinely valuable (like the successful app stores) or
struggle (like many enterprise-software marketplaces did) depends on whether third-party agents
deliver enough value to sustain the flywheel, which is still being determined. But the *strategy* —
own the marketplace, own the ecosystem, deepen the moat — is a clear part of the platform land-grab,
and it is another front on which incumbents leverage their existing partner relationships.

*Nov 2026 update:* the ecosystem play is shifting from *marketplaces of agents* to **registries
and control planes for agents**. These are places where agents from *any* vendor get
discovered, permissioned, observed and, where needed, killed. Examples are Microsoft Agent 365's
registry (50M+ agents), ServiceNow's AI Passport for third-party agent scopes, and Agentforce's
third-party agent orchestration *(official)*. App vendors are also distributing their agents
*through* rivals' surfaces: Workday ships Sana into Copilot, Gemini Enterprise, Slack and Claude.
That suggests the durable lock-in point may be the governance registry more than the storefront
*(inferred)*.

## Roadmap and outlook (confidence-tagged)

- **Incumbents dominate via data/workflow moats** *(official trend; high confidence).* Salesforce,
  Microsoft, ServiceNow, SAP, and the app vendors ride their existing enterprise positions; agents
  live where the data lives, favoring incumbents. — *Nov 2026: confirmed on revenue. Agentforce
  ARR is >$1.5B, ServiceNow's AI-ACV target is $1.7B, and the Agent 365 registry holds 50M+
  agents. One caveat: SAP's DSAG survey shows owning the data does not guarantee agent adoption.*
- **Consumption/outcome pricing matures** *(inferred; medium-high confidence).* "Pay for work done"
  pricing (Flex Credits and successors) spreads, shifting agent economics toward outcome-based models
  — and driving the build-at-scale calculus. — *Nov 2026: confirmed. SAP moved Joule to AI-Unit
  billing and Salesforce now reports Agentic Work Units. Microsoft, however, layered a per-user
  control-plane fee (Agent 365, E7) on top, so hybrid seat-plus-consumption is the actual pattern.*
- **Standards support becomes an enterprise requirement** *(inferred; high confidence).* Enterprises
  demand MCP/A2A support to hedge lock-in, so even proprietary platforms add interoperability — the
  standards are the enterprise's portability insurance. — *Nov 2026: confirmed and extended to
  models. Agentforce added Claude and Bedrock models plus third-party agent orchestration, and
  Workday ships Sana into rival surfaces.*
- **Best-of-breed startups hold the neutral/cross-system and premium niches** *(inferred; medium
  confidence).* Sierra/Decagon (CX), Glean/Dust (cross-app employee agents) sustain on neutrality and
  quality against incumbent integration, especially for cross-system and best-in-class needs. —
  *Nov 2026: holding, and richly valued (Sierra $15.8B, Decagon $4.5B). Sana's absorption into
  Workday shows the consolidation path for those that don't scale independently.*
- **Semi-autonomous is the enterprise reality through 2026–2027** *(inferred; high confidence).*
  Reliability and security limits (§05, §08, §12) keep enterprise agents human-overseen for
  consequential work; platforms compete on making semi-autonomous operation productive and governed.
  — *Nov 2026: still true. Even so, "long-horizon" agents that pursue goals over days or weeks
  (Agentforce, Dreamforce 2026) are entering pilot. Watch whether they reach GA with meaningful
  autonomy.*
- **New (Nov 2026): the agent control plane becomes the main battleground for 2027**
  *(inferred; medium-high confidence).* Registry, identity, observability and kill-switch layers
  that govern *any* vendor's agents are now core SKUs (Agent 365, AI Control Tower/AI Passport,
  Gemini Enterprise Agent Platform). Expect Ignite (Nov 17–20) and re:Invent (early Dec) to
  extend them. Expect consolidation pressure on standalone agent-governance startups.
- **New (Nov 2026): model vendors compete directly for the enterprise agent layer**
  *(speculative; medium confidence).* OpenAI Frontier's move from limited availability to broad
  availability, and its pricing, are the signals to watch in H1 2027. The question is whether
  incumbents respond by deepening multi-model neutrality, as Agentforce did with Claude and
  Bedrock.

---

## Interoperability as the enterprise's lock-in hedge

A dynamic worth developing because it shapes the whole layer's future: enterprises, having learned
hard lessons about vendor lock-in from previous software eras, are actively using **standards
(MCP, A2A) as a hedge** against agent-platform lock-in — and this is reshaping how the platforms
position:

- **Enterprises demand portability.** Burned by past lock-in, sophisticated enterprise buyers ask
  "can I move my agents/tools/data if I switch platforms?" and prefer platforms that support open
  standards (MCP for tools §04/§15, A2A for agent-to-agent §06) over fully-proprietary ones. Standards
  support is becoming a procurement requirement.
- **The platforms respond by supporting standards — cautiously.** Even the ecosystem-anchored
  incumbents add MCP/A2A support (Google is A2A-native; the others add MCP tool support) because
  refusing would cost deals — while still designing for stickiness through data integration and
  workflow depth. The result is platforms that are *interoperable at the edges* (tools, agent-to-agent)
  but *sticky at the core* (data, workflows, governance). Enterprises get portability of the pieces
  that are easy to standardize and lock-in on the pieces that aren't.
- **The multi-platform reality.** Large enterprises end up running *multiple* agent platforms
  (Agentforce for CX, Copilot Studio for productivity, custom for differentiation), and want them to
  *interoperate* — driving demand for cross-platform agent orchestration and the standards that enable
  it. No single platform serves all of a large enterprise's needs, so interop across platforms becomes
  a real requirement, not just a lock-in hedge.

The strategic implication: **the standards (§15) function as the enterprise's insurance policy against
platform lock-in**, and enterprise demand is a major force pushing even proprietary platforms toward
interoperability. This is a healthy dynamic — it means the lock-in is bounded (your tools and
agent-to-agent connections are portable even if your platform isn't), and it connects this layer
directly to §15's standards story: enterprises adopting agents at scale are a primary *demand-side*
driver of the standards' consolidation, because they need the portability the standards provide. The
platforms that embrace this (offering both deep integration *and* standards-based portability) reduce
buyer lock-in anxiety and win deals; those that resist it face procurement friction.

## Integration and connectors: the unglamorous moat

Beneath the agent capability, a large part of enterprise-platform value — and a real competitive moat
— is the **breadth and quality of integrations/connectors** to enterprise systems, because an agent is
only as useful as the systems it can reach:

- **Connector breadth.** The platforms compete on how many enterprise systems they connect to
  out-of-the-box (databases, SaaS apps, legacy systems). An agent that can't reach the system holding
  the relevant data is useless, so pre-built connectors are a key value-add and a real moat (building
  and maintaining hundreds of connectors is hard, ongoing work). The incumbents' existing integration
  ecosystems (Salesforce's AppExchange, Microsoft's connectors, MuleSoft, etc.) are a genuine
  advantage.
- **MCP as the connector standard.** MCP (§04/§15) is increasingly the *standard* way to expose
  enterprise systems to agents, and the growing ecosystem of MCP servers (18,000+) means agents can
  connect to more systems via a common protocol — partially commoditizing the connector advantage over
  time, and giving enterprises a standard integration path that reduces platform lock-in on the
  integration axis.
- **Data readiness.** Even with connectors, agents need the underlying enterprise data to be
  accessible, clean, and permissioned (§07's ingestion problem, §13's permission-aware access at the
  enterprise level) — and much enterprise data isn't, making "data readiness" a common gating
  constraint on enterprise agent value. The unglamorous data-plumbing work (§07's "ingestion
  determines the ceiling") applies at enterprise scale.

The integration reality: **enterprise agent value is gated by integration breadth and data
readiness** — the agent capability is table stakes (shared underlying tech), but reaching the right
systems with the right data, permissioned correctly, is the hard, moat-worthy work. This is another
reason incumbents (with existing integration ecosystems and data) are well-positioned, and another
place where the unglamorous plumbing, not the flashy agent capability, determines real-world value.
MCP's spread is slowly commoditizing the connector layer, which over time erodes this incumbent moat —
a dynamic worth watching, as it could shift advantage toward the neutral cross-platform players if the
connector advantage that anchors the incumbents becomes a standard everyone has.

## Section takeaways

- Enterprise agent platforms are the **packaging/distribution layer** (maturity 6.0, contestedness
  7.0) that turns agent tech (§02–§13) into deployable, governed business software — and enterprise
  agentic AI moved from **pilots to production commitments**: Agentforce >$1.5B ARR (Aug 2026,
  broadened definition), Copilot Studio ~160k orgs/400k agents, an Agent 365 registry of 50M+
  agents, and a ~$8B→$53B market at ~46% CAGR.
- The value is **pre-integrated data/workflows + low-code building + built-in governance + fast
  time-to-production**; the catch is **ecosystem lock-in** — the integration that creates value
  creates dependence.
- The architectural split is **ecosystem-anchored** (Agentforce/CRM, Copilot Studio/M365,
  ServiceNow/workflow, SAP Joule/ERP — ride the incumbent's data moat, highest adoption) vs.
  **open/cross-platform** (Google Gemini Enterprise, AWS AgentCore, OpenAI Frontier — neutral layer
  across systems). By late 2026 both camps are converging on cross-vendor **agent control planes**.
- **Every enterprise-software incumbent is turning its data/workflow moat into an agent platform** —
  the layer is the agentic re-fight of every enterprise-software category at once.
- **Build vs. buy** is the central decision: buy for speed/fit/governance, build for control/
  portability/differentiation, hybrid in practice — and the answer **changes at scale** as
  consumption pricing bites (buy to start, build for high-volume differentiated workloads).
- The platform's real value is as much **governance, integration, and adoption support** as agent
  capability (which is shared underlying tech) — favoring incumbents with enterprise relationships;
  **standards (MCP/A2A) support is the enterprise's lock-in hedge**; and **semi-autonomous with
  human oversight** is the production reality.

- The deeper strategic contest is **system of record vs. system of action** — incumbents extend their
  data moats into agents to avoid being demoted to back-end data stores below a new neutral agent
  layer; the likely outcome is contested coexistence. Enterprises use **standards (MCP/A2A) as a
  lock-in hedge**, making standards support a procurement requirement and enterprises a key demand-side
  driver of §15's consolidation.
- Value is gated by **integration breadth and data readiness** (the unglamorous connector/plumbing
  moat, slowly commoditized by MCP), and adoption is as much **organizational transformation**
  (change management, workforce, process redesign) as technology — with a maturity curve from
  experimentation → point solutions → process integration → agentic operations, where most
  enterprises sit at "point solutions in production" and stage 4 remains gated by the field's
  security/reliability/identity bottlenecks. **Agent marketplaces** are the ecosystem play deepening
  the moat.

*Word count target: 6,500. This section: ~8,600 after the November 2026 update, including the update log and sources list (verified via `wc`).*

## Sources (November 2026 update)

- TechMarketView, Salesforce Q2 FY27 — https://www.techmarketview.com/ukhotviews/archive/2026/08/27/salesforce-q2-keeps-agentforce-growth-story-moving
- Pulse 2.0, Salesforce Q2 FY27 Agentforce + Data 360 ARR — https://pulse2.com/salesforce-net-income-jumps-87-as-agentforce-and-data-360-arr-surges-more-than-210-to-nearly-3-9-billion/
- Salesforce Q2 FY27 release (Seeking Alpha PR mirror) — https://seekingalpha.com/pr/20631301
- Nasdaq, Salesforce Q2 call highlights — https://www.nasdaq.com/articles/salesforce-q2-earnings-call-highlights
- Salesforce, 21 things announced at Dreamforce 2026 — https://www.salesforce.com/blog/dreamforce-2026-announcements/
- Cyntexa, Dreamforce 2026 highlights — https://cyntexa.com/blog/dreamforce-2026-highlights/
- Microsoft FY27 Q1 earnings call (investor page) — https://www.microsoft.com/en-us/investor/events/fy-2027/earnings-fy-2027-q1
- Motley Fool, Microsoft Q1 FY27 transcript — https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/
- UC Today, Copilot seats unreported in Q1 FY27 — https://uctoday.com/microsoft-q1-copilot-usage-jumps-seat-count-goes-missing
- The Register, Microsoft 365 E7 — https://www.theregister.com/2026/03/09/microsoft_adds_a_premium_tier/
- Let's Data Science, M365 E7 / Agent 365 — https://letsdatascience.com/news/microsoft-launches-e7-enterprise-ai-subscription-396f64d4
- Moscone Center, Microsoft Ignite 2026 dates — https://moscone.com/events/microsoft-ignite-2026
- ServiceNow Q3 2026 8-K — https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000092/erq3fy26.htm
- ServiceNow, AI Control Tower expansion (Knowledge 2026) — https://s205.q4cdn.com/916135447/files/doc_news/ServiceNow-expands-AI-Control-Tower-to-discover-observe-govern-secure-and-measure-AI-deployed-across-any-system-in-the-enterprise-2026.pdf
- Google Cloud, Gemini Enterprise Agent Platform release notes — https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes?hl=de
- HPCwire, Gemini Enterprise Agent Platform launch — https://www.hpcwire.com/aiwire/2026/04/23/google-unveils-gemini-enterprise-agent-platform/
- PYMNTS, Alphabet / Gemini Enterprise seats — https://www.pymnts.com/google/2026/alphabet-bets-185b-on-gemini-agentic-commerce-and-enterprise-ai/
- AWS, top announcements of AWS Summit New York 2026 — https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/
- AWS, AgentCore release notes — https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.md
- AWS Builder Center, AgentCore overview (Agents Classic) — https://builder.aws.com/content/3ItUUFljIPOutbUGruzDO3RX7Gw/amazon-bedrock-agentcore
- Constellation Research, OpenAI Frontier launch — https://www.constellationr.com/insights/news/openai-launches-openai-frontier-aims-be-ai-agent-orchestrator
- PYMNTS, OpenAI Frontier — https://www.pymnts.com/news/artificial-intelligence/2026/openai-targets-enterprise-market-with-new-ai-agent-platform/
- Workday, Sana everywhere employees work (Oct 13, 2026) — https://investor.workday.com/news-and-events/press-releases/news-details/2026/Workday-to-Bring-Sana-Everywhere-Employees-Work-Including-Claude-Gemini-Enterprise-Microsoft-Copilot-Slack-and-Teams/default.aspx
- Constellation Research, Workday Rising 2026 — https://constellationr.com/insights/news/workday-makes-sana-its-interface-launches-agent-harness-decision-and-work
- Börse Express, DSAG survey on Joule usage — https://www.boerse-express.com/news/articles/sap-aktie-nur-3-prozent-nutzen-joule-produktiv-903874
- SiliconANGLE, Sierra $950M Series E — https://siliconangle.com/?p=746652
- Sierra, $100M ARR post — https://sierra.ai/uk/blog/100m-arr
- Bloomberg, Decagon $4.5B — https://www.bloomberg.com/news/articles/2026-01-28/ai-customer-support-startup-decagon-valued-at-4-5-billion
- Crypto Briefing, Glean $300M ARR — https://cryptobriefing.com/glean-300m-arr-enterprise-ai-growth/
- Hostinger, agentic AI statistics (Gartner spending figures, secondary) — https://www.hostinger.com/tutorials/?p=151992
