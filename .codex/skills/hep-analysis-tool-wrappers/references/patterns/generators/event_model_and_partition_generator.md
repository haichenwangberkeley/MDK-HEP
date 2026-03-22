# Event Model and Partition Generator

Pattern: Generator

Derived from:
- `SKILL_EVENT_IO_AND_COLUMNAR_MODEL`
- `SKILL_OBJECT_DEFINITIONS`
- `SKILL_CATEGORY_CHANNEL_REGION_PARTITIONING`

## Purpose

Turn the reviewed analysis summary into executable object, category, channel, and region contracts that downstream selection stages can run without interpreting prose on the fly.

## When to use

- the summary reviewer has approved the overall schema
- category, object, or region logic changed
- downstream stages need a stable partition spec or object-definition record

## Required inputs

- normalized summary
- event column availability
- category and region intent
- sample semantics when category roles depend on process assignments

## Outputs

- object-definition record
- partition specification
- region definition contract
- overlap-policy manifest

## Generation steps

1. Resolve which observables and derived quantities are available from the event model.
2. Write object definitions before region logic.
3. Generate category and channel partitions with stable identifiers.
4. Encode SR, CR, SB, and VR roles explicitly.
5. Surface any ambiguity about overlap or region purpose before the selection engine runs.

## Output contract

- all identifiers are unique
- region logic is executable
- mutual exclusivity is the default for regions used together in a fit

## Constraints

- prose-only selections are not sufficient
- any overlap exception must be explicit and justified
- region definitions must stay aligned with the reviewed summary

## Related skills

- `../tool_wrappers/selection_and_partition_wrapper.md`
- `../reviewers/analysis_summary_reviewer.md`
- `../pipelines/hep_analysis_meta_pipeline.md`
