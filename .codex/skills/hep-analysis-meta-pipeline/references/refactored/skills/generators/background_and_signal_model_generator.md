# Background and Signal Model Generator

Pattern: Generator

Derived from:
- `SKILL_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS`
- `SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION`
- `SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION`

## Purpose

Create the strategy and model artifacts that define how backgrounds are constrained, how blinding is applied, and how signal and background parameterizations are chosen for the HEP fit workflow.

## When to use

- reviewed templates and sample semantics exist
- the analysis needs CR and SR transfer intent, blinding outputs, or signal and background PDF choices
- a fit or report stage needs explicit model provenance

## Required inputs

- template artifacts
- sample semantics and nominal mapping
- fit-region definitions
- blinding and fit-policy decision record

## Outputs

- background modeling strategy
- CR and SR constraint map
- blinding summary
- signal PDF artifact
- background scan and chosen model artifacts
- spurious-signal artifact

## Generation steps

1. Use `sample_strategy_inversion.md` to resolve process roles and constraint intent.
2. Use `blinding_and_fit_policy_inversion.md` to resolve allowed data visibility and fit semantics.
3. Build explicit background modeling and control-to-signal mappings.
4. Generate or record the signal parameterization, background scan, chosen model, and spurious-signal evidence.
5. Emit provenance for nominal template choice, sideband normalization, smoothing context, and blinding behavior.

## Output contract

- every constrained background has an explicit CR to SR map
- blinding behavior is recorded as an artifact, not implied
- nominal background template choice and sideband normalization are explicit for H to gammagamma

## Constraints

- no silent merge of low-statistics auxiliary backgrounds into the central nominal template
- no silent exposure of observed data in a blinded window
- if model choice remains ambiguous, block and escalate through the inversion or reviewer path

## Related skills

- `skills/inversions/sample_strategy_inversion.md`
- `skills/inversions/blinding_and_fit_policy_inversion.md`
- `skills/reviewers/statistical_readiness_reviewer.md`
- `skills/reviewers/blinding_and_visualization_reviewer.md`
