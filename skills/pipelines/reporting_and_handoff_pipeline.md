# Reporting and Handoff Pipeline

Pattern: Pipeline

Derived from:
- `SKILL_PLOTTING_AND_REPORT`
- `SKILL_DATA_MC_DISCREPANCY_SANITY_CHECK`
- `SKILL_ENFORCEMENT_PRE_HANDOFF_GATE`
- `SKILL_FINAL_REPORT_REVIEW_AND_HANDOFF`

## Stage ordering

| Stage | Inputs | Producing skills | Gate | Exit criteria |
|---|---|---|---|---|
| Plot and report assembly | reviewed physics artifacts | `report_package_generator.md`, `report_packaging_wrapper.md` | `blinding_and_visualization_reviewer.md` | report draft, plot manifest, and captions exist |
| Discrepancy audit | report draft, plots, yields | `data_mc_discrepancy_reviewer.md` | same reviewer | discrepancy audit exists even for zero-issue runs |
| Handoff enforcement | report package, enforcement artifacts | `reproducibility_and_handoff_reviewer.md` | same reviewer | enforcement handoff gate is `ok` |
| Failure extraction | reviewer findings and run logs | `failure_to_skill_inversion.md` | `reproducibility_and_handoff_reviewer.md` | handoff package includes remediation or candidate skill notes |

## Gates

- no final handoff without an explicit discrepancy artifact
- no final handoff without an explicit enforcement gate result

## Dependencies

- `skills/shared/evidence_requirements.md`
- `skills/shared/pipeline_logging_contract.md`

## Escalation paths

- escalate if the report would have to omit a central blocker to appear complete
- escalate if a missing artifact would force the reviewer to infer handoff readiness

## Logging requirements

- log report paths, plot manifest paths, discrepancy verdicts, and final handoff status
- attach candidate-skill notes when repeated failures were observed

## Related skills

- `skills/pipelines/hep_analysis_meta_pipeline.md`
- `skills/reviewers/reproducibility_and_handoff_reviewer.md`
