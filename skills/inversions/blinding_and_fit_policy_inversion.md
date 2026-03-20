# Blinding and Fit Policy Inversion

Pattern: Inversion

Derived from:
- `SKILL_ENFORCEMENT_POLICY_DEFAULTS`
- `SKILL_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION`
- `SKILL_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION`
- `SKILL_WORKSPACE_AND_FIT_PYHF`
- `SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE`
- `SKILL_ASIMOV_EXPECTED_SIGNIFICANCE_SPLUSB`
- `SKILL_STATTOOL_OPTIONAL_PYHF_BACKEND`
- `SKILL_ROOTMLTOOL_CACHED_ANALYSIS`

## Trigger condition

Use this inversion when the agent must decide whether a fit, significance result, smoothing choice, or backend can legitimately support a central claim.

## Decision structure

1. Decide whether the run is blinded or explicitly unblinded.
2. Decide whether the requested statistical output is expected or observed.
3. Decide whether the available backend can support a central claim or only a cross-check.
4. Decide whether effective-luminosity and smoothing rules are satisfied or should block the stage.

## Branch criteria

- Blinded run: observed significance is blocked; expected significance may proceed only with full-range Asimov pseudo-data.
- Explicitly unblinded run: observed significance may proceed if the reviewer evidence is complete.
- RooFit available: central H to gammagamma fit path is allowed.
- Only non-ROOT backend available: cross-check only, or block if the user requested a central claim.
- Effective luminosity below policy or smoothing required without provenance: block central fit progression.

## Required evidence per branch

- enforcement or luminosity artifacts
- smoothing artifacts
- backend availability evidence
- blinding summary
- user-approved unblinding status when applicable

## Output decision record

Record:

- blinding state
- allowed significance modes
- allowed backend role
- smoothing and effective-luminosity disposition
- blocking reasons

## Related skills

- `skills/reviewers/statistical_readiness_reviewer.md`
- `skills/shared/hep_domain_guardrails.md`
