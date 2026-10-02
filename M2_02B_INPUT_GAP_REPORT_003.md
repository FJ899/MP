# M2-02B INPUT_CLASSIFICATION_PRECHECK — INPUT_GAP_REPORT

protocol: TWO-WEBAI/0.2
project_id: MP
precheck_id: M2-02B-INPUT-CLASSIFICATION-PRECHECK-20261002-001
authorization: HUMAN-M2-02B-INPUT-CLASSIFICATION-PRECHECK-AUTH-001
authorization_context_subject: ea3ffdd425197762490dca4cbcfbdcf85bf5c305
status: COMPLETED / INPUT_GAP_REMAINS
m2_02b_execution: NOT_STARTED / NOT_AUTHORIZED
metrics: NOT_RUN
human_quality_labels: NOT_RUN
formal_matched_group_admission: NOT_RUN
formal_experiment_midpoint_selection: NOT_RUN
new_capture_or_flight: NOT_RUN

## Scope actually checked

Already accessible/mounted material only.

Native MP4 inventory:
- Air3s_normal.MP4
- Air3s_D-logM.MP4
- Air3s_HLG.MP4
- Air3s_D-logM(1).MP4
- Coler_normal.MP4
- Coler_HDR.MP4
- Coler_D-LogM_24mm.MP4
- Coler_D-LogM_70mm.MP4
- Slow_24mm_4K120fps.MP4
- Slow_70mm_4K120fps.MP4

Associated still/raw inventory:
- 9 mounted DNG paths, representing 7 unique SHA-256 objects because two pairs are byte-identical duplicates;
- 72 bd_img_* bridge-inspection stills.

No web acquisition, flight, new recording, installation, metric calculation or HUMAN quality labeling was performed.

## Precheck method

For each of the 10 native MP4 files:
- SHA-256 and basic ffprobe identity were recorded;
- representative preview frames were extracted at fixed 10%, 25%, 50%, 75% and 90% positions of container duration;
- selection was fixed by position only and was not based on any quality metric;
- previews were used only to classify scene family and plausible condition availability.

These previews are NOT M2-02B formal midpoint frames and do NOT constitute matched-group admission or HUMAN labeling.

## Candidate scene clusters

### P1 — indoor room / wide view

Files:
- Air3s_normal.MP4
- Air3s_D-logM.MP4
- Air3s_HLG.MP4

Scene relationship:
PROMISING / UNVERIFIED.

REF:
AVAILABLE AS CANDIDATE — Air3s_normal.MP4 is a plausible reference candidate, but the formal REF role is not established.

NAT_BLUR:
NOT ESTABLISHED.
No plausible capture-blur candidate was observed in the fixed representative samples.
This does not prove that no blurred frame exists elsewhere in the files.

NAT_DARK:
NOT ESTABLISHED.
Visible tonal differences exist between Normal / D-LogM / HLG, but these are recording-profile variants, not a verified natural underexposure family.

NAT_BRIGHT:
NOT ESTABLISHED.
Visible tonal differences exist, but none is verified as a naturally overexposed/bright degradation case under the M2-02B contract.

Complete four-condition set:
NO.

### P2 — waterfall / wide approximately 24 mm

Files:
- Coler_normal.MP4
- Coler_HDR.MP4
- Coler_D-LogM_24mm.MP4
- Slow_24mm_4K120fps.MP4

Scene relationship:
PROMISING / UNVERIFIED.

REF:
AVAILABLE AS CANDIDATE — Coler_normal.MP4 is the strongest current reference candidate for this cluster.

NAT_BLUR:
NOT ESTABLISHED.
The waterfall contains moving water, but representative samples do not establish camera/capture blur that degrades the same inspection detail.
Slow_24mm cannot be called NAT_BLUR merely from recording-rate mode or moving-water content.

NAT_DARK:
NOT ESTABLISHED.
Coler_normal appears tonally darker than some profile variants in representative previews, but the difference is confounded by Normal / HDR / D-LogM / slow-motion recording modes.

NAT_BRIGHT:
NOT ESTABLISHED.
HDR / D-LogM / Slow material may appear tonally different, but no file is verified as a naturally overexposed degradation capture.

Complete four-condition set:
NO.

