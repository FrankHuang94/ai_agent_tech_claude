# 15 — Standards and Interoperability Landscape

*The connective tissue. MCP, A2A, and competing proposals; the consolidation path; and what
historical standards fights tell us about where this goes. Target: 6,500 words. Current as of
November 2026 (snapshot of July 22, 2026, updated).*

---

## The most consequential meta-story in the agent stack

Standards and interoperability is not a technology layer but the **connective tissue** that
determines whether the whole agent ecosystem coheres or fragments — and it is the subject of the most
consequential meta-story in the field. In the executive summary it scores **4.0/10 maturity, 9.0/10
contestedness** — the *most contested* dimension of the entire stack, because standards fights are
inherently contests over control, and getting the standard wrong (or having no standard) fragments
everything built on top.

But the headline finding of this section is optimistic and somewhat surprising: **the agent-standards
fight is consolidating far faster than standards fights historically do.** MCP going from an Anthropic
experiment (late 2024) to a Linux-Foundation-governed standard backed by OpenAI, Google, Microsoft,
and AWS (by end of 2025) is one of the fastest standards convergences in computing history — closer to
the organic speed of a de-facto winner like JSON than the grinding pace of a committee standard. A2A
is following the same path a year behind — and since August 2026 sits beside MCP in the same
foundation. This section maps the landscape, explains *why* it's consolidating so fast, examines the
genuinely open contests (the residual agent-to-agent alternatives, the payments land-grab), and uses
historical standards fights to predict where it lands.

Why does a document about *technology* devote a full section to *standards*? Because in a multi-vendor
ecosystem, the standards are not a footnote to the technology — they are what decides whether the
technology composes into a coherent whole or fractures into incompatible islands. An agent stack where
every capability layer is excellent but nothing interoperates is worth far less than the sum of its
parts. The standards are the difference between fifteen brilliant layers that snap together and
fifteen brilliant layers that don't. That is why this "non-technology" layer is one of the most
strategically important in the document, and why its unusually fast, unusually cooperative
consolidation is such a consequential piece of good news for the field.

---

## What changed since July 2026 (November 2026 update)

The four months since the July 22 snapshot mostly *confirmed* this section's consolidation thesis,
and in places moved faster than it predicted. MCP shipped its largest revision so far, a stateless
core built for horizontally scaled remote servers. A2A moved into the Agentic AI Foundation (AAIF), so
the tool layer and the agent-to-agent layer now share one neutral home. The AAIF grew from a single
protocol's home into a broad umbrella: ten hosted projects and more than 300 members. Two corrections
to the snapshot are also needed. First, the "A2A vs. ACP" contest the snapshot treated as open had
already been settled in August 2025, when IBM's Agent Communication Protocol merged into A2A. The
snapshot had mixed up IBM's ACP with the separate Cisco-led AGNTCY project. Second, the payments
protocols had already begun moving to neutral homes in April 2026, a change the snapshot missed.

**Dated log of material developments:**

