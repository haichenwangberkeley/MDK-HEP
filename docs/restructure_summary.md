# Restructure Summary

Export note: in this standalone skills repository, the refactored pattern tree is bundled under `.codex/skills/_hep-analysis-refactored/skills/`. Path examples written as `skills/...` refer to that bundled tree rather than to a required top-level repo directory.

## What changed

The source pack was converted from a single-router contract library into a pattern-based skill system under:

- `skills/tool_wrappers/`
- `skills/generators/`
- `skills/reviewers/`
- `skills/inversions/`
- `skills/pipelines/`
- `skills/shared/`

New repository-level docs were added for the audit, migration map, pattern authoring rules, and skill index.

## Why the new structure is better

- Each skill now has one dominant responsibility.
- Planning, generation, review, decision logic, and orchestration are explicit instead of blended together.
- Shared HEP rules such as blinding, normalization, plotting invariants, and evidence requirements now live in reusable shared files.
- The central pipeline is now a clear orchestration entry point with stage gates and logging requirements.
- Reviewers now act as independent gates rather than self-certification embedded inside generator contracts.

## Major splits and merges

- The old top-level router was split into `analysis_router_inversion.md` and `hep_analysis_meta_pipeline.md`.
- Sample, normalization, and nominal-selection logic were decomposed into a wrapper, a generator, a reviewer, and an inversion.
- Statistical policy was decomposed into `background_and_signal_model_generator.md`, `systematics_and_workspace_generator.md`, `fit_and_significance_wrapper.md`, `statistical_readiness_reviewer.md`, and `blinding_and_fit_policy_inversion.md`.
- Plotting, discrepancy handling, and final reporting were decomposed into a report generator, a report wrapper, dedicated reviewers, and a reporting pipeline.
- Shared invariants and templates were centralized in `skills/shared/`.

## Open issues

- Some repository stages still rely on integrated pipeline functions rather than stage-specific CLIs, so a few Tool Wrappers document controlled Python-entrypoint usage as well as shell commands.
- The old source pack still contains the `36.0 fb^-1` default in one policy file; the new system resolves this in favor of the repository-wide `36.1 fb^-1` central-result policy, but the source pack itself remains unchanged by design.
- The new pattern system is documented in Markdown rather than a stricter schema; future automation may want a machine-readable manifest for the new files.

## Recommended next iteration

- Add an automated linter that checks each new skill for required pattern sections.
- Add a machine-readable manifest for the new skills similar to the old `manifest.yaml`, but aligned with the new pattern taxonomy.
- Add lightweight tests that verify the central pipeline and router reference only existing skill paths.
- Consider adding repository scripts for stage-specific report regeneration and significance reruns so fewer wrappers need Python API fallbacks.
