# Report Package Generator

Pattern: Generator

Derived from:
- `SKILL_PLOTTING_AND_REPORT`
- `SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW`

## Purpose

Generate the plot-rich, note-style report package that communicates the analysis while preserving traceability to the artifacts and reviewer outcomes that support each claim.

## When to use

- fit, significance, blinding, discrepancy, and normalization artifacts exist
- the workflow is ready to produce a human-readable report and a machine-readable handoff package

## Required inputs

- normalized summary
- sample semantics and normalization artifacts
- cut-flow and yield artifacts
- fit and significance artifacts
- blinding and discrepancy artifacts
- plot manifest inputs

## Outputs

- report markdown
- final report in `reports/`
- plot manifest and artifact inventory
- report-ready sample selection summary
- report appendix inputs for assumptions, deviations, and unresolved issues

## Generation steps

1. Assemble the required sections in a stable order.
2. Embed plots inline and place a caption directly next to each embedded image.
3. Distinguish central nominal samples from alternatives in the narrative.
4. State expected versus observed significance explicitly.
5. Append assumptions, deviations, unresolved issues, and reviewer-linked evidence.

## Output contract

- the report distinguishes data and MC sample descriptions
- the report cites only central claims that passed reviewer gates
- blocked central claims stay blocked in the narrative

## Constraints

- do not hide data-MC discrepancies
- do not cite plot paths without embedding the plots
- do not mix observed and expected significance language

## Related skills

- `../tool_wrappers/report_packaging_wrapper.md`
- `../reviewers/blinding_and_visualization_reviewer.md`
- `../reviewers/data_mc_discrepancy_reviewer.md`
- `../pipelines/reporting_and_handoff_pipeline.md`
