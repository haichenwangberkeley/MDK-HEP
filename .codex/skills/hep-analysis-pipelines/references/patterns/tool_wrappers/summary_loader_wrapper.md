# Summary Loader Wrapper

Pattern: Tool Wrapper

Derived from:
- `SKILL_READ_SUMMARY_AND_VALIDATE`
- `SKILL_JSON_SPEC_DRIVEN_EXECUTION`

## When to use

Use this wrapper when the agent needs a normalized analysis summary, schema validation, inventory counts, or overlap-policy outputs derived from the repository summary loader.

## Inputs

- analysis summary JSON path
- output directory

## Outputs

- `outputs/summary.normalized.json`
- `outputs/validation/inventory.json`
- `outputs/validation/diagnostics.json`
- `outputs/validation/overlap_policy.json`

## Preconditions

- the summary file exists
- preflight has not already blocked execution

## Postconditions

- the repository summary loader is the only source of normalized summary structure used downstream
- any normalization or schema error is surfaced instead of repaired silently

## Call procedure

1. Run `.rootenv/bin/python -m analysis.config.load_summary --summary <summary> --out <outputs/summary.normalized.json>` when a direct normalized summary artifact is needed.
2. Use `analysis.cli bootstrap` when the surrounding bootstrap outputs are also needed.
3. Hand the produced artifacts to the summary reviewer before downstream generation begins.

## Failure modes

- invalid enums or missing required keys
- unresolved region, fit, or signature references
- missing or contradictory overlap policy

## Verification expectations

- the normalized summary exists
- diagnostics are empty or explicitly blocking
- reviewer findings cite the normalized summary rather than the raw narrative prompt

## Related skills

- `../reviewers/analysis_summary_reviewer.md`
- `../generators/analysis_spec_generator.md`
- `../pipelines/spec_to_runtime_pipeline.md`
