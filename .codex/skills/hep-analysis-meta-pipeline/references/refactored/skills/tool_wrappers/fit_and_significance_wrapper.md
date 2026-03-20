# Fit and Significance Wrapper

Pattern: Tool Wrapper

Derived from:
- `SKILL_WORKSPACE_AND_FIT_PYHF`
- `SKILL_PROFILE_LIKELIHOOD_SIGNIFICANCE`
- `SKILL_ASIMOV_EXPECTED_SIGNIFICANCE_SPLUSB`
- `SKILL_STATTOOL_OPTIONAL_PYHF_BACKEND`

## When to use

Use this wrapper when the agent needs to execute the repository fit, systematics, or significance code after policy decisions have already established whether the result can support a central claim.

## Inputs

- reviewed model artifacts
- reviewed template artifacts
- fit identifier
- backend decision record
- output directory

## Outputs

- fit outputs under `outputs/fit/<FIT_ID>/`
- significance outputs under `outputs/fit/<FIT_ID>/`
- systematics outputs consumed by the final report

## Preconditions

- statistical readiness reviewer has not blocked the stage
- any central-result backend decision has already been made

## Postconditions

- fit and significance provenance are explicit
- cross-check results are labeled as cross-checks rather than silently promoted

## Call procedure

1. Use `.rootenv/bin/python -m analysis.stats.fit` for direct fit execution when the workspace is already prepared.
2. Use `.rootenv/bin/python -m analysis.stats.systematics` when nuisance artifacts need a focused refresh.
3. Use `.rootenv/bin/python -m analysis.cli run` when fit and significance should remain coupled to the integrated pipeline.
4. Use direct Python entrypoints for significance only when the stage contract explicitly documents the function-level invocation and provenance.

## Failure modes

- RooFit unavailable for a central H to gammagamma claim
- significance constructed with the wrong blinding scope or parameter-floating policy
- optional backends mislabeled as central outputs

## Verification expectations

- fit provenance names the backend
- significance provenance names the dataset type and generation hypothesis
- reviewer evidence distinguishes expected and observed significance

## Related skills

- `skills/generators/systematics_and_workspace_generator.md`
- `skills/reviewers/statistical_readiness_reviewer.md`
- `skills/inversions/blinding_and_fit_policy_inversion.md`
