# Codex Skills Index

Canonical entry:

- `$hep-analysis-meta-pipeline`

Session skill packages:

- `hep-analysis-meta-pipeline`: main HEP orchestration entrypoint
- `hep-analysis-pipelines`: pipeline-focused entry skill
- `hep-analysis-inversions`: decision and routing entry skill
- `hep-analysis-generators`: artifact-generation entry skill
- `hep-analysis-reviewers`: validation and gate entry skill
- `hep-analysis-tool-wrappers`: repository command and workflow wrapper entry skill
- `hep-analysis-env-setup`: runtime environment setup helper
- `hep-meta-first`: preserved legacy single-entry pack

Vendored refactored pattern tree:

- `.codex/skills/hep-analysis-meta-pipeline/references/refactored/skills/`

Key vendored files:

- `skills/pipelines/hep_analysis_meta_pipeline.md`
- `skills/inversions/analysis_router_inversion.md`
- `skills/shared/hep_domain_guardrails.md`
- `skills/shared/pipeline_logging_contract.md`
- `skills/shared/artifact_matrix.md`
