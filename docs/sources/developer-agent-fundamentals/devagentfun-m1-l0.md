# The Evolution from LLMs to AI Agents

> **Source:** T-DEVAGENTFUN-I-m1-l0-en-file-1.en.pdf
> **Added:** 2026-05-26
> **Tags:** ai-agents, llm, function-calling, agent-evolution, autonomy
> **Type:** documentation

## Summary

Traces the progression from LLM APIs through function calling to AI agents, framing each step around a single limitation: the gap between *knowing* and *doing*. Agents close that gap by adding autonomy to tool use — the model pursues goals rather than waiting for explicit step-by-step instructions.

## Key points

- **The knowing-doing gap**: LLMs give great advice but can't act. You still have to do the work.
- Three evolutionary stages: LLM API (text only) → LLM + function calling (tools, but you orchestrate) → AI Agent (tools + autonomy, pursues goals).
- Function calling was a huge improvement but didn't grant autonomy — every function call still needed explicit human direction.
- Agents close the gap: instead of "I can search if you tell me the dates," the agent finds options, matches them, and asks "shall I proceed?"

## Notes

### The three stages of AI evolution

| Stage | Technology | Capability | Limitation |
|---|---|---|---|
| **1** | LLM API | Conversation, text generation | Frozen in time, no external access |
| **2** | LLM + Function Calling | Can call APIs, update databases | You still orchestrate every step |
| **3** | AI Agent | Pursues goals autonomously | — |

The formula: `Stage 1 + Functions = Stage 2` · `Stage 2 + Autonomy = Stage 3`

### Why function calling wasn't enough

With function calling you get *capability* but not *autonomy*. Booking a trip still meant manually coordinating: search flights → check availability → compare prices → book flights → find hotels → book hotels → arrange transport. The model got better at each step, but the human was still the planner.

### The Paris trip example

| Approach | Response |
|---|---|
| LLM | "Here's how to book a trip to Paris…" (advice only) |
| Function calling | "I can search for flights if you tell me the exact dates, then I can search for hotels if you tell me the area…" |
| Agent | "I've found three flight options that work with your calendar, matched them with nearby hotels in your budget, and I'm ready to book. Should I proceed?" |

The agent result is the same single request, but the output is a decision point, not a task list.

## Quotes worth keeping

> "It's akin to having a world-class advisor who can't pick up the phone, send an email, or press a button on your behalf."

> "That's the promise of agents."

## Open questions

- ~~At what point does function calling become an agent?~~ Answered in [[devagentfun-m3-l1]]: if the task is a single step with no adaptation, just use function calling directly. Agents start where multi-step, adaptive orchestration begins.

## Related sources

- [[gcloud-agents-intro]] — provides the observe→tools→act definition that Stage 3 implements; the travel domain used here (Paris) extends the travel row in intro's application domain table
- [[devagentfun-m1-l1]] — next lesson: the five characteristics that define the "true agent" at Stage 3; resolves the open question of when function calling becomes an agent
