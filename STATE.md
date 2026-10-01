# STATE

protocol: TWO-WEBAI/0.2
project_id: MP
state_version: 4
goal_version: 1
project_profile: REPO_INTEGRATION
work_mode: AUDIT
changed_fields: governance_enforcement, research_gate_automation, state_version, next_action

## Approved goal
Sprawdzić, czy z istniejących narzędzi można złożyć minimalne laboratorium, które przyjmuje materiał z lotu inspekcyjnego, analizuje go kilkoma komplementarnymi metodami, łączy wyniki i przekazuje operatorowi ograniczoną listę miejsc CONFIRM / REJECT / RECHECK.

Hipoteza:
> Czy MP wyławia z 30 minut filmu miejsca, którym człowiek rzeczywiście powinien przyjrzeć się ponownie?

## Approved scope
CURRENT BUILD SCOPE:
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

RESEARCH SCOPE MAY ALSO INSPECT:
- quality-gate implementations
- telemetry parsers
- route-generation / DJI WPML/KMZ tools
- re-inspection/recollection systems
- whole-system UAV inspection implementations
- datasets/benchmarks relevant to defect detection

Research inclusion does not promote an item into CURRENT BUILD SCOPE.

## Non-goals now
- Air 3S control implementation
- autonomous return/waypoints implementation
- OMVS product architecture
- dual-use architecture
- edge deployment
- multisensor/thermal
- custom autopilot
- full 3D reconstruction
- production GUI

## Working method — SEARCH BEFORE BUILD
For every major component before design/implementation:

1. PROBLEM — define the exact unresolved function.
2. VERTICAL SEARCH — find systems solving nearly the same end-to-end problem.
3. HORIZONTAL SEARCH — find implementations solving the exact component.
4. INSPECT / RUN — inspect source first; execute the cheapest discriminating test where justified.
5. COMPARE — compare candidates against MP requirements.
6. CLASSIFY — assign integration_role and decision.
7. BUILD — only when existing solutions are insufficient or adaptation costs more than a minimal custom implementation.

BUILD is the last option, not the default.

### Integration roles
- DEPENDENCY
- COMPONENT
- REFERENCE_IMPLEMENTATION
- BENCHMARK
- REJECTED

### Decision/status vocabulary
- EVALUATE
- USE
- ADAPT
- LEARN
- REJECT
- PARK

Each radar entry must include REPLACES WHAT? and WHY.

## Current milestone
M1 — TECHNOLOGY RECONNAISSANCE + REPOSITORY SUITABILITY AUDIT

M1 has one milestone and two ordered phases:
- M1A: Technology Reconnaissance around the current MP problem map.
- M1B: Suitability audit of the strongest candidates.

MP Architecture v0.1 is NOT READY TO FREEZE until M1 completes.

## M1 DONE
1. Exact source identity or UNRESOLVED.
2. Verified INPUT -> FUNCTION -> OUTPUT.
3. Repo license separated from model/weights license where relevant.
4. CPU/GPU requirements recorded from sources.
5. Training/reference/prompt/downstream dependencies identified.
6. Adapter need classified.
7. Each KEEP/USE/ADAPT linked to the RECHECK hypothesis.
8. No speculative component retained only for future value.
9. COLMAP/telemetry remain non-blocking to first vision-value proof.
10. Concrete M2 smoke-test candidate list produced.
11. Each major problem area has recorded VERTICAL and/or HORIZONTAL searches, including query/date/no-result where applicable.
12. Radar candidates record NAME, URL, PROBLEM SOLVED, INPUT, OUTPUT, LICENSE, LAST ACTIVE, TESTS, DOCUMENTATION, GPU/CPU, MATURITY, INTEGRATION COST, WHAT WE CAN LEARN, REPLACES WHAT?, ROLE, DECISION and WHY.
13. Rejected candidates keep a durable WHY/evidence record.
14. A custom BUILD proposal must identify which existing candidates were inspected and why USE/ADAPT/LEARN did not satisfy the requirement.
15. MP Architecture v0.1 is not frozen before the reconnaissance pass is reviewed.

## Authorization
audit_read: authorized
technology_reconnaissance: authorized
branch_changes_for_review: authorized by current task
merge_to_main: NOT AUTHORIZED
build_orchestrator: NOT AUTHORIZED
publish/release/deploy: NOT AUTHORIZED

## Governance enforcement
Research Gate is now represented by:
- AGENTS.md
- governance/BUILD_POLICY.md
- research/records/*.json
- governance/build_requests/*.json
- scripts/check_research_gate.py
- .github/workflows/research-gate.yml
- .github/PULL_REQUEST_TEMPLATE.md
- .github/CODEOWNERS

The automated gate is intended to block protected implementation-like changes without accepted research/build records.

Repository ruleset status observed on 2026-10-01:
- repository rulesets: none configured
- connector cannot write branch-protection/ruleset settings

Therefore hard merge enforcement on main is PENDING OWNER CONFIGURATION after review.

## Next action
Independent review of M1 Technology Reconnaissance plus the new Research Gate enforcement design on branch audit/m1-repo-suitability-v2.
