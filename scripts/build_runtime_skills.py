#!/usr/bin/env python3
"""Build self-contained runtime skills from the human-maintained source tree."""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SkillPackage:
    name: str
    short_description: str
    mode: str


REFACTORED_PACKAGES = (
    SkillPackage(
        name="hep-analysis-meta-pipeline",
        short_description="main HEP orchestration entrypoint",
        mode="bundle_patterns",
    ),
    SkillPackage(
        name="hep-analysis-pipelines",
        short_description="pipeline-focused entry skill",
        mode="bundle_patterns",
    ),
    SkillPackage(
        name="hep-analysis-inversions",
        short_description="decision and routing entry skill",
        mode="bundle_patterns",
    ),
    SkillPackage(
        name="hep-analysis-generators",
        short_description="artifact-generation entry skill",
        mode="bundle_patterns",
    ),
    SkillPackage(
        name="hep-analysis-reviewers",
        short_description="validation and gate entry skill",
        mode="bundle_patterns",
    ),
    SkillPackage(
        name="hep-analysis-tool-wrappers",
        short_description="repository command and workflow wrapper entry skill",
        mode="bundle_patterns",
    ),
)

PASSTHROUGH_PACKAGES = (
    SkillPackage(
        name="hep-analysis-env-setup",
        short_description="runtime environment setup helper",
        mode="copy_template",
    ),
    SkillPackage(
        name="hep-meta-first",
        short_description="preserved legacy single-entry pack",
        mode="copy_template",
    ),
)

ALL_PACKAGES = REFACTORED_PACKAGES + PASSTHROUGH_PACKAGES


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def source_root() -> Path:
    return repo_root() / "skill_src"


def runtime_root() -> Path:
    return repo_root() / ".codex" / "skills"


def copy_tree(src: Path, dst: Path) -> None:
    shutil.copytree(src, dst)


def reset_managed_runtime_dirs() -> None:
    root = runtime_root()
    root.mkdir(parents=True, exist_ok=True)
    managed_names = {pkg.name for pkg in ALL_PACKAGES}
    managed_names.add("_hep-analysis-refactored")
    for name in managed_names:
        target = root / name
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()
    index_path = root / "INDEX.md"
    if index_path.exists():
        index_path.unlink()


def build_runtime_packages() -> None:
    src_root = source_root()
    root = runtime_root()
    pattern_src = src_root / "patterns"
    templates = src_root / "runtime_templates"

    for package in ALL_PACKAGES:
        template_dir = templates / package.name
        if not template_dir.exists():
            raise FileNotFoundError(f"Missing runtime template: {template_dir}")
        target = root / package.name
        copy_tree(template_dir, target)
        if package.mode == "bundle_patterns":
            bundled_patterns = target / "references" / "patterns"
            bundled_patterns.parent.mkdir(parents=True, exist_ok=True)
            copy_tree(pattern_src, bundled_patterns)


def write_runtime_index() -> None:
    lines = [
        "# Codex Skills Index",
        "",
        "This runtime pack is generated from `skill_src/` by `scripts/build_runtime_skills.py`.",
        "",
        "Canonical entry:",
        "",
        "- `$hep-analysis-meta-pipeline`",
        "",
        "Generated runtime skill packages:",
        "",
    ]
    for package in REFACTORED_PACKAGES + PASSTHROUGH_PACKAGES:
        lines.append(f"- `{package.name}`: {package.short_description}")
    lines.extend(
        [
            "",
            "Refactored runtime skills are self-contained.",
            "Each one bundles its local pattern references under:",
            "",
            "- `references/patterns/`",
            "",
            "The legacy `hep-meta-first` pack is preserved for comparison and migration history.",
            "",
        ]
    )
    (runtime_root() / "INDEX.md").write_text("\n".join(lines))


def validate_runtime_pack() -> None:
    root = runtime_root()
    required_files = [root / "INDEX.md"]
    for package in ALL_PACKAGES:
        required_files.append(root / package.name / "SKILL.md")
        required_files.append(root / package.name / "agents" / "openai.yaml")
        if package.mode == "bundle_patterns":
            required_files.append(root / package.name / "references" / "patterns" / "INDEX.md")
            required_files.append(root / package.name / "references" / "patterns" / "metadata.csv")
    missing = [path for path in required_files if not path.exists()]
    if missing:
        joined = "\n".join(str(path.relative_to(repo_root())) for path in missing)
        raise FileNotFoundError(f"Missing generated runtime files:\n{joined}")

    ref_pattern = re.compile(
        r"(?<![A-Za-z0-9_./-])((?:\./\.codex/skills/|\.\.?/|\.codex/skills/|references/|scripts/)"
        r"[A-Za-z0-9_./-]+\.(?:md|csv|sh|yaml))"
    )
    checked = 0
    problems: list[tuple[Path, str, Path]] = []
    files_to_check = list(root.rglob("*.md"))
    for path in files_to_check:
        text = path.read_text()
        for match in ref_pattern.finditer(text):
            ref = match.group(1)
            if ref.startswith("./.codex/skills/"):
                target = repo_root() / ref[2:]
            elif ref.startswith(".codex/skills/"):
                target = repo_root() / ref
            else:
                target = (path.parent / ref).resolve()
            checked += 1
            if not target.exists():
                problems.append((path.relative_to(repo_root()), ref, target))
    if problems:
        lines = ["Broken runtime references:"]
        for src, ref, target in problems:
            pretty_target = target.relative_to(repo_root()) if target.is_relative_to(repo_root()) else target
            lines.append(f"- {src}: {ref} -> {pretty_target}")
        raise RuntimeError("\n".join(lines))

    leaked = []
    for package in REFACTORED_PACKAGES:
        skill_file = root / package.name / "SKILL.md"
        text = skill_file.read_text()
        if "../_hep-analysis-refactored/" in text:
            leaked.append(skill_file.relative_to(repo_root()))
    if leaked:
        joined = "\n".join(str(path) for path in leaked)
        raise RuntimeError(f"Found obsolete shared-folder references in generated SKILLs:\n{joined}")

    print(f"Built {len(ALL_PACKAGES)} runtime skill packages.")
    print(f"Validated {checked} runtime references.")


def main() -> None:
    reset_managed_runtime_dirs()
    build_runtime_packages()
    write_runtime_index()
    validate_runtime_pack()


if __name__ == "__main__":
    main()
