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

If either search is missing, STOP BUILD and create/update the Research Record.

If a suitable existing solution is found, prefer USE or ADAPT unless evidence supports BUILD.

## Build Request rule

Protected implementation work requires a per-change Build Request.

Do not rely on a historical broad permission.

Every current protected file must be listed exactly in:
`authorized_files`

Globs such as `src/**` are not valid authorization.

A NARROW_REPAIR may reuse an already accepted Research Record and does not require repeating Vertical/Horizontal search, provided the repair does not reopen the component/model/dependency/contract choice.

The Build Request must preserve the real human authorization provenance:
- decision_id
- source
- state_version
- subject_version

Never invent ACCEPTED status.

## Unknown implementation location

Moving executable code outside the expected layout does not bypass Research Gate.

Examples that remain protected:
- main.py
- tools/new_detector.py
- governance/evil.py

## Evidence

Do not call source inspection an execution test.
Do not call a README claim verified runtime behavior.
Do not infer Air 3S compatibility from support for another DJI model.

## Scope

Research may inspect broader technologies without promoting them into CURRENT BUILD SCOPE.

## Canonical policy

If this file conflicts with `governance/BUILD_POLICY.md`, the build policy controls.
