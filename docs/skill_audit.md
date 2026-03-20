# Skill Audit

Source root audited: `/Users/haichenwang/Work/analysis-automation/.codex/skills/hep-meta-first`

## Source design philosophy

The source pack is a router-centric HEP skill system. One top-level entry skill delegates into a large `references/` library of contract-like markdown files with explicit inputs, outputs, checks, and handoff hints. The pack preserves strong scientific content, but most contracts mix several responsibilities at once:

- stage routing
- artifact generation
- policy defaults
- review gates
- handoff logic

That mixing makes the pack scientifically rich but operationally hard to compose. The redesign in `GCT-hep-meta` keeps the physics rules, output contracts, and reviewer gates, while separating them into Tool Wrappers, Generators, Reviewers, Inversions, and Pipelines.

## Main findings

- The strongest preserved asset is the HEP-specific policy content, especially blinding, normalization, smoothing, effective-luminosity, and RooFit-primary rules.
- The biggest structural problem is mixed-purpose contracts that both create artifacts and certify them.
- Router logic exists in several places (`SKILL.md`, `00_INDEX.md`, `ROUTING_GUIDE.md`, `manifest.yaml`) and needed consolidation into a single Inversion plus a single central Pipeline.
- Statistical policy is especially mixed: backend choice, Asimov construction, smoothing, and significance semantics were spread across generators, gates, and reporting contracts.
- The source pack contains an internal policy inconsistency: `SKILL_ENFORCEMENT_POLICY_DEFAULTS.md` uses `36.0 fb^-1`, while the broader HEP workflow repeatedly uses `36.1 fb^-1` for central normalization. The new structure treats `36.1 fb^-1` as the repository default and records the inconsistency as a legacy issue.

## Skill inventory

Paths below are relative to the audited source root.

### Meta entry, specification, and governance

