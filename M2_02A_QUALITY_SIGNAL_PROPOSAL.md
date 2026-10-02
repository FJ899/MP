# Next Experiment Proposal — M2-02A Model-Free Quality Signal Sanity Check

status:
PROPOSED_FOR_REVIEW_AND_HUMAN_DECISION

experiment_id:
M2-02A

execution_authorization:
NOT_GRANTED

implementation_authorization:
NOT_GRANTED

dependency_installation:
NOT_REQUIRED / NOT_AUTHORIZED

architecture_freeze:
NOT_AUTHORIZED

## Why this is the next smallest experiment

M2-01 established provenance for one supplied Air 3S sample:

source SHA-256
→ stream
→ decoded-frame ordinal
→ raw PTS/timebase
→ frame pixels
→ saved evidence.

The next smallest uncertainty is not yet:
"Can MP classify production-quality frames?"

It is only:

"Do simple existing, model-free quality signals move in the expected direction under controlled obvious degradation while preserving M2-01 provenance?"

This is a sanity check for candidate quality signals, not a production gate.

## Relation to original M2-02

Original M2-02 proposed BRISQUE as one signal.

That branch remains:

BLOCKED_BY_MODEL_ARTIFACT_TERMS.

Reason:
rehanguha/brisque default execution depends on:
- brisque/models/svm.txt
- brisque/models/normalize.pickle

Their independent provenance/terms remain UNRESOLVED.

M2-02A therefore does NOT execute BRISQUE.

This proposal is an alternative experiment for review.
It does not silently replace or redefine the accepted M2 plan.

## Options compared

### Option A — BRISQUE now

Status:
DEFER / BLOCKED.

Advantages:
- no-reference quality score already exists;
- directly aligned with M1 quality reconnaissance.

Blocking issue:
default SVM and normalization artifact provenance/terms remain unresolved.

Decision:
do not execute under this proposal.

### Option B — model-free classical metrics

Status:
PROPOSED.

Candidate signals:
- variance of Laplacian for blur sensitivity;
- mean grayscale/luma level;
- fraction of grayscale pixels <= 5;
- fraction of grayscale pixels >= 250.

No pretrained model.
No downloaded weights.
No new package installation.

This is the proposed M2-02A path.

### Option C — FFmpeg blurdetect / signalstats

Environment observation:
the available FFmpeg build exposes both filters.

Status:
PARK as secondary alternative.

Reason:
OpenCV/NumPy already provide enough for the smallest paired controlled test.
Adding a second metric implementation in the same smoke test would make interpretation less clean.

## Available environment

Observed during proposal preparation without installing anything:

Python:
3.13.5

opencv-python:
4.13.0.92

OpenCV package license metadata:
Apache-2.0

NumPy:
2.3.5

NumPy installed-package license:
BSD-style core distribution with bundled components separately described in package metadata.

FFmpeg:
available from prior M2-01 execution; not required for metric calculation itself except for exact source-frame extraction if source PNG evidence is not already available.

GPU:
NOT REQUIRED.

Additional installation:
NONE.

## Available input

Available source:
Air3s_normal.MP4

M2-01 source SHA-256:
cc8ace8fc18280d09318d29f5b7dbcc1b7b44d986c2d83035d4421e0d927bcaa

Provenance-anchored M2-01 candidate frames:

p10:
- enumeration ordinal 34
- raw PTS 34034
- PTS time 1.134467 s

p50:
- enumeration ordinal 168
- raw PTS 168168
- PTS time 5.605600 s

p90:
- enumeration ordinal 302
- raw PTS 302302
- PTS time 10.076733 s

These three are proposed only to minimize the experiment while spanning the tested clip.

## Important input gap

We do NOT currently have a reviewed set of naturally:
- motion-blurred,
- defocused,
- severely underexposed,
- severely overexposed

Air 3S inspection frames with human quality labels.

Therefore five M2-01 frames, or the three proposed here, are NOT treated as sufficient real good/bad examples.

M2-02A uses controlled synthetic stress cases only.

PASS cannot establish a production quality threshold or real-world classifier accuracy.

## Controlled degradation design

For each of p10, p50 and p90:

ORIGINAL:
exact provenance-bound source frame from M2-01.

Generate three deterministic derivatives.

### BLUR

Use:

cv2.GaussianBlur(
    image_rgb,
    ksize=(0, 0),
    sigmaX=4.0,
    sigmaY=4.0
)

Purpose:
controlled obvious blur stress.

This is not claimed to simulate every real motion/defocus blur pattern.

### DARK_CLIP

Use uint8-safe deterministic transformation:

    dark = clip(image_rgb.astype(int16) - 96, 0, 255).astype(uint8)

Purpose:
controlled dark/clipped shadow stress.

This is not claimed to reproduce real camera exposure physics.

### BRIGHT_CLIP

Use:

    bright = clip(image_rgb.astype(int16) + 96, 0, 255).astype(uint8)

Purpose:
controlled bright/highlight clipping stress.

This is not claimed to reproduce real camera exposure physics.

## Metric definitions

For each ORIGINAL and each derived image:

Convert exact RGB24 to grayscale with:

    cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

Record:

### laplacian_variance

    var(
      cv2.Laplacian(gray, cv2.CV_64F)
    )

Hypothesis:
BLUR should reduce this value relative to ORIGINAL for the same source frame.

### mean_luma

    mean(gray)

Hypotheses:
DARK_CLIP should reduce it.
BRIGHT_CLIP should increase it.

### black_fraction

    count(gray <= 5) / pixel_count

Hypothesis:
DARK_CLIP should increase it.

### white_fraction

    count(gray >= 250) / pixel_count

Hypothesis:
BRIGHT_CLIP should increase it.

