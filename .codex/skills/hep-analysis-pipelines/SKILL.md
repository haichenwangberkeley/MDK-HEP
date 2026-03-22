---
name: hep-analysis-pipelines
description: Use when you want the refactored HEP pipeline skills from this installed skill pack for the current ATLAS Open Data H-to-gammagamma project, including the dedicated sample-and-template semantics pipeline.
---

# HEP Analysis Pipelines

Use this skill as the main entrypoint for the refactored pipeline architecture in the current analysis project.

## Quick Start

1. Read `../_hep-analysis-refactored/skills/pipelines/hep_analysis_meta_pipeline.md` first for the full stage map.
2. If the task is mainly about sample contracts, data-driven templates, or likelihood sample roles, read `../_hep-analysis-refactored/skills/pipelines/sample_and_template_semantics_pipeline.md`.
3. If the task is only about spec intake or execution-contract setup, read `../_hep-analysis-refactored/skills/pipelines/spec_to_runtime_pipeline.md`.
4. If the task is only about plotting, report assembly, or handoff, read `../_hep-analysis-refactored/skills/pipelines/reporting_and_handoff_pipeline.md`.
5. Always pair the chosen pipeline file with:
   - `../_hep-analysis-refactored/skills/shared/hep_domain_guardrails.md`
   - `../_hep-analysis-refactored/skills/shared/pipeline_logging_contract.md`
   - `../_hep-analysis-refactored/skills/shared/artifact_matrix.md`
6. Load only the specific vendored pattern files needed for the current blocker. Do not fall back to the legacy `.codex/skills/hep-meta-first/references/` contracts.

## What This Skill Covers

- runtime and environment stage ordering
- sample preparation, likelihood-role, and data-template sequencing
- modeling and statistical stage gates
- validation, reporting, and handoff sequencing

## Stop Conditions

- the requested task would require inventing missing physics content
- a reviewer gate is required but its evidence is missing
- a central-result policy would be violated by continuing
