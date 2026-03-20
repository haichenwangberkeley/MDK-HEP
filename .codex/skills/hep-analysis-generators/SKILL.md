---
name: hep-analysis-generators
description: Use when you need the refactored HEP generator skills in this repository for analysis-spec creation, sample semantics, event and partition contracts, cut flows, templates, modeling artifacts, statistical products, or report packaging. Prefer this over the legacy `hep-meta-first` contracts when the main job is to create or transform analysis artifacts.
---

# HEP Analysis Generators

Use this skill when the task is to create a concrete analysis artifact in the refactored system.

## Quick Start

1. Read only the repo-local generator file that matches the artifact you need:
   - `../hep-analysis-meta-pipeline/references/refactored/skills/generators/analysis_spec_generator.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/generators/sample_semantics_generator.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/generators/event_model_and_partition_generator.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/generators/selection_and_yield_generator.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/generators/histogram_and_template_generator.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/generators/background_and_signal_model_generator.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/generators/systematics_and_workspace_generator.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/generators/report_package_generator.md`
2. Also read `../hep-analysis-meta-pipeline/references/refactored/skills/shared/evidence_requirements.md`.
3. If the generator depends on a branch decision, load the relevant inversion file before execution.
4. If the generator calls repo code, pair it with the matching repo-local tool-wrapper file.

## What This Skill Covers

- spec generation
- sample and normalization generation
- region, cut-flow, and template generation
- model, fit, significance, and report artifact generation

## Stop Conditions

- required inputs are missing
- the generator would guess missing physics values
- a mandatory reviewer gate has not yet passed
