# DECISIONS

## D-001 — Laboratory before product
Human decision: build a lab to test RECHECK value before defining the final product.

## D-002 — Post-flight first
Air 3S is initially only a material source. Drone-control integration is outside the first proof.

## D-003 — Telemetry after vision value
Timestamp -> telemetry is deferred until the vision pipeline produces useful candidate events.

## D-004 — 3D only if needed
COLMAP / detailed geometry are LATER unless simple timestamp-to-telemetry proves insufficient.

## D-005 — Thin replaceable integration
Analyzers should communicate through a common normalized contract so a component can be replaced without rebuilding the full pipeline.

## D-006 — Audit before build
No orchestrator architecture is frozen before real I/O, dependencies and constraints of candidates are audited.

## Pending decisions
- final M1 KEEP/LATER/DROP set
- exact common event contract
- whether VLM belongs in first executable smoke test
- exact YOLO model/weights
- exact telemetry parser

## D-007 — Vertical + horizontal search before major component design
Human decision: before designing a major component, run both:
- VERTICAL SEARCH for near-end-to-end systems,
- HORIZONTAL SEARCH for implementations of the exact component.

## D-008 — BUILD is the last option
Human decision: the default sequence is PROBLEM -> SEARCH EXISTING SOLUTIONS -> INSPECT/RUN -> COMPARE -> BORROW/ADAPT/BUILD. Custom implementation requires evidence that reuse/adaptation is insufficient.

## D-009 — Repository role classification
Human decision: repositories are classified as DEPENDENCY, COMPONENT, REFERENCE_IMPLEMENTATION, BENCHMARK or REJECTED. Evaluation status/decision is tracked separately as EVALUATE, USE, ADAPT, LEARN, REJECT or PARK.

## D-010 — Durable rejection rationale
Human decision: rejected solutions remain recorded with WHY and evidence so later work can explain why a custom solution exists.

## D-011 — Architecture freeze follows reconnaissance
Human decision: one Technology Reconnaissance pass around the current MP architecture must complete before MP Architecture v0.1 is frozen.

## D-012 — YOLO is a candidate, not an architectural decision
Human decision: detector selection must be informed by task-relevant benchmarks/datasets; YOLO is one candidate alongside alternatives such as RT-DETR or other methods supported by evidence.

## Working hypothesis — VLM authority
Source-derived hypothesis to test, not yet a frozen human decision:
use the detector/anomaly model as the source of detection verdict and treat VLM output as interpretation/explanation unless MP evidence later justifies a stronger role.

## D-013 — Two search rhythms
Human decision:
- targeted search is mandatory before designing each major component,
- broad ecosystem scan is periodic only, normally weekly or biweekly when useful,
- do not run a daily broad "AI drone repo" search that creates noise without a decision hinge.

## D-014 — Research Gate is a merge prerequisite for major build work
Human intent interpreted from current instruction: search must not be optional memory. Major implementation changes require a durable research record plus build request satisfying VERTICAL + HORIZONTAL search before BUILD.

## D-015 — Layered enforcement
Project governance uses:
- AGENTS.md for AI entry instructions,
- BUILD_POLICY.md as normative contract,
- structured research/build records for machine validation,
- GitHub Actions Research Gate for automated checking,
- PR template/CODEOWNERS for review discipline.

## D-016 — Main branch rules remain a required external configuration
A CI workflow alone cannot guarantee that an administrator will not bypass or disable it. Strong enforcement requires a GitHub ruleset/branch-protection rule that requires the Research Gate status check and review for governance/workflow changes.

Observed current repo state:
no repository ruleset configured.

Connector limitation:
current GitHub integration exposes ruleset reads but not ruleset/branch-protection writes.


## D-017 — Build Requests are per-change, not reusable blanket permissions
Correction after AI-B review:
Every protected implementation diff requires a Build Request added or modified in that same diff. Authorization uses an exact file list; wildcard scopes such as src/** are rejected.

Purpose:
prevent an accepted historical request from silently authorizing a future model family or subsystem.

## D-018 — Narrow repair reuses research, not stale change authorization
A NARROW_REPAIR may reuse the accepted Research Record for its component and does not require repeating Vertical/Horizontal search.

It still requires a current per-change Build Request that records:
- repair_of,
- exact authorized_files,
- component_id,
- pinned Research Record SHA-256,
- real human authorization provenance.

## D-019 — Unknown implementation locations fail closed
Executable/code files outside canonical component paths are protected by default.
Moving code to main.py, tools/, governance/ or another unrecognized location is not a bypass.

## D-020 — Research Gate validation is regression-tested
Gate changes must preserve tests for:
- unknown path blocking,
- stale request blocking,
- narrow repair reuse,
- glob rejection,
- real ISO dates,
- non-empty queries,
- valid integration_role.


## D-021 — Functional manifests outrank directory exemptions
Correction after AI-B review MP/review-002:
Dependency/runtime manifests are classified before generic documentation/data-directory exemptions.

Therefore requirements.txt, package.json, docker-compose.yml, environment.yml and equivalent manifests remain protected regardless of placement under docs/, experiments/, governance/, research/ or another data-oriented directory.

## D-022 — Draft contract exemption is format-limited
Only explicit contract design/data drafts in JSON/YAML/YML/Markdown are exempt from implementation gating.

A filename containing ".draft." does not exempt executable code.
Example:
contracts/adapter.draft.py remains protected.

## D-023 — Second repair-review cycle is final automatic loop
This is repair-review cycle 2 of the protocol maximum 2.
If AI-B still identifies a blocking/major Research Gate defect after this candidate, AI-A must escalate to HUMAN instead of silently starting a third repair cycle.


## D-024 — HUMAN accepts Research Gate repair MP-R01–MP-R04

decision_id:
HUMAN-ARTIFACT-DECISION-RG-001

source:
HUMAN_EXPLICIT_ACCEPT

subject_version:
f799d26184504ae890b3a8ab064ad29de9267cbd

artifact_decision:
ACCEPT

acceptance_scope:
Techniczna naprawa Research Gate MP-R01–MP-R04, reviewed by AI-B in MP/review-003/AI-B.

This acceptance does NOT authorize:
- merge,
- BUILD orchestrator,
- product implementation,
- release/deploy/publication,
- M1 closure,
- MP Architecture v0.1 freeze.

Preserved limitations:
- GitHub Actions PASS not observed,
- hard merge enforcement not verified,
- classic branch protection unavailable through current connector,
- process records do not cryptographically prove human intent,
- semantic correctness of future code still requires review.

Next approved project activity:
continue unfinished M1 Technology Reconnaissance.
