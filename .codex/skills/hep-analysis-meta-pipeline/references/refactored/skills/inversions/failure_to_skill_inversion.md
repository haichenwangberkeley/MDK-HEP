# Failure-to-Skill Inversion

Pattern: Inversion

Derived from:
- `SKILL_EXTRACT_NEW_SKILL_FROM_FAILURE`
- `SKILL_DATA_MC_DISCREPANCY_SANITY_CHECK`

## Trigger condition

Use this inversion when a reviewer finds a recurring failure, a discrepancy remains unresolved, or the workflow uncovers a missing reusable capability.

## Decision structure

1. Classify the failure as one of:
   - implementation defect
   - missing evidence or logging
   - scientific ambiguity requiring human input
   - repeated workflow pattern that should become a reusable skill
2. Identify the smallest component that owns the problem.
3. Decide whether to repair locally, escalate, or propose a new skill.

## Branch criteria

- Single-run implementation bug: route to the owning wrapper or generator.
- Missing evidence: route to the reviewer-paired generator or pipeline stage.
- Scientific ambiguity without repository evidence: escalate to a human.
- Repeated failure with reusable structure: write a candidate skill note and include it in the handoff package.

## Required evidence per branch

- reviewer findings
- blocked artifacts
- prior run history or repeated occurrence evidence
- current assumptions and deviation logs

## Output decision record

Record:

- failure class
- owning component
- smallest remediation path
- whether a new skill candidate should be proposed
- whether human escalation is required

## Related skills

- `skills/reviewers/data_mc_discrepancy_reviewer.md`
- `skills/reviewers/reproducibility_and_handoff_reviewer.md`
