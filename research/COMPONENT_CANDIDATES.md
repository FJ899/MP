# COMPONENT CANDIDATES — M1 Synthesis

Status: CANDIDATE_SET_READY_FOR_REVIEW
Architecture freeze: NOT_READY

This file maps each MP problem area to existing solutions after the first targeted Technology Reconnaissance pass.

## 1. Video ingestion

Search status:
COMPLETE FOR M1 FIRST PASS.

Inspected:
- FFmpeg
- OpenCV
- PySceneDetect
- PyAV
- VidGear

Proposed M2 evaluation:
FFmpeg + OpenCV.

PARK:
PySceneDetect, PyAV, VidGear.

Reason:
no evidence that a custom or broader ingestion framework improves the RECHECK hypothesis.

Audit:
audits/video-ingestion.md

## 2. Quality gate

Search status:
COMPLETE FOR M1 FIRST PASS.

Inspected:
- IIQC
- Framework-for-UAV-image-quality
- rehanguha/brisque

Proposed M2:
BRISQUE as one existing licensed quality signal on manually obvious good/bad frames.

LEARN:
IIQC architecture and simple blur/exposure metric families.

PARK as direct dependency:
IIQC and Framework-for-UAV-image-quality because of scope/licensing concerns.

No operational quality threshold is selected.

Audit:
audits/quality-gate.md

## 3. Anomaly path

Search status:
SUFFICIENT FOR M1 FIRST PASS.

Candidate:
open-edge-platform/anomalib / PatchCore.

Reference:
AI-Visual-Inspector.

Proposed M2:
small PatchCore normal-reference experiment.

Authority hypothesis:
detector/anomaly model decides anomaly evidence;
VLM may later explain but does not override the detector in the first design hypothesis.

Unresolved:
pretrained backbone/model-license chain must be pinned before execution.

## 4. Known-defect detector

Search status:
COMPLETE FOR M1 FIRST PASS; EXECUTION PRECONDITION UNRESOLVED.

Benchmark:
BFD-UAV2K.

Candidate families evidenced by benchmark:
- YOLO family
- RT-DETR
- Faster R-CNN
- Cascade R-CNN

Framework candidate:
Ultralytics.

Optional later mode:
SAHI sliced inference.

M2:
BLOCKED until task-relevant weights/checkpoint + acceptable license are identified or HUMAN authorizes a deliberately scoped training experiment on suitably licensed data.

Important:
generic COCO YOLO is not accepted as facade-defect validation.

Audit:
audits/detector-selection.md

## 5. Segmentation / tracking

Search status:
COMPLETE FOR M1 FIRST PASS.

Inspected:
- SAM2
- Cutie
- XMem
- DEVA
- Track-Anything
- CoTracker discovery

Proposed M2:
SAM2.1 Hiera Small with a supplied candidate box on one short clip.

LEARN:
DEVA detector→temporal-fusion architecture.

PARK:
Cutie/XMem/Track-Anything unless SAM2 smoke exposes a real gap.

Audit:
audits/segmentation-tracking.md

## 6. Merger / temporal event clustering

Search status:
COMPLETE FOR M1 FIRST PASS, WITH AN EXPLICIT INTEGRATION GAP.

Inspected:
- Weighted Boxes Fusion
- Norfair
- ByteTrack
- DEVA
- tank-inspection-uav spatial aggregator
- AegisInspect persistence patterns
- Hawk-I NMS/integration patterns

Solved subproblems:
- same-frame box fusion: WBF/NMS
- temporal association: Norfair/SAM2/DEVA patterns
- later coordinate-space dedup: spatial registry patterns

No inspected repo directly solves:
provenance-preserving CandidateEvent construction for static surface defects seen repeatedly by a moving UAV camera.

Proposed M2:
- WBF semantics smoke
- Norfair moving-camera association smoke
- compare with SAM2 persistence evidence
- only then revise Observation/CandidateEvent contract.

Audit:
audits/merger-temporal.md

## 7. Telemetry

Search status:
COMPLETE FOR M1 FIRST PASS.

Candidates:
- FergusInLondon/dji_parse
- jetervaz/dji-telemetry
- AiryAir/dji-srt2csv
- aero-oli/DatCon

Current uncertainty:
actual Air 3S recording/log format and available fields.

Status:
PARK / NON-BLOCKING.

First later test:
inspect one actual Air 3S output file/log before selecting a parser.

## 8. Route generation

Search status:
COMPLETE FOR M1 FIRST PASS.

Candidates:
- BanaanKiamanesh/WayPoint
- fcsonline/droneroute
- jamiepinkham/drone-mission-planning

Findings:
- WayPoint README explicitly claims Air 3S support.
- DroneRoute provides WPML/KMZ/controller transfer but current support list does not establish Air 3S.
- drone-mission-planning contains Air 3S-specific format research but says calibration against a real Air 3S dummy mission is still required.

Status:
PARK.
No custom KMZ generator is justified.

## 9. Recheck / recollection

Search status:
COMPLETE FOR M1 FIRST PASS, INCLUDING RECORDED DIRECT NO_RESULT QUERIES + BROADER DISCOVERY.

References:
- IIQC — quality failure→recollection
- carloscs04/uav-vision-pipeline-inspection — logged flagged coordinates→targeted second inspection
- EdwinTSalcedo/RDMO-DigitalTwin — Baseline/Hover/Micro/Skip-revisit recovery policies

Status:
LEARN.

First MP proof:
RECHECK can remain a human-facing source interval/frame/reason without autonomous route execution.

Audit:
audits/recheck-recollection.md

## 10. Whole system

Search status:
COMPLETE FOR M1 FIRST PASS.

Vertical references:
- Hawk-I
- AegisInspect
- dual-UAV pipeline inspection
- RDMO Digital Twin
- tank-inspection-uav

Use:
integration patterns, evidence boundaries, persistence, dedup and reinspection semantics.

Do not import:
ROS/LiDAR/edge/autonomy/3D merely because references contain them.

## Proposed first M2 candidate set

- FFmpeg
- OpenCV
- BRISQUE
- Anomalib/PatchCore
- SAM2.1 Hiera Small
- Weighted Boxes Fusion
- Norfair

Not in first M2 executable set:
- known-defect detector: BLOCKED by checkpoint/license precondition
- VLM: PARK
- CVAT: PARK
- telemetry: PARK
- route generation: PARK
- COLMAP/3D: PARK

See:
M2_SMOKE_TEST_PLAN.md

## Architecture freeze gate

MP Architecture v0.1 remains NOT READY TO FREEZE.

M1 output now identifies candidates and gaps, but no USE/ADAPT/BUILD choice becomes HUMAN_ACCEPTED until independent M1 review and subsequent HUMAN decision.
