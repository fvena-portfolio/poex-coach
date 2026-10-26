# Task-planning readiness

Read this reference only when assessing work before implementation. Do not load or reproduce the full PR-review template.

## Readiness decision

Use the canonical POEX Coach states and identify the target gate separately:

- `SUPERADO`: the target gate is satisfied. For `ready to specify`, product behavior and the current system are understood and material decisions are resolved. For `ready to implement`, requirements, scope, contracts, validation, dependencies, and the first increment are sufficiently defined.
- `REVISAR`: evidence, understanding, alignment, or a material decision is incomplete.
- `BLOQUEADO`: an external decision, dependency, or inaccessible source prevents progress.

State the target gate and evidence boundary. Do not infer readiness from the existence of Jira text, a plan, or generated documentation.

## Assessment

Establish:

1. Official goal, current requirements, accepted clarifications, priority, and exclusions.
2. Current behavior and the end-to-end flow relevant to the task.
3. Maintained precedents, repository guidance, and ownership of affected responsibilities.
4. Producers, consumers, contracts, permissions, data, errors, observability, deployment, and compatibility when applicable.
5. Material questions, decision owners, dependencies, and required team alignment.
6. Proposed behavioral change without inventing implementation detail.
7. Validation seams and the evidence each criterion will require.
8. The smallest coherent first increment.
9. Scope risks, speculative work, and unrelated improvements.

Use proportional depth. Investigate accessible facts before asking questions. Surface conflicts between Jira, code, tests, documentation, and team decisions.

## Coverage

Use a compact matrix when more than one criterion or contract is involved:

| Requirement or decision | Current behavior | Planned behavior or responsibility | Intended verification | Status |
| --- | --- | --- | --- | --- |
| Verified source and brief requirement | Evidence | Plan or unresolved decision | Observable evidence | Covered / Partial / Missing / Unclear |

A planned test name, document, or ticket is not verification evidence.

## Output

Present:

1. Readiness state and confidence.
2. At most three reasons for the state.
3. Confirmed facts and evidence boundary.
4. Coverage gaps, contradictions, and decisions.
5. Scope and contract risks.
6. Recommended next gate or one concrete action.

Do not produce a PR verdict, findings about nonexistent code, CI status, or merge recommendation.
