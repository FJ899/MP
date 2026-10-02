# M2-02B Input Gap Report 002

protocol:
TWO-WEBAI/0.2

project_id:
MP

report_type:
INPUT_GAP_REPORT

proposal:
M2-02B — Natural Quality Relevance Pilot

accepted_plan_subject:
58be2e74fac96858dbf38ef134bc489614a023c4

accepted_plan_decision:
HUMAN-PLAN-DECISION-M2-02B-001

supersedes_availability_report:
M2_02B_INPUT_GAP_REPORT_001.md

execution_authorization:
NOT_GRANTED

metrics:
NOT_RUN

human_labeling:
NOT_RUN

flight_or_new_capture:
NOT_AUTHORIZED / NOT_PERFORMED

## Newly supplied accessible files

All files below are currently accessible as actual bytes.

| File | Size bytes | SHA-256 | Main video |
|---|---:|---|---|
| Air3s_normal.MP4 | 74451639 | cc8ace8fc18280d09318d29f5b7dbcc1b7b44d986c2d83035d4421e0d927bcaa | HEVC 3840x2160 30000/1001 fps |
| Air3s_D-logM.MP4 | 127519330 | bd36586cb49e40566ce83bbff31e96c88c3578d880125b24bfbf40fa43e81330 | HEVC 3840x2160 30000/1001 fps |
| Air3s_HLG.MP4 | 162357067 | fb59b43c961c36aa897d7dc67d455ff99271a154b1ee368d1d3fdd12c788b87f | HEVC 3840x2160 30000/1001 fps |
| Coler_D-LogM_24mm.MP4 | 191787467 | ab84eba120518d2989471bcf1562da74d09af00a8964c262cd356cb7c07e785e | HEVC 3840x2160 60000/1001 fps |
| Coler_D-LogM_70mm.MP4 | 193194428 | 3b569dfa71a81ec4618d3ad290c91bdf8fea851d6e99930979592397880c97a6 | HEVC 3840x2160 60000/1001 fps |
| Coler_HDR.MP4 | 188664845 | 31bcc92de48b22b32f95187dc1940557f21821fedee0f9f82db2c7ce11338fcf | HEVC 3840x2160 60000/1001 fps |
| Slow_24mm_4K120fps.MP4 | 289931570 | 7af1a2f285491b958314b209cd9f59720654fd7a8a4aea85cc9b9e21fd5d99d9 | HEVC 3840x2160; playback stream 30000/1001 fps; time_base 1/120000 |
| Slow_70mm_4K120fps.MP4 | 295050094 | a2504fec6b4720ed7a4cbbbd52d65a0789ca085abb6c80a1f3e97d40f00c6a40 | HEVC 3840x2160; playback stream 30000/1001 fps; time_base 1/120000 |

Embedded strings in all eight files include identifiers supporting DJI Air 3S identity, including dvtm_Air3s.proto and DJI Air3s / DJI FC9113 markers where present.

Boundary:
this supports file/sample identity only.
It is not an independent untouched-camera-original chain-of-custody proof.

## Timing / metadata observations

Air3s_normal:
- creation_time 2024-10-14T03:48:53Z from prior accepted M2-01 evidence
- duration 11.244567 s

Air3s_D-logM:
- creation_time 2024-10-14T03:49:16Z
- duration 12.746067 s
- 382 main video frames

Air3s_HLG:
- creation_time 2024-10-14T03:49:40Z
- duration 16.182833 s
- 485 main video frames

Coler_HDR:
- creation_time 2024-10-10T07:37:41Z
- duration 15.799117 s
- 947 main video frames

Coler_D-LogM_24mm:
- creation_time 2024-10-10T07:38:00Z
- duration 16.032683 s
- 961 main video frames

Slow_24mm_4K120fps:
- creation_time 2024-10-10T07:38:24Z
- duration 62.562500 s
- 1875 main video frames

Slow_70mm_4K120fps:
- creation_time 2024-10-10T07:38:45Z
- duration 63.763700 s
- 1911 main video frames

Coler_D-LogM_70mm:
- creation_time 2024-10-10T07:39:10Z
- duration 16.182833 s
- 970 main video frames

These timestamps and filenames make candidate grouping plausible, but do not establish degradation condition or final matched admission.

## Non-formal visual availability preview

For availability grouping only, the embedded 960x540 MJPEG preview stream was inspected.

Important:
- these previews are NOT M2-02B selected midpoint frames;
- no formal scene contract was created;
- no matched_group_admission was run;
- no HUMAN usability label was collected;
- no metric was calculated.

Observed candidate scene clusters:

### Candidate cluster A — indoor room

Files:
- Air3s_normal.MP4
- Air3s_D-logM.MP4
- Air3s_HLG.MP4

Embedded previews show the same indoor room from closely similar framing.

Potential comparability:
PROMISING / UNVERIFIED.

Condition status:
- recording-profile differences are visible/declared;
- REF / NAT_BLUR / NAT_DARK / NAT_BRIGHT roles are NOT VERIFIED.

