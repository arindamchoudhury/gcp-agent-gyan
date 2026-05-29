# The Agent Architecture

> **Source:** [Google Cloud Training — T-GCAGNT-B](https://storage.googleapis.com/cloud-training/cls-html5-courses/T-GCAGNT-B/v1.0.1/index.html#/lessons/yaA_1phCn7wjXaruR1COGdPAXh23UTjw)
> **Added:** 2026-05-26
> **Tags:** ai-agents, google-cloud, agent-architecture, mcp, memory, agent-patterns
> **Type:** documentation

## Summary

Agents are built from three technical building blocks — a model (intelligence), tools (ability to act), and memory (context across interactions). These are the *how* behind the three core capabilities defined in [[gcloud-agents-core-capabilities]]: model → reasoning/planning, tools → autonomous action, memory → continuous learning. The lesson also introduces three foundational agent patterns: the simple single agent, the sub-agent pattern, and the orchestrator/router pattern (the latter being the technical implementation of the multi-agent collaboration scenario in [[gcloud-agents-core-capabilities]]).

## Key points

- **Three components**: model + tools + memory. All three are required for an effective agent.
- Models today are often "thinking models" — capable of self-reflection before responding, suited for complex tasks.
- **MCP (Model Context Protocol)** is the standard for giving agents access to tools; it extends an API with semantic meaning about when/how to use it.
- Memory has three layers: context window (active), short-term, and long-term. Context requires active management as tasks evolve.
- **Three agent patterns**: simple single agent → sub-agent → orchestrator/router. Each adds more coordination complexity.

## Notes

### Building block 1 — Model

The model is the "brain" of the agent. Modern agents use **thinking models** — models with built-in self-reflection ability. They consider a set of ideas before producing a final response, making them well-suited to complex, multi-step tasks where the agent must reason before acting.

### Building block 2 — Tools (and MCP)

Tools let the agent interact with the world — APIs, databases, code execution, search.

**Model Context Protocol (MCP)** is the dominant standard for agent tool access:

- Like an API, but enriched with semantic instructions
- Tells the agent *what* an API does, *when* to use it, and *what the inputs/outputs mean*
- Gives the agent enough understanding to decide autonomously which tool to invoke in which situation

> Analogy: API = what you can call. MCP = API + instructions on when and why to call it.

### Building block 3 — Memory

Memory gives agents context across interactions. Three layers:

| Layer | Description |
|---|---|
| **Context window** | The active working memory — everything the agent currently "sees" |
| **Short-term memory** | Temporary storage across a session or task |
| **Long-term memory** | Persistent storage; retrieved and injected into context as needed |

**Context management is active work.** As a task evolves, the agent (or system) must:

- Compress or summarize old context to make room
- Drop irrelevant context
- Pull in new context from short/long-term memory when needed

Agents build context-based memory through interactions with users and other agents — the richer the context, the better the agent understands available tools and the task goal.

### Agent patterns

Three common patterns, ordered from simplest to most complex:

**1. Simple single agent**
- One agent, a set of instructions, some tools, connected to a model.
- No loops, no sub-agents.
- Best for: clearly defined tasks, getting started, learning agentic behavior.

**2. Sub-agent pattern**
- Main agent handles most tasks; offloads specialized work to a sub-agent.
- Key detail: context passed to the sub-agent is *selective* — only what's needed for that task.
- Example: a general worker agent routes invoice documents to a specialized extraction agent, then moves the result to the next pipeline step.

**3. Orchestrator / router pattern**
- The starting agent acts as a **router** — it interprets intent and forwards the request to whichever downstream agent is best suited to handle it.
- Routing is harder than it looks: it must be fast and accurately identify user/agent intent to connect them to the right specialist.
- This is the same pattern as the multi-agent refund workflow in [[gcloud-agents-core-capabilities]] — orchestrator → verification agent → fulfillment agent.

## Quotes worth keeping

> "Context, just like when you're working on a task, requires active management. You want to think about updating the window as a task evolves — compressing context, summarizing context, throwing context out if it's not relevant, or using other memory pieces to bring more context in."

> "MCP is kind of like an API except it provides additional instructions about how an API is actually used and what the meaning of the inputs and outputs are."

## Open questions

- Does Google Cloud's Agent Builder / Vertex AI use MCP natively, or is it abstracted away?
- How does long-term memory get populated and retrieved — is this RAG over a vector store, or something specific to the platform?
- Are there more agent patterns beyond these three covered later in the course?

## Related sources

- [[gcloud-agents-intro]] — foundational observe→tools→act definition; this lesson explains *how* to build that loop
- [[gcloud-agents-core-capabilities]] — the three capabilities this architecture implements; multi-agent refund workflow is the orchestrator pattern in practice
- [[devagentfun-m1-l1]] — the five characteristics that emerge when all three building blocks are present and working together
