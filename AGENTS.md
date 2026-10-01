# MP — AI WORKING INSTRUCTIONS

These instructions apply to AI-assisted work in this repository.

## Mandatory first reads

Before planning or modifying a major component, read:

1. `STATE.md`
2. `governance/BUILD_POLICY.md`
3. `research/REPO_RADAR.md`
4. relevant files under `research/records/`
5. `DECISIONS.md`

## STOP RULE

Do not design or implement a major component until the Research Gate is complete.

Required sequence:

PROBLEM
→ VERTICAL SEARCH
→ HORIZONTAL SEARCH
→ INSPECT/RUN
→ COMPARE
→ USE/ADAPT/LEARN/REJECT/PARK
→ BUILD only when justified.

If either search is missing, STOP BUILD and create/update the research record.

If a suitable existing solution is found, prefer USE or ADAPT unless evidence supports BUILD.

## Never infer acceptance

AI review PASS is not HUMAN acceptance.
A proposed dependency, architecture, model, schema or build path remains proposed until the project state/decision record says otherwise.

## Evidence

Do not call source inspection an execution test.
Do not call a README claim verified runtime behavior.
Do not infer Air 3S compatibility from support for another DJI model.

## Scope

Research may inspect broader technologies without promoting them into CURRENT BUILD SCOPE.

## Canonical policy

If this file conflicts with `governance/BUILD_POLICY.md`, the build policy controls.
