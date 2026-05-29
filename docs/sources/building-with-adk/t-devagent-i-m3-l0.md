# Three Deployment Methods

> **Source:** T-DEVAGENT-I-m3-l0-en-file-4.en.pdf
> **Added:** 2026-05-29
> **Tags:** adk, google-cloud, deployment, adk-run, adk-api-server, programmatic, runner, sessions, python
> **Type:** documentation

> 📌 **Version note:** PDF covers ADK 1.x patterns. Current release is **v2.1.0** (May 2026). The `Runner`/`InMemorySessionService`/`run_async()` programmatic pattern is compatible with 2.x. ADK 2.0 breaking changes: (1) `BaseAgent` now subclasses `BaseNode` — custom `_run_async_impl()` overrides are bypassed; (2) Event schema has new `node_info`/`output` fields — custom DB-backed session storage needs schema migration; (3) never manually append to `context.session.events` — breaks graph determinism; (4) avoid broad `except Exception:` in tools — disables automatic retries. `InMemorySessionService` is unaffected by all four.

## Summary

Three execution methods beyond `adk web`: `adk run` (terminal), `adk api_server` (REST API), and programmatic Python execution using `Runner` and `InMemorySessionService`. Includes a complete copy-paste-ready async Python example and a comparison table of all four methods.

## Key points

- `adk run` — terminal interaction, no browser, useful for CI/CD and server environments without GUI.
- `adk api_server` — runs agent as a REST API; intended for web/mobile app backends and pre-production testing before deploying to Cloud Run.
- Programmatic execution — full Python control via `Runner` + `InMemorySessionService`; events streamed async; use `await run_agent()` in Jupyter/Colab, `asyncio.run(run_agent())` in scripts.
- All four methods use the same `agent.py` — only the interaction layer changes.

## Notes

### Method 1 — `adk run` (terminal execution)

Interact with the agent directly from the terminal, no browser needed.

**From agent directory:**

```shell
cd my_first_agent
adk run
```

**From parent directory:**

```shell
adk run my_first_agent
```

**Example interaction:**

```shell
$ adk run my_first_agent

You: How do I solve x + 5 = 10?
Agent: Great question! Let's work through this together. What do you think we
need to do to get x by itself on one side?

You: Subtract 5 from both sides?
Agent: Exactly! That's the right approach. When we subtract 5 from both sides...
```

Press `Ctrl+C` to exit.

**When to use `adk run`**

Good for:

- Quick testing during development
- Command-line workflows
- Server environments without GUI
- Automated testing scripts
- CI/CD pipelines

Not ideal for: presenting to stakeholders or debugging complex conversations — use `adk web` instead.

### Method 2 — `adk api_server` (REST API)

Runs the agent as a REST API service; other applications send requests over HTTP.

**Start the server:**

```shell
# From agent directory
cd my_first_agent
adk api_server

# Or from parent directory
adk api_server my_first_agent
```

**Expected output:**

```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

**Test with cURL (in a separate terminal):**

`POST /run` — blocking, returns all events as a JSON array when complete:

```shell
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{
    "appName": "math_tutor_app",
    "userId": "u_123",
    "sessionId": "s_abc",
    "newMessage": {
      "role": "user",
      "parts": [{"text": "What is 2x + 5 = 13?"}]
    }
  }'
```

`POST /run_sse` — streaming, returns events via Server-Sent Events as they're generated:

```shell
curl -X POST http://localhost:8000/run_sse \
  -H "Content-Type: application/json" \
  -d '{
    "appName": "math_tutor_app",
    "userId": "u_123",
    "sessionId": "s_abc",
    "newMessage": {
      "role": "user",
      "parts": [{"text": "What is 2x + 5 = 13?"}]
    },
    "streaming": true
  }'
```

Browse `http://localhost:8000/docs` for the auto-generated Swagger UI with full endpoint docs. Request bodies use camelCase (`appName`, `userId`, `sessionId`, `newMessage`).

**When to use `adk api_server`**

Good for:

- Integrating agents into web applications
- Mobile app backends
- Microservices architectures
- Pre-production testing
- Local API development before deploying to Cloud Run

