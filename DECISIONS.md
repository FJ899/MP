# DECISIONS

## D-001 — Laboratory before product
Human decision: build a lab to test RECHECK value before defining the final product.

## D-002 — Post-flight first
Air 3S is initially only a material source. Drone-control integration is outside the first proof.

## D-003 — Telemetry after vision value
Timestamp -> telemetry is deferred until the vision pipeline produces useful candidate events.

## D-004 — 3D only if needed
COLMAP / detailed geometry are LATER unless simple timestamp-to-telemetry proves insufficient.

## D-005 — Thin replaceable integration
Analyzers should communicate through a common normalized contract so a component can be replaced without rebuilding the full pipeline.

## D-006 — Audit before build
No orchestrator architecture is frozen before real I/O, dependencies and constraints of candidates are audited.

## Pending decisions
- final M1 KEEP/LATER/DROP set
- exact common event contract
- whether VLM belongs in first executable smoke test
- exact YOLO model/weights
- exact telemetry parser
