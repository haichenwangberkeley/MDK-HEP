# Reproducibility and Handoff Reviewer

Pattern: Reviewer

Derived from:
- `SKILL_FULL_STATISTICS_EXECUTION_POLICY`
- `SKILL_SKILL_REFRESH_AND_CHECKPOINTING`
- `SKILL_SMOKE_TESTS_AND_REPRODUCIBILITY`
- `SKILL_ENFORCEMENT_PRE_HANDOFF_GATE`
- `SKILL_FINAL_REPORT_REVIEW_AND_HANDOFF`

## Review scope

Verify that the run used the approved statistics scope, produced reproducibility evidence, passed mandatory checkpoint gates, and is genuinely ready for handoff.

## Required evidence

- run manifest
- smoke or reproducibility artifacts
- skill refresh or checkpoint logs
- enforcement handoff gate
- final report package
- skill extraction summary

## Criteria

- `pass`: handoff is supported by full evidence and all mandatory gates pass
- `conditional_pass`: non-blocking follow-up items remain but central claims are intact
- `block`: any mandatory gate artifact is missing or failing
- `fail`: the run claims central results without full-statistics or without required enforcement evidence

## Common failure modes

- partial-statistics run presented as final
- checkpoint artifacts missing at stage boundaries
- enforcement handoff gate absent or failing
- no skill extraction summary after a completed run

## Required remediation guidance

- rerun the blocked stage through the central pipeline or the smallest matching wrapper
- use `skills/inversions/failure_to_skill_inversion.md` to classify recurring failure modes
- escalate to a human if central-result scope cannot be recovered without changing the approved run contract

## Related skills

- `skills/pipelines/reporting_and_handoff_pipeline.md`
- `skills/shared/pipeline_logging_contract.md`
