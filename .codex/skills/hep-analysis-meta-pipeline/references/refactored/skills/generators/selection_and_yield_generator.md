# Selection and Yield Generator

Pattern: Generator

Derived from:
- `SKILL_SELECTION_ENGINE_AND_REGIONS`
- `SKILL_CUT_FLOW_AND_YIELDS`

## Purpose

Produce the cut-flow, region-yield, and provenance artifacts that connect executable selections to the event counts and weighted yields used later in histogramming and reporting.

## When to use

- reviewed partition and region contracts exist
- nominal sample semantics are available
- a downstream stage needs cut-flow evidence or central yields

## Required inputs

- region definitions
- sample registry
- nominal sample mapping
- event model or processed sample access

## Outputs

- cut-flow tables
- region-yield tables
- process-aggregated views
- sample-resolved views
- cut-flow provenance

## Generation steps

1. Run the executable region logic over the nominal sample set.
2. Record both unweighted counts and weighted yields.
3. Compute process-level and combined totals without hiding sample-level detail by default.
4. Record uncertainty proxies from event weights.
5. Link final selected yields to the same region semantics that downstream histogramming will use.

## Output contract

- cut-flow steps are ordered
- unweighted counts do not increase across stricter sequential cuts
- MC uncertainties come from weighted bookkeeping
- H to gammagamma cut-flow views separate signal production modes, prompt diphoton background, and data

## Constraints

- merged process rows require an explicit merge map
- alternative samples do not enter central totals unless the decision record says so

## Related skills

- `skills/tool_wrappers/selection_and_partition_wrapper.md`
- `skills/reviewers/nominal_sample_and_normalization_reviewer.md`
- `skills/generators/histogram_and_template_generator.md`
