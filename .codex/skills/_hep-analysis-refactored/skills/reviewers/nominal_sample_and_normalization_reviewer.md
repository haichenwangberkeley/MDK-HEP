# Nominal Sample and Normalization Reviewer

Pattern: Reviewer

Derived from:
- `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION`
- `SKILL_MC_SAMPLE_DISAMBIGUATION_AND_NOMINAL_SELECTION`
- `SKILL_MC_NORMALIZATION_METADATA_STACKING`
- `SKILL_13TEV25_DETAILS`

## Review scope

Verify that sample identity, nominal-versus-alternative status, and normalization are explicit enough for central yields, templates, and fits.

## Required evidence

- signal-signature and likelihood-intake decision record
- sample registry
- sample contract set
- nominal sample selection record
- normalization table
- metadata resolution log
- sample-strategy decision record when ambiguity existed

## Criteria

- `pass`: each relevant process has one central nominal path, one explicit normalization mode, and any alternatives are segregated from the central prediction
- `conditional_pass`: non-central samples or optional metadata gaps are logged without affecting central outputs
- `block`: the central nominal sample set is ambiguous or the normalization inputs are incomplete
- `fail`: central yields would double count processes or misuse metadata

## Common failure modes

- multiple candidate nominal samples for the same process
- raw event counts used instead of signed generator-weight sums
- central results using `36.0 fb^-1` because of stale policy text instead of the repository default `36.1 fb^-1`
- background normalization mode is missing for a process that is intended to be theory-constrained, CR-constrained, or floating
- background template choice is not traceable to an explicit nominal diphoton sample

## Required remediation guidance

- rerun `../inversions/signal_signature_and_likelihood_intake_inversion.md` when the authority for nominal choice is missing
- use `../inversions/sample_strategy_inversion.md` to pick the correct branch
- rerun `../generators/sample_semantics_generator.md` after the decision record is updated
- run `likelihood_sample_role_reviewer.md` when data, template, or validation roles remain mixed
- escalate if repository facts and metadata cannot establish a unique central sample set

## Related skills

- `likelihood_sample_role_reviewer.md`
- `../shared/open_data_dataset_facts.md`
- `../shared/hep_domain_guardrails.md`
