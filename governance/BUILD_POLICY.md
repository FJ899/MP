# MP BUILD POLICY

Status: NORMATIVE PROJECT GOVERNANCE
Project: MP
Policy version: 1

## 1. Core rule

No major component may enter DESIGN/BUILD before the Research Gate has been satisfied.

Mandatory sequence:

```
PROBLEM
  ↓
VERTICAL SEARCH
+
HORIZONTAL SEARCH
  ↓
INSPECT / RUN
  ↓
COMPARE
  ↓
USE / ADAPT / LEARN / REJECT / PARK
  ↓
BUILD only if justified
```

BUILD is the last option, not the default.

## 2. What counts as a major component

Research Gate is mandatory when a change introduces or materially changes any of the following:

- a subsystem or pipeline stage,
- an external dependency or model family,
- an adapter to an external tool,
- a data/event contract,
- a new detector/segmenter/tracker/VLM role,
- quality-gate logic,
- telemetry integration,
- route/mission generation,
- merger/deduplication/event clustering,
- persistent storage/provenance architecture,
- a new runtime/service boundary,
- a replacement of an existing component.

Routine documentation edits and narrow bug fixes inside an already accepted component do not require a fresh search unless they reopen an architectural choice.

If classification is uncertain, treat the change as major until reviewed.

## 3. Research Gate requirements

A major component must have a durable JSON record under:

`research/records/<component-id>.json`

The record must contain:

- component_id
- problem
- vertical_search
  - date
  - status: DONE or NO_RESULT
  - queries
  - candidates
- horizontal_search
  - date
  - status: DONE or NO_RESULT
  - queries
  - candidates
- inspected_candidates
- comparison_summary
- integration_role
- decision
- replaces_what
- why
- review_status
- human_decision

Allowed integration_role values:

- DEPENDENCY
- COMPONENT
- REFERENCE_IMPLEMENTATION
- BENCHMARK
- REJECTED

Allowed decision values:

- USE
- ADAPT
- BUILD
- LEARN
- REJECT
- PARK

Only USE, ADAPT or BUILD may authorize implementation work.

If decision=BUILD, `build_justification` is mandatory and must explain why inspected USE/ADAPT candidates were insufficient.

## 4. Build authorization record

Protected implementation changes must also have a durable record under:

`governance/build_requests/<change-id>.json`

It links implementation scope to the accepted research record.

Required fields:

- change_id
- description
- scope
- research_record
- authorized_decision
- review_status
- human_decision

The `scope` field contains repository globs, for example:

```json
["components/quality_gate/**", "adapters/iiqc/**"]
```

A build request is valid only when:

- referenced research record exists,
- vertical search is DONE or NO_RESULT with recorded queries,
- horizontal search is DONE or NO_RESULT with recorded queries,
- decision is USE, ADAPT or BUILD,
- build request decision matches research decision,
- review_status=PASS,
- human_decision=ACCEPTED.

## 5. Protected build paths

The automated gate treats implementation-like changes as protected, including:

- src/**
- app/**
- pipeline/**
- components/**
- adapters/** except README-only changes
- models/**
- non-draft contracts/**
- dependency manifests such as pyproject.toml, requirements*.txt, package*.json, lockfiles
- Docker/runtime configuration

The exact executable check lives in:

`scripts/check_research_gate.py`

and is run by:

`.github/workflows/research-gate.yml`

## 6. Evidence rule

README similarity is not execution evidence.

Maintain separate states for:

- SOURCE_INSPECTED
- INSTALL_VERIFIED
- SMOKE_TEST_PASS/FAIL
- PIPELINE_COMPATIBILITY_VERIFIED

A search may produce NO_RESULT, but the query and date must be preserved.

## 7. Rejections are durable

REJECTED solutions remain recorded with:

- candidate/version
- expected replacement
- evidence
- why rejected
- limitations of verdict
- revisit condition

PARK is not REJECT.

## 8. Architecture freeze

MP Architecture v0.1 cannot be frozen while any architecture-critical component has:

- search not performed,
- unresolved candidate role,
- unresolved material license issue,
- unresolved compatibility that changes architecture,
- no review of the reconnaissance result.

## 9. AI instructions

Any AI working in this repository must:

1. Read `AGENTS.md`.
2. Read this policy.
3. Read `STATE.md`.
4. Check `research/REPO_RADAR.md` and existing `research/records/`.
5. Refuse to proceed directly to major BUILD when Research Gate evidence is missing.
6. Produce/update the research record first.
7. Never self-promote a proposal into HUMAN_ACCEPTED.

## 10. Enforcement limitation

Files and CI can strongly prevent accidental bypass, but they are not cryptographic guarantees against an administrator intentionally disabling the gate.

For strongest enforcement on `main`, GitHub repository rules should require:
- pull requests,
- the `Research Gate` status check,
- human/code-owner review for governance and workflow changes,
- no routine bypass of required checks.

The repository connector currently used by MP can create the files/workflow but does not expose ruleset/branch-protection write operations. GitHub settings must therefore be configured separately by the repository owner.
