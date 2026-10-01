# M1 Repository Suitability Matrix

Status meanings:
- SOURCE_INSPECTED
- INSTALL_NOT_RUN / INSTALL_VERIFIED
- SMOKE_TEST_NOT_RUN / SMOKE_TEST_PASS / FAIL
- PIPELINE_COMPATIBILITY_NOT_TESTED / VERIFIED

| Component | Actual role | Input | Output | Compute | Adapter | Critical limitation | Current recommendation |
|---|---|---|---|---|---|---|---|
| Anomalib / PatchCore | anomaly detection against learned normal reference | image(s) + normal-reference memory bank | anomaly score/map | GPU useful; exact target TBD | THIN-MODERATE | needs representative normal training/reference images | KEEP FOR AUDIT |
| Ultralytics YOLO | detector framework; usefulness depends on selected weights/model | image/video | boxes/classes/confidence, model-dependent | CPU/GPU model-dependent | THIN | vanilla framework does not prove crack/spalling/corrosion capability | KEEP FOR AUDIT |
| SAHI | sliced inference wrapper around detector | image + detector | merged detections from slices | inherits detector requirements | THIN | not an independent semantic detector | KEEP AS MODE, NOT PARALLEL DETECTOR |
| SAM2 | promptable segmentation and video propagation; also image mask generation | frame/video + prompt/box for tracked object path | masks / propagated masklets | GPU recommended for useful speed | THIN-MODERATE | video tracking path needs initial prompt/region | KEEP DOWNSTREAM OF CANDIDATE |
| CVAT | annotation/review tooling | images/video/tasks | human annotations | service/tooling | MODERATE if automated | not part of first inference path | OPTIONAL / LATER |
| Ollama + Gemma 3 | local model runtime + model interpretation | image/text depending on model/runtime path | text/structured response | model/hardware dependent | THIN-MODERATE | may add narrative without improving RECHECK quality | OPTIONAL EXPERIMENT |
| COLMAP | SfM / poses / reconstruction | overlapping images | camera poses / 3D reconstruction | CPU/GPU workflow-dependent | HEAVY relative to M1 goal | unnecessary until timestamp->telemetry proves insufficient | LATER |
| Hawk-I | reference implementation integrating related components | mixed | mixed | mixed | REFERENCE ONLY | similarity can bias us toward oversized architecture | REFERENCE |
| DJI telemetry | unresolved parser/component | flight log | telemetry | TBD | TBD | exact source/log compatibility unresolved | UNRESOLVED |

## Preliminary source-backed findings

### F-001 — PatchCore reference data
PatchCore is not "zero preparation anomaly detection". The inspected Anomalib implementation describes a training phase that stores patch features from normal training images in a memory bank, then compares inference images against that bank.

Consequence: anomaly detection may still avoid defect-class labeling, but it requires a useful definition of normality.

### F-002 — SAHI role
SAHI documentation shows an AutoDetectionModel plus get_sliced_prediction and uses Ultralytics as a backend example.

Consequence: model the path as YOLO direct vs YOLO+SAHI sliced inference, not YOLO and SAHI as two independent detectors.

### F-003 — SAM2 role
SAM2 video workflow is promptable: initialize video state, add point/box prompts, then propagate masks through video. Automatic mask generation also exists for images.

Consequence: first candidate architecture should test SAM2 mainly after another mechanism identifies a region/event.

### F-004 — Hawk-I role
Hawk-I documents an inspection stack combining YOLO, YOLO-World, SAM2.1, DINOv2, Gemma 3/Ollama, GPS/MAVLink and reporting.

Consequence: use it to inspect integration patterns and failure modes, not as the target architecture by default.

## Not yet verified
- exact licenses for every repository and every model weight
- exact current commit/tag to freeze for M1
- installation success
- inference success
- compatibility on our flight footage
- detector weights/classes for crack/spalling/corrosion
- Gemma 3 exact model artifact
- DJI flight-log parser identity
