# Full PR review report

Read this reference only for a full PR review. Use all eleven section names below in this order. Empty sections use `None.` or the specified no-issue text. Do not force findings, lessons, questions, or diagrams. Keep repeated issues in Findings and reference their identifiers elsewhere. The finding criteria and fields are defined in `SKILL.md`; do not maintain a second rubric here.

# 1. Verdict

**Verdict:** 🟢 Ready to merge | 🟡 Needs attention | 🔴 Blocked  
**Confidence:** Low | Medium | High  
**Reviewed revision:** Head commit or verified revision reference.

Give the assessment and at most three reasons. State material access or verification limitations.

- **Ready to merge:** No identified blockers, sufficient evidence, and relevant required checks satisfied.
- **Needs attention:** A decision, correction, pending check, or material verification gap remains.
- **Blocked:** A confirmed issue or unmet mandatory requirement prevents merging.

Unavailable evidence is not itself a defect, but may prevent a confident recommendation. Confidence describes evidence strength and coverage, not issue severity.

# 2. Jira summary

Orient a reviewer who may not have read Jira. For parent and subtask, identify both **Story** and **PR work item**. Otherwise identify **Ticket**. Link each using its real key, meaningful summary, and verified Jira URL. If unavailable, identify the requirement source actually used.

### Goal

One to three sentences describing the business or user goal.

### Key requirements

Only the requirements needed to understand this PR; do not copy the ticket.

### Relevant clarification

Accepted clarifications, scope boundaries, or unresolved conflicts materially affecting interpretation. Otherwise, `None.`

# 3. What changed

At most approximately five bullets explaining user-visible or operational behavior, major technical changes, affected modules/domains, and important design decisions. Describe resulting behavior, not editing history.

# 4. How it works

Explain important execution/data flow and responsibilities. Cover the business rules, state, contracts, persistence, permissions, integrations, and failure handling relevant to this change. Use diagrams or short snippets when useful; do not enumerate all files.

# 5. Jira coverage

| Requirement / AC | Implementation | Verification | Evidence |
| --- | --- | --- | --- |
| Actual identifier and brief requirement | Met / Partial / Missing / Unclear / Outside scope | Covered / Partial / Not found / Not inspected / Not applicable | Relevant code, test, or execution reference |

Include every relevant AC without inventing identifiers. Separate implementation from test coverage. "Not found" means the relevant area was inspected; "Not inspected" means coverage is unknown. Identify obligations owned elsewhere and dependencies affecting readiness. Names, tags, PR descriptions, and automated summaries are not proof.

# 6. Does it fit POEX?

### ✅ Matches existing patterns

Meaningful matches with concrete repository examples; no generic praise.

### 🟡 Differences worth reviewing

Deviations requiring a conscious decision, with their benefit or cost. Do not automatically label them defects.

### ❌ Inconsistencies

Concrete conflicts with applicable guidance, supported patterns, or responsibility boundaries. Reference findings where appropriate. Use `None.` for empty subsections.

# 7. Tests & CI

Summarize what relevant tests establish, meaningful gaps or test complexity, Jira traceability, and CI at the reviewed revision.

CI states: ✅ Passing · ❌ Failing · 🟡 Pending · ❓ Unavailable.

Distinguish inspected results from tests executed. Separate PR-attributable and unrelated failures when evidence permits. Identify the behavior or regression any recommended test would protect.

# 8. Out-of-scope changes

Classify meaningful candidates: ✅ In scope · 🟡 Adjacent / defensible · 🔴 Out of scope.

For a material candidate:

**Change:** ...  
**Relationship to the task:** ...  
**Risk or review cost:** ...  
**Recommendation:** Keep here / reduce / separate.

Apply the scope and contract criteria from `SKILL.md`. If none: `✅ No material out-of-scope changes found.`

# 9. Findings

Use the finding fields, severity, and disposition rules in `SKILL.md`, with stable identifiers. Show material uncertainty. Keep any requested comment-by-comment assessment distinct from actionable findings.

If none: `✅ No actionable findings.`

# 10. What to learn from this PR

Only lessons that help the reviewer understand unfamiliar concepts or judge this PR. Explain rationale and meaningful alternatives where useful. Do not repeat findings or force educational content. If none, use `None.`

# 11. Questions for the author

At most three unresolved questions whose answers could materially change the assessment. State what decision each affects. Do not ask what accessible sources already answer or disguise a verified defect as a question. If none, use `None.`
