# ADK Environment Setup

> **Source:** T-DEVAGENT-I-m1-l1-en-file-1.en.pdf
> **Added:** 2026-05-29
> **Tags:** adk, google-cloud, setup, python, gemini, development-environment
> **Type:** documentation

## Summary

Step-by-step setup guide for the ADK development environment: installing Python and ADK, creating a virtual environment, scaffolding a first agent project, configuring API credentials, and verifying the setup with `adk web`. Ties each setup step back to the three-component architecture (model + tools + orchestration) from course 1.

## Key points

- ADK supports Python 3.10–3.13 and Java 17+; this course uses Python. (PDF says 3.11+; PyPI metadata says `>=3.10`; classifiers list 3.10–3.13. 3.14 not yet supported as of google-adk 2.1.0.)
- Two API access options: Google AI Studio (quick, free tier, recommended for learning) or Gemini Enterprise Agent Platform (enterprise, production; formerly Vertex AI).
- `adk create <name>` scaffolds a project with `agent.py`, `__init__.py`, and `.env` — ADK auto-loads `.env` so API keys never appear in code.
- The `Agent` class automatically runs the Perceive → Think → Act → Check loop — orchestration is implicit, not hand-coded.
- Development workflow: edit `agent.py` → run `adk web` → iterate.
- Never commit `.env` to Git.

## Notes

### Setup workflow (8 steps)

**Step 1 — Verify Python**

```shell
python --version     # or python3 --version
# Required: Python 3.10 or higher (3.13 recommended)
```

**Step 2 — Create workspace**

```shell
mkdir adk-workspace
cd adk-workspace
```

**Step 3 — Create virtual environment**

**venv (from PDF)**

```shell
# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\activate.bat
```

**conda (preferred)**

```shell
# Use 3.13 — latest officially supported version (classifiers: 3.10–3.13)
# 3.14 is not yet in the classifier list as of google-adk 2.1.0
conda create -n adk-workspace python=3.13 -y
conda activate adk-workspace

# Deactivate when done
conda deactivate
```

Conda env name shows in prompt: `(adk-workspace)`. Must run `conda activate adk-workspace` in every new terminal session.

**Step 4 — Install ADK**

**venv or conda** (same command — google-adk is not on conda-forge)

```shell
pip install google-adk
adk --version    # verify; expect 1.0.0 or higher
```

**Step 5 — Get API key (two options)**

**Option A — Google AI Studio** (recommended for learning)

1. Visit Google AI Studio
2. Sign in → Click **Create API Key**
3. Copy key (looks like `AIzaSyC...`)

**Option B — Gemini Enterprise Agent Platform** (production, formerly Vertex AI)

> 📌 **Setup changed (2026):** The old Vertex AI flow (gcloud CLI + `gcloud auth application-default login` + manual `.env` project/location config) has been replaced by **Agents CLI**. Source: [ADK + Agents CLI quickstart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/quickstart-adk)

1. Have a Google Cloud project with the **Agent Platform API** enabled
2. Install `uv` (Python package manager) — [installation guide](https://docs.astral.sh/uv/getting-started/installation/)
3. Run the Agents CLI setup:
   ```shell
   uvx google-agents-cli setup
   ```
4. Open your AI dev tool (Gemini CLI, Claude Code, etc.) — Agents CLI skills activate via natural language prompts and handle project/location config interactively

No manual `.env` configuration needed for the platform connection — the CLI handles it.

**Step 6 — Scaffold first agent**

```shell
adk create my_first_agent
cd my_first_agent
```

`adk create` now prompts interactively — you no longer need to manually edit `.env` afterward:

1. **Choose a model** — select from available options (e.g. `gemini-2.5-flash`)
2. **Choose a backend** — Google AI (API key) or Gemini Enterprise Agent Platform (formerly Vertex AI)
3. **Enter API key** — paste your key from AI Studio (if Google AI selected); `.env` is written automatically

Project structure created (unchanged from PDF):

```
my_first_agent/
├── agent.py      # Main agent code (edit this)
├── __init__.py   # Python package initialization
└── .env          # Pre-filled by adk create — verify contents before use
```

Default `agent.py`:

```python
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant agent.',
    instruction='You are a helpful assistant.'
)
```

**Step 7 — Configure API key**

> 📌 If you completed the interactive prompts in Step 6, `.env` is already written — skip to Step 8 and verify. Only edit manually if you skipped prompts or need to switch backends.

**Option A (Google AI Studio)**

```shell
# .env
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your-actual-api-key-here
```

**Option B (Gemini Enterprise Agent Platform)**

> ❓ The old Vertex AI `.env` vars (`GOOGLE_GENAI_USE_VERTEXAI`, `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`) may still work for direct API access, but the new Agents CLI flow configures credentials interactively — verify against current docs before using these manually.

Security rule: never commit `.env` to Git. It must be in `.gitignore`. Use `GOOGLE_API_KEY`, not `GEMINI_API_KEY` (common mistake).

**Step 8 — Verify setup**

```shell
adk web
```

**Expected output**

```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Browser opens to the ADK web UI. Agent name visible → setup complete.

**Common errors:**

| Error | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'google.adk'` | Env not activated — run `conda activate adk-workspace` or `source .venv/bin/activate` |
| `Invalid API key` | Wrong variable name in `.env` — use `GOOGLE_API_KEY`, not `GEMINI_API_KEY`; check for spaces around `=` |
| `Command 'adk' not found` | Env not activated, or ADK not installed — activate env then run `pip install google-adk` |

### How agent.py connects to the three-component architecture

The annotated default agent ties setup back to the model + tools + orchestration framework from [[devagentfun-m2-l0]]:

```python
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',        # Model: The reasoning engine (Course 1!)
    name='root_agent',               # Identity: Required identifier
    description='A helpful agent.',  # Purpose: What this agent does
    instruction='You are helpful.'   # Behavior: How to act
    # Tools: You'll add these in Module 3
    # Orchestration: Handled automatically by the Agent class
)
```

- **Model** (`gemini-2.5-flash`): LLM providing reasoning and decision-making; configured via `.env`
- **Tools**: not in this lesson — added in Module 3
- **Orchestration**: the `Agent` class automatically runs Perceive → Think → Act → Check; no manual loop needed

### Development workflow

```
Edit agent.py      →  define agent behavior
adk web            →  test in browser UI
Iterate            →  change, refresh, test

adk run            →  terminal-based interaction (alternative to web UI)
adk api_server     →  deploy as API service
```

### File roles

| File | Role |
|---|---|
| `agent.py` | Agent definition: model, tools, orchestration wired together |
| `__init__.py` | Package init; imports agent module so ADK can discover it |
| `.env` | Secrets (API keys, project IDs); auto-loaded by ADK; never committed |

## Open questions

- What does `__init__.py` need to import exactly — just `root_agent`, or the full module?
- Does `adk web` hot-reload on `agent.py` changes, or does it need a restart?
- What is `adk api_server` and how does it differ from deploying to Agent Engine?

## Related sources

- [[gcloud-agents-adk-intro]] — conceptual overview of ADK's three pillars; this lesson is the practical setup companion
- [[devagentfun-m2-l0]] — three-component architecture (model + tools + orchestration); agent.py maps each parameter to a component
- [[devagentfun-m2-l1]] — the Perceive → Think → Act → Check loop; `Agent` class runs this automatically
- [[gcloud-agents-building]] — introduced ADK in the Google Cloud platform context; this lesson is the hands-on entry point
