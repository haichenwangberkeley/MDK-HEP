# Sample Semantics Generator

Pattern: Generator

Derived from:
- `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION`
- `SKILL_MC_NORMALIZATION_METADATA_STACKING`

## Purpose

Generate the reviewed sample registry, machine-readable likelihood sample contracts, normalization records, and nominal-versus-alternative mapping needed for central yields, templates, and fits.

## When to use

- normalized summary is ready
- sample inventory or metadata changed
- a reviewer blocked central results because the sample semantics are ambiguous

## Required inputs

- normalized summary
- input sample inventory
- metadata CSV artifact or equivalent metadata source; in this vendored pack the file is `../metadata.csv`, while some legacy repo layouts used `skills/metadata.csv`
- luminosity policy
- signal-signature and likelihood-intake decision record
- sample-strategy decision record
- likelihood sample contract schema

## Outputs

- sample registry
- likelihood sample contract set
- MC sample selection or nominal mapping record
- normalization table
- sample classification and process-role metadata
- relevance and exclusion log
- metadata resolution log

## Generation steps

1. Build the registry keyed by stable sample identifiers.
2. Match metadata rows and compute normalization factors with explicit unit handling.
3. Instantiate one contract record per central or reviewer-visible sample using the likelihood-sample schema.
4. Separate data, signal, irreducible background, reducible background, and negligible semantics.
5. Mark one nominal sample set per central process and record alternatives, validation-only samples, or discarded candidates separately.
6. Emit provenance linking the summary, intake decision, strategy decision, metadata source, and selected luminosity.

## Output contract

- central outputs never double count nominal and alternative samples
- each contract declares provenance, likelihood role, physics role, nominality, normalization mode, and event-overlap policy
- observed data and template-source data never share the same contract record
- default central luminosity is `36.1 fb^-1` unless an approved override is recorded
- signed generator-weight sums remain intact

## Constraints

- intake ambiguity routes to `../inversions/signal_signature_and_likelihood_intake_inversion.md`
- relevance or nominality ambiguity routes to `../inversions/sample_strategy_inversion.md`
- the generator never invents missing cross section or sum-of-weights values
- the generator never invents fake-rate arguments, closure evidence, or decorrelation claims
- sample names alone are insufficient when stable identifiers are available

## Related skills

- `../tool_wrappers/sample_registry_and_metadata_wrapper.md`
- `data_driven_template_generator.md`
- `../reviewers/nominal_sample_and_normalization_reviewer.md`
- `../reviewers/likelihood_sample_role_reviewer.md`
- `../shared/likelihood_sample_contract_schema.md`
- `../inversions/sample_strategy_inversion.md`
