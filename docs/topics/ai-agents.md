# AI Agents

Cross-source synthesis on what AI agents are, how they work, and what makes them different from simpler systems.

## Sources

- [[gcloud-agents-intro]] — defines what an agent is; the autonomous action vs. chatbot distinction
- [[gcloud-agents-core-capabilities]] — the three core capabilities + multi-agent collaboration + chatbot comparison
- [[gcloud-agents-architecture]] — technical deep-dive: model + tools + memory building blocks; agent patterns
- [[devagentfun-m1-l0]] — LLM → function calling → agent evolution; the knowing-doing gap
- [[devagentfun-m1-l1]] — five defining characteristics of a true agent; Google whitepaper definition; paradigm shift framing
- [[devagentfun-m2-l0]] — why you need the architecture (brittle code without it); maps three components to five characteristics; introduces "orchestration" vs. "memory" divergence
- [[devagentfun-m2-l1]] — deep-dive on each component; defines the agent loop (Perceive → Think → Act → Check); three tool types; reasoning frameworks; full Paris booking walkthrough
- [[devagentfun-m3-l0]] — over- vs. under-engineering failure modes; frames the "when to use" question
- [[devagentfun-m3-l1]] — decision framework: four agent-shaped problem signals, three trigger types, five anti-patterns, decision tree
- [[devagentfun-m4-l0]] — course wrap-up; "trusted employees" analogy; restaurant model for architecture; quick reference card
- [[gcloud-agents-enterprise-use-cases]] — six enterprise agent categories (customer, employee, creative, data, code, security); KPI alignment framing; Zebra Technologies case study
- [[gcloud-agents-building]] — Google Cloud's three-tier product stack for building agents; ADK outerloop vs. Gemini API inner-loop distinction; Agent Engine as managed runtime
- [[gemini-enterprise-intro]] — deep-dive into Gemini Enterprise internals: four agent types (Google-built, no-code, high-code, third-party), functional taxonomy, orchestrator-hub workflow
- [[geaplab-create-app]] — hands-on walkthrough: app creation, data store connection, pre-built agents (Idea Generation, Deep Research), NotebookLM Studio
- [[gcloud-agents-adk-intro]] — ADK deep-dive: three pillars (precision & control, dev experience, open ecosystem), workflow agent types, A2A protocol, built-in evaluation with trajectory
- [[t-devagent-i-m2-l0]] — four Agent() parameters in depth; description vs instruction distinction; root_agent convention

## What is an AI agent?

An AI agent is a software system that uses AI (typically an LLM) to **autonomously achieve a specific goal** on behalf of a user — not just respond to queries, but pursue goals. The key differentiator from a chatbot or LLM with tools is *autonomy*: agents independently set sub-goals and carry them out without step-by-step human direction.

Google's agent whitepaper puts it this way:
> "A generative AI agent can be defined as an application that attempts to achieve a goal by observing the world and acting upon it using the tools that it has at its disposal. Agents are autonomous and can act independently of human intervention, especially when provided with proper goals or objectives they are meant to achieve. Agents can also be proactive in their approach to reaching their goals."

Core structure (consistent across multiple sources):
> **Observe** the world → use **tools** to interact → **act** autonomously to accomplish a goal

Concrete examples across sources: customer service (order status, returns, callbacks), productivity scheduling, smart pantry reordering, travel planning, software development, expense processing.

**Three-tier analogy** ([[devagentfun-m4-l0]]) — the most intuitive framing for non-technical audiences:

| Tier | Analogy | What it can do |
|---|---|---|
| LLM API | Consultant | Gives advice; can't implement |
| LLM + function calling | Assistant with tools | Uses tools when told |
| AI Agent | **Trusted employee** | Given a goal — figures out the rest |

## The evolution that led here

Agents didn't appear out of nowhere — they're the third step in a progression ([[devagentfun-m1-l0]]):

| Stage | Technology | Capability | Limitation |
|---|---|---|---|
| 1 | LLM API | Text generation, advice | Frozen in time; no external access |
| 2 | LLM + Function Calling | Can call APIs, use tools | You still orchestrate every step |
| 3 | AI Agent | Pursues goals autonomously | — |

