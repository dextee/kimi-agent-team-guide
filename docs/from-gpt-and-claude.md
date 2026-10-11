[Home](../README.md) · [Models, context and effort](models-context-effort.md) · [Subagents and the model pool](subagents-and-model-pool.md)

Checked against official documentation: **10 October 2026**.

# From the GPT and Claude guides

This guide is the third in a series. If you already use the [ChatGPT](https://github.com/dextee/chatgpt-agent-team-guide) or Claude agent-team guides, the tables below map their roles and levers onto Kimi Code. Model assignments in all three guides are editorial starting points.

## Role mapping

| Series role | GPT guide | Claude guide | This guide (Kimi) |
|---|---|---|---|
| Architect | GPT-6 Astra / high | Opus / high | K3 / max |
| Implementer | GPT-6.1 Sol / medium | Sonnet / medium | kimi-for-coding / high (K3 / high for large work) |
| Worker / mechanical | GPT-6 Luna / medium | Haiku / low | kimi-for-coding-highspeed loop, or kimi-for-coding / low |
| Explorer | GPT-6 Luna / high (read-only) | Haiku / low (read-only) | kimi-for-coding / low (read-only) |
| Reviewer | GPT-6.1 Sol / high | — (advisor pattern) | kimi-for-coding / high |
| Auditor | GPT-6 Astra / high | Opus / high | K3 / max |
| Researcher | GPT-6.1 Sol / high | — | kimi-for-coding / high |
| Editor | GPT-6.1 Sol / medium | — | kimi-for-coding / low |
| Visual director | GPT-6.1 Sol / medium + image tool | — | not ported; Kimi Code artwork in this series is Mermaid-only |

## Lever mapping

| Concept | GPT guide (Codex) | Claude guide | Kimi Code |
|---|---|---|---|
| Agent definition | TOML custom agents | Markdown plugin agents | Markdown files with YAML frontmatter |
| Per-agent model pin | `model` + `model_reasoning_effort` fields | model aliases | **Not supported** — session `/model` + `[secondary_model]` pool |
| Reasoning control | reasoning effort | thinking/effort levels | thinking effort `low` / `high` / `max` (K3, K2.8 Preview) |
| Fast tier | (same model, effort tuning) | Haiku | `kimi-for-coding-highspeed` (separate model ID) |
| Deep tier | Astra | Opus / Fable | `k3` / `k3-256k` |
| Review escalation | independent reviewer agent | `/advisor` pattern | reviewer/auditor agents at rising effort |
| Delegation | custom agents, `/agent` | subagents | built-in `coder` / `explore` / `plan` + custom agents |
| Read-only search | explorer agent | — | built-in `explore` sub-agent |

## What changed conceptually

**From Codex:** the biggest difference is that Kimi agent files pin *tools, not models*. Where a Codex TOML enforces "this role always runs Astra at high effort", the Kimi equivalent is a convention: keep the subagent pool default on `kimi-for-coding`, and promote architect/auditor work to K3 at `max` effort through session and pool configuration. Write that convention into your team instructions (`AGENTS.md`), because the file itself cannot enforce it.

**From Claude:** Kimi's effort levels map cleanly onto Claude's thinking tiers, and the built-in `plan` sub-agent covers the planning half of the old advisor pattern. The interactive "advise without editing" half maps to Kimi's read-only custom agents.

**Shared spine:** all three guides keep the same discipline — define outcome and acceptance checks first, explore before editing, escalate on ambiguity or consequence, and verify the actual final result rather than the agent's summary of it.
