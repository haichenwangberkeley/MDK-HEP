# Codex HEP Skills

This repository packages the HEP analysis skills from the `GCT-hep-meta` workspace without including the analysis codebase itself.

## What is included

- `.codex/skills/`: session-ready Codex skill folders plus vendored refactored references
- `.codex/skills/INDEX.md`: quick navigation for the exported session pack
- `docs/`: audit, migration, and authoring documentation for the skill system
- `README_skills.md`: architecture overview for the refactored pattern system

## Main entrypoint

The canonical session-skill entrypoint is:

- `.codex/skills/hep-analysis-meta-pipeline`

Use:

```text
Use $hep-analysis-meta-pipeline for this task.
```

## Other entry skills

- `hep-analysis-pipelines`
- `hep-analysis-inversions`
- `hep-analysis-generators`
- `hep-analysis-reviewers`
- `hep-analysis-tool-wrappers`
- `hep-analysis-env-setup`

`hep-meta-first` is retained as a legacy skill pack for comparison and migration history.

## Where the refactored pattern files live

The session skills under `.codex/skills` are the triggerable Codex skill packages.
The refactored Tool Wrapper, Generator, Reviewer, Inversion, Pipeline, and shared reference files are vendored under:

```text
.codex/skills/hep-analysis-meta-pipeline/references/refactored/skills/
```

This keeps the exported repo self-contained. Other session skills point into that vendored tree by relative path, and the vendored copy also includes `metadata.csv`.

## Intended workflow

1. Trigger `$hep-analysis-meta-pipeline` or one of the pattern-specific sibling skills.
2. Maintain the vendored pattern files under `.codex/skills/hep-analysis-meta-pipeline/references/refactored/skills/`.
3. Keep the historical audit and migration docs under `docs/`.
4. Version and publish this directory without the analysis code or outputs.

## Local git notes

This export directory is prepared as its own git repository.
You can later connect it to GitHub with:

```bash
git remote add origin <your-github-repo-url>
git push -u origin main
```