| Skill | Current source path | Inferred purpose | Current problems | Target pattern | Recommended action |
|---|---|---|---|---|---|
| `hep-meta-first` | `SKILL.md` | Single-entry router over the entire HEP pack. | Mixed purpose: routing, context-loading, and execution-spine advice are bundled together. | Inversion | Split into `analysis_router_inversion.md` plus `hep_analysis_meta_pipeline.md`. |
| `SKILL_SKILLS_PACK_INDEX` | `references/SKILL_SKILLS_PACK_INDEX.md` | Pack-level repository and workflow index. | Mixed purpose: index, workflow definition, and artifact expectations live together. | Pipeline | Merge into `README_skills.md`, `skills/INDEX.md`, and the central pipeline. |
| `SKILL_BOOTSTRAP_REPO` | `references/SKILL_BOOTSTRAP_REPO.md` | Bootstrap repository runtime and stage entrypoints. | Mixed purpose: bootstrap, runtime recovery, compliance rewriting, and validation checks are bundled. | Tool Wrapper | Split into `runtime_and_preflight_wrapper.md` and `reproducibility_and_handoff_reviewer.md`. |
| `SKILL_AGENT_PRE_FLIGHT_FACT_CHECK` | `references/SKILL_AGENT_PRE_FLIGHT_FACT_CHECK.md` | Check that execution-critical facts are explicit before the run starts. | Mostly reviewer-shaped already, but still embedded in a contract format that also implies execution flow. | Reviewer | Retain as a dedicated reviewer in `preflight_fact_check_reviewer.md`. |
| `SKILL_NARRATIVE_TO_ANALYSIS_JSON_TRANSLATOR` | `references/SKILL_NARRATIVE_TO_ANALYSIS_JSON_TRANSLATOR.md` | Translate a narrative analysis request into analysis JSON plus a gap report. | Mixed with downstream validation and workflow handoff. | Generator | Keep the generation core in `analysis_spec_generator.md`; move orchestration to `spec_to_runtime_pipeline.md`. |
| `SKILL_JSON_SPEC_DRIVEN_EXECUTION` | `references/SKILL_JSON_SPEC_DRIVEN_EXECUTION.md` | Treat analysis JSON as the execution source of truth and record runtime deviations. | Mixed purpose: spec translation, override policy, and execution orchestration. | Pipeline | Rebuild as `spec_to_runtime_pipeline.md` with generator and reviewer hooks. |
| `SKILL_READ_SUMMARY_AND_VALIDATE` | `references/SKILL_READ_SUMMARY_AND_VALIDATE.md` | Normalize and validate the summary schema and cross references. | Mixed purpose: calls a loader, validates output, and provides workflow routing. | Reviewer | Split into `summary_loader_wrapper.md` and `analysis_summary_reviewer.md`. |
| `SKILL_FULL_STATISTICS_EXECUTION_POLICY` | `references/SKILL_FULL_STATISTICS_EXECUTION_POLICY.md` | Require full-statistics execution for final claims. | Policy gate is correct but buried among broader execution semantics. | Reviewer | Merge into `reproducibility_and_handoff_reviewer.md` as a hard gate. |
| `SKILL_ENFORCEMENT_POLICY_DEFAULTS` | `references/SKILL_ENFORCEMENT_POLICY_DEFAULTS.md` | Resolve default policy constants such as luminosity and thresholds. | Decision logic mixed with stale numeric default (`36.0`) and gate setup. | Inversion | Move override resolution into `blinding_and_fit_policy_inversion.md`; preserve constants in shared guardrails. |
| `SKILL_SKILL_REFRESH_AND_CHECKPOINTING` | `references/SKILL_SKILL_REFRESH_AND_CHECKPOINTING.md` | Re-check policy compliance at stage boundaries. | Mixed purpose: scheduling, logging, and gate semantics are all inline. | Pipeline | Split into `pipeline_logging_contract.md`, `hep_analysis_meta_pipeline.md`, and `reproducibility_and_handoff_reviewer.md`. |
| `SKILL_EXTRACT_NEW_SKILL_FROM_FAILURE` | `references/SKILL_EXTRACT_NEW_SKILL_FROM_FAILURE.md` | Turn recurring failure modes into candidate new skills. | Good inversion idea, but currently placed as a governance contract rather than a diagnosis pattern. | Inversion | Recast as `failure_to_skill_inversion.md`. |

### Samples, normalization, and event model

