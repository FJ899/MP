# M1 Reconnaissance Evidence

candidate_status:
READY_FOR_INDEPENDENT_REVIEW

snapshot_date:
2026-10-01

execution_boundary:
No proposed M2 component was installed or run by MP during M1.

Evidence statuses used:
- SOURCE_INSPECTED
- UPSTREAM_REPORTED
- MP_NOT_RUN
- UNRESOLVED

## E-M1-001 — PatchCore normal-reference requirement

claim:
PatchCore requires a memory bank built from representative normal training images and compares inference patches to stored features.

source:
open-edge-platform/anomalib

commit:
1f503a6c3614e2637472cdb6d9ca21054c83ac26

file:
src/anomalib/models/image/patchcore/torch_model.py

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
PatchCore may avoid named defect labels but does not avoid the need to define normal reference material.

## E-M1-002 — Anomalib runtime/dependency shape

source:
open-edge-platform/anomalib

commit:
1f503a6c3614e2637472cdb6d9ca21054c83ac26

file:
pyproject.toml

observed:
- Python >=3.10;
- Apache-2.0 code license;
- CPU and accelerator dependency extras;
- model libraries including timm;
- video/VLM extras exist but are optional.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

limitation:
pretrained backbone/model licensing must be checked for the exact selected backbone before M2 execution.

## E-M1-003 — SAHI is sliced inference around a detector

source:
obss/sahi

commit:
80ebdb699851facf87def03c0597e1aeb87a9a2d

files:
README.md
pyproject.toml
LICENSE

observed:
- SAHI provides sliced prediction with underlying detection backends;
- package version 0.12.8 at pinned ref;
- MIT license.

source_status:
SOURCE_INSPECTED

impact:
SAHI is an optional inference mode, not an independent defect detector.

## E-M1-004 — BFD-UAV2K detector benchmark

source:
Real-world-UAV-Structural-Defects/BFD-UAV2K

commit:
18a4a3a1ed3d8eac308e85d7a03de9144123175e

file:
README.md

observed:
- 2,000 real full-frame UAV facade images;
- 1,600/200/200 split;
- 2,664 defect instances;
- DJI Mini 3, 2–30 m inspection geometry;
- benchmark includes YOLO, RT-DETR, Faster R-CNN, Cascade R-CNN;
- reported results show different speed/localization/recall trade-offs;
- license section says license information will be added with official public release.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
YOLO cannot be selected merely by familiarity.
Dataset/checkpoint use is not authorized by M1.

## E-M1-005 — SAM2 prompted video propagation

source:
facebookresearch/sam2

commit:
2b90b9f5ceec907a1c18123530e92e794ad901a4

files:
README.md
LICENSE

observed:
- initialize video state;
- add point/box prompts;
- propagate masks through video;
- Python/PyTorch requirements documented;
- GPU path recommended;
- code and SAM2 model checkpoints described under Apache-2.0.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
SAM2 is suitable for a prompted persistence smoke after candidate generation, not proof of automatic defect detection.

## E-M1-006 — Cutie alternative

source:
hkchengrex/Cutie

commit:
ec5cdd4cf16f75c73ad785a2f96fb97dbad4125a

files:
README.md
LICENSE
pyproject.toml

observed:
- video object segmentation;
- MIT code;
- PyTorch/CUDA-oriented dependencies;
- pretrained models downloaded separately.

model_weight_terms:
UNRESOLVED in inspected material.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
valid alternative, but no reason to test before SAM2 unless SAM2 exposes a gap.

## E-M1-007 — DEVA decoupled temporal fusion

source:
hkchengrex/Tracking-Anything-with-DEVA

commit:
404a112df77f9644d5c7211811329ccd8174b8c3

file:
README.md

observed:
- task-specific image segmentation/detection can be integrated with generic temporal propagation;
- semi-online fusion combines hypotheses across frames;
- source explicitly warns temporal propagation can amplify false positives.

license:
UNRESOLVED at standard path.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
strong architecture reference for keeping candidate generation separate from temporal continuity.

## E-M1-008 — WBF same-frame box fusion

source:
ZFTurbo/Weighted-Boxes-Fusion

commit:
96880f3df8d45ac21dce8d243fcfab420cadda47

files:
README.md
LICENSE
setup.py

observed:
- inputs: box lists, score lists, class labels and optional model weights;
- outputs: fused boxes/scores/labels;
- implements NMS/Soft-NMS/NMW/WBF;
- MIT license;
- package dependencies NumPy/Pandas/Numba.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

limitation:
native fusion result does not by itself encode all MP observation provenance.

## E-M1-009 — Norfair temporal association

source:
tryolabs/norfair

commit:
e517b4236f6b67a6ecf342f5df1fccb7788dbc54

files:
README.md
pyproject.toml

