# When to Use Agents: Introduction

> **Source:** T-DEVAGENTFUN-I-m3-l0-en-file-5.en.pdf
> **Added:** 2026-05-26
> **Tags:** ai-agents, agent-design, when-to-use, decision-making
> **Type:** documentation

## Summary

Module 3 introduction — frames the core problem of agent adoption: teams either over-engineer simple problems with agents, or under-engineer complex ones with basic automation. The lesson sets up the question that [[devagentfun-m3-l1]] answers: how do you know which is which?

## Key points

- Two symmetric failure modes: using agents for FAQ bots (overkill), or using if-then automation for returns processing (underpowered).
- The problem isn't the technology — it's knowing when to use it.

## Notes

### The two failure modes

**Over-engineering:** A team spends six weeks building an agent that can reason, search multiple sources, and compose answers — for a FAQ bot that fields "What are your business hours?" A simpler retrieval system would have been sufficient.

**Under-engineering:** Another team is drowning in unmaintainable if-then automation trying to handle customer returns — checking order history, evaluating return policies, calculating refunds, updating inventory, issuing credits. This is exactly the multi-system, multi-step, adaptive problem agents are built for. The same scenario [[gcloud-agents-core-capabilities]] uses to show why agents beat chatbots.

The asymmetry is instructive: both teams chose the wrong tool, but in opposite directions.

## Related sources

- [[devagentfun-m3-l1]] — the solution: clear decision criteria, agent-shaped problem characteristics, anti-patterns, decision tree
- [[gcloud-agents-core-capabilities]] — develops the customer returns scenario (from "under-engineering" example above) into a full multi-agent refund workflow
