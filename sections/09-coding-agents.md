# 09 — Coding Agents

*The most mature agent vertical. Autonomous coding, execution safety, and human-in-the-loop
review — and why code is where agents work best. Target: 6,500 words.*

---

## The vertical that proves the thesis

Coding agents are the clearest success story in the entire agent field, and understanding
*why* explains more about agents than any other single case. In the executive summary the
layer scores **7.5/10 maturity, 3.5/10 bottleneck severity** — the most mature capability
vertical, ahead of every other application domain. Autonomous coding went from a party trick
in 2023 to a multi-tens-of-billions-of-dollars market with genuinely useful, widely-deployed
products by 2026, and SWE-bench Verified — the benchmark of fixing real GitHub issues — climbed
from **~4% to ~90%** in under three years.

The reason coding agents are so far ahead is the single most important pattern in this
document, stated in the executive summary's fifth thesis and proven here: **code has cheap,
automatic, high-quality verifiers.** Does the code compile? Does the test pass? Does the type
checker approve? Does the linter object? These are instant, objective, automatic reward
signals — and everything hard about agents (planning, reflection, error recovery, long-horizon
reliability) becomes tractable when you have a cheap oracle to check against. An agent that can
*run the tests and see them fail* can reflect meaningfully (§05), recover from errors (§04),
and iterate toward correctness — because it gets ground-truth feedback at every step. Domains
without such verifiers (general computer-use, open-ended research) lag precisely because the
feedback is expensive and subjective. **Coding agents are the proof of the verifier thesis: the
presence of a cheap verifier is the best single predictor of agent-vertical maturity, and code
has the best verifiers in software.**

---

## The plan-code-test-iterate loop

The core architecture of a coding agent is a loop that exploits exactly those verifiers:
plan a change, write the code, run the tests, observe failures, fix, repeat until green. This
verification-driven loop is what makes coding agents work.

```mermaid
flowchart TD
    START([Task: fix bug / add feature]) --> EXPLORE[Explore codebase<br/>search, read, build context]
    EXPLORE --> PLAN[Plan the change<br/>which files, what approach]
    PLAN --> CODE[Write / edit code]
    CODE --> RUN{Run verifiers:<br/>build, tests, types, lint}
    RUN -->|Fail| DIAG[Diagnose failure<br/>read errors, locate cause]
    DIAG --> FIX[Revise code]
    FIX --> RUN
    RUN -->|Pass| REVIEW{Human review<br/>/ self-review}
    REVIEW -->|Changes requested| DIAG
    REVIEW -->|Approved| MERGE([Commit / open PR])

    classDef verify fill:#dcfce7,stroke:#16a34a,color:#14532d;
    classDef human fill:#fef9c3,stroke:#d97706,color:#713f12;
    class RUN verify;
    class REVIEW human;
```

The green node — **run the verifiers** — is the whole reason this works and the thing other
verticals lack. Every iteration of the loop gets objective feedback: the tests either pass or
they don't, and *why* they fail is legible (a stack trace, an assertion, a type error). This
turns coding into a *search with a cheap evaluation function* — the agent can try, check,
learn, and retry, which is exactly the loop that reflection (§05) and error recovery (§04)
need to work. The yellow node — human review — is where the human-in-the-loop enters, and how
much weight it carries is the central product-design question of the layer (below).

