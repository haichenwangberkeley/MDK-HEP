# Histogram and Template Generator

Pattern: Generator

Derived from:
- `SKILL_HISTOGRAMMING_AND_TEMPLATES`
- `SKILL_FREEZE_ANALYSIS_HISTOGRAM_PRODUCTS`

## Purpose

Generate the histogram and template artifacts that statistical and reporting stages consume, while keeping cache reuse or frozen products explicit and auditable.

## When to use

- reviewed selections and observables exist
- downstream modeling needs a stable template set
- a rerun should reuse or freeze expensive histogram products

## Required inputs

- processed samples or selection outputs
- reviewed observables
- normalization and sample semantics
- cache or freeze policy

## Outputs

- histogram template manifest
- per-sample or per-process template artifacts
- cache or freeze provenance
- template-level statistical bookkeeping

## Generation steps

1. Build templates from the reviewed nominal sample set.
2. Keep observable definitions and binning stable within a comparison set.
3. Preserve weighted yields and statistical uncertainty bookkeeping.
4. If products are reused, emit a manifest that proves exactly which products were frozen or loaded from cache.

## Output contract

- fit-critical templates remain traceable to the nominal sample set
- cache reuse is explicit
- smoothing is not implied by template production

## Constraints

- the generator does not decide whether smoothing is allowed
- frozen templates must remain immutable for the remainder of the reviewed run

## Related skills

- `../tool_wrappers/histogram_and_template_wrapper.md`
- `../reviewers/statistical_readiness_reviewer.md`
- `../shared/plotting_invariants.md`
