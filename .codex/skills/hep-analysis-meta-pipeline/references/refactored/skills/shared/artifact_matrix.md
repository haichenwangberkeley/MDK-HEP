# Artifact Matrix

| Stage | Primary artifacts | Primary generator or wrapper | Mandatory reviewer |
|---|---|---|---|
| Spec intake | analysis JSON draft, gap report, source trace, execution contract | `../generators/analysis_spec_generator.md`, `../tool_wrappers/summary_loader_wrapper.md` | `../reviewers/preflight_fact_check_reviewer.md`, `../reviewers/analysis_summary_reviewer.md` |
| Samples | sample registry, classification, norm table, nominal mapping | `../generators/sample_semantics_generator.md`, `../tool_wrappers/sample_registry_and_metadata_wrapper.md` | `../reviewers/nominal_sample_and_normalization_reviewer.md` |
| Event model and partitions | object definition record, partition spec, region definitions | `../generators/event_model_and_partition_generator.md`, `../tool_wrappers/selection_and_partition_wrapper.md` | `../reviewers/analysis_summary_reviewer.md` |
| Selections and yields | cut flows, yields, provenance | `../generators/selection_and_yield_generator.md` | `../reviewers/nominal_sample_and_normalization_reviewer.md` |
| Histogramming | template manifest, freeze manifest, cache provenance | `../generators/histogram_and_template_generator.md`, `../tool_wrappers/histogram_and_template_wrapper.md` | `../reviewers/statistical_readiness_reviewer.md` |
| Modeling | background strategy, CR and SR map, signal PDFs, spurious-signal outputs | `../generators/background_and_signal_model_generator.md` | `../reviewers/statistical_readiness_reviewer.md`, `../reviewers/blinding_and_visualization_reviewer.md` |
| Systematics and fits | nuisance model, workspaces, fit results, significance artifacts | `../generators/systematics_and_workspace_generator.md`, `../tool_wrappers/fit_and_significance_wrapper.md` | `../reviewers/statistical_readiness_reviewer.md` |
| Reporting | report markdown, plots, captions, artifact inventory | `../generators/report_package_generator.md`, `../tool_wrappers/report_packaging_wrapper.md` | `../reviewers/blinding_and_visualization_reviewer.md`, `../reviewers/data_mc_discrepancy_reviewer.md` |
| Handoff | run manifest, checkpoint log, enforcement gate, final review note | `../pipelines/reporting_and_handoff_pipeline.md` | `../reviewers/reproducibility_and_handoff_reviewer.md` |
