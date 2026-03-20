# Selection and Partition Wrapper

Pattern: Tool Wrapper

Derived from:
- `SKILL_EVENT_IO_AND_COLUMNAR_MODEL`
- `SKILL_CATEGORY_CHANNEL_REGION_PARTITIONING`
- `SKILL_SELECTION_ENGINE_AND_REGIONS`

## When to use

Use this wrapper when the agent needs to materialize region partitions, process events into executable selections, or inspect per-sample region yields through repository code.

## Inputs

- normalized summary
- sample registry
- region or partition configuration
- input data paths
- optional event cap

## Outputs

- partition specs under `outputs/partition/`
- per-sample selection or region artifacts
- region yield and overlap evidence consumed by downstream generators

## Preconditions

- object and region intent are defined in the summary or generator contract
- sample semantics are available

## Postconditions

- selection logic is executable rather than prose-only
- overlap evidence exists for reviewer checks

## Call procedure

1. Use `.rootenv/bin/python -m analysis.selections.partitioning` to materialize category and region partitions.
2. Use `.rootenv/bin/python -m analysis.selections.engine` for per-sample selection and cut-flow execution.
3. Use `.rootenv/bin/python -m analysis.io.readers` only for focused event-ingestion inspection, not as a substitute for partition or selection evidence.

## Failure modes

- partition identifiers not aligned with the normalized summary
- SR and CR overlap unresolved
- selection expressions not executable

## Verification expectations

- partition and selection artifacts exist
- overlap checks are explicit
- downstream cut-flow and template generators consume the same region definitions

## Related skills

- `../generators/event_model_and_partition_generator.md`
- `../generators/selection_and_yield_generator.md`
- `../reviewers/analysis_summary_reviewer.md`
