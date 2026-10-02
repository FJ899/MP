# STATE

protocol: TWO-WEBAI/0.2
project_id: MP
state_version: 18
goal_version: 1
project_profile: REPO_INTEGRATION
work_mode: AUDIT / M2_TRANSITION_PLANNING
changed_fields: M2_02A_human_authorization, execution_status, state_version, next_action

## Approved goal

Sprawdzić, czy z istniejących narzędzi można złożyć minimalne laboratorium, które przyjmuje materiał z lotu inspekcyjnego, analizuje go kilkoma komplementarnymi metodami, łączy wyniki i przekazuje operatorowi ograniczoną listę miejsc CONFIRM / REJECT / RECHECK.

Hypothesis:
Czy MP wyławia z 30 minut filmu miejsca, którym człowiek rzeczywiście powinien przyjrzeć się ponownie?

## Research Gate

technical_repair_acceptance:
HUMAN_ACCEPTED_IN_REVIEWED_SCOPE

accepted_research_gate_version:
f799d26184504ae890b3a8ab064ad29de9267cbd

decision_id:
HUMAN-ARTIFACT-DECISION-RG-001

Known limitations remain:
- GitHub Actions PASS for accepted artifact was not observed,
- hard merge enforcement is not verified,
- classic branch protection is unavailable through connector,
- future semantic correctness and NARROW_REPAIR classification still require review.

## M1 artifact decision

m1_status:
HUMAN_ACCEPTED

m1_decision_id:
HUMAN-ARTIFACT-DECISION-M1-001

m1_decision_source:
HUMAN_EXPLICIT_ACCEPT

accepted_M1_version:
c701a8e87ae1f4e067dcabbfd3902bc35b43de19

accepted_review:
MP/m1-repair-review-001/AI-B

accepted_review_verdict:
PASS

acceptance_scope:
- first targeted Technology Reconnaissance,
- Repository Suitability Audit,
- current EVALUATE / LEARN / PARK set,
- explicit unresolved dependencies and limitations,
- M2_SMOKE_TEST_PLAN.md as a proposal/backlog only.

Important:
the accepted artifact remains exactly c701a8e87ae1f4e067dcabbfd3902bc35b43de19.
Commits after that version record the HUMAN decision and prepare transition planning; they do not silently redefine the accepted M1 artifact.

## Current phase

current_phase:
M2 — M2-01 ACCEPTED / NEXT EXPERIMENT PROPOSAL ONLY

MP Architecture v0.1:
NOT READY TO FREEZE / NOT AUTHORIZED TO FREEZE

M2_01:
HUMAN_ACCEPTED / PASS_FOR_SUPPLIED_SAMPLE

M2_execution:
NOT AUTHORIZED

dependency_installation:
NOT AUTHORIZED

implementation:
NOT AUTHORIZED

merge_to_main:
NOT AUTHORIZED

publish/release/deploy:
NOT AUTHORIZED

flight/route_execution:
NOT AUTHORIZED

## Proposed first experiment

experiment_id:
M2-01

name:
Video Timestamp Integrity

goal:
Sprawdzić powtarzalne powiązanie klatki z czasem i źródłowym materiałem, potrzebne dla dowodów RECHECK.

proposal_artifact:
M2_01_EXECUTION_PROPOSAL.md

proposal_status:
REVISION_3 / REVIEWED PASS / HUMAN AUTHORIZED

## M2-01 input availability

required_input:
one native DJI Air 3S MP4 clip, 30–60 seconds.

repository_scan:
NO VIDEO FILE FOUND in FJ899/MP at accepted M1 candidate.

conversation/library search:
NO NATIVE AIR 3S MP4 FOUND.
Search returned documentation/reports but no relevant video artifact.

input_status:
AVAILABLE — Air3s_normal.MP4 supplied by HUMAN.

Substitute video:
may test generic procedure only;
must NOT be used as evidence of Air 3S compatibility.

## M2-01 execution environment availability

Observed environment without installing anything:

ffmpeg:
7.1.5-0+deb13u1

ffprobe:
7.1.5-0+deb13u1

ffmpeg build note:
Debian build reports --enable-gpl.
This binary identity must be recorded in experiment evidence and is not assumed identical to the M1 pinned FFmpeg source commit.

python:
3.13.5

opencv_python:
4.13.0

minimal_M2_01_installation_need:
NONE for the proposed ffprobe/ffmpeg path.

OpenCV:
available but optional for M2-01; not required for the minimal first execution proposal.

GPU:
NOT REQUIRED.

## Preserved limitations from accepted M1

- BRISQUE default model provenance/terms: UNRESOLVED.
- PatchCore exact backbone identity/terms: PRECONDITION.
- known-defect checkpoint/license: BLOCKED.
- M2-01 timestamp/frame provenance: TESTED / PASS for the specific supplied sample identified as Air 3S; general Air 3S compatibility: NOT_ESTABLISHED.
- quality thresholds: NOT_ACCEPTED.
- CandidateEvent integration semantics: OPEN HYPOTHESIS.
- M2-01 runtime evidence: PASS and HUMAN_ACCEPTED; all other M2 experiments: NOT_RUN.
- MP end-to-end: NOT_BUILT / NOT_RUN.

