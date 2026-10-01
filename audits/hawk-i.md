# Hawk-I audit — preliminary

repository: Arvoxis/hawk-i
role: integration reference
execution_status: NOT_RUN
pipeline_compatibility: NOT_TESTED

## Source-backed behavior
README describes a drone-inspection stack combining:
- YOLOv11n
- YOLO-World
- SAM 2.1
- DINOv2
- Gemma 3 via Ollama
- FastAPI/WebSocket
- GPS/MAVLink
- reporting/database/dashboard elements

The README also places SAM2 downstream of detections, using boxes to obtain masks.

## Integration implication
This repository is unusually close to our problem class and is useful for:
- interface ideas,
- failure-mode discovery,
- checking how detector -> segmenter -> verification -> report can be wired.

It must not become our target architecture merely because it is comprehensive.

## Adapter hypothesis
REFERENCE ONLY for M1.

## Critical unknowns
- which README claims are verified by execution in its own repository
- which components are necessary for our narrower post-flight hypothesis
- whether any code can be reused cleanly without importing unrelated edge/GCS architecture
- license/weights details

## Recommendation
REFERENCE; do not make it a required runtime dependency.
