---
name: hep-analysis-reviewers
description: Use when you need the refactored HEP reviewer skills in this repository for preflight fact checks, summary consistency, nominal-sample and normalization validation, blinding and visualization checks, statistical readiness, data-MC discrepancy review, or reproducibility and handoff gates. Prefer this over the legacy `hep-meta-first` review contracts when the task is to judge whether a stage is actually acceptable.
---

# HEP Analysis Reviewers

Use this skill when the task is to validate a stage, block unsafe progression, or certify handoff readiness.

## Quick Start

1. Read only the reviewer file that matches the current gate:
   - `../hep-analysis-meta-pipeline/references/refactored/skills/reviewers/preflight_fact_check_reviewer.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/reviewers/analysis_summary_reviewer.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/reviewers/nominal_sample_and_normalization_reviewer.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/reviewers/blinding_and_visualization_reviewer.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/reviewers/statistical_readiness_reviewer.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/reviewers/data_mc_discrepancy_reviewer.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/reviewers/reproducibility_and_handoff_reviewer.md`
2. Pair the reviewer with:
   - `../hep-analysis-meta-pipeline/references/refactored/skills/shared/review_rubric.md`
   - `../hep-analysis-meta-pipeline/references/refactored/skills/shared/evidence_requirements.md`
3. When a reviewer blocks, route to the smallest matching inversion or generator instead of rerunning everything.

## What This Skill Covers

- factual readiness before execution
- schema and partition consistency
- nominal sample and normalization validity
- blinding and plot correctness
- statistical-readiness gates
- discrepancy handling
- reproducibility and final handoff gates

## Stop Conditions

- reviewer evidence is missing
- the run would advance without a mandatory gate
- the only possible conclusion would rely on inference rather than artifacts
