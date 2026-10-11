# Set up your Kimi agent team

[Home](README.md) · [Subagents and the model pool](docs/subagents-and-model-pool.md) · [Agent files](agents/README.md)

This setup installs **seven Kimi Code custom agents**. There is no installer and nothing to compile: Kimi Code discovers agent Markdown files automatically by directory, so installation is a copy operation you can review line by line.

## 1. Check prerequisites

- Current Kimi Code CLI, Desktop or VS Code extension.
- A membership plan with access to the models you intend to use (Plus+ for Kimi Code and K3 — including `kimi-for-coding`'s 1M context; Pro+ for K3's 1M window and HighSpeed on current plans — [tier table](docs/quota-and-cost.md)).

```bash
kimi --version
git clone https://github.com/dextee/kimi-agent-team-guide.git
cd kimi-agent-team-guide
```

## 2. Choose a scope and copy

**Project scope** — one repository, travels with it for collaborators:

```bash
mkdir -p /path/to/your/project/.kimi-code/agents
cp agents/guide_*.md /path/to/your/project/.kimi-code/agents/
```

**User scope** — every project on this machine:

```bash
mkdir -p ~/.kimi-code/agents
cp agents/guide_*.md ~/.kimi-code/agents/
```

Do not install the same roles into both scopes unless you intend to manage precedence yourself; project files outrank user files. Alternatively, point `extra_agent_dirs` in `config.toml` at a checkout of this repository and updates arrive with `git pull`.

## 3. Route models to the team

Agent files set tools and prompts, not models. Configure model routing once:

```toml
# ~/.kimi-code/config.toml — merge deliberately; do not overwrite unrelated settings
[secondary_model]
default_model = "kimi-for-coding"
```

- `/model` — switch the main session model (use `k3` or `k3-256k` for deep sessions; start a new session after switching, because switching invalidates the prompt cache).
- `/secondary-model` — inspect or set the sub-agent default.
- With the subagent model pool on by default, heavyweight spawns (architect, auditor) can be routed to `k3` at `max` effort by the main agent when the task warrants it.

## 4. Verify the installation

Start a session in your project and ask:

```text
Use guide-explorer to identify this project's entry points and test commands.
Return only evidence with file references. Make no edits.
```

Confirm the dispatch is offered and completes. Then try one deep role:

```text
Use guide-architect to draft a plan for [a real upcoming task],
with acceptance checks and open decisions.
```

Installation alone is not proof that your account can run a model: if a dispatch fails, check plan tier, `/usage` quota, agent-file placement and session model before blaming the agent definition.

## Rollback

Remove the copied `guide_*.md` files from the scope you installed into. No configuration files, credentials or account state were touched, so nothing else needs rollback. Customized copies should be reviewed before deletion.

## What was tested here

The agent files and repository links have local static checks — frontmatter validity, internal link resolution and counted artifacts. Live model execution is account-dependent and is not part of those checks. See [validation evidence](VALIDATION.md) for the exact completed gates.