No production threshold is proposed for any metric.

## Minimal execution structure

Three source frames.

Per source frame:
- ORIGINAL
- BLUR
- DARK_CLIP
- BRIGHT_CLIP

Total:
12 image states.

Run the complete deterministic generation + metric calculation twice:

Run A
Run B.

Purpose:
confirm reproducibility of:
- derived RGB24 bytes,
- derived image SHA-256,
- metric outputs.

No model training.
No inference weights.
No network/API.

## Provenance record per result

Every metric row must retain:

- experiment ID,
- run ID,
- source video SHA-256,
- global video stream index,
- source enumeration_ordinal,
- raw PTS,
- time_base,
- source RGB24 SHA-256,
- transform ID:
  - ORIGINAL
  - BLUR_SIGMA4
  - DARK_MINUS96
  - BRIGHT_PLUS96
- exact transform parameters,
- derived RGB24 SHA-256,
- width,
- height,
- OpenCV version,
- NumPy version,
- laplacian_variance,
- mean_luma,
- black_fraction,
- white_fraction.

This preserves:

source
→ exact frame
→ controlled transform
→ quality observation.

## PASS criteria

M2-02A PASS requires all of the following:

### Reproducibility

For all 12 image states:
- Run A derived RGB24 SHA-256 == Run B;
- dimensions match;
- metric values are identical under the recorded runtime/configuration.

### Blur directional sanity

For p10, p50 and p90 independently:

    laplacian_variance(BLUR)
    <
    laplacian_variance(ORIGINAL)

All three pairs must satisfy the direction.

### Dark directional sanity

For each source frame:

    mean_luma(DARK_CLIP)
    <
    mean_luma(ORIGINAL)

and:

    black_fraction(DARK_CLIP)
    >
    black_fraction(ORIGINAL)

All three pairs must satisfy both directions.

### Bright directional sanity

For each source frame:

    mean_luma(BRIGHT_CLIP)
    >
    mean_luma(ORIGINAL)

and:

    white_fraction(BRIGHT_CLIP)
    >
    white_fraction(ORIGINAL)

All three pairs must satisfy both directions.

### Provenance

Every metric row is traceable to M2-01 source/frame identity and exact derived-image hash.

## FAIL criteria

FAIL if a correctly executed controlled test shows that one of the proposed signals does not respond in the intended direction across the required pairs, for example:

- BLUR does not reduce Laplacian variance for one or more selected frames;
- DARK_CLIP does not reduce mean_luma or increase black_fraction;
- BRIGHT_CLIP does not increase mean_luma or white_fraction;
- repeated generation/measurement is not reproducible;
- provenance cannot bind a metric observation to the source frame and transform.

FAIL means:
the affected signal/definition should not automatically proceed as a quality-gate candidate.

FAIL does NOT authorize a custom quality model.

## INCONCLUSIVE criteria

INCONCLUSIVE if the experiment is started but a procedure/input/environment defect prevents fair interpretation, for example:

- source file no longer matches the accepted M2-01 SHA-256;
- exact source frame cannot be reconstructed;
- runtime changes between runs;
- transform implementation is not deterministic due to an execution defect;
- evidence capture fails.

## What PASS would mean

PASS would establish only:

the selected classical metrics are deterministic and directionally sensitive to three deliberately controlled degradation types on three provenance-anchored frames from the tested sample.

PASS would NOT establish:

- real-world Air 3S quality discrimination;
- accepted thresholds;
- false-positive/false-negative performance;
- RECHECK policy;
- production suitability;
- superiority over BRISQUE;
- equivalence to natural motion blur, defocus or exposure failures.

## What happens after PASS

Do not automatically build a gate.

The next decision should be based on whether to obtain a small naturally degraded Air 3S frame set and test these same signals against human-visible quality judgments.

BRISQUE remains separately blocked until its model-artifact condition is resolved.

## What happens after FAIL

Do not build a custom model.

First decide whether:
- the metric definition is not useful;
- a different existing classical metric should be inspected;
- natural examples are needed before judging the signal;
- BRISQUE provenance/terms should be resolved and compared.

## Evidence package proposal

After authorization:

    evidence/m2-02a/<experiment-id>/

Proposed compact files:

- README.md
- input_identity.txt
- environment.txt
- commands_or_transient_script.txt
- source_frames.csv
- transforms.csv
- metrics_runA.csv
- metrics_runB.csv
- derived_hashes_runA.txt
- derived_hashes_runB.txt
- RESULT.md

Do not commit large derivative image sets unless needed for review.
Hashes + exact transform definitions are the primary compact record.

## Cost

Paid API:
none.

GPU:
none.

New dependency installation:
none.

Training:
none.

Expected data volume:
small.

Main cost:
seconds/minutes of CPU work plus review of a 12-state metric table.

## Authorization requested if proposal passes review

### AUTHORIZE_M2_02A

Would authorize exactly:
- reconstruction of p10/p50/p90 source frames from the accepted M2-01 sample;
- creation of the three deterministic synthetic derivatives per frame;
- two repeated calculation runs;
- calculation of the four specified model-free metrics;
- compact evidence package;
- PASS / FAIL / INCONCLUSIVE result.

Would NOT authorize:
- BRISQUE execution,
- dependency installation,
- model training,
- threshold selection,
- quality gate implementation,
- M2-03+,
- merge,
- architecture freeze.

### ACCEPT_PLAN_ONLY

Accept plan but keep execution unauthorized.

### REQUEST_CHANGES

Return changes.

### DEFER

Do not proceed.

## Current recommendation

PROPOSE M2-02A FOR REVIEW.

BRISQUE remains BLOCKED_BY_MODEL_ARTIFACT_TERMS.

No experiment has been executed under this proposal.
