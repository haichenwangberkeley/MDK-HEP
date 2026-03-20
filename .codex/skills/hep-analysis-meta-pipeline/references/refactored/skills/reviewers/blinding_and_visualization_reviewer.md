# Blinding and Visualization Reviewer

Pattern: Reviewer

Derived from:
- `SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION`
- `SKILL_VISUAL_VERIFICATION`
- `SKILL_HISTOGRAM_PLOTTING_INVARIANTS`

## Review scope

Verify that blinding, plot content, plot captions, and visual diagnostics satisfy repository physics and reporting rules.

## Required evidence

- blinding summary
- plot manifest
- report markdown or draft
- category, control-region, and signal-region plots

## Criteria

- `pass`: blinding and visual requirements are satisfied and traceable
- `conditional_pass`: minor style issues remain but the scientific message and blinding state are intact
- `block`: a required plot class or caption is missing, or blinding behavior is undocumented
- `fail`: observed data in a blinded window are exposed or required H to gammagamma plots are absent

## Common failure modes

- signal-region observed data shown in blinded mode
- control-region pre-fit and post-fit comparisons missing
- plot captions absent or detached from the figures
- category-resolved or statistical-input plots missing for H to gammagamma

## Required remediation guidance

- use `skills/inversions/blinding_and_fit_policy_inversion.md` to resolve policy ambiguity
- rerun `skills/generators/background_and_signal_model_generator.md` or `skills/generators/report_package_generator.md` for missing artifacts
- keep discrepancies visible; never remediate by hiding bins or relabeling plots cosmetically

## Related skills

- `skills/shared/plotting_invariants.md`
- `skills/generators/report_package_generator.md`
