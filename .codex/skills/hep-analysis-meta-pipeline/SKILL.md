---
name: hep-analysis-meta-pipeline
description: Use when you want the refactored main HEP orchestration skill in this repository. This skill is the session-ready entrypoint for the vendored refactored HEP pipeline, covering runtime setup, sample preparation, selections, modeling, statistical stages, validation, and report or handoff flow for ATLAS Open Data H-to-gammagamma work.
---

# HEP Analysis Meta Pipeline

Use this as the single session-skill entrypoint for the refactored HEP workflow in this workspace.

## Quick Start

1. Read `references/refactored/skills/pipelines/hep_analysis_meta_pipeline.md`.
2. Also read:
   - `references/refactored/skills/shared/hep_domain_guardrails.md`
   - `references/refactored/skills/shared/pipeline_logging_contract.md`
   - `references/refactored/skills/shared/artifact_matrix.md`
3. Load only the vendored pattern file needed for the current stage or blocker.
4. Prefer the vendored refactored files under `references/refactored/skills/` over the legacy `.codex/skills/hep-meta-first/references/` contracts.

## Use This Skill For

- full end-to-end workflow orchestration
- stage-by-stage handoff planning
- deciding which reviewer or generator must run next
- enforcing the refactored pipeline gates

## Stop Conditions

- a mandatory reviewer would be skipped
- a missing artifact would force guessed physics content
- a central-result policy would be violated by continuing
