# M2 Smoke Test Plan — Proposed by M1

status: PROPOSED_FOR_REVIEW
implementation_authorization: NOT_GRANTED

Purpose:
run the cheapest discriminating tests that can reduce uncertainty about the RECHECK hypothesis without building the full MP pipeline.

General rule:
a smoke test may demonstrate component behavior. It does not promote the component to an accepted dependency or freeze architecture.

## M2-01 — Video timestamp integrity

Question:
Can MP reproducibly map a native Air 3S video interval to extracted frames and timestamps?

Input:
- one 30–60 second native Air 3S MP4 clip;
- no need for a 30-minute flight.

Candidate tools:
- FFmpeg pinned in M1;
- OpenCV pinned in M1.

Required observations:
- source filename;
- frame index;
- PTS/timestamp or equivalent reproducible time reference;
- extracted image dimensions;
- extraction parameters.

Observable result:
- monotonically ordered time references;
- repeated extraction returns the same selected timestamps/frames within documented decoder/timebase behavior;
- no silent frame/time reordering.

Failure that matters:
timestamp/frame mapping is unstable enough that later CandidateEvent provenance cannot point back to source material.

Do not freeze:
sampling cadence such as 10 s / step 8 s.

## M2-02 — Existing image-quality signal feasibility

Question:
Can an existing licensed quality metric distinguish obviously degraded inspection frames from visibly usable ones well enough to justify a simple upstream gate?

Input:
- 20–50 frames from the same or comparable Air 3S material;
- include manually identified examples of strong blur, severe underexposure/overexposure or compression where available;
- manual labels are only a small smoke reference, not a quality dataset.

Candidate:
rehanguha/brisque at M1 pinned commit.

Default model dependencies:
- brisque/models/svm.txt
- brisque/models/normalize.pickle

Precondition before execution:
- resolve provenance/terms for the bundled default SVM + normalization artifacts, OR
- supply a custom BRISQUE model with pinned acceptable provenance/terms.

This precondition does not authorize training.

Output:
- BRISQUE score per frame;
- provenance linking score to source frame.

Observable result:
- score ordering/distribution for manually obvious good vs bad cases;
- examples where score disagrees with human inspection judgment.

Success is NOT:
choosing a production threshold.

Decision after test:
- if signal has discriminating value: ADAPT/continue evaluation;
- if it does not: PARK and inspect other existing metrics before custom BUILD.

## M2-03 — PatchCore anomaly ranking

Question:
Can a small normal-reference bank rank suspicious facade/inspection crops above normal-looking crops without being dominated by capture-quality artifacts?

Input:
- approximately 20–100 representative normal-reference crops from one visually coherent surface/domain;
- small test set containing normal-looking and intentionally selected irregular/candidate regions;
- quality-degraded examples should be kept identifiable.

Candidate:
open-edge-platform/anomalib PatchCore at pinned M1 commit.

Requirements:
- Python >=3.10;
- Anomalib dependencies;
- CPU or supported accelerator path;
- exact pretrained backbone used must be recorded with its source/license before execution.

Output:
- anomaly score;
- anomaly map;
- source frame/crop identity.

Observable result:
- relative ranking of known/reference cases;
- whether blur/exposure dominates anomaly score;
- whether anomaly map is localized enough to create a candidate region.

Success is NOT:
claiming crack detection or production accuracy.

## M2-04 — SAM2 candidate persistence

Question:
Given one candidate box on one frame, can SAM2 follow the suspicious region through adjacent UAV frames well enough to provide temporal persistence evidence?

Input:
- one 5–15 second inspection clip;
- one manually supplied candidate box/region on a chosen frame.

Candidate:
facebookresearch/sam2
checkpoint proposal: SAM2.1 Hiera Small.

Requirements:
- documented SAM2 Python/PyTorch stack;
- GPU preferred for useful iteration speed;
- exact checkpoint identity recorded.

Output:
- per-frame mask;
- object ID;
- tracked frame span.

Observable result:
- fraction of adjacent frames with plausible mask;
- visible drift/failure points;
- effect of viewpoint/camera motion;
- whether mask persistence provides useful support for one CandidateEvent.

