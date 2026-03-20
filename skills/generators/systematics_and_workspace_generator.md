# Systematics and Workspace Generator

Pattern: Generator

Derived from:
- `SKILL_SYSTEMATICS_AND_NUISANCES`
- `SKILL_WORKSPACE_AND_FIT_PYHF`
- `SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE`
- `SKILL_ASIMOV_EXPECTED_SIGNIFICANCE_SPLUSB`

## Purpose

Generate nuisance, workspace, fit, and significance artifacts after the policy decisions and reviewer gates have established what statistical products are allowed to count as central results.

## When to use

- modeling artifacts are reviewed
- template readiness is reviewed
- the workflow is ready to construct workspaces, fits, and significance products

## Required inputs

- reviewed modeling artifacts
- reviewed templates
- systematics scope
- fit-policy decision record
- fit identifier

## Outputs

- nuisance model
- workspace and fit provenance
- fit results
- significance artifacts
- Asimov provenance and parameter-floating policy

## Generation steps

1. Build nuisance and correlation metadata.
2. Materialize the workspace and fit configuration.
3. Execute the fit wrapper with the approved backend choice.
4. Construct observed or expected significance only if the fit-policy inversion allows it.
5. Record which quantities were fixed or floating, especially for H to gammagamma DSCB and background parameters.

## Output contract

- central H to gammagamma claims name `pyroot_roofit` as the primary backend
- Asimov generation records full-range provenance and `mu_gen = 1` when used for expected discovery significance
- expected and observed significance are never conflated

## Constraints

- a blocked central fit remains blocked rather than downgraded silently into a cross-check
- reviewer gates must pass before the report treats these artifacts as central claims

## Related skills

- `skills/tool_wrappers/fit_and_significance_wrapper.md`
- `skills/reviewers/statistical_readiness_reviewer.md`
- `skills/inversions/blinding_and_fit_policy_inversion.md`
