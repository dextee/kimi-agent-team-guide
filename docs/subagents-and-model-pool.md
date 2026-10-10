[Home](../README.md) · [Agent files](../agents/README.md) · [Setup](../SETUP.md)

# Subagents and the model pool

Checked against official documentation: **10 October 2026**. Where this page and the live docs disagree, the docs win — report it via [contributing](../CONTRIBUTING.md).

## Built-in sub-agents

Every Kimi Code session is driven by a main Agent, which can dispatch **sub-agents** for focused sub-tasks. Three are built in:

| Sub-agent | Behavior | Tools |
|---|---|---|
| `coder` | General-purpose engineering; reads, writes, runs commands, lands changes | Nearly the main agent's full set |
| `explore` | Read-only codebase exploration and summarization | Read-only |
| `plan` | Implementation planning and architecture design | No shell commands |

Each sub-agent works in an **isolated context**: it sees only the task description the main agent passes, and only its final result returns to the main agent's history. This keeps the main context lean and lets sub-agents run in parallel — but each sub-agent independently consumes quota, so dispatching one for trivial work is waste.

The built-in sub-agents cannot dispatch further sub-agents, which bounds delegation depth. Custom agents inherit the built-in delegation allowlist (`coder`, `explore`, `plan`) unless they declare a `subagents` allowlist of their own.

## Custom agents

A custom agent is a Markdown file: YAML frontmatter declares `name`, `description`, `whenToUse`, `tools`, `disallowedTools`, `subagents` and `override`; the body is the system prompt. There is **no model field** — model selection is a session and pool concern, covered below. This repository's [agent files](../agents/README.md) follow that format.

Discovery is by scope, most specific first:

1. **Explicit** — a file passed with `--agent-file` for one launch; outranks everything.
2. **Project** — `.kimi-code/agents/` and `.agents/agents/` in the project root (nearest directory containing `.git`).
3. **Extra** — directories listed in `extra_agent_dirs` in `config.toml`.
4. **User** — `~/.kimi-code/agents/` (or `$KIMI_CODE_HOME/agents/`) and `~/.agents/agents/`.
5. **Plugin** — agents contributed by enabled plugins.
6. **Built-in** — the distributed defaults.

Same-name conflicts resolve in that order; a directory-discovered file only overrides a same-name built-in when it declares `override: true`. An explicit `--agent` or `--agent-file` can also make a custom agent the **main** agent for a session.

### Trust caution

Agent files are prompt configuration, and project-scoped files arrive with any repository you clone. A project file named `agent.md` with `override: true` replaces the default main agent's entire system prompt, and one without a `tools` list keeps every tool. Review `.kimi-code/agents/` in unfamiliar repositories with the same caution you would apply to scripts — and do not commit session directories or wire files, which can contain credentials, to public repos.

## Routing models: the subagent model pool

Model selection in Kimi Code happens at three layers:

| Layer | Control | Effect |
|---|---|---|
| Session | `/model` | Switches the model for the current session's main agent |
| Sub-agent default | `/secondary-model` (alias `/subagent-model`) | Writes `[secondary_model] default_model` in `config.toml` |
| Per spawn | The subagent model pool | With candidates listed under `[secondary_model]`, the main agent picks a pool model per sub-agent spawn |

The subagent model pool is **on by default** in current releases. A minimal `config.toml` fragment:

```toml
[secondary_model]
default_model = "kimi-for-coding"
```

For candidate-model details see Kimi's [configuration documentation](https://www.kimi.com/code/docs/en/kimi-code-cli/configuration/). The practical effect for this guide's team: keep the pool default on `kimi-for-coding` for routine roles, and route architect and auditor spawns to `k3` at `max` effort when the main agent judges the task demands it.

## Permissions and delegation

Sub-agent permission rules inherit from the main agent: approval decisions you have already granted propagate to dispatched sub-agents. If a tool must be unavailable inside sub-agents, tighten the rule on the main agent. Dispatch itself is presented as an approval request unless an allow rule or the active permission mode covers it.

Sub-agents can run in the background, and a completed sub-agent only reports after its background tasks settle — the parent receives the result when the underlying work is actually done. An existing sub-agent instance can be resumed to continue the same task.

## Sources

- [Agents and sub-agents](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/agents.html)
- [Slash commands](https://www.kimi.com/code/docs/en/kimi-code-cli/reference/slash-commands.html) — `/model`, `/secondary-model`
- [Kimi Code what's new](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) — pool graduation from experimental
