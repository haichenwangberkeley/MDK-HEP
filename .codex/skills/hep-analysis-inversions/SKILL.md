---
name: hep-analysis-inversions
description: Use when you need the refactored HEP inversion skills in this repository: blocker routing, sample-strategy branching, blinding and fit-policy decisions, or failure-to-skill diagnosis. Prefer this over the legacy `hep-meta-first` routing references when the hard part is deciding what to do next rather than executing a stage.
---

# HEP Analysis Inversions

Use this skill when the workflow is blocked on a decision rather than on a command.

## Quick Start

1. Read `../hep-analysis-meta-pipeline/references/refactored/skills/inversions/analysis_router_inversion.md` for blocker-to-next-skill routing.
2. Read `../hep-analysis-meta-pipeline/references/refactored/skills/inversions/sample_strategy_inversion.md` for nominal sample, process-role, and CR-to-SR strategy decisions.
3. Read `../hep-analysis-meta-pipeline/references/refactored/skills/inversions/blinding_and_fit_policy_inversion.md` for blinding, backend, smoothing, and significance-policy decisions.
4. Read `../hep-analysis-meta-pipeline/references/refactored/skills/inversions/failure_to_skill_inversion.md` when a reviewer has already found a recurring failure or capability gap.
5. Use `../hep-analysis-meta-pipeline/references/refactored/skills/shared/decision_record_template.md` for every non-trivial branch.

## What This Skill Covers

- routing from missing artifact to next skill
- nominal sample and background-strategy branching
- blinding and backend eligibility decisions
- failure classification and skill extraction

## Stop Conditions

- the required evidence for a branch is missing
- a human approval is needed for unblinding or central-result override
- the decision would promote a cross-check into a central claim
