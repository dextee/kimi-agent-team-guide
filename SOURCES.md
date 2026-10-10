# Sources

[Home](README.md) · [Validation](VALIDATION.md)

Every product fact in this guide was checked against the official Kimi Code documentation on **10 October 2026**. Model access, tier names and interfaces can change after that date; the linked pages are the source of truth. Scenario routing (which model for which task) is this guide's editorial recommendation and is labelled as such wherever it appears.

| Claim | Source |
|---|---|
| Four model IDs and their descriptions (`k3`, `k3-256k`, `kimi-for-coding`, `kimi-for-coding-highspeed`) | [Kimi Code overview](https://www.kimi.com/code/docs/en/) |
| K3 flagship positioning; 2.8T parameters; long-horizon programming strengths | [Kimi Code overview](https://www.kimi.com/code/docs/en/) · [What's new](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) |
| Output up to 260 tokens/s (vendor-reported) | [Kimi Code overview](https://www.kimi.com/code/docs/en/) |
| HighSpeed ≈ 5–6× Standard output speed (vendor-reported) | [What's new](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) |
| `k3-256k` same results within 256K at ~half the quota; no video input | [Kimi Code overview](https://www.kimi.com/code/docs/en/) |
| Thinking effort `low` / `high` / `max` on K3 and K2.8 Preview | [Kimi Code overview](https://www.kimi.com/code/docs/en/) · [What's new](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) |
| Tier gates: Plus+ for Kimi Code/K3; Pro+ for 1M and HighSpeed; legacy Andante/Moderato/Allegretto mapping | [Membership benefits](https://www.kimi.com/code/docs/en/kimi-code/membership.html) |
| New plans drop weekly limit; 5-hour rolling rate window; monthly total; legacy 7-day refresh | [Membership benefits](https://www.kimi.com/code/docs/en/kimi-code/membership.html) |
| Extra Usage mechanics: deducted last, monthly cap, RMB usage billing, top-up limits | [Membership benefits](https://www.kimi.com/code/docs/en/kimi-code/membership.html) |
| Built-in sub-agents (coder/explore/plan), isolation, permission inheritance, background completion | [Agents and sub-agents](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/agents.html) |
| Custom agent file format, frontmatter fields, discovery scopes and precedence, trust model | [Agents and sub-agents](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/agents.html) |
| `/model`, `/secondary-model` (writes `[secondary_model] default_model`), `/usage` | [Slash commands](https://www.kimi.com/code/docs/en/kimi-code-cli/reference/slash-commands.html) |
| Subagent model pool on by default; per-spawn candidate selection | [What's new](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) |
| Model/agent switch invalidates prompt cache; start a new session for K3 work | [What's new](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) |
| API base URLs (OpenAI- and Anthropic-compatible, China/overseas); key management (5 keys, console) | [Kimi Code overview](https://www.kimi.com/code/docs/en/) |
| User-Agent tampering is a membership violation | [Kimi Code overview](https://www.kimi.com/code/docs/en/) |
| K2.8 Preview fully rolled out under unchanged ID `kimi-for-coding`; performance close to K3 with more efficient thinking | [What's new](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) |
| Multi-provider CLI (Anthropic, OpenAI, Gemini, Vertex) | [Providers and models](https://www.kimi.com/code/docs/en/kimi-code-cli/configuration/providers.html) |

## Claim boundaries

- **Not claimed:** benchmark comparisons between Kimi models and other vendors' models; client outcomes for VYR; measured token speeds. Vendor-reported figures are attributed as such.
- **Editorial:** all task-to-model routing in the README, the 24-task selector, the 12 recipes, and the team table in `agents/README.md`.
- **Inherited conventions:** guide structure, verification-date discipline, delegation brief, evaluation worksheet and VYR conversion page pattern from the companion [ChatGPT Agent Team Guide](https://github.com/dextee/chatgpt-agent-team-guide), adapted for Kimi Code's agent and quota model.
