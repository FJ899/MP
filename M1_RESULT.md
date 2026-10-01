# M1 Result — Technology Reconnaissance + Repository Suitability Audit

status: READY_FOR_INDEPENDENT_REVIEW
human_acceptance: PENDING
architecture_freeze: NOT_READY
implementation_authorization: NOT_GRANTED
merge_authorization: NOT_GRANTED

## Goal preserved

M1 remained centered on the project hypothesis:

Can MP reduce post-flight inspection material to a limited, evidence-backed set of places a human should CONFIRM / REJECT / RECHECK?

M1 did not redesign the project into autonomy, 3D mapping, a drone controller or a production product.

## Main result

The first MP proof does not need a custom implementation of every originally imagined layer.

Existing components can test most early uncertainties:

1. video decode/timestamp provenance:
   FFmpeg + OpenCV

2. one existing image-quality signal:
   BRISQUE, subject to a separate default-model provenance/license precondition

3. unknown-irregularity branch:
   Anomalib / PatchCore

4. candidate-region temporal persistence:
   SAM2.1 Hiera Small

5. same-frame detector-box fusion:
   Weighted Boxes Fusion

6. temporal association:
   Norfair

Reference implementations already cover useful mechanisms for:
- quality→recollection,
- detector authority vs VLM explanation,
- detector→temporal propagation,
- persistent defect identity,
- spatial deduplication,
- targeted reinspection.

The main integration gap remaining after reconnaissance is narrower:

provenance-preserving construction of an MP CandidateEvent from raw observations, same-frame fusion and temporal continuity evidence.

That gap is identified, not authorized for BUILD.

## Proposed M2 evaluation set

EVALUATE:
- FFmpeg
- OpenCV
- rehanguha/brisque
- Anomalib PatchCore
- SAM2.1 Hiera Small
- Weighted Boxes Fusion
- Norfair

See:
M2_SMOKE_TEST_PLAN.md

## Intentionally not in first M2 executable set

### Known-defect detector — BLOCKED

Reason:
no exact task-relevant checkpoint with acceptable/known use terms is pinned yet.

BFD-UAV2K supplies strong task evidence but its README says license information is pending.
Ultralytics supplies a framework, not proof that generic pretrained weights detect facade defects.

Do not substitute generic COCO YOLO and call it a meaningful defect smoke test.

### VLM — PARK

Reason:
first establish useful candidate evidence.
AI-Visual-Inspector is retained as a reference for detector authority + descriptive VLM.

### CVAT — PARK

Reason:
annotation infrastructure should follow demonstrated data/labeling burden, not precede it.

### Telemetry / route generation / COLMAP — PARK / NON-BLOCKING

Reason:
first prove vision candidate value.
Existing parsers/mission generators already reduce the risk of later reinventing these layers.

## Proposed component dispositions

| Area | Candidate | Proposed M1 disposition | Reason |
|---|---|---|---|
| ingestion | FFmpeg/OpenCV | EVALUATE M2 | minimal mature decode/frame path |
| scene detection | PySceneDetect | PARK | scene cuts != defect/recheck events |
| quality | BRISQUE | EVALUATE M2 WITH PRECONDITION | code Apache-2.0; default SVM/normalization artifacts separately unresolved |
| quality architecture | IIQC | LEARN | closest recollection pattern; direct dependency too heavy/license unclear |
| anomaly | PatchCore | EVALUATE M2 | unknown irregularity test with normal-reference bank |
| VLM pattern | AI-Visual-Inspector | LEARN / PARK runtime | detector decides, VLM explains |
| known defect | BFD benchmark + detector families | BENCHMARK / BLOCK runtime | evidence useful; executable checkpoint/license unresolved |
| sliced inference | SAHI | PARK until detector | mode, not detector |
| segmentation/tracking | SAM2.1 Small | EVALUATE M2 | clean box→mask propagation and license |
| VOS alternative | Cutie | PARK | fallback only; weight terms unresolved |
| temporal fusion reference | DEVA | LEARN | useful detector→propagation pattern |
| box fusion | WBF | EVALUATE M2 | solved same-frame geometry fusion |
| temporal association | Norfair | EVALUATE M2 | moving-camera/custom distance support |
| ByteTrack | ByteTrack | PARK | less aligned/heavier for first unusual association test |
| spatial dedup | tank-inspection-uav | LEARN | simple 3D radius dedup once coordinates exist |
| persistence | AegisInspect | LEARN | persistent identity/evidence boundary |
| whole system | Hawk-I | LEARN | architecture competitor/reference only |
| reinspection | dual-UAV pipeline | LEARN | durable flagged-target→second inspection pattern |
| revisit policy | RDMO Digital Twin | LEARN | revisit policy trade-offs |
| telemetry | existing parsers | PARK | Air 3S file compatibility later |
| route | existing KMZ/WPML tools | PARK | custom generator unjustified |
| 3D | COLMAP | PARK | not required for first proof |

