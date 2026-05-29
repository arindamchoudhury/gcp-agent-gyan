# Course Wrap-Up: Foundations of AI Agents

> **Source:** T-DEVAGENTFUN-I-m4-l0-en-file-7.en.pdf
> **Added:** 2026-05-26
> **Tags:** ai-agents, agent-design, mental-models, quick-reference
> **Type:** documentation

## Summary

Course conclusion for the devagentfun foundational module. No new technical concepts — value here is in the compact mental models and analogies that synthesize all prior material. The "trusted employees" analogy and the restaurant model are the two framings worth keeping that don't appear in earlier notes.

## Key points

- **Trusted employees analogy**: LLMs = consultants (advise but don't implement); LLMs + functions = assistants with tools (use tools when told); Agents = trusted employees (give them goals, they figure it out).
- **Restaurant model**: model = cook (knows recipes, makes decisions); tools = kitchen equipment (actually does the work); orchestration = process (order → plan → cook → serve).
- Quick reference card condenses all course learning into a single reference — see below.

## Notes

### The three analogies

A progression that maps to [[devagentfun-m1-l0]]'s three evolutionary stages:

| Stage | Analogy | Capability |
|---|---|---|
| LLM API | **Consultant** | Gives advice; can't implement |
| LLM + function calling | **Assistant with tools** | Can use tools when explicitly told |
| AI Agent | **Trusted employee** | Given a goal; figures out the rest independently |

The "trusted employee" framing is the most intuitive way to convey what agents are to a non-technical audience — you hand them a goal, not a task list.

### The restaurant model (new metaphor for the architecture)

A concrete analogy for [[devagentfun-m2-l0]]'s three-component architecture:

- **Model = Cook** — knows the recipes, makes the decisions about how to prepare
- **Tools = Kitchen equipment** — actually executes the cooking; nothing gets done without them
- **Orchestration = Process** — the flow: take order → plan the meal → cook → serve

Like the car analogy (engine/wheels/steering), the restaurant model emphasizes that all three are required — a cook without equipment can't serve food; equipment without a cook sits idle.

### Quick reference card

**What is an agent?** An autonomous system that achieves goals by observing and acting in its environment.

**Agent equation:** agent = model + tools + orchestration

**Agent loop:** Perceive → Think → Act → Check → repeat until done

**Use agents when:** multi-step workflows, adaptation required, reasoning required, external actions needed

**Don't use agents when:** simple single operations, deterministic workflows, real-time requirements, simple Q&A

**Tool types:** pre-built integrations, custom functions, information retrieval

### Key takeaways (course-level)

1. Agents ≠ chatbots — agents are autonomous systems that can perceive, reason, and act
2. Architecture matters — model + tools + orchestration working together creates the behavior
3. Tools = superpowers — without tools, even the smartest model can only generate text
4. Not everything needs an agent — sometimes simple automation is correct
5. Autonomy is the key — goal-directed autonomous behavior is the defining feature

### Additional resources mentioned

The PDF cites five resources for further learning (URLs not included in the PDF — titles only):

- "Intro to AI Agents" — Google; deep dive on definitions, capabilities, use cases, architectural approaches
- "Workflows versus agents" — how agentic workflows differ from traditional ones
- "The Agent Factory – Episode 1: Agents" — what makes a true agent; Agent Developer Kit
- "Conversational versus non-conversational AI Agents" — multi-turn interactions, prompt templates
- "From gen AI to agentic AI: Everything you need to know – Part 1 and Part 2" — Google two-part series

## Related sources

- [[devagentfun-m1-l0]] — the three evolutionary stages that map to the three analogies here
- [[devagentfun-m2-l0]] — three-component architecture that the restaurant model and agent equation summarize
- [[devagentfun-m3-l1]] — the decision framework condensed into the quick reference card
