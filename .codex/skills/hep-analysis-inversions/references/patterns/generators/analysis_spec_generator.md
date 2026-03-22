# Analysis Spec Generator

Pattern: Generator

Derived from:
- `SKILL_NARRATIVE_TO_ANALYSIS_JSON_TRANSLATOR`
- `SKILL_JSON_SPEC_DRIVEN_EXECUTION`

## Purpose

Create or refine the analysis specification so the validated summary, execution contract, and deviation log become the only authoritative inputs to the runtime pipeline.

## When to use

- a user provided narrative instructions rather than a ready analysis JSON
- the runtime pipeline needs an explicit `spec_to_runtime` contract
- summary validation found missing but representable fields

## Required inputs

- narrative description or analysis JSON
- repository schema expectations
- approved runtime constraints

## Outputs

- analysis JSON draft or revised JSON
- gap report
- source trace map
- execution contract
- deviations-from-spec log

## Generation steps

1. Extract objective, target process, observables, regions, fit scope, and result types.
2. Mark unknown values explicitly instead of guessing.
3. Normalize naming so the summary loader can validate it.
4. Record every assumption and every user override.
5. Produce an execution contract that names summary path, inputs path, outputs path, blinding mode, luminosity, and primary fit backend expectation.

## Output contract

- no field invented without being labeled as an assumption
- every unresolved item appears in the gap report
- every runtime override is listed with source and expected impact

## Constraints

- never fabricate physics numbers
- preserve the distinction between user-provided facts and agent assumptions
- do not bypass the summary reviewer

## Related skills

- `../tool_wrappers/summary_loader_wrapper.md`
- `../reviewers/preflight_fact_check_reviewer.md`
- `../reviewers/analysis_summary_reviewer.md`
- `../pipelines/spec_to_runtime_pipeline.md`
