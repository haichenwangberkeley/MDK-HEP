# Runtime Skill Build Model

This repository separates skill authoring from runtime packaging.

## Why this exists

The refactored HEP skills are easiest for humans to maintain as one coherent pattern tree, but the runtime skill folders under `.codex/skills/` are easier for agents to use when each skill is self-contained.

That leads to a three-part model:

1. `skill_src/`
   Human-maintained source.
2. `scripts/build_runtime_skills.py`
   Build step that assembles runtime skills.
3. `.codex/skills/`
   Generated runtime pack that agents actually load.

## Directory roles

### `skill_src/patterns/`

The master copy of the refactored Tool Wrapper, Generator, Reviewer, Inversion, Pipeline, and shared pattern files.

Examples:

- `skill_src/patterns/pipelines/hep_analysis_meta_pipeline.md`
- `skill_src/patterns/pipelines/sample_and_template_semantics_pipeline.md`
- `skill_src/patterns/shared/hep_domain_guardrails.md`
- `skill_src/patterns/shared/likelihood_sample_contract_schema.md`

### `skill_src/runtime_templates/`

The master copy of the runtime skill folders.

Examples:

- `skill_src/runtime_templates/hep-analysis-meta-pipeline/SKILL.md`
- `skill_src/runtime_templates/hep-analysis-generators/SKILL.md`
- `skill_src/runtime_templates/hep-analysis-env-setup/`
- `skill_src/runtime_templates/hep-meta-first/`

These templates define the triggerable session skills. For the refactored skills, the templates point to local files under `references/patterns/`, not to a sibling skill directory.

### `.codex/skills/`

The generated runtime pack.

Each refactored runtime skill is self-contained. For example:

```text
.codex/skills/hep-analysis-meta-pipeline/
  SKILL.md
  agents/openai.yaml
  references/patterns/pipelines/hep_analysis_meta_pipeline.md
  references/patterns/shared/hep_domain_guardrails.md
  ...
```

## Build command

Run this from the repository root:

```bash
python scripts/build_runtime_skills.py
```

## What the build script does

The build script:

1. Removes the previously generated refactored runtime skill folders under `.codex/skills/`.
2. Removes the old shared runtime folder `.codex/skills/_hep-analysis-refactored/` if it exists.
3. Copies the runtime templates from `skill_src/runtime_templates/`.
4. Bundles `skill_src/patterns/` into each refactored runtime skill under `references/patterns/`.
5. Regenerates `.codex/skills/INDEX.md`.
6. Verifies that the generated runtime references resolve.

## Editing workflow

Use this rule of thumb:

- edit `skill_src/patterns/` for refactored scientific logic, reviewer rubrics, pipelines, and shared contracts
- edit `skill_src/runtime_templates/` for `SKILL.md`, agent metadata, and preserved runtime-only folders
- do not hand-edit generated files under `.codex/skills/` unless you are debugging the build itself

After making changes:

1. run `python scripts/build_runtime_skills.py`
2. inspect `.codex/skills/`
3. commit both the source changes and the regenerated runtime pack

## Concrete mapping example

Human-maintained source:

```text
skill_src/patterns/pipelines/hep_analysis_meta_pipeline.md
```

Generated runtime copies:

```text
.codex/skills/hep-analysis-meta-pipeline/references/patterns/pipelines/hep_analysis_meta_pipeline.md
.codex/skills/hep-analysis-pipelines/references/patterns/pipelines/hep_analysis_meta_pipeline.md
.codex/skills/hep-analysis-generators/references/patterns/pipelines/hep_analysis_meta_pipeline.md
...
```

This duplication is intentional in the runtime pack. It keeps each generated skill self-contained while preserving a single human-maintained source of truth.

## Legacy note

`hep-meta-first` is preserved as a legacy runtime skill pack. It lives in `skill_src/runtime_templates/hep-meta-first/` and is copied through by the build script rather than rebuilt from the refactored pattern tree.
