# Data-MC Discrepancy Reviewer

Pattern: Reviewer

Derived from:
- `SKILL_DATA_MC_DISCREPANCY_SANITY_CHECK`

## Review scope

Check whether substantial disagreement between observed data and MC expectations has been investigated, classified, and reported honestly.

## Required evidence

- data-versus-MC plots and tables
- discrepancy audit
- discrepancy check log
- cut-flow and yield context
- normalization and sample-mapping artifacts

## Criteria

- `pass`: the audit exists and all substantial discrepancies are either explained or openly unresolved
- `conditional_pass`: no substantial discrepancy is present and the explicit zero-issue path is documented
- `block`: discrepancy artifacts are missing or incomplete
- `fail`: the workflow hid or cosmetically suppressed a material discrepancy

## Common failure modes

- discrepancy artifacts missing on a supposedly clean run
- changes to binning, selection, or sample composition made only to improve visual agreement
- bug and modeling-mismatch cases not distinguished

## Required remediation guidance

- send implementation issues to `skills/inversions/failure_to_skill_inversion.md`
- rerun the affected generator or wrapper with the smallest possible write scope
- keep the discrepancy visible in the report even when unresolved

## Related skills

- `skills/generators/report_package_generator.md`
- `skills/reviewers/reproducibility_and_handoff_reviewer.md`
