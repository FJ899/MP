# Next Experiment Proposal — M2-02B Natural Quality Relevance Pilot

status:
REVISION_2 / PROPOSED_FOR_REVIEW_AND_HUMAN_DECISION

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

## Scene contract and matched-group admission

Before HUMAN labeling and before any metric calculation or disclosure, create a frozen scene contract for each S1 / S2 / S3.

Required fields per scene:

- scene_id;
- concrete physical surface/object being inspected;
- inspection_question: the same inspection purpose for REF / NAT_BLUR / NAT_DARK / NAT_BRIGHT;
- detail_type_to_judge: a plain-language description of the type of visual detail whose visibility matters for that inspection question;
- declared source clips/segments for all four conditions;
- relevant visible-content differences between the four selected midpoint frames;
- matched_group_admission:
  - ADMIT
  - INPUT_MATCH_INVALID
- admission_rationale.

A known true defect label is NOT required.

The contract must answer, in practical terms:

"Are all four frames asking the HUMAN to judge the same inspection task on the same physical surface/object at a comparable visual scale?"

### Matched-group admission criteria

ADMIT only when, before metrics are viewed:

1. the same physical surface/object is visible in all four conditions;

2. the same inspection_question applies to all four frames;

3. the same detail_type_to_judge is relevant to all four frames;

4. the visual scale of the detail is comparable enough that a change in HUMAN usability can reasonably be attributed to capture quality rather than a materially different object scale;

5. viewpoint and frame content are comparable enough that the same region/task can be assessed in all four frames;

6. material differences that may affect comparability are explicitly recorded.

No arbitrary numeric geometric tolerance is required for this pilot.

The admission decision is a documented HUMAN/experiment-design control made before metric inspection.

### INPUT_MATCH_INVALID

If the matched-group criteria are not met, record:

INPUT_MATCH_INVALID

This is distinct from:

HUMAN_DEGRADATION_NOT_EXERCISED.

INPUT_MATCH_INVALID means the comparison itself is not interpretable because the scene/task pairing is not sufficiently comparable.

It must NOT:
- count as evidence against the metric;
- count as an ordinary non-exercised degradation;
- be silently replaced after metric inspection by another frame.

If INPUT_MATCH_INVALID is discovered after authorized execution has started:
- preserve the invalidity evidence and rationale;
- exclude the invalid pair/group from directional support counting;
- mark the affected degradation family INCONCLUSIVE if fewer than two valid HUMAN_EXERCISED matched pairs remain;
- preserve all unaffected family sub-results.

Do not select replacement material after metric inspection to manufacture interpretability.

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

Only frames from ADMITTED matched groups enter the HUMAN review set.

### Presentation contract

The HUMAN receives the same inspection-task information for every frame in a given scene:

- scene_id masked from condition identity;
- inspection_question;
- detail_type_to_judge.

The HUMAN may know what inspection task is being judged.

The HUMAN must NOT see:
- REF / NAT_BLUR / NAT_DARK / NAT_BRIGHT condition labels;
- source filenames;
- source folder names or metadata that reveal condition;
- metric values;
- metric-derived ranking.

All frames must be reviewed using the same presentation method:

- same viewer and display/session where practical;
- full-resolution source frame available;
- initial view: full frame fit-to-window;
- allowed detail inspection: native 100% zoom with pan;
- no sharpening, denoise, contrast enhancement, super-resolution or other image enhancement;
- no crop-only presentation that hides context;
- the same zoom/pan capabilities for every reviewed frame.

Record the presentation contract in evidence.

### Masking and order

Before HUMAN labeling:

1. create Q01...Q12 masked IDs;
2. create a fixed permutation independent of metric values;
3. save the Q-ID -> source/condition mapping separately;
4. hide filenames and condition-revealing metadata from the review surface;
5. hash/freeze the masked review order before labels are collected.

The permutation may be generated deterministically from a predeclared seed or by another predeclared method, but it must be fixed before metric results are available.

If HUMAN previously participated in capturing or organizing the source material and may recognize specific clips/scenes:

record:
MASKING_LIMITATION_KNOWN_SOURCE_FAMILIARITY

