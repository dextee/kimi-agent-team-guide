# The agent files

[Home](../README.md) · [Setup](../SETUP.md) · [Subagents and the model pool](../docs/subagents-and-model-pool.md)

Seven custom agents for Kimi Code. Each file's frontmatter sets the agent's **name, description, when-to-use hint and tool permissions**; the body is its system prompt. The last sentence of every body reminds the agent that its final message is the complete handoff to the caller — Kimi sub-agents do not share their intermediate reasoning with the main agent.

## What these files do not set

Kimi Code custom agent files have **no model field**. A `model` key in the frontmatter is ignored, so these files deliberately omit one. Model routing is configured separately:

- `/model` switches the model for the current session (main agent).
- `/secondary-model` sets the default model for spawned sub-agents (`[secondary_model] default_model` in `config.toml`).
- With the subagent model pool active (it is on by default), the main agent can pick among the pool's candidate models per spawn, so heavyweight roles can route to K3 while routine roles stay on `kimi-for-coding`.

Suggested `config.toml` fragment, reviewed line by line before merging:

```toml
[secondary_model]
default_model = "kimi-for-coding"
```

Thinking effort (`low` / `high` / `max`, supported on K3 and K2.8 Preview) is chosen per session and per task, not in the agent file. The table below is the guide's recommended pairing.

## Roles and recommended pairing

| File | Role | Recommended model / effort | Tool posture |
|---|---|---|---|
| [guide_architect.md](guide_architect.md) | Architect | K3 / max | Read-only |
| [guide_implementer.md](guide_implementer.md) | Implementer | K3 / high | Full, minus nothing |
| [guide_explorer.md](guide_explorer.md) | Explorer | kimi-for-coding / low | Read-only, no Bash |
| [guide_reviewer.md](guide_reviewer.md) | Reviewer | kimi-for-coding / high | No Write/Edit; Bash allowed for checks |
| [guide_auditor.md](guide_auditor.md) | Auditor | K3 / max | Read-only |
| [guide_researcher.md](guide_researcher.md) | Researcher | kimi-for-coding / high | Read-only, no Bash |
| [guide_editor.md](guide_editor.md) | Editor | kimi-for-coding / low | Write/Edit, no Bash |

For rapid mechanical loops (renames, formatting, small repeated fixes), run the session on `kimi-for-coding-highspeed` instead — Kimi describes it as the same coding ability at roughly 5–6× the output speed — and step back up when a failure resists repeated attempts.
