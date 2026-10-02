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


## Pending M1 artifact decision

Current candidate:
M1_RESULT.md

status:
READY_FOR_INDEPENDENT_REVIEW

Important:
The dispositions EVALUATE / LEARN / PARK in M1_RESULT.md and REPO_RADAR.md are AI-A proposals for review, not HUMAN decisions.

No USE / ADAPT / BUILD decision has been promoted from this M1 work.

Next decision sequence:
AI-B independent review
→ HUMAN M1 artifact decision
→ only then any separately scoped M2 execution authorization.


## D-025 — HUMAN accepts M1 Technology Reconnaissance + Repository Suitability Audit

decision_id:
HUMAN-ARTIFACT-DECISION-M1-001

source:
HUMAN_EXPLICIT_ACCEPT

accepted_subject_version:
c701a8e87ae1f4e067dcabbfd3902bc35b43de19

accepted_review:
MP/m1-repair-review-001/AI-B

review_verdict:
PASS

artifact_decision:
ACCEPT

acceptance_scope:
- first targeted Technology Reconnaissance,
- Repository Suitability Audit,
- current EVALUATE / LEARN / PARK candidate classification,
- explicitly recorded unresolved dependencies and limitations,
- M2_SMOKE_TEST_PLAN.md as a proposal/backlog for later human authorization.

This acceptance does NOT authorize:
- M2 execution,
- dependency installation,
- training,
- implementation or adapter creation,
- BUILD orchestrator,
- merge to main,
- MP Architecture v0.1 freeze,
- flight/route execution,
- publish/release/deploy.

Preserved limitations include:
- BRISQUE default model provenance/terms UNRESOLVED,
- PatchCore exact backbone identity/terms PRECONDITION,
- known-defect checkpoint/license BLOCKED,
- Air 3S compatibility NOT_TESTED,
- quality thresholds NOT_ACCEPTED,
- CandidateEvent semantics OPEN HYPOTHESIS,
- previously recorded Research Gate GitHub-enforcement limitations.

Next project action:
prepare a separate M2-01 Video Timestamp Integrity execution proposal for HUMAN decision.
Do not execute M2 without separate authorization.


## D-026 — HUMAN authorizes M2-01 Video Timestamp Integrity

decision_id:
HUMAN-M2-01-AUTH-001

source:
HUMAN_EXPLICIT_AUTHORIZE_M2_01

proposal_revision:
3

authorized_subject_version:
2b2926d8e0c91997913a30ff889725e0abdf54b7

proposal_artifact:
M2_01_EXECUTION_PROPOSAL.md

authorization_scope:
Execute exactly M2-01 revision 3 on one supplied native DJI Air 3S MP4.

Permitted:
- input SHA-256 and identity recording,
- ffprobe stream discovery,
- two decoded-frame enumerations,
- enumeration-order timestamp anomaly analysis,
- deterministic 10/30/50/70/90% sample selection,
- two exact ordinal-based extraction runs for five frames,
- source RGB24 raw-pixel hashing,
- saved PNG decode-to-RGB24 hashing and dimension comparison,
- PNG byte hashing,
- command stderr/exit-status capture,
- compact evidence package and PASS / FAIL / INCONCLUSIVE result.

Explicitly not authorized:
- M2-02 or later experiments,
- dependency installation,
- model execution/training,
- repository implementation/adapters/orchestrator,
- merge to main,
- architecture freeze,
- flight/route execution,
- publish/release/deploy.

Input:
Air3s_normal.MP4 supplied by HUMAN in current conversation.

Next action:
execute only M2-01 and return result for independent review.


## D-027 — HUMAN accepts M2-01 execution result

decision_id:
HUMAN-ARTIFACT-DECISION-M2-01-001

source:
HUMAN_EXPLICIT_ACCEPT

accepted_experiment:
M2-01-20261001-AIR3S-NORMAL-001

accepted_subject_version:
58e138899829969a6dda5dced482b78c3343279a

accepted_review:
MP/m2-01-execution-review-001/AI-B

review_verdict:
PASS

artifact_decision:
ACCEPT

acceptance_scope:
PASS for timestamp/frame/pixel provenance on the specific supplied sample identified as Air 3S.

Accepted evidence meaning:
for that supplied file and tested runtime, the experiment reproducibly bound:
source SHA-256 -> selected video stream -> decoded-frame ordinal -> raw PTS/timebase -> selected frame -> RGB24 pixels -> saved PNG evidence.

