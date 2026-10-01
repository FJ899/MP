# SOURCES

This is the M1 source index.

Canonical exact branch/commit identities:
research/PINNED_SOURCES.md

Search provenance:
research/SEARCH_LOG.md

Candidate decision radar:
research/REPO_RADAR.md

Functional audits:
audits/

## Current source classes

### First M2 evaluation candidates

- FFmpeg/FFmpeg — video decode/timestamps
- opencv/opencv — frame/image operations
- rehanguha/brisque — one no-reference quality signal
- open-edge-platform/anomalib — PatchCore anomaly path
- facebookresearch/sam2 — prompted mask propagation
- ZFTurbo/Weighted-Boxes-Fusion — same-frame box fusion
- tryolabs/norfair — temporal association

These are PROPOSED_FOR_M2, not accepted dependencies.

### Benchmarks / decision evidence

- Real-world-UAV-Structural-Defects/BFD-UAV2K
- Malga-Vision/FBD-Dataset
- andreluizbvs/InsPLAD
- KangchengLiu/Crack-Detection-and-Segmentation-Dataset-for-UAV-Inspection

### Architecture/reference implementations

- fwan133/IIQC
- AliAbdien/AI-Visual-Inspector
- Arvoxis/hawk-i
- AritraAcherjee/autonomous-drone-infrastructure-inspection
- hkchengrex/Tracking-Anything-with-DEVA
- mercwrite/tank-inspection-uav
- carloscs04/uav-vision-pipeline-inspection
- EdwinTSalcedo/RDMO-DigitalTwin

### Later/non-blocking candidates

Telemetry:
- FergusInLondon/dji_parse
- jetervaz/dji-telemetry
- AiryAir/dji-srt2csv
- aero-oli/DatCon

Route:
- BanaanKiamanesh/WayPoint
- fcsonline/droneroute
- jamiepinkham/drone-mission-planning

Other:
- cvat-ai/cvat
- ollama/ollama
- colmap/colmap

## Unresolved identities/terms that matter

- exact task-relevant known-defect checkpoint/weights: UNRESOLVED
- BFD-UAV2K use license: PENDING per source README
- exact Gemma/VLM model artifact and model license: UNRESOLVED and PARKED
- actual Air 3S telemetry/log compatibility: UNRESOLVED
- some reference repositories have no clear top-level license; they remain references, not dependencies

## Rules

- Repository identity is not runtime proof.
- Every source-derived claim used for execution should bind to a pinned commit.
- Code license, dataset license and model/checkpoint license are separate.
- A README claim is SOURCE_INSPECTED evidence, not INSTALL_VERIFIED or SMOKE_TEST_PASS.
- Search discovery does not promote a repository into build scope.