| Skill | Current source path | Inferred purpose | Current problems | Target pattern | Recommended action |
|---|---|---|---|---|---|
| `SKILL_13TEV25_DETAILS` | `references/SKILL_13TEV25_DETAILS.md` | Provide dataset-specific facts used in open-data workflows. | Fact source is too opaque and weakly connected to downstream sample decisions. | Inversion | Fold dataset decision logic into `sample_strategy_inversion.md` and preserve facts in `open_data_dataset_facts.md`. |
| `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION` | `references/SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION.md` | Build the sample registry, process roles, and normalization convention. | Strong scientific content but mixed generation, decision logic, and validation. | Generator | Split into `sample_semantics_generator.md`, `sample_registry_and_metadata_wrapper.md`, and `nominal_sample_and_normalization_reviewer.md`. |
| `SKILL_MC_SAMPLE_DISAMBIGUATION_AND_NOMINAL_SELECTION` | `references/SKILL_MC_SAMPLE_DISAMBIGUATION_AND_NOMINAL_SELECTION.md` | Pick a unique nominal MC set when multiple candidates exist. | Core value is branch selection, but it is embedded in a contract that also owns acceptance checks. | Inversion | Move into `sample_strategy_inversion.md`; keep reviewer confirmation separate. |
| `SKILL_MC_NORMALIZATION_METADATA_STACKING` | `references/SKILL_MC_NORMALIZATION_METADATA_STACKING.md` | Use metadata-driven normalization for open-data MC stacks. | Mixed purpose: metadata matching, weight construction, stacking, and review all in one file. | Generator | Split across `sample_semantics_generator.md`, `sample_registry_and_metadata_wrapper.md`, and `nominal_sample_and_normalization_reviewer.md`. |
| `SKILL_EVENT_IO_AND_COLUMNAR_MODEL` | `references/SKILL_EVENT_IO_AND_COLUMNAR_MODEL.md` | Define how event data are ingested and represented for analysis. | Operational wrapper logic and object-prep semantics are coupled. | Tool Wrapper | Keep the invocation layer in `selection_and_partition_wrapper.md`; move derived-contract creation elsewhere. |
| `SKILL_OBJECT_DEFINITIONS` | `references/SKILL_OBJECT_DEFINITIONS.md` | Define reconstructed objects before higher-level selections. | Conceptually a generator, but previously hidden among physics-fact style contracts. | Generator | Merge into `event_model_and_partition_generator.md`. |
| `SKILL_CATEGORY_CHANNEL_REGION_PARTITIONING` | `references/SKILL_CATEGORY_CHANNEL_REGION_PARTITIONING.md` | Define categories, channels, and region partitions. | Mostly generator-shaped, but still carries handoff logic and acceptance checks. | Generator | Merge into `event_model_and_partition_generator.md`. |
| `SKILL_SELECTION_ENGINE_AND_REGIONS` | `references/SKILL_SELECTION_ENGINE_AND_REGIONS.md` | Run executable region logic and overlap checks. | Mixed purpose: tool mediation and review-style overlap checks live together. | Tool Wrapper | Split into `selection_and_partition_wrapper.md` and downstream generators or reviewers. |
| `SKILL_CUT_FLOW_AND_YIELDS` | `references/SKILL_CUT_FLOW_AND_YIELDS.md` | Produce cut flows and yield tables for selected samples. | Mostly generator-shaped, but central-sample policy checks are embedded inline. | Generator | Keep artifact creation in `selection_and_yield_generator.md`; leave nominal validation to the reviewer. |

### Templates, modeling, and statistics

