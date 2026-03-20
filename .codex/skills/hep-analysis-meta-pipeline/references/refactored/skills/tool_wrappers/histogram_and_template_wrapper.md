# Histogram and Template Wrapper

Pattern: Tool Wrapper

Derived from:
- `SKILL_HISTOGRAMMING_AND_TEMPLATES`
- `SKILL_FREEZE_ANALYSIS_HISTOGRAM_PRODUCTS`

## When to use

Use this wrapper when the agent needs repository code to build histograms, create fit templates, or reuse cached histogram products.

## Inputs

- processed samples or selection outputs
- runtime defaults and observable definitions
- histogram output path
- optional cache or freeze settings

## Outputs

- histogram products under `outputs/hists/`
- cache artifacts under `outputs/cache/`
- freeze or manifest metadata when histogram products are intentionally reused

## Preconditions

- nominal sample selection is reviewable
- selections and observables are fixed for the current stage

## Postconditions

- histogram artifacts preserve statistical bookkeeping and provenance
- template reuse is explicit rather than implicit

## Call procedure

1. Use `.rootenv/bin/python -m analysis.hists.histmaker` for direct histogram production where a focused stage run is enough.
2. Use `analysis.pipeline.run_all_stages` or `.rootenv/bin/python -m analysis.cli run` when histogram production must stay aligned with the integrated pipeline outputs.
3. Record whether cache reuse or frozen products were used before statistical stages begin.

## Failure modes

- mismatched binning across compared templates
- missing provenance for reused histogram products
- histogram products not aligned with the reviewed nominal sample set

## Verification expectations

- template manifests exist
- statistical bookkeeping such as weighted yields or `sumw2` is preserved
- smoothing and effective-luminosity reviewers receive the same template set that the fits will consume

## Related skills

- `../generators/histogram_and_template_generator.md`
- `../reviewers/statistical_readiness_reviewer.md`
- `../shared/plotting_invariants.md`