`Stage 1 + Functions = Stage 2` · `Stage 2 + Autonomy = Stage 3`

The gap function calling couldn't close: booking a trip still meant manually coordinating every function call (search flights → check availability → compare prices → book → find hotels…). The model got better at steps; the human was still the planner. Agents close that gap.

## Two lenses on what makes an agent

Different sources frame agent capabilities differently — both are useful:

### Lens 1 — Three core capabilities (gcloud course)

| Capability | What it means |
|---|---|
| **Autonomous action** | Executes complex, multi-step workflows without a human prompt at each step |
| **Reasoning and planning** | Uses AI models to decide what to do next and adapt to changing conditions |
| **Continuous learning** | Improves from experience over time, unlike static rule-based systems |

### Lens 2 — Five defining characteristics (Google whitepaper / devagentfun)

All five must be present for a true agent — not everything using an LLM and tools qualifies:

| # | Characteristic | What it means |
|---|---|---|
| 1 | **Goal-directed** | Works toward objectives; understands current vs. desired state and acts to close the gap |
| 2 | **Autonomous** | Acts independently once given a goal; no explicit per-step instruction needed |
| 3 | **Proactive** | Takes initiative even without explicit instruction sets |
| 4 | **Environmentally aware** | Perceives and continuously updates a model of the world from inputs (API responses, DB states, errors) |
| 5 | **Tool-using** | Interacts with external systems beyond text generation |

The two lenses overlap substantially — "autonomous action" maps to characteristics 2 and 3; "reasoning and planning" maps to 1 and 4 — but the five-characteristic framework is more precise for diagnosing whether a system is truly agentic.

## Why agents > chatbots

Chatbots are reactive: fixed scripts, single data source, escalate on anything complex.
Agents are proactive: goal-driven, multi-system access, chain actions to resolve.

> "The biggest distinction between a traditional chatbot and an agentic system is the ability to act autonomously across multiple systems to resolve a complex issue." — [[gcloud-agents-core-capabilities]]

| | Chatbot | Agent |
|---|---|---|
| **Behavior** | Reactive, script-bound | Autonomous, goal-driven |
| **Data access** | Single source | Multiple systems |
| **Complex tasks** | Fails → escalates to human | Chains actions → resolves |
| **Adaptability** | Fixed responses | Adapts to context |

## Multi-agent collaboration

Single agents hit a ceiling on very large or complex goals. Multi-agent systems:
- Divide tasks by specialization (orchestrator, verification, fulfillment agents)
- Share knowledge across agents
- Chain actions to accomplish what no solo agent could

**Example — autonomous refund processing:**
```
Customer: complex refund request (multiple payment sources)
  → Orchestrator agent
  → Verification agent (policy check + order lookup)
  → Fulfillment agent (payment processing + confirmation email)
```

## Technical building blocks

Two sources cover the same three-component architecture from different angles:

**[[gcloud-agents-architecture]]** frames the components as: model + tools + **memory**
**[[devagentfun-m2-l0]]** frames them as: model + tools + **orchestration** (citing the Google whitepaper)

These aren't contradictory — they zoom into different aspects of the third component. Memory (what the agent retains across a task) is arguably part of orchestration (the process loop that manages what context the model sees at each step).

| Component | Role | gcloud term | devagentfun term |
|---|---|---|---|
| **Model** | Intelligence; thinking models self-reflect before responding | model | model |
| **Tools / MCP** | Interact with the world; MCP adds semantic context to APIs | tools | tools |
| **Memory / Orchestration** | Context across interactions + the loop connecting model to tool use | memory | orchestration |

**[[devagentfun-m2-l0]]** also maps each component to the five characteristics:
- Model → autonomous operation (2) + environmental awareness (4)
- Tools → tool use (5)
- Orchestration → goal-directed behavior (1) + proactive initiative (3)

### Why the architecture matters: the brittle code problem

