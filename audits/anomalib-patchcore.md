# Anomalib / PatchCore audit — preliminary

repository: open-edge-platform/anomalib
role: anomaly detection candidate
execution_status: NOT_RUN
pipeline_compatibility: NOT_TESTED

## Source-backed behavior
Inspected PatchCore implementation states:
- training extracts and stores patch features from normal training images,
- inference compares test-image patches to stored features using nearest-neighbor search,
- pretrained backbone is used by default,
- outputs include anomaly information through the inference path.

## Input
- normal reference/training images to build memory bank
- test image(s)

## Output
- anomaly score/map through Anomalib inference objects

## Integration implication
PatchCore may detect deviations without named defect classes, but it is not zero-preparation. Our smoke test must include a representative normal-reference set.

## Adapter hypothesis
THIN-MODERATE:
normalize Anomalib score/map/region into the future common observation contract.

## Critical unknowns
- amount/diversity of normal material required for useful building-surface results
- threshold calibration
- performance on drone imagery
- exact frozen release/ref
- repository/model dependency licenses

## Recommendation
KEEP FOR M1 AUDIT; execution decision deferred to M2.
