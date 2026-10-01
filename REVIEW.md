# M1 Independent Review Request

review_target:
FJ899/MP branch audit/m1-repo-suitability-v2

review_subject:
M1 — Technology Reconnaissance + Repository Suitability Audit

candidate_status:
READY_FOR_INDEPENDENT_REVIEW

## Review inputs

Primary:
- STATE.md
- M1_RESULT.md
- M2_SMOKE_TEST_PLAN.md
- AUDIT_MATRIX.md
- SOURCES.md
- research/PINNED_SOURCES.md
- research/SEARCH_LOG.md
- research/REPO_RADAR.md
- research/COMPONENT_CANDIDATES.md
- research/ARCHITECTURE_REFERENCES.md

Component audits:
- audits/video-ingestion.md
- audits/quality-gate.md
- audits/anomalib-patchcore.md
- audits/detector-selection.md
- audits/sahi.md
- audits/segmentation-tracking.md
- audits/merger-temporal.md
- audits/recheck-recollection.md
- audits/hawk-i.md
- audits/unresolved.md

Governance:
Research Gate technical repair is already HUMAN-ACCEPTED in its reviewed scope. Do not reopen that review unless the M1 changes introduce a new contradiction.

## Required review questions

### RQ-01 Goal alignment
Does M1 remain centered on:
post-flight inspection material → limited evidence-backed CONFIRM / REJECT / RECHECK candidates?

### RQ-02 Search sufficiency
Are Vertical + Horizontal searches broad enough for the current decision surface, or is a materially important class of existing solution missing?

Do not demand exhaustive repository collection merely for completeness.

### RQ-03 Search-to-backlog effect
Did reconnaissance actually remove/postpone unnecessary custom work?

Check specifically:
- custom ingestion,
- custom image-quality model,
- custom mask tracker,
- generic box fusion,
- generic tracker,
- telemetry parser,
- KMZ generator.

### RQ-04 Source identity
Are serious source claims pinned to exact commits or explicitly UNRESOLVED?

### RQ-05 Evidence discipline
Are SOURCE_INSPECTED, reported upstream execution, and MP execution kept distinct?

M1 has not run the proposed M2 components.

### RQ-06 Licensing
Are code, dataset and model/checkpoint licenses separated correctly?
Flag any place where UNKNOWN/PENDING was silently treated as permission.

Pay special attention to:
- FFmpeg build configuration,
- PatchCore pretrained backbone,
- BFD-UAV2K,
- Cutie pretrained model,
- IIQC,
- Hawk-I/AegisInspect/reference repos,
- Ultralytics code vs defect weights.

### RQ-07 Ingestion choice
Is FFmpeg/OpenCV a justified minimal first smoke candidate after inspecting PySceneDetect/PyAV/VidGear?

### RQ-08 Quality gate
Is BRISQUE appropriately treated as one test signal rather than a complete gate?
Is IIQC correctly LEARN rather than runtime dependency?

### RQ-09 Anomaly
Is PatchCore correctly scoped as anomaly ranking requiring normal-reference material, not crack detection?

### RQ-10 Detector path
Is the known-defect smoke correctly BLOCKED pending task-relevant checkpoint/license rather than faked using generic YOLO?

### RQ-11 Segmentation/tracking
Is SAM2.1 Small a reasonable cheapest first prompted-persistence smoke after inspecting Cutie/XMem/DEVA/Track-Anything?

### RQ-12 Merger gap
Does the evidence support this decomposition:
- WBF for same-frame geometric fusion,
- Norfair/SAM2 for temporal continuity,
- spatial dedup later,
- MP-specific CandidateEvent semantics still open?

Challenge this if an inspected or obvious missing implementation already solves the complete problem better.

### RQ-13 Recheck boundary
Is it reasonable for first MP RECHECK to remain a human-facing source interval/frame/reason rather than autonomous revisit?

### RQ-14 M2 minimality
Can the seven proposed M2 smoke tests be reduced while still answering the central hypothesis?
If so, identify what can be removed and why.

### RQ-15 M1 DONE coverage
Independently verify D1–D15 in M1_RESULT.md.
Do not accept a criterion merely because AI-A marked it satisfied.

### RQ-16 Architecture freeze
Confirm that M1 review does not itself freeze MP Architecture v0.1.

## Blocking / major finding contract

For each BLOCKING or MAJOR:
- issue_id
- severity
- violated M1 DONE / source / evidence rule
- exact artifact/location
- evidence
- consequence
- minimum correction
- verification method

MINOR/NOTE findings should not silently become new M1 requirements.

## Explicit non-authorization

A PASS review does NOT:
- merge the branch,
- run M2,
- install dependencies,
- train models,
- create implementation adapters,
- freeze MP Architecture v0.1,
- authorize flight/route actions.

After review, HUMAN decides whether to accept M1 result and authorize any next phase.


## Focused repair review — MP-M1-001

Source review:
MP/m1-review-001/AI-B

Verify the following correction only:

1. BRISQUE source code/repository license is recorded separately from its bundled default runtime artifacts.
2. audits/quality-gate.md records:
   - brisque/models/svm.txt,
   - brisque/models/normalize.pickle,
   - constructor loading behavior,
   - artifact provenance/terms = UNRESOLVED.
3. research/PINNED_SOURCES.md and REPO_RADAR.md no longer imply that Apache-2.0 alone resolves the complete default runtime model chain.
4. M2-02 cannot execute with the default BRISQUE model until:
   - bundled artifact provenance/terms are resolved, or
   - a custom model with pinned acceptable provenance/terms is provided.
5. D3 and D5 in M1_RESULT.md are corrected consistently.
6. evidence/M1_RECON_EVIDENCE.md records exact default artifact identities and does not claim either that Apache-2.0 covers them or that it excludes them.

This repair does not require:
- installation,
- training,
- replacing BRISQUE,
- reopening broad reconnaissance,
- M2 execution.

Non-blocking notes N01–N05 remain notes unless they expose a separate violated M1 DONE criterion.
