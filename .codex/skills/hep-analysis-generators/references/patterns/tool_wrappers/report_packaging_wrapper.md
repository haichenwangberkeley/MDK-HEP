# Report Packaging Wrapper

Pattern: Tool Wrapper

Derived from:
- `SKILL_PLOTTING_AND_REPORT`
- `SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW`

## When to use

Use this wrapper when the agent needs repository code to assemble plots, report text, or final package artifacts after the upstream artifacts have already been generated and reviewed.

## Inputs

- normalized summary
- fit and significance artifacts
- registry and normalization artifacts
- discrepancy and blinding artifacts
- output and reports directories

## Outputs

- report artifacts under `outputs/report/`
- rendered final report under `reports/`
- plot manifests and artifact link inventories

## Preconditions

- required statistical and validation artifacts exist
- blinding policy and discrepancy posture are explicit

## Postconditions

- the report package is reviewer-ready
- plot embedding and caption evidence exist

## Call procedure

1. Use the integrated pipeline via `.rootenv/bin/python -m analysis.cli run` when report assembly should stay synchronized with upstream production.
2. Use `analysis.report.make_report.build_report` through a controlled Python entrypoint only when focused report regeneration is required and the inputs are frozen.

## Failure modes

- report text describes artifacts that were not produced
- plots are cited by path only instead of embedded with captions
- expected and observed significance are conflated

## Verification expectations

- report markdown exists
- plot manifests exist
- final reviewers can trace narrative claims to concrete artifacts

## Related skills

- `../generators/report_package_generator.md`
- `../reviewers/blinding_and_visualization_reviewer.md`
- `../pipelines/reporting_and_handoff_pipeline.md`