Without all three components working as a unified system, building intelligent behavior means writing if-then-else code for every possible task variation. The scheduling example ([[devagentfun-m2-l0]]): "Schedule a meeting with Sarah next week" requires 6 coordinated steps, each with failure paths. Without orchestration, you hardcode logic for every variant — thousands of lines that break on any deviation. The three-component architecture replaces brittle code with flexible, intelligent behavior.

### The agent loop (orchestration in detail)

Orchestration is not abstract — it is a specific loop ([[devagentfun-m2-l1]]):

```
Perceive → Think → Act → Check → (repeat until goal achieved)
```

| Step | What happens |
|---|---|
| **Perceive** | Takes in current state: user input, tool results, errors |
| **Think** | Reasons about next action; uses a framework (ReAct, chain-of-thought, tree-of-thoughts) |
| **Act** | Invokes a tool, asks a clarifying question, or produces output |
| **Check** | Is the goal achieved? If not, loop again |

The loop maps directly back to the five characteristics: Perceive = environmental awareness (4), Think = goal-directed (1), Act = tool use (5) + autonomous operation (2), Check = goal-directed (verifying goal state).

**Reasoning frameworks** (ReAct, chain-of-thought, tree-of-thoughts) shape how the Think step works — different strategies for deciding what to do next, all sitting inside the same outer Perceive → Think → Act → Check loop.

### Tool types

Three categories of tools ([[devagentfun-m2-l1]]):

| Type | Role |
|---|---|
| **Pre-built integrations** | Connect to external services (Google Flights, weather APIs); hides API details |
| **Custom functions** | Delegate to your existing application code; agent prepares the request, your app executes (enables human approval gates) |
| **Information retrieval** | Accesses knowledge beyond training data — company docs, customer histories, product catalogs |

Power comes from **chaining** these across loop iterations, not from any single tool.

## Enterprise agent categories

[[gcloud-agents-enterprise-use-cases]] organizes agents by the business function they serve — a different taxonomy from the use-case examples in [[gcloud-agents-intro]]:

| Category | Business function |
|---|---|
| **Customer** | Customer-facing interactions (service, sales, support) |
| **Employee** | Internal workforce productivity and assistance |
| **Creative** | Content generation and creative work |
| **Data** | Analysis, intelligence, reporting |
| **Code** | Software development and engineering |
| **Security** | Threat detection, incident response |

> ⚠️ Individual category descriptions not fully captured — lesson uses interactive cards. Only names confirmed.

Each category should map to specific KPIs. Agents that can't be tied to a measurable business outcome are delivering a demo, not value.

## Building agents on Google Cloud

([[gcloud-agents-building]]) Google Cloud organizes agent development into three tiers, primarily by *who is building* and *how much control they need*:

| Tier | Product | Primary user | Best for |
|---|---|---|---|
| **SaaS / off-the-shelf** | Gemini Enterprise | Any user | Employee productivity; pre-built + custom agents with enterprise connectors and knowledge graph |
| **No-code / low-code** | Conversational Agents | Business users | Customer-facing voice/chat bots; structured multi-turn conversations; mix deterministic flows + LLM |
| **Developer platform** | Vertex AI Agent Builder | Developers | Customized agents; code-defined logic; complex multi-agent systems |

An enterprise governance layer (security, compliance, policy enforcement) cuts across all three tiers.

### Gemini Enterprise internals

([[gemini-enterprise-intro]]) Gemini Enterprise is not just a chat interface — it's a hub combining Gemini reasoning + Google Search + enterprise data. Four agent types are available within it:

| Type | Who builds | Notes |
|---|---|---|
| **Google-built** | Google | Gemini LLM (broad tasks), Search (retrieval), NotebookLM (research on user-provided sources) |
| **No-code** | Business users | Visual tool; 4-step: define purpose → connect data → provide instructions → iterate |
| **High-code** | Developers | Full code; custom data sources, custom logic, model fine-tuning |
| **Third-party** | External partners | Pre-built connectors: Salesforce, Jira, SharePoint, Microsoft Copilot; **source-system ACLs are respected** |

The ACL point is notable: third-party integration does not create a permission bypass — if a user can't see a document in the source system, the agent won't surface it either.

