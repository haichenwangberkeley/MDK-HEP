# Codex HEP Skills

This repository packages the HEP analysis skills from the `GCT-hep-meta` workspace without including the analysis codebase itself.

## What is included

- `.codex/skills/`: session-ready Codex skill folders plus vendored refactored references
- `.codex/skills/INDEX.md`: quick navigation for the exported session pack
- `docs/`: audit, migration, and authoring documentation for the skill system
- `README_skills.md`: architecture overview for the refactored pattern system

The current pack includes an explicit data and MC sample-semantics subsystem that separates:

- signal-signature and likelihood intake,
- sample relevance and nominal-vs-alternative decisions,
- sample contract generation,
- data-driven template generation,
- likelihood-role review before modeling or fit setup.

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
The refactored Tool Wrapper, Generator, Reviewer, Inversion, Pipeline, and shared reference files are bundled under a shared non-skill directory:

```text
.codex/skills/_hep-analysis-refactored/skills/
```

This keeps the exported repo self-contained without making one skill depend on another skill's private `references/` directory. The shared reference pack also includes `metadata.csv`.

## Intended workflow

1. Trigger `$hep-analysis-meta-pipeline` or one of the pattern-specific sibling skills.
2. Use `.codex/skills/_hep-analysis-refactored/skills/pipelines/sample_and_template_semantics_pipeline.md` when the task hinges on data or MC sample roles, nominality, normalization, or data-driven templates.
3. Maintain the bundled pattern files under `.codex/skills/_hep-analysis-refactored/skills/`.
4. Keep the historical audit and migration docs under `docs/`.
5. Version and publish this directory without the analysis code or outputs.

## Local git notes

This export directory is prepared as its own git repository.
You can later connect it to GitHub with:

```bash
git remote add origin <your-github-repo-url>
git push -u origin main
```
