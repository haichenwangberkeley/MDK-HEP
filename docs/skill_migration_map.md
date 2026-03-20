# Skill Migration Map

Source root: `/Users/haichenwang/Work/analysis-automation/.codex/skills/hep-meta-first`

Paths below are relative to that root for old files and relative to `GCT-hep-meta` for new files.

Interpretation note:

- Most rows map into one of the five executable patterns.
- Some source content now lives in `skills/shared/` or `docs/` because it is reusable support material rather than a standalone executable skill in the new system. Those rows are labeled `Shared support` or `Documentation` in the target-pattern column on purpose.

## Skill-to-skill mapping

### Meta entry, specification, and governance

| Old skill or file | Old source path | New skill or file | New target path | Target pattern | Migration mode |
|---|---|---|---|---|---|
| `hep-meta-first` | `SKILL.md` | `analysis_router_inversion.md` | `skills/inversions/analysis_router_inversion.md` | Inversion | split and adapted |
| `hep-meta-first` | `SKILL.md` | `hep_analysis_meta_pipeline.md` | `skills/pipelines/hep_analysis_meta_pipeline.md` | Pipeline | split and adapted |
| `SKILL_SKILLS_PACK_INDEX` | `references/SKILL_SKILLS_PACK_INDEX.md` | `README_skills.md` | `README_skills.md` | Pipeline support | rewritten and merged |
| `SKILL_SKILLS_PACK_INDEX` | `references/SKILL_SKILLS_PACK_INDEX.md` | `INDEX.md` | `skills/INDEX.md` | Pipeline support | rewritten and merged |
| `SKILL_SKILLS_PACK_INDEX` | `references/SKILL_SKILLS_PACK_INDEX.md` | `hep_analysis_meta_pipeline.md` | `skills/pipelines/hep_analysis_meta_pipeline.md` | Pipeline | adapted and merged |
| `SKILL_BOOTSTRAP_REPO` | `references/SKILL_BOOTSTRAP_REPO.md` | `runtime_and_preflight_wrapper.md` | `skills/tool_wrappers/runtime_and_preflight_wrapper.md` | Tool Wrapper | split and adapted |
| `SKILL_BOOTSTRAP_REPO` | `references/SKILL_BOOTSTRAP_REPO.md` | `reproducibility_and_handoff_reviewer.md` | `skills/reviewers/reproducibility_and_handoff_reviewer.md` | Reviewer | split and merged |
| `SKILL_AGENT_PRE_FLIGHT_FACT_CHECK` | `references/SKILL_AGENT_PRE_FLIGHT_FACT_CHECK.md` | `preflight_fact_check_reviewer.md` | `skills/reviewers/preflight_fact_check_reviewer.md` | Reviewer | adapted |
| `SKILL_NARRATIVE_TO_ANALYSIS_JSON_TRANSLATOR` | `references/SKILL_NARRATIVE_TO_ANALYSIS_JSON_TRANSLATOR.md` | `analysis_spec_generator.md` | `skills/generators/analysis_spec_generator.md` | Generator | adapted |
| `SKILL_JSON_SPEC_DRIVEN_EXECUTION` | `references/SKILL_JSON_SPEC_DRIVEN_EXECUTION.md` | `analysis_spec_generator.md` | `skills/generators/analysis_spec_generator.md` | Generator | merged and adapted |
| `SKILL_JSON_SPEC_DRIVEN_EXECUTION` | `references/SKILL_JSON_SPEC_DRIVEN_EXECUTION.md` | `spec_to_runtime_pipeline.md` | `skills/pipelines/spec_to_runtime_pipeline.md` | Pipeline | split and adapted |
| `SKILL_READ_SUMMARY_AND_VALIDATE` | `references/SKILL_READ_SUMMARY_AND_VALIDATE.md` | `summary_loader_wrapper.md` | `skills/tool_wrappers/summary_loader_wrapper.md` | Tool Wrapper | split |
| `SKILL_READ_SUMMARY_AND_VALIDATE` | `references/SKILL_READ_SUMMARY_AND_VALIDATE.md` | `analysis_summary_reviewer.md` | `skills/reviewers/analysis_summary_reviewer.md` | Reviewer | split |
| `SKILL_FULL_STATISTICS_EXECUTION_POLICY` | `references/SKILL_FULL_STATISTICS_EXECUTION_POLICY.md` | `reproducibility_and_handoff_reviewer.md` | `skills/reviewers/reproducibility_and_handoff_reviewer.md` | Reviewer | merged |
| `SKILL_ENFORCEMENT_POLICY_DEFAULTS` | `references/SKILL_ENFORCEMENT_POLICY_DEFAULTS.md` | `blinding_and_fit_policy_inversion.md` | `skills/inversions/blinding_and_fit_policy_inversion.md` | Inversion | split and adapted |
| `SKILL_ENFORCEMENT_POLICY_DEFAULTS` | `references/SKILL_ENFORCEMENT_POLICY_DEFAULTS.md` | `hep_domain_guardrails.md` | `skills/shared/hep_domain_guardrails.md` | Shared support | merged and adapted |
| `SKILL_SKILL_REFRESH_AND_CHECKPOINTING` | `references/SKILL_SKILL_REFRESH_AND_CHECKPOINTING.md` | `pipeline_logging_contract.md` | `skills/shared/pipeline_logging_contract.md` | Shared support | split |
| `SKILL_SKILL_REFRESH_AND_CHECKPOINTING` | `references/SKILL_SKILL_REFRESH_AND_CHECKPOINTING.md` | `hep_analysis_meta_pipeline.md` | `skills/pipelines/hep_analysis_meta_pipeline.md` | Pipeline | split and merged |
| `SKILL_SKILL_REFRESH_AND_CHECKPOINTING` | `references/SKILL_SKILL_REFRESH_AND_CHECKPOINTING.md` | `reproducibility_and_handoff_reviewer.md` | `skills/reviewers/reproducibility_and_handoff_reviewer.md` | Reviewer | split and merged |
| `SKILL_EXTRACT_NEW_SKILL_FROM_FAILURE` | `references/SKILL_EXTRACT_NEW_SKILL_FROM_FAILURE.md` | `failure_to_skill_inversion.md` | `skills/inversions/failure_to_skill_inversion.md` | Inversion | adapted |