- **Aug 29, 2025 (missed by snapshot): IBM's ACP merges into A2A** under the Linux Foundation; the
  ACP team wound down independent development and published a migration path *(official)*
  ([LF AI & Data](https://lfaidata.foundation/?p=7689)).
- **Feb 17, 2026 (missed): NIST's CAISI launches the AI Agent Standards Initiative**, with pillars on
  industry-led standards, open protocols, and agent security/identity *(official)*
  ([NIST](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure)).
- **Mar 12, 2026 (missed): A2A v1.0**, the first stable release (`tasks/list`, modernized OAuth flows,
  gRPC multi-tenancy); v1.0.1 followed on May 28 *(official)* ([A2A releases](https://github.com/a2aproject/A2A/releases)).
- **Apr 2026 (missed): payments protocols go neutral.** The **x402 Foundation** launched under the
  Linux Foundation, with Coinbase contributing x402 and Cloudflare and Stripe as co-developers
  *(official)* ([Coinbase docs](https://docs.cdp.coinbase.com/x402/support/x402-foundation)). Google
  **donated AP2 to the FIDO Alliance** alongside Mastercard's Verifiable Intent, and FIDO formed
  agentic-authentication and payments working groups *(official)*
  ([Google](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/)).
- **Jul 23, 2026: IETF 126 (Vienna)** held a working-group-forming BoF on agent communication
  protocols (`agentproto`) and a BoF on agent discovery (DAWN). Secondary reports conflict on whether
  a working group has since been chartered *(inferred)*
  ([IETF 126 slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-agentproto-agentproto-03)).
- **Jul 28, 2026: MCP specification `2026-07-28` final.** It has a stateless core (the initialize
  handshake and `Mcp-Session-Id` are retired, and per-request `_meta` replaces them). Multi
  Round-Trip Requests replace server-initiated elicitation and sampling. It also adds header-based
  routing, cacheable list results, and authorization hardening (RFC 9207 issuer validation; Client ID
  Metadata Documents preferred over Dynamic Client Registration), plus a formal extensions framework
  (Tasks, MCP Apps, Enterprise-Managed Authorization). Roots, Sampling, Logging and the legacy HTTP+SSE
  transport are deprecated with twelve-month windows. Tier-1 SDKs report "close to half-a-billion
  downloads a month" *(official)* ([MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/)).
- **Aug 2026: AAIF adds 57 members (247 total)**, including Alibaba, Visa and Wells Fargo *(official)*
  ([LF press](https://www.linuxfoundation.org/press/agentic-ai-foundation-welcomes-57-new-members-gaining-major-financial-services-players-and-apac-leaders)).
- **Aug 17, 2026: A2A joins the AAIF as a hosted project**, alongside MCP, goose and AGENTS.md. A few
  secondary outlets give Aug 20 *(official)* ([AAIF](https://aaif.io/blog/a2a-joins-aaif)).
- **Aug 22, 2026: new MCP roadmap.** It sets five undated priorities: agentic messaging primitives
  (server-initiated events, Tasks into the core spec), HTTP-native transport unification, agent
  identity and enterprise security (DPoP, workload identity federation, ID-JAG, in coordination with
  the IETF OAuth and WIMSE working groups), improved primitives (progressive discovery for large tool
  catalogs), and SDK experience. A Server Card working group is standardizing `.well-known` discovery
  *(official)* ([roadmap post](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2026-08-22-mcp-roadmap.md)).
- **Sep 9, 2026: Agent Router (formerly Envoy AI Gateway) becomes a standalone AAIF project**
  *(official)* ([Tetrate](https://tetrate.io/blog/agent-router-joins-aaif)).
- **Oct 2026: the x402 Foundation names an executive director (Oct 1).** A tracker also reports that
  Block has joined the foundation and added Bitcoin Lightning support. Fireblocks separately reports that monthly x402 transactions fell about 92% from their
  December 2025 peak *(inferred; tracker and analyst sources)*
  ([tracker](https://agenticplug.ai/current-state-of-agentic-commerce)).
- **Oct 2026: the MCP Registry is still labeled preview.** Third-party censuses count about
  43,000–47,500 active servers, up from about 18,000 community-indexed in mid-2026 *(inferred)*
  ([LocalCan census](https://www.localcan.com/blog/state-of-mcp-server-development)).
- **Oct 22, 2026: at AGNTCon + MCPCon North America, the AAIF adds Agent Skills (Anthropic), Open
  Responses (OpenAI), OpenEnv (Hugging Face) and OpenSandbox (Alibaba).** That brings it to 10 hosted
  projects, and membership passes 300 *(official)*
  ([LF press](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox);
  [LF press](https://www.linuxfoundation.org/press/agentic-ai-foundation-surpasses-300-members-in-less-than-one-year)).
  Coverage describes the conference agenda as shifting from new protocol features to security and
  identity *(inferred)* ([InfoQ](https://www.infoq.com/news/2026/10/agntcon-mcpcon-2026/)).

**Net effect.** The tool layer is more settled than in July. The agent-to-agent layer has moved from
"leading" to "consolidating," because its only same-layer rival folded into A2A and A2A now shares
MCP's foundation. The payments layer is still commercially contested, but it now has neutral
governance (FIDO for AP2, the Linux Foundation for x402). The frontier has moved to agent
**identity**, which MCP's roadmap, the IETF BoFs and NIST's initiative all target.

---

## The layered standards stack, revisited

§06 introduced the key insight that the agent-interop standards form a *layered stack* of
complementary protocols, not a single winner-take-all fight. This is worth restating as the
organizing frame, because the most common analytical error — treating "MCP vs. A2A" as rivals — comes
from missing it. The standards address *different layers* and mostly *compose*:

```mermaid
flowchart TB
    subgraph App["Application / agent logic"]
        AGENT[The agent]
    end
    subgraph AgentLayer["Agent-to-agent layer"]
        A2A["A2A — consolidating (AAIF; absorbed IBM ACP)"]
        AGNTCY["AGNTCY (SLIM / OASF) — complementary"]
    end
    subgraph ToolLayer["Tool / context layer"]
        MCP["MCP — won (AAIF)"]
    end
    subgraph DiscoveryLayer["Discovery / identity layer"]
        ANP[ANP — decentralized]
        OASF[OASF / Agent Cards]
    end
    subgraph PayLayer["Payments / commerce layer"]
        AP2[AP2]
        ACOMM[Agentic Commerce Protocol]
        X402[x402]
    end
    subgraph Foundation["Web foundations (reused)"]
        OAUTH[OAuth 2.1 / OIDC]
        HTTP[HTTP / JSON-RPC / SSE]
    end

    AGENT --> A2A
    AGENT --> MCP
    A2A -.discovery.-> OASF
    A2A -.identity.-> ANP
    A2A --> PayLayer
    A2A --> Foundation
    MCP --> Foundation
    AGNTCY -.complements.-> A2A

    classDef won fill:#dcfce7,stroke:#16a34a,color:#14532d;
    classDef leading fill:#dbeafe,stroke:#2563eb,color:#1e3a8a;
    classDef contested fill:#fef9c3,stroke:#d97706,color:#713f12;
    class MCP won;
    class A2A leading;
    class AGNTCY,AP2,ACOMM,X402,ANP contested;
```

Read the colors: **MCP has *won* the tool/context layer** (green — settled de-facto standard); **A2A
is *leading* the agent-to-agent layer** (blue — front-runner but a year younger; IBM's ACP merged
into it in August 2025, and the Cisco-led AGNTCY stack now positions its SLIM transport and OASF
schema as complements rather than rivals); and the **discovery, identity, and payments layers are
*contested*** (yellow — multiple proposals, no winner, though AP2 and x402 now have neutral homes). The whole stack rests on reused web foundations (OAuth 2.1, HTTP,
JSON-RPC, Server-Sent Events) — the standards *extend* the web rather than replacing it, which is a
large part of why they adopted so fast.

The critical reframe: **there is no single "the agent standard" — there is a stack of layer-specific
standards, some settled, some contested, that compose.** The interesting questions are *within* layers
(A2A vs. ACP for agent-to-agent; the payments contest), not *across* them, and the layers are at very
different maturity stages.

---

## MCP: the standard that won

MCP (Model Context Protocol) is the clearest standards success in the agent field, and its trajectory
is the template. Launched by Anthropic in November 2024 as a client-server protocol for connecting
agents to tools, data resources, and prompts, it was adopted with startling speed:

- **March 2025:** OpenAI adopted MCP in its Agents SDK — a rival adopting a competitor's protocol,
  the strongest possible signal of de-facto-standard status.
- **Through 2025:** Google, Microsoft, AWS, and essentially every serious agent platform adopted it.
- **December 2025:** Anthropic donated MCP to the **Linux Foundation** (under the Agentic AI
  Foundation), with OpenAI and Block as co-founders and AWS, Google, Microsoft, Cloudflare, GitHub,
  and Bloomberg as supporting members — cementing vendor-neutral governance.
- **By mid-2026:** ~18,000+ community-indexed MCP servers, tens of millions of monthly SDK downloads.
- **July–November 2026:** the `2026-07-28` specification made the core stateless. Tier-1 SDKs
  (TypeScript, Python, Go, C#, with Ruby promoted to Tier 1 on Oct 30) report close to half a billion
  downloads a month *(official)*. Third-party censuses count roughly 43,000–47,500 active servers in
  the official registry, which is still in preview *(inferred)*.

**Why MCP won so decisively:** it solved a real, universal pain (every agent needed to connect to
tools, and everyone was building bespoke glue), it was *simple* and *open* from the start (a
well-specified protocol on familiar web foundations), it came from a credible source and was
*given away* rather than controlled, and — crucially — a rival (OpenAI) adopted it early, which
tipped it from "one vendor's protocol" to "the standard." Once OpenAI adopted it, everyone else had
to, and the network effects (more servers → more valuable → more adoption) did the rest. This is the
classic de-facto-standard dynamic (like JSON, like REST) — an open, simple solution to a universal
problem, adopted by rivals, tipping via network effects — playing out in ~14 months instead of years.

The strategic lesson MCP teaches: **the fastest path to a standard is an open, simple, genuinely
useful protocol that a credible player gives away and a rival adopts.** MCP is now settled
infrastructure — the tool-connection question is answered — which is why §04's tool layer is the
least-contested in the stack. The "which tool-connection standard" risk that would normally paralyze
adoption simply doesn't exist anymore.

---

## A2A: following the template, a year behind

A2A (Agent2Agent) is repeating MCP's trajectory one layer up and one year behind. Launched by Google
in April 2025 for agent-to-agent communication (capability discovery via Agent Cards, task
delegation, result exchange), it was donated to the Linux Foundation in June 2025, absorbed IBM's
competing ACP in August 2025, shipped its first stable release (v1.0) in March 2026, and passed 150+
supporting organizations (including AWS, Cisco, IBM, Microsoft, Salesforce, SAP, ServiceNow) by its
first anniversary. On **August 17, 2026 it joined the Agentic AI Foundation** as a hosted project,
completing MCP's governance template *(official)*.

A2A is the *leading* agent-to-agent standard but not yet the *settled* one, for reasons that are
instructive about why the agent-to-agent layer is harder than the tool layer:

- **It's younger.** A year less adoption and entrenchment than MCP.
- **The problem is harder to specify.** Agent-to-agent involves task lifecycle, discovery, and
  *trust* (§13), not just call/response — a bigger, fuzzier surface than tool connection, so
  convergence is naturally slower.
- **Its same-layer rival is gone, but its boundary with MCP is blurring.** IBM's ACP merged into A2A
  (Aug 2025), and AGNTCY now positions itself as complementary *(inferred)*. Meanwhile MCP's
  roadmap moves toward "agentic messaging primitives" (long-running Tasks, server-initiated events).
  The remaining open question is less "A2A vs. ACP" than where MCP-with-Tasks ends and A2A begins
  *(inferred)*.

Still, A2A has the strongest position: Google's backing, AAIF governance alongside MCP, broad adoption,
and the same "open, given away, rivals adopting" dynamic that made MCP win. The timeline chart shows
both trajectories:

![Agent-standards timeline](../assets/charts/15_standards_timeline.png)

The pattern is unmistakable — **both MCP and A2A launched, gained rival adoption, and moved to neutral
Linux Foundation governance within ~1 year**, with A2A trailing MCP by roughly that year. If A2A
completes the template (which its trajectory suggests), the agent-to-agent layer settles on A2A over
2026–2027, much as the tool layer settled on MCP. *Nov 2026: the governance half of the template is
complete (both in AAIF); what remains is adoption depth, which is still far behind MCP.*

---

## The genuinely open contests

The July snapshot named two contests as genuinely unsettled. One of them, A2A vs. ACP, had in fact
already resolved, and the record is corrected below. The other, payments, remains open.

### A2A vs. ACP for the agent-to-agent layer (resolved: merged)

Introduced in §06. The July snapshot mixed up two different projects under the "ACP" label.
**ACP (Agent Communication Protocol)** was IBM Research's REST/HTTP-verb agent messaging protocol
(from the BeeAI project). It was the genuine same-layer rival to A2A, and in **August 2025 it merged
into A2A** under the Linux Foundation *(official)*. **AGNTCY** is the separate Cisco-led collective
(formative members Cisco, Dell, Google Cloud, Oracle, Red Hat; LangChain and LlamaIndex were early
supporters). It joined the Linux Foundation in July 2025 with its own Agent Connect Protocol, the OASF
agent schema and the SLIM messaging transport. AGNTCY remains a separate LF project outside the AAIF.
It increasingly presents OASF and SLIM as complements to A2A (OASF maps to and from Agent Cards; SLIM
as a transport beneath A2A) rather than as a rival *(inferred)*. The corrected comparison:

| Dimension | A2A | ACP (IBM) | AGNTCY (Cisco-led) |
|---|---|---|---|
| Origin | Google | IBM Research (BeeAI) | AGNTCY collective |
| Governance | LF → **AAIF** (Aug 2026) | LF; **merged into A2A** (Aug 2025) | Linux Foundation (separate project) |
| Approach | Task/Agent-Card model; v1.0 (Mar 2026) | REST/HTTP-verb messaging | OASF schema, SLIM transport, Agent Connect Protocol |
| Backers | Google, AWS, Cisco, IBM, Microsoft, Salesforce, SAP, ServiceNow; 150+ | IBM | Cisco, Dell, Google Cloud, Oracle, Red Hat |
| Adoption | Leading | Archived; migration guide to A2A | Smaller; infrastructure niche |
| Relationship to A2A | — | Absorbed | Complementary (discovery/transport) |

The snapshot's predicted outcome order was (1) A2A becomes dominant with ACP concepts folded in;
(2) formal convergence under LF stewardship; (3) stable coexistence with bridges. What actually
happened was a mix of **(1) and (2)**. ACP's team folded its work into A2A, and the shared Linux
Foundation governance did reconcile rather than fight. That is the field learning from past
standards wars, as predicted, only a year earlier than the snapshot realized.

### The payments land-grab

The most contested new sub-layer, introduced in §13: AP2 (Google), Agentic Commerce Protocol
(OpenAI+Stripe), x402 (Coinbase), and the card networks' schemes (Visa, Mastercard) all racing to be
how agents pay. This is genuinely wide open — multiple credible proposals from different power centers
(platforms, card networks, crypto), no clear winner, and high stakes (agentic commerce). It is the
*least* settled part of the stack and the most likely to take years to resolve, probably toward the
card networks' rails plus one or two platform/crypto options coexisting.

*Nov 2026 update:* the payments protocols have repeated the neutral-governance move, though the
commercial contest continues. In April 2026 Google donated **AP2 to the FIDO Alliance**, together
with Mastercard's Verifiable Intent framework, and FIDO formed agentic-authentication and payments
working groups *(official)*. Also in April 2026, **x402 moved to a new x402 Foundation under the Linux
Foundation**, co-developed by Coinbase, Cloudflare and Stripe with roughly 40 launch members including
Google, Visa and Mastercard *(official)*. Usage signals are mixed. Analysts report x402 monthly
transactions well below their late-2025 peak, and the counts do not show how many payments agents
actually initiated *(inferred)*. The Agentic Commerce Protocol spec continues on GitHub, while OpenAI
reportedly scaled back its Instant Checkout surface in 2026 *(inferred; secondary reports conflict on
dates)*. The card networks now sit *inside* the neutral bodies (FIDO's payments group; x402
Foundation membership). That supports the snapshot's call that card rails anchor the outcome.

The standards-comparison chart positions all the standards on adoption vs. governance maturity, sized
by consolidation likelihood:

![Agent standards: adoption vs. governance maturity](../assets/charts/15_standards_comparison.png)

MCP sits alone in the upper-right (high adoption, mature governance, near-certain to remain the
standard); A2A follows, now closer after joining the AAIF; the AAIF's Agent Skills + AGENTS.md pair
appears as a new mid-adoption entrant for agent instructions/packaging; and the contested standards
(AGNTCY, ANP, the payment protocols) cluster to the left (emerging adoption, uncertain consolidation;
AP2 and x402 gained governance scores with their neutral homes). The visual tells the whole story:
**one settled standard (MCP), one consolidating front-runner (A2A), and a contested frontier
(discovery, identity, payments).**

---

## Why the fast consolidation? The forces at work

The agent-standards consolidation is unusually fast, and understanding *why* both explains the present
and predicts the future:

- **The pain was universal and acute.** Every agent builder faced the same integration problems
  (connecting tools, connecting agents) simultaneously, creating enormous, aligned demand for a
  standard — the precondition for fast convergence.
- **The players learned from history.** The industry has lived through standards wars (browser wars,
  messaging protocols, container formats) and *knows* fragmentation hurts everyone — so there's a
  collective incentive to converge rather than fight, visible in the rush to neutral Linux Foundation
  governance.
- **Open-and-given-away beat proprietary-and-controlled.** The standards that won (MCP) were open and
  donated, not controlled — because in a multi-vendor world, no vendor could impose a proprietary
  standard, and an open one adopted by rivals wins. The vendors chose neutral governance because it
  was the only way to get universal adoption.
- **Network effects tip fast.** Once a standard reaches critical mass (MCP after OpenAI adopted it),
  the network effects (more servers/agents → more value → more adoption) tip it rapidly to dominance —
  the winner-take-most dynamic of protocol standards.
- **The web foundations were reusable.** Building on OAuth, HTTP, and JSON-RPC rather than inventing
  from scratch dramatically lowered the adoption cost — you're extending the familiar web, not
  learning a new paradigm.

The synthesis: **aligned universal demand + historical lesson-learning + open-given-away protocols +
network effects + reusable foundations = unusually fast consolidation.** This is why the agent-
standards story, despite being the "most contested" dimension, is actually one of the *more settled*
in practice for the layers that matter most (tools, and increasingly agent-to-agent).

---

## Historical standards fights as a guide

The best way to predict where this goes is to look at analogous historical standards fights, because
the patterns rhyme. Several precedents illuminate different possible outcomes:

- **JSON vs. XML (de-facto winner via simplicity).** JSON beat XML for data interchange not through
  a committee but by being *simpler* and *good enough*, adopted organically until it was the default.
  MCP looks like JSON — an open, simple, good-enough solution winning by organic adoption. *Lesson:
  simplicity and openness beat committee complexity; the agent standards that win will be the simple,
  open ones.*
- **REST vs. SOAP (simplicity beats enterprise heft).** REST beat the heavier, enterprise-backed SOAP
  for web APIs by being simpler and more developer-friendly. The A2A-vs-ACP contest had echoes. It
  ended in a merger into the more-adopted option (Aug 2025) rather than a protracted fight, which is a
  faster resolution than REST vs. SOAP got. *Lesson: developer experience and adoption momentum win
  agent-to-agent too, and shared governance can shortcut the fight.*
- **TCP/IP and the web (open standards beat proprietary networks).** The open internet protocols beat
  proprietary networks (AOL, CompuServe) because open won. The agent standards' openness (vs. any
  vendor's proprietary agent protocol) is the same dynamic. *Lesson: the open agent-interop stack
  beats any vendor's walled garden.*
- **The browser wars (fragmentation is painful, standards bodies help).** The browser wars' pain led
  to standards bodies (W3C) governing convergence — mirroring the Linux Foundation's role for agent
  standards. *Lesson: neutral governance is how fragmentation gets resolved, which is exactly what's
  happening.*
- **USB / connector standards (consolidation after fragmentation).** Physical connectors went through
  fragmentation before consolidating on USB (and USB-C). The payments land-grab may follow this — a
  period of competing standards before consolidation. *Lesson: the contested layers (payments) will
  likely fragment then consolidate, taking longer than the tool layer did.*

The composite prediction from history: **the tool layer (MCP) has already had its JSON moment and
settled; the agent-to-agent layer (A2A) is having its REST-vs-SOAP moment and will likely settle on
the simpler, more-adopted option under neutral governance; and the payments layer will have its
USB-style fragment-then-consolidate period, taking longest.** The consistent throughline is that
*open, simple, neutrally-governed standards win*, which is the direction all the agent standards are
heading.

---

## The competitive/standards table

### Comparison table — agent interoperability standards

| Standard | Layer | Status | Governance | Backers (confidence) | Likely outcome | Historical analogue |
|---|---|---|---|---|---|---|
| **MCP** | Tool/context | **Won** | LF Agentic AI Foundation | Anthropic, OpenAI, Google, MS, AWS; spec `2026-07-28` (official) | Settled standard | JSON |
| **A2A** | Agent-to-agent | Leading → consolidating | LF Agentic AI Foundation (since Aug 2026) | Google, AWS, Cisco, IBM, MS, Salesforce, SAP, ServiceNow, 150+ (official) | Likely settles; v1.0 shipped | REST |
| **ACP (IBM)** | Agent-to-agent | **Merged into A2A (Aug 2025)** | Linux Foundation | IBM (official) | Folded into A2A; repo archived | SOAP-ish |
| **ANP** | Decentralized discovery | Emerging | Community | Open community (inferred) | Niche (decentralized vision) | — |
| **AGNTCY (OASF / SLIM / Agent Connect)** | Discovery/identity/transport | Emerging | Linux Foundation (outside AAIF) | Cisco, Dell, Google Cloud, Oracle, Red Hat (official) | Complements A2A Cards; transport niche (inferred) | — |
| **AP2** | Payments | Proposed (v0.2) | FIDO Alliance (since Apr 2026) | Google, Mastercard, payment networks (official) | Contested; partial adoption | — |
| **Agentic Commerce Protocol** | Commerce | Proposed | OpenAI+Stripe | OpenAI, Stripe (official) | Contested; checkout niche; ChatGPT checkout scaled back (inferred) | — |
| **x402** | Micropayments | Proposed | x402 Foundation (LF, since Apr 2026) | Coinbase, Cloudflare, Stripe, Google, Visa, Mastercard (official) | Crypto/agent-to-agent niche | — |
| **Visa/Mastercard schemes** | Payments | Proposed | Card networks | Visa, Mastercard (official) | Likely win card-rail payments | — |
| **OAuth 2.1 / OIDC** | Auth foundation | Adopted | IETF | Universal (official) | Settled foundation | HTTP auth |
| **AGUI / agent-UI protocols** | Agent-UI | Emerging | Community | Various (inferred) | Early; MCP Apps extension overlaps | — |
| **Agent Skills + AGENTS.md** | Agent instructions/packaging | Emerging → adopted | LF Agentic AI Foundation | Anthropic, OpenAI, coding-agent vendors (official) | Partial answer to agent-definition gap | — |
| **Open Responses** | Model API | Emerging | LF Agentic AI Foundation (Oct 2026) | OpenAI (official) | Portable model-call interface | — |
| **WebMCP** | Agent-to-web page | Draft (Chrome origin trial) | W3C Web ML Community Group | Google, Microsoft editors (inferred) | Early; browser-side tool exposure | — |
| **IETF agentproto / DAWN** | Agent comms / discovery | BoF stage (Jul 2026) | IETF | Multi-vendor (inferred) | Uncertain; may formalize A2A/MCP-adjacent pieces | — |

That is fifteen distinct standards/proposals spanning the stack's layers — well past ten — at very
different maturity stages (one, IBM's ACP, now merged away). The through-line: **the foundational and
tool layers are settled (OAuth, MCP), the agent-to-agent layer is consolidating (A2A, now beside MCP
in the AAIF, having absorbed ACP), and the discovery/identity/payments layers are contested
frontiers** — exactly the "settled below, contested above" pattern that characterizes a maturing but
incomplete standards stack.

---

## MCP mechanics: what the winning standard actually specifies

Understanding *what MCP actually is* clarifies why it won and what a good agent standard looks like.
MCP is a client-server protocol (built on JSON-RPC, with transports including stdio for local and
Streamable HTTP for remote; the legacy HTTP+SSE transport was deprecated in the `2026-07-28` spec)
where **servers expose capabilities and clients (agents) consume them.** It
defines three core primitives:

- **Tools** — functions the agent can call (the function-calling of §04), exposed with JSON Schema
  definitions. This is the most-used primitive and the reason MCP is "the tool-connection standard."
- **Resources** — data the agent can read (files, database records, documents) — a standardized way to
  give the agent access to context/data (connecting to retrieval §07).
- **Prompts** — reusable prompt templates the server can offer, letting servers provide
  tested interaction patterns.

The design virtues that made it win are visible in this simplicity: **it's a small, well-specified
protocol on familiar foundations (JSON-RPC, HTTP) that solves a universal problem (connect agents to
tools/data) without imposing opinions about the agent's internals.** A server author exposes their
tool once, and *any* MCP client works with it; an agent builder speaks MCP once, and *any* MCP server
works. That clean separation — servers don't know about clients, clients don't know about servers'
internals — is what enables the ecosystem (18,000+ servers by mid-2026, and roughly 43,000–47,500
registry entries by October 2026 per third-party counts, usable by any agent). It's the same
architectural virtue (opacity across a clean interface) that makes A2A work for agents, and the same
that made the web's protocols win.

The 2026 evolution of MCP worth noting: the protocol added **remote server support** with proper
**OAuth 2.1 authentication** (§13), **streaming** (HTTP/SSE), and **elicitation** (servers requesting
input) — maturing from a local-first developer protocol into production-grade remote infrastructure.
The addition of required OAuth for remote servers is what ties MCP to the identity layer (§13) and
made it enterprise-deployable. This maturation — from a clever local protocol to governed,
authenticated, remote-capable production infrastructure — is part of why it consolidated: it grew up
fast enough to be trusted for real deployments.

**The `2026-07-28` revision (July 28, 2026) is the biggest step in that maturation** *(official)*.
The core became **stateless**. The `initialize` handshake and the `Mcp-Session-Id` header are gone,
and each request carries its protocol version, client identity and capabilities in `_meta`, with an
optional `server/discover` call. As a result, remote servers can sit behind ordinary load balancers
without sticky sessions. Server-initiated requests (elicitation, sampling, roots) that needed
held-open streams are replaced by **Multi Round-Trip Requests**: the server answers
"input required" and the client retries with the inputs. Streamable HTTP requests carry `Mcp-Method`
and `Mcp-Name` headers for gateway routing. List results are cacheable (`ttlMs`). Authorization was
hardened: issuer validation per RFC 9207, credentials bound to their issuer, and Client ID Metadata
Documents preferred, with Dynamic Client Registration deprecated. A **formal extensions framework**
now houses Tasks (long-running work), MCP Apps (interactive UI) and Enterprise-Managed Authorization.
Roots, Sampling and Logging are deprecated under a new twelve-month deprecation policy. Two points
matter strategically. First, MCP is now designed for **cloud-scale, gateway-fronted deployment**.
Second, it is growing **agentic primitives** (Tasks, and server-initiated events on the August 2026
roadmap) that edge toward A2A's territory, so the MCP/A2A boundary is worth watching *(inferred)*.

## The embrace-extend risk and conformance

A real risk to any standard, learned from decades of standards history, is **embrace-extend-
extinguish** — a vendor adopting a standard nominally but adding proprietary extensions that
fragment it, or implementing it incompatibly so "MCP support" means different things across vendors.
This is the "standard-in-name-only" failure, and it's a genuine risk as adoption broadens:

- **The risk.** As more vendors implement MCP/A2A, incompatible implementations or proprietary
  extensions could fragment the nominal standard — everyone claims support, but interoperability
  breaks in practice. This has killed the value of nominal standards before.
- **The mitigations.** Neutral governance (Linux Foundation) that maintains a canonical spec,
  **conformance testing** (verifying implementations actually interoperate), and a strong reference
  implementation reduce this risk. The Linux Foundation's stewardship is partly *about* preventing
  embrace-extend by keeping the spec canonical and multi-vendor. *Nov 2026:* MCP now runs a formal
  SDK tiering system scored against conformance tests. For example, the Ruby SDK reached Tier 1 on
  Oct 30, 2026 with 100% conformance on both scored spec versions *(official)*. MCP also has a formal
  extensions framework, which gives vendors a sanctioned place for additions instead of forks.
- **The countervailing force.** The whole *point* of adopting the standard is interoperability, so
  vendors have an incentive *not* to fragment it (fragmenting defeats the purpose they adopted it
  for). The network effects that make the standard valuable also punish fragmenting it.

The assessment: **embrace-extend is a real but manageable risk, held in check by neutral governance,
conformance efforts, and the vendors' own interest in interoperability.** The fact that the standards
moved to genuine multi-vendor Linux Foundation governance (rather than staying under one vendor's
control) is the strongest structural defense — a standard genuinely governed by many can't easily be
captured or fragmented by one. This is a key reason the neutral-governance step matters so much: it's
not just optics, it's the mechanism that protects the standard's integrity as it scales.

## Standards for the other layers

Beyond the tool/agent-to-agent/payments stack, other layers have their own standardization stories
worth mapping, because "agent standards" is broader than MCP/A2A:

- **Observability: OpenTelemetry** (§11). The tracing/observability layer is standardizing on
  OpenTelemetry (with GenAI semantic conventions / OpenLLMetry) — the vendor-neutral tracing standard,
  playing the same lock-in-reducing role for observability that MCP plays for tools. This is a
  significant, under-discussed standardization that lets teams instrument once and switch backends.
- **Agent definition: the open gap** (§02). There is *no* standard for the agent's *internal*
  definition — the graph, prompts, state schema — so agents aren't portable across frameworks. This is
  the real remaining lock-in gap, and whether a declarative agent-definition standard emerges (given
  the MCP/A2A precedent and enterprise demand) is an open 2027 question. A2A's Agent Cards standardize
  the agent's *interface* but not its *implementation*. *Nov 2026:* the gap has narrowed at the edges.
  The AAIF now hosts **AGENTS.md** (repo-level agent instructions) and, since October 22, 2026,
  **Agent Skills** (Anthropic's packaging format for reusable instructions and resources) and **Open
  Responses** (OpenAI's interoperable model-API spec) *(official)*. Together these make an agent's
  *instructions, skills and model calls* portable. The orchestration graph and state schema are still
  not portable.
- **Memory: no standard** (§03). Memory has no portability standard — you can't export/import an
  agent's memory across systems — and the vendors have an incentive against it. An open gap, unlikely
  to be filled soon. (*Nov 2026:* a W3C AI Agent Memory Interoperability Community Group formed in
  June 2026. Community groups do not produce W3C Recommendations, so this is an early signal and not a
  standard *(inferred)*.)
- **Evaluation: emerging conventions** (§11). Eval is standardizing informally around common
  benchmarks and LLM-judge practices, and OpenTelemetry for the observability half, but there's no
  formal eval standard.
- **Agent-UI: emerging** (AG-UI and similar). Protocols for how agents present interfaces to users are
  early. MCP's **MCP Apps** extension (interactive UI from MCP servers) brings part of this layer under
  the MCP umbrella *(official)*.
- **Agent-to-web: emerging (WebMCP).** WebMCP lets web pages expose tools to in-browser agents. As of
  October 2026 it is a Draft Community Group Report in the W3C Web Machine Learning CG, with a Chrome
  origin trial; other browsers have not committed *(inferred)*.
- **Agent environments and sandboxes: newly under governance.** OpenEnv (Hugging Face; training and
  evaluation environments) and OpenSandbox (Alibaba; managed execution environments) joined the AAIF
  on Oct 22, 2026 *(official)*. It is too early to call either a standard.

The pattern across layers: **the layers with clean interfaces and universal pain standardized (tools/
MCP, observability/OTel, agent-to-agent/A2A), while the layers with fuzzy interfaces or vendor
lock-in incentives (agent definition, memory) haven't.** Standardization follows the same
tractability logic as everything else — clean interface + universal pain + no strong lock-in incentive
= standardizes; fuzzy interface or lock-in incentive = doesn't. This predicts which layers will
standardize next (those developing clean interfaces and shared pain) and which won't (those where
vendors profit from lock-in).

## The vendor-power and geopolitical dimension

Standards are never purely technical — they're contests over *power and control* — and the agent-
standards story has a power dimension worth surfacing:

- **Whoever controls the standard shapes the ecosystem.** A vendor whose protocol becomes the
  standard gains influence over the whole ecosystem's direction. This is why vendors both *want* their
  protocol to win *and* accept neutral governance (controlling a captured standard is worth less than
  a widely-adopted neutral one they helped shape).
- **The neutral-governance bargain.** Vendors donated their protocols (MCP from Anthropic, A2A from
  Google) to neutral governance because a proprietary standard couldn't achieve universal adoption in
  a multi-vendor world — better to shape a neutral standard everyone adopts than to own a proprietary
  one no rival will touch. This is a rational-power calculation, not altruism, and it's why the
  consolidation happened.
- **The geopolitical layer.** As with all critical infrastructure standards, there's a geopolitical
  dimension — different regions/blocs may favor different standards or governance, and agent
  infrastructure (like other critical tech) could see some regional fragmentation. The Linux
  Foundation's international-neutral positioning helps, but the geopolitics of AI broadly could
  eventually touch agent standards. This is more latent than active in 2026 but worth watching as
  agents become critical infrastructure. *Nov 2026:* the signals so far point toward participation
  rather than fragmentation. Alibaba joined the AAIF as a Gold member in August 2026 and contributed
  OpenSandbox in October, and Ant Group joined at Gold in the October cohort *(official)*. Meanwhile
  the US government's channel is NIST's AI Agent Standards Initiative, which works *with*
  industry-led protocols rather than competing with them *(official)*.
- **The open-source-vs-proprietary throughline.** The agent standards' openness is part of the
  broader open/closed dynamic in AI — open standards, like open models (§05), distribute power and
  resist single-vendor control, which is why they're favored by everyone except a would-be
  monopolist. No single vendor is dominant enough to impose a proprietary agent standard, so open won
  by necessity.

The power reading: **the fast consolidation on open, neutrally-governed standards reflects that no
single vendor could dominate the agent ecosystem, so all rationally chose open standards over
proprietary control they couldn't enforce.** It's a multi-vendor equilibrium that happens to produce
a good outcome (open interoperability) — driven by competitive dynamics, not benevolence. Whether that
equilibrium holds depends on no single player becoming dominant enough to defect toward proprietary
control, which the current competitive balance makes unlikely.

## What could derail the consolidation

For balance, the scenarios that could *derail* the optimistic consolidation story:

- **A dominant player defects.** If one vendor became dominant enough to impose a proprietary standard
  and abandon the neutral one, consolidation could fracture. Currently unlikely (no vendor is that
  dominant), but not impossible if the competitive balance shifts.
- **A contested layer fragments permanently.** If A2A/ACP *don't* converge, or payments fragment
  durably, those layers stay fractured — real friction, though bounded to those layers (the tool layer
  is safe). (*Nov 2026:* A2A/ACP did converge; payments remain the live risk.)
- **MCP and A2A overlap.** As MCP adds Tasks and server-initiated events, the boundary between "agent
  calls a tool" and "agent delegates to an agent" could blur into duplicated functionality. Shared
  AAIF governance makes reconciliation more likely than a fight *(speculative)*.
- **Security failures discredit a standard.** If MCP tool poisoning or agent kill chains (§12) cause
  major incidents that the standard can't address, trust could erode — mitigated by security hardening,
  but a real risk given §12's unsolved problems.
- **The technology shifts underneath.** If the agent paradigm shifts fundamentally (e.g., CodeAct §04
  making tool-by-tool connection less central), the standards built for today's paradigm could
  partially obsolete — standards always risk being overtaken by paradigm shifts.
- **Governance dysfunction.** If the neutral governance becomes slow or captured, the standards could
  stagnate or fragment — mitigated by the Linux Foundation's track record but always a risk for
  committee-governed standards.

The balanced assessment: **the consolidation is real and fast but not guaranteed** — it rests on a
competitive equilibrium, neutral governance, and continued alignment that could, in principle, break.
The base case is strongly toward continued consolidation (the forces driving it are powerful and
aligned), but the risks are real enough that "the standards are settled forever" would be
overconfident. The most likely disruption is not the tool layer (MCP is safe) but the contested layers
(agent-to-agent if convergence fails, payments) staying fractured longer than hoped.

## Standards and the other layers

- **↔ Tool use (§04).** MCP *is* the tool-connection standard; §04's low contestedness is MCP's win.
- **↔ Multi-agent (§06).** A2A (which absorbed IBM's ACP) is the agent-to-agent standard; §06's coordination happens over
  them.
- **↔ Identity (§13).** OAuth foundations, agent identity, and the payments standards live at the
  §13/§15 boundary.
- **↔ Enterprise platforms (§14).** Enterprises demand standards support as a lock-in hedge, making
  them a key demand-side driver of consolidation.
- **↔ Orchestration (§02).** Standardizing tools (MCP) and agent-boundaries (A2A) reduces framework
  lock-in — the portability §02 recommends.

---

## Failure modes and risks specific to standards

1. **Fragmentation of a contested layer.** Payments fragmenting hurts everyone (the agent-to-agent
   version of this risk receded when ACP merged into A2A). Mitigated by neutral governance pushing
   convergence: AP2 at FIDO and x402 at the Linux Foundation since April 2026.
2. **Premature lock-in to a losing standard.** Betting on a standard that doesn't win. Mitigated by
   backing the neutrally-governed front-runners (MCP, A2A).
3. **Standard-in-name-only.** A "standard" that vendors implement incompatibly (embrace-extend).
   Mitigated by conformance testing and neutral governance.
4. **Governance capture.** A vendor capturing a nominally-neutral standard. Mitigated by genuine
   multi-vendor Linux Foundation governance.
5. **Security gaps in standards.** Standards that don't adequately address security (MCP tool
   poisoning, §12) create ecosystem-wide risk. Mitigated by security-hardening the standards.
6. **The internal-agent-definition gap.** No standard for the agent's internal definition (§02) —
   real lock-in remains there. An open gap.

---

## Practical guidance: which standards to adopt now

Cutting through the analysis, the practical question for a team building agents is *which standards to
adopt today*, and the answer is clear enough to state directly:

- **Adopt MCP for tools/data connection — unambiguously.** MCP has won; standardizing your tools on
  MCP makes them portable across frameworks and models (§02) and connects you to an ecosystem of
  tens of thousands of servers. There is no reason not to, and it's the single highest-value standards
  decision. This is settled infrastructure — build on it. *Nov 2026:* target the `2026-07-28`
  revision for new remote servers. Plan migrations off the deprecated HTTP+SSE transport, Dynamic
  Client Registration, and Roots/Sampling/Logging within their twelve-month windows.
- **Adopt A2A for agent-to-agent boundaries — with mild caution.** A2A is the front-runner for
  agent-to-agent, and adopting it for cross-agent/cross-org boundaries is the right bet. The caution
  now concerns the layer's edges (MCP Tasks overlap, identity), not a rival protocol, since ACP merged
  into A2A. The risk of betting on A2A is low (v1.0 stable, AAIF-governed, broadly adopted). Note that
  v1.0 broke compatibility with v0.3, so pin and test versions. The alternative (no standard) is worse.
- **Adopt OpenTelemetry for observability — unambiguously.** Standardize tracing on OTel (§11) so
  your observability survives a backend switch — the same portability logic as MCP, applied to
  observability. Settled direction, adopt it.
- **Use OAuth 2.1 for auth — it's the foundation.** The identity layer (§13) builds on OAuth 2.1;
  use it (MCP requires it for remote servers anyway).
- **Wait on payments standards.** The payments layer is unsettled; unless you specifically need
  agentic payments now, waiting for consolidation avoids betting on a loser. If you must, the card-
  network schemes (Visa/Mastercard) are the safest bet for card-rail payments given incumbent trust.
  Track the FIDO Alliance payments working group (AP2 + Verifiable Intent), which now brings Google,
  Mastercard and Visa into one venue.
- **Accept lock-in on the agent definition — for now.** No standard exists for the internal agent
  definition (§02), so framework choice remains sticky; mitigate by keeping tools (MCP), agent-
  boundaries (A2A), and tracing (OTel) portable so the *framework* is the only lock-in. Where it
  fits, also put instructions in AGENTS.md and reusable capabilities in Agent Skills (both AAIF-hosted
  as of Nov 2026), so the portable share of the agent definition keeps growing.

The one-line practical takeaway: **standardize on MCP (tools), A2A (agent-to-agent), OTel
(observability), and OAuth 2.1 (auth) today — these are settled-enough to build on — and accept that
the agent definition and payments remain non-portable for now.** This is the concrete portability
strategy that recurs through §02, §11, §14, and here — and it's the actionable core of the whole
standards story: build on the settled standards, hedge the unsettled ones, and keep the sticky
framework decision isolated behind portable interfaces.

## The "internet of agents" standards vision

The most expansive vision the standards enable is the **"internet of agents"** — an open ecosystem
where agents anywhere discover, communicate, transact, and collaborate as freely as web servers serve
any client. §06 flagged this as compelling-but-aspirational; here it's worth mapping which standards
would need to mature to realize it, because it clarifies what's built and what's missing:

- **Communication (mostly there).** A2A (with AGNTCY's SLIM as an optional transport) provides agent-to-agent communication — the plumbing for
  agents to talk. This layer is maturing well.
- **Discovery (emerging).** Agent Cards (A2A), OASF, and ANP provide capability discovery — how agents
  find each other. Emerging, especially for the enterprise/federated case; the open decentralized case
  (ANP) is earlier. *Nov 2026:* MCP's Server Card working group (`.well-known` server metadata) and
  the IETF DAWN discovery BoF are pulling discovery toward web-native conventions *(official /
  inferred)*.
- **Identity and trust (the gap).** Verifiable agent identity and trust across organizations (§13) is
  the hard, largely-missing piece — the plumbing exists but the trust infrastructure (verifiable
  credentials, reputation) doesn't. This is the gating gap, as §06 and §13 both emphasize. *Nov
  2026:* it is now the explicit priority of every major venue. Examples are MCP's agent-identity
  roadmap item (DPoP, workload identity federation, coordination with IETF WIMSE), NIST CAISI's
  identity-and-authorization work, FIDO's agentic-authentication working group, and W3C community
  groups on agent identity. There is plenty of activity but no finished standard yet.
- **Payments (contested/early).** Agent-to-agent payments (x402, AP2) provide the economic substrate —
  contested and early, but developing.
- **Governance and safety (missing).** Frameworks for governing, securing (§12), and holding
  accountable an open agent network are largely absent — and given §12's unsolved security, an open
  agent network is a serious risk surface.

The assessment matches §06: **the communication and discovery standards for an internet of agents are
maturing, but the trust, identity, payments, and governance/safety substrate is not — so the open
internet of agents remains aspirational, gated on exactly the least-mature layers (identity §13,
security §12).** The standards are laying the groundwork (the "TCP/IP of agents" is being built), but
the full vision needs the trust and safety layers that don't yet exist. The near-term reality is
*federated* agent interoperability within trust boundaries (using the standards as plumbing, human-
negotiated trust as the foundation), with the open permissionless version as a longer-term direction
that the standards enable but don't by themselves deliver. Standards are necessary but not sufficient
for the internet of agents — the trust infrastructure is the harder, missing half.

## A brief history of agent standards

The compressed history explains the remarkable speed. **Before late 2024**, there were no agent
standards — every agent builder wired tools and integrations bespoke, and the pain of that
fragmentation grew as agents proliferated. **November 2024** was the watershed: Anthropic launched MCP,
proposing an open standard for the universal tool-connection problem. It could have been ignored (one
vendor's protocol), but the pain it solved was real and universal.

**Early-to-mid 2025** was the tipping: OpenAI adopted MCP (March) — a rival adopting a competitor's
protocol, the signal that tipped MCP from proposal to de-facto standard — and Google, Microsoft, and
AWS followed. Simultaneously, Google launched A2A (April) for the agent-to-agent layer, and both MCP
and A2A began moving toward neutral governance (A2A to the Linux Foundation in June; the Cisco-led
AGNTCY stack to the LF in July; IBM's rival ACP merged into A2A in August). The industry,
recognizing that fragmentation would hurt everyone, rushed toward open, neutrally-governed standards.
**Late 2025** cemented it: MCP donated to the Linux Foundation's new Agentic AI Foundation (December)
with OpenAI, Google, Microsoft, and AWS backing — a near-complete industry consensus on the tool
layer — while the payments contest (AP2, Agentic Commerce Protocol, x402) opened as agentic commerce
loomed.

**2026** is the current state. MCP is settled: tens of thousands of servers, universal backing, and a
stateless `2026-07-28` core. A2A shipped v1.0 (March) and joined MCP in the Agentic AI Foundation
(August). The AAIF grew to ten projects and 300+ members by October. Payments moved to neutral homes
(FIDO for AP2, a Linux Foundation foundation for x402) but stayed commercially contested. Government
and formal bodies entered, with NIST's initiative (February) and IETF BoFs (July). The overall
open, neutrally governed, layered-stack pattern is firmly established. The arc
is one of the fastest and most cooperative standards consolidations in computing history — driven by
aligned universal demand and the industry's hard-won knowledge that standards wars hurt everyone. It's
a rare case where the "most contested" dimension produced, in practice, unusually fast agreement on
the layers that matter most — because everyone needed it and everyone knew fighting would be worse than
converging. The standards story is, against expectation, one of the more *optimistic* in this
document: the connective tissue is coming together faster than the capability and trust layers it
connects.

## Roadmap and outlook (confidence-tagged)

- **MCP remains the settled tool standard** *(official; very high confidence).* The tool-connection
  question is answered; MCP is infrastructure. — *Nov 2026: confirmed; the `2026-07-28` stateless
  revision and ~half-billion monthly Tier-1 SDK downloads deepen the lock-in.*
- **A2A settles the agent-to-agent layer, likely absorbing/coexisting with ACP** *(inferred; high
  confidence).* A2A completes MCP's template over 2026–2027; convergence with ACP under LF governance
  is more likely than a war. — *Nov 2026: largely confirmed. IBM's ACP had already merged into A2A
  (Aug 2025), and A2A joined MCP in the AAIF (Aug 2026). Adoption depth still lags MCP.*
- **Payments fragment then consolidate slowly** *(speculative; medium confidence).* The
  AP2/ACP/x402/card-network contest resolves over multiple years toward card rails + a platform/crypto
  option or two — a USB-style fragment-then-consolidate. — *Nov 2026: partly. Governance has
  consolidated (AP2 at FIDO, x402 Foundation at the LF), but the commercial contest has not resolved.*
- **An agent-definition portability standard may emerge** *(speculative; low-medium confidence).* The
  §02 internal-agent-definition gap (real lock-in) may attract a standard by 2027, given the MCP/A2A
  precedent and enterprise lock-in demand — but nothing has clearly won. — *Nov 2026: partly. AGENTS.md
  and Agent Skills (AAIF) standardize instructions and skills; graph and state portability is not yet
  addressed.*
- **Security hardening of the standards becomes a priority** *(inferred; medium-high confidence).* As
  MCP tool poisoning and agent kill chains (§12) become concrete, hardening the standards against them
  is a growing focus. — *Nov 2026: confirmed. MCP's authorization hardening shipped in `2026-07-28`, and
  agent identity is a named roadmap priority; the October AAIF conference reportedly centered on
  security and identity.*
- **The open agent-interop stack solidifies** *(inferred; high confidence).* The overall direction —
  an open, neutrally-governed, layered standards stack extending the web — is set; it's the connective
  tissue that lets the multi-vendor agent ecosystem cohere rather than fragment. — *Nov 2026:
  confirmed; the AAIF hosts 10 projects with 300+ members.*
- **New (Nov 2026): the MCP/A2A boundary becomes the next interop design question** *(speculative;
  medium confidence).* MCP Tasks and server-initiated events overlap A2A's long-running-task model.
  Expect AAIF-level guidance or bridging work in 2027 rather than a fight.
- **New (Nov 2026): formal-body standards for agent identity and discovery** *(inferred; medium
  confidence).* IETF (`agentproto`/DAWN, WIMSE), NIST CAISI and FIDO are all working on agent
  identity and discovery. The first normative outputs plausibly arrive in 2027 and are more likely to
  *profile* MCP/A2A than to replace them.

---

## The deeper lesson: standards as coordination technology

Stepping back, the agent-standards story illustrates something important about how the whole field
progresses. Standards are **coordination technology** — they let independent parties build on shared
foundations without central control — and their maturation follows a different logic than capability
(§05) or product (§09) maturation. Capability improves when a lab trains a better model; a standard
matures only when an *ecosystem agrees*, which requires aligned incentives, credible neutral
governance, and enough shared pain to overcome each party's temptation to control the standard itself.

This is why the standards story is simultaneously the "most contested" dimension and one of the
fastest-consolidating in practice: contested because standards are inherently power contests, fast-
consolidating because the coordination incentives happened to align strongly (universal pain,
multi-vendor balance where no one could dominate, historical lesson-learning). When those conditions
hold — universal aligned demand, no dominant player, credible neutral governance — standards consolidate
fast (MCP). When they don't — fuzzy interface, vendor lock-in incentive, or genuine multi-power contest
— they lag (agent definition, memory, payments). The tractability logic that governs every layer
governs standards too: **standards consolidate where coordination is easy (clean interface, aligned
incentives, no dominant defector) and lag where it's hard.**

The implication for reading the rest of the field: **watch the coordination conditions to predict
which standards emerge next.** A layer developing a clean interface with universal pain and no strong
lock-in incentive (the way the tool layer did) will standardize; a layer with a fuzzy interface or
where vendors profit from lock-in (memory, agent definition) will resist standardization until those
conditions change. The standards stack will keep filling in from the layers where coordination is
easiest toward the layers where it's hardest — which predicts observability (OTel, easy) and agent-to-
agent (A2A, moderately easy) settling before agent-definition and memory (hard, lock-in-favoring).

## Standards and the shape of the ecosystem

Finally, standards *shape the competitive structure* of the entire agent ecosystem, which is why they
matter beyond their technical role. The open, layered, neutrally-governed standards stack has profound
structural consequences:

- **It commoditizes the connection layer**, so value migrates up (to agent logic, products, and
  data) and down (to models and infrastructure) rather than being captured at the connection layer —
  no one owns "how agents connect," which prevents a connection-layer monopoly.
- **It reduces lock-in**, which favors best-of-breed assembly (pick the best tool, the best agent,
  the best model, connected via standards) over single-vendor stacks — good for buyers, and the reason
  enterprises (§14) champion the standards as a lock-in hedge.
- **It enables the ecosystem to be larger than any vendor**, because open standards let a long tail of
  participants (tens of thousands of MCP servers, thousands of agent builders) contribute — the network effects that
  make the ecosystem valuable are only possible *because* it's open.
- **It shifts competition to where value genuinely is** — model capability, product/workflow value,
  data, and trust — rather than to controlling proprietary plumbing. This is healthier for the
  ecosystem and for buyers than a world where one vendor owned the connective tissue.

The structural reading: **the open standards stack is why the agent ecosystem is a multi-vendor
ecosystem rather than a single-vendor platform** — and that structure, more than any individual
technology, shapes where value accrues and how the whole field competes. The standards are not just
plumbing; they are the constitutional structure of the agent economy, determining that it's an open
market rather than a walled garden. That this constitutional structure came together so fast, and so
open, is one of the more consequential and under-appreciated developments in the whole agent story —
it set the ecosystem on an open trajectory at exactly the formative moment when it could have gone
proprietary.

## Section takeaways

- Standards is the **most contested dimension** (contestedness 9.0) but consolidating **unusually
  fast** — MCP went from experiment to Linux-Foundation standard in ~14 months, closer to JSON's
  organic speed than a committee's grind.
- The standards form a **layered, complementary stack**, not a single winner: **MCP *won* the tool
  layer**, **A2A *leads* the agent-to-agent layer** (a year behind MCP; it absorbed IBM's ACP in 2025 and joined MCP in the AAIF in Aug 2026), and
  **discovery/payments are contested frontiers** — the "MCP vs. A2A" framing is a category error.
- **Fast consolidation** is driven by aligned universal demand, historical lesson-learning (frag-
  mentation hurts everyone → neutral governance), open-given-away protocols beating proprietary ones,
  network effects, and reusable web foundations (OAuth/HTTP/JSON-RPC).
- **History predicts the outcome**: MCP had its *JSON moment* (settled); A2A is having its *REST-vs-
  SOAP moment* (simpler/more-adopted wins under neutral governance); payments will have a *USB-style
  fragment-then-consolidate* (slowest). The throughline: **open, simple, neutrally-governed standards
  win.**
- The snapshot's **A2A vs. ACP** contest had already resolved (IBM's ACP merged into A2A, Aug 2025;
  AGNTCY is complementary), so the genuinely open contest is the **payments land-grab**
  (AP2/ACP/x402/card-networks — now under neutral homes at FIDO and the LF, but years to resolve
  commercially), with **agent identity** the new frontier every standards venue is targeting.
- **Enterprises drive consolidation** (standards as a lock-in hedge, §14); the real remaining lock-in
  gap is the **internal agent definition** (§02), where AGENTS.md and Agent Skills (AAIF) now cover
  instructions and skills but nothing covers the orchestration graph or state.

- **Practically, adopt now**: MCP (tools), A2A (agent-to-agent, mild caution), OpenTelemetry
  (observability), and OAuth 2.1 (auth) — these are settled-enough to build on; wait on payments, and
  accept that the internal agent definition (§02) and memory (§03) remain non-portable because their
  fuzzy interfaces and lock-in incentives resist standardization.
- **Standards are coordination technology** that mature only when an *ecosystem agrees* — so they
  consolidate fast where coordination is easy (universal pain, no dominant defector, neutral
  governance: MCP) and lag where it's hard (lock-in incentives: agent definition, memory). And they
  **shape the ecosystem's structure**: the open, layered, neutrally-governed stack is *why* the agent
  economy is an open multi-vendor market rather than a walled garden — arguably the most consequential
  and under-appreciated development in the whole agent story, set at the formative moment it could have
  gone proprietary. In a field where most layers are bottlenecks or contests, the standards layer is
  the rare piece of durable, structural good news — the connective tissue came together open and fast,
  which is precisely the precondition for everything else in this document to eventually cohere into a
  working, interoperable agent stack rather than a set of vendor silos.

The bottom line for the standards layer: it is the one place in this document where the trajectory is
clearly, structurally positive, and where the field's collective behavior — choosing open, neutral,
layered standards over proprietary control — has already largely determined a good outcome for the
layers that matter most.

*Word count target: 6,500. This section: ~9,100 (verified via `wc`; includes the November 2026 update).*

## Sources (November 2026 update)

- MCP blog — The 2026-07-28 Specification: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- MCP blog index (Ruby SDK Tier 1, Oct 30, 2026; registry launch Sep 2025): https://blog.modelcontextprotocol.io/
- MCP — The New MCP Roadmap (Aug 22, 2026): https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2026-08-22-mcp-roadmap.md
- MCP specification release 2026-07-28: https://github.com/modelcontextprotocol/specification/releases/tag/2026-07-28
- A2A releases (v1.0.0 Mar 12, 2026; v1.0.1 May 28, 2026): https://github.com/a2aproject/A2A/releases
- AAIF — A2A joins AAIF's open agentic stack (Aug 17, 2026): https://aaif.io/blog/a2a-joins-aaif
- Linux Foundation — A2A surpasses 150 organizations (Apr 2026): https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
- Linux Foundation — AAIF welcomes 57 new members (Aug 2026): https://www.linuxfoundation.org/press/agentic-ai-foundation-welcomes-57-new-members-gaining-major-financial-services-players-and-apac-leaders
- Linux Foundation — AAIF announces Agent Skills, Open Responses, OpenEnv, OpenSandbox (Oct 22, 2026): https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox
- Linux Foundation — AAIF surpasses 300 members: https://www.linuxfoundation.org/press/agentic-ai-foundation-surpasses-300-members-in-less-than-one-year
- Linux Foundation — AAIF 2026 events program (AGNTCon + MCPCon): https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-global-2026-events-program-anchored-by-agntcon-mcpcon-north-america-and-europe
- InfoQ — AGNTCon + MCPCon 2026 coverage: https://www.infoq.com/news/2026/10/agntcon-mcpcon-2026/
- Tetrate — Agent Router joins AAIF (Sep 2026): https://tetrate.io/blog/agent-router-joins-aaif
- LF AI & Data — ACP joins forces with A2A (Aug 29, 2025): https://lfaidata.foundation/?p=7689
- AGNTCY project proposal / status: https://github.com/aaif/project-proposals/issues/57 ; https://agntcy.org/changelog
- Google — AP2 donated to the FIDO Alliance (Apr 2026): https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/
- FIDO Alliance — AP2 donation: https://fidoalliance.org/google-donates-agent-payments-protocol-to-fido-alliance/
- Coinbase — x402 Foundation: https://docs.cdp.coinbase.com/x402/support/x402-foundation
- Linux Foundation — x402 Foundation launch: https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol
- State of Agentic Commerce tracker (x402 governance/usage, Oct 2026): https://agenticplug.ai/current-state-of-agentic-commerce
- NIST — AI Agent Standards Initiative (Feb 17, 2026): https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure
- IETF 126 agentproto BoF materials: https://datatracker.ietf.org/meeting/126/materials/slides-126-agentproto-agentproto-03
- IETF 126 BoFs overview: https://www.ietf.org/blog/ietf126-bofs/
- W3C AI Agent Protocol Community Group list archive: https://lists.w3.org/Archives/Public/public-agentprotocol/
- W3C proposed AI Agent Memory Interoperability CG: https://lists.w3.org/Archives/Public/public-dataspaces/2026May/0005.html
- WebMCP status overview (secondary): https://dev.to/ai-agent-economy/webmcp-in-2026-which-browsers-support-navigatormodelcontext-complete-compatibility-status-1oe4
- LocalCan — State of MCP server development (Oct 2026 registry census): https://www.localcan.com/blog/state-of-mcp-server-development

