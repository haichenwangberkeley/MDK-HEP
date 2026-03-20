# Codex HEP Skills

This repository packages the HEP analysis skills from the `GCT-hep-meta` workspace without including the analysis codebase itself.

## What is included

- `.codex/skills/`: session-ready Codex skill folders
- `skills/`: refactored pattern-based source material used by the session skills
- `docs/`: audit, migration, and authoring documentation for the skill system
- `README_skills.md`: architecture overview from the source workspace

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

## Why both `.codex/skills` and `skills/` exist

The session skills under `.codex/skills` are the triggerable Codex skill packages.
They rely on the refactored pattern files under `skills/` plus supporting docs under `docs/`.

This repository keeps both layers together so the packaged session skills remain understandable and maintainable when versioned separately from the analysis code.

## Intended workflow

1. Maintain the skill definitions here.
2. Connect this directory to a GitHub repository.
3. Push from this directory only, without the analysis code or outputs.

## Local git notes

This export directory is prepared as its own git repository.
You can later connect it to GitHub with:

```bash
git remote add origin <your-github-repo-url>
git push -u origin main
```
