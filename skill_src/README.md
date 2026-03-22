# Skill Source Tree

`skill_src/` is the human-maintained master copy for the runtime skill pack.

- edit `patterns/` for refactored scientific logic and shared pattern files
- edit `runtime_templates/` for `SKILL.md`, agent metadata, and preserved runtime-only skill folders
- rebuild `.codex/skills/` with:

```bash
python scripts/build_runtime_skills.py
```

The generated runtime folders under `.codex/skills/` should not be treated as the primary authoring location.
