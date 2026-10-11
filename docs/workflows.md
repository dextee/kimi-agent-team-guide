[Home](../README.md) · [24-task selector](task-selector.md) · [Agent files](../agents/README.md)

Checked against official documentation: **10 October 2026**. Routes are editorial starting points to evaluate on your own workload.

# Workflow recipes

Twelve copy-adaptable workflows. Each names a recommended model and effort, the agents to involve, the hand-off between them and the completion check. These are starting configurations to evaluate on your own workload — not benchmarked team results.

Use the [delegation brief](../README.md#a-better-delegation-brief) when dispatching to a named agent.

### 1. Feature delivery

- **Route:** explore (kimi-for-coding / low) → implementer (kimi-for-coding / high) → reviewer (kimi-for-coding / high).
- **Hand-off:** explorer returns a file map; implementer returns changed files and verification output; reviewer returns severity-ranked findings.
- **Completion:** acceptance checks pass on the real build; reviewer reports no open high-severity findings.

### 2. Hard bug

- **Route:** explore → implementer (kimi-for-coding / high). Escalate to k3-256k / max after two wrong hypotheses.
- **Hand-off:** each failed hypothesis goes back as new evidence, not as a retry of the same prompt.
- **Completion:** reproduction fails after the fix; a regression check exists for the original trigger.

### 3. Migration design

- **Route:** explorer → architect (k3-256k / max) → implementer per phase.
- **Hand-off:** architect returns phases with ownership, dependencies, checkpoints and a rollback path.
- **Completion:** each phase lands with its checkpoint verified; rollback path is exercised at least once on sample data.

### 4. Research brief

- **Route:** researchers (kimi-for-coding / high) split by question → editor (kimi-for-coding / low) after evidence is reconciled.
- **Hand-off:** researcher returns claims bound to dated sources and flags conflicts; editor never adds new claims.
- **Completion:** every claim carries a source; every conflict is stated, not smoothed over.

### 5. Consequential proposal

- **Route:** researcher → architect (k3-256k / max for the recommendation logic) → editor.
- **Hand-off:** the proposal separates verified facts, stated assumptions and open questions into labeled sections.
- **Completion:** a skeptical reader can trace each load-bearing claim to its evidence.

### 6. Data reconciliation

- **Route:** explorer → implementer (kimi-for-coding / high) with objective checks → auditor (k3-256k / max) on exceptions only.
- **Hand-off:** mismatches land in an exception list with reasons; never silently "fixed".
- **Completion:** totals match between source and target; the exception list is reviewed and dispositioned.

### 7. Cross-file refactor

- **Route:** explorer → implementer per file area → reviewer; escalate to k3-256k / max when behavior isolation gets hard.
- **Hand-off:** one owner per writable area at a time.
- **Completion:** behavior-preserving tests stay green; structure notes record what moved and why.

### 8. Long-document work

- **Route:** main agent on k3-256k / low-high; k3 when the document exceeds 256K.
- **Hand-off:** summarize by section first; then work section by section with references.
- **Completion:** every derived claim references a section; nothing beyond the document's scope is asserted.

### 9. Rapid mechanical loop

- **Route:** session on kimi-for-coding-highspeed; no sub-agents for single-file work.
- **Hand-off:** batch the mechanical edits; verify the batch once, not per edit.
- **Completion:** batch diff shows only intended changes; step up to kimi-for-coding when a failure resists three attempts.

### 10. Repository audit

- **Route:** explorer → auditor (k3-256k / max, or k3 for very large repos) with the [auditor agent](../agents/guide_auditor.md).
- **Hand-off:** requirements enumerated first; auditor closes each with evidence or flags it unresolved.
- **Completion:** per-requirement verdict table; discrepancies reported with file references.

### 11. Document repair

- **Route:** explorer → implementer (kimi-for-coding / low) → editor.
- **Hand-off:** the repair note lists what was broken and what changed, so the fix itself is auditable.
- **Completion:** the artifact renders/builds; the change list contains no silent content changes.

### 12. Budget-sensitive automation

- **Route:** highspeed for mechanical passes; kimi-for-coding / low for drafting; sub-agents only where isolation or parallelism pays.
- **Hand-off:** a session budget is stated up front; the loop stops when acceptance checks pass, not when the budget runs out silently.
- **Completion:** the [evaluation worksheet](../templates/evaluation.csv) records accuracy, rework and elapsed time for the run; `/usage` confirms the quota actually spent.

Escalation is a control, not a failure: unclear requirements, conflicting evidence, repeated failure or rising consequence are the four triggers that justify a stronger model or effort level.
