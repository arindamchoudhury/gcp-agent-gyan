# Hands-On: Transform Your Agent

> **Source:** T-DEVAGENT-I-m2-l1-en-file-3.en.pdf
> **Added:** 2026-05-29
> **Tags:** adk, google-cloud, hands-on, agent-identity, instructions, python
> **Type:** documentation

## Summary

Practical exercise transforming the default agent from module 1 into a specialized math tutor, applying the four `Agent()` parameters from [[t-devagent-i-m2-l0]]. Covers the full edit → save → restart → test cycle, with troubleshooting tips for `adk web`.

## Key points

- Only `model` and `name` are technically required; `instruction` is critical for useful behaviour; `description` matters for multi-agent systems.
- The server **must be restarted** to pick up code changes — `adk web` does not hot-reload.
- Run `adk web` from the **parent directory** of your agent folder, or specify the path: `adk web my_first_agent`.
- Simple, focused instructions beat vague ones: define the role, set a personality trait, specify the task.

## Notes

### Transformation workflow

**Starting point — default agent from module 1**

```python
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant agent.',
    instruction='You are a helpful assistant.'
)
```

**Step 1 — Update the internal name**

Make `name` descriptive of what the agent actually does:

```python
root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor_agent',  # More specific internal name
    description='A helpful assistant agent.',
    instruction='You are a helpful assistant.'
)
```

**Step 2 — Write a specific description**

`description` tells *other agents* what this agent does (see [[t-devagent-i-m2-l0]] for the description vs instruction distinction):

```python
root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor_agent',
    description='Helps students learn algebra by guiding them through problem-solving steps.',
    instruction='You are a helpful assistant.'
)
```

**Step 3 — Write a simple instruction**

`instruction` tells *this agent* how to behave:

```python
root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor_agent',
    description='Helps students learn algebra by guiding them through problem-solving steps.',
    instruction='You are a patient math tutor. Help students with algebra problems.'
)
```

**Complete transformed agent — save to `agent.py` in your `my_first_agent` directory**

```python
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor_agent',
    description='Helps students learn algebra by guiding them through problem-solving steps.',
    instruction='You are a patient math tutor. Help students with algebra problems.'
)
```

What this instruction encodes:

- Role: math tutor
- Personality: patient
- Task scope: algebra problems

### Testing the customized agent

**Step 1 — Start the web interface**

Run from the parent directory of `my_first_agent`:

```shell
adk web
```

Or specify the path directly:

```shell
adk web my_first_agent
```

**Expected output**

```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

**Step 2 — Interact with your math tutor**

Select your agent from the dropdown (shows the internal `name`). Test prompts:

- `"What is 2x + 5 = 13?"` → should act as a math tutor, help with the problem, demonstrate patient tone
- `"I don't understand algebra at all."` → should respond as a patient tutor, offer help with concepts, maintain a supportive approach

**Step 3 — Observe the difference**

| | Generic agent (module 1) | Math tutor (module 2) |
|---|---|---|
| Instruction | `'You are a helpful assistant.'` | `'You are a patient math tutor. Help students with algebra problems.'` |
| Behaviour | Generic responses, no domain expertise | Focused on math tutoring, patient teaching approach, specialised for algebra |

**Step 4 — Stop the server**

```shell
Ctrl+C
```

### Troubleshooting

| Problem | Fix |
|---|---|
| Agent doesn't appear in dropdown | Run `adk web` from the parent directory of `my_first_agent`, or use `adk web my_first_agent` to specify the path |
| Still seeing old generic responses | Save changes to `agent.py`, then stop (`Ctrl+C`) and restart `adk web` — the server does not hot-reload |

### Key takeaways and common pitfalls

**Best practices**

- Write simple, focused instructions that define the role and task
- Be specific about what the agent does — don't just say "be helpful"
- Include a personality trait to guide the tone
- Test with `adk web` to see how instructions affect behaviour

**Common pitfalls**

- Vague instructions like `'be helpful'`
- Confusing `description` (for other agents) with `instruction` (for this agent) — see [[t-devagent-i-m2-l0]]
- Forgetting to assign the agent to the `root_agent` variable
- Using unclear or generic `name` values

## Open questions

- Does `adk web` ever support hot-reload, or is a restart always required?
- Can you run multiple agents in the same `adk web` session and switch between them?

## Related sources

- [[t-devagent-i-m2-l0]] — defines all four `Agent()` parameters; description vs instruction distinction; root_agent convention
- [[t-devagent-i-m1-l1]] — environment setup and initial `adk create` / `adk web` workflow