Success is NOT:
automatic defect discovery. The candidate is supplied to SAM2.

## M2-05 — Same-frame detector fusion semantics

Question:
If two analysis mechanisms report overlapping boxes in the same frame, can existing fusion remove duplicate geometry without destroying the provenance MP needs?

Input:
- a small synthetic or persisted set of normalized boxes/scores/labels from two named sources;
- no defect model execution required.

Candidate:
ZFTurbo/Weighted-Boxes-Fusion.

Output:
- fused box/score/label.

Critical observation:
WBF's native output does not by itself preserve full source-observation provenance.

Test result must answer:
can MP wrap WBF as geometry fusion while separately retaining original Observation IDs, or does this create semantic ambiguity?

Success is NOT:
a complete CandidateEvent merger.

## M2-06 — Temporal association under moving camera

Question:
Can a generic tracker associate repeated candidate boxes into useful spans when the inspected surface is mostly static but the UAV camera moves?

Input:
- one short moving-camera clip;
- precomputed/manual candidate boxes on selected frames.

Candidate:
tryolabs/norfair.

Modes to compare where feasible:
- simple box/centroid distance;
- moving-camera compensation.

Output:
- track IDs;
- first/last frame;
- association history.

Observable result:
- track fragmentation;
- false merges;
- sensitivity to camera motion;
- whether custom distance logic is likely required.

Success is NOT:
proving a final merger architecture.

## M2-07 — CandidateEvent contract evidence test

Question:
After M2-05 and M2-06, what information must survive into a human-reviewable event?

This is a contract/evidence exercise, not an orchestrator implementation.

Input:
outputs/evidence from M2-01, M2-05 and M2-06, optionally M2-04.

Required candidate information to validate:
- source video identity;
- start/end timestamps;
- original Observation IDs;
- detector/analyzer identity;
- original scores;
- fused/track relation;
- representative frame/region;
- quality status;
- reason for RECHECK;
- confidence/status without pretending it is a human decision.

Observable result:
a revised Observation vs CandidateEvent schema proposal grounded in actual component outputs.

The existing candidate_event.schema.draft.json remains NON-FROZEN until this test.

## M2-BLOCKED-01 — Known-defect detector

Status:
BLOCKED BY PRECONDITION.

Do not run generic COCO YOLO and call it facade-defect validation.

Unblock when:
- a task-relevant pretrained checkpoint with acceptable code/weights license is pinned; or
- HUMAN later authorizes a deliberately scoped training experiment on suitably licensed data.

BFD-UAV2K remains a benchmark/reference while its README says license information is pending.

SAHI remains an optional direct-vs-sliced mode after a real detector exists.

## M2-PARKED-01 — VLM interpretation

Status:
PARK.

Reason:
M2 first needs useful candidate evidence.
A VLM that produces fluent descriptions without improving human triage does not advance the main hypothesis.

If later tested:
detector/anomaly evidence remains the verdict source unless a new reviewed experiment justifies different authority.

## M2-PARKED-02 — CVAT

Status:
PARK.

Use only if smoke tests reveal a real annotation/review dataset burden.
Do not deploy annotation infrastructure preemptively.

## M2-PARKED-03 — Telemetry / route / 3D

Status:
PARK / NON-BLOCKING.

First later telemetry test:
inspect one actual Air 3S recording/log to identify SRT/subtitle/FlightRecord/DAT availability and compare with pinned existing parsers.

Route generation and COLMAP remain downstream of proven RECHECK value.

## Proposed M2 order

1. M2-01 timestamp integrity
2. M2-02 quality signal
3. M2-03 PatchCore
4. M2-04 SAM2 persistence
5. M2-05 WBF semantics
6. M2-06 Norfair temporal association
7. M2-07 contract evidence test

Rationale:
each step is small, reversible and can remove a component or expose a real integration gap before orchestration exists.

## M2 authorization boundary

This plan is a review artifact only.
Running these tests, adding dependency manifests, creating adapters or writing implementation code requires the appropriate HUMAN/Research Gate authorization after M1 review.
