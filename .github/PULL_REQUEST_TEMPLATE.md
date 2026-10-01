## MP change

### Goal / DONE
Describe what this PR changes and the observable DONE condition.

### Change class
- [ ] Documentation/research only
- [ ] NARROW_REPAIR inside an already accepted component
- [ ] MAJOR component / dependency / architecture change

### Research Gate
For protected implementation changes:

Research record:
`research/records/________________.json`

Build request created/modified in THIS PR:
`governance/build_requests/________________.json`

- [ ] VERTICAL SEARCH recorded or legitimately reused for NARROW_REPAIR
- [ ] HORIZONTAL SEARCH recorded or legitimately reused for NARROW_REPAIR
- [ ] candidates inspected/compared for MAJOR choice
- [ ] REPLACES WHAT? recorded
- [ ] research decision is USE / ADAPT / BUILD
- [ ] BUILD justification present if custom BUILD
- [ ] Build Request component_id matches Research Record
- [ ] Research Record SHA-256 is pinned
- [ ] authorized_files lists exact changed implementation paths; no globs
- [ ] authorization contains real decision_id/source/state_version/subject_version
- [ ] independent review PASS recorded
- [ ] HUMAN acceptance/authorization provenance recorded

### Narrow repair only
- [ ] repair_of identifies the defect/issue
- [ ] repair does not reopen model/dependency/contract/component choice
- [ ] existing Research Record is still applicable

### Evidence
State clearly what was:
- inspected,
- installed,
- executed,
- smoke-tested,
- integration-tested.

Do not convert README claims into execution evidence.

### Scope control
- [ ] No LATER/research-only item was silently promoted into build scope.
- [ ] MP Architecture/version was not changed without explicit decision.

### Reviewer
Check `governance/BUILD_POLICY.md` before approving.
