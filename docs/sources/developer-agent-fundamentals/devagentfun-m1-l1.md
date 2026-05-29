# The Agent Abstraction: What Makes a True Agent

> **Source:** T-DEVAGENTFUN-I-m1-l1-en-file-2.en.pdf
> **Added:** 2026-05-26
> **Tags:** ai-agents, agent-definition, autonomy, agent-characteristics, google-whitepaper
> **Type:** documentation

## Summary

Defines what separates a true agent from an LLM with tools bolted on. An agent is a fundamentally different abstraction — a system that *pursues goals* rather than responds to queries. Five characteristics must all be present: goal-directed behavior, autonomous operation, proactive initiative, environmental awareness, and tool use. The lesson illustrates all five with a weather/jacket example and identifies four categories of problems only agents can solve.

## Key points

- An agent is **not** just an LLM + tools. It's a different abstraction: a system that pursues goals.
- Five defining characteristics (all five required for a true agent): goal-directed, autonomous, proactive, environmentally aware, tool-using.
- Google whitepaper definition: agents observe the world, act on it with tools, and are autonomous and proactive.
- Paradigm shift framing: reactive → proactive, isolated → integrated, advisory → executive, static → adaptive.

## Notes

### The five essential characteristics

| # | Characteristic | What it means |
|---|---|---|
| 1 | **Goal-directed behavior** | Works toward objectives; understands current vs. desired state and acts to close the gap |
| 2 | **Autonomous operation** | Acts independently once given a goal; no explicit instruction needed per step |
| 3 | **Proactive initiative** | Actively works toward goals even without explicit instruction sets |
| 4 | **Environmental awareness** | Perceives the world through inputs (API responses, DB states, errors); builds and updates a model of the world |
| 5 | **Tool use** | Interacts with external systems (APIs, databases, services) to act beyond text generation |

Not everything using an LLM and tools is an agent — all five must be present.

### Google whitepaper definition

> "A generative AI agent can be defined as an application that attempts to achieve a goal by observing the world and acting upon it using the tools that it has at its disposal. Agents are autonomous and can act independently of human intervention, especially when provided with proper goals or objectives they are meant to achieve. Agents can also be proactive in their approach to reaching their goals."

The "observing the world and acting upon it using tools" phrasing is the same observe→tools→act formula first articulated in [[gcloud-agents-intro]]'s transcript definition. This source provides the formal written version; intro provides the verbal one.

### How the five characteristics map to the three core capabilities

[[gcloud-agents-core-capabilities]] defines three capabilities; this source defines five characteristics. They cover the same ground but at different granularity:

| This source (five characteristics) | [[gcloud-agents-core-capabilities]] (three capabilities) |
|---|---|
| Autonomous operation (2) + Proactive initiative (3) | **Autonomous action** |
| Goal-directed (1) + Environmental awareness (4) | **Reasoning and planning** |
| Tool use (5) | (implicit in autonomous action) |
| — | **Continuous learning** |

Notable gap: "continuous learning" has no direct equivalent in the five characteristics. The five characteristics describe what an agent *is*; the three capabilities add what it *does over time*.

### Weather/jacket example — all three approaches

**With an LLM:** "I don't have access to current weather data, but generally you should wear a jacket if it's below 60°F or raining." *(No environmental awareness, no tool use)*

**With LLM + function calling:** Calls weather API when asked, returns result, then answers follow-up question separately. *(Tool use, but not autonomous or proactive — you're managing the conversation flow)*

**With an agent:**
```
[Checks your location]
[Queries weather API]
[Checks your calendar for outdoor activities]
[Considers the forecast for when you'll be outside]
→ "Yes, wear a jacket. It's 55°F now, but drops to 48°F by 6 PM for your outdoor meeting."
```
All five characteristics in action from a single question.

### Problem categories only agents solve

1. **Complex multi-step workflows** — e.g., expense processing: extract receipts → categorize → check policy → route for approval → update accounting. One request, many coordinated actions.
2. **Dynamic problem solving** — e.g., travel booking where flights sell out and prices change; the agent adapts based on what it discovers.
3. **Ongoing task management** — e.g., "book when Tokyo flights drop below $800" — a continuous responsibility, not a one-time query.
4. **Integrated experiences** — e.g., event planning across calendar, venue, catering, invitations — one agent orchestrating multiple systems.

### The paradigm shift (key takeaways)

| From | To |
|---|---|
| Reactive | Proactive — agents pursue goals |
| Isolated | Integrated — context and state across interactions |
| Advisory | Executive — agents don't tell you what to do, they do it |
| Static | Adaptive — agents adjust based on what they learn |

> "This isn't just an incremental improvement, but a paradigm shift enabling entirely new application categories."

## Quotes worth keeping

> "An agent isn't just an LLM with tools bolted on. It's a fundamentally different abstraction; a system that can pursue goals autonomously."

> "Instead of responding to each request in isolation, an agent maintains context, plans ahead, and takes initiative to achieve objectives."

## Open questions

- The five characteristics are described as all-or-nothing ("not everything is an agent"). How does this square with partial implementations — e.g., a system that's autonomous and tool-using but not proactive?

## Related sources

- [[devagentfun-m1-l0]] — previous lesson: the three-stage evolution; this lesson defines what "Stage 3" actually means
- [[gcloud-agents-intro]] — provides the observe→tools→act formula this source's whitepaper definition formalises; earlier/simpler framing of the same core idea
- [[gcloud-agents-core-capabilities]] — defines the same territory as three capabilities; autonomous action = characteristics 2+3 here, reasoning/planning = characteristics 1+4; notably adds "continuous learning" with no equivalent in the five characteristics
- [[gcloud-agents-architecture]] — technical implementation: model + tools + memory are the building blocks that produce all five characteristics when combined
