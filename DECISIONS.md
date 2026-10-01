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

## D-007 — Vertical + horizontal search before major component design
Human decision: before designing a major component, run both:
- VERTICAL SEARCH for near-end-to-end systems,
- HORIZONTAL SEARCH for implementations of the exact component.

## D-008 — BUILD is the last option
Human decision: the default sequence is PROBLEM -> SEARCH EXISTING SOLUTIONS -> INSPECT/RUN -> COMPARE -> BORROW/ADAPT/BUILD. Custom implementation requires evidence that reuse/adaptation is insufficient.

## D-009 — Repository role classification
Human decision: repositories are classified as DEPENDENCY, COMPONENT, REFERENCE_IMPLEMENTATION, BENCHMARK or REJECTED. Evaluation status/decision is tracked separately as EVALUATE, USE, ADAPT, LEARN, REJECT or PARK.

## D-010 — Durable rejection rationale
Human decision: rejected solutions remain recorded with WHY and evidence so later work can explain why a custom solution exists.

## D-011 — Architecture freeze follows reconnaissance
Human decision: one Technology Reconnaissance pass around the current MP architecture must complete before MP Architecture v0.1 is frozen.

## D-012 — YOLO is a candidate, not an architectural decision
Human decision: detector selection must be informed by task-relevant benchmarks/datasets; YOLO is one candidate alongside alternatives such as RT-DETR or other methods supported by evidence.

## Working hypothesis — VLM authority
Source-derived hypothesis to test, not yet a frozen human decision:
use the detector/anomaly model as the source of detection verdict and treat VLM output as interpretation/explanation unless MP evidence later justifies a stronger role.

## D-013 — Two search rhythms
Human decision:
- targeted search is mandatory before designing each major component,
- broad ecosystem scan is periodic only, normally weekly or biweekly when useful,
- do not run a daily broad "AI drone repo" search that creates noise without a decision hinge.