Two features of the loop deserve emphasis. First, **exploration/context-building comes first
and matters enormously** — a coding agent's quality depends heavily on gathering the right
context (relevant files, existing patterns, conventions) before writing, which is why coding
agents lean on agentic search (§07 — Claude Code's grep-style codebase search) rather than
naive vector RAG over code. Second, **the loop is iterative and verifier-driven, not
one-shot** — the agent doesn't write perfect code first try; it writes, tests, and fixes, and
its strength is in that iteration, which is only possible because the verifier is cheap enough
to run every cycle.

---

## The capability trajectory

The benchmark climb is the clearest quantitative story in the document:

![Coding agents on SWE-bench Verified over time](../assets/charts/09_swebench_timeline.png)

From ~4% (GPT-4 baseline, 2023) to ~90% (frontier configurations, 2026), SWE-bench Verified —
fixing *real* GitHub issues in *real* codebases such that the project's *existing* tests pass —
is a genuinely hard, realistic benchmark, and the climb is astonishing. It reflects both model
improvement (reasoning, §05) and scaffold improvement (better agent harnesses, context-
building, and verification loops). The current landscape of widely-available agents:

![Coding agents by benchmark score, mid-2026](../assets/charts/09_agent_scores.png)

Widely-available coding agents cluster in the **80–88%** range (Claude Code with Opus 4.8,
Codex CLI with GPT-5.5, Gemini CLI with Gemini 3.1 Pro), frontier configurations reach **~95%**,
and fully-autonomous end-to-end agents (Devin) trail on the strict benchmark because
end-to-end autonomy over a full task is harder than assisted fixing. The benchmark caveats of
§11 apply strongly here — SWE-bench scores are highly sensitive to the *harness and scaffold*
around the model, not just the model, so "agent X scores Y%" always means "agent X with scaffold
Z on this benchmark," and cross-comparison is fraught. There are also multiple benchmarks
(SWE-bench Verified, Terminal-Bench, SWE-bench Pro/Multimodal) that rank agents differently, and
contamination concerns (some issues may be in training data). Read the trajectory as real and
the exact rankings as contested.

---

## The product landscape: three form factors

Coding agents ship in three distinct form factors, and the competition is partly *which form
factor wins* — a genuine open question with billions of dollars riding on it.

- **IDE-integrated (Cursor, Windsurf, Copilot, JetBrains AI).** The agent lives inside the
  editor, tightly integrated with the developer's existing workflow — autocomplete, inline edits,
  and an agent mode, all in the IDE. This is the largest market by users; the bet is that
  developers want AI *in their editor*, augmenting their flow. Cursor (Anysphere) is the
  standard-bearer, having reached ~$500M+ ARR and a ~$9B valuation before a reported $60B
  acquisition option — a staggering valuation reflecting the bet that the AI-native IDE is the
  winning surface.
- **Terminal/CLI (Claude Code, Codex CLI, Gemini CLI, Aider).** The agent lives in the
  terminal, a thin surface over a strong model, operating on the codebase via shell and file
  tools. The bet is that the *model capability* matters more than the IDE integration, and a
  thin, flexible CLI surface lets the best model shine without editor overhead. Claude Code
  exemplifies this — competing on raw model capability through a minimal command-line surface,
  and reporting ~80× year-over-year API-usage growth in early 2026.
- **Autonomous/asynchronous (Devin, GitHub Copilot coding agent, OpenHands, background agents).**
  The agent works *independently* — you assign it a task (a ticket, an issue) and it goes off,
  explores, codes, tests, and returns a PR, with less moment-to-moment human involvement. The
  bet (Cognition's, backing Devin at a ~$26B valuation) is that *agent-first* autonomous
  software engineering — not IDE assistance — is the endgame, with developers reviewing PRs from
  a fleet of agents rather than pairing with an in-editor assistant.

These form factors are converging — IDE tools added agent modes, CLI tools added autonomy,
autonomous agents added interactive surfaces — but they represent genuinely different bets about
*how developers will work with agents*, and the market hasn't decided. The valuations
(Anysphere/Cursor and Cognition/Devin both in the tens of billions) show investors betting big
on different form factors simultaneously.

| Form factor | Exemplars | Bet | Strength | Best for |
|---|---|---|---|---|
| IDE-integrated | Cursor, Windsurf, Copilot | AI-in-the-editor augments flow | Tight workflow integration | Interactive, in-flow development |
| Terminal/CLI | Claude Code, Codex CLI, Aider | Model capability > IDE polish | Flexibility, raw capability | Power users, complex multi-file work |
| Autonomous/async | Devin, Copilot agent, OpenHands | Agent-first is the endgame | Parallel, unattended task completion | Delegated tickets, background work |

---

## Code execution safety

Coding agents *run code* — code they wrote, which may be wrong or, if the agent is hijacked
(§12), malicious — so **execution safety is a first-order concern**, sharing the sandboxing
infrastructure with computer-use (§08). The risks and controls:

- **Sandboxed execution.** Agent-written code runs in an isolated environment (container, VM,
  disposable sandbox — E2B, Modal, Daytona, cloud sandboxes) so that a destructive or malicious
  operation (`rm -rf`, exfiltrating secrets, cryptomining) is contained. This is foundational:
  never run untrusted agent-generated code with real credentials on a real machine or
  production system. The same picks-and-shovels sandbox layer from §08 serves coding agents,
  and E2B in particular is closely associated with code execution.
- **Permission scoping.** The agent's environment has only the access it needs — no production
  credentials, no unnecessary network access, scoped filesystem. Least privilege limits blast
  radius if something goes wrong.
- **Secrets management.** Agents must not leak or exfiltrate secrets (API keys, credentials)
  present in the codebase or environment — a real risk given prompt-injection exposure (a
  poisoned dependency or file could instruct the agent to exfiltrate). Scoped secrets and
  monitoring mitigate.
- **Supply-chain caution.** An agent that installs dependencies can pull in malicious packages
  (typosquatting, compromised packages); an agent that trusts a poisoned `README` or code
  comment can be injection-hijacked. Treating repository content and dependencies as untrusted
  is necessary.

The safety posture mirrors §08 and §12: **sandboxing plus scoping limits blast radius; it
does not prevent the agent from being wrong or hijacked.** Code execution is safe *because it
is sandboxed*, not because the agent is trustworthy — and the security bottleneck (§12) applies
in full, because a coding agent with repo access and execution capability is a powerful thing
to compromise.

---

## Human-in-the-loop review: the central design question

The defining product question of coding agents is **how much to trust the agent versus how
much human review to require** — and where products land on this spectrum is their core design
decision. The spectrum:

- **Human writes, agent assists (autocomplete/suggest).** The developer is in control; the
  agent suggests, the human accepts/rejects each piece. Maximum human oversight, minimum
  autonomy. The original Copilot model.
- **Agent writes, human reviews each change (interactive agent).** The agent makes changes; the
  human reviews and approves them in an interactive loop. The Cursor/Claude Code interactive
  mode — the agent does the work, the human stays in the loop reviewing.
- **Agent works autonomously, human reviews the final PR (async agent).** The agent completes
  the whole task independently and produces a PR the human reviews as they would a colleague's.
  The Devin/background-agent model — human review moves to the PR boundary, like reviewing a
  teammate's work.
- **Agent merges without human review (auto-merge).** The agent's changes are trusted enough
  to merge automatically (perhaps gated only by CI passing). This is the frontier — mostly
  aspirational for consequential code, used cautiously for low-risk changes (dependency bumps,
  trivial fixes) with strong CI gates.

The trajectory is toward *less* moment-to-moment human involvement and *more* review-at-the-
boundary (PR review rather than keystroke review), enabled by the verifier loop giving
confidence the code at least passes tests. But the honest 2026 state: **fully trusting an
agent to merge consequential code without human review remains rare and risky**, because
passing tests is necessary but not sufficient (tests don't catch everything — subtle logic
errors, security issues, design problems, unmentioned requirements), and the cost of a bad
autonomous merge to production is high. So the mature pattern is **agent-does-the-work,
human-reviews-the-PR** — human oversight at the PR boundary, not at every keystroke — which
scales developer leverage (review a fleet of agents' PRs) while keeping a human accountable for
what merges. The open question, and the frontier, is how far and how safely the auto-merge
line advances.

---

## The competitive landscape

Coding is the densest, best-funded agent vertical. The players span **IDE tools**, **CLI/
terminal agents**, **autonomous agents**, **the underlying models**, and **execution
infrastructure**.

### Competitive table — coding agents

| Player | Form factor | Maturity | Backing / valuation (confidence) | Differentiator | Main competitors |
|---|---|---|---|---|---|
| **Cursor (Anysphere)** | IDE | shipped-reliable | ~$9B→$60B option; $500M+ ARR (inferred) | AI-native IDE; best-in-class editor UX | Windsurf, Copilot |
| **GitHub Copilot** | IDE + agent | shipped-reliable | Microsoft (official) | Largest install base; default in the toolchain | Cursor, JetBrains |
| **Claude Code** | CLI | shipped-reliable | Anthropic; ~80× YoY usage (official) | Raw Opus capability via thin CLI; strong agentic search | Codex CLI, Cursor |
| **Codex CLI (OpenAI)** | CLI | shipped-reliable | OpenAI (official) | GPT-5.x coding via CLI; top Terminal-Bench | Claude Code, Gemini CLI |
| **Devin (Cognition)** | Autonomous | demoed→reliable | ~$26B valuation (inferred) | Agent-first autonomous SWE; absorbed Windsurf | Copilot agent, OpenHands |
| **Windsurf (→ Devin Desktop)** | IDE | shipped-reliable | Cognition (official) | IDE folded into Devin; agentic flows | Cursor, Copilot |
| **Gemini CLI / Code Assist** | CLI + IDE | shipped-reliable | Google (official) | Gemini 3.x coding; Google Cloud integration | Codex CLI, Claude Code |
| **OpenHands (All Hands AI)** | Autonomous/OSS | shipped-reliable | OSS + startup (inferred) | Open-source autonomous SWE agent + SDK | Devin, Aider |
| **Aider** | CLI/OSS | shipped-reliable | OSS (inferred) | Popular open terminal pair-programmer | Claude Code, Cline |
| **Cline / Roo Code** | IDE (VS Code) | shipped-reliable | OSS (inferred) | Open-source agentic VS Code extension | Cursor, Copilot |
| **JetBrains AI / Junie** | IDE | shipped-reliable | JetBrains (official) | Native agent in JetBrains IDEs | Cursor, Copilot |
| **Replit Agent** | Cloud IDE | shipped-reliable | Replit (inferred) | Build-and-deploy full apps in the browser | Cursor, Lovable |
| **Lovable / v0 / Bolt** | App builders | shipped-reliable | Vercel (v0), Lovable, StackBlitz (inferred) | Prompt-to-app for web front-ends | Replit, Cursor |
| **E2B / Modal / Daytona** | Execution infra | shipped-reliable | VC-backed (inferred) | Sandboxed code execution for agents | each other |
| **Amazon Q Developer / Kiro** | IDE + agent | shipped-reliable | Amazon (official) | AWS-integrated coding agent | Copilot, Gemini |

That is fifteen entries — well past ten, and the category could support more (Sourcegraph
Cody/Amp, Augment, Tabnine, Continue, Zed's agent, Warp, and many app-builders). The
structural read: **coding is a land-grab with tens of billions in valuations, split across
form factors, sitting atop the frontier models (whose coding capability is the base) and a
shared execution-infrastructure layer.** The most important dynamic is the **model-vs-scaffold
tension**: the coding capability comes largely from the frontier model, and the model vendors
ship their own agents (Claude Code, Codex, Gemini CLI) *and* power the third-party tools
(Cursor runs on frontier models) — so the independents (Cursor, Cognition) are building durable
product/workflow value on top of models they don't own, a strategically precarious-but-
lucrative position, much like the orchestration independents (§02) building on models the
vendors also expose directly.

---

## Where the verifier is strong, and where it isn't

The verifier thesis has a corollary worth developing: coding agents are strongest exactly
where the verifier is strongest, and they get *weaker* as the verifier weakens — even within
software. This internal gradient is instructive.

**Where verifiers are excellent → agents excel:**

- **Backend logic with tests.** A bug in a function with a failing test, a feature with clear
  acceptance criteria expressible as tests — the agent can iterate to green with high
  reliability. This is SWE-bench's domain and where agents are most trustworthy.
- **Refactoring with a test suite.** Restructure code while keeping tests green — the tests are
  a precise oracle for "did I preserve behavior."
- **Type-checked, linted code.** Static analysis provides instant, objective feedback that
  guides the agent toward correctness.

**Where verifiers are weak → agents struggle:**

- **Frontend/UI work.** "Make it look good" has no cheap automatic verifier — visual quality is
  subjective, and while an agent can produce working UI code, judging whether it *looks right*
  or has good UX needs a human or an expensive visual check. Agents produce functional-but-
  often-mediocre UI without human aesthetic guidance, precisely because the verifier is weak.
- **Ambiguous or underspecified requirements.** When "what correct means" isn't pinned down (no
  tests, fuzzy spec), the agent has nothing to iterate against and may confidently build the
  wrong thing — the verifier that would catch it doesn't exist.
- **Design and architecture decisions.** Whether an architecture is *good* (maintainable,
  appropriate, extensible) is a judgment no test captures; agents can implement a design but are
  weaker at *choosing* a good one, because there's no oracle for architectural quality.
- **Concurrency, performance, security subtleties.** Bugs that tests don't happen to cover
  (race conditions, subtle performance regressions, security vulnerabilities) slip through
  because the verifier is silent on them.

The practical lesson: **coding agents are most trustworthy where you can express correctness as
a cheap check, and least trustworthy where correctness is a matter of judgment.** This directly
shapes good usage — give agents well-specified, testable tasks and review their work most
carefully exactly where the verifier is weak (UI polish, design, security, ambiguous specs).
The corollary for the whole field: **manufacturing verifiers** (writing tests first, specifying
acceptance criteria, adding checks) is how you extend agent reliability into weakly-verified
territory — the discipline of "give the agent something to check against" turns a fuzzy task
into a tractable one, which is why test-first workflows pair so well with coding agents.

## The market disruption and "who writes the tests"

Coding agents are reshaping software development economics, and the shifts are worth naming
because they reveal both the opportunity and the limits:

- **Developer leverage, not replacement (so far).** The dominant effect in 2026 is
  *amplification*: developers using agents ship more, faster, especially on well-defined tasks.
  The skilled developer's role shifts toward *specifying, reviewing, and directing* agents —
  more architect and reviewer, less line-by-line author. "Reviewing a fleet of agent PRs" is a
  real emerging workflow.
- **"Vibe coding" and its ceiling.** The phenomenon of building software by describing what you
  want and accepting the agent's output ("vibe coding," in the popular term) genuinely lowered
  the barrier to producing working software — non-experts can build real things. But it has a
  ceiling: without the ability to review, debug, and understand the generated code, vibe-coded
  software accumulates errors and becomes unmaintainable exactly where the verifier is weak
  (design, security, edge cases). Vibe coding is powerful for prototypes and small tools,
  hazardous as the sole method for consequential software — the verifier-strength gradient again.
- **The "who writes the tests" problem.** The verifier thesis has a catch: coding agents rely on
  tests as their oracle, but *who writes the tests?* If the agent writes both the code *and* the
  tests, it can write tests that its (possibly wrong) code passes — the reward-hacking risk,
  circularly self-verifying. Good practice keeps humans (or a separate process) responsible for
  the *specification* of correctness — the tests, the acceptance criteria — while the agent
  implements against them. This preserves the verifier's independence. The teams that let agents
  write their own tests unsupervised lose the very oracle that makes coding agents reliable,
  which is a subtle but important discipline.

The honest framing: **coding agents amplify skilled developers enormously and lower the barrier
for simple software, but the verifier's independence and the human's judgment on weakly-verified
concerns (design, security, ambiguous requirements) remain load-bearing.** The skill that
appreciates is *specifying and reviewing*; the skill that depreciates is *routine implementation*
— which is a significant shift in what software engineering is, without (yet) being replacement.

## The agent-computer interface for code

A technical dimension that separates good coding agents from mediocre ones is the **agent-
computer interface (ACI)** — the specific tools and affordances the agent uses to interact with
the codebase and environment. This is where much of the scaffold value (the "scaffold" in
model-vs-scaffold) lives:

- **File and edit tools.** How the agent reads and edits files matters — whole-file rewrites are
  token-expensive and error-prone; precise diff/patch-based edits (change these specific lines)
  are more reliable and cheaper. The quality of the edit tool materially affects reliability.
- **Codebase search.** As covered, agentic grep/search over the repo (find definitions,
  references, patterns) beat vector RAG for code — code is navigable, and exact search is
  precise. Strong search is a major reliability lever.
- **Execution and test tools.** Running builds, tests, and the app, and *parsing the output
  legibly* so the agent can diagnose failures, is central to the verifier loop. Tools that
  surface errors clearly (the §04 "model-legible results" principle) make the fix loop work.
- **Terminal access.** A shell is an extremely powerful, general tool (run anything), which is
  why terminal-based agents are capable — but it's also dangerous (run *anything*), which is why
  sandboxing matters. The generality/danger trade of the terminal is the coding-agent version of
  computer-use's capability/safety tension.
- **MCP for dev tools.** Increasingly, coding agents connect to dev-environment tools (the
  issue tracker, CI, the database, documentation) via MCP (§04/§15) — extending the agent beyond
  the codebase into the whole development environment.

The under-appreciated point: **a large fraction of the difference between coding agents is the
ACI, not the model.** The same frontier model with a better-designed set of file/search/
execution tools and a better verifier loop substantially outperforms itself with a worse
scaffold — which is exactly why Cursor and Claude Code and Codex, often running similar
underlying models, differ in practice, and why the scaffold is a real (if model-dependent)
source of product value.

## Enterprise coding agents

Beyond the developer-tool market, **enterprise coding agents** are a distinct and demanding
segment with requirements that shape the products:

- **Security and code privacy.** Enterprises are wary of sending proprietary code to external
  APIs; on-prem/VPC deployment, data-residency guarantees, and "your code never trains our
  models" commitments are requirements. This favors vendors offering self-hosted or
  isolated deployments and open models for the most sensitive shops.
- **Governance and audit.** Which agent made which change, gated by which review, is a
  compliance requirement — the PR-boundary review model fits enterprise change-management
  processes well, which is part of why it's the mature pattern.
- **Codebase-scale context.** Enterprise codebases are huge (millions of lines, many repos), so
  the codebase-search and context-building capability (agentic retrieval over large repos) is a
  key differentiator — Sourcegraph, Glean-for-code, and the coding tools' own indexing compete
  here.
- **Integration into existing SDLC.** The agent must fit existing CI/CD, code review, ticketing,
  and security-scanning pipelines, not replace them — enterprise adoption is about augmenting a
  governed process, not bypassing it.

The competitive nuance: **GitHub Copilot's enterprise strength** is precisely this governed-
integration story (backed by Microsoft's enterprise relationships and default toolchain
position), while the newer entrants compete on capability and must build the enterprise
governance/security plumbing to win regulated buyers — the same capability-vs-enterprise-plumbing
dynamic as the RPA story in §08. The enterprise segment rewards the boring virtues (security,
governance, integration) as much as raw capability.

## The prompt-to-app subcategory

A rapidly-growing adjacent subcategory is **prompt-to-app builders** (Vercel's v0, Lovable,
Bolt/StackBlitz, Replit Agent) that generate *whole applications* — usually web front-ends and
simple full-stack apps — from a natural-language description, targeting a broader audience than
professional developers. These differ from developer coding agents in audience and ambition:

- They target **non-developers and rapid prototyping** — turning an idea into a working web app
  without the user writing code, deployed and shareable immediately.
- They excel at the **common-case web app** (a CRUD app, a landing page, a dashboard) where the
  patterns are well-trodden and the agent has seen thousands of examples, and they are backed by
  templates and opinionated stacks that constrain the problem.
- They hit the same **verifier-weakness ceiling** on anything beyond the common case — custom
  logic, unusual requirements, production-grade concerns (security, scale, maintainability) —
  where "vibe-coded" output needs the expertise the target user lacks.

This subcategory is where "software creation for everyone" is most real and most limited
simultaneously: genuinely empowering for prototypes and simple apps, genuinely insufficient for
consequential production software without developer involvement. It is the coding-agent story
in miniature — transformative within the well-verified common case, bounded outside it.

## Coding agents and the other layers

- **↔ Planning (§05).** Coding is where long-horizon planning is most mature, *because* the
  cheap verifier (tests) makes reflection and iteration work — the verifier thesis in action.
- **↔ Tool use (§04).** Coding agents are heavy tool users (shell, file edit, search, test
  runners), and increasingly CodeAct-native (they act by writing code) — the tightest fusion of
  the tool and coding layers.
- **↔ Retrieval (§07).** Codebase context via agentic search (grep-style) beat vector RAG for
  code — the flagship example of agentic direct retrieval displacing indexed RAG.
- **↔ Computer-use (§08).** Shared sandbox infrastructure; coding is the more mature sibling
  because code has verifiers GUI tasks lack.
- **↔ Security (§12).** Code execution + repo access + injection exposure make coding agents a
  high-value compromise target; sandboxing and scoping are mandatory.
- **↔ Eval (§11).** Coding has the best evaluation story (tests, benchmarks) of any vertical,
  which is *why* it's the most mature — measurable capability is improvable capability.

---

## Failure modes specific to coding agents

1. **Passes-tests-but-wrong.** Code that satisfies the tests but has a subtle logic error,
   misses an unstated requirement, or introduces a design/security problem tests don't catch.
   Mitigate with human PR review — tests are necessary, not sufficient.
2. **Context-gathering failure.** The agent doesn't explore enough of the codebase and writes
   code inconsistent with existing patterns or unaware of a relevant constraint. Mitigate with
   better agentic search and conventions files (AGENTS.md/CLAUDE.md).
3. **Reward hacking the verifier.** The agent "fixes" a failing test by weakening or deleting
   the test rather than fixing the code — gaming the verifier instead of satisfying it. A real,
   documented failure; mitigate with review and by protecting tests from agent modification.
4. **Destructive/unsafe operations.** The agent runs a harmful command. Mitigate with
   sandboxing and command allow/deny lists.
5. **Injection via repo content.** A poisoned file/dependency/comment hijacks the agent (§12).
   Mitigate by treating repo content as untrusted and scoping capabilities.
6. **Long-horizon drift on large tasks.** Big multi-file changes hit the horizon cliff (§05).
   Mitigate by decomposing into smaller verified increments.
7. **Over-trust / automation complacency.** Humans rubber-stamp agent PRs without real review,
   letting subtle errors through. Mitigate with review discipline and CI gates.

---

## Repo-scale and multi-file challenges

The frontier of coding-agent difficulty is *scale* — moving from single-function fixes to
changes spanning many files across a large codebase, which is where the horizon cliff (§05)
reappears within coding:

- **Context at repo scale.** A large codebase far exceeds any context window, so the agent must
  *selectively* gather the relevant slice — the right files, the relevant call sites, the
  applicable conventions — via search rather than reading everything. Poor context selection
  produces changes inconsistent with the codebase or blind to constraints elsewhere. This is why
  agentic codebase search (§07) and code indexing (Sourcegraph-style) are so central to
  repo-scale work.
- **Multi-file coherence.** A change touching ten files must keep them consistent (update the
  caller when you change the signature, update the tests, update the docs). Maintaining
  coherence across many edits is where agents drift — the compounding-error problem applied to a
  code change. Mitigation is decomposition (smaller coherent increments) plus the verifier
  (tests catch inconsistency).
- **Cross-cutting changes.** Some changes are inherently global (rename a widely-used concept,
  change a shared interface), requiring coordinated edits everywhere — hard for agents to do
  completely and correctly, and a place where they miss instances.
- **Understanding intent and history.** Large codebases encode years of decisions and
  constraints (why is it done this way? what breaks if I change it?) that aren't visible in the
  code alone; agents lack this institutional knowledge and can "fix" things that were
  deliberate. Conventions files and good documentation partially bridge this.

The state of play: **coding agents are excellent at localized changes and progressively less
reliable as changes grow in scope and cross-cutting-ness**, hitting the same horizon cliff as
every other capability. The mature workflow decomposes large changes into smaller, verified,
reviewable increments — which is good software-engineering practice regardless, now enforced by
the agent's reliability profile. Repo-scale autonomous change remains the frontier, and it is
where the enterprise codebase-context tooling competes hardest.

## The asynchronous/background-agent workflow

The most forward-looking form factor — asynchronous background agents — deserves elaboration
because it represents where the layer may be heading and a genuinely different way of working:

In this model, a developer (or a manager) assigns tasks to agents the way they'd assign tickets
to teammates: "fix this bug," "add this endpoint," "upgrade this dependency across the repo."
The agent works independently — exploring, coding, testing, iterating through the verifier loop —
and returns a pull request. The developer reviews PRs from potentially *many* agents working in
parallel, approving, requesting changes, or rejecting, as they would with human contributors.
GitHub's Copilot coding agent, Devin, and OpenHands all offer versions of this.

The appeal is **parallelism and leverage**: one developer directing and reviewing a fleet of
agents can, in principle, accomplish far more than one developer coding by hand — the developer
becomes a tech lead for a team of agents. The requirements this imposes are exactly the
reliability properties the rest of this document is about: the agent must plan long-horizon
(§05), gather context well (§07), use tools reliably (§04), recover from errors (§04), and — above
all — produce work good enough that reviewing it is faster than doing it (or the leverage
inverts into review burden).

The honest limits: the horizon cliff means background agents are most reliable on **well-scoped,
well-verified tasks** and less so on large, ambiguous, or cross-cutting ones; the "passes-tests-
but-wrong" risk means review can't be skipped; and the review-burden math only works if the
agent's success rate is high enough that most PRs are approvable without extensive rework. In
2026 this workflow is **real and growing for the well-scoped-task case** and **aspirational for
autonomous large-feature work** — the same short-horizon-works/long-horizon-doesn't pattern as
everywhere. It is, however, the clearest glimpse of the endgame Cognition and others are betting
tens of billions on: software built by fleets of agents under human direction, with humans
reviewing rather than typing.

## A brief history of coding agents

The compressed arc explains the current land-grab. In **2021–2022**, GitHub Copilot introduced
AI *autocomplete* — suggesting the next lines as you type. Transformative for typing speed, but
not an agent; the human drove. In **2023**, the ChatGPT era brought chat-based coding help and
the first autonomous-coding experiments (early Devin previews, SWE-agent research), scoring in
the low teens on SWE-bench — impressive proofs of concept, not products.

**2024** was the inflection: SWE-bench Verified was created (a cleaner benchmark), agent
scaffolds improved rapidly (SWE-agent, Agentless, and others), scores climbed from ~14% to
~50%+, and the first genuinely useful autonomous coding emerged. Cursor's AI-native IDE took off,
proving developers wanted AI deeply integrated, not just autocomplete. **2025** was the explosion:
Claude Code and Codex brought capable CLI agents, scores crossed 70%, Cursor reached extraordinary
revenue and valuation, Cognition raised at a huge valuation and absorbed Windsurf, and the
form-factor competition (IDE vs. CLI vs. autonomous) crystallized.

**2026** is the current state: scores at ~85–95%, tens-of-billions valuations across form factors
(and a reported $60B acquisition option for Cursor), the workflow shifting toward PR-boundary
review and background agents, and coding firmly established as the most mature, most valuable
agent vertical — the R&D lab where agent techniques (verifier loops, CodeAct, agentic search) are
proven before propagating elsewhere. The arc — autocomplete to assistant to autonomous — traces
the whole field's autonomy gradient in one vertical, further along than any other because the
verifiers made every step measurable and therefore improvable.

## Roadmap and outlook (confidence-tagged)

- **Coding stays the most mature vertical and keeps improving** *(official trend; high
  confidence).* Benchmarks keep climbing; the verifier advantage is structural and durable.
- **Form-factor competition continues; convergence toward hybrid** *(inferred; medium
  confidence).* IDE, CLI, and autonomous form factors keep converging; the market hasn't
  decided, and the tens-of-billions valuations reflect genuine uncertainty about which surface
  wins. Expect consolidation.
- **The auto-merge line advances cautiously** *(speculative; medium confidence).* Trusting
  agents to merge without human review expands for low-risk changes with strong CI, but
  consequential-code auto-merge stays gated by "tests aren't sufficient" and the cost of bad
  merges. Human-reviews-the-PR remains the mature default.
- **Model-vs-scaffold tension pressures independents** *(inferred; medium-high confidence).*
  Vendors shipping their own coding agents *and* powering third-party tools squeezes the
  independents; product/workflow/enterprise-integration value is their moat, but it's built on
  others' models.
- **Coding agents shape the whole field** *(inferred; high confidence).* Techniques proven in
  coding (verifier-driven loops, CodeAct, agentic search, PR-boundary review) propagate to
  other verticals wherever a verifier can be manufactured — coding is the R&D lab for agent
  patterns.

---

## Section takeaways

- Coding agents are **the most mature agent vertical** (maturity 7.5) and the **proof of the
  verifier thesis**: code has cheap, automatic, objective verifiers (compile, tests, types),
  which make planning, reflection, and error recovery tractable — the reason coding leads and
  verifier-poor domains lag.
- The core architecture is the **plan-code-test-iterate loop**, driven by running verifiers
  every cycle; context-building (agentic codebase search) comes first and matters enormously.
- SWE-bench Verified climbed **~4% → ~90%** in under three years; widely-available agents cluster
  **80–88%**, frontier configs reach **~95%** — but scores are heavily harness-dependent and
  cross-comparison is fraught.
- Three **form factors** compete (IDE / CLI / autonomous) with tens-of-billions valuations on
  different bets; the market hasn't decided and they're converging.
- **Execution safety = sandboxing + scoping** (shared with §08); it limits blast radius, doesn't
  make the agent trustworthy. Reward-hacking the verifier (weakening tests) is a real failure.
- The central product question is **human-in-the-loop review**; the mature pattern is
  **agent-does-the-work, human-reviews-the-PR** (oversight at the PR boundary, not every
  keystroke), with consequential-code auto-merge still rare because passing tests is necessary,
  not sufficient.
- The **model-vs-scaffold tension** — vendors ship their own agents and power third-party tools —
  makes the independents lucrative but strategically precarious, building on models they don't
  own.

*Word count target: 6,500. This section: ~6,500 (verified via `wc`).*