## M2-01 proposal review

review_packet:
MP/m2-01-proposal-review-002/AI-B

review_result:
REQUEST_CHANGES

revision_completed:
YES

proposal_revision:
3

Prior revision-2 corrections remain preserved.

New revision-3 corrections:
- selected timestamp integrity is now inspected in original enumeration_ordinal order before any sorting;
- every MISSING, DUPLICATE and REGRESSION timestamp event is retained with ordinal/value evidence;
- sorting into presentation_ordinal is used only for deterministic sample selection and cannot erase anomalies from PASS evaluation;
- every timestamp regression requires diagnosis before PASS;
- duplicate timestamps do not automatically fail if frame identity remains unambiguous through ordinal evidence;
- PNG extraction now explicitly inserts format=rgb24;
- source selected-frame pixels are hashed as explicit RGB24 rawvideo;
- every saved PNG is decoded back to RGB24 and its pixel hash + dimensions are compared against the selected source-frame RGB24 evidence;
- PNG file SHA remains a separate byte-container check.

No experiment command was executed as part of this revision.

## M2-01 HUMAN authorization

decision_id:
HUMAN-M2-01-AUTH-001

source:
HUMAN_EXPLICIT_AUTHORIZE_M2_01

authorized_subject_version:
2b2926d8e0c91997913a30ff889725e0abdf54b7

proposal_revision:
3

authorization_scope:
exact M2-01 only.

Explicitly not authorized:
- M2-02 or later,
- dependency installation,
- model execution/training,
- repository implementation,
- merge,
- architecture freeze,
- flight/route execution,
- publish/release/deploy.

## M2-01 execution result

experiment_id:
M2-01-20261001-AIR3S-NORMAL-001

proposal_revision:
3

execution_result:
PASS

review_status:
HISTORICAL — SUPERSEDED BY MP/m2-01-execution-review-001/AI-B PASS AND HUMAN ACCEPTANCE

input:
Air3s_normal.MP4

input_size_bytes:
74451639

input_sha256:
cc8ace8fc18280d09318d29f5b7dbcc1b7b44d986c2d83035d4421e0d927bcaa

tested_stream:
global stream index 0 — HEVC 3840x2160, 30000/1001 fps, time_base 1/30000

observed_duration:
11.244567 s

frame_count:
337

timestamp_basis:
RAW_PTS

timestamp_integrity_run1:
MISSING=0 / DUPLICATE=0 / REGRESSION=0 / FORWARD=336

timestamp_integrity_run2:
MISSING=0 / DUPLICATE=0 / REGRESSION=0 / FORWARD=336

selected_ordinals:
34 / 101 / 168 / 235 / 302

formal_probe_runs_identity_equal:
YES

formal_command_nonzero_status:
NONE

for all five samples:
- showinfo PTS/time matched selected frame,
- source RGB24 Run A == source RGB24 Run B,
- saved PNG decoded RGB24 == corresponding source RGB24,
- dimensions matched 3840x2160,
- PNG byte SHA-256 Run A == Run B.

result_interpretation:
For this supplied Air 3S sample and tested runtime, MP can reproducibly bind source SHA-256 -> stream -> decoded-frame ordinal -> raw PTS/timebase -> extracted frame -> RGB24 pixels -> saved PNG evidence.

limitations:
- supplied clip is 11.244567 s, shorter than proposed target 30–60 s,
- embedded identifiers strongly support Air 3S identity but no independent chain-of-custody proves an untouched camera original,
- one file/recording profile does not establish all Air 3S modes,
- no telemetry, quality model, detector or other AI component was tested.

execution_incidents:
1. transient PIPESTATUS wrapper defect before clean formal run;
2. transient stdin/sample-list wrapper defect before clean formal restart;
3. container harness timeout after completed formal Run A and Run B p10; remaining independent Run B samples continued.

incident_boundary:
No incident is treated as media/timestamp failure. PASS is based only on the clean formal evidence set and all-zero formal command statuses.

repository_evidence:
- evidence/m2-01/M2-01-20261001-AIR3S-NORMAL-001/RESULT.md
- evidence/m2-01/M2-01-20261001-AIR3S-NORMAL-001/selected_samples.csv
- evidence/m2-01/M2-01-20261001-AIR3S-NORMAL-001/statuses_formal.txt
- evidence/m2-01/M2-01-20261001-AIR3S-NORMAL-001/HASH_EVIDENCE.md
- evidence/m2-01/M2-01-20261001-AIR3S-NORMAL-001/INCIDENTS.md

## Authorization after M2-01

M2-01:
EXECUTED UNDER HUMAN-M2-01-AUTH-001

M2-02:
NOT AUTHORIZED

dependency installation:
NOT AUTHORIZED

