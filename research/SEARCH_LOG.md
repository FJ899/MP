# M1 Search Log

Date: 2026-10-01

Purpose: durable evidence that major MP problem areas received targeted reconnaissance before architecture work. Search results are discovery evidence only; all serious candidates are subsequently inspected and pinned in `research/PINNED_SOURCES.md`.

## Search classes

VERTICAL:
near-end-to-end systems solving a problem close to MP.

HORIZONTAL:
implementations solving the exact current component.

## Whole-system / vertical

Queries included:
- drone inspection infrastructure
- UAV inspection
- UAV infrastructure inspection AI drone defect detection
- semi autonomous UAV inspection
- drone repeat inspection defect tracking
- site:github.com UAV reinspection recollection defect revisit waypoint drone inspection

Serious candidates retained:
- Arvoxis/hawk-i
- AritraAcherjee/autonomous-drone-infrastructure-inspection
- carloscs04/uav-vision-pipeline-inspection
- EdwinTSalcedo/RDMO-DigitalTwin
- mercwrite/tank-inspection-uav

Disposition:
LEARN / REFERENCE_IMPLEMENTATION or BENCHMARK. None is promoted to target architecture.

## Video ingestion

Horizontal queries:
- video frame extraction scene detection python
- video ingestion ffmpeg opencv pipeline

Candidates inspected:
- FFmpeg/FFmpeg
- opencv/opencv
- Breakthrough/PySceneDetect
- PyAV-Org/PyAV
- abhiTronix/vidgear

Result:
Existing mature tools already cover decode/frame access. No reason to design a custom ingestion framework in M1.
PySceneDetect solves cut/scene detection rather than defect/recheck semantics.
PyAV itself advises that direct ffmpeg is preferable when the command line already solves the job.

Proposed M2 evaluation:
FFmpeg + OpenCV baseline.

## Quality gate

Horizontal queries:
- image quality UAV
- UAV image quality inspection blur exposure recollection
- UAV image quality check
- no reference image quality BRISQUE Python

Candidates inspected:
- fwan133/IIQC
- GattuPriyanka/Framework-for-UAV-image-quality
- rehanguha/brisque

Result:
IIQC is the closest architecture reference for quality→recollection, but is heavy and has unresolved project licensing.
Framework-for-UAV-image-quality exposes concrete blur/exposure/NIQE/BRISQUE mechanisms but has no LICENSE file.
rehanguha/brisque is a small Apache-2.0 no-reference quality-score component and is a cleaner smoke-test candidate.

No final operational quality threshold is selected.

## Anomaly / interpretation

Horizontal queries and source inspection centered on:
- video anomaly detection inspection
- Anomalib PatchCore normal image memory bank
- anomaly detector VLM explanation

Candidates:
- open-edge-platform/anomalib
- AliAbdien/AI-Visual-Inspector

Result:
PatchCore remains a candidate for anomaly ranking but needs representative normal-reference material.
AI-Visual-Inspector is retained as a reference for the authority split:
detector decides; VLM explains.

VLM is not promoted to a second defect vote.

## Defect detector / benchmark

Horizontal queries:
- facade defect detection
- UAV facade defect detection benchmark
- UAV crack detection segmentation

Candidates/benchmarks:
- Real-world-UAV-Structural-Defects/BFD-UAV2K
- ultralytics/ultralytics
- Malga-Vision/FBD-Dataset
- andreluizbvs/InsPLAD
- KangchengLiu/Crack-Detection-and-Segmentation-Dataset-for-UAV-Inspection

Result:
BFD-UAV2K is the closest task benchmark found and demonstrates meaningful trade-offs between YOLO-family and RT-DETR/two-stage models.
However its README says license information is pending and its GitHub repository does not currently contain the dataset/scripts/checkpoints described as expected future contents.

Therefore an exact defect detector is NOT selected in M1.
Generic COCO YOLO weights are not accepted as evidence of facade-defect capability.

## Segmentation / tracking

