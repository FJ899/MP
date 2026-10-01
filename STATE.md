# STATE

protocol: TWO-WEBAI/0.2
project_id: MP
state_version: 8
goal_version: 1
project_profile: REPO_INTEGRATION
work_mode: AUDIT
changed_fields: M1_reconnaissance_result, M1_review_candidate, M2_smoke_proposal, source_pins, next_action

## Approved goal

Sprawdzić, czy z istniejących narzędzi można złożyć minimalne laboratorium, które przyjmuje materiał z lotu inspekcyjnego, analizuje go kilkoma komplementarnymi metodami, łączy wyniki i przekazuje operatorowi ograniczoną listę miejsc CONFIRM / REJECT / RECHECK.

Hypothesis:
Czy MP wyławia z 30 minut filmu miejsca, którym człowiek rzeczywiście powinien przyjrzeć się ponownie?

## Current scope

CURRENT:
- post-flight video analysis
- video/frame provenance
- quality-gate research
- anomaly detection
- known-defect detection research
- sliced inference research
- segmentation/tracking
- merger/deduplication
- CandidateEvent evidence
- operator CONFIRM / REJECT / RECHECK

RESEARCH-ONLY / LATER:
- Air 3S telemetry integration
- route/WPML/KMZ automation
- autonomous reinspection
- COLMAP/full 3D
- edge deployment
- thermal/multisensor
- production GUI/productization

## Working method

For every major component:

PROBLEM
→ VERTICAL SEARCH + HORIZONTAL SEARCH
→ INSPECT / RUN where justified
→ COMPARE
→ USE / ADAPT / LEARN / REJECT / PARK
→ BUILD only when existing solutions are insufficient.

Research Gate technical repair:
HUMAN-ACCEPTED in reviewed scope.

accepted_research_gate_version:
f799d26184504ae890b3a8ab064ad29de9267cbd

decision_id:
HUMAN-ARTIFACT-DECISION-RG-001

Known Research Gate limitations remain:
- GitHub Actions PASS for accepted artifact was not observed,
- hard merge enforcement is not verified,
- classic branch protection is unavailable through connector.

## Current milestone

M1 — TECHNOLOGY RECONNAISSANCE + REPOSITORY SUITABILITY AUDIT

m1_status:
READY_FOR_INDEPENDENT_REVIEW

m1_human_acceptance:
PENDING

m1_result:
M1_RESULT.md

m2_proposal:
M2_SMOKE_TEST_PLAN.md

MP Architecture v0.1:
NOT READY TO FREEZE

## M1 DONE contract

1. Exact source identity or UNRESOLVED.
2. Verified INPUT -> FUNCTION -> OUTPUT.
3. Repo license separated from model/weights/data license where relevant.
4. CPU/GPU requirements recorded from sources.
5. Training/reference/prompt/downstream dependencies identified.
6. Adapter need classified.
7. Each serious EVALUATE/USE/ADAPT tied to RECHECK hypothesis.
8. No speculative component retained only for future value.
9. COLMAP/telemetry remain non-blocking.
10. Concrete M2 smoke-test candidate list produced.
11. Major problem areas have recorded Vertical/Horizontal searches including NO_RESULT where applicable.
12. Serious Radar candidates record required decision fields.
13. Rejected candidates retain WHY/evidence; no false REJECT is required when PARK is correct.
14. Any custom BUILD proposal must prove existing solutions insufficient.
15. Architecture is not frozen before independent review + HUMAN decision.

Coverage claim:
see M1_RESULT.md.
It remains a claim for AI-B to verify, not self-acceptance.

## Proposed M2 candidate set

EVALUATE after future authorization:
- FFmpeg
- OpenCV
- BRISQUE
- Anomalib PatchCore
- SAM2.1 Hiera Small
- Weighted Boxes Fusion
- Norfair

BLOCKED:
known-defect detector until task-relevant checkpoint/license or separately authorized training path exists.

PARK:
- VLM
- CVAT
- telemetry
- route generation
- COLMAP/3D
- extra tracker/VOS alternatives unless a smoke test exposes a gap.

## Authorization

audit_read:
AUTHORIZED

technology_reconnaissance:
AUTHORIZED

repository_suitability_audit:
AUTHORIZED

prepare_M1_for_review:
AUTHORIZED

M1 acceptance:
PENDING HUMAN

M2 execution:
NOT AUTHORIZED

dependency installation:
NOT AUTHORIZED by this state

implementation:
NOT AUTHORIZED

merge_to_main:
NOT AUTHORIZED

architecture_freeze:
NOT AUTHORIZED

publish/release/deploy:
NOT AUTHORIZED

flight/route execution:
NOT AUTHORIZED

## Execution status

MP execution of proposed M2 components:
NOT_RUN

End-to-end MP pipeline:
NOT_BUILT / NOT_RUN

No source README claim is promoted to MP runtime evidence.

## Material open gaps

- exact licensed task-relevant known-defect checkpoint unresolved;
- PatchCore pretrained backbone identity/terms must be pinned before execution;
- no MP hardware benchmarks;
- no actual Air 3S video/log compatibility execution in M1;
- no accepted quality thresholds;
- CandidateEvent semantic merger remains an open integration hypothesis;
- some reference repos have unresolved/no top-level license.

## Next action

AI-B performs independent M1 review of the pinned candidate artifacts.

After AI-B review:
HUMAN decides whether to ACCEPT / REQUEST_CHANGES / DEFER the M1 result and whether any M2 smoke execution should be authorized.

No architecture freeze or implementation occurs before that decision.
