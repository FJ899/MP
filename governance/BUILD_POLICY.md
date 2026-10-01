# MP BUILD POLICY

Status: NORMATIVE PROJECT GOVERNANCE
Project: MP
Policy version: 2

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

## 2. Major change vs narrow repair

Research Gate is mandatory when a change introduces or materially changes:
- a subsystem or pipeline stage,
- an external dependency or model family,
- an adapter to an external tool,
- a data/event contract,
- a detector/segmenter/tracker/VLM role,
- quality-gate logic,
- telemetry integration,
- route/mission generation,
- merger/deduplication/event clustering,
- persistent storage/provenance architecture,
- a runtime/service boundary,
- replacement of an existing component.

A NARROW_REPAIR fixes behavior inside an already accepted component without reopening:
- component choice,
- model/dependency family,
- public contract,
- service boundary,
- architectural role.

NARROW_REPAIR does not require a fresh Vertical/Horizontal search. It may reuse the accepted Research Record for that component.

If classification is uncertain, treat the change as MAJOR until reviewed.

## 3. Research Record

A major component has a durable record:

`research/records/<component-id>.json`

It records:
- component_id
- problem
- vertical_search
- horizontal_search
- inspected_candidates
- comparison_summary
- integration_role
- decision
- replaces_what
- why
- review_status
- human_decision
- human_acceptance

Allowed integration_role:
- DEPENDENCY
- COMPONENT
- REFERENCE_IMPLEMENTATION
- BENCHMARK
- REJECTED

Allowed implementation-authorizing decision:
- USE
- ADAPT
- BUILD

LEARN / REJECT / PARK remain valid research outcomes in the Radar, but they do not authorize implementation.

If decision=BUILD, `build_justification` must explain why inspected USE/ADAPT candidates were insufficient.

Search evidence must contain:
- a real ISO date,
- at least one non-empty query,
- DONE + candidates, or
- NO_RESULT + empty candidates.

A syntactically valid JSON file is not evidence that a search happened.

## 4. Per-change Build Request

Every protected implementation diff requires a Build Request that is ADDED OR MODIFIED IN THAT SAME DIFF:

`governance/build_requests/<change-id>.json`

This is intentionally separate from the Research Record.

Research Record answers:
> What solution/component choice is accepted?

Build Request answers:
> What exact repository change is authorized now?

Required:
- change_id
- change_kind: MAJOR or NARROW_REPAIR
- component_id
- description
- authorized_files
- research_record
- research_record_sha256
- authorized_decision
- authorization
- review_status
- human_decision

`authorized_files` is an exact list of repository paths.
Wildcards/globs are forbidden.

Example:

```json
[
  "components/quality_gate/adapter.py",
  "tests/test_quality_gate.py"
]
```

This prevents an old broad permission such as `src/**` from silently authorizing a future model family or subsystem.

The Build Request must:
- reference a non-template Research Record,
- pin the exact Research Record contents with SHA-256,
- use the same component_id and decision,
- include versioned authorization provenance.

Authorization provenance contains:
- decision_id
- source
- state_version
- subject_version

For NARROW_REPAIR:
- `repair_of` is mandatory,
- the accepted Research Record may be reused,
- an existing human authorization may be reused only when its recorded scope genuinely covers repair work in that component; otherwise a new human decision is required.

The AI must never invent ACCEPTED status or provenance.

## 5. Fail-closed implementation detection

The automated gate uses two layers:

1. explicit protected locations such as:
   - src/**
   - app/**
   - pipeline/**
   - components/**
   - models/**
   - adapters/**
   - non-draft contracts/**
   - dependency/runtime manifests

2. fail-closed unknown locations:
   executable/code files such as Python, JS/TS, Go, Rust, Java, C/C++, shell, PowerShell, notebooks, SQL and proto are protected even when placed outside the expected layout.

Therefore:
- `main.py` is protected,
- `tools/new_detector.py` is protected,
- moving code outside `components/` does not bypass the gate.

Narrow explicit exemptions exist only for governance/research/documentation artifacts needed to operate this policy.

Unknown non-document artifacts outside those exemptions are protected until classified.

The executable rule lives in:

`scripts/check_research_gate.py`

## 6. Evidence rule

Keep separate:
- SOURCE_INSPECTED
- INSTALL_VERIFIED
- SMOKE_TEST_PASS/FAIL
- PIPELINE_COMPATIBILITY_VERIFIED

README similarity is not runtime proof.

## 7. Rejections are durable

REJECTED solutions preserve:
- candidate/version
- expected replacement
- evidence
- why rejected
- limitations
- revisit condition

PARK is not REJECT.

## 8. Architecture freeze

MP Architecture v0.1 cannot freeze while an architecture-critical component has:
- search not performed,
- unresolved candidate role,
- material license ambiguity,
- architecture-changing compatibility unknown,
- missing review of reconnaissance.

## 9. AI entry instructions

Any AI working in this repository must:
1. Read `AGENTS.md`.
2. Read this policy.
3. Read `STATE.md`.
4. Check `research/REPO_RADAR.md` and relevant Research Records.
5. Stop before MAJOR BUILD if Research Gate evidence is missing.
6. Create/update research evidence first.
7. Never self-promote proposal/review into HUMAN_ACCEPTED.

## 10. Automated checks

GitHub Actions runs:
- regression tests for Research Gate,
- Research Gate validation against the PR/push diff.

The regression suite must include at least:
- unknown root code path blocked,
- unknown nested code path blocked,
- stale historical Build Request cannot authorize a new protected file,
- narrow repair can reuse accepted Research Record with a fresh per-change Build Request,
- invalid ISO date rejected,
- blank query rejected,
- invalid integration_role rejected.

## 11. CODEOWNERS

When GitHub Code Owner review is required, owner review must cover:
- governance/**
- .github/workflows/**
- .github/CODEOWNERS
- AGENTS.md
- research/records/**
- scripts/check_research_gate.py
- tests/test_research_gate.py

This protects both the written policy and the executable enforcement logic.

## 12. GitHub enforcement limitation

Files and CI strongly prevent accidental bypass but cannot stop an administrator from intentionally disabling the protection.

Strong merge enforcement on `main` should require:
- pull requests,
- the `Research Gate` status check,
- Code Owner review for governance/enforcement changes,
- dismissal/re-review after material changes where available,
- no routine bypass.

Observed repository rulesets and classic branch protection must be reported separately:
- empty ruleset list does not prove classic branch protection is absent,
- if classic branch protection cannot be read, status is UNAVAILABLE rather than NONE.

The current connector can create/update repository files but does not expose ruleset/branch-protection writes. Owner configuration remains an external step after review.
