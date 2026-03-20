# Sample Strategy Inversion

Pattern: Inversion

Derived from:
- `SKILL_MC_SAMPLE_DISAMBIGUATION_AND_NOMINAL_SELECTION`
- `SKILL_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS`
- `SKILL_13TEV25_DETAILS`

## Trigger condition

Use this inversion when the workflow must work backward from an analysis target or a sample ambiguity to determine the correct nominal sample set, process role, or CR and SR strategy.

## Decision structure

1. Identify the central analysis target.
2. Determine which processes are signal, background, or data for that target.
3. For each central process, decide whether there is exactly one nominal sample set.
4. Decide whether any background should be constrained from CR to SR and what overlap policy applies.

## Branch criteria

- If DSIDs and metadata establish a unique nominal sample set, accept it and record the evidence.
- If only filenames are available, treat the choice as provisional and block central claims until the reviewer accepts it.
- If the H to gammagamma background template is under discussion, require an explicit nominal diphoton sample choice and reject silent merges of low-statistics auxiliary samples.
- If CR and SR overlap is non-zero, require explicit justification or block the branch.

## Required evidence per branch

- sample registry draft
- metadata resolution output
- open-data dataset facts
- reviewed summary and partition artifacts

## Output decision record

Record:

- analysis target
- selected nominal samples by process
- alternative samples by process
- constraint intent for each background
- blocking ambiguities

## Related skills

- `skills/generators/sample_semantics_generator.md`
- `skills/reviewers/nominal_sample_and_normalization_reviewer.md`
