[Home](../README.md) · [Models, context and effort](models-context-effort.md) · [Subagents and the model pool](subagents-and-model-pool.md)

# Using Kimi models in third-party tools

Checked against official documentation: **10 October 2026**.

## API access

Kimi membership includes an API Key (create and manage up to five in the [Kimi Code Console](https://www.kimi.com/code/); each key is shown once). The API is protocol-compatible with both OpenAI and Anthropic conventions:

| Protocol | Base URL (China) | Base URL (overseas) |
|---|---|---|
| OpenAI-compatible | `https://api.kimi.com/coding/v1` | `https://api.kimi.ai/coding/v1` |
| Anthropic-compatible | `https://api.kimi.com/coding/` | `https://api.kimi.ai/coding/` |

The same four model IDs are accepted on both protocols: `k3`, `k3-256k`, `kimi-for-coding`, `kimi-for-coding-highspeed`. Requests from CLI, Desktop, VS Code and API keys all draw on the same membership quota.

## Kimi Code in other agent tools

Kimi Code works with Claude Code, OpenCode, Codex and other mainstream agent tools — configure the Base URL and API Key from the table above and pick a model ID. When using the managed service inside the official Kimi Code CLI, `/login` handles authentication with OAuth and no manual key configuration is needed.

One rule from Kimi's documentation worth repeating: maintain the tool's real identity identifier. Tampering with the client User-Agent is treated as a violation and can suspend membership benefits.

## When to use which surface

| Surface | Use when |
|---|---|
| Kimi Code CLI / Desktop / VS Code | Interactive agent work with subagents, skills, plugins and sessions |
| API from third-party tools | You are already invested in another agent's workflow and want Kimi models behind it |
| `kimi-for-coding-highspeed` in a third-party tool | Rapid output where that tool exposes model selection directly |

## Sources

- [Kimi Code overview](https://www.kimi.com/code/docs/en/) — endpoints, model IDs, key management, client-identifier rule
- [Using Kimi Code in other coding agents](https://www.kimi.com/code/docs/en/third-party-tools/other-coding-agents.html)
