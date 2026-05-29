# About Gemini Enterprise

> **Source:** [Google Cloud Training — C-AGTSPI-B v1.0.1](https://storage.googleapis.com/cloud-training/cls-html5-courses/C-AGTSPI-B/v1.0.1/index.html#/lessons/CoL6bbMndCKfO9ZhVWtgXpl8MyWpYUXM)
> **Added:** 2026-05-28
> **Tags:** ai-agents, google-cloud, gemini-enterprise, saas, no-code, enterprise
> **Type:** documentation

## Summary

A detailed look inside Gemini Enterprise — Google's SaaS-tier agent platform introduced in [[gcloud-agents-building]]. Explains what Gemini Enterprise actually is (intelligent assistant + search + enterprise data hub), how it categorizes AI agents by function, and the four types of agents available within it: Google-built, no-code, high-code, and third-party. The lesson is aimed at business users and frames agents in everyday terms rather than architectural ones.

## Key points

- Gemini Enterprise = Gemini reasoning + Google-quality search + enterprise data, all accessible through a single prompt.
- Three Google-built agents included out-of-the-box: Gemini LLM (broad requests), Search (retrieval), NotebookLM (deep research from provided sources).
- No-code agents: anyone can build one using a visual tool — four steps: define purpose → connect data → provide instructions → improve iteratively.
- High-code agents: full Python/framework access for developers; can pull from custom data sources and integrate with any system.
- Third-party agents: pre-built connectors for Salesforce, Jira, SharePoint, Microsoft Copilot; **ACLs from the source system are respected** — Gemini Enterprise doesn't bypass permissions.
- Four functional agent categories: information retrieval & summarization, task automation, data analysis & reporting, communication & interaction.
- Gemini Enterprise acts as an **orchestrator hub**: takes a prompt → orchestrates internal capabilities + custom agents → connects to data & fulfillment systems → delivers actionable response.

## Notes

### What Gemini Enterprise is

[[gcloud-agents-building]] described Gemini Enterprise as the "no-code UI and centralized hub for internal employee productivity." This lesson fills in the detail: it combines three things:

1. **Gemini's advanced reasoning** — the language model for understanding and generating
2. **Google-quality search** — finding specific information across vast data sources
3. **Enterprise data** — your company's own content, wherever it's hosted

The value proposition: employees can accomplish complex tasks (planning, research, content generation, action execution) with a single prompt, rather than switching between tools.

### Four agent categories (functional taxonomy)

Gemini Enterprise categorizes what AI agents *do* by function:

| Category | What it does |
|---|---|
| **Information retrieval & summarization** | Finds specific information from large datasets; generates concise summaries of documents or data |
| **Task automation** | Performs actions from user requests or predefined rules (update records, send notifications); automates complex multi-step workflows |
| **Data analysis & reporting** | Analyzes data for trends, patterns, and insights; generates reports and visualizations |
| **Communication & interaction** | Engages in natural language conversations (e.g., customer support chatbots); answers frequently asked questions |

This is a *functional* taxonomy (what the agent does) complementing [[gcloud-agents-enterprise-use-cases]]'s *business-function* taxonomy (customer, employee, creative, data, code, security) — different levels of the same idea.

### Four agent types in Gemini Enterprise

| Type | Who builds it | Key characteristics |
|---|---|---|
| **Google-built** | Google | Ready-to-use out-of-the-box; Gemini LLM, Search, NotebookLM |
| **No-code** | Business users | Visual tool, no coding; 4-step creation workflow |
| **High-code** | Developers / data scientists | Full coding capabilities; custom logic, custom data, fine-tuning |
| **Third-party** | External developers / partners | Pre-built connectors; Salesforce, Jira, SharePoint, Microsoft Copilot; ACLs respected |

**Google-built agents in detail:**
- *Gemini LLM* — handles broad requests, text generation, everyday tasks
- *Search* — finds and retrieves specific information from large data sources
- *NotebookLM* — in-depth research using sources you provide (different from Search: user-supplied corpus, not enterprise-wide)

**No-code agent creation — four steps:**
1. **Define the purpose** — clear, precise task description; specificity directly affects performance
2. **Connect data** — link to relevant sources (documents, spreadsheets, business apps)
3. **Provide instructions** — natural language, no code; the agent interprets everyday words
4. **Improve performance** — test in real time, iterate, refine

**Third-party integration detail:** ACLs from the original system are respected. If a user doesn't have access to a Jira ticket, the agent won't surface it — the integration doesn't create a permission bypass. This is a governance point absent from [[gcloud-agents-building]]'s description.

### Gemini Enterprise as orchestrator

The workflow description confirms the orchestrator pattern from [[gcloud-agents-architecture]] applies here: Gemini Enterprise acts as a hub that receives a prompt, orchestrates its own internal capabilities and any custom agents, connects to enterprise data and external systems, and delivers an integrated response. This mirrors the multi-agent orchestration model from [[gcloud-agents-core-capabilities]] but at the product layer rather than the architectural layer.

![Gemini Enterprise orchestrator diagram](https://storage.googleapis.com/cloud-training/cls-html5-courses/C-AGTSPI-B/v1.0.1/assets/Screenshot%202025-10-02%20at%2010.10.19%E2%80%AFPM.png)

*Prompt flows into Gemini Enterprise, which contains built-in capabilities (Assistant, Search, Actions) and a custom Agents panel (Custom tasks / logic / code). Bidirectional arrows connect to Data stores and External systems on the right; Response returns on the left.*

## Quotes worth keeping

> "Gemini Enterprise acts as your intelligent assistant and central command center for all your work information."

> "By bringing together Gemini's advanced reasoning, Google-quality search, and your enterprise data (regardless of where it's hosted), Gemini Enterprise unlocks enterprise expertise for employees."

## Open questions

- What exactly do "information retrieval & summarization" and "task automation" agents do in Gemini Enterprise? (accordion content not captured)
- How does NotebookLM differ from the Search agent in practice — is it always user-supplied sources, or can it also pull from enterprise data?
- What fulfillment systems does Gemini Enterprise natively support — is email/calendar/ticketing built-in, or configured per deployment?
- What is the full list of third-party connectors beyond Salesforce, Jira, SharePoint, Copilot?

## Related sources

- [[gcloud-agents-building]] — introduced Gemini Enterprise as the SaaS tier; this lesson is the detailed expansion of that single row
- [[gcloud-agents-enterprise-use-cases]] — "employee" category maps to Gemini Enterprise's core use case; the functional taxonomy here (4 categories) is a finer-grained version of those 6 business categories
- [[gcloud-agents-architecture]] — hub-and-orchestrator pattern; Gemini Enterprise's workflow (prompt → orchestrate → data → response) is this pattern at the product level
- [[gcloud-agents-core-capabilities]] — multi-agent collaboration; Gemini Enterprise's internal orchestration of Google-built + custom + third-party agents is a product-level expression of this
- [[gcloud-agents-intro]] — first introduced AI agents in everyday terms; this lesson uses the same framing (Google Assistant, chatbots) as entry-level examples