### Samples, normalization, and event model

| Old skill or file | Old source path | New skill or file | New target path | Target pattern | Migration mode |
|---|---|---|---|---|---|
| `SKILL_13TEV25_DETAILS` | `references/SKILL_13TEV25_DETAILS.md` | `open_data_dataset_facts.md` | `skills/shared/open_data_dataset_facts.md` | Shared support | merged and adapted |
| `SKILL_13TEV25_DETAILS` | `references/SKILL_13TEV25_DETAILS.md` | `sample_strategy_inversion.md` | `skills/inversions/sample_strategy_inversion.md` | Inversion | split |
| `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION` | `references/SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION.md` | `sample_registry_and_metadata_wrapper.md` | `skills/tool_wrappers/sample_registry_and_metadata_wrapper.md` | Tool Wrapper | split |
| `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION` | `references/SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION.md` | `sample_semantics_generator.md` | `skills/generators/sample_semantics_generator.md` | Generator | split |
| `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION` | `references/SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION.md` | `nominal_sample_and_normalization_reviewer.md` | `skills/reviewers/nominal_sample_and_normalization_reviewer.md` | Reviewer | split |
| `SKILL_MC_SAMPLE_DISAMBIGUATION_AND_NOMINAL_SELECTION` | `references/SKILL_MC_SAMPLE_DISAMBIGUATION_AND_NOMINAL_SELECTION.md` | `sample_strategy_inversion.md` | `skills/inversions/sample_strategy_inversion.md` | Inversion | adapted |
| `SKILL_MC_SAMPLE_DISAMBIGUATION_AND_NOMINAL_SELECTION` | `references/SKILL_MC_SAMPLE_DISAMBIGUATION_AND_NOMINAL_SELECTION.md` | `nominal_sample_and_normalization_reviewer.md` | `skills/reviewers/nominal_sample_and_normalization_reviewer.md` | Reviewer | split and merged |
| `SKILL_MC_NORMALIZATION_METADATA_STACKING` | `references/SKILL_MC_NORMALIZATION_METADATA_STACKING.md` | `sample_registry_and_metadata_wrapper.md` | `skills/tool_wrappers/sample_registry_and_metadata_wrapper.md` | Tool Wrapper | split |
| `SKILL_MC_NORMALIZATION_METADATA_STACKING` | `references/SKILL_MC_NORMALIZATION_METADATA_STACKING.md` | `sample_semantics_generator.md` | `skills/generators/sample_semantics_generator.md` | Generator | split |
| `SKILL_MC_NORMALIZATION_METADATA_STACKING` | `references/SKILL_MC_NORMALIZATION_METADATA_STACKING.md` | `nominal_sample_and_normalization_reviewer.md` | `skills/reviewers/nominal_sample_and_normalization_reviewer.md` | Reviewer | split and merged |
| `SKILL_EVENT_IO_AND_COLUMNAR_MODEL` | `references/SKILL_EVENT_IO_AND_COLUMNAR_MODEL.md` | `selection_and_partition_wrapper.md` | `skills/tool_wrappers/selection_and_partition_wrapper.md` | Tool Wrapper | split and adapted |
| `SKILL_EVENT_IO_AND_COLUMNAR_MODEL` | `references/SKILL_EVENT_IO_AND_COLUMNAR_MODEL.md` | `event_model_and_partition_generator.md` | `skills/generators/event_model_and_partition_generator.md` | Generator | split and merged |
| `SKILL_OBJECT_DEFINITIONS` | `references/SKILL_OBJECT_DEFINITIONS.md` | `event_model_and_partition_generator.md` | `skills/generators/event_model_and_partition_generator.md` | Generator | merged |
| `SKILL_CATEGORY_CHANNEL_REGION_PARTITIONING` | `references/SKILL_CATEGORY_CHANNEL_REGION_PARTITIONING.md` | `event_model_and_partition_generator.md` | `skills/generators/event_model_and_partition_generator.md` | Generator | merged |
| `SKILL_SELECTION_ENGINE_AND_REGIONS` | `references/SKILL_SELECTION_ENGINE_AND_REGIONS.md` | `selection_and_partition_wrapper.md` | `skills/tool_wrappers/selection_and_partition_wrapper.md` | Tool Wrapper | split |
| `SKILL_SELECTION_ENGINE_AND_REGIONS` | `references/SKILL_SELECTION_ENGINE_AND_REGIONS.md` | `selection_and_yield_generator.md` | `skills/generators/selection_and_yield_generator.md` | Generator | split and merged |
| `SKILL_CUT_FLOW_AND_YIELDS` | `references/SKILL_CUT_FLOW_AND_YIELDS.md` | `selection_and_yield_generator.md` | `skills/generators/selection_and_yield_generator.md` | Generator | adapted |

