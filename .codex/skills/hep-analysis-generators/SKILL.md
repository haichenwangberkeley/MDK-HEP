---
name: hep-analysis-generators
description: Use when you need the refactored HEP generator skills from this installed skill pack to create or transform analysis artifacts for the current ATLAS Open Data H-to-gammagamma project, including sample contracts and data-driven template contracts.
---

# HEP Analysis Generators

Use this skill when the task is to create a concrete analysis artifact in the refactored system.

## Quick Start

1. Read only the bundled generator reference that matches the artifact you need:
   - `../_hep-analysis-refactored/skills/generators/analysis_spec_generator.md`
   - `../_hep-analysis-refactored/skills/generators/sample_semantics_generator.md`
   - `../_hep-analysis-refactored/skills/generators/data_driven_template_generator.md`
   - `../_hep-analysis-refactored/skills/generators/event_model_and_partition_generator.md`
   - `../_hep-analysis-refactored/skills/generators/selection_and_yield_generator.md`
   - `../_hep-analysis-refactored/skills/generators/histogram_and_template_generator.md`
   - `../_hep-analysis-refactored/skills/generators/background_and_signal_model_generator.md`
   - `../_hep-analysis-refactored/skills/generators/systematics_and_workspace_generator.md`
   - `../_hep-analysis-refactored/skills/generators/report_package_generator.md`
2. Also read `../_hep-analysis-refactored/skills/shared/evidence_requirements.md`.
3. If the generator depends on a branch decision, load the relevant inversion file before execution.
4. If the generator must call code in the current analysis project, pair it with the matching tool-wrapper skill or bundled wrapper reference.

## What This Skill Covers

- spec generation
- sample, normalization, and likelihood-contract generation
- data-driven template generation
- region, cut-flow, and template generation
- model, fit, significance, and report artifact generation

## Stop Conditions

- required inputs are missing
- the generator would guess missing physics values
- a mandatory reviewer gate has not yet passed
