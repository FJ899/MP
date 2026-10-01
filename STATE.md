# STATE

protocol: TWO-WEBAI/0.2
project_id: MP
state_version: 12
goal_version: 1
project_profile: REPO_INTEGRATION
work_mode: AUDIT / M2_TRANSITION_PLANNING
changed_fields: M2_01_proposal_revision_2, M2_01_status_semantics, frame_identity_procedure, state_version, next_action

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
M2 TRANSITION — PROPOSAL ONLY

MP Architecture v0.1:
NOT READY TO FREEZE / NOT AUTHORIZED TO FREEZE

M2_01:
PROPOSAL_REVISION_2_READY_FOR_HUMAN_DECISION

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
REVISION_2 / PENDING HUMAN DECISION

## M2-01 input availability

required_input:
one native DJI Air 3S MP4 clip, 30–60 seconds.

repository_scan:
NO VIDEO FILE FOUND in FJ899/MP at accepted M1 candidate.

conversation/library search:
NO NATIVE AIR 3S MP4 FOUND.
Search returned documentation/reports but no relevant video artifact.

input_status:
NOT_STARTED / BLOCKED_BY_INPUT.

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
- Air 3S compatibility: NOT_TESTED.
- quality thresholds: NOT_ACCEPTED.
- CandidateEvent integration semantics: OPEN HYPOTHESIS.
- M2 runtime evidence: NOT_RUN.
- MP end-to-end: NOT_BUILT / NOT_RUN.

## M2-01 proposal review

review_packet:
MP/m2-01-proposal-review-001/AI-B

review_result:
PROPOSAL_DIRECTION_ACCEPTED / REVISION_REQUIRED

revision_completed:
YES

proposal_revision:
2

Key corrections recorded:
- 10/30/50/70/90% targets are derived from the observed selected-stream timestamp range T_min..T_max, not from zero;
- raw PTS and best_effort_timestamp remain distinct;
- both enumeration_ordinal and presentation_ordinal are preserved;
- exact extraction uses decoded-frame ordinal selection, not approximate seek;
- source/frame identity, decoded-pixel equality and PNG-byte equality are evaluated separately;
- current pre-execution state is NOT_STARTED / BLOCKED_BY_INPUT, not INCONCLUSIVE.

No experiment command was executed as part of this revision.

## Next action

HUMAN reviews M2_01_EXECUTION_PROPOSAL.md revision 2 and returns one of:
- AUTHORIZE_M2_01
- ACCEPT_PLAN_ONLY
- REQUEST_CHANGES
- DEFER

Do not execute M2-01 until:
1. HUMAN explicitly authorizes M2-01 execution, and
2. a native Air 3S clip is available if the result is intended to establish Air 3S compatibility.

No installation, extraction, decoding experiment or evidence generation is authorized by M1 acceptance alone.
