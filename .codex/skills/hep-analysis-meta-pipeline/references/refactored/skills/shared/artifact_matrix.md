# Artifact Matrix

| Stage | Primary artifacts | Primary generator or wrapper | Mandatory reviewer |
|---|---|---|---|
| Spec intake | analysis JSON draft, gap report, source trace, execution contract | `skills/generators/analysis_spec_generator.md`, `skills/tool_wrappers/summary_loader_wrapper.md` | `skills/reviewers/preflight_fact_check_reviewer.md`, `skills/reviewers/analysis_summary_reviewer.md` |
| Samples | sample registry, classification, norm table, nominal mapping | `skills/generators/sample_semantics_generator.md`, `skills/tool_wrappers/sample_registry_and_metadata_wrapper.md` | `skills/reviewers/nominal_sample_and_normalization_reviewer.md` |
| Event model and partitions | object definition record, partition spec, region definitions | `skills/generators/event_model_and_partition_generator.md`, `skills/tool_wrappers/selection_and_partition_wrapper.md` | `skills/reviewers/analysis_summary_reviewer.md` |
| Selections and yields | cut flows, yields, provenance | `skills/generators/selection_and_yield_generator.md` | `skills/reviewers/nominal_sample_and_normalization_reviewer.md` |
| Histogramming | template manifest, freeze manifest, cache provenance | `skills/generators/histogram_and_template_generator.md`, `skills/tool_wrappers/histogram_and_template_wrapper.md` | `skills/reviewers/statistical_readiness_reviewer.md` |
| Modeling | background strategy, CR and SR map, signal PDFs, spurious-signal outputs | `skills/generators/background_and_signal_model_generator.md` | `skills/reviewers/statistical_readiness_reviewer.md`, `skills/reviewers/blinding_and_visualization_reviewer.md` |
| Systematics and fits | nuisance model, workspaces, fit results, significance artifacts | `skills/generators/systematics_and_workspace_generator.md`, `skills/tool_wrappers/fit_and_significance_wrapper.md` | `skills/reviewers/statistical_readiness_reviewer.md` |
| Reporting | report markdown, plots, captions, artifact inventory | `skills/generators/report_package_generator.md`, `skills/tool_wrappers/report_packaging_wrapper.md` | `skills/reviewers/blinding_and_visualization_reviewer.md`, `skills/reviewers/data_mc_discrepancy_reviewer.md` |
| Handoff | run manifest, checkpoint log, enforcement gate, final review note | `skills/pipelines/reporting_and_handoff_pipeline.md` | `skills/reviewers/reproducibility_and_handoff_reviewer.md` |
