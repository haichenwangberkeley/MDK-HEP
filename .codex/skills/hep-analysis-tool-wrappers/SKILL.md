---
name: hep-analysis-tool-wrappers
description: Use when you need the refactored HEP tool-wrapper skills in this repository to call repo entrypoints safely: runtime and preflight, summary loading, sample registry and metadata, selection and partition execution, histogram and template production, fit and significance execution, or report packaging. Prefer this over the legacy `hep-meta-first` contracts when the task is mainly to drive existing code paths correctly.
---

# HEP Analysis Tool Wrappers

Use this skill when the hard part is invoking the right repository code path with the right preconditions.

## Quick Start

1. Read only the wrapper file that matches the code path you need:
   - `skills/tool_wrappers/runtime_and_preflight_wrapper.md`
   - `skills/tool_wrappers/summary_loader_wrapper.md`
   - `skills/tool_wrappers/sample_registry_and_metadata_wrapper.md`
   - `skills/tool_wrappers/selection_and_partition_wrapper.md`
   - `skills/tool_wrappers/histogram_and_template_wrapper.md`
   - `skills/tool_wrappers/fit_and_significance_wrapper.md`
   - `skills/tool_wrappers/report_packaging_wrapper.md`
2. If this is the first command in the repo or the shell is not normalized, pair this skill with the existing session skill `hep-analysis-env-setup`.
3. Always read the paired repo-local reviewer before treating a wrapper result as complete.

## What This Skill Covers

- invoking repository CLIs and integrated pipeline entrypoints
- preserving provenance around code-path selection
- separating command execution from policy decisions

## Stop Conditions

- the wrapper would run without its required reviewer evidence
- the selected backend is not eligible for the intended claim
- the repo runtime is not ready for the requested command