Horizontal queries:
- video object segmentation Cutie
- video object segmentation XMem
- open world video segmentation DEVA
- point tracking CoTracker
- Track Anything video segmentation

Candidates inspected:
- facebookresearch/sam2
- hkchengrex/Cutie
- hkchengrex/XMem
- hkchengrex/Tracking-Anything-with-DEVA
- gaomingqi/Track-Anything
- facebookresearch/co-tracker (discovery only; lower fit to mask/region requirement)

Result:
SAM2 has the cleanest first-smoke interface and licensing evidence for MP:
candidate box/prompt → propagated masks through video; code and checkpoints described as Apache-2.0.
Cutie/XMem are valid VOS alternatives but their inspected source did not separately establish pretrained-weight licensing.
DEVA is highly relevant to detector→temporal fusion but has more dependency/license complexity.

Proposed M2 evaluation:
SAM2.1 Hiera Small on one short clip and one known candidate box.

## Same-frame fusion / temporal merger

Horizontal queries:
- weighted boxes fusion
- multi model detection fusion
- multi object tracking Norfair
- ByteTrack
- detection fusion temporal clustering
- defect aggregation
- spatial defect deduplication

Candidates inspected:
- ZFTurbo/Weighted-Boxes-Fusion
- tryolabs/norfair
- FoundationVision/ByteTrack
- mercwrite/tank-inspection-uav
- AegisInspect patterns
- DEVA patterns

Search result:
No single inspected repository directly implements MP's complete problem:
multiple analysis observations of a mostly static surface defect, seen across frames from a moving UAV camera, merged into a provenance-preserving CandidateEvent.

Useful solved subproblems:
- WBF/NMS: same-frame multi-detector box fusion.
- Norfair: detector-agnostic temporal association, moving-camera support and custom distance functions.
- SAM2/DEVA: mask/region temporal continuity.
- tank-inspection-uav/AegisInspect: spatial/persistent defect dedup when mapped coordinates are available.

This leaves an MP-specific integration gap, but no BUILD is authorized in M1.

## Telemetry

Horizontal queries:
- DJI telemetry parser
- DJI flight log parser
- DJI SRT telemetry
- DJI MP4 subtitle telemetry

Candidates:
- FergusInLondon/dji_parse
- jetervaz/dji-telemetry
- AiryAir/dji-srt2csv
- aero-oli/DatCon

Result:
Candidate set exists.
The unresolved question is actual Air 3S file/log compatibility, not lack of parsers.

Status:
PARK / non-blocking until vision produces useful candidate events.

## Route generation

Horizontal queries:
- DJI waypoint KMZ
- DJI Air 3S WPML KMZ waypoint

Candidates:
- BanaanKiamanesh/WayPoint
- fcsonline/droneroute
- jamiepinkham/drone-mission-planning

Result:
Custom KMZ generation is not justified before testing these existing solutions.
Route generation remains outside the first post-flight vision proof.

## Recheck / recollection

GitHub repository search queries:
- UAV reinspection recollection inspection waypoint defect
- drone reinspection defect revisit waypoint
- UAV image recollection inspection quality
- drone repeat inspection defect tracking

Direct repository search result:
NO_RESULT for these exact broad formulations.

Broader external discovery followed by GitHub source verification found:
- carloscs04/uav-vision-pipeline-inspection
- EdwinTSalcedo/RDMO-DigitalTwin
- IIQC as an upstream quality/recollection reference

Mechanisms learned:
- flagged defect coordinates can become a second targeted inspection task,
- revisit/skip/hover/local reposition can be compared as recovery policies,
- quality failure can trigger recollection independently of defect detection.

Status:
LEARN only. No autonomous revisit implementation is authorized.

## Search limitation

This reconnaissance is targeted, not an exhaustive survey of all GitHub, papers, or commercial products.
A NO_RESULT entry means the recorded query did not return a useful repository; it never means no solution exists anywhere.

M1 uses stopping by decision value:
once multiple credible alternatives expose the relevant design trade-off, more repository collection is not automatically useful.
