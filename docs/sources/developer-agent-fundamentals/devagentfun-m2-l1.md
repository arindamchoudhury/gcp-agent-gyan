# The Three Components in Detail

> **Source:** T-DEVAGENTFUN-I-m2-l1-en-file-4.en.pdf
> **Added:** 2026-05-26
> **Tags:** ai-agents, agent-architecture, orchestration, agent-loop, tools, model, reasoning-frameworks
> **Type:** documentation

## Summary

Deep-dive on each of the three architectural components introduced in [[devagentfun-m2-l0]]. The key new concept is the **agent loop** — the precise mechanism of orchestration: Perceive → Think → Act → Check, repeating until the goal is achieved. The model's three functions (understanding intent, making decisions, learning from feedback) and three tool types (pre-built integrations, custom functions, information retrieval) are each unpacked in detail. A full four-iteration Paris flight booking walkthrough shows all three components operating together.

## Key points

- **Orchestration is the agent loop**: Perceive → Think → Act → Check. This is the cyclical process that connects model intelligence to tool capability. Directly answers the open question from [[devagentfun-m2-l0]].
- The model does three things: understand intent (handle ambiguity), make decisions (what to do next), learn from feedback (adapt when tools return errors or unexpected results).
- Three tool types: pre-built integrations, custom functions, information retrieval from databases.
- Reasoning frameworks (ReAct, chain-of-thought, tree-of-thoughts) guide *how* the model thinks at each loop iteration — different frameworks, same loop structure.
- Tool chaining — orchestrating multiple tool calls in sequence — is where agent power comes from.

## Notes

### Component 1 — The model (brain)

The model is the centralized decision maker. It does three things at each step of the loop:

| Function | What it means |
|---|---|
| **Understanding intent** | Extracts the actual goal from natural language; handles ambiguity (e.g., "Paris next week" → *which Paris? France or Texas?*) |
| **Making decisions** | Decides what to do next: search flights first or hotels? Ask for more info or proceed with defaults? Reasons about priorities and dependencies |
| **Learning from feedback** | Interprets tool results and errors; adapts approach (flight too expensive → try different dates; API error → try alternative service) |

"Learning from feedback" here is the per-loop adaptation behavior — distinct from [[gcloud-agents-core-capabilities]]' "continuous learning" capability, which describes improvement over many sessions.

### Component 2 — Tools (hands)

Three types:

| Type | What it does | Example |
|---|---|---|
| **Pre-built integrations** | Connects to external services; hides API details behind a simple interface | Google Flights, weather APIs |
| **Custom functions** | Delegates to your existing application code; agent prepares the request, your app executes it | "Require human approval before purchase" |
| **Information retrieval** | Accesses knowledge beyond training data: company docs, customer histories, product catalogs | Internal knowledge base query |

The power isn't any single tool — it's **chaining**: retrieve preferences from a database → find flights matching those preferences → prepare a booking function for approval. One goal, three coordinated tool calls.

For the technical standard governing how agents access tools, see [[gcloud-agents-architecture]] (MCP).

### Component 3 — Orchestration (the agent loop)

Orchestration is not just "the process" — it's a specific loop:

```
Perceive → Think → Act → Check
    ↑________________________|  (if not done)
```

> "The orchestration layer is a cyclical process that governs how the agent takes in information, performs internal reasoning, and uses that reasoning to inform its next action or decision." — Google whitepaper

| Step | What happens |
|---|---|
| **Perceive** | Takes in current state: user input, tool results, errors |
| **Think** | Reasons about what to do next; applies a reasoning framework |
| **Act** | Invokes a tool, asks a clarifying question, or produces output |
| **Check** | Evaluates: is the goal achieved? If not, loop again |

**Reasoning frameworks** guide the Think step — the model can use ReAct (reasoning + acting interleaved), chain-of-thought (step-by-step reasoning before acting), or tree-of-thoughts (exploring multiple reasoning paths). Different frameworks, same Perceive → Think → Act → Check outer loop.

### Paris flight booking — full walkthrough (4 iterations)

```
User: "Book me a flight to Paris next week"

Iteration 1:
  Perceive: user wants Paris flight, next week
  Think:    ambiguity — France or Texas? Need to ask
  Act:      ask clarifying question
  Check:    not done

User: "Paris, France. Flexible on dates."

Iteration 2:
  Perceive: destination Paris France, flexible dates
  Think:    check calendar for next-week availability
  Act:      calendar tool → "Available Mon–Wed"
  Check:    not done — have dates, no flights yet

Iteration 3:
  Perceive: available Mon–Wed
  Think:    search flights for those dates
  Act:      flight search → 3 options returned
  Check:    not done — need user choice

Agent presents 3 options ($450 direct, $380 one-stop, $520 premium)

User: "Book option 1"

Iteration 4:
  Perceive: user chose $450 direct
  Think:    ready to book
  Act:      booking tool → confirmed
  Check:    done ✓
```

Orchestration managed the loop. The model handled ambiguity, calendar lookup, search, and confirmation decisions. Three different tools were chained across four iterations.

## Quotes worth keeping

> "Without tools, even the smartest model is just generating text about what it would do."

> "The orchestration layer is a cyclical process that governs how the agent takes in information, performs internal reasoning, and uses that reasoning to inform its next action or decision."

> "The beauty of this architecture is how simple components working together create complex, autonomous behavior."

## Open questions

- How do the three reasoning frameworks (ReAct, chain-of-thought, tree-of-thoughts) compare in practice — when would you choose one over another?
- Does the course cover how custom functions handle the "human approval" case — is that a synchronous pause or an async handoff?

## Related sources

- [[devagentfun-m2-l0]] — previous lesson: introduced the three components and the brittle code problem; this lesson is the deep-dive; also answers m2-l0's open question about what orchestration precisely is
- [[gcloud-agents-architecture]] — same three components from the gcloud lens; adds MCP (tools standard), memory layers, and agent patterns not covered here; uses "memory" where this uses "orchestration"
- [[devagentfun-m1-l1]] — the five characteristics that the agent loop implements: Perceive = environmental awareness (4), Think = goal-directed (1), Act = tool use (5) + autonomous operation (2), Check = goal-directed (verifying goal state)
- [[gcloud-agents-core-capabilities]] — "continuous learning" maps loosely to "learning from feedback" here, but gcloud means improvement over sessions; this means per-loop adaptation
