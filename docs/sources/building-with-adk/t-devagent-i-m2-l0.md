# Defining Your Agent's Identity

> **Source:** T-DEVAGENT-I-m2-l0-en-file-2.en.pdf
> **Added:** 2026-05-29
> **Tags:** adk, google-cloud, agent-identity, llm-agent, multi-agent, instructions, python
> **Type:** documentation

## Summary

Deep-dive into the four `Agent()` parameters — `model`, `name`, `description`, `instruction` — explaining what each does, when to use it, and how they interact. The critical insight: `description` is read by *other* agents for routing decisions; `instruction` is read by *this* agent to govern its own behaviour. Also explains the `root_agent` naming convention required by ADK's CLI tools.

## Key points

- `model` and `name` were required per the PDF; ADK 1.0 GA made `model` optional with a default fallback. `name` is still required.
- `description` and `instruction` are optional but practically essential.
- `description` audience = other agents ("should I delegate here?"); `instruction` audience = this agent ("how do I behave?").
- ADK CLI tools (`adk web`, `adk run`) look for a Python variable named exactly `root_agent` as the entry point — this is separate from the internal `name` parameter.
- The internal `name` and the variable name `root_agent` can differ; use `root_agent = my_specialized_agent` to assign any agent as the entry point.
- Instruction tips: be specific, use markdown for complex instructions, include few-shot examples for output format, explain *when and why* to use tools (not just list them).

## Notes

### The four core parameters

```python
from google.adk.agents.llm_agent import Agent  # LlmAgent is an alias

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant agent.',
    instruction='You are a helpful assistant.'
)
```

#### 1. `model` (optional as of ADK v1.22.0 — was required in earlier versions)

The LLM that powers the agent's reasoning. Determines intelligence, cost, and speed. ADK v1.22.0 made this optional; the PDF described it as required.

Default resolution hierarchy when `model` is omitted:
1. Inherit from ancestor agent (in multi-agent hierarchies)
2. Fall back to system default: **`gemini-2.5-flash`**

Override the system default globally: `LlmAgent.set_default_model('gemini-2.5-pro')`

```python
model='gemini-2.5-flash'
```

**Key models**

- `gemini-2.5-flash` — fast, efficient, good for most tasks
- `gemini-2.5-pro` — more capable, better for complex reasoning

> "Like choosing the engine for your car — more powerful engines handle more complex tasks but may cost more."

#### 2. `name` (required)

Unique string identifier used internally by ADK for logging, debugging, and agent delegation.

```python
name='root_agent'
```

**Naming conventions**

- Use lowercase with underscores: `customer_support_agent`
- Be descriptive: `data_analysis_agent`, `math_tutor_agent`
- Avoid reserved names: don't use `user`
- Don't use camelCase: use `my_agent` not `myAgent`

> "This name is crucial for internal operations, especially in multi-agent systems, where agents need to refer to or delegate tasks to each other."

#### 3. `description` (optional — recommended for multi-agent)

A concise summary used by *other agents* to decide whether to route a task here. Not read by the agent itself.

```python
description='Answers user questions about the capital city of a given country.'
```

**Good descriptions**

- `"Handles customer billing inquiries and processes payment updates"`
- `"Analyzes sales data and generates weekly performance reports"`

**Bad descriptions**

- `"Billing agent"` (too vague)
- `"Helper"` (not specific enough)

> "This description is primarily used by other LLM agents to determine if they should route a task to this agent. Make it specific enough to differentiate it from peers."

#### 4. `instruction` (critical but optional)

The behavioral blueprint for *this* agent — defines its personality, task, constraints, and how to use tools.

```python
instruction="""You are a helpful assistant that tells the current time in cities.
Use the 'get_current_time' tool for this purpose."""
```

**What it controls**

- Personality and communication style
- Core task or goal
- Boundaries and constraints on behaviour
- When and how to use tools
- Output format

> "The instruction parameter is arguably the most critical for shaping an LlmAgent's behavior. It tells the agent its core task or goal, its personality or persona, constraints on its behavior, and how and when to use its tools."

**Tips for effective instructions**

- **Be specific** — avoid ambiguity; state desired actions and outcomes clearly
- **Use markdown** — headings and lists improve readability for complex instructions
- **Provide examples (few-shot)** — for complex tasks or specific output formats
- **Guide tool use** — don't just list tools; explain *when and why* to use them

### `description` vs `instruction` — the key difference

| Parameter | Audience | Question it answers | Example |
|---|---|---|---|
| `description` | Other agents | "Should I route this task here?" | `"Handles billing inquiries"` |
| `instruction` | This agent | "How should I behave?" | `"You are a billing expert who…"` |

