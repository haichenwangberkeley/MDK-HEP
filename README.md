# Codex HEP Skills

This repository packages the HEP analysis skills from the `GCT-hep-meta` workspace without including the analysis codebase itself.

## What is included

- `skill_src/`: human-maintained source for refactored pattern files and runtime skill templates
- `scripts/build_runtime_skills.py`: rebuilds the runtime pack from `skill_src/`
- `.codex/skills/`: generated session-ready Codex skill folders
- `.codex/skills/INDEX.md`: quick navigation for the exported session pack
- `docs/`: audit, migration, and authoring documentation for the skill system
- `README_skills.md`: architecture overview for the refactored pattern system
- `docs/runtime_skill_build.md`: explains the source/build/runtime packaging model

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

## Source, build, and runtime

This repository now uses a three-layer model:

- Humans edit `skill_src/`.
- `scripts/build_runtime_skills.py` packages the runtime skill folders.
- Agents use the generated `.codex/skills/` folders.

For the refactored runtime skills, each generated skill folder bundles its own local pattern references under `references/patterns/`, so the live skill no longer depends on a sibling `_hep-analysis-refactored` directory.

## Build

Rebuild the runtime pack with:

```bash
python scripts/build_runtime_skills.py
```

The build step refreshes `.codex/skills/`, regenerates `.codex/skills/INDEX.md`, removes the old shared `_hep-analysis-refactored` runtime folder, and validates the generated references.

## Intended workflow

1. Edit `skill_src/patterns/` when changing shared refactored pattern content.
2. Edit `skill_src/runtime_templates/` when changing runtime `SKILL.md`, `agents/openai.yaml`, or preserved legacy runtime folders.
3. Run `python scripts/build_runtime_skills.py`.
4. Trigger `$hep-analysis-meta-pipeline` or one of the pattern-specific sibling skills from the generated `.codex/skills/` pack.
5. Keep the historical audit and migration docs under `docs/`.
6. Version and publish this directory without the analysis code or outputs.

## Local git notes

This export directory is prepared as its own git repository.
You can later connect it to GitHub with:

```bash
git remote add origin <your-github-repo-url>
git push -u origin main
```
