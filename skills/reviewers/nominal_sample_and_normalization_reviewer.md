# Nominal Sample and Normalization Reviewer

Pattern: Reviewer

Derived from:
- `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION`
- `SKILL_MC_SAMPLE_DISAMBIGUATION_AND_NOMINAL_SELECTION`
- `SKILL_MC_NORMALIZATION_METADATA_STACKING`
- `SKILL_13TEV25_DETAILS`

## Review scope

Verify that sample identity, process role, nominal-versus-alternative status, and normalization are explicit enough for central yields and fits.

## Required evidence

- sample registry
- nominal sample selection record
- normalization table
- metadata resolution log
- sample-strategy decision record when ambiguity existed

## Criteria

- `pass`: each sample has one role, one normalization path, and one central-versus-alternative status
- `conditional_pass`: non-central samples or optional metadata gaps are logged without affecting central outputs
- `block`: the central nominal sample set is ambiguous or the normalization inputs are incomplete
- `fail`: central yields would double count processes or misuse metadata

## Common failure modes

- multiple candidate nominal samples for the same process
- raw event counts used instead of signed generator-weight sums
- central results using `36.0 fb^-1` because of stale policy text instead of the repository default `36.1 fb^-1`
- background template choice not traceable to an explicit nominal diphoton sample

## Required remediation guidance

- use `skills/inversions/sample_strategy_inversion.md` to pick the correct branch
- rerun `skills/generators/sample_semantics_generator.md` after the decision record is updated
- escalate if repository facts and metadata cannot establish a unique central sample set

## Related skills

- `skills/shared/open_data_dataset_facts.md`
- `skills/shared/hep_domain_guardrails.md`
