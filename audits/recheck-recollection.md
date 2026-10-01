# M1 Audit — Recheck and Recollection

execution_status: NOT_RUN
flight_execution: NOT_AUTHORIZED

## Problem

A CandidateEvent is useful only if it can drive a human decision:
CONFIRM / REJECT / RECHECK.

For RECHECK, MP eventually needs enough provenance to identify what should be captured again. M1 is limited to learning the mechanism; autonomous revisit is outside current build scope.

## Search result

Direct GitHub repository searches with:
- UAV reinspection recollection inspection waypoint defect
- drone reinspection defect revisit waypoint
- UAV image recollection inspection quality
- drone repeat inspection defect tracking

returned no useful repository candidates under those exact formulations.

Broader discovery followed by GitHub source verification found the following references.

## Dual-UAV pipeline inspection

repository: carloscs04/uav-vision-pipeline-inspection
pinned_commit: 5d4389b19c4dd237e456842d80b969135fcfe74d
license: MIT

Source facts:
- primary Tello drone logs defect/hazard outcomes and telemetry;
- flagged locations are written to a shared manifest;
- secondary drone parses flagged target coordinates and performs targeted re-inspection.

MP lesson:
CandidateEvent -> durable target/provenance record -> later reinspection task is an existing pattern.
The Tello/autonomous-flight implementation itself is out of MP's current scope.

Disposition:
REFERENCE_IMPLEMENTATION + LEARN.

## RDMO Digital Twin

repository: EdwinTSalcedo/RDMO-DigitalTwin
pinned_commit: 1152268834a4a1bac541867d4be463677c827e6f
license: UNRESOLVED

Source facts:
simulates pavement inspection recovery strategies:
- Baseline,
- Hover,
- Micro local reposition,
- Skip and revisit later.

Reports trade-offs in recovery coverage, time and energy.

MP lesson:
RECHECK is not one universal action; different recovery policies trade information gain against mission cost.

Disposition:
REFERENCE / BENCHMARK + LEARN.

## IIQC recollection pattern

repository: fwan133/IIQC
pinned_commit: b60ddf0aebe8bdafcdbf2e0122d51c63b60462c8

MP lesson:
quality failure itself can trigger recollection, independently of defect confidence.

Disposition:
LEARN.

## M1 boundary

No autonomous recheck route or Air 3S mission upload is part of M2.

For the first MP proof, RECHECK output can remain:
- source video,
- timestamp interval,
- representative frame/crop,
- reason/evidence,
- later optional telemetry reference.

This is enough for a human operator to locate the suspicious interval manually.

## M1 proposed disposition

LEARN existing event->revisit patterns.
PARK route automation until vision candidate events are useful and Air 3S telemetry/mission compatibility is proven.

REPLACES WHAT?:
premature custom autonomous revisit system.