Not ideal for: interactive development (use `adk web`) or quick testing (use `adk run`).

### Method 3 — Programmatic execution (Python)

Run agents directly in Python code — full programmatic control.

> **Why no `root_agent` here?** The `root_agent` naming convention (from [[t-devagent-i-m2-l0]]) exists solely for the ADK CLI tools (`adk web`, `adk run`, `adk api_server`) — they scan `agent.py` looking for a variable named exactly `root_agent`. In programmatic execution you bypass the CLI entirely and hand the agent object directly to `Runner(agent=agent)`, so any variable name works.

Good for: Jupyter notebooks, Google Colab, custom Python applications, data processing pipelines, research and experimentation.

**Complete example — copy-paste ready for a Python script or Jupyter notebook:**

```python
"""
Complete example: Running an ADK agent programmatically
Copy this entire code block to run it in a Python script or notebook.
"""

# Step 1: Install ADK (run this in terminal or notebook cell)
# pip install google-adk

# Step 2: Set your API key
# Option A: Set as environment variable before running
#   export GOOGLE_API_KEY=your-api-key-here
# Option B: Uncomment and use this code:
# import os
# os.environ['GOOGLE_API_KEY'] = 'your-api-key-here'
# os.environ['GOOGLE_GENAI_USE_VERTEXAI'] = 'FALSE'

# Step 3: Import required libraries
import asyncio
from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# Step 4: Define your agent
agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor',
    instruction="""You are a patient math tutor.
    Guide students through problems step-by-step.
    Don't just give answers - help them discover solutions."""
)

# Step 5: Set up session and runner
APP_NAME = "math_tutor_app"
USER_ID = "student_1"
SESSION_ID = "session_001"

session_service = InMemorySessionService()
runner = Runner(
    agent=agent,
    app_name=APP_NAME,
    session_service=session_service
)

# Step 6: Define async function to run the agent
async def run_agent():
    # Create session
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print(f"Session created: {SESSION_ID}\n")

    # Prepare user message
    user_message = Content(
        role="user",
        parts=[Part(text="How do I solve 2x + 5 = 13?")]
    )

    # Run agent and collect response
    print("User: How do I solve 2x + 5 = 13?\n")
    print("Agent: ", end="")

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_message
    ):
        # Print final response
        if event.is_final_response() and event.content and event.content.parts:
            print(event.content.parts[0].text)

# Step 7: Run the agent
# For Jupyter/Colab: Use await directly
# await run_agent()

# For Python scripts: Use asyncio.run()
asyncio.run(run_agent())
```

**Running in Jupyter notebook or Google Colab** (event loop already running):

```shell
await run_agent()
```

**Expected output:**

```
Session created: session_001

User: How do I solve 2x + 5 = 13?

Agent: Great question! Let's work through this together. First, what do you
think we need to do to get x by itself on one side?
```

### Comparison — when to use each method

| Method | Best for | Session persistence | Setup complexity |
|---|---|---|---|
| `adk web` | Development, debugging, demos | Yes (in browser) | Low |
| `adk run` | Quick tests, CLI workflows | No | Very low |
| `adk api_server` | API integration, production | Depends on client | Low |
| Programmatic | Custom apps, notebooks | Yes (managed) | Medium |

**Quick decision guide:**

- Developing? → `adk web`
- Quick test? → `adk run`
- Building an API? → `adk api_server`
- Custom integration? → programmatic execution

## Open questions

- Does `adk api_server` maintain session state between separate `/run` calls using the same `sessionId`, or is each call independent?
- What other event types does `runner.run_async()` emit beyond `is_final_response()`?
- Can `InMemorySessionService` be swapped for a persistent store (e.g. database-backed)?

## Related sources

- [[t-devagent-i-m2-l1]] — introduced `adk web` testing workflow; this lesson adds three more methods
- [[t-devagent-i-m1-l1]] — original `adk web` setup; the troubleshooting note about restarting the server applies to `adk api_server` too
- [[gcloud-agents-adk-intro]] — ADK deployment options pillar (Agent Engine, Cloud Run, GKE); `adk api_server` is the local precursor to Cloud Run deployment
