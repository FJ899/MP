# M1 Repository Suitability Matrix — Candidate for Review

Status vocabulary:
- SOURCE_INSPECTED
- INSTALL_NOT_RUN / INSTALL_VERIFIED
- SMOKE_TEST_NOT_RUN / PASS / FAIL
- PIPELINE_COMPATIBILITY_NOT_TESTED / VERIFIED

All rows below are SOURCE_INSPECTED unless explicitly stated otherwise.
No runtime row is PASS.

| Problem area | Strongest candidate/reference | Input | Output | Source requirements / compute | Repo/model license state | Adapter | M1 disposition | RECHECK relevance | Critical limitation |
|---|---|---|---|---|---|---|---|---|---|
| Video ingestion | FFmpeg + OpenCV | native video | frames + timestamps + arrays | CPU baseline; HW decode optional | FFmpeg default LGPL-2.1+ config-sensitive; OpenCV Apache-2.0 | THIN | EVALUATE M2 | preserves exact source interval/frame evidence | Air 3S timestamp behavior NOT_TESTED |
| Quality signal | rehanguha/brisque | image | BRISQUE score | CPU; NumPy/SciPy/scikit-image/libsvm/OpenCV + bundled SVM/normalization artifacts | code Apache-2.0; default svm.txt/normalize.pickle provenance+terms UNRESOLVED | THIN | EVALUATE M2 WITH PRECONDITION | can reject obviously poor evidence before analysis | not a complete gate; default model artifacts cannot be treated as cleared until terms/provenance resolved |
| Quality architecture | IIQC | UAV inspection image + pose/bridge context | quality/recollection feedback | ROS/pose/3D/PCL/OctoMap context | project license UNRESOLVED | HIGH direct / NONE reference | LEARN | shows quality failure→recollection pattern | too heavy/unclear license for direct first component |
| Anomaly | Anomalib PatchCore | normal references + test image | anomaly score/map | Python>=3.10; CPU/GPU extras; pretrained backbone | Apache-2.0 code; backbone/model license separate | THIN-MODERATE | EVALUATE M2 | can surface unknown irregularities for RECHECK | needs representative normality; quality artifacts may dominate |
| VLM authority reference | AI-Visual-Inspector | detector verdict/heatmap + image | descriptive explanation | Anomalib + Ollama/Qwen; hardware model-dependent | no LICENSE found | REFERENCE | LEARN / PARK runtime | useful human explanation without VLM overriding detector | source project license unresolved; no need in first smoke |
| Known-defect benchmark | BFD-UAV2K | real UAV facade images | detector benchmark metrics | model-dependent | dataset/license PENDING per README | BENCHMARK | EVALUATE evidence | closest task evidence for detector family | no licensed ready checkpoint selected |
| Detector framework | Ultralytics | image/video + selected weights | boxes/classes/scores | Python/PyTorch; CPU/GPU | AGPL-3.0 code; defect weights/license unresolved | THIN | PARK/BLOCKED | could provide known-defect candidates | generic weights do not prove facade defects |
| Sliced detector mode | SAHI | image + detector | merged sliced predictions | inherits detector + OpenCV | MIT | THIN | PARK until detector exists | may improve small-defect recall | not independent detector |
| Temporal mask propagation | SAM2.1 Small | short video + candidate box/prompt | masks/object IDs across frames | Python>=3.10; torch>=2.5.1; GPU recommended | Apache-2.0 code + checkpoints per README | THIN-MODERATE | EVALUATE M2 | supports persistence of one suspicious region | automatic discovery is not its role |
| VOS alternative | Cutie | frames + initial mask | propagated masks | PyTorch/CUDA-oriented demo | MIT code; weights license not separately established | MODERATE | PARK | alternate persistence mechanism | no reason to test before SAM2 unless gap appears |
| Same-frame fusion | Weighted Boxes Fusion | model boxes/scores/labels | fused boxes/scores/labels | CPU NumPy/Pandas/Numba | MIT | THIN | EVALUATE M2 | reduces duplicate geometry from analyzers | native output does not preserve MP provenance |
| Temporal association | Norfair | detections per frame | track IDs/spans | core CPU; custom distance; moving-camera support | BSD-3-Clause | THIN-MODERATE | EVALUATE M2 | groups repeated observations into candidate spans | static defect + moving camera fit unproven |
| MOT alternative | ByteTrack | detection boxes | MOT tracks | heavier YOLOX/MOT stack; GPU benchmarks | MIT | MODERATE | PARK | possible temporal grouping | benchmark/domain less aligned than Norfair |
| Spatial dedup reference | tank-inspection-uav | mapped x/y/z defects | deduplicated registry | ROS/3D stack | no LICENSE found | REFERENCE | LEARN | proves simple coordinate-radius dedup pattern | coordinates unavailable in first proof |
| Persistence reference | AegisInspect | mapped observations | persistent defect records/reports | ROS/LiDAR/3D stack | no LICENSE found | REFERENCE | LEARN | persistent IDs, aggregation, evidence boundaries | avoid importing autonomy/3D scope |
| Whole-system reference | Hawk-I | camera/detections/GPS | masks/verification/report/dashboard | Jetson + GCS GPU architecture | license UNRESOLVED in inspected source | REFERENCE | LEARN | integration/failure-handling competitor | architecture is much larger than MP first proof |
| Reinspection reference | dual-UAV pipeline inspection | flagged findings + telemetry | target manifest + second inspection | Tello/YOLO/control stack | MIT | REFERENCE | LEARN | CandidateEvent→recheck-task pattern | autonomous flight out of scope |
| Revisit policy reference | RDMO Digital Twin | simulated occlusion/inspection state | coverage/time/energy by recovery policy | Unity + model server | no LICENSE found | BENCHMARK | LEARN | shows Hover/Micro/Skip/revisit trade-offs | simulation/pavement context |
| Annotation | CVAT | image/video task | human labels | service stack | MIT | MODERATE | PARK | useful only if data burden emerges | not needed for first inference smoke |
| Telemetry | existing DJI parsers | MP4/SRT/DAT | timestamps/GPS/altitude/etc. | mostly CPU | candidate-specific; several MIT | THIN-MODERATE | PARK/NON-BLOCKING | later maps CandidateEvent to flight context | actual Air 3S compatibility unknown |
| Route generation | WayPoint / DroneRoute / Air3S format research | mission definition | KMZ/WPML/controller mission | app-specific | WayPoint/DroneRoute MIT; format research terms TO VERIFY | MODERATE | PARK | later could automate RECHECK capture | no route execution authorized; Air 3S verification incomplete |
| 3D | COLMAP | overlapping images | poses/3D reconstruction | CPU/GPU workflow | verify before use | HEAVY | PARK | only if telemetry insufficient | unnecessary for first vision-value proof |