## M1 DONE coverage

### D1 — exact source identity or UNRESOLVED

Status:
SATISFIED FOR M1 CANDIDATE SET.

Evidence:
research/PINNED_SOURCES.md

Every serious source has an exact repository + pinned commit.
Material unknowns are named rather than guessed.

### D2 — verified INPUT -> FUNCTION -> OUTPUT

Status:
SATISFIED BY SOURCE INSPECTION FOR SHORTLISTED/REFERENCE COMPONENTS.

Evidence:
AUDIT_MATRIX.md
audits/*.md

Limitation:
SOURCE_INSPECTED only. Runtime compatibility is not implied.

### D3 — repository license separated from model/weights/data license

Status:
SATISFIED AFTER MP-M1-001 CORRECTION, SUBJECT TO REVIEW.

Examples:
- BRISQUE: repository/code context Apache-2.0; bundled svm.txt + normalize.pickle provenance/terms are separately UNRESOLVED.
- SAM2: code + checkpoints explicitly Apache-2.0 in source README.
- Anomalib: code Apache-2.0; pretrained backbone/model terms remain separate and unresolved before execution.
- Ultralytics: code AGPL-3.0; exact defect weights unresolved.
- BFD-UAV2K: dataset license pending.
- Cutie: code MIT; pretrained-weight terms not separately established.
- IIQC/Hawk-I/AegisInspect: useful references but project license unresolved/no license found.

No UNKNOWN is converted to permission to reuse code/data/model artifacts.

### D4 — CPU/GPU requirements sourced

Status:
SATISFIED FOR PROPOSED M2 CANDIDATES AT REQUIREMENT LEVEL.

Examples:
- BRISQUE: CPU image metric stack.
- PatchCore/Anomalib: CPU and accelerator extras available.
- SAM2: documented Python/PyTorch/CUDA/GPU path.
- WBF: NumPy/Pandas/Numba CPU numeric fusion.
- Norfair core: CPU; detector may require GPU.
- FFmpeg/OpenCV: CPU baseline.

Limitation:
MP hardware benchmarks are NOT_RUN.

### D5 — training/reference/weights/prompt/downstream dependencies identified

Status:
SATISFIED AFTER MP-M1-001 CORRECTION, SUBJECT TO REVIEW.

Key dependencies:
- BRISQUE default path needs bundled svm.txt + normalize.pickle; their provenance/terms remain unresolved before M2-02.
- PatchCore needs normal-reference images + pretrained backbone.
- SAM2 needs candidate prompt/box and checkpoint.
- WBF needs detector boxes/scores/labels.
- Norfair needs detections and an association/distance configuration.
- SAHI needs an underlying detector.
- known-defect path needs actual task-relevant weights/data.

### D6 — adapter need classified

Status:
SATISFIED.

Evidence:
AUDIT_MATRIX.md and component audit files.

No orchestrator implementation exists.

### D7 — each KEEP/USE/ADAPT tied to RECHECK hypothesis

Status:
SATISFIED FOR PROPOSED EVALUATE SET.

M1 intentionally does not use USE/ADAPT as accepted decisions before HUMAN review.
Each EVALUATE candidate has a specific M2 question related to evidence reduction or candidate-event construction.

### D8 — no speculative component retained only for future value

Status:
SATISFIED.

Examples deliberately PARKED:
- VLM,
- CVAT,
- telemetry,
- route generation,
- COLMAP,
- ByteTrack,
- extra VOS alternatives.

Reference repos remain because they answer a current design question, not because they may someday be useful.

### D9 — COLMAP/telemetry are not hard dependencies

Status:
SATISFIED.

They remain PARK/NON-BLOCKING.

### D10 — concrete M2 smoke-test candidate list

Status:
SATISFIED.

Evidence:
M2_SMOKE_TEST_PLAN.md

Seven small proposed tests plus explicitly BLOCKED/PARKED paths.

### D11 — major problem areas have recorded Vertical/Horizontal search

Status:
SATISFIED FOR FIRST TARGETED RECONNAISSANCE PASS.

Evidence:
research/SEARCH_LOG.md

Recorded areas:
- whole system,
- ingestion,
- quality,
- anomaly,
- detector,
- segmentation/tracking,
- merger/temporal,
- telemetry,
- route generation,
- recheck/recollection.

Direct NO_RESULT recheck searches are retained and not interpreted as global absence.

### D12 — Radar candidate fields

Status:
SATISFIED FOR SERIOUS M1 CANDIDATES.

Evidence:
research/REPO_RADAR.md

Includes:
name, source identity, search type, problem, I/O, license, activity, tests/evidence, documentation, compute, maturity, integration cost, what to learn, replaces what, role, decision and why.

### D13 — durable rejection rationale

Status:
NOT_APPLICABLE / NO HARD REJECT YET.

M1 intentionally used PARK when evidence is insufficient or a component is unnecessary now.
No repository is falsely labeled REJECTED merely to satisfy the criterion.

If a later smoke test produces REJECT, research/REJECTED_SOLUTIONS.md defines the durable record.

### D14 — custom BUILD must prove existing alternatives insufficient

Status:
SATISFIED AS A GOVERNANCE CONDITION; NO BUILD PROPOSAL EXISTS.

The CandidateEvent semantic gap is explicitly documented but is not a build request.

No custom ingestion, quality model, mask tracker, generic fusion tracker, telemetry parser or KMZ generator is proposed for BUILD.

### D15 — architecture is not frozen before reconnaissance review

Status:
SATISFIED.

MP Architecture v0.1 remains NOT_READY.

## Open gaps presented to review

These are not silently treated as solved:

1. Known-defect execution:
   task-relevant checkpoint + license unresolved.

2. BRISQUE model chain:
   default svm.txt + normalize.pickle provenance/terms must be resolved before M2-02 default-model execution.

3. PatchCore model chain:
   exact pretrained backbone identity/terms must be pinned before M2 execution.

4. Runtime:
   all proposed M2 candidates remain INSTALL_NOT_RUN / SMOKE_TEST_NOT_RUN by MP.

5. Air 3S:
   no actual Air 3S video/log compatibility test has been run in M1.

6. Quality:
   no accepted threshold exists.

7. Merger:
   CandidateEvent semantics are a discovered integration gap; no custom implementation is authorized.

8. Licensing:
   several reference implementations have no clear repository license.
   They remain LEARN references only.

9. Reconnaissance coverage:
   targeted and sufficient for current decisions, not an exhaustive literature/commercial-product survey.

10. GitHub enforcement:
   Research Gate technical repair was accepted, but GitHub Actions run/required merge enforcement remains a separate known limitation.

## Recommended reviewer decision surface

AI-B should not decide final architecture.

Review should answer:

1. Is the first reconnaissance pass broad enough to stop searching and begin the proposed M2 smoke phase after HUMAN decision?
2. Are any EVALUATE candidates unjustified or missing a materially better inspected alternative?
3. Is the known-defect path correctly BLOCKED rather than faked with generic weights?
4. Is the CandidateEvent merger gap real enough to preserve as an open hypothesis?
5. Are any license/hardware/source claims overstated?
6. Is M2_SMOKE_TEST_PLAN.md the smallest useful next experiment set, or can it be reduced further?

## Candidate M1 state

M1:
READY_FOR_INDEPENDENT_REVIEW

M1:
NOT HUMAN_ACCEPTED

MP Architecture v0.1:
NOT READY TO FREEZE

Implementation:
NOT AUTHORIZED

Merge:
NOT AUTHORIZED