### Templates, modeling, and statistics

| Old skill or file | Old source path | New skill or file | New target path | Target pattern | Migration mode |
|---|---|---|---|---|---|
| `SKILL_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS` | `references/SKILL_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS.md` | `sample_strategy_inversion.md` | `skills/inversions/sample_strategy_inversion.md` | Inversion | split |
| `SKILL_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS` | `references/SKILL_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS.md` | `background_and_signal_model_generator.md` | `skills/generators/background_and_signal_model_generator.md` | Generator | split |
| `SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION` | `references/SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION.md` | `blinding_and_fit_policy_inversion.md` | `skills/inversions/blinding_and_fit_policy_inversion.md` | Inversion | split |
| `SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION` | `references/SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION.md` | `blinding_and_visualization_reviewer.md` | `skills/reviewers/blinding_and_visualization_reviewer.md` | Reviewer | split |
| `SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION` | `references/SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION.md` | `report_package_generator.md` | `skills/generators/report_package_generator.md` | Generator | split and merged |
| `SKILL_HISTOGRAMMING_AND_TEMPLATES` | `references/SKILL_HISTOGRAMMING_AND_TEMPLATES.md` | `histogram_and_template_wrapper.md` | `skills/tool_wrappers/histogram_and_template_wrapper.md` | Tool Wrapper | split |
| `SKILL_HISTOGRAMMING_AND_TEMPLATES` | `references/SKILL_HISTOGRAMMING_AND_TEMPLATES.md` | `histogram_and_template_generator.md` | `skills/generators/histogram_and_template_generator.md` | Generator | split |
| `SKILL_FREEZE_ANALYSIS_HISTOGRAM_PRODUCTS` | `references/SKILL_FREEZE_ANALYSIS_HISTOGRAM_PRODUCTS.md` | `histogram_and_template_wrapper.md` | `skills/tool_wrappers/histogram_and_template_wrapper.md` | Tool Wrapper | merged |
| `SKILL_BACKGROUND_TEMPLATE_SMOOTHING_POLICY` | `references/SKILL_BACKGROUND_TEMPLATE_SMOOTHING_POLICY.md` | `statistical_readiness_reviewer.md` | `skills/reviewers/statistical_readiness_reviewer.md` | Reviewer | merged |
| `SKILL_MC_EFFECTIVE_LUMI_COVERAGE_GATE` | `references/SKILL_MC_EFFECTIVE_LUMI_COVERAGE_GATE.md` | `statistical_readiness_reviewer.md` | `skills/reviewers/statistical_readiness_reviewer.md` | Reviewer | merged |
| `SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION` | `references/SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION.md` | `background_and_signal_model_generator.md` | `skills/generators/background_and_signal_model_generator.md` | Generator | split |
| `SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION` | `references/SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION.md` | `blinding_and_fit_policy_inversion.md` | `skills/inversions/blinding_and_fit_policy_inversion.md` | Inversion | split |
| `SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION` | `references/SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION.md` | `statistical_readiness_reviewer.md` | `skills/reviewers/statistical_readiness_reviewer.md` | Reviewer | split and merged |
| `SKILL_SYSTEMATICS_AND_NUISANCES` | `references/SKILL_SYSTEMATICS_AND_NUISANCES.md` | `systematics_and_workspace_generator.md` | `skills/generators/systematics_and_workspace_generator.md` | Generator | adapted |
| `SKILL_WORKSPACE_AND_FIT_PYHF` | `references/SKILL_WORKSPACE_AND_FIT_PYHF.md` | `fit_and_significance_wrapper.md` | `skills/tool_wrappers/fit_and_significance_wrapper.md` | Tool Wrapper | split |
| `SKILL_WORKSPACE_AND_FIT_PYHF` | `references/SKILL_WORKSPACE_AND_FIT_PYHF.md` | `systematics_and_workspace_generator.md` | `skills/generators/systematics_and_workspace_generator.md` | Generator | split |
| `SKILL_WORKSPACE_AND_FIT_PYHF` | `references/SKILL_WORKSPACE_AND_FIT_PYHF.md` | `statistical_readiness_reviewer.md` | `skills/reviewers/statistical_readiness_reviewer.md` | Reviewer | split |
| `SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE` | `references/SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE.md` | `systematics_and_workspace_generator.md` | `skills/generators/systematics_and_workspace_generator.md` | Generator | split |
| `SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE` | `references/SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE.md` | `blinding_and_fit_policy_inversion.md` | `skills/inversions/blinding_and_fit_policy_inversion.md` | Inversion | split |
| `SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE` | `references/SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE.md` | `statistical_readiness_reviewer.md` | `skills/reviewers/statistical_readiness_reviewer.md` | Reviewer | split and merged |
| `SKILL_ASIMOV_EXPECTED_SIGNIFICANCE_SPLUSB` | `references/SKILL_ASIMOV_EXPECTED_SIGNIFICANCE_SPLUSB.md` | `systematics_and_workspace_generator.md` | `skills/generators/systematics_and_workspace_generator.md` | Generator | merged and adapted |
| `SKILL_ASIMOV_EXPECTED_SIGNIFICANCE_SPLUSB` | `references/SKILL_ASIMOV_EXPECTED_SIGNIFICANCE_SPLUSB.md` | `blinding_and_fit_policy_inversion.md` | `skills/inversions/blinding_and_fit_policy_inversion.md` | Inversion | split |
| `SKILL_STATTOOL_OPTIONAL_PYHF_BACKEND` | `references/SKILL_STATTOOL_OPTIONAL_PYHF_BACKEND.md` | `fit_and_significance_wrapper.md` | `skills/tool_wrappers/fit_and_significance_wrapper.md` | Tool Wrapper | split |
| `SKILL_STATTOOL_OPTIONAL_PYHF_BACKEND` | `references/SKILL_STATTOOL_OPTIONAL_PYHF_BACKEND.md` | `blinding_and_fit_policy_inversion.md` | `skills/inversions/blinding_and_fit_policy_inversion.md` | Inversion | split |
| `SKILL_ROOTMLTOOL_CACHED_ANALYSIS` | `references/SKILL_ROOTMLTOOL_CACHED_ANALYSIS.md` | `runtime_and_preflight_wrapper.md` | `skills/tool_wrappers/runtime_and_preflight_wrapper.md` | Tool Wrapper | merged and adapted |