| Skill | Current source path | Inferred purpose | Current problems | Target pattern | Recommended action |
|---|---|---|---|---|---|
| `SKILL_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS` | `references/SKILL_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS.md` | Decide signal and background roles plus CR-to-SR constraint semantics. | Core value is branching logic, but artifact generation and checks are bundled into the same file. | Inversion | Split into `sample_strategy_inversion.md` and `background_and_signal_model_generator.md`. |
| `SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION` | `references/SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION.md` | Encode blinding behavior and CR/SR visualization rules. | Three concerns are mixed: blinding decisions, plot generation intent, and review criteria. | Inversion | Split into `blinding_and_fit_policy_inversion.md`, `blinding_and_visualization_reviewer.md`, and report-generation guidance. |
| `SKILL_HISTOGRAMMING_AND_TEMPLATES` | `references/SKILL_HISTOGRAMMING_AND_TEMPLATES.md` | Build histograms and fit templates. | Mixed generation, wrapper hints, and downstream reviewer expectations. | Generator | Split into `histogram_and_template_generator.md` plus `histogram_and_template_wrapper.md`. |
| `SKILL_FREEZE_ANALYSIS_HISTOGRAM_PRODUCTS` | `references/SKILL_FREEZE_ANALYSIS_HISTOGRAM_PRODUCTS.md` | Freeze expensive histogram products for reuse. | Operational wrapper logic sits in a standalone file without shared cache conventions. | Tool Wrapper | Merge into `histogram_and_template_wrapper.md`. |
| `SKILL_BACKGROUND_TEMPLATE_SMOOTHING_POLICY` | `references/SKILL_BACKGROUND_TEMPLATE_SMOOTHING_POLICY.md` | Enforce explicit smoothing policy. | Already reviewer-like, but isolated from the broader statistical readiness gate. | Reviewer | Merge into `statistical_readiness_reviewer.md`. |
| `SKILL_MC_EFFECTIVE_LUMI_COVERAGE_GATE` | `references/SKILL_MC_EFFECTIVE_LUMI_COVERAGE_GATE.md` | Enforce effective-MC-luminosity coverage before fitting or handoff. | Already a gate, but duplicated policy resolution lives elsewhere. | Reviewer | Merge into `statistical_readiness_reviewer.md`. |
| `SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION` | `references/SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION.md` | Build signal and background parameterizations with spurious-signal control. | Mixed with template choice decisions, smoothing context, and backend provenance. | Generator | Split between `background_and_signal_model_generator.md`, `blinding_and_fit_policy_inversion.md`, and the statistical reviewer. |
| `SKILL_SYSTEMATICS_AND_NUISANCES` | `references/SKILL_SYSTEMATICS_AND_NUISANCES.md` | Build nuisance-parameter representations for the analysis. | Mostly generator-shaped, but currently bound too tightly to source contract routing. | Generator | Recast as `systematics_and_workspace_generator.md`. |
| `SKILL_WORKSPACE_AND_FIT_PYHF` | `references/SKILL_WORKSPACE_AND_FIT_PYHF.md` | Build workspaces and fit results, with RooFit primary for H to gammagamma. | Mixed tool mediation, generation, reviewer criteria, and backend policy. | Tool Wrapper | Split into `fit_and_significance_wrapper.md`, `systematics_and_workspace_generator.md`, and `statistical_readiness_reviewer.md`. |
| `SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE` | `references/SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE.md` | Generate profile-likelihood significance outputs under strict HEP rules. | Strong generator content, but backend and blinding policy are mixed into the same file. | Generator | Split into `systematics_and_workspace_generator.md`, `blinding_and_fit_policy_inversion.md`, and `statistical_readiness_reviewer.md`. |
| `SKILL_ASIMOV_EXPECTED_SIGNIFICANCE_SPLUSB` | `references/SKILL_ASIMOV_EXPECTED_SIGNIFICANCE_SPLUSB.md` | Generate expected discovery sensitivity using S+B Asimov pseudo-data. | Valuable generator, but too entangled with policy and reporting semantics. | Generator | Merge into `systematics_and_workspace_generator.md` with policy extracted to the inversion and reviewer layers. |
| `SKILL_STATTOOL_OPTIONAL_PYHF_BACKEND` | `references/SKILL_STATTOOL_OPTIONAL_PYHF_BACKEND.md` | Allow optional pyhf/stattool cross-check backend. | Optional backend policy is mixed with execution semantics. | Tool Wrapper | Split into `fit_and_significance_wrapper.md` and `blinding_and_fit_policy_inversion.md`. |
| `SKILL_ROOTMLTOOL_CACHED_ANALYSIS` | `references/SKILL_ROOTMLTOOL_CACHED_ANALYSIS.md` | Manage optional cached event backend and parity checks. | Backend choice logic is correct, but it belongs with runtime mediation rather than a physics contract library. | Tool Wrapper | Merge into `runtime_and_preflight_wrapper.md`. |

### Plotting, validation, and reporting