This acceptance does NOT establish:
- general compatibility of every DJI Air 3S recording mode, firmware or codec profile,
- untouched-camera-original chain of custody,
- telemetry compatibility,
- quality-model validity,
- detector validity,
- CandidateEvent behavior,
- 30-minute or end-to-end MP operation.

Preserved limitations:
- one short file / one recording profile,
- no independent proof of untouched camera original,
- telemetry NOT_TESTED,
- BRISQUE default model provenance/terms UNRESOLVED,
- PatchCore exact backbone identity/terms PRECONDITION,
- known-defect checkpoint/license BLOCKED,
- quality thresholds NOT_ACCEPTED,
- CandidateEvent semantics OPEN HYPOTHESIS.

This acceptance does NOT authorize:
- M2-02 or later experiments,
- dependency installation,
- model training/execution beyond separately authorized scope,
- repository implementation/adapters/orchestrator,
- merge to main,
- architecture freeze,
- flight/route execution,
- publish/release/deploy.

Next action:
prepare a separate smallest next quality-signal experiment proposal for review and HUMAN decision.


## D-028 — HUMAN authorizes M2-02A Model-Free Quality Signal Sanity Check

decision_id:
HUMAN-M2-02A-AUTH-001

source:
HUMAN_EXPLICIT_AUTHORIZE_M2_02A

authorized_subject_version:
0fdebf44fc5241163f6dee47fcb189e07c5a9586

proposal_revision:
2

review_reference:
MP/m2-02a-proposal-review-002/AI-B

review_verdict:
PASS

authorization_scope:
Execute exactly M2-02A revision 2.

Permitted:
- reconstruct accepted M2-01 frames p10 / p50 / p90 from the accepted source;
- generate ORIGINAL / BLUR_SIGMA4 / DARK_MINUS96 / BRIGHT_PLUS96 states;
- run exactly two complete deterministic passes;
- calculate only Laplacian variance, mean_gray_intensity, black_fraction and white_fraction;
- preserve source/frame provenance, source/derived RGB24 SHA-256, dimensions, runtime versions, raw clipping counts and metric values;
- apply frozen dtype/filter/border/serialization contract;
- create compact evidence;
- return PASS / FAIL / INCONCLUSIVE.

Clipping semantics:
- no decrease is required;
- strict increase = EXERCISED_CONFIRMED;
- equality = CLIPPING_RESPONSE_NOT_EXERCISED;
- lack of clipping exercise is not an independent FAIL;
- full PASS requires both black and white clipping signals to be exercised at least once, with no decreases;
- parameters must not be tuned after observing results.

Explicitly not authorized:
- BRISQUE,
- dependency installation,
- pretrained models,
- model training,
- production threshold selection,
- quality-gate implementation,
- M2-03 or later experiments,
- BUILD orchestrator,
- merge to main,
- architecture freeze,
- flight/route execution,
- publish/release/deploy.

Result acceptance:
not included.
A later HUMAN artifact decision is required after independent review.

Next action:
execute only M2-02A revision 2 and stop after producing the review candidate.


## D-029 — HUMAN accepts M2-02A execution result

decision_id:
HUMAN-ARTIFACT-DECISION-M2-02A-001

source:
HUMAN_EXPLICIT_ACCEPT

accepted_experiment:
M2-02A-20261002-AIR3S-QUALITY-001

accepted_subject_version:
75f216e0edfc0e975eb5408657acc70584eb060f

accepted_review:
MP/m2-02a-execution-review-001/AI-B

review_verdict:
PASS

artifact_decision:
ACCEPT

acceptance_scope:
M2-02A revision 2 result for p10 / p50 / p90 and ORIGINAL / BLUR_SIGMA4 / DARK_MINUS96 / BRIGHT_PLUS96.

Accepted evidence meaning:
- two-run reproducibility for the recorded 12 states;
- provenance continuity from accepted M2-01 source frames;
- source and derived RGB24 hash consistency;
- expected directional response of Laplacian variance and mean_gray_intensity;
- black and white clipping signals were EXERCISED_CONFIRMED under the frozen transforms.

This acceptance does NOT establish:
- discrimination of naturally good vs naturally bad Air 3S footage,
- operator usefulness,
- production quality thresholds,
- false-positive / false-negative behavior,
- a production quality gate,
- equivalence of the synthetic transforms to natural capture failures,
- superiority over BRISQUE.

