# Analysis Router Inversion

Pattern: Inversion

Derived from:
- `SKILL.md` in the source pack
- `SKILL_SKILLS_PACK_INDEX`
- the legacy pack index
- the legacy routing guide

## Trigger condition

Use this inversion when the next action is unclear, when the workflow starts from a blocker or missing artifact instead of a clean stage boundary, or when multiple candidate skills look plausible.

## Decision structure

1. Identify the blocker in one sentence.
2. Classify the blocker as one of:
   - missing specification
   - missing runtime readiness
   - ambiguous sample semantics
   - missing region or selection artifacts
   - statistical gate failure
   - reporting or handoff failure
3. Choose the smallest skill set that can close that blocker.
4. Prefer the branch with the smallest write scope and the closest downstream handoff.

## Branch criteria

- Missing or ambiguous summary: route to `spec_to_runtime_pipeline.md`.
- Missing sample registry, normalization, or nominal mapping: route to `sample_semantics_generator.md` and its reviewer.
- Missing executable regions or yields: route to `event_model_and_partition_generator.md` or `selection_and_yield_generator.md`.
- Failed smoothing, effective-lumi, or backend gate: route to `blinding_and_fit_policy_inversion.md` and `statistical_readiness_reviewer.md`.
- Failed discrepancy or handoff gate: route to `reporting_and_handoff_pipeline.md` or `failure_to_skill_inversion.md`.

## Required evidence per branch

- normalized summary or explicit gap report
- current outputs inventory
- reviewer findings or blocking artifact
- prior decision records that constrain the next branch

## Output decision record

Write a decision record using `../shared/decision_record_template.md` that names:

- blocker
- chosen next skill or pipeline
- rejected alternatives
- required reviewer before advancement

## Related skills

- `../pipelines/hep_analysis_meta_pipeline.md`
- `../shared/artifact_matrix.md`
