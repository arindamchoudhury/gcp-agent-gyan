# Developing Agents with Google Cloud

> **Source:** [Google Cloud Training — T-GCAGNT-B v1.0.0](https://storage.googleapis.com/cloud-training/cls-html5-courses/T-GCAGNT-B/v1.0.0/index.html#/lessons/NktkaVfRteX2wRKH_AgOqjLTPW2pUbxm)
> **Added:** 2026-05-28
> **Tags:** ai-agents, google-cloud, vertex-ai, adk, agent-engine, gemini, platforms
> **Type:** documentation

> 📌 **Platform rename (2026):** Vertex AI was rebranded to **Gemini Enterprise Agent Platform** at Google Cloud Next 2026. References to "Vertex AI Agent Builder" in this note reflect the terminology used in the source material (v1.0.0, 2026-05-28). Features still exist, reorganised under a "Models" sub-menu. SDK migration deadline: June 24, 2026.

## Summary

Maps Google Cloud's agent development landscape to a three-tier stack: off-the-shelf SaaS agents for business users (Gemini Enterprise), no-code/low-code tools for customer-facing bots (Conversational Agents), and a full developer platform for custom agents (Vertex AI Agent Builder). The choice between them is primarily a function of who is building and how much control they need. An enterprise governance layer applies across all tiers.

## Key points

- Three distinct tiers: SaaS → no-code/low-code → developer platform. The right choice depends on who is building and how much control is needed.
- **Vertex AI Agent Builder** is the developer platform: ADK (outerloop orchestration) + Agent Engine (managed runtime) + Gemini API (inner-loop tools).
- **ADK** is open source and open-runtime, designed for complex multi-agent systems. Explicitly described as providing "outerloop" orchestration — distinct from the Gemini API's "inner-loop" tools (code interpreter, search).
- **Agent Engine** is the managed runtime for deployment: handles monitoring, trace logging, long-term memory, session management, few-shot examples (Example Store), and quality evaluation (Agentic Autorater).
- Enterprise governance applies at every tier — all agents are subject to security, reliability, and compliance controls regardless of how they were built.

## Notes

### The three-tier stack

Google's agent offerings are organized by user and complexity:

| Tier | Product | User | Best for |
|---|---|---|---|
| **SaaS / off-the-shelf** | Gemini Enterprise | Any user | Employee productivity, internal chat/search; pre-built + custom agents with connectors and knowledge graph |
| **No-code / low-code** | Conversational Agents (Customer Engagement Suite) | Business users | Customer service voice/chat bots; structured multi-turn conversations; deterministic flows + LLM mix |
| **Developer platform** | Vertex AI Agent Builder | Developers | Customized agents, full control over logic; code-first, complex multi-agent systems |

A fourth cross-cutting concern — **Enterprise governance** — applies to all tiers: policy enforcement, security, reliability, compliance.

### Vertex AI Agent Builder in detail

The developer platform has four components:

| Component | Role |
|---|---|
| **ADK (Agent Development Kit)** | Open-source, code-first framework; handles "outerloop" orchestration — how agents reason over multiple steps and call tools |
| **Agent Garden** | Pre-built tools and integrations accessible to ADK agents |
| **Agent Engine** | Fully managed runtime for deployment; provides monitoring, trace logging, long-term memory, session management, Example Store (few-shot examples), Agentic Autorater (quality eval) |
| **Gemini API** | Core model access; "inner-loop" tools built in — code interpreter, search, multimodal reasoning — all optimized for agentic planning |

**Outerloop vs. inner-loop:** ADK provides the outerloop (the orchestration cycle connecting model decisions to multi-step tool use). The Gemini API provides inner-loop tools (capabilities the model invokes within a single reasoning step). This maps onto the agent loop from [[devagentfun-m2-l1]] — outerloop ≈ Perceive → Think → Act → Check; inner-loop ≈ tools invoked within the Act step.

### Platform selection guidance

- **Gemini Enterprise**: simplest entry point; best for internal productivity agents, no-code chat/search
- **Conversational Agents**: customer-facing; structured conversation design with CI/CD tooling
- **Vertex AI Agent Builder**: when you need to write code defining agent logic; most control

### Knowledge check — product definitions (all 4 cards)

The lesson's flip-card quiz gives the most concise official definitions for each product:

| Product | Definition |
|---|---|
| **Gemini Enterprise** | No-code UI and centralized hub for discovering, creating, and running AI Agents focused on internal employee productivity |
| **ADK** | Code-first, open-source framework that simplifies end-to-end development of complex, multi-agent systems with full programmatic control via a Python SDK |
| **Vertex AI Agent Builder** | Comprehensive platform for grounding agents to enterprise data, managing their lifecycle, and deploying them to a fully managed runtime (Agent Engine) |
| **Conversational Agents** | For building customer-facing AI applications (voice/chat bots) using a reliable, visual state-machine flow model to manage and direct conversations |

Two details not surfaced earlier: ADK uses a **Python SDK** specifically; Conversational Agents uses a **visual state-machine flow model** for conversation control (not just "deterministic flows").

### Also mentioned

- **Genkit** — Google's framework for building any AI application (not just agents), also open source
- **Gemini Code Assist, Jules, Firebase Studio** — developer acceleration tools in the ecosystem
- Multi-agent systems are specifically supported through ADK

## Quotes worth keeping

> "ADK is built on a foundation of open source, open tools, open LLM, and open runtime."

> "The best agent platform for your project depends primarily on who is building it and the required level of control and complexity."

## Open questions

- What exactly is in Agent Garden? What categories of pre-built tools?
- How does Example Store differ from RAG-based memory? Is it few-shot only, or also long-form context?
- How does Agentic Autorater evaluate agent quality — LLM-as-judge, golden set, or both?
- What does "grounding agents to enterprise data" mean in practice — RAG, vector search, connectors?

## Related sources

- [[gcloud-agents-enterprise-use-cases]] — defines the *business categories* for agents (customer, employee, creative…); this lesson defines the *platform layer* for building them
- [[gcloud-agents-architecture]] — covers model + tools + memory as the three architectural components; ADK's "outerloop" maps directly to the orchestration component, Gemini API's "inner-loop" tools map to the tools component
- [[devagentfun-m2-l1]] — describes the agent loop (Perceive → Think → Act → Check) and three tool types; ADK provides that loop at the platform level; Gemini API's built-in tools are the "pre-built integrations" category
- [[gcloud-agents-intro]] — introduced Google Cloud as an agent platform generally; this lesson provides the specific product breakdown