| Skill | Current source path | Inferred purpose | Current problems | Target pattern | Recommended action |
|---|---|---|---|---|---|
| `SKILL_PLOTTING_AND_REPORT` | `references/SKILL_PLOTTING_AND_REPORT.md` | Build plots and report-ready narrative artifacts. | Mixed generation, report assembly, discrepancy handling, and review checks. | Generator | Split into `report_package_generator.md`, `report_packaging_wrapper.md`, `blinding_and_visualization_reviewer.md`, and `data_mc_discrepancy_reviewer.md`. |
| `SKILL_HISTOGRAM_PLOTTING_INVARIANTS` | `references/SKILL_HISTOGRAM_PLOTTING_INVARIANTS.md` | Define mandatory plotting rules and statistical display invariants. | Invariant set should be shared, not a standalone skill that pretends to be executable. | Reviewer | Move the rules into `skills/shared/plotting_invariants.md` and consume them from reviewers and generators. |
| `SKILL_VISUAL_VERIFICATION` | `references/SKILL_VISUAL_VERIFICATION.md` | Require visual validation of objects, selections, categories, and final fits. | Already reviewer-shaped, but duplicated plotting-rule content exists elsewhere. | Reviewer | Merge into `blinding_and_visualization_reviewer.md`. |
| `SKILL_DATA_MC_DISCREPANCY_SANITY_CHECK` | `references/SKILL_DATA_MC_DISCREPANCY_SANITY_CHECK.md` | Audit data-MC disagreement and force explicit handling. | Good reviewer content, but remediation logic is mixed into the same file. | Reviewer | Keep the review function in `data_mc_discrepancy_reviewer.md`; route remediation through `failure_to_skill_inversion.md`. |
| `SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW` | `references/SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW.md` | Orchestrate final report content and physics communication. | Strong stage orchestration mixed with content generation and reviewer logic. | Pipeline | Split into `report_package_generator.md`, `reporting_and_handoff_pipeline.md`, and the central meta pipeline. |
| `SKILL_ENFORCEMENT_PRE_HANDOFF_GATE` | `references/SKILL_ENFORCEMENT_PRE_HANDOFF_GATE.md` | Enforce the final non-bypassable handoff gate. | Pure reviewer semantics, but isolated from the broader handoff review process. | Reviewer | Merge into `reproducibility_and_handoff_reviewer.md` and `reporting_and_handoff_pipeline.md`. |
| `SKILL_FINAL_REPORT_REVIEW_AND_HANDOFF` | `references/SKILL_FINAL_REPORT_REVIEW_AND_HANDOFF.md` | Final structured review after report generation. | Reviewer logic is right, but the handoff pipeline was implicit rather than explicit. | Reviewer | Merge into `reproducibility_and_handoff_reviewer.md` and `reporting_and_handoff_pipeline.md`. |
| `SKILL_SMOKE_TESTS_AND_REPRODUCIBILITY` | `references/SKILL_SMOKE_TESTS_AND_REPRODUCIBILITY.md` | Require smoke-test and reproducibility evidence across runs. | Mixed with checkpoint scheduling and broader governance logic. | Reviewer | Split into `runtime_and_preflight_wrapper.md` and `reproducibility_and_handoff_reviewer.md`. |

## Source support artifacts

These files are not standalone skills, but they materially shaped the redesign.

| Source path | Purpose in source pack | Recommended disposition |
|---|---|---|
| `references/00_INDEX.md` | Dependency-ordered execution spine and stage grouping. | Fold into `skills/pipelines/hep_analysis_meta_pipeline.md` and `skills/shared/artifact_matrix.md`. |
| `references/ROUTING_GUIDE.md` | Fast-path routing rules and ambiguity guidance. | Fold into `skills/inversions/analysis_router_inversion.md`. |
| `references/manifest.yaml` | Machine-readable producer and dependency index. | Adapt into `skills/shared/artifact_matrix.md`. |
| `references/MIGRATION_NOTES.md` | Prior 1:1 conversion notes. | Preserve historically; superseded by `docs/skill_migration_map.md`. |
| `references/skills_refactor_audit.md` | Prior audit of the old conversion pass. | Preserve historically; superseded by this audit. |
| `agents/openai.yaml` | UI metadata for the old single-entry skill. | Do not migrate as-is; the new system is intentionally more harness-agnostic. |

## Split, merge, and deprecate summary

- Split-heavy contracts: `SKILL_BOOTSTRAP_REPO`, `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION`, `SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION`, `SKILL_WORKSPACE_AND_FIT_PYHF`, `SKILL_PLOTTING_AND_REPORT`, and `SKILL_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW`.
- Merge targets: plotting invariants, dataset-specific facts, handoff gates, and checkpoint rules moved into shared or reviewer layers.
- Deprecated as standalone execution concepts: the old pack index, the old routing guide, and UI-only metadata. Their content survives, but not as top-level skills.
