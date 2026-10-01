# Review request — revised M1 candidate

Review target: branch audit/m1-repo-suitability-v2

## Change under review
Human corrected the working method:

PROBLEM
-> VERTICAL SEARCH + HORIZONTAL SEARCH
-> INSPECT / RUN
-> COMPARE
-> USE / ADAPT / LEARN / REJECT / PARK
-> BUILD only if a real gap remains.

The goal did not change.
MP Architecture v0.1 is explicitly NOT READY TO FREEZE.

## Reviewer questions
1. Does the revised candidate preserve the approved hypothesis: 30 min video -> limited candidate events -> human RECHECK?
2. Does the SEARCH-BEFORE-BUILD gate materially prevent premature custom implementation?
3. Are VERTICAL and HORIZONTAL searches distinct enough to catch both whole-system competitors and component-level substitutes?
4. Are integration roles (DEPENDENCY / COMPONENT / REFERENCE_IMPLEMENTATION / BENCHMARK / REJECTED) correctly separated from decisions (EVALUATE / USE / ADAPT / LEARN / REJECT / PARK)?
5. Does REPO_RADAR capture enough information to influence backlog, especially REPLACES WHAT? and WHY?
6. Are source claims separated from MP assessments and execution evidence?
7. Is architecture freeze correctly blocked until Technology Reconnaissance is reviewed?
8. Are any current findings overstated, especially:
   - IIQC as a possible quality-gate source despite its heavier ROS/3D/pose context,
   - AI-Visual-Inspector as a detector-authority/VLM-description reference,
   - WayPoint's claimed Air 3S support without MP execution,
   - DroneRoute's lack of Air 3S in its current supported-drone list,
   - drone-mission-planning's explicit need for Air 3S calibration,
   - BFD-UAV2K's pending license information?
9. Is the current first-pass reconnaissance sufficiently broad to continue M1, while still marking incomplete searches as incomplete rather than pretending coverage?
10. Has any research-only item (telemetry/route generation/whole-system references) leaked into CURRENT BUILD SCOPE?

## Blocking criteria
A finding is BLOCKING/MAJOR only if it conflicts with approved goal/DONE, source discipline, evidence discipline, search-before-build discipline, or creates material integration risk.

## Expected reviewer output
For each BLOCKING/MAJOR:
- issue_id
- violated DONE/contract
- evidence
- impact
- minimum correction

Reviewer may recommend a simpler search/audit path.
Reviewer must not freeze MP Architecture v0.1 or choose final dependencies on behalf of HUMAN.

## Explicit non-authorization
Review PASS does not authorize merge, implementation, model training, flight execution, route upload, deployment, publication, or promotion of any candidate to dependency.


## Research Gate enforcement review

11. Is `governance/BUILD_POLICY.md` a clear normative source of truth rather than duplicating STATE ambiguously?
12. Does `AGENTS.md` create a useful AI entry STOP rule without pretending all tools automatically enforce it?
13. Does `scripts/check_research_gate.py` protect the right implementation-like paths?
14. Are README-only adapter docs and explicit *.draft.* contracts correctly excluded from hard build blocking?
15. Does the gate avoid requiring a fresh search for every narrow bug fix in an already accepted component?
16. Are research record and build request separate for a good reason:
    - research answers "what should we do?",
    - build request answers "what exact repository scope is now authorized?"
17. Is requiring review_status=PASS and human_decision=ACCEPTED appropriate before protected implementation?
18. Can the gate be bypassed accidentally by placing code outside currently protected path patterns?
19. Should the project adopt a future canonical implementation layout (for example components/<id>/) to make gate coverage easier?
20. Is CODEOWNERS coverage sufficient for governance/workflow files once GitHub owner enables required Code Owner review?
21. Current repository rulesets are empty. Confirm that CI alone is NOT hard merge enforcement until main requires the Research Gate status check.
22. Is the enforcement design proportionate to MP, or has it become process-heavy enough to slow small experiments?

### Required reviewer distinction
Classify any finding as:
- POLICY flaw,
- AUTOMATION flaw,
- GITHUB CONFIGURATION gap,
- PROCESS OVERHEAD suggestion.

Do not treat the absence of current branch protection as a code defect in the policy. It is an explicit owner-configuration gap.


## Repair review after MP/review-001/AI-B

Review the repaired candidate specifically against:

### MP-R01
Expected:
- main.py => protected
- tools/new_detector.py => protected
- governance/evil.py => protected
- unknown non-document artifact => fail closed unless explicitly classified/exempted.

### MP-R02
Expected:
- historical Build Request not changed in current diff cannot authorize a new protected file,
- authorized_files are exact paths, not globs,
- component_id must match Research Record,
- Research Record contents are pinned by SHA-256,
- authorization records decision_id/source/state_version/subject_version,
- NARROW_REPAIR may reuse Research Record but requires a current per-change Build Request.

### MP-R03
Expected CODEOWNERS:
- /scripts/check_research_gate.py @FJ899
- /tests/test_research_gate.py @FJ899
- /.github/CODEOWNERS @FJ899
plus existing governance/workflow/records coverage.

### MP-R04
Expected validation:
- YYYY-MM-DD placeholder rejected,
- invalid calendar date rejected,
- blank query rejected,
- invalid integration_role rejected,
- DONE with no candidates rejected,
- NO_RESULT with candidates rejected.

### Separation
Do not interpret Research Gate PASS as M1 DONE.
M1 remains OPEN and Architecture v0.1 remains NOT_READY.


## Final MP-R01 repair review — cycle 2/2

Source:
MP/review-002/AI-B

Verify only the remaining MP-R01 gap and regression impact.

### Counterexamples that must now be protected

- experiments/requirements.txt
- docs/package.json
- governance/docker-compose.yml
- research/environment.yml
- contracts/adapter.draft.py

### Draft artifact that must remain exempt

- contracts/candidate_event.schema.draft.json

### Required Git behavior

A diff adding:
experiments/requirements.txt

without a current Build Request must produce:
FAIL
and identify the manifest as protected.

### Ordering requirement

Classification order must enforce:
1. exact enforcement exemptions,
2. dependency/runtime manifests,
3. contract draft rule,
4. canonical protected paths,
5. executable/code suffixes,
6. generic governance/research/docs data exemptions,
7. safe documentation suffixes,
8. fail-closed default.

### Cycle limit

This is repair-review cycle 2/2.
If a remaining BLOCKING/MAJOR defect is found, return it clearly; AI-A must escalate to HUMAN rather than automatically perform a third repair loop.