Concrete multi-agent example:

```python
# Multi-agent system with 3 agents
billing_agent = Agent(
    model='gemini-2.5-flash',
    name='billing_agent',
    # OTHER agents read this to decide if they should delegate here
    description='Handles customer billing inquiries and payment processing',
    # THIS agent reads this to know how to behave
    instruction="""You are a billing specialist.

    When helping customers:
    1. Be empathetic and patient
    2. Explain charges clearly
    3. Use the billing_lookup tool to check account details
    4. Never promise refunds without manager approval

    Always maintain a professional, helpful tone."""
)

support_agent = Agent(
    model='gemini-2.5-flash',
    name='support_agent',
    description='Handles general customer support questions',
    instruction="""You are a customer support agent.

    If a question is about billing, transfer to the billing_agent.
    Otherwise, help the customer directly."""
)
```

In this example: `support_agent` reads `billing_agent`'s `description` to decide "is this a billing question?" — then `billing_agent` reads its own `instruction` to know how to handle it.

### The `root_agent` naming convention

ADK CLI tools (`adk web`, `adk run`, `adk api_server`) look for a Python variable named exactly `root_agent` as the entry point to your agent system. This is separate from the internal `name` parameter inside `Agent()`.

```python
# Internal ADK name (used for logging, delegation)
my_specialized_agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor_agent',  # Used by ADK internally
    description='Helps students with algebra',
    instruction='You are a patient math tutor...'
)

# Variable name that ADK tools look for (must be root_agent)
root_agent = my_specialized_agent
```

> "The agent.py file contains a root_agent definition, which is the only required element of an ADK agent."

**Key rule:** always assign your main agent to a variable named `root_agent` so ADK tools can find it. The internal `name` can be anything.

### Writing effective instructions (basic)

For getting started, a simple one-liner is enough:

```python
instruction="You are a patient math tutor. Help students with algebra problems."
```

This covers: role (math tutor), personality trait (patient), task (help with algebra). Advanced patterns — multi-section structures, persona/boundary definitions, few-shot examples, production-ready templates — are covered in course 3.

### Additional parameters (not covered in PDF — current ADK docs)

The PDF covers the four identity parameters. The full `LlmAgent` class has more:

| Parameter | Purpose |
|---|---|
| `tools` | List of capabilities the agent can invoke (covered in module 3) |
| `generate_content_config` | Controls temperature, `max_output_tokens`, `top_p`, `top_k`, and safety settings |
| `planner` | Enables multi-step reasoning — `BuiltInPlanner` (Gemini thinking) or `PlanReActPlanner` |
| `code_executor` | Allows the agent to execute code blocks produced in LLM responses |
| `output_schema` | Desired output format/structure |
| `output_key` | State dictionary key for storing the agent's final response |
| `include_contents` | Whether to send conversation history to the model — `'default'` or `'none'` |

**ADK 1.0 GA additions (Google Cloud Next 2026)**

- TypeScript is now a 4th supported language (alongside Python, Go, Java)
- Event Compaction: sliding window of recent events + summary of older ones — up to 38% token reduction, 18% latency improvement
- `PROGRESSIVE_SSE_STREAMING` enabled by default

**ADK 2.0 (May 2026) — current release v2.1.0**

- `BaseAgent` now subclasses `BaseNode` — agents are nodes in a Workflow graph engine; custom `_run_async_impl()` overrides are bypassed
- Event schema: new `node_info` and `output` fields — custom DB-backed session storage needs schema migration (JSON blob storage unaffected)
- Never manually append to `context.session.events` — breaks graph determinism
- Avoid broad `except Exception:` in tools — disables automatic retries; `except BaseException:` breaks HITL
- The four `Agent()` parameters (`model`, `name`, `description`, `instruction`) are unchanged

## Open questions

- Can `root_agent` be overridden via CLI flag, or must it always be that exact variable name?
- Does `description` need to be present for the ADK routing mechanism to work, or does the orchestrator fall back to `name`?
- What happens if two agents in the same system have the same `name`?

## Related sources

- [[t-devagent-i-m1-l1]] — set up the environment and created the default agent; this lesson explains what those parameters actually mean
- [[gcloud-agents-adk-intro]] — ADK's multi-agent architecture pillar; `description` is the mechanism by which delegation works
- [[devagentfun-m2-l0]] — three-component architecture; `model` maps to Model component, `instruction` + `description` shape the Orchestration component's behaviour
- [[devagentfun-m2-l1]] — the agent loop and tool types; `instruction` is where you guide when/how to invoke tools
