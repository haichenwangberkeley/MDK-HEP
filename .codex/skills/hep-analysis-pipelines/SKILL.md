---
name: hep-analysis-pipelines
description: Use when you want the refactored session-ready HEP pipeline skills in this repository, especially the vendored orchestration entrypoints for ATLAS Open Data H-to-gammagamma work. Prefer this over the legacy `hep-meta-first` pack when the task is end-to-end workflow orchestration, spec-to-runtime staging, or reporting and handoff sequencing.
---

# HEP Analysis Pipelines

Use this skill as the main entrypoint for the refactored pipeline architecture in this workspace.

## Quick Start

1. Read `../hep-analysis-meta-pipeline/references/refactored/skills/pipelines/hep_analysis_meta_pipeline.md` first for the full stage map.
2. If the task is only about spec intake or execution-contract setup, read `../hep-analysis-meta-pipeline/references/refactored/skills/pipelines/spec_to_runtime_pipeline.md`.
3. If the task is only about plotting, report assembly, or handoff, read `../hep-analysis-meta-pipeline/references/refactored/skills/pipelines/reporting_and_handoff_pipeline.md`.
4. Always pair the chosen pipeline file with:
   - `../hep-analysis-meta-pipeline/references/refactored/skills/shared/hep_domain_guardrails.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/shared/pipeline_logging_contract.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/shared/artifact_matrix.md`
5. Load only the specific vendored pattern files needed for the current blocker. Do not fall back to the legacy `.codex/skills/hep-meta-first/references/` contracts.

## What This Skill Covers

- runtime and environment stage ordering
- sample preparation and selection sequencing
- modeling and statistical stage gates
- validation, reporting, and handoff sequencing

## Stop Conditions

- the requested task would require inventing missing physics content
- a reviewer gate is required but its evidence is missing
- a central-result policy would be violated by continuing
