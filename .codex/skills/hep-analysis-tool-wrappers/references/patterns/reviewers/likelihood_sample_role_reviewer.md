# Likelihood Sample Role Reviewer

Pattern: Reviewer

Derived from:
- `SKILL_SAMPLE_REGISTRY_AND_NORMALIZATION`
- `SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION`
- `SKILL_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS`

## Review scope

Verify that every data or MC sample used by the analysis has an explicit role in the likelihood and that observed data, data-driven templates, nominal MC, and alternative MC are not conflated.

## Required evidence

- signal-signature and likelihood-intake decision record
- sample contract set
- nominal sample selection record
- data-driven template contracts when used
- region map and event-overlap policy
- closure or weak-correlation rationale when data-driven templates are used

## Criteria

- `pass`: every central or reviewer-visible sample has an explicit likelihood role, physics role, nominality, and normalization mode
- `conditional_pass`: optional validation-only or non-central samples remain explicit and segregated from central likelihood inputs
- `block`: observed-data and template-source roles are ambiguous, or the role contract is incomplete for a central input
- `fail`: the same events are implicitly used on both the observed-data side and the PDF side of the likelihood, or a noncentral alternative is silently promoted

## Common failure modes

- the same data events appear as both `observed_data` and `template_source` without a disjoint-event declaration
- a data-driven template lacks closure, decorrelation, or weak-correlation rationale
- reducible, irreducible, and negligible background classes are asserted without supporting reasoning
- an MC alternative sample is used as the central template without explicit approval
- normalization mode is missing for a background that should be theory-constrained, CR-constrained, floating, or shape-only
- the template observable or transfer relation is not stated

## Required remediation guidance

- rerun `../inversions/signal_signature_and_likelihood_intake_inversion.md` when the likelihood roles are underspecified
- use `../inversions/sample_strategy_inversion.md` when process relevance or nominality remains ambiguous
- rerun `../generators/sample_semantics_generator.md` to regenerate the sample contracts
- rerun `../generators/data_driven_template_generator.md` when a template-source contract is incomplete or missing

## Related skills

- `../shared/likelihood_sample_contract_schema.md`
- `../shared/hep_domain_guardrails.md`
- `nominal_sample_and_normalization_reviewer.md`
