# Analysis Summary Reviewer

Pattern: Reviewer

Derived from:
- `SKILL_READ_SUMMARY_AND_VALIDATE`
- `SKILL_JSON_SPEC_DRIVEN_EXECUTION`

## Review scope

Verify that the normalized analysis summary, partition semantics, and execution contract are internally consistent and precise enough for downstream sample, selection, and fit stages.

## Required evidence

- `outputs/summary.normalized.json`
- validation diagnostics and overlap policy artifacts
- execution contract and deviations log
- partition spec when categories or regions are already materialized

## Criteria

- `pass`: all cross references resolve and the runtime contract matches the summary
- `conditional_pass`: non-blocking cosmetic or naming issues are logged
- `block`: unresolved region, fit, observable, or overlap references remain
- `fail`: the summary is internally contradictory or the runtime contract silently dropped required scope

## Common failure modes

- fit regions or reported results reference missing region IDs
- overlap policy missing for SR and CR pairs used together
- runtime overrides not recorded
- category or observable names drift between summary and generated artifacts

## Required remediation guidance

- use `skills/tool_wrappers/summary_loader_wrapper.md` to regenerate normalized artifacts
- use `skills/generators/analysis_spec_generator.md` for summary contract repair
- use `skills/generators/event_model_and_partition_generator.md` when the summary is valid but partitions are incomplete

## Related skills

- `skills/pipelines/spec_to_runtime_pipeline.md`
- `skills/shared/hep_domain_guardrails.md`