Important:
Normal / D-LogM / HLG are capture/profile labels, not natural degradation labels.

Current count:
3 candidate captures for this scene, not the required four verified conditions.

### Candidate cluster B — waterfall wide / approximately 24 mm family

Files:
- Coler_D-LogM_24mm.MP4
- Coler_HDR.MP4
- Slow_24mm_4K120fps.MP4

Embedded previews show the same waterfall subject with broadly comparable wide framing.

Potential comparability:
PROMISING / UNVERIFIED.

Condition status:
REF / NAT_BLUR / NAT_DARK / NAT_BRIGHT NOT VERIFIED.

Important:
- D-LogM is not NAT_DARK by definition;
- HDR is not NAT_BRIGHT by definition;
- 4K120fps / slow playback is not NAT_BLUR by definition.

Current count:
3 candidate captures for this approximate scale family, not four verified conditions.

### Candidate cluster C — waterfall tele / approximately 70 mm family

Files:
- Coler_D-LogM_70mm.MP4
- Slow_70mm_4K120fps.MP4

Embedded previews show the same waterfall at a much tighter visual scale than the wide family.

Potential comparability:
PROMISING WITHIN 70 mm PAIR / UNVERIFIED.

Cross-comparison against 24 mm files:
NOT SAFE TO ASSUME because visual scale differs materially.

Condition status:
REF / NAT_BLUR / NAT_DARK / NAT_BRIGHT NOT VERIFIED.

Current count:
2 candidate captures.

## Updated availability matrix

This matrix records candidate file availability only.
It does not assign degradation truth.

| Candidate scene family | REF candidate | NAT_BLUR candidate | NAT_DARK candidate | NAT_BRIGHT candidate | Potential comparability |
|---|---|---|---|---|---|
| S1 indoor | AVAILABLE candidates exist, role unverified | CONDITION_NOT_VERIFIED | CONDITION_NOT_VERIFIED | CONDITION_NOT_VERIFIED | PROMISING / needs midpoint-frame scene contract |
| S2 waterfall wide ~24 mm | AVAILABLE candidates exist, role unverified | CONDITION_NOT_VERIFIED | CONDITION_NOT_VERIFIED | CONDITION_NOT_VERIFIED | PROMISING / needs midpoint-frame scene contract |
| S3 waterfall tele ~70 mm | AVAILABLE candidates exist, role unverified | CONDITION_NOT_VERIFIED | CONDITION_NOT_VERIFIED | CONDITION_NOT_VERIFIED | PARTIAL ONLY / only 2 candidate files |

This is intentionally not a one-file-per-condition assignment.

## Readiness decision

accessible_native_video_count:
8

complete four-condition verified matched groups:
0

verified REF conditions:
0

verified NAT_BLUR conditions:
0

verified NAT_DARK conditions:
0

verified NAT_BRIGHT conditions:
0

matched_group_admission:
NOT_RUN

human_labels:
NOT_RUN

metrics:
NOT_RUN

INPUT_READINESS:
NO

INPUT_GAP:
YES

M2-02B remains:
NOT_STARTED / BLOCKED_BY_INPUT.

## Why readiness is still NO

The new uploads solve the previous file-availability gap substantially, but not the experimental-condition gap.

M2-02B requires actual natural quality contrast relative to one inspection task.

Current filenames/profile modes establish candidate captures, not:
- natural blur,
- natural underexposure,
- natural overexposure,
- usable reference,
- or comparable midpoint-frame admission.

At least one complete candidate scene would need four actual roles established before M2-02B could be considered input-ready.

The accepted plan asks for three scene groups.

## What this report does NOT conclude

It does NOT conclude:
- that any of these files are unsuitable;
- that D-LogM/HLG/HDR/120fps cannot contain a useful natural quality difference;
- that the required degradation is absent inside the clips;
- that new footage is necessary;
- that 24 mm and 70 mm footage can be mixed in one matched group.

It concludes only:
the complete three-scene M2-02B input contract is not yet established from the currently accessible files.

## Next decision hinge

Before any M2-02B execution authorization, HUMAN may decide whether AI-A should perform a separate, explicitly scoped INPUT_CLASSIFICATION_PRECHECK on the existing eight clips.

Such a precheck could inspect content only to determine whether any clips/segments plausibly contain:
- natural blur,
- natural dark exposure,
- natural bright/clipped exposure,
- usable reference,
while preserving the rule that this is not metric calculation or HUMAN usability labeling.

That precheck is NOT authorized by this report.

Alternatively HUMAN may:
- provide additional already existing footage;
- identify known segments/conditions in these files;
- defer M2-02B.

No flight or new recording is authorized.

## Preserved non-authorizations

- M2-02B execution
- formal midpoint-frame selection for the experiment
- scene admission
- HUMAN labeling
- metric calculation
- flight
- new recording
- BRISQUE
- dependency installation
- pretrained models
- training
- production thresholds
- quality gate
- M2-03+
- BUILD orchestrator
- merge
- architecture freeze
- publish/release/deploy
