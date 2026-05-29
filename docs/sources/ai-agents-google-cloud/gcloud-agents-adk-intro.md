# Introduction to Agent Development Kit

> **Source:** [Google Cloud Training — T-GCAGNT-B v1.0.0](https://storage.googleapis.com/cloud-training/cls-html5-courses/T-GCAGNT-B/v1.0.0/index.html#/lessons/hQUEVTc6N0Cb1bwVXdxv7Y8ucGAtxlZJ)
> **Added:** 2026-05-29
> **Tags:** ai-agents, google-cloud, adk, agent-development-kit, multi-agent, orchestration, mcp, a2a
> **Type:** documentation

## Summary

A deep dive into ADK's core features across three pillars: precision and control (flexible orchestration, multi-agent architecture, rich tooling), integrated developer experience (code-first, CLI + web UI, built-in evaluation), and open ecosystem (model flexibility, interoperability, MCP + A2A protocols, safety). Expands significantly on [[gcloud-agents-building]]'s one-row introduction to ADK.

## Key points

- ADK's orchestration has two modes: **predictable pipelines** using workflow agents (sequential, parallel, loop) and **LLM-driven dynamic routing** that adapts strategy in real-time.
- Multi-agent systems are built as hierarchies: a primary agent delegates to specialized sub-agents based on their specific roles.
- Code-first in Python, Go, or Java — not Python-only as [[gcloud-agents-building]] implied.
- Built-in evaluation covers both the *final answer quality* and the *execution trajectory* (the reasoning path taken to reach it).
- Supports the **Agent-to-Agent (A2A) protocol** alongside MCP — enables standardized communication between agents from different vendors.
- Safety patterns are built in: explicit authorization for actions, in-tool guardrails, sandboxed code execution, and network controls to prevent data exfiltration.

> ⚠️ **Partial capture:** The "Deployment options" and "Native streaming" tab content was not captured — exclusive tab behavior kept only the last-clicked tab (Safety and Security) visible during extraction.

## Notes

### Three feature pillars

ADK's features are organized into three pillars:

| Pillar | What it covers |
|---|---|
| **Precision and control** | Orchestration modes, multi-agent architecture, tool ecosystem |
| **Integrated developer experience** | Code-first design, local tooling (CLI + web UI), built-in evaluation |
| **Open ecosystem** | Model flexibility, interoperability, agent protocols, deployment, safety |

### Precision and control

**Flexible orchestration — two modes:**
- *Workflow agents*: deterministic, predictable pipelines using **sequential agents** (ordered steps), **parallel agents** (concurrent branches), and **loop agents** (repeat until condition).
- *LLM-driven dynamic routing*: the agent adapts its strategy in real-time based on incoming information — used when the path cannot be predetermined.

This maps directly onto the orchestration layer in [[gcloud-agents-architecture]] and the Perceive → Think → Act → Check loop from [[devagentfun-m2-l1]]. The workflow agent types are a practical implementation of the "deterministic sub-agent" pattern.

**Multi-agent architecture:**
Instead of one complex agent, ADK encourages a hierarchy: a primary agent delegates to specialized sub-agents based on each one's role. This matches the orchestrator/sub-agent pattern in [[gcloud-agents-core-capabilities]] and [[gcloud-agents-architecture]] — ADK provides the scaffolding to build it.

**Rich tool ecosystem:**
- Pre-built: Google Search, Code Execution
- Custom: any API or enterprise system
- Third-party: functions from libraries like LangChain
- Agents as tools: other agents can be used as tools for a modular design

### Integrated developer experience

**Code-first and modular:** agent logic, tools, and orchestration are defined directly in **Python, Go, or Java** — promotes modularity, testability, and version control. [[gcloud-agents-building]] mentioned only Python SDK; Go and Java support are additions.

**Integrated tooling:**
- CLI for running and testing agents locally
- Web-based UI for local development and debugging

**Built-in evaluation:** tests agent performance against predefined scenarios, evaluating:
1. *Final answer quality* — did the agent produce the right output?
2. *Execution trajectory* — did the agent reason through the correct steps to get there?

Trajectory evaluation is important: an agent can get the right answer through the wrong reasoning, which is a reliability risk in production.

### Open ecosystem

**Model flexibility:** a base interface allows ADK to work with various LLMs, not just Gemini.

**Interoperability:** integrates with other popular agent frameworks — ADK is not a walled garden.

**Agent communication protocols:**
- **MCP (Model Context Protocol)** — also covered in [[gcloud-agents-architecture]]; standardizes how agents access tools and context
- **A2A (Agent-to-Agent) protocol** — new here; enables secure, standardized communication *between agents from different vendors*. MCP connects agents to tools; A2A connects agents to agents across vendor boundaries.

**Safety and security patterns:**
- Explicit authorization for sensitive actions
- In-tool guardrails to restrict system access
- Sandboxed code execution
- Network controls to prevent data exfiltration

> ⚠️ **Partial capture:** Deployment options (how/where to deploy ADK agents) and Native streaming (real-time output) tab content not captured.

## Open questions

- What are ADK's supported deployment targets? (Deployment options tab not captured — likely Agent Engine + local + other GCP services)
- What does "native streaming" mean in ADK — token-level streaming, event streaming, or something else?
- How does A2A differ from simply calling another ADK agent as a tool? Is it cross-vendor or also cross-network?
- What are the limits of workflow agents vs. LLM routing — when is each preferred?

## Related sources

- [[gcloud-agents-building]] — introduced ADK as one row in the platform table; this lesson is the detailed expansion of that row
- [[gcloud-agents-architecture]] — covers MCP, orchestration, and the three agent patterns; ADK implements these at the framework level
- [[gcloud-agents-core-capabilities]] — multi-agent collaboration and orchestrator/sub-agent patterns; ADK's hierarchy model is the implementation
- [[devagentfun-m2-l1]] — the agent loop and three tool types; ADK's workflow agents are a structured implementation of the loop; its tool ecosystem maps to the three tool categories
