# COMPONENT CANDIDATES

This file maps MP problem areas to existing solutions before custom design.

## 1. Video ingestion
Current candidates:
- FFmpeg
- OpenCV

Recon status:
HORIZONTAL SEARCH NOT YET COMPLETE.
Do not design a custom ingestion framework before checking mature video->frames/events pipelines.

## 2. Quality gate
Candidates:
- fwan133/IIQC — LEARN
- GattuPriyanka/Framework-for-UAV-image-quality — EVALUATE

Open question:
What is the minimum quality gate needed for MP's first post-flight experiment versus IIQC's much richer bridge/pose framework?

## 3. Anomaly path
Candidates:
- open-edge-platform/anomalib / PatchCore
- AliAbdien/AI-Visual-Inspector
- InsPLAD as UAV anomaly benchmark/reference

Working hypothesis:
anomaly detector decides anomaly/no-anomaly;
VLM explains/localizes/labels in natural language but does not vote on existence of defect unless evidence later supports that role.

## 4. Defect detector
Candidates/benchmarks:
- BFD-UAV2K
- YOLO family
- RT-DETR
- Faster R-CNN / Cascade R-CNN as benchmark baselines
- FBD classification ensemble — different task, reference only
- UAV crack detection/segmentation benchmark

Important:
YOLO is not frozen. BFD-UAV2K reports materially different trade-offs between YOLO and RT-DETR on a problem much closer to MP than generic benchmarks.

## 5. Segmentation / tracking
Current candidate:
- facebookresearch/sam2

HORIZONTAL SEARCH:
INCOMPLETE.
Need alternatives before freezing SAM2.

## 6. Merger / temporal event clustering
Reference mechanisms:
- Hawk-I per-class NMS / verification flow
- AegisInspect persistent defect aggregation and repeated-observation association

HORIZONTAL SEARCH:
INCOMPLETE.
Need dedicated multi-model/temporal fusion search before custom merger design.

## 7. Telemetry
Candidates:
- FergusInLondon/dji_parse — MP4 subtitle telemetry
- jetervaz/dji-telemetry — SRT telemetry + time lookup
- AiryAir/dji-srt2csv — simple multi-format SRT conversion
- aero-oli/DatCon — richer .DAT path but compatibility risk on newer/encrypted logs

Key experiment before any custom parser:
Does an actual Air 3S recording/log produced in our workflow contain compatible SRT/subtitle telemetry with the fields MP needs?

## 8. Route generation / recheck mission
Candidates:
- BanaanKiamanesh/WayPoint
- fcsonline/droneroute
- jamiepinkham/drone-mission-planning

Current facts:
- WayPoint README explicitly lists Air 3S support.
- DroneRoute supports WPML/KMZ and controller upload, but its current README supported-drone list does not include Air 3S.
- drone-mission-planning contains Air 3S-specific file-format research but explicitly awaits calibration/validation with a real Air 3S dummy mission.

Therefore:
custom KMZ generator is not justified before testing/inspecting these candidates.

## 9. Recheck / recollection
Relevant references:
- IIQC for image recollection trigger
- route-generation candidates above

Dedicated search:
INCOMPLETE.

## 10. Whole system
Vertical references:
- Arvoxis/hawk-i
- AritraAcherjee/autonomous-drone-infrastructure-inspection

Purpose:
identify already-solved integration, provenance, aggregation and human-review mechanisms; do not clone their entire scope.

## Architecture freeze gate
MP Architecture v0.1 remains NOT READY TO FREEZE until:
- each section above has a recorded reconnaissance result,
- strongest candidates have source-level suitability findings,
- custom BUILD items identify the gap that existing solutions did not close.