Do not describe that review as fully blind.

The review remains usable as a masked-condition pilot, with that limitation preserved.

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

## Pair validity before HUMAN exercise

A pair can reach HUMAN_EXERCISED only if its scene contract is:

matched_group_admission = ADMIT

If the pair/group is INPUT_MATCH_INVALID:

pair_status:
INPUT_MATCH_INVALID

Do not evaluate HUMAN_EXERCISED for that pair.

## HUMAN exercise rule

For a valid admitted pair, it is HUMAN_EXERCISED for its intended degradation only when:

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

Use the same model-free measurements and calculation contract as M2-02A revision 2.

Runtime candidate:
- existing OpenCV;
- existing NumPy;
- FFmpeg/ffprobe only for source/frame provenance.

No new installation.
No pretrained model.

### Frozen calculation contract carried from M2-02A revision 2

Source frame:
- RGB24 uint8;
- shape H x W x 3.

Grayscale:
- cv2.cvtColor(rgb_uint8, cv2.COLOR_RGB2GRAY);
- uint8 grayscale intensity, not physical luminance.

Laplacian:
- cv2.Laplacian(
    gray_uint8,
    cv2.CV_64F,
    ksize=1,
    borderType=cv2.BORDER_DEFAULT
  );
- variance computed in float64.

mean_gray_intensity:
- float64 mean of the grayscale image.

black clipping support:
- raw black_count = count(gray <= 5);
- black_fraction = black_count / pixel_count.

white clipping support:
- raw white_count = count(gray >= 250);
- white_fraction = white_count / pixel_count.

Serialization:
- preserve raw integer counts and pixel_count;
- preserve float metrics with stable machine-readable precision sufficient for round-trip comparison in the same recorded runtime.

Any transient script must record its SHA-256 and exact runtime versions.

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

Only pairs that are both:
- matched_group_admission = ADMIT; and
- HUMAN_EXERCISED

may count toward directional family support.

INPUT_MATCH_INVALID pairs never count as metric evidence.

A degradation family is interpretable only if at least:

2 of its 3 planned matched pairs

remain valid and HUMAN_EXERCISED.

If fewer than 2 are exercised:

family_result:
INCONCLUSIVE

because the natural input did not provide enough valid HUMAN-confirmed examples of that degradation.

This can occur because of:
- HUMAN_DEGRADATION_NOT_EXERCISED;
- INPUT_MATCH_INVALID;
- or a mixture of both.

Preserve these causes separately.

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

INPUT_MATCH_INVALID handling:
- if it leaves a family with fewer than two valid HUMAN_EXERCISED pairs, that family is INCONCLUSIVE;
- unaffected families retain their own resolved results.

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
- scene_contracts.csv
- matched_group_admission.csv
- presentation_contract.txt
- masked_review_order.csv
- masked_review_order_sha256.txt
- masking_limitations.txt
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
- creation and freeze of scene contracts and matched-group admission decisions before metrics;
- deterministic midpoint-frame selection;
- creation of a fixed-permutation masked HUMAN review set with filenames/condition cues hidden;
- use of the frozen presentation contract;
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

## Review correction history

Revision 2 incorporates AI-B review MP/m2-02b-proposal-review-001/AI-B.

Resolved finding:
M2-02B-P01 — insufficiently specified input comparability and inspection usefulness.

Revision 2 adds:
- scene-specific inspection_question and detail_type_to_judge;
- explicit matched-group admission before metrics;
- INPUT_MATCH_INVALID distinct from HUMAN_DEGRADATION_NOT_EXERCISED;
- family-level INCONCLUSIVE handling when invalid input prevents enough valid exercised pairs;
- uniform HUMAN presentation contract with full-resolution/native-100% access and no image enhancement;
- fixed pre-label permutation independent of metrics;
- hidden filenames/condition metadata;
- explicit masking limitation when HUMAN knows the source material;
- the exact M2-02A revision-2 RGB24 / RGB2GRAY / Laplacian / float64 / raw-count calculation contract.

No new metric, crop, model or production threshold was added.
