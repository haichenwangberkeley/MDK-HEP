# Sample Semantics Generator

Pattern: Generator

Derived from:
- `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION`
- `SKILL_MC_NORMALIZATION_METADATA_STACKING`

## Purpose

Generate the reviewed sample registry, normalization records, nominal-versus-alternative mapping, and process-role metadata needed for central yields and fits.

## When to use

- normalized summary is ready
- sample inventory or metadata changed
- a reviewer blocked central results because the sample semantics are ambiguous

## Required inputs

- normalized summary
- input sample inventory
- metadata CSV artifact or equivalent metadata source; in this vendored pack the file is `../metadata.csv`, while some legacy repo layouts used `skills/metadata.csv`
- luminosity policy and sample-strategy decision record

## Outputs

- sample registry
- MC sample selection or nominal mapping record
- normalization table
- sample classification and process-role metadata
- metadata resolution log

## Generation steps

1. Build the registry keyed by stable sample identifiers.
2. Match metadata rows and compute normalization factors with explicit unit handling.
3. Separate data, signal, and background semantics.
4. Mark one nominal sample set per central process and record alternatives separately.
5. Emit provenance linking the summary, metadata source, and selected luminosity.

## Output contract

- central outputs never double count nominal and alternative samples
- default central luminosity is `36.1 fb^-1` unless an approved override is recorded
- signed generator-weight sums remain intact

## Constraints

- ambiguity routes to `sample_strategy_inversion.md`
- the generator never invents missing cross section or sum-of-weights values
- sample names alone are insufficient when stable identifiers are available

## Related skills

- `../tool_wrappers/sample_registry_and_metadata_wrapper.md`
- `../reviewers/nominal_sample_and_normalization_reviewer.md`
- `../inversions/sample_strategy_inversion.md`
