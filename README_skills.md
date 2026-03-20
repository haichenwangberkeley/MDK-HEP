# Pattern-Based Skills for GCT-hep-meta

This repository now keeps HEP analysis skills as a pattern-based system instead of a single router plus mixed-purpose reference contracts. The old source pack remains read-only. The new system lives entirely under `skills/` and `docs/`.

## Architecture

The pattern folders are:

- `skills/tool_wrappers/`: safe entrypoints for repository commands and workflow components
- `skills/generators/`: artifact creation and transformation contracts
- `skills/reviewers/`: independent quality, physics, and compliance gates
- `skills/inversions/`: branching, diagnosis, and work-backward decision logic
- `skills/pipelines/`: orchestration layers that sequence the smaller skills
- `skills/shared/`: reusable templates, guardrails, evidence contracts, and rubrics

## How an agent should use the skills

1. Start with `skills/pipelines/hep_analysis_meta_pipeline.md` for an end-to-end run.
2. Use `skills/inversions/analysis_router_inversion.md` when the entry point is a blocker, missing artifact, or failed review rather than a full fresh run.
3. Use a Generator to create the next artifact.
4. Use the paired Reviewer before claiming the stage is complete.
5. Use Tool Wrappers only to call the repo code paths that the Generator or Pipeline selected.
6. Reuse `skills/shared/` instead of copying common evidence rules, guardrails, or templates into new skills.

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
2. Reuse the templates and rules in `skills/shared/`.
3. Declare explicit inputs, outputs, evidence, failure modes, and escalation.
4. Link the skill from `skills/INDEX.md`.
5. Update `docs/skill_migration_map.md` if the skill replaces or absorbs an old source contract.

## Naming conventions

- Use lowercase snake case filenames.
- Let the folder convey the pattern; do not repeat the pattern in the filename unless clarity needs it.
- Prefer domain-first names such as `sample_semantics_generator.md` over generic names such as `generator_1.md`.
- Keep one dominant responsibility per file.