Independent-review limitation preserved:
AI-B did not independently replay GaussianBlur pixels because its review environment lacked OpenCV.
That part was verified by script inspection, Run A/B evidence and directional criteria rather than full independent pixel replay.

Evidence-practice note:
historical reconstruction command lines that were not preserved must not be recreated from memory as evidence.
Future experiments should preserve exact invocations plus relevant stdout/stderr, exit statuses, script identity and runtime identity.

This acceptance does NOT authorize:
- another experiment,
- BRISQUE,
- dependency installation,
- pretrained models,
- training,
- production thresholds,
- quality-gate implementation,
- M2-03,
- BUILD orchestrator,
- merge to main,
- architecture freeze,
- flight/route execution,
- publish/release/deploy.

Next action:
prepare a separate proposal for the smallest useful natural-degradation Air 3S test with HUMAN quality judgment.
Do not execute it without separate HUMAN authorization.


## D-030 — HUMAN accepts M2-02B revision 2 plan only

decision_id:
HUMAN-PLAN-DECISION-M2-02B-001

source:
HUMAN_EXPLICIT_ACCEPT_PLAN_ONLY

accepted_proposal:
M2-02B — Natural Quality Relevance Pilot

accepted_subject_version:
58be2e74fac96858dbf38ef134bc489614a023c4

proposal_revision:
2

accepted_review:
MP/m2-02b-proposal-review-002/AI-B

review_verdict:
PASS

decision:
ACCEPT_PLAN_ONLY

acceptance_scope:
Accept the construction of M2-02B revision 2, including scene contracts, matched-group admission, INPUT_MATCH_INVALID, HUMAN_DEGRADATION_NOT_EXERCISED, deterministic midpoint-frame selection, masked-condition HUMAN review, frozen HUMAN labels before metric disclosure, inherited M2-02A calculation contract, family-level support semantics, overall PASS / FAIL / INCONCLUSIVE, provenance and evidence requirements.

Execution status:
NOT_STARTED / BLOCKED_BY_INPUT.

Execution authorization:
NOT_GRANTED.

Input status:
NOT_ESTABLISHED.

This decision authorizes only an availability check of already accessible Air 3S material.

It does NOT authorize:
- M2-02B execution,
- HUMAN labeling,
- metric calculation,
- flight or route execution,
- recording new footage,
- BRISQUE,
- dependency installation,
- pretrained models,
- training,
- production thresholds,
- quality-gate implementation,
- M2-03+,
- BUILD orchestrator,
- merge to main,
- architecture freeze,
- publish/release/deploy.

Next action:
inspect only already available sources for candidate native Air 3S material and report INPUT_READINESS or INPUT_GAP_REPORT.


## D-031 — HUMAN authorizes INPUT_CLASSIFICATION_PRECHECK for M2-02B

decision_id:
HUMAN-M2-02B-INPUT-CLASSIFICATION-PRECHECK-AUTH-001

source:
HUMAN_EXPLICIT_AUTHORIZE_INPUT_CLASSIFICATION_PRECHECK

authorization_context_subject:
ea3ffdd425197762490dca4cbcfbdcf85bf5c305

authorized_action:
INPUT_CLASSIFICATION_PRECHECK on already accessible existing material only.

scope:
- inspect already accessible Air 3S native video files and associated existing still/raw material;
- identify plausible scene clusters and candidate REF / NAT_BLUR / NAT_DARK / NAT_BRIGHT roles;
- inspect file/container metadata and representative visual samples only as needed for classification;
- report whether any complete plausible four-condition matched set exists;
- preserve uncertainty between AVAILABLE, DECLARED_BUT_UNVERIFIED, POTENTIAL_SCENE_MATCH, MISSING and NOT_ESTABLISHED;
- prepare INPUT_READINESS or INPUT_GAP_REPORT.

explicitly_not_authorized:
- M2-02B execution;
- metric calculation;
- HUMAN quality labeling;
- formal matched-group admission;
- formal midpoint-frame selection for the experiment;
- parameter tuning;
- BRISQUE;
- dependency installation;
- pretrained models;
- training;
- flight or route execution;
- recording new material;
- M2-03+;
- BUILD orchestrator;
- merge to main;
- architecture freeze;
- publish/release/deploy.

result_acceptance:
not included.
Any later M2-02B execution still requires a separate HUMAN authorization.

stop_rule:
stop after the classification precheck and return the resulting readiness/gap packet.
