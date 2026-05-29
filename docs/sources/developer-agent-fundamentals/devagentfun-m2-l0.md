# Building Agents: The Three-Component Architecture

> **Source:** T-DEVAGENTFUN-I-m2-l0-en-file-3.en.pdf
> **Added:** 2026-05-26
> **Tags:** ai-agents, agent-architecture, orchestration, model, tools
> **Type:** documentation

## Summary

All five agent characteristics from Module 1 emerge from just three architectural components working together: the model (thinking), the tools (doing), and the orchestration (the process connecting them). The lesson argues from the problem direction — without this structured architecture, building intelligent behavior forces you into thousands of lines of brittle if-then-else code that breaks on any variation.

## Key points

- Three components produce all five characteristics: model → autonomous decision-making + environmental awareness; tools → real-world action; orchestration → goal-directed + proactive behavior.
- **Orchestration** is named as the third component here (vs. **memory** in [[gcloud-agents-architecture]] — see note below).
- The "brittle code" problem: without the three-component architecture, complex tasks require hardcoded logic for every possible path, which collapses under variation.
- Car analogy: engine (model) + wheels (tools) + steering (orchestration) — every agent has these three regardless of type.

## Notes

### The three-component mapping

| Component | Role | Characteristics it enables |
|---|---|---|
| **Model** | Thinking — understands requests, makes decisions | Autonomous operation (2), Environmental awareness (4) |
| **Tools** | Doing — takes real-world action | Tool use (5) |
| **Orchestration** | Connecting — the process that ties model and tools together | Goal-directed behavior (1), Proactive initiative (3) |

Characteristic numbers refer to [[devagentfun-m1-l1]]'s five-characteristic framework.

### Why you need the architecture: the brittle code problem

Naively, you might think you can just wire a language model to some APIs. The scheduling example shows why that fails:

**Task:** "Schedule a meeting with Sarah next week"

Steps required:
1. Understand who Sarah is
2. Check both calendars for availability
3. Find a mutually free time
4. Send a meeting invitation
5. Add to both calendars
6. Confirm with user

Without the three-component architecture, you write specific code for each possible deviation: what if Sarah is busy? what if the user's calendar is full? what if the email fails? The result is thousands of lines of if-then-else logic that breaks the moment a user phrases something slightly differently.

> The root problem isn't task complexity — it's that without model + tools + orchestration working as a unified system, you're forced to handle complexity with rigid code instead of flexible, intelligent behavior.

### Divergence: "orchestration" vs. "memory"

[[gcloud-agents-architecture]] names the three building blocks as **model + tools + memory**. This source (citing the Google whitepaper directly) names them as **model + tools + orchestration**.

These are not contradictory — they're different framings of the third component:
- **Memory** emphasizes the agent's ability to retain and retrieve context across a task or session.
- **Orchestration** emphasizes the process loop that connects the model's decisions to tool invocations and back — the "steering system."

Memory is arguably *part of* orchestration (the orchestration layer manages what context the model sees). Neither framing is wrong; they zoom into different aspects of the same component.

## Quotes worth keeping

> "Three components, working together, produce all five agent characteristics."

> "Without the model, tools, and orchestration working together as a unified architecture, you're forced to handle that complexity with rigid, brittle code instead of flexible, intelligent behavior."

## Open questions

- ~~Does the course later define orchestration more precisely?~~ Answered in [[devagentfun-m2-l1]]: orchestration *is* the agent loop — Perceive → Think → Act → Check.
- How does the orchestration component relate to Google Cloud's specific orchestration tools (Vertex AI Agent Builder, etc.)?

## Related sources

- [[devagentfun-m2-l1]] — next lesson: deep-dive on each component; defines the agent loop (Perceive → Think → Act → Check) as the precise mechanism of orchestration
- [[devagentfun-m1-l1]] — defines the five characteristics this lesson explains architecturally; confirms this is Module 2 building directly on Module 1
- [[gcloud-agents-architecture]] — same territory (model + tools + third component) but names the third component "memory" instead of "orchestration"; extends this with MCP, three memory layers, and agent patterns
- [[devagentfun-m1-l0]] — preceding module: the three evolutionary stages that led to needing this architecture