### Plotting, validation, and reporting

| Old skill or file | Old source path | New skill or file | New target path | Target pattern | Migration mode |
|---|---|---|---|---|---|
| `SKILL_PLOTTING_AND_REPORT` | `references/SKILL_PLOTTING_AND_REPORT.md` | `report_package_generator.md` | `skills/generators/report_package_generator.md` | Generator | split |
| `SKILL_PLOTTING_AND_REPORT` | `references/SKILL_PLOTTING_AND_REPORT.md` | `report_packaging_wrapper.md` | `skills/tool_wrappers/report_packaging_wrapper.md` | Tool Wrapper | split |
| `SKILL_PLOTTING_AND_REPORT` | `references/SKILL_PLOTTING_AND_REPORT.md` | `blinding_and_visualization_reviewer.md` | `skills/reviewers/blinding_and_visualization_reviewer.md` | Reviewer | split |
| `SKILL_PLOTTING_AND_REPORT` | `references/SKILL_PLOTTING_AND_REPORT.md` | `data_mc_discrepancy_reviewer.md` | `skills/reviewers/data_mc_discrepancy_reviewer.md` | Reviewer | split |
| `SKILL_HISTOGRAM_PLOTTING_INVARIANTS` | `references/SKILL_HISTOGRAM_PLOTTING_INVARIANTS.md` | `plotting_invariants.md` | `skills/shared/plotting_invariants.md` | Shared support | merged and adapted |
| `SKILL_HISTOGRAM_PLOTTING_INVARIANTS` | `references/SKILL_HISTOGRAM_PLOTTING_INVARIANTS.md` | `blinding_and_visualization_reviewer.md` | `skills/reviewers/blinding_and_visualization_reviewer.md` | Reviewer | split and merged |
| `SKILL_VISUAL_VERIFICATION` | `references/SKILL_VISUAL_VERIFICATION.md` | `blinding_and_visualization_reviewer.md` | `skills/reviewers/blinding_and_visualization_reviewer.md` | Reviewer | merged |
| `SKILL_DATA_MC_DISCREPANCY_SANITY_CHECK` | `references/SKILL_DATA_MC_DISCREPANCY_SANITY_CHECK.md` | `data_mc_discrepancy_reviewer.md` | `skills/reviewers/data_mc_discrepancy_reviewer.md` | Reviewer | adapted |
| `SKILL_DATA_MC_DISCREPANCY_SANITY_CHECK` | `references/SKILL_DATA_MC_DISCREPANCY_SANITY_CHECK.md` | `failure_to_skill_inversion.md` | `skills/inversions/failure_to_skill_inversion.md` | Inversion | split |
| `SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW` | `references/SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW.md` | `report_package_generator.md` | `skills/generators/report_package_generator.md` | Generator | split |
| `SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW` | `references/SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW.md` | `reporting_and_handoff_pipeline.md` | `skills/pipelines/reporting_and_handoff_pipeline.md` | Pipeline | split |
| `SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW` | `references/SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW.md` | `hep_analysis_meta_pipeline.md` | `skills/pipelines/hep_analysis_meta_pipeline.md` | Pipeline | split and merged |
| `SKILL_ENFORCEMENT_PRE_HANDOFF_GATE` | `references/SKILL_ENFORCEMENT_PRE_HANDOFF_GATE.md` | `reproducibility_and_handoff_reviewer.md` | `skills/reviewers/reproducibility_and_handoff_reviewer.md` | Reviewer | split and merged |
| `SKILL_ENFORCEMENT_PRE_HANDOFF_GATE` | `references/SKILL_ENFORCEMENT_PRE_HANDOFF_GATE.md` | `reporting_and_handoff_pipeline.md` | `skills/pipelines/reporting_and_handoff_pipeline.md` | Pipeline | split and merged |
| `SKILL_FINAL_REPORT_REVIEW_AND_HANDOFF` | `references/SKILL_FINAL_REPORT_REVIEW_AND_HANDOFF.md` | `reproducibility_and_handoff_reviewer.md` | `skills/reviewers/reproducibility_and_handoff_reviewer.md` | Reviewer | merged and adapted |
| `SKILL_FINAL_REPORT_REVIEW_AND_HANDOFF` | `references/SKILL_FINAL_REPORT_REVIEW_AND_HANDOFF.md` | `reporting_and_handoff_pipeline.md` | `skills/pipelines/reporting_and_handoff_pipeline.md` | Pipeline | split |
| `SKILL_SMOKE_TESTS_AND_REPRODUCIBILITY` | `references/SKILL_SMOKE_TESTS_AND_REPRODUCIBILITY.md` | `runtime_and_preflight_wrapper.md` | `skills/tool_wrappers/runtime_and_preflight_wrapper.md` | Tool Wrapper | split and merged |
| `SKILL_SMOKE_TESTS_AND_REPRODUCIBILITY` | `references/SKILL_SMOKE_TESTS_AND_REPRODUCIBILITY.md` | `reproducibility_and_handoff_reviewer.md` | `skills/reviewers/reproducibility_and_handoff_reviewer.md` | Reviewer | split and merged |

