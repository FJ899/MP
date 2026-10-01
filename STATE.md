# STATE

protocol: TWO-WEBAI/0.2
project_id: FRANKENSTEIN_INSPECTION_LAB
state_version: 1
goal_version: 1
project_profile: REPO_INTEGRATION
work_mode: AUDIT

## Approved goal
Sprawdzić, czy z istniejących narzędzi można złożyć minimalne laboratorium, które przyjmuje materiał z lotu inspekcyjnego, analizuje go kilkoma komplementarnymi metodami, łączy wyniki i przekazuje operatorowi ograniczoną listę miejsc CONFIRM / REJECT / RECHECK.

Hipoteza:
> Czy Frankenstein wyławia z 30 minut filmu miejsca, którym człowiek rzeczywiście powinien przyjrzeć się ponownie?

## Approved scope
CURRENT:
- post-flight video analysis
- FFmpeg/OpenCV preprocessing
- anomaly detection
- known-defect detection
- sliced inference
- segmentation/tracking
- optional VLM interpretation
- merger/deduplication
- candidate events
- operator review
- audit of CVAT as annotation support
- audit of Hawk-I as integration reference

## Non-goals now
- Air 3S control
- autonomous return/waypoints
- OMVS product architecture
- dual-use architecture
- edge deployment
- multisensor/thermal
- custom autopilot
- full 3D reconstruction
- production GUI

## Current milestone
M1 — REPOSITORY SUITABILITY AUDIT

## M1 DONE
1. Exact source identity or UNRESOLVED.
2. Verified INPUT -> FUNCTION -> OUTPUT.
3. Repo license separated from model/weights license where relevant.
4. CPU/GPU requirements recorded from sources.
5. Training/reference/prompt/downstream dependencies identified.
6. Adapter need classified.
7. Each KEEP linked to RECHECK hypothesis.
8. No speculative component retained only for future value.
9. COLMAP/telemetry remain non-blocking.
10. Concrete M2 smoke-test candidate list produced.

## Authorization
audit_read: authorized
branch_changes_for_review: authorized by current task
merge_to_main: NOT AUTHORIZED
build_orchestrator: NOT AUTHORIZED
publish/release/deploy: NOT AUTHORIZED

## Next action
Independent PLAN/ARTIFACT review of M1 audit candidate on branch audit/m1-repo-suitability.
