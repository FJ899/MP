# Research Gate repair evidence — cycle 2

Review source:
- MP/review-002/AI-B
- verdict: REQUEST_CHANGES
- open finding: MP-R01 only

## Repair

Classification precedence was changed so dependency/runtime manifests are evaluated before generic data-directory exemptions.

Protected counterexamples:
- experiments/requirements.txt
- docs/package.json
- governance/docker-compose.yml
- research/environment.yml

Contract draft exemption is now restricted to design/data formats:
- .json
- .yaml
- .yml
- .md

Therefore:
- contracts/adapter.draft.py => protected
- contracts/candidate_event.schema.draft.json => exempt design draft

## Regression additions

tests/test_research_gate.py now includes direct classification assertions for all five AI-B counterexamples.

It also includes a Git integration regression:

test_manifest_outside_layout_requires_current_build_request

Procedure:
- create experiments/requirements.txt
- commit it in a temporary Git repo
- do not add a current Build Request
- execute Research Gate for base...head

Expected:
- exit code 1
- stderr mentions experiments/requirements.txt
- stderr states no Build Request was added/modified

## Targeted local classifier execution

Observed locally against the repaired classification logic:

experiments/requirements.txt => protected=True
docs/package.json => protected=True
governance/docker-compose.yml => protected=True
research/environment.yml => protected=True
contracts/adapter.draft.py => protected=True
contracts/candidate_event.schema.draft.json => protected=False
main.py => protected=True
research/REPO_RADAR.md => protected=False

All expected classifications matched.

## Execution limitation

The full current GitHub regression suite was not observed through GitHub Actions in this repair step.

The Git integration regression has been added to the repository for independent execution/review.
Do not treat its presence as a GitHub Actions PASS.

## Prior findings

Per MP/review-002/AI-B:
- MP-R02 RESOLVED for reviewed counterexamples
- MP-R03 RESOLVED_BY_INSPECTION
- MP-R04 RESOLVED_BY_EXECUTION

This repair does not reopen them except for regression review.

## M1 boundary

M1 remains OPEN.
Architecture v0.1 remains NOT_READY.
No merge/build/release authorization is created by this repair.
