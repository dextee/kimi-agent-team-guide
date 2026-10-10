[Home](../README.md) · [Models, context and effort](models-context-effort.md)

# Quota and cost

Checked against official documentation: **10 October 2026**. Kimi's plan names and quota rules have changed recently; verify against the [membership page](https://www.kimi.com/code/docs/en/kimi-code/membership.html) before relying on specifics.

## How quota works

- **One pool:** Kimi on the web, Kimi Code (CLI, Desktop, VS Code) and API keys share the same membership quota.
- **Rolling 5-hour rate window:** too many requests in a short window trigger rate limiting, which recovers automatically as the window rolls over.
- **Monthly total quota:** when the monthly total is reached, Kimi Code quota freezes until the monthly reset or an upgrade.
- **Legacy-plan members:** quota refreshes every 7 days from the subscription date and unused quota does not roll over; the 5-hour window still applies. New-plan members have no weekly limit — only the 5-hour window and the monthly total.
- **Devices:** keys and devices share quota; devices inactive 30+ days are unbound and restored with `/login`.

Check remaining quota with `/usage` in the CLI or the Kimi Code Console on the web.

## Membership gates for models

| Capability | New plans | Legacy plans |
|---|---|---|
| Kimi Code access | Plus and above | Andante and above |
| K3 (`k3`, `k3-256k`) | Plus and above | Moderato and above |
| 1M context (`k3`, `kimi-for-coding`) | Pro and above | Allegretto and above |
| HighSpeed (`kimi-for-coding-highspeed`) | Pro and above | Allegretto and above |

Pricing and tier names are current as of the verification date; the official plan page is the source of truth.

## Extra Usage

When subscription quota runs out, **Extra Usage** balance keeps requests flowing instead of erroring:

- Only subscribed members can enable it; Kimi web and Kimi Code share one balance.
- Subscription quota is always deducted first; Extra Usage is the fallback.
- Billing is usage-based in RMB at rates close to the Kimi Open Platform API; Kimi's own guidance is that heavy users are usually better served by upgrading the subscription.
- Set a **monthly spending cap** in settings — without one there is none. Balance does not expire and stacks across top-ups.
- Top-ups start at ¥25, capped at ¥3,000/day and ¥10,000 balance.

## Cost-control checklist

- [ ] Check `/usage` before long sessions and after escalations.
- [ ] Prefer `k3-256k` over `k3` when the task fits in 256K — Kimi's documentation prices it at about half the quota for the same results.
- [ ] Start a new session (`/new`) after switching models; switching invalidates the prompt cache and raises consumption.
- [ ] Dispatch sub-agents for isolation and parallelism, not by default — each consumes quota independently.
- [ ] Record accuracy, rework and elapsed time per run in the [evaluation worksheet](../templates/evaluation.csv), so model upgrades are decisions with evidence.
- [ ] State a session budget up front and stop when acceptance checks pass.

## Sources

- [Membership benefits](https://www.kimi.com/code/docs/en/kimi-code/membership.html)
- [Kimi Code overview](https://www.kimi.com/code/docs/en/) — `k3-256k` quota relationship
- [Kimi Code what's new](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) — Extra Usage launch, quota behaviors
