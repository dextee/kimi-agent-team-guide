[Home](../README.md) · [24-task selector](task-selector.md) · [Quota and cost](quota-and-cost.md)

# Models, context and effort

Checked against official documentation: **10 October 2026**. Kimi reports all figures below; this page restates them and adds editorial starting-point recommendations.

## The four model IDs

Kimi Code accepts four model IDs across its CLI, Desktop, VS Code and API surfaces:

| Model ID | Model | Context | Thinking effort | Tier gate (new plans) | Tier gate (legacy plans) |
|---|---|---|---|---|---|
| `k3` | K3 flagship | up to 1M tokens | `low` / `high` / `max` | Plus+ for K3; **Pro+** for 1M window | Moderato+; Allegretto+ for 1M |
| `k3-256k` | K3, 256K version | 256K tokens | `low` / `high` / `max` | Plus+ | Moderato+ |
| `kimi-for-coding` | K2.8 Preview | up to 1M tokens | `low` / `high` / `max` | Plus+ | Andante+ |
| `kimi-for-coding-highspeed` | K2.7 Code HighSpeed | per plan | — | Pro+ | Allegretto+ |

Key quota fact from Kimi's documentation: within 256K context, `k3-256k` delivers the same results as `k3` and consumes about **half the quota**. If the work fits, the 256K version is the cheaper way to get K3 answers. Video input is not supported on `k3-256k`.

## How we use them

| Model | Starting use | Step up when | Example |
|---|---|---|---|
| `kimi-for-coding` | Everyday implementation, review, research, writing | Requirements conflict, failure repeats, consequence rises | Build a feature; review a diff; reconcile sources |
| `kimi-for-coding-highspeed` | Small mechanical edits in a rapid loop | Three failed attempts at the same fix | Rename sweeps, format passes, quick test iterations |
| `k3-256k` | Demanding synthesis within 256K tokens | The corpus genuinely exceeds 256K | Multi-file audit, migration design, evidence reconciliation |
| `k3` | Whole-codebase or long-document reasoning at 1M | — (already the ceiling) | Large-system audit, whole-repo refactor planning |

Kimi positions K3 — 2.8 trillion parameters, KDA hybrid linear attention — as its strongest model for long-horizon programming, front-end visual design, knowledge work and complex reasoning. Kimi reports output up to **260 tokens/s** across tiers, and describes HighSpeed as the same underlying model at roughly **5–6×** Standard's output speed. Treat both as vendor-reported figures, not measurements from this guide.

## Thinking effort

K3 and K2.8 Preview accept `low`, `high` and `max` effort. Effort is the cheapest quality lever you control:

| Effort | Use for | Watch for |
|---|---|---|
| `low` | Extraction, search, mechanical edits, first drafts | Shallow tradeoff analysis; verify before reuse |
| `high` | Implementation, review, research synthesis | Higher per-call quota consumption |
| `max` | Ambiguous architecture, consequential audits, conflicting evidence | Slowest and most expensive; reserve it |

Two practical notes from Kimi's documentation: effort persists across sessions only below a model's top tier, and switching models or effort **invalidates the existing prompt cache** — starting a new session before big K3 work avoids paying extra for a cold cache.

## Choosing between K3 and K2.8 Preview

Kimi describes K2.8 Preview as close to K3 on coding and agent tasks with significantly more efficient thinking, and it carries the same `low`/`high`/`max` effort levels and up to 1M context. Our editorial starting point: use K2.8 Preview as the everyday lead and promote specific sessions to K3 when the task is ambiguous, spans very long context, or deserves the strongest available review. Promote by opening a new session (`/new`) on `k3` rather than switching mid-conversation.

## Sources

- [Kimi Code overview](https://www.kimi.com/code/docs/en/) — model IDs, tier gates, context, 260 tokens/s claim
- [Membership benefits](https://www.kimi.com/code/docs/en/kimi-code/membership.html) — new vs legacy plan gates
- [Kimi Code what's new](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) — K3 release notes, K2.8 Preview rollout, HighSpeed 5–6× claim, effort persistence, cache-invalidation hints
