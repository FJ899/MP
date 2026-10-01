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