## Support-file mapping

| Old file | Old source path | New file | New target path | Target pattern | Migration mode |
|---|---|---|---|---|---|
| `00_INDEX.md` | `references/00_INDEX.md` | `hep_analysis_meta_pipeline.md` | `skills/pipelines/hep_analysis_meta_pipeline.md` | Pipeline | merged and adapted |
| `00_INDEX.md` | `references/00_INDEX.md` | `artifact_matrix.md` | `skills/shared/artifact_matrix.md` | Shared support | merged and adapted |
| `ROUTING_GUIDE.md` | `references/ROUTING_GUIDE.md` | `analysis_router_inversion.md` | `skills/inversions/analysis_router_inversion.md` | Inversion | adapted |
| `manifest.yaml` | `references/manifest.yaml` | `artifact_matrix.md` | `skills/shared/artifact_matrix.md` | Shared support | adapted |
| `MIGRATION_NOTES.md` | `references/MIGRATION_NOTES.md` | `skill_migration_map.md` | `docs/skill_migration_map.md` | Documentation | rewritten |
| `skills_refactor_audit.md` | `references/skills_refactor_audit.md` | `skill_audit.md` | `docs/skill_audit.md` | Documentation | rewritten |
| `openai.yaml` | `agents/openai.yaml` | none | none | Deprecated | deprecated |

## Interpretation notes

- `copied` was intentionally rare because a straight 1:1 copy would preserve the old mixed-purpose structure.
- `split` means one old contract became multiple pattern-pure skills.
- `merged` means content from several old files now lives in one reusable shared or reviewer skill.
- `adapted` means the physics content was retained but rewritten into the new pattern contract.
- `rewritten` means a document was reauthored because the new repository needs documentation rather than another skill contract.