Gemini Enterprise's internal workflow matches the orchestrator pattern from [[gcloud-agents-architecture]]: prompt → orchestrate internal capabilities + custom agents → connect to data & fulfillment systems → actionable response.

### Vertex AI Agent Builder decomposed

The developer platform has four components that map onto the agent architecture from [[gcloud-agents-architecture]] and [[devagentfun-m2-l1]]:

| Component | Role | Maps to |
|---|---|---|
| **ADK** | Open-source framework; "outerloop" orchestration — multi-step reasoning and tool invocation | Orchestration component; Perceive → Think → Act → Check loop |
| **Agent Garden** | Pre-built tools and integrations | Tools component |
| **Agent Engine** | Managed runtime: monitoring, trace logging, long-term memory, session management, Example Store, Agentic Autorater | Runtime/memory |
| **Gemini API** | "Inner-loop" tools built into the model: code interpreter, search, multimodal reasoning | Model capabilities + pre-built integrations |

**Outerloop vs. inner-loop** is a new framing introduced here. The outer loop is the orchestration cycle across a whole task (what ADK manages). The inner loop is what happens within a single model invocation — the model's own built-in tool use (code interpreter, search). Both feed into the same Perceive → Think → Act → Check loop, but operate at different levels of granularity.

## When to use agents (and when not to)

From [[devagentfun-m3-l1]]. Four signals of an agent-shaped problem:

| Signal | What it means |
|---|---|
| **Goal-oriented** | Task has an objective to reach, not just a question to answer |
| **Multi-step + external actions** | Sequence of dependent steps, each interacting with external systems |
| **Adaptive** | Approach must change based on what the agent discovers mid-task |
| **Multi-system** | Spans multiple systems — no single API covers it |

### Trigger types where agents shine

| Trigger | Example |
|---|---|
| **Event-triggered** | Production error → agent analyzes logs, checks deployments, routes to on-call, rolls back if criteria met |
| **Chat-triggered** | "Competitive analysis of top 3 competitors" → agent researches, synthesizes, produces report with citations |
| **Time-triggered** | Daily 8 AM briefing → agent pulls metrics, identifies anomalies, sends personalized summaries |

### Anti-patterns — when to skip agents

| Situation | Use instead |
|---|---|
| Simple Q&A ("What's your return policy?") | Retrieval system / FAQ |
| Single API call ("Get today's weather") | Direct function calling |
| High-volume, low-complexity (10k identical ops) | Traditional automation |
| Deterministic workflow (pure if-then rules) | Workflow automation |
| Real-time / latency-sensitive (trading, safety) | Specialized fast systems |

### Decision tree

1. Multiple dependent steps? → if no: **use simple API or LLM**
2. Needs adaptation? → if no: **use workflow automation**
3. Needs reasoning + external actions? → if yes: **use agent**

## Agent patterns

| Pattern | Description | Best for |
|---|---|---|
| **Simple single agent** | One agent, instructions, tools, model — no loops | Clear tasks, getting started |
| **Sub-agent** | Main agent offloads specialized work to a dedicated sub-agent | Specialized subtasks in a pipeline |
| **Orchestrator / router** | Starting agent routes requests to the best downstream agent | Complex intent-routing across specialists |

## The paradigm shift

| From | To |
|---|---|
| Reactive | Proactive — agents pursue goals |
| Isolated | Integrated — context and state across interactions |
| Advisory | Executive — agents don't tell you what to do, they do it |
| Static | Adaptive — agents adjust based on what they learn |

## Open questions (to resolve with later sources)

- How does "continuous learning" work in practice — fine-tuning, RAG, or something else?
- Does ADK use MCP natively, or is it abstracted behind Agent Garden?
- How is long-term memory in Agent Engine populated and retrieved — RAG over vector store?
- What does the Agentic Autorater use for evaluation — LLM-as-judge, golden set, or both?
- ~~At what point does function calling become an agent?~~ Answered ([[devagentfun-m3-l1]]): single-step + no adaptation = use function calling; multi-step + adaptive = agent.
- ~~Does orchestration have a precise definition?~~ Answered ([[devagentfun-m2-l1]]): it's the agent loop — Perceive → Think → Act → Check.
