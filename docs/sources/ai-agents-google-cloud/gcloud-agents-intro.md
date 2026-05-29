# Introduction to AI Agents

> **Source:** [Google Cloud Training — T-GCAGNT-B](https://storage.googleapis.com/cloud-training/cls-html5-courses/T-GCAGNT-B/v1.0.1/index.html#/lessons/m0f5eF-m5WKKkbwZ8QtKPTsX6UMJSBqi)
> **Added:** 2026-05-26
> **Tags:** ai-agents, google-cloud, llm, autonomous-systems
> **Type:** documentation

## Summary

An AI agent is a software system that uses AI (typically an LLM) to autonomously achieve a specific goal on behalf of a user. Unlike rule-based chatbots, agents can independently set sub-goals and carry them out — they act rather than just respond.

## Key points

- Agents use AI (usually language models) to achieve goals, not just answer questions.
- Key distinction: **autonomous action** — agents can independently set and pursue goals within a defined environment.
- They are not rule-based; they learn how to best achieve a goal from available inputs and tools.
- Practical applications span logistics (travel planning), productivity, and technical tasks (software development).

## Notes

### What makes an agent different from a chatbot

Chatbots and simple assistants follow predefined rules and respond to direct queries. Agents go further — they can break down a goal, decide on steps, use tools, and execute actions without constant human direction. The key differentiator is the capacity for **autonomous action**.

### How agents achieve goals

Agents are given a goal, tools (APIs, code execution, search), and inputs (context, user data, environment state), then reason across multiple steps to achieve the goal. For the full technical breakdown of how model + tools + memory implement this, see [[gcloud-agents-architecture]].

### Application domains

Five concrete examples from the transcript:

| Example | What it does |
|---|---|
| **Customer service** | Answers order status questions, handles returns, schedules callbacks for complex issues |
| **Productivity** | Reads a to-do list, estimates task duration, breaks up large tasks, schedules calendar with minimal context switching |
| **Smart pantry** | Monitors inventory, proactively reorders items when running low |
| **Travel** | Picks destination, finds hotels and flights, plans an itinerary matching the user's preferences |
| **Software development** | Writes code, delivers software for new ideas, adds features or AI to existing applications |

The customer service example is the same domain that [[gcloud-agents-core-capabilities]] develops into a full multi-agent refund workflow. The travel example is the domain [[devagentfun-m1-l0]] uses for its LLM → function calling → agent comparison (the Paris trip).

### Core definition from the transcript

> An agent can **observe** the world around it, use **tools** to interact with the world, **take action** on your behalf — or act **autonomously** — to accomplish a goal or perhaps find a goal.

This three-part structure (observe → tool use → act) is the durable definition that held up over 18+ months of rapid agent development.

## Quotes worth keeping

> "Agents focus on autonomous action. This means they have a higher ability to independently set goals and carry them out within a defined environment."

> "The simplest way to think about an agent is that an agent can observe the world around it, use tools to interact with the world in order to accomplish a goal, and agents can take action on your behalf, or even act autonomously to accomplish a goal or perhaps find a goal."

## Open questions

- How does this course define the boundary between an "agent" and a "tool-calling LLM"?
- What specific Google Cloud services underpin agent construction in this course?

## Related sources

- [[gcloud-agents-core-capabilities]] — extends autonomous action into three named capabilities; provides the full chatbot vs. agent comparison and refund workflow detail
- [[gcloud-agents-architecture]] — technical deep-dive: how model + tools + memory implement the observe→tools→act loop defined here
- [[devagentfun-m1-l0]] — extends the travel domain into the Paris trip example; shows *why* function calling alone isn't enough before agents
- [[devagentfun-m1-l1]] — provides more precise definition via five characteristics; the Google whitepaper quote builds directly on the observe→tools→act formula defined here
