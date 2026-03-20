# Sample Registry and Metadata Wrapper

Pattern: Tool Wrapper

Derived from:
- `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION`
- `SKILL_MC_NORMALIZATION_METADATA_STACKING`
- `SKILL_MC_SAMPLE_DISAMBIGUATION_AND_NOMINAL_SELECTION`

## When to use

Use this wrapper when the agent needs to call repository code that inventories samples, builds the sample registry, resolves metadata, or writes normalization tables.

## Inputs

- normalized summary
- input sample directory
- target luminosity
- optional DSID or sample filters for scoped runs

## Outputs

- `outputs/samples.registry.json`
- `outputs/report/mc_sample_selection.json`
- `outputs/normalization/norm_table.json`
- metadata resolution outputs written by the repository pipeline

## Preconditions

- summary validation has passed
- the target luminosity and sample identifiers are explicit or reviewable

## Postconditions

- sample registry, nominal mapping, and normalization evidence exist before cut flows or templates are treated as central

## Call procedure

1. Use `.rootenv/bin/python -m analysis.samples.registry` for direct registry building when a targeted stage run is sufficient.
2. Use `.rootenv/bin/python -m analysis.samples.metadata` or the integrated pipeline when metadata resolution and `skills/metadata.csv` updates are needed.
3. Use `.rootenv/bin/python -m analysis.samples.strategy` after the registry exists if background strategy outputs are required immediately.

## Failure modes

- ambiguous nominal sample choice
- metadata rows missing cross section, k-factor, filter efficiency, or signed sum of weights
- lumi policy not aligned with repository guardrails

## Verification expectations

- the nominal-versus-alternative distinction is explicit
- normalization artifacts are reviewer-ready
- any sample ambiguity is routed to `sample_strategy_inversion.md`

## Related skills

- `skills/generators/sample_semantics_generator.md`
- `skills/reviewers/nominal_sample_and_normalization_reviewer.md`
- `skills/inversions/sample_strategy_inversion.md`
