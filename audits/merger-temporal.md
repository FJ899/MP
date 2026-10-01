# M1 Audit — Merger, Deduplication and Temporal Event Construction

execution_status: NOT_RUN
pipeline_compatibility: NOT_TESTED

## Problem

MP must avoid turning many frame-level observations into many duplicate findings.
The desired result is a smaller CandidateEvent with:
- source interval,
- supporting observations,
- provenance,
- spatial/temporal continuity evidence,
- human RECHECK action.

No single inspected repository was found that directly implements this full problem for static surface defects observed by a moving UAV camera.

## Weighted Boxes Fusion

repository: ZFTurbo/Weighted-Boxes-Fusion
pinned_commit: 96880f3df8d45ac21dce8d243fcfab420cadda47
license: MIT
package: ensemble_boxes 1.0.9

Input:
per-model normalized bounding boxes + scores + class labels + optional weights.

Output:
fused boxes, scores and labels using NMS / Soft-NMS / NMW / WBF.

Dependencies:
NumPy, Pandas, Numba.

Compute:
CPU-oriented numeric fusion; no GPU requirement.

Adapter:
THIN for same-frame normalized detections.

MP limitation:
WBF fuses boxes. It does not create a provenance-rich temporal CandidateEvent by itself.

M1 disposition:
EVALUATE in M2 for same-frame multi-detector overlap only.

## Norfair

repository: tryolabs/norfair
pinned_commit: e517b4236f6b67a6ecf342f5df1fccb7788dbc54
license: BSD-3-Clause
package version at inspected ref: 2.3.0

Input:
detections represented by points/boxes and optional metadata/distance features.

Output:
tracked objects with stable IDs over time.

Source facts:
- detector-agnostic;
- custom distance function;
- moving-camera support;
- ReID option;
- SAHI/small-object example;
- core tracker itself does not require GPU; detector demos may.

Dependencies:
Python >=3.8, filterpy, scipy, numpy, rich; OpenCV optional for video helpers.

Adapter:
THIN-MODERATE:
MP observation -> Norfair Detection;
track ID/span -> CandidateEvent continuity evidence.

MP limitation:
generic MOT assumptions may not map cleanly to mostly static defects while the camera moves. Moving-camera compensation must be tested.

M1 disposition:
EVALUATE in M2.

## ByteTrack

repository: FoundationVision/ByteTrack
pinned_commit: d1bf0191adff59bc8fcfeaa0b33d3d1642552a99
license: MIT

Source facts:
box-association MOT; reported benchmarks are pedestrian/object MOT datasets and V100 performance.

MP assessment:
PARK.
It is strong MOT technology, but less configurable for the unusual static-surface/moving-camera association problem than Norfair and carries a heavier YOLOX-oriented repository stack.

## Spatial dedup references

### tank-inspection-uav

repository: mercwrite/tank-inspection-uav
pinned_commit: 9883295959f04a4ae3a0e1061653f23b9a84fb56
license: UNRESOLVED

Inspected defect_aggregator.py:
- stores defect_type, x/y/z and source;
- calculates Euclidean distance to existing records;
- suppresses a new record when within configurable 3D radius (default 0.5 m).

MP lesson:
once trustworthy mapped coordinates exist, simple spatial dedup can be effective.
This is later because MP telemetry/3D are intentionally non-blocking.

### AegisInspect

repository: AritraAcherjee/autonomous-drone-infrastructure-inspection
pinned_commit: 816a28619010ce1e42331bb215620f52d18a7d31
license: UNRESOLVED

Reference mechanisms:
persistent defect identity, repeated-observation aggregation, explicit human review and provenance.

MP lesson:
CandidateEvent should retain observation provenance rather than merely emitting a fused score.

## Architecture gap discovered

Solved pieces exist:
1. same-frame fusion: WBF/NMS,
2. temporal association: Norfair/SAM2/DEVA patterns,
3. later coordinate-space dedup: spatial registry patterns.

Unsolved/MP-specific in inspected sources:
a thin rule that turns those pieces into one provenance-preserving CandidateEvent for human RECHECK.

This is a documented integration gap, NOT authorization to BUILD it.

## M1 proposed disposition

M2:
- WBF smoke with synthetic/persisted detections,
- Norfair smoke on a moving-camera short clip,
- compare Norfair track continuity with SAM2 mask continuity.

Only after those results may MP decide whether a small custom CandidateEvent merger is needed.

REPLACES WHAT?:
most generic fusion/tracking logic; leaves only MP-specific event semantics if evidence confirms the gap.
