# Next Experiment Proposal — M2-02B Natural Quality Relevance Pilot

status:
PROPOSED_FOR_REVIEW_AND_HUMAN_DECISION

experiment_id:
M2-02B

execution_authorization:
NOT_GRANTED

input_status:
NOT_STARTED / BLOCKED_BY_INPUT until a complete natural-capture set is supplied.

dependency_installation:
NOT_REQUIRED / NOT_AUTHORIZED

flight_or_capture_execution:
NOT_INCLUDED / NOT_AUTHORIZED

architecture_freeze:
NOT_AUTHORIZED

## Why this is the next smallest valuable experiment

M2-02A established only that four model-free measurements are deterministic and respond in the expected direction to frozen synthetic stress transforms.

The next uncertainty is materially different:

Do the same signals agree with HUMAN inspection-usability judgments on naturally captured Air 3S degradation, when scene content is controlled by matched captures?

This is the first proposed step from:
"the metric mathematically reacts"

toward:
"the signal may be relevant to the operator."

It is still a pilot.
It does not establish a production threshold or a quality gate.

## Explicit non-goals

M2-02B does NOT test:
- BRISQUE;
- anomaly detection;
- defect detection;
- CandidateEvent semantics;
- end-to-end MP;
- production thresholds;
- automatic ACCEPT/REJECT/RECHECK decisions;
- a statistically representative Air 3S population.

## Why matched natural captures are required

Laplacian variance and brightness-related measurements depend strongly on scene content.

Comparing unrelated frames could confuse:
- texture/detail differences,
- facade color,
- sky proportion,
- viewpoint,
- shadows,

with actual capture quality.

Therefore the smallest useful natural test uses matched scene groups.

## Required input material

A complete execution set requires three scene groups:

S1
S2
S3

For each scene group, provide four native Air 3S video clips or clearly pre-declared non-overlapping native-video segments representing:

1. REF
   A visibly usable reference capture of the same subject/viewpoint family.

2. NAT_BLUR
   A naturally captured blur case produced in-camera during acquisition.
   No synthetic blur or post-processing.

3. NAT_DARK
   A naturally underexposed/dark capture produced in-camera.
   No post-processing.

4. NAT_BRIGHT
   A naturally overexposed/bright capture produced in-camera.
   No post-processing.

Target:
3 scenes × 4 conditions = 12 target frames.

The three scene groups should use different physical scene content where practical, while each four-condition group should remain closely matched in subject and viewpoint.

Preferred:
- same Air 3S recording profile within a scene group;
- same resolution and codec across the full pilot when practical;
- native unedited MP4;
- no social-media/export/transcode copy.

## Input boundary

No reviewed natural-degradation dataset is assumed to exist now.

Until all three scene groups are supplied and pass input checks:

execution_status:
NOT_STARTED / BLOCKED_BY_INPUT

Missing input before execution is NOT an INCONCLUSIVE experiment result.

This proposal does not authorize a flight, route, or new data-acquisition operation.

HUMAN may:
- supply suitable existing native footage;
- or separately decide later whether acquisition should be authorized.

## Deterministic frame selection

Metric-driven frame selection is forbidden.

For each supplied condition clip/segment:

1. Establish the usable declared segment before metrics are calculated.
2. Bind the source file by SHA-256.
3. Enumerate frames using the accepted M2-01 provenance method.
4. Select the frame nearest the temporal midpoint of the declared segment.
5. Use the same deterministic nearest-frame/tie rules as M2-01.
6. Record exact:
   - source SHA-256,
   - stream index,
   - enumeration ordinal,
   - raw PTS,
   - time_base,
   - RGB24 SHA-256.

No frame may be replaced after viewing metric values.

If the midpoint frame is technically undecodable or the declared segment is invalid, diagnose before proceeding.
Do not search nearby frames for a more favorable metric outcome.

## HUMAN quality judgment

HUMAN labels must be frozen BEFORE metric calculation is revealed.

The 12 selected frames are presented to HUMAN under deterministic masked IDs:

Q01 ... Q12

The visible review must not expose:
- REF / NAT_BLUR / NAT_DARK / NAT_BRIGHT labels;
- metric values;
- metric-derived ranking.

The mapping from Q-ID to source condition is preserved in evidence but hidden during labeling.

### HUMAN question

For each frame:

