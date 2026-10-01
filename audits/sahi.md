# SAHI audit — preliminary

repository: obss/sahi
role: sliced-inference layer
execution_status: NOT_RUN
pipeline_compatibility: NOT_TESTED

## Source-backed behavior
Inspected documentation describes AutoDetectionModel and get_sliced_prediction, including an Ultralytics backend example.

## Input
- image
- configured detector/model
- slicing parameters

## Output
- merged detector predictions originating from slices

## Integration implication
SAHI should not be counted as an independent semantic detector beside YOLO. The meaningful comparison is typically direct detector inference vs detector + SAHI sliced inference.

## Adapter hypothesis
THIN:
same normalized detection contract as the underlying detector; preserve metadata indicating sliced inference.

## Critical unknowns
- whether small-defect recall improves enough to justify added cost
- overlap/slice parameters for 4K drone frames
- runtime cost on selected hardware
- frozen release/ref and licenses

## Recommendation
KEEP AS OPTIONAL DETECTOR MODE; do not duplicate it as a parallel evidence source.
