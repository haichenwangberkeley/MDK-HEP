# Pattern Authoring Guide

This repository uses five skill patterns. Every skill should have one dominant pattern even when it references other patterns.

## Repository-wide rules

- Prefer plain Markdown contracts over harness-specific syntax.
- Keep repository commands, artifact paths, and evidence requirements explicit.
- Treat HEP domain rules as binding. A skill can never relax blinding, provenance, or reviewer gates for convenience.
- Route repeated rules into `skills/shared/` instead of duplicating them across pattern files.
- Every skill must state what blocks execution and what requires human escalation.

## Tool Wrapper

Use a Tool Wrapper when the skill's main job is to call an existing code path, command, script, or workflow component safely and repeatably.

Required content:
- When to use
- Inputs
- Outputs
- Preconditions
- Postconditions
- Call procedure
- Failure modes
- Verification expectations

Repository notes:
- Name the real module, script, or command.
- Separate tool invocation from policy. If the hard part is choosing whether the tool is allowed, that choice belongs in an Inversion or Reviewer.
- Tool Wrappers should emit provenance and point to the reviewer that must validate the result.

## Generator

Use a Generator when the primary responsibility is to create or transform an artifact such as analysis JSON, a registry, templates, plots, reports, or fit products.

Required content:
- Required inputs
- Generation steps
- Output contract
- Constraints
- Examples when useful

Repository notes:
- Generators may call Tool Wrappers but should not embed the wrapper contract inline.
- A Generator must declare what evidence proves the generated artifact is usable downstream.
- If a Generator also decides among competing scientific strategies, split that decision into an Inversion.

## Reviewer

Use a Reviewer when the main job is to check correctness, completeness, compliance, scientific validity, or handoff readiness.

Required content:
- Review scope
- Pass, conditional-pass, block, and fail criteria
- Required evidence
- Common failure modes
- Required remediation guidance

Repository notes:
- Reviewers are independent gates. They do not quietly rewrite outputs.
- Reviewer findings must be traceable to artifacts, logs, or plots.
- A blocking reviewer must state the smallest next skill that can remediate the issue.

## Inversion

Use an Inversion when the key value is working backward from the objective, failure, or constraint to the correct next action.

Required content:
- Trigger condition
- Decision structure
- Branch criteria
- Required evidence per branch
- Output decision record

Repository notes:
- Inversions own ambiguous choices such as nominal sample selection, allowed blinding behavior, and whether a backend can support a central claim.
- Keep branches explicit and fail closed when the evidence is insufficient.
- Do not hide policy decisions inside a Generator or Tool Wrapper.

## Pipeline

Use a Pipeline when the skill orchestrates multiple stages or subskills in sequence or dependency order.

Required content:
- Stage ordering
- Stage inputs and outputs
- Gates
- Dependencies
- Escalation paths
- Logging requirements

Repository notes:
- Pipelines should call smaller skills rather than repeat their full content.
- Each stage must name its producing skills, required reviewers, and exit criteria.
- A Pipeline advances only when mandatory reviewer gates pass.

## Pattern selection checklist

Choose the pattern whose failure would most damage the workflow:

- If misuse of a command is the main risk, use a Tool Wrapper.
- If incorrect artifact construction is the main risk, use a Generator.
- If false confidence is the main risk, use a Reviewer.
- If wrong branching or diagnosis is the main risk, use an Inversion.
- If stage ordering and gates are the main risk, use a Pipeline.