### P3 — waterfall / tele approximately 70 mm

Files:
- Coler_D-LogM_70mm.MP4
- Slow_70mm_4K120fps.MP4

Scene relationship:
PARTIAL / UNVERIFIED.

REF:
NOT ESTABLISHED.

NAT_BLUR:
NOT ESTABLISHED in representative samples.

NAT_DARK:
NOT ESTABLISHED.

NAT_BRIGHT:
NOT ESTABLISHED.

Complete four-condition set:
NO.

### P4 — landscape / hills

File:
- Air3s_D-logM(1).MP4

Scene relationship:
SINGLETON.

REF / NAT_BLUR / NAT_DARK / NAT_BRIGHT:
NOT ESTABLISHED.

Complete four-condition set:
NO.

## M2-02B availability matrix

| precheck scene | REF | NAT_BLUR | NAT_DARK | NAT_BRIGHT | current interpretation |
|---|---|---|---|---|---|
| P1 indoor | candidate available / unverified | not established | not established; profile confounder | not established; profile confounder | incomplete |
| P2 waterfall 24 mm | strongest candidate available / unverified | not established | not established; profile/mode confounder | not established; profile/mode confounder | incomplete |
| P3 waterfall 70 mm | not established | not established | not established | not established | incomplete |
| P4 landscape | not established | not established | not established | not established | singleton |

Verified complete four-condition matched groups:
0

Plausible complete four-condition matched groups from the checked representative samples:
0

## Associated DNG material

The DNG material is useful, but it does not satisfy the accepted M2-02B native-video input contract.

Checked metadata confirms DJI camera families FC9113 / FC9184.
Observed capture contrasts include:
- ISO 100 wide and tele material;
- ISO 1600 tele material;
- ISO 3200 wide material;
- 24 mm and 70 mm focal-length equivalents;
- 12 MP / 48 MP / 50 MP named capture variants.

Two duplicate pairs were detected by exact SHA-256:
- air 3s 3x 12 megapixel raw.DNG == air 3s 3x 12 megapixel raw (1).DNG;
- air 3s high iso 3x 12 megapixels.DNG == air 3s high iso 3x 12 megapixels(1).DNG.

Interpretation:
HIGH VALUE FOR A SEPARATE FUTURE ROBUSTNESS / DETAIL-VISIBILITY TEST.
NOT AN M2-02B SUBSTITUTE.

## Bridge-inspection stills

72 bd_img_* files are mounted.
Their dimensions span 1600x1200, 1920x1440, 2048x1080, 2048x1152 and 2048x1536.
Only 3 expose camera EXIF in the current inspection and identify a Canon PowerShot SD1000; most do not provide camera identity through the inspected metadata.

They are visually relevant to bridge/structural inspection content, but are not verified native Air 3S video and therefore do not close M2-02B input requirements.

Potential future value:
defect/anomaly/segmentation challenge material, subject to provenance and dataset-use checks before any formal use.

## Result

report_type:
INPUT_GAP_REPORT

input_readiness_for_M2_02B:
NO

blocking_gap:
No checked cluster supplies a verified REF / NAT_BLUR / NAT_DARK / NAT_BRIGHT set for the same physical scene/task.

most_important_missing_condition:
NAT_BLUR is not plausibly established in the representative samples for any current cluster.

additional_missing_conditions:
verified NAT_DARK and NAT_BRIGHT captures are also absent; current tonal differences are confounded by recording profile/mode.

## Boundary

This precheck does NOT establish that suitable segments do not exist somewhere else inside the checked clips.
It establishes only that the fixed representative samples do not provide enough evidence to declare a complete candidate set.

No search was made outside already accessible material.
"Not established in checked samples" must not be rewritten as "does not exist".

## Stop condition

The authorized INPUT_CLASSIFICATION_PRECHECK is complete.
Stop here.

M2-02B remains:
NOT_STARTED / NOT_AUTHORIZED / BLOCKED_BY_INPUT.

A later HUMAN decision is required before any of:
- deeper condition-specific segment search;
- formal scene contracts/admission;
- HUMAN labeling;
- M2-02B execution;
- new recording/flight;
- a separate robustness/detail experiment using the DNG material.
