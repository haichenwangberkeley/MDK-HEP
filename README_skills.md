# Pattern-Based HEP Skills

This repository packages the refactored HEP analysis skill system as self-contained session skills. The old source pack remains read-only. The operational skill pack lives under `.codex/skills/`, and the refactored pattern files are vendored under `.codex/skills/hep-analysis-meta-pipeline/references/refactored/skills/`.

## Path convention

Unless otherwise noted, path examples like `skills/pipelines/hep_analysis_meta_pipeline.md` are relative to:

```text
.codex/skills/hep-analysis-meta-pipeline/references/refactored/
```

## Architecture

The pattern folders are:

- `skills/tool_wrappers/`: safe entrypoints for repository commands and workflow components
- `skills/generators/`: artifact creation and transformation contracts
- `skills/reviewers/`: independent quality, physics, and compliance gates
- `skills/inversions/`: branching, diagnosis, and work-backward decision logic
- `skills/pipelines/`: orchestration layers that sequence the smaller skills
- `skills/shared/`: reusable templates, guardrails, evidence contracts, and rubrics

## How an agent should use the skills

1. Start with `$hep-analysis-meta-pipeline` for an end-to-end run.
2. Use `skills/pipelines/hep_analysis_meta_pipeline.md` when you need the underlying vendored pipeline contract.
3. Use `skills/inversions/analysis_router_inversion.md` when the entry point is a blocker, missing artifact, or failed review rather than a full fresh run.
4. Use a Generator to create the next artifact.
5. Use the paired Reviewer before claiming the stage is complete.
6. Use Tool Wrappers only to call the repo code paths that the Generator or Pipeline selected.
7. Reuse `skills/shared/` instead of copying common evidence rules, guardrails, or templates into new skills.

## Central HEP pipeline

The central pipeline covers:

- runtime and environment setup
- sample identification and preparation
- feature and variable preparation
- event selection and cut flow
- categorization
- background modeling or estimation
- signal and background fitting or statistical setup
- validation and cross-checks
- result packaging
- report and log generation

Each stage names:

- entry criteria
- producing skills
- required reviewer gates
- required logging artifacts
- escalation conditions

## Shared components

The shared layer provides:

- a common frontmatter template
- required section checklists
- evidence rules
- a reviewer rubric
- a decision-record template
- pipeline logging requirements
- HEP guardrails
- plotting invariants
- an artifact matrix

## Adding a new skill

1. Pick one dominant pattern using `docs/pattern_authoring_guide.md`.
2. Add or edit the refactored Markdown contract under `.codex/skills/hep-analysis-meta-pipeline/references/refactored/skills/`.
3. Reuse the templates and rules in `skills/shared/`.
4. Declare explicit inputs, outputs, evidence, failure modes, and escalation.
5. Link the skill from `.codex/skills/INDEX.md`.
6. Update `docs/skill_migration_map.md` if the skill replaces or absorbs an old source contract.

## Naming conventions

- Use lowercase snake case filenames.
- Let the folder convey the pattern; do not repeat the pattern in the filename unless clarity needs it.
- Prefer domain-first names such as `sample_semantics_generator.md` over generic names such as `generator_1.md`.
- Keep one dominant responsibility per file.