## Cross-cutting findings

### F-001 — PatchCore needs normal-reference data
No named defect class is required, but a useful memory bank of normal imagery is.

### F-002 — SAHI is a detector mode, not a second detector
Compare direct detector vs detector+slicing. Do not double-count it as independent evidence.

### F-003 — SAM2 belongs downstream of candidate generation
Its clean first role is box/prompt→mask propagation.

### F-004 — VLM should not be a default second vote
AI-Visual-Inspector provides a working reference for detector authority + descriptive VLM. MP still needs evidence before any VLM role is accepted.

### F-005 — YOLO is not an architectural decision
BFD-UAV2K reports different strengths for YOLO and RT-DETR. Generic pretrained YOLO does not prove defect capability.

### F-006 — Merger is decomposable but not fully solved
Existing components cover:
- same-frame fusion,
- temporal association,
- prompted mask continuity,
- later spatial dedup.

The MP-specific gap is provenance-preserving CandidateEvent semantics across these observations. BUILD remains unauthorized.

### F-007 — Search-before-build prevented unnecessary custom work
Likely custom work removed or postponed:
- ingestion framework,
- image-quality model,
- mask tracker,
- generic box fusion,
- generic MOT tracker,
- telemetry parser,
- KMZ generator.

### F-008 — Licensing changes component roles
Examples:
- IIQC: useful LEARN reference but direct dependency licensing unclear.
- Hawk-I/AegisInspect: architecture references, not code dependencies.
- BFD-UAV2K: benchmark evidence but data use remains license-pending.
- SAM2: unusually clear code+checkpoint terms among segmentation candidates.

## Execution state

INSTALL_NOT_RUN:
all proposed M2 candidates.

SMOKE_TEST_NOT_RUN:
all proposed M2 candidates.

PIPELINE_COMPATIBILITY_NOT_TESTED:
all proposed M2 candidates.

No statement in this matrix means MP currently works end-to-end.


### F-009 — BRISQUE has separate default model artifacts
At pinned commit 42c854ef9278f09d047abb8600d5204f779eca52, BRISQUE.__init__() loads:
- brisque/models/svm.txt via libsvm svm_load_model,
- brisque/models/normalize.pickle via pickle.load.

The root code license is Apache-2.0.
The provenance and independent terms of the bundled model/normalization artifacts are not established by M1.

Consequence:
M2-02 is conditional on resolving those artifacts or supplying a custom BRISQUE model with pinned acceptable provenance/terms.
