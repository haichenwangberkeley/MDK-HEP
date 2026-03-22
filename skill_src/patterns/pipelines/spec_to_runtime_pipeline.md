# Spec-to-Runtime Pipeline

Pattern: Pipeline

Derived from:
- `SKILL_NARRATIVE_TO_ANALYSIS_JSON_TRANSLATOR`
- `SKILL_JSON_SPEC_DRIVEN_EXECUTION`
- `SKILL_READ_SUMMARY_AND_VALIDATE`

## Stage ordering

| Stage | Inputs | Producing skills | Gate | Exit criteria |
|---|---|---|---|---|
| Preflight intent check | user request, repo paths | `runtime_and_preflight_wrapper.md` | `preflight_fact_check_reviewer.md` | run objective and paths are explicit |
| Spec generation or refinement | narrative or JSON | `analysis_spec_generator.md` | `preflight_fact_check_reviewer.md` | draft summary and gap report exist |
| Summary normalization | summary path | `summary_loader_wrapper.md` | `analysis_summary_reviewer.md` | normalized summary and diagnostics exist |
| Runtime contract finalization | normalized summary, overrides | `analysis_spec_generator.md` | `analysis_summary_reviewer.md` | execution contract and deviations log are reviewer-approved |

## Gates

- no downstream stage may start without a reviewed normalized summary
- all runtime overrides must be logged before sample processing

## Dependencies

- `../shared/hep_domain_guardrails.md`
- `../shared/pipeline_logging_contract.md`

## Escalation paths

- escalate when the summary cannot be made valid without inventing physics content
- escalate when unblinding or luminosity scope is requested but not approved explicitly

## Logging requirements

- record every assumption, override, and unresolved field
- record which summary path became the authoritative run input

## Related skills

- `hep_analysis_meta_pipeline.md`
- `../inversions/analysis_router_inversion.md`
