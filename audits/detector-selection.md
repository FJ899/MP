# M1 Audit — Known-Defect Detector Selection

execution_status: BLOCKED_FOR_MEANINGFUL_SMOKE
reason: exact task-relevant weights/data license not yet resolved

## Problem

MP should not select YOLO merely because the framework is familiar.
The detector must show evidence on a problem close to UAV facade inspection.

## BFD-UAV2K benchmark

repository: Real-world-UAV-Structural-Defects/BFD-UAV2K
pinned_commit: 18a4a3a1ed3d8eac308e85d7a03de9144123175e

Source facts from inspected README:
- 2,000 full-frame real UAV facade images;
- 1,600 / 200 / 200 split;
- 912 positive and 1,088 negative images;
- 2,664 defect boxes;
- single class defect covering cracking, spalling and hollow-drum-like facade damage;
- DJI Mini 3, 2–30 m wall-facing capture geometry.

Reported benchmark compares:
- YOLOv5mu,
- YOLOv8m,
- YOLOv11m,
- RT-DETR-L,
- Faster R-CNN,
- Cascade R-CNN.

Reported results show trade-offs:
- YOLOv5mu: strongest reported mAP@0.5 and fastest listed inference;
- RT-DETR-L: strongest reported mAP@0.5:0.95, recall and F1;
- no single family dominates every objective.

Critical availability/licensing facts:
- README says license information will be added with the official public release;
- inspected GitHub root currently contains README/assets, while data/scripts/checkpoints are described as expected/public dataset material elsewhere.

MP disposition:
BENCHMARK + EVALUATE, not runtime dependency.

## Ultralytics framework

repository: ultralytics/ultralytics
pinned_commit: 9b790cf26ffce6809723873a2547160085329b92
code_license: AGPL-3.0

Source facts:
framework supports detection, segmentation and tracking and generic pretrained model families.

Critical limitation:
generic COCO/standard weights do not establish facade crack/spalling capability.

Exact defect weights:
UNRESOLVED.

Weights license:
UNRESOLVED.

MP disposition:
candidate framework only.
No architecture decision.

## SAHI

repository: obss/sahi
pinned_commit: 80ebdb699851facf87def03c0597e1aeb87a9a2d
license: MIT
package version: 0.12.8

Role:
sliced-inference wrapper around an underlying detector.

MP disposition:
EVALUATE only as direct-vs-sliced mode after a real detector/weights choice exists.

## Other benchmarks

FBD:
useful facade-classification evidence, but classification crops are not the same task as full-frame UAV detection.

InsPLAD:
useful real-UAV inspection/anomaly benchmark in a different infrastructure domain.

UAV crack dataset:
useful secondary crack segmentation/detection reference.

None is treated as direct proof that a chosen detector will work on MP footage.

## M1 proposed disposition

Do NOT include a known-defect detector in the first executable M2 sequence until at least one of these is true:
1. a task-relevant pretrained checkpoint with acceptable license is identified, or
2. a licensed benchmark/dataset supports a deliberately authorized tiny training experiment.

This does not block:
- ingestion,
- quality,
- PatchCore,
- SAM2 prompt propagation,
- synthetic merger/tracking smoke tests.

REPLACES WHAT?:
premature choice of YOLO as the detector.

## M2 status

Known-defect detector smoke:
BLOCKED / PRECONDITION REQUIRED.
