# Enterprise Use Cases for AI Agents

> **Source:** [Google Cloud Training — T-GCAGNT-B v1.0.0](https://storage.googleapis.com/cloud-training/cls-html5-courses/T-GCAGNT-B/v1.0.0/index.html#/lessons/cfxFmcm1pRKJSwGH1uHQNmPjR34bp3Er)
> **Added:** 2026-05-28
> **Tags:** ai-agents, google-cloud, enterprise, use-cases, agentic-workflow
> **Type:** documentation

## Summary

Categorizes AI agents by the business value they create, grouping enterprise use cases into six functional types. The key framing shift from earlier lessons: agents should be evaluated against real KPIs, not hypothetical use cases. Includes a Zebra Technologies case study showing four specialized employee agents for retail frontline workers.

## Key points

- Six enterprise agent categories: **customer, employee, creative, data, code, and security** agents — each maps to specific KPIs.
- Agents move beyond simple automation to address bottlenecks and complexity — framed as a business transformation tool, not just a technology.
- Agentic workflow components listed as: models, tools, orchestration, **and runtime** — adds "runtime" as a fourth component not named in [[devagentfun-m2-l0]] or [[devagentfun-m2-l1]]'s three-component framework.
- KPI alignment is essential: understanding the problem your agent solves and the metrics it improves ensures business value, not just a demo.

## Notes

### Six agent categories by business function

![Six enterprise agent categories — Customer service, Employee productivity, Creative, Code, Data, Security](https://storage.googleapis.com/cloud-training/cls-html5-courses/T-GCAGNT-B/v1.0.0/assets/agent-core-use-cases.png)

*The six categories arranged as an arc: Customer service, Employee productivity, Creative, Code, Data, Security agents.*

> ⚠️ **Partial capture:** The lesson uses interactive click-to-expand cards for each category. The fetch script captured Customer service agents; the other 5 descriptions were not captured (exclusive accordion — clicking one closes the previous). Only that one description plus the key takeaway section is confirmed text.

The six categories named:

| Category | Description | Related prior example |
|---|---|---|
| **Customer** | Deliver highly personalized customer experiences by understanding and resolving customer needs; often use Conversational Agent features like Generative Responses and Generative Playbooks | Customer service domain in [[gcloud-agents-intro]] and refund workflow in [[gcloud-agents-core-capabilities]] |
| **Employee** | *(description not captured)* | Productivity + smart pantry in [[gcloud-agents-intro]]; Zebra case study below |
| **Creative** | *(description not captured)* | Not previously covered |
| **Data** | *(description not captured)* | Research/analysis trigger type in [[devagentfun-m3-l1]] |
| **Code** | *(description not captured)* | Software dev domain in [[gcloud-agents-intro]] |
| **Security** | *(description not captured)* | Automated incident response in [[devagentfun-m3-l1]] (adjacent domain) |

This is a different taxonomy from [[gcloud-agents-intro]]'s domain list (customer service, productivity, smart pantry, travel, software dev) — that list organizes by use-case scenario; this list organizes by the enterprise function served.

### The runtime component

This lesson describes agent components as: **models + tools + orchestration + runtime**. This adds "runtime" to the three-component framework used throughout [[devagentfun-m2-l0]] and [[devagentfun-m2-l1]]. The lesson doesn't define "runtime" explicitly, but context suggests it refers to the execution environment that hosts and runs the agent loop.

> ❓ Unverified: whether "runtime" is a distinct architectural component or an umbrella term encompassing orchestration + infrastructure.

### Case study — Zebra Technologies (employee agents)

**Context:** Global frontline worker shortage (~85 million by 2030) driving need for AI-assisted workflows in retail, logistics, warehousing.

**Zebra Companion** — four specialized agents working together:

| Agent | Function |
|---|---|
| **Knowledge assistant** | Gives workers instant access to store SOPs, policy documents, procedures |
| **Merchandising agent** | Helps workers rapidly verify shelf is guest-ready |
| **Sales agent** | Enables assistive selling — helps store associates recommend to customers |
| **Device agent** | Troubleshoots interoperability issues across Zebra's device portfolio |

The four-agent design is a real-world example of the multi-agent collaboration from [[gcloud-agents-core-capabilities]] — specialized agents each handling a distinct function rather than one agent trying to do everything. The specific routing structure maps to the orchestrator/router pattern in [[gcloud-agents-architecture]].

**Interface evolution:** Moving beyond GUI/natural language toward a "real-world interface" combining voice, vision, and contextual data (wearables that see what the worker sees). This extends environmental awareness (characteristic 4 in [[devagentfun-m1-l1]]) to physical sensor inputs, not just API responses.

### KPI alignment framing

> "Understanding the problem your agents are solving and the metrics by which they can be measured helps ensure your agents are delivering business value, not just a hypothetical use case."

This connects to the decision framework in [[devagentfun-m3-l1]] — don't use agents for the sake of agents; evaluate against the business outcome they produce.

## Quotes worth keeping

> "With AI, agents can move beyond simple automation to directly address bottlenecks and complexities."

> "It's important to understand the specific business impact of utilizing various AI Agents… they can each map directly to key performance indicators (KPIs) that matter to you and your organization."

## Open questions

- What are the descriptions of the remaining 5 agent categories (Employee, Creative, Data, Code, Security)? The page uses an exclusive accordion — clicking one card closes the previous, so only Customer service was captured. Needs a card-by-card navigator similar to carousel handling.
- How does "runtime" relate to orchestration — is it a container/platform layer, or does it extend the three-component model?

## Related sources

- [[gcloud-agents-intro]] — earlier domain list (5 examples); this lesson provides the business-function taxonomy that maps across those examples
- [[gcloud-agents-core-capabilities]] — defines multi-agent collaboration (specialized agents dividing tasks); Zebra's four-agent design is the same pattern
- [[gcloud-agents-architecture]] — orchestrator/router and sub-agent patterns; three components (model + tools + memory); this lesson adds "runtime" as a possible fourth
- [[devagentfun-m3-l1]] — when to use agents; KPI alignment here extends that decision framework into enterprise context
- [[devagentfun-m1-l1]] — environmental awareness (characteristic 4); Zebra's wearable vision extends this to physical sensors