"Is there enough visible inspection detail in this frame to judge the observed surface without needing a better frame from the same location?"

Required quality label:

USABLE
- enough detail for inspection from this frame.

BORDERLINE
- partially usable, but adjacent/better imagery would be preferred before relying on it.

UNUSABLE
- insufficient for inspection; a better frame or reacquisition would be needed.

Required primary reason:

NONE
BLUR
TOO_DARK
TOO_BRIGHT_OR_CLIPPED
OTHER
UNSURE

Optional confidence:

LOW
MEDIUM
HIGH

HUMAN is not asked to predict metric values.

## Frozen HUMAN label evidence

Before any metric-result comparison:

save:
human_labels_v1.csv

record:
human_labels_v1_sha256

After the label file is frozen:
- do not silently alter labels;
- any HUMAN relabeling must create a new explicit version and invalidate the prior analysis candidate rather than overwrite it.

## Pair construction

Within each scene group:

REF vs NAT_BLUR
REF vs NAT_DARK
REF vs NAT_BRIGHT

This creates:

3 blur pairs
3 dark pairs
3 bright pairs

Total:
9 matched comparisons.

Define ordinal usability score only for pair analysis:

USABLE = 2
BORDERLINE = 1
UNUSABLE = 0

The score is an analysis encoding only.
It is not a production threshold.

## HUMAN exercise rule

A pair is HUMAN_EXERCISED for its intended degradation only when:

1. HUMAN usability score(REF) > usability score(DEGRADED)

AND

2. HUMAN primary reason on the degraded frame matches the intended family:

NAT_BLUR:
BLUR

NAT_DARK:
TOO_DARK

NAT_BRIGHT:
TOO_BRIGHT_OR_CLIPPED

If the HUMAN scores are equal, REF is worse, or the reason does not match:

record:
HUMAN_DEGRADATION_NOT_EXERCISED

That pair does NOT count as evidence against the metric.

Do not relabel or select another frame after metric inspection to manufacture an exercised pair.

## Metrics

Use the same model-free measurements as M2-02A.

Runtime candidate:
- existing OpenCV;
- existing NumPy;
- FFmpeg/ffprobe only for source/frame provenance.

No new installation.
No pretrained model.

### blur primary signal

laplacian_variance

Expected pair direction when HUMAN_EXERCISED:

laplacian_variance(NAT_BLUR)
<
laplacian_variance(REF)

### dark primary signal

mean_gray_intensity

Expected pair direction when HUMAN_EXERCISED:

mean_gray_intensity(NAT_DARK)
<
mean_gray_intensity(REF)

### bright primary signal

mean_gray_intensity

Expected pair direction when HUMAN_EXERCISED:

mean_gray_intensity(NAT_BRIGHT)
>
mean_gray_intensity(REF)

### supporting clipping observations

For NAT_DARK:
record black_count / black_fraction.

For NAT_BRIGHT:
record white_count / white_fraction.

These clipping fractions are observational support in M2-02B.

They are NOT required to increase for PASS because natural under/overexposure may degrade usability without pushing grayscale values into the <=5 or >=250 categories.

Record whether each supporting clipping response:
- INCREASED,
- EQUAL,
- DECREASED.

Do not promote clipping fractions to a production criterion.

## Reproducibility

Metric calculation is performed twice:

Run A
Run B

for all 12 selected natural frames.

Required:
- source/frame identity equal;
- RGB24 SHA-256 equal;
- metric values equal under the recorded runtime;
- exact command invocation preserved;
- relevant stdout/stderr preserved;
- exit status preserved;
- script identity preserved if a transient script is used;
- runtime identity preserved.

This explicitly carries forward the evidence-practice correction from M2-02A review.

## Per-family support result

A degradation family is interpretable only if at least:

2 of its 3 matched pairs

are HUMAN_EXERCISED.

If fewer than 2 are exercised:

family_result:
INCONCLUSIVE

because the natural input did not provide enough HUMAN-confirmed examples of that degradation.

For an interpretable family:

SUPPORTED:
the primary metric moves in the expected direction in at least two-thirds of HUMAN_EXERCISED pairs.

NOT_SUPPORTED:
the primary metric fails the expected direction in more than one-third of HUMAN_EXERCISED pairs.

With exactly 2 exercised pairs:
SUPPORTED requires 2/2 directional agreement.

