# Knowing When Agents Add Value

> **Source:** T-DEVAGENTFUN-I-m3-l1-en-file-6.en.pdf
> **Added:** 2026-05-26
> **Tags:** ai-agents, agent-design, when-to-use, decision-making, anti-patterns
> **Type:** documentation

## Summary

A decision framework for choosing when to use agents vs. simpler alternatives. Defines four characteristics of "agent-shaped" problems, three trigger types with concrete examples, five anti-patterns where agents are the wrong tool, and a decision tree that maps directly back to Module 1 and 2 concepts. The core principle: agents earn their cost when you need reasoning + adaptation + multi-step execution across multiple systems.

## Key points

- Four signals that a problem is agent-shaped: goal-oriented behavior, multi-step reasoning + external actions, adaptive problem-solving, multi-system integration.
- Three trigger types for agents: event-triggered, chat-triggered, time-triggered.
- Five anti-patterns — when to skip agents: simple Q&A, single API calls, high-volume/low-complexity, deterministic workflows, real-time/latency-sensitive.
- Decision tree anchored to prior modules: questions map directly to orchestration loop (m2), autonomous+proactive (m1), model as decision maker (m2), tool use+environmental awareness (m1).
- Also resolves the open question from [[devagentfun-m1-l0]]: if it's a single step with no adaptation, just use function calling — agents start where multi-step autonomous orchestration begins.

## Notes

### Four signals of an agent-shaped problem

| Signal | What it means |
|---|---|
| **Goal-oriented behavior** | Task has an objective to reach, not just a question to answer |
| **Multi-step reasoning + external actions** | Solving the problem requires a sequence of dependent steps that each interact with external systems |
| **Adaptive problem-solving** | The approach must change based on what the agent discovers mid-task |
| **Multi-system integration** | The task spans multiple systems seamlessly — no single API or database covers it |

If most of these apply, you have an agent-shaped problem.

### Where agents excel — three trigger types

**Event-triggered: Automated incident response**
A production error fires → agent analyzes logs, checks recent deployments, queries monitoring, determines severity, creates incident ticket, routes to on-call, rolls back if criteria met, updates stakeholders. All before a human needs to ask.
> "It's infrastructure that thinks."

**Chat-triggered: Research and analysis**
"Prepare a competitive analysis of our top three competitors" → agent identifies competitors, gathers news, pulls financial data, analyzes product offerings, compiles reviews, generates comparison matrix with citations. Days of human work, automated. Agents here are *force multipliers for knowledge work*.

**Time-triggered: Daily business intelligence**
Every morning at 8 AM → agent pulls metrics from sales/support/product, compares against targets and trends, identifies anomalies, generates executive summary, adapts format based on what's significant, sends personalized briefings. No manual scheduling.

### Where agents don't make sense — five anti-patterns

| Anti-pattern | Why agents are wrong here | Use instead |
|---|---|---|
| **Simple Q&A** | "What's your return policy?" — no reasoning, planning, or tool use needed | Retrieval system / FAQ page |
| **Single API call** | "Get today's weather" — one function, no orchestration needed | Direct function calling |
| **High-volume, low-complexity** | 10,000 identical operations (resize images, send notifications) — agents add latency and cost with no benefit | Traditional automation |
| **Deterministic workflows** | Fully rule-based, no variation ("if order > $100, free shipping") — reasoning capability wasted | Workflow automation |
| **Real-time / latency-sensitive** | Microsecond trading, real-time game actions, safety-critical controls — the agent loop adds unacceptable latency | Specialized fast systems |

### Decision tree

Four questions; "yes" to most means use an agent:

1. **Multiple steps that depend on each other?** (→ orchestration loop, [[devagentfun-m2-l1]])
2. **Needs to adapt based on what it discovers?** (→ autonomous + proactive, [[devagentfun-m1-l1]])
3. **Needs to reason about the best approach?** (→ model as decision maker, [[devagentfun-m2-l1]])
4. **Needs to take actions in external systems?** (→ tool use + environmental awareness, [[devagentfun-m1-l1]])

Decision paths:
- No to multiple steps + no complex reasoning → **use simple API**
- No to multiple steps + yes complex reasoning + no external actions → **use LLM**
- Yes to multiple steps + no adaptation → **use workflow automation**
- Yes to multiple steps + yes adaptation → **use agent**

## Quotes worth keeping

> "Agents are powerful, but they're not the answer to everything. Use them where their unique capabilities — autonomous reasoning and action — provide real value."

> "Agents add latency and cost. When you need to process 10,000 identical operations, use traditional automation."

## Open questions

- How does the course handle hybrid cases — e.g., a high-volume task with occasional adaptive exceptions?
- Is there guidance on agent cost/latency benchmarks to make the anti-pattern tradeoffs quantitative?

## Related sources

- [[devagentfun-m3-l0]] — previous lesson: the two failure modes (over- and under-engineering) that motivate this framework
- [[devagentfun-m1-l1]] — five characteristics map directly to decision tree questions 2 and 4
- [[devagentfun-m2-l1]] — agent loop and model as decision maker map to questions 1 and 3
- [[gcloud-agents-core-capabilities]] — the customer returns scenario from m3-l0 is developed into the full multi-agent refund workflow there; the research/analysis trigger type here connects to that same "agents chain actions to resolve" capability
