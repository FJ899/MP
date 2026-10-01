# REPO RADAR — M1 Candidate Set

Snapshot: 2026-10-01

Purpose:
prevent MP from rebuilding solved problems before inspecting existing implementations.

Source facts and MP assessments are separate.
No row below is HUMAN_ACCEPTED as an architecture choice.

Detailed exact commit identities:
see research/PINNED_SOURCES.md.

Detailed search evidence:
see research/SEARCH_LOG.md.

## Serious candidates and references

| Name | URL / pinned commit | Search type | Problem solved | Input | Output | License | Last active | Tests / evidence | Documentation | GPU / CPU | Maturity | Integration cost | What MP can learn | Replaces what? | Integration role | Decision | Why |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FFmpeg | https://github.com/FFmpeg/FFmpeg / 0eb6a369 | HORIZONTAL | media decode/extraction | video | frames/clips/timebase data | LGPL-2.1+ default; config-sensitive | 2026-10-01 | mature upstream project; MP NOT_RUN | extensive | CPU baseline; HW decode optional | mature | LOW | use proven decode/timebase | custom ingestion engine | DEPENDENCY candidate | EVALUATE | smallest path for deterministic post-flight extraction |
| OpenCV | https://github.com/opencv/opencv / 237b3c2e | HORIZONTAL | frame/image operations | video/frame | arrays/transforms | Apache-2.0 | 2026-10-01 | mature upstream; MP NOT_RUN | extensive | CPU; GPU optional modules | mature | LOW | simple frame/crop operations | custom CV utility layer | DEPENDENCY candidate | EVALUATE | already matches thin post-decode needs |
| PySceneDetect | https://github.com/Breakthrough/PySceneDetect / 81c414cb | HORIZONTAL | cut/scene detection | video | scene intervals/images | BSD-3-Clause | 2026-09-21 | upstream tests/benchmarks; MP NOT_RUN | strong CLI/API docs | CPU/OpenCV | production/stable per package metadata | LOW | scene-change handling | custom scene detector | REFERENCE | PARK | scene cuts are not defect/recheck events |
| IIQC | https://github.com/fwan133/IIQC / b60ddf0a | HORIZONTAL | UAV inspection quality + recollection | images + bridge/pose context | quality/recollection feedback | UNRESOLVED; package.xml license TODO, mixed notices | 2023-11-15 | README reports validation; MP NOT_RUN | research README | CPU/3D/ROS stack dependent | research prototype | HIGH direct / LOW reference | quality→recollection architecture | custom quality architecture | REFERENCE_IMPLEMENTATION | LEARN | closest problem, but too heavy/unclear license for direct component |
| BRISQUE | https://github.com/rehanguha/brisque / 42c854ef | HORIZONTAL | no-reference image quality score | image ndarray | numeric score | code Apache-2.0; bundled SVM + normalization artifact provenance/terms UNRESOLVED | 2026-02-22 | examples/tests in package; MP NOT_RUN | good README + custom-model API | CPU | packaged library | LOW | whether generic IQA helps reject bad frames | custom IQA model | COMPONENT candidate | EVALUATE | small quality signal, but default model artifacts require provenance/terms resolution before M2 execution |
| Anomalib PatchCore | https://github.com/open-edge-platform/anomalib / 1f503a6c | HORIZONTAL | anomaly detection from normal reference | normal refs + test image | anomaly score/map | Apache-2.0 code; backbone weights separate | 2026-10-01 | production/stable metadata; MP NOT_RUN | extensive | CPU and accelerator extras available | mature library | MEDIUM | anomaly ranking without defect classes | bespoke anomaly detector | COMPONENT candidate | EVALUATE | directly tests unknown-irregularity branch |
| AI-Visual-Inspector | https://github.com/AliAbdien/AI-Visual-Inspector / 100f7468 | HORIZONTAL | deterministic anomaly verdict + constrained VLM explanation | image | verdict/heatmap + text | no LICENSE found | 2026-09-11 | README reports real runs and tests; MP NOT_RUN | strong project README/setup | PatchCore CPU possible; EfficientAd GPU; Ollama model dependent | working prototype | LOW as reference | detector authority vs VLM description | ad-hoc anomaly/VLM arbitration | REFERENCE_IMPLEMENTATION | LEARN | useful mechanism, license blocks direct reuse assumption |
| BFD-UAV2K | https://github.com/Real-world-UAV-Structural-Defects/BFD-UAV2K / 18a4a3a1 | HORIZONTAL / BENCHMARK | real UAV facade defect benchmark | 2,000 facade images | detector metrics/failure patterns | PENDING per README | 2026-06-10 | reported benchmark only; MP NOT_RUN | detailed README | model-dependent | benchmark release | LOW as reference | detector-family trade-offs on close task | familiarity-based detector choice | BENCHMARK | EVALUATE | closest task evidence, but use rights/checkpoints unresolved |
| SAM2 | https://github.com/facebookresearch/sam2 / 2b90b9f5 | HORIZONTAL | prompted image/video segmentation | video + point/box prompt | masks/object IDs over frames | Apache-2.0 code + checkpoints per README | 2024-12-16 | published benchmarks; MP NOT_RUN | strong README/notebooks | GPU recommended; Python>=3.10, torch>=2.5.1 | mature research release | MEDIUM | candidate-region persistence | custom video mask tracker | COMPONENT candidate | EVALUATE | clean interface/license for first propagation smoke |
| Cutie | https://github.com/hkchengrex/Cutie / ec5cdd4c | HORIZONTAL | video object segmentation | frame sequence + initial mask | propagated masks | MIT code; weights terms not separately established | 2024-11-08 | research evaluation; MP NOT_RUN | README/scripts | CUDA-oriented demo; PyTorch | mature research code | MEDIUM | alternative VOS behavior | custom VOS | COMPONENT alternative | PARK | useful fallback if SAM2 fails; weight terms need clarity |
| DEVA | https://github.com/hkchengrex/Tracking-Anything-with-DEVA / 404a112d | HORIZONTAL | image-model + generic temporal propagation/fusion | image detections/segments + video | coherent temporal segmentation | no LICENSE found | pinned snapshot | research paper/demo; MP NOT_RUN | strong README | GPU/PyTorch; optional Gurobi path | research framework | HIGH direct / LOW reference | detector→temporal propagation architecture and false-positive risks | custom temporal fusion concept | REFERENCE_IMPLEMENTATION | LEARN | very relevant mechanism but dependency/license complexity |
| Weighted Boxes Fusion | https://github.com/ZFTurbo/Weighted-Boxes-Fusion / 96880f3d | HORIZONTAL | same-frame detector ensemble | boxes/scores/labels from models | fused boxes/scores/labels | MIT | 2026-07-27 | pytest suite documented; MP NOT_RUN | concise README/examples | CPU; NumPy/Numba | stable small package | LOW | geometry fusion vs provenance needs | custom NMS/WBF code | COMPONENT candidate | EVALUATE | solves same-frame overlap cheaply |
| Norfair | https://github.com/tryolabs/norfair / e517b423 | HORIZONTAL | detector-agnostic temporal association | detections per frame | track IDs/trajectories | BSD-3-Clause | 2025-04-30 | CI/demos/benchmarks; MP NOT_RUN | extensive | core CPU; detector may need GPU | production/stable package metadata | LOW-MEDIUM | moving-camera association/custom distance | custom generic tracker | COMPONENT candidate | EVALUATE | best fit among inspected generic trackers for unusual moving-camera case |
| tank-inspection-uav | https://github.com/mercwrite/tank-inspection-uav / 98832959 | VERTICAL/HORIZONTAL reference | spatial defect dedup in mapped coordinates | visual/geometric 3D defect observations | deduplicated defect registry | no LICENSE found | 2026-06-12 | code inspected; MP NOT_RUN | detailed README | ROS/PX4/GPU stack | prototype | LOW as reference / HIGH direct | simple coordinate-radius dedup | custom later spatial dedup | REFERENCE_IMPLEMENTATION | LEARN | actual aggregator source shows concise solved mechanism once coordinates exist |
| Hawk-I | https://github.com/Arvoxis/hawk-i / 0af5ec50 | VERTICAL | integrated drone inspection stack | camera/detections/GPS | masks/verification/report/dashboard | UNRESOLVED; no LICENSE file/text found in inspected root/README | 2026-09-30 | README/tests documented; MP NOT_RUN | detailed | Jetson/GCS GPU architecture | integrated prototype | LOW reference / HIGH direct | detector→segmentation→verification→report boundaries | inventing full integration pattern | REFERENCE_IMPLEMENTATION | LEARN | architecture competitor, not target |
| AegisInspect | https://github.com/AritraAcherjee/autonomous-drone-infrastructure-inspection / 816a2861 | VERTICAL | inspection persistence/mapping/evidence | detections/sensors | persistent mapped findings/reports | no LICENSE found | 2026-09-30 | measured/demonstrated/pending evidence labels | detailed | ROS/Gazebo/LiDAR stack | mature capstone prototype | LOW reference / HIGH direct | persistent IDs, repeated observations, provenance, review state | custom evidence/persistence concepts | REFERENCE_IMPLEMENTATION | LEARN | unusually disciplined evidence boundary |
| Dual-UAV pipeline inspection | https://github.com/carloscs04/uav-vision-pipeline-inspection / 5d4389b1 | VERTICAL | defect logging → targeted second inspection | primary detections + telemetry | target manifest + second UAV revisit | MIT | 2026-08-31 | real project code/docs; MP NOT_RUN | good README | Tello/FFmpeg/YOLO stack | project prototype | LOW reference / HIGH direct | CandidateEvent→reinspection handoff | inventing revisit semantics | REFERENCE_IMPLEMENTATION | LEARN | validates durable flagged-location→recheck pattern |
| RDMO Digital Twin | https://github.com/EdwinTSalcedo/RDMO-DigitalTwin / 11522688 | VERTICAL | compare inspection recovery policies | simulated inspection state | recovery coverage/time/energy | no LICENSE found | 2026-09-03 | recorded experiment tables/videos | extensive | Unity + optional NVIDIA GPU | research framework | LOW reference / HIGH direct | hover/micro/skip revisit trade-offs | assuming one universal RECHECK action | BENCHMARK / REFERENCE | LEARN | useful future policy evidence, outside first post-flight proof |