implementation:
NOT AUTHORIZED

merge_to_main:
NOT AUTHORIZED

architecture_freeze:
NOT AUTHORIZED

publish/release/deploy:
NOT AUTHORIZED

flight/route execution:
NOT AUTHORIZED

## Next action

Execute exactly M2-02A revision 2 under HUMAN-M2-02A-AUTH-001.

After execution:
- record PASS / FAIL / INCONCLUSIVE,
- preserve compact evidence,
- submit the result to AI-B for independent review,
- stop.

Do not execute BRISQUE, M2-03 or later work.
Do not freeze architecture.


## M2-01 artifact decision

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

accepted_review_verdict:
PASS

artifact_decision:
ACCEPT

acceptance_scope:
PASS for timestamp/frame/pixel provenance on the specific supplied sample identified as Air 3S.

Accepted meaning:
source SHA-256 -> selected stream -> decoded-frame ordinal -> raw PTS/timebase -> selected frame -> RGB24 pixels -> saved PNG evidence was reproducible for the tested file/profile/runtime.

General Air 3S compatibility:
NOT_ESTABLISHED.

Other M2 runtime:
NOT_RUN.

Important:
the accepted M2-01 result artifact remains exactly 58e138899829969a6dda5dced482b78c3343279a.
Later commits only record HUMAN acceptance and prepare a separate proposal.

Non-authorizations remain:
- M2-02/M2-02A execution NOT AUTHORIZED,
- dependency installation NOT AUTHORIZED,
- model execution/training NOT AUTHORIZED unless separately approved,
- implementation/adapters/orchestrator NOT AUTHORIZED,
- merge NOT AUTHORIZED,
- architecture freeze NOT AUTHORIZED,
- flight/route execution NOT AUTHORIZED,
- publish/release/deploy NOT AUTHORIZED.


## Next experiment proposal

proposal_id:
M2-02A

name:
Model-Free Quality Signal Sanity Check

proposal_artifact:
M2_02A_QUALITY_SIGNAL_PROPOSAL.md

proposal_status:
REVISION_2 / REVIEWED PASS / HUMAN AUTHORIZED

execution_status:
AUTHORIZED / EXECUTION_PENDING

execution_authorization:
GRANTED FOR M2-02A REVISION 2 ONLY

BRISQUE branch:
BLOCKED_BY_MODEL_ARTIFACT_TERMS

BRISQUE unresolved artifacts:
- brisque/models/svm.txt
- brisque/models/normalize.pickle

Proposed alternative:
use already available OpenCV/NumPy only, with no pretrained model and no new installation, to test directional sanity of:
- Laplacian variance for controlled blur,
- mean luma,
- black clipping fraction,
- white clipping fraction

on three provenance-anchored frames and deterministic synthetic stress variants.

Available runtime observed during proposal preparation:
- Python 3.13.5
- opencv-python 4.13.0.92
- NumPy 2.3.5

Important input gap:
no reviewed naturally degraded Air 3S frame set with human quality labels is available.
Therefore M2-02A can only test deterministic directional sanity, not real-world threshold/classification performance.

No quality threshold is proposed or accepted.
No experiment has been executed under M2-02A.


## M2-02A proposal review correction

review_packet:
MP/m2-02a-proposal-review-001/AI-B

review_result:
REQUEST_CHANGES

proposal_revision:
2

execution_status:
NOT_STARTED

execution_authorization:
NOT_GRANTED

resolved_review_point:
M2-02A-P01 — strict clipping inequality.

Revision-2 semantics:
- black_fraction(DARK_CLIP) and white_fraction(BRIGHT_CLIP) must not decrease;
- strict increase records EXERCISED_CONFIRMED;
- equality records CLIPPING_RESPONSE_NOT_EXERCISED;
- lack of exercise is not a signal FAIL by itself;
- overall full-hypothesis PASS requires both clipping signals to be exercised and confirmed at least once with no decreases;
- if reproducibility / blur / mean-intensity checks are resolved but a clipping signal is never exercised, overall result is INCONCLUSIVE while resolved sub-results are preserved;
- frozen ±96 transforms cannot be tuned after seeing results to force PASS.

Non-blocking notes incorporated:
- grayscale output is described as grayscale intensity, not physical luminance;
- exact dtype conversions, GaussianBlur/Laplacian parameters, BORDER_DEFAULT and serialization/raw clipping counts are specified;
- M2-01 historical review status is marked as superseded by PASS + HUMAN acceptance.

No M2-02A command has been executed.


## M2-02A HUMAN authorization

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
exact M2-02A revision 2 only.

Result acceptance:
NOT_GRANTED / requires later HUMAN artifact decision.

Preserved non-authorizations:
- BRISQUE,
- dependency installation,
- pretrained models,
- training,
- production thresholds,
- quality-gate implementation,
- M2-03+,
- BUILD orchestrator,
- merge,
- architecture freeze,
- flight/route execution,
- publish/release/deploy.
