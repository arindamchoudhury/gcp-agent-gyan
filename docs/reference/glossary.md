# Glossary

| Term | Definition | Source |
|---|---|---|
| AI Agent | A software system that uses AI (typically an LLM) to autonomously achieve a specific goal; distinguished from chatbots by its capacity for independent goal-setting and action | [[gcloud-agents-intro]] |
| Autonomous action | The ability of an agent to independently set sub-goals and carry them out within a defined environment, without needing step-by-step human direction | [[gcloud-agents-intro]], [[gcloud-agents-core-capabilities]] |
| Reasoning and planning | An agent's use of advanced AI models to make informed decisions and adapt dynamically to changing environments | [[gcloud-agents-core-capabilities]] |
| Continuous learning | An agent's ability to learn from experience and improve performance over time, beyond static rule-based systems | [[gcloud-agents-core-capabilities]] |
| Multi-agent collaboration | A pattern where multiple specialized agents share knowledge, divide complex tasks, and coordinate actions to achieve goals no single agent could manage alone | [[gcloud-agents-core-capabilities]] |
| Orchestrator agent | In a multi-agent system, the agent that receives the top-level task and delegates sub-tasks to specialized agents | [[gcloud-agents-core-capabilities]], [[gcloud-agents-architecture]] |
| Thinking model | An AI model with built-in self-reflection ability — it considers a set of ideas before producing a final response; suited for complex agent tasks | [[gcloud-agents-architecture]] |
| Model Context Protocol (MCP) | A standard for giving agents access to tools; extends an API with semantic instructions about when and how to use it, so agents can decide autonomously which tool to invoke | [[gcloud-agents-architecture]] |
| Context window | An agent's active working memory — everything currently visible to the model; requires active management (compression, summarization, pruning) as tasks evolve | [[gcloud-agents-architecture]] |
| Sub-agent pattern | An agent architecture where a main agent offloads specialized or complex subtasks to a dedicated sub-agent, passing only selective context | [[gcloud-agents-architecture]] |
| Router pattern | An agent architecture where the starting agent acts as a router, interpreting intent and forwarding requests to the most appropriate downstream specialist agent | [[gcloud-agents-architecture]] |
| Knowing-doing gap | The gap between an AI that can advise on a task vs. one that can execute it; agents close this gap by adding autonomy to tool use | [[devagentfun-m1-l0]] |
| Function calling | An LLM capability allowing the model to call external APIs and functions; adds tool use but not autonomy — the human still orchestrates each step | [[devagentfun-m1-l0]] |
| Goal-directed behavior | An agent characteristic: working toward an objective by understanding the gap between current and desired state and taking actions to close it | [[devagentfun-m1-l1]] |
| Proactive initiative | An agent characteristic: actively working toward goals even without explicit instruction; reasoning about what to do next unprompted | [[devagentfun-m1-l1]] |
| Environmental awareness | An agent characteristic: perceiving and building a model of the world from inputs (API responses, DB states, user requests, errors) and updating it continuously | [[devagentfun-m1-l1]] |
| Orchestration (agent component) | The process loop that connects the model's decisions to tool invocations and back — the "steering system" of an agent. Enables goal-directed and proactive behavior. Named as the third architectural component by the Google whitepaper; [[gcloud-agents-architecture]] uses "memory" for the same slot | [[devagentfun-m2-l0]] |
| Brittle code problem | The consequence of building intelligent behavior without the three-component agent architecture: every task variation requires hardcoded if-then-else logic, resulting in code that breaks on any deviation | [[devagentfun-m2-l0]] |
| Agent loop | The cyclical process at the core of orchestration: Perceive → Think → Act → Check, repeating until the agent achieves its goal | [[devagentfun-m2-l1]] |
| ReAct | A reasoning framework where the model interleaves reasoning and acting at each Think step of the agent loop; one of several frameworks (chain-of-thought, tree-of-thoughts) that can guide agent decision-making | [[devagentfun-m2-l1]] |
| Agent-shaped problem | A problem that benefits from the agent architecture: goal-oriented, multi-step with external actions, adaptive, and spanning multiple systems | [[devagentfun-m3-l1]] |
| Event-triggered agent | An agent activated by a system event (e.g., production error) rather than a user request; acts autonomously before a human needs to ask | [[devagentfun-m3-l1]] |
| Time-triggered agent | An agent that runs on a schedule (e.g., daily briefing); produces adaptive output rather than a fixed report | [[devagentfun-m3-l1]] |
| Agentic workflow | The end-to-end process created when model, tools, orchestration, and runtime work together to accomplish a business goal; the unit of value delivery in enterprise agent deployments | [[gcloud-agents-enterprise-use-cases]] |
| ADK (Agent Development Kit) | Google Cloud's open-source, code-first framework for building complex multi-agent systems; provides "outerloop" orchestration connecting model decisions to multi-step tool use | [[gcloud-agents-building]] |
| Agent Engine | Fully managed runtime within Vertex AI Agent Builder; provides deployment infrastructure including monitoring, trace logging, long-term memory, session management, Example Store, and Agentic Autorater | [[gcloud-agents-building]] |
| Vertex AI Agent Builder | Google Cloud's developer platform for building agents: combines ADK (outerloop orchestration), Agent Garden (integrations), Agent Engine (managed runtime), and Gemini API (inner-loop tools) | [[gcloud-agents-building]] |
| Conversational Agents | Google Cloud's no-code/low-code platform for building customer-facing voice/chat AI applications; uses a visual state-machine flow model to manage conversations; part of Customer Engagement Suite | [[gcloud-agents-building]] |
| Outerloop orchestration | The multi-step reasoning and tool-invocation cycle managed by the agent framework (ADK); encompasses the full Perceive → Think → Act → Check loop across a task | [[gcloud-agents-building]] |
| Inner-loop tools | Built-in model capabilities invoked within a single reasoning step — code interpreter, search, multimodal reasoning; provided by the Gemini API, distinct from outerloop orchestration | [[gcloud-agents-building]] |
| Agentic Autorater | Agent Engine feature for automated quality assurance and performance evaluation of deployed agents | [[gcloud-agents-building]] |
| Example Store | Agent Engine feature for managing few-shot examples (small datasets that guide model behavior) | [[gcloud-agents-building]] |
| NotebookLM | Google-built agent in Gemini Enterprise for in-depth research using user-provided sources; distinct from the Search agent which retrieves from broad enterprise data | [[gemini-enterprise-intro]] |
| No-code agent | An AI agent built using a visual tool without writing code; configured through natural language instructions and connected data sources | [[gemini-enterprise-intro]] |
| High-code agent | An AI agent built with full coding capabilities; allows custom logic, integration with any system, and fine-tuning of AI models | [[gemini-enterprise-intro]] |
| Third-party agent | An agent in Gemini Enterprise that integrates with non-Google platforms (Salesforce, Jira, SharePoint, Microsoft Copilot); respects source-system ACLs | [[gemini-enterprise-intro]] |
| Idea Generation agent | Pre-built Gemini Enterprise agent that runs a team of sub-agents to plan, generate, and evaluate ideas; presents a plan for human review before executing | [[geaplab-create-app]] |
| Deep Research agent | Pre-built Gemini Enterprise agent that performs in-depth analysis and produces comprehensive reports; drafts a research plan for human review before running | [[geaplab-create-app]] |
| NotebookLM Studio | The Studio tab within NotebookLM that transforms source material into dynamic formats — audio overviews, video presentations, mind maps, reports | [[geaplab-create-app]] |
| Workforce Identity | Google Cloud identity provider configuration required to share a Gemini Enterprise app with an organization's workforce | [[geaplab-create-app]] |
| Connected data store | A data source linked to a Gemini Enterprise app; supported types include Google Drive, Google Calendar, and Google Cloud Storage (documents) | [[geaplab-create-app]] |
| Sequential agent | ADK workflow agent type that executes steps in a fixed, ordered sequence — for predictable pipelines | [[gcloud-agents-adk-intro]] |
| Parallel agent | ADK workflow agent type that executes multiple branches concurrently | [[gcloud-agents-adk-intro]] |
| Loop agent | ADK workflow agent type that repeats a step until a condition is met | [[gcloud-agents-adk-intro]] |
| LLM-driven dynamic routing | ADK orchestration mode where the LLM adapts its strategy in real-time based on incoming information, rather than following a predetermined pipeline | [[gcloud-agents-adk-intro]] |
| Execution trajectory | The reasoning path an agent took to reach its answer; evaluated separately from answer quality in ADK's built-in evaluation | [[gcloud-agents-adk-intro]] |
| A2A protocol | Agent-to-Agent protocol; enables secure, standardized communication between agents from different vendors — complements MCP (agent-to-tool) with agent-to-agent connectivity | [[gcloud-agents-adk-intro]] |
| Native streaming | ADK built-in support for bidirectional audio and video streaming; enables real-time, human-like interactions beyond text | [[gcloud-agents-adk-intro]] |
