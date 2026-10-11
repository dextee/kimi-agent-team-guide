[Home](../README.md) · [Models, context and effort](models-context-effort.md) · [Workflow recipes](workflows.md)

Checked against official documentation: **10 October 2026**.

# 24-task selector

Pick a starting point, then escalate only when the trigger fires. Model names are Kimi Code model IDs; effort levels apply to K3 and K2.8 Preview. These assignments are this guide's editorial recommendations, not benchmark results.

| # | Task | Start with | Escalate when | Evidence of completion |
|---|---|---|---|---|
| 1 | Locate code or config in an unfamiliar repo | kimi-for-coding / low | The area spans many modules | Paths, symbols and excerpts with file references |
| 2 | Mechanical edit (rename, format, sweep) | kimi-for-coding-highspeed | Three failed attempts at the same edit | Diff shows only the intended mechanical change |
| 3 | Implement a well-specified feature | kimi-for-coding / high | Requirements conflict mid-build | Changed files plus real test or build output |
| 4 | Design a feature before building | k3-256k / max | Tradeoffs remain unresolved after one pass | Plan with alternatives, chosen tradeoffs, acceptance checks |
| 5 | Fix a hard bug | kimi-for-coding / high | Two wrong hypotheses; then k3-256k / max | Reproduction, root cause, fix and regression check |
| 6 | Review a routine change | kimi-for-coding / high | Findings contradict the implementer's claims | Severity-ranked findings with file:line evidence |
| 7 | Audit a consequential release | k3-256k / max | The corpus exceeds 256K tokens; then k3 | Per-requirement verdicts with evidence |
| 8 | Refactor across many files | kimi-for-coding / high | Behavior changes are hard to isolate; then k3-256k / max | Green tests plus before/after structure notes |
| 9 | Migrate data or schema | k3-256k / max | Rollback path is unclear | Migration plan, rollback plan, verification queries |
| 10 | Reconcile conflicting sources | k3-256k / high | Evidence exceeds context; then k3 | Claims bound to sources, conflicts stated, verdicts |
| 11 | Technology-choice research | kimi-for-coding / high | Decision is consequential or hard to reverse | Comparison table with dated sources |
| 12 | Draft a proposal or document | kimi-for-coding / low | Stakes or scrutiny rise | Structured draft with claims marked verified/unverified |
| 13 | Edit verified material for an audience | kimi-for-coding / low | Message must survive expert review | Revised text; hedges and attributions preserved |
| 14 | Summarize a long document | k3-256k / low | Document exceeds 256K; then k3 | Summary with section references |
| 15 | Analyze a whole large codebase | k3 / max | — | Module map, dependency notes, risk list |
| 16 | Generate repetitive test cases | kimi-for-coding-highspeed | Coverage logic becomes subtle | Test files plus a list of covered cases |
| 17 | Triage a queue of similar items | kimi-for-coding-highspeed | Classification repeatedly wrong | Labeled items plus an exception list |
| 18 | Repair a broken document or config | kimi-for-coding / low | Failure cause stays hidden after two looks | Working artifact plus what was wrong |
| 19 | Prepare a demo with sample data | kimi-for-coding / high | Demo must carry a business claim | Runnable demo plus stated limitations |
| 20 | Investigate an incident | k3-256k / max | Timeline evidence conflicts | Timeline, contributing causes, recommended action |
| 21 | Plan a large migration | k3-256k / max | Whole-system coupling emerges; then k3 | Phased plan with ownership and checkpoints |
| 22 | Quick question on your own codebase | main agent, no sub-agent | Answer changes a consequential decision | Direct answer with file reference |
| 23 | Rapid prototype to learn a question | kimi-for-coding / high | Prototype will become production | Working prototype plus its known gaps |
| 24 | Long-running autonomous objective | kimi-for-coding lead; k3 for hard steps | Goal stalls across repeated turns | Completed checks with a stop rule recorded |

Rules of thumb: below ~a screenful of reasoning, stay on `kimi-for-coding` and let effort do the work; reserve K3 for ambiguity, long context or consequence; reserve HighSpeed for loops, not thinking.

[Workflow recipes](workflows.md) turn these rows into complete hand-offs.
