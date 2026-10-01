# SAM2 audit — preliminary

repository: facebookresearch/sam2
role: segmentation / temporal propagation candidate
execution_status: NOT_RUN
pipeline_compatibility: NOT_TESTED

## Source-backed behavior
README documents:
- prompted image segmentation,
- automatic mask generation for images,
- video predictor with initialized video state,
- point/box prompts,
- propagation of masks through video.

## Input
Primary video path:
- video/frames
- initial point/box prompt or candidate region

## Output
- masks / propagated masklets for tracked object regions

## Integration implication
For the first MP pipeline, SAM2 is better treated as downstream evidence enrichment after a candidate region exists, not as a fourth independent defect detector.

## Adapter hypothesis
THIN-MODERATE:
candidate region -> SAM2 prompt;
returned masks/tracks -> persistence/region evidence.

## Critical unknowns
- exact latency/VRAM on target hardware
- useful persistence thresholds for moving drone footage
- robustness to viewpoint change
- frozen checkpoint/ref/license combination

## Recommendation
KEEP DOWNSTREAM OF CANDIDATE; smoke-test after detector/anomaly path exists.