With 3 exercised pairs:
SUPPORTED requires at least 2/3.

This is a pilot continuation criterion, not a statistical validation claim.

## Overall result

PASS:
- provenance/reproducibility PASS;
- BLUR family SUPPORTED;
- DARK family SUPPORTED;
- BRIGHT family SUPPORTED.

FAIL:
- provenance/reproducibility is technically valid;
- at least one family is interpretable and NOT_SUPPORTED.

If one family is NOT_SUPPORTED and another is INCONCLUSIVE:
overall remains FAIL for the full three-family hypothesis, with family-level results preserved.

INCONCLUSIVE:
- provenance/reproducibility is valid;
- no family is NOT_SUPPORTED;
- but at least one required family is INCONCLUSIVE because insufficient HUMAN-confirmed natural degradation was exercised.

Procedure/input/runtime failures after an authorized start may also produce INCONCLUSIVE if fair interpretation cannot be completed.

## Interpretation boundary

PASS would mean only:

On this small matched natural-capture pilot, the selected primary signals usually moved in the same direction as HUMAN inspection-usability judgments for the three tested degradation families.

PASS would NOT establish:
- a production threshold;
- population-level accuracy;
- false-positive/false-negative rates;
- automatic operator replacement;
- final quality-gate design;
- universal Air 3S behavior.

FAIL would mean only:

At least one tested signal family did not show enough directional agreement with HUMAN judgments in this pilot to justify treating that signal as supported without further explanation or an alternative method.

FAIL would NOT authorize a custom quality model.

INCONCLUSIVE would mean:

The supplied natural material or executed evidence did not exercise enough HUMAN-confirmed examples to resolve the full pilot.

## Decision impact

If PASS:
do not build a gate automatically.

The next decision may be whether a slightly larger naturally captured sample is worth collecting to estimate useful thresholds / error tradeoffs.

If FAIL:
do not tune thresholds post hoc.

First inspect:
- scene-content confounding;
- whether the primary metric is the wrong signal;
- whether another already-existing metric should be compared;
- whether BRISQUE provenance/terms is worth resolving.

If INCONCLUSIVE:
do not manufacture synthetic replacements.
Decide whether obtaining better natural examples is worth the acquisition cost.

## Proposed evidence package

After separate authorization and once complete input exists:

evidence/m2-02b/<experiment-id>/

- README.md
- input_manifest.csv
- source_identity.txt
- environment.txt
- exact_commands.txt
- command_statuses.txt
- relevant_stdout_stderr/
- frame_selection.csv
- masked_review_order.csv
- human_labels_v1.csv
- human_labels_v1_sha256.txt
- metrics_runA.csv
- metrics_runB.csv
- pair_analysis.csv
- script_identity.txt
- RESULT.md

Do not reconstruct missing historical commands from memory.

## Cost

Paid API:
NONE.

GPU:
NONE.

New dependency installation:
NONE.

Training:
NONE.

Main cost:
- obtaining suitable natural input if it does not already exist;
- one HUMAN blind review of 12 frames;
- small CPU-only metric pass.

## Authorization requested if review passes

### AUTHORIZE_M2_02B

Would authorize only:
- validation of already supplied native input clips/segments;
- deterministic midpoint-frame selection;
- creation of the 12-frame masked HUMAN review set;
- collection and freezing of HUMAN quality labels;
- two repeated calculations of the same four model-free metrics;
- matched-pair directional analysis;
- compact evidence package;
- PASS / FAIL / INCONCLUSIVE result.

Would NOT authorize:
- flying or recording new footage;
- BRISQUE;
- dependency installation;
- pretrained models;
- training;
- production threshold selection;
- quality-gate implementation;
- M2-03+;
- BUILD orchestrator;
- merge;
- architecture freeze;
- publish/release/deploy.

### ACCEPT_PLAN_ONLY

Accept plan but keep execution unauthorized.

### REQUEST_CHANGES

Return changes.

### DEFER

Do not proceed.

## Current status

proposal:
READY_FOR_REVIEW

execution:
NOT_STARTED

execution_authorization:
NOT_GRANTED

input:
NOT YET ESTABLISHED

BRISQUE:
BLOCKED_BY_MODEL_ARTIFACT_TERMS

No M2-02B command has been executed.
