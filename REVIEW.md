# Review request — M1 candidate

Review target: branch audit/m1-repo-suitability-v2

## Reviewer questions
1. Does the candidate preserve the approved hypothesis: 30 min video -> limited candidate events -> human RECHECK?
2. Does any file silently promote OMVS, telemetry, 3D, edge, GUI or autonomous flight into current scope?
3. Are detector, wrapper, segmenter, runtime and reference implementation roles kept distinct?
4. Are inspection claims clearly separated from execution claims?
5. Is the draft event schema correctly marked NON-FROZEN?
6. Is anything already overengineered for an audit repository?
7. What is the smallest safe next step after review: more source audit, one-component smoke test, or schema work?

## Blocking criteria
A finding is BLOCKING/MAJOR only if it conflicts with approved goal/DONE, source discipline, evidence discipline, or creates material integration risk.

## Explicit non-authorization
Review PASS does not authorize merge, build, deployment, publication, external effects or promotion of the draft schema to frozen contract.