## Secondary / parked candidates

| Candidate | Pinned identity | Disposition | Reason |
|---|---|---|---|
| PyAV | PyAV-Org/PyAV@b618b2d9 | PARK | direct FFmpeg likely simpler until packet-level access is needed |
| VidGear | abhiTronix/vidgear@549de2b1 | PARK | broader streaming framework than first file-ingestion need |
| Framework-for-UAV-image-quality | GattuPriyanka/...@9344d90c | LEARN/PARK | concrete blur/exposure/NIQE/BRISQUE metrics but no LICENSE found |
| XMem | hkchengrex/XMem@f3b841d5 | LEARN/PARK | predecessor to Cutie; useful long-video reference |
| Track-Anything | gaomingqi/Track-Anything@5e410c60 | PARK | interactive user-click flow not first MP automation path |
| ByteTrack | FoundationVision/ByteTrack@d1bf0191 | PARK | strong MOT but less flexible fit than Norfair for static defect/moving camera case |
| SAHI | obss/sahi@80ebdb69 | EVALUATE LATER | mode for an accepted detector, not independent detector |
| Ultralytics | ultralytics/ultralytics@9b790cf2 | PARK pending weights | AGPL-3.0 framework; generic weights do not prove defect capability |
| FBD / InsPLAD / UAV crack datasets | see PINNED_SOURCES | LEARN/PARK | secondary benchmarks; different task/domain or licensing not yet sufficient |
| CVAT | cvat-ai/cvat@cde80590 | PARK | annotation infrastructure only if smoke tests create real labeling burden |
| Ollama/Gemma | ollama/ollama@3b1999d1 + model unresolved | PARK | interpretation after candidate value; model license separate |
| Telemetry parsers | see PINNED_SOURCES | PARK | candidate set exists; actual Air 3S file compatibility is later question |
| WayPoint / DroneRoute / Air3S format research | see PINNED_SOURCES | PARK | route/recheck automation is later and custom generator is not justified |
| COLMAP | colmap/colmap@25ff12a8 | PARK | geometry is not needed for first vision-value proof |

## Radar conclusion

The reconnaissance does not support a nine-component custom build.

The strongest M2 questions can be tested with existing components:
- FFmpeg/OpenCV — ingestion,
- BRISQUE — one quality signal,
- Anomalib/PatchCore — anomaly branch,
- SAM2 — prompted temporal mask persistence,
- WBF — same-frame geometric fusion,
- Norfair — temporal association.

Known-defect detector:
BLOCKED/PARK until task-relevant weights/data licensing is resolved.

Potential genuinely MP-specific gap:
provenance-preserving CandidateEvent construction across observations/tracks.
This is a discovered gap, not authorization to implement it.

## Rule

No candidate becomes a dependency or architecture choice from source similarity alone.
EVALUATE means: include in the cheapest discriminating smoke test after authorization.
