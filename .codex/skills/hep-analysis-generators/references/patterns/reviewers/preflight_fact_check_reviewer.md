# Preflight Fact Check Reviewer

Pattern: Reviewer

Derived from:
- `SKILL_AGENT_PRE_FLIGHT_FACT_CHECK`

## Review scope

Verify that the analysis objective, inputs, runtime scope, and repository readiness are unambiguous enough to start execution without inventing missing physics content.

## Required evidence

- user task or approved execution contract
- summary path or narrative source
- preflight outputs
- runtime and inputs path confirmation

## Criteria

- `pass`: objective, summary, inputs, and run scope are explicit
- `conditional_pass`: small non-physics ambiguities remain but are logged and non-blocking
- `block`: a missing fact would force the agent to guess analysis intent, luminosity, blinding scope, or central-result method
- `fail`: the repository or requested paths are not runnable for the requested task

## Common failure modes

- no validated summary or no approved narrative-to-summary translation
- missing explicit unblinding instruction when observed significance is requested
- unclear input data location or output location
- runtime environment missing required capabilities for the requested central claim

## Required remediation guidance

- route narrative ambiguity to `../generators/analysis_spec_generator.md`
- route runtime issues to `../tool_wrappers/runtime_and_preflight_wrapper.md`
- escalate to a human when the missing fact cannot be reconstructed from repository artifacts

## Related skills

- `../pipelines/spec_to_runtime_pipeline.md`
- `../shared/review_rubric.md`