observed:
- detector-agnostic tracking;
- custom distance functions;
- moving-camera support;
- ReID and SAHI examples;
- package metadata version 2.3.0;
- BSD-3-Clause;
- core tracker does not require GPU.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
strong first candidate for temporal association, but static-defect/moving-camera behavior remains an empirical question.

## E-M1-010 — UAV quality metrics already exist

source:
GattuPriyanka/Framework-for-UAV-image-quality

commit:
9344d90ca9f56bf7bd54623b090c794c8c68d3f9

file:
metrics.py

observed code:
- DFT/DCT blur calculations;
- near-white/near-black pixel counts;
- NIQE;
- BRISQUE;
- folder-level aggregation.

license:
no LICENSE found.

source_status:
SOURCE_INSPECTED

impact:
MP does not need to invent the metric family from first principles.

## E-M1-011 — BRISQUE small licensed quality component

source:
rehanguha/brisque

commit:
42c854ef9278f09d047abb8600d5204f779eca52

files:
README.md
LICENSE
setup.py

observed:
- no-reference image quality score;
- image ndarray input;
- Apache-2.0;
- NumPy/SciPy/scikit-image/libsvm dependencies;
- selectable OpenCV package variant.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
clean candidate for one small quality-signal smoke; it is not a complete quality gate.

## E-M1-012 — IIQC quality→recollection architecture

source:
fwan133/IIQC

commit:
b60ddf0aebe8bdafcdbf2e0122d51c63b60462c8

observed:
rapid UAV inspection image-quality/recollection objective plus heavier pose/3D/ROS dependencies.

license evidence:
- no top-level LICENSE found;
- package.xml surfaced with license TODO;
- some inherited source files carry their own GPL/BSD notices.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
LEARN architecture; do not treat as direct dependency until licensing/integration is resolved.

## E-M1-013 — AI-Visual-Inspector detector authority

source:
AliAbdien/AI-Visual-Inspector

commit:
100f7468ca110b9e8bee65a2b4767b8eda198cc4

file:
README.md

observed:
- Anomalib model sets deterministic defect verdict;
- VLM runs afterward to describe detected region;
- contradictory VLM response is discarded;
- upstream author reports real training/end-to-end runs.

license:
no LICENSE found.

source_status:
SOURCE_INSPECTED

upstream_execution:
UPSTREAM_REPORTED

mp_execution:
MP_NOT_RUN

impact:
supports detector-authority/VLM-description pattern without making it an MP dependency.

## E-M1-014 — Spatial dedup exists when coordinates exist

source:
mercwrite/tank-inspection-uav

commit:
9883295959f04a4ae3a0e1061653f23b9a84fb56

file:
src/perception_3d/perception_3d/defect_aggregator.py

observed code:
- registry stores defect type, x/y/z and source;
- new detections are suppressed when Euclidean distance to existing record is below configurable radius (0.5 m default).

license:
no LICENSE found.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
spatial dedup is a solved thin mechanism after coordinates exist; it is not a first-proof dependency.

## E-M1-015 — Targeted reinspection precedent

source:
carloscs04/uav-vision-pipeline-inspection

commit:
5d4389b19c4dd237e456842d80b969135fcfe74d

files:
README.md
LICENSE

observed:
primary UAV logs flagged inspection outcomes/telemetry; secondary UAV consumes flagged coordinates for targeted reinspection.

license:
MIT

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
RECHECK can be represented as a durable target/evidence handoff without MP inventing the concept.

## E-M1-016 — Revisit policy trade-offs

source:
EdwinTSalcedo/RDMO-DigitalTwin

commit:
1152268834a4a1bac541867d4be463677c827e6f

file:
README.md

observed:
Baseline/Hover/Micro/Skip recovery strategies with reported coverage/time/energy trade-offs.

license:
no LICENSE found.

source_status:
SOURCE_INSPECTED

mp_execution:
MP_NOT_RUN

impact:
later RECHECK policy should be evaluated as a trade-off, not assumed to have one universal maneuver.

## E-M1-017 — Hawk-I architecture reference licensing correction

source:
Arvoxis/hawk-i

commit:
0af5ec508631544596dd1ab6926fd2337c34452c

observed:
integrated detector→SAM2→verification→LLM/report/GPS architecture.

license:
UNRESOLVED in inspected repository root/README.
No top-level LICENSE file was found.

source_status:
SOURCE_INSPECTED

impact:
Hawk-I remains LEARN reference, not a code dependency.
This supersedes the earlier preliminary Radar statement that suggested MIT.

## E-M1-018 — M1 execution boundary

claim:
M1 is reconnaissance/audit, not component execution.

actual MP status for proposed M2 set:
- INSTALL_NOT_RUN
- SMOKE_TEST_NOT_RUN
- PIPELINE_COMPATIBILITY_NOT_TESTED

evidence:
AUDIT_MATRIX.md
M1_RESULT.md
M2_SMOKE_TEST_PLAN.md

interpretation:
No source claim or upstream benchmark is presented as proof that MP works.
