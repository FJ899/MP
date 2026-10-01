# M2-01 Execution Proposal — Video Timestamp Integrity

status:
HUMAN_DECISION_REQUIRED

experiment_id:
M2-01

execution_authorization:
NOT_GRANTED

implementation_authorization:
NOT_GRANTED

dependency_installation:
NOT_REQUIRED / NOT_AUTHORIZED

architecture_freeze:
NOT_AUTHORIZED

## Decision purpose

Determine whether a native DJI Air 3S MP4 can be mapped reproducibly from:

source file
→ video stream/timebase
→ presentation timestamps
→ selected frame identity

so a later CandidateEvent can point back to evidence a human can RECHECK.

This experiment intentionally does NOT test:
- defect detection,
- BRISQUE,
- PatchCore,
- SAM2,
- WBF,
- Norfair,
- telemetry,
- route planning,
- orchestrator integration.

## Why M2-01 is first

All later visual findings need durable source provenance.

If MP cannot reliably say:

"this observation came from this source video at this presentation time / frame position"

then anomaly scores, masks and CandidateEvents cannot form auditable RECHECK evidence.

M2-01 therefore tests provenance plumbing before model quality.

## Required input

One native, unedited DJI Air 3S MP4:
- target duration: 30–60 seconds,
- original camera file preferred,
- no social-media/export/transcode copy,
- retain original filename and metadata.

Input availability observed during proposal preparation:

Repository FJ899/MP:
NO video file found.

Conversation + Library search:
NO native Air 3S MP4 found.
Search returned documents/reports rather than a relevant video artifact.

INPUT_STATUS:
MISSING.

Consequence:
Air 3S compatibility cannot be tested until a native clip is supplied.

A substitute MP4 may validate the generic measurement procedure only.
It must be labeled GENERIC_PROCEDURE_ONLY and cannot establish Air 3S compatibility.

## Available execution environment

Observed without installation:

### FFmpeg

binary version:
7.1.5-0+deb13u1

build:
Debian package; reports --enable-gpl.

Use in experiment:
decode selected video stream and extract deterministic selected frames.

Important identity boundary:
this installed binary is not assumed byte/source-identical to the FFmpeg commit pinned during M1 reconnaissance.

The experiment evidence must record the actual binary version/configuration used.

### FFprobe

version:
7.1.5-0+deb13u1

Use:
stream metadata and per-frame timestamp/PTS inspection.

### Python

version:
3.13.5

Use:
not required for the minimal CLI experiment.
May be used only if HUMAN later authorizes a small evidence-comparison helper.

### OpenCV

version:
4.13.0

Use:
available, but OPTIONAL.
M2-01 does not need OpenCV in the minimal path.

### GPU

not required.

## Installation plan

None.

The minimal proposed execution uses already available:
- ffprobe,
- ffmpeg,
- standard shell hashing/comparison utilities.

If the authorized environment changes before execution, record the new exact tool identities before running.

## Experiment scope

One source file.
One video stream.
Two repeated measurement/extraction runs.

No repository implementation code is required.

No dependency manifest change is required.

No adapter is created.

## Step 0 — Input identity

Record:

- original filename,
- file size,
- SHA-256 of complete input file,
- acquisition/source note: native Air 3S original vs substitute,
- experiment date,
- experiment ID.

Do not commit the source video to Git solely for this experiment unless HUMAN explicitly requests it.

The evidence package can bind to the video by SHA-256.

## Step 1 — Record tool identity

Persist:

- ffmpeg -version output,
- ffprobe -version output,
- exact command lines,
- operating environment note.

This distinguishes:
source-inspection evidence from the exact runtime binary used.

## Step 2 — Probe stream metadata

Use ffprobe to record at minimum:

- video stream index,
- codec name,
- width/height,
- time_base,
- r_frame_rate,
- avg_frame_rate,
- start_time,
- duration,
- frame count if reported,
- format duration,
- metadata/tags relevant to source identity.

Proposed output:

evidence/m2-01/<experiment-id>/stream_metadata.json

## Step 3 — Probe frame presentation timestamps twice

Run the same ffprobe frame enumeration twice.

Record for the selected video stream at minimum:

- ordinal/decode listing position,
- best_effort_timestamp,
- best_effort_timestamp_time,
- pkt_dts when available,
- pkt_dts_time when available,
- picture type where useful.

Outputs:

frames_run1.csv
frames_run2.csv

Purpose:
test whether repeated probing yields the same presentation-time mapping.

## Step 4 — Choose deterministic sample positions

Select five interior sample points based on the observed duration:

- approximately 10%
- approximately 30%
- approximately 50%
- approximately 70%
- approximately 90%

For each point:
choose the nearest frame by presentation timestamp from the recorded frame list.

Record:

- sample ID,
- frame ordinal/index used by the experiment,
- PTS,
- PTS time,
- target percentage/time.

Do not freeze a production sampling cadence.

These five points exist only to test reproducibility.

## Step 5 — Extract selected frames twice

Using the same ffmpeg binary and identical parameters:

Run A:
extract the five selected frames.

Run B:
repeat extraction independently.

For every extracted image record:

- sample ID,
- source frame/PTS mapping,
- image dimensions,
- output filename,
- SHA-256.

Expected:
the same sample selected under the same source and parameters produces byte-identical extracted evidence, or any non-identical behavior is explicitly explained and investigated.

Preferred lossless output:
PNG.

## Step 6 — Compare run evidence

Compare:

### Frame timestamp table
run1 vs run2:
- same number/order of observed frames relevant to the experiment,
- same best-effort PTS values,
- same best-effort PTS times.

### Selected frames
run1 vs run2:
- same selected source positions,
- same dimensions,
- same output SHA-256.

### Ordering
presentation timestamps must not move backwards.

Any duplicates or irregular timing must be preserved as evidence rather than silently normalized away.

## PASS criteria

PASS requires all of the following for a native Air 3S input:

1. input SHA-256 is recorded;
2. the intended video stream is unambiguously identified;
3. stream time_base is available;
4. frame-level presentation timestamps are available for the selected stream;
5. repeated ffprobe runs produce the same relevant timestamp mapping;
6. selected presentation timestamps are monotonic/non-reversing;
7. the five deterministic sample positions map to the same frames/PTS on both runs;
8. repeated extraction with identical parameters produces matching image dimensions and SHA-256 for each sample;
9. every extracted frame can be traced back to:
   source SHA-256 + stream + frame/PTS + extraction parameters;
10. no unexplained timestamp reorder/corruption undermines RECHECK provenance.

PASS means:
the tested Air 3S clip supports a reproducible source→time→frame evidence path in this environment.

PASS does NOT mean:
all Air 3S recording modes/codecs/firmware are compatible.

## FAIL criteria

FAIL if any of the following occurs and cannot be explained as an experiment/configuration error:

- frame-level presentation timestamps cannot be obtained,
- repeated probes produce materially different mappings,
- presentation timestamps reverse unexpectedly,
- the same selected source position maps to different frames across identical runs,
- deterministic repeated extraction produces different image evidence for the same recorded source mapping,
- the source cannot be decoded sufficiently to preserve auditable mapping.

FAIL does not automatically justify custom BUILD.
It triggers diagnosis and comparison of existing alternatives/configuration.

## INCONCLUSIVE criteria

INCONCLUSIVE if:

- no native Air 3S clip is used,
- the file is edited/transcoded and source provenance is uncertain,
- the clip is corrupted/truncated,
- required metadata is missing for reasons that cannot be separated from the supplied file,
- environment identity changes between the two runs,
- a test-procedure defect prevents a fair comparison.

Most important current condition:

NO NATIVE AIR 3S INPUT
→ M2-01 AIR 3S RESULT = INCONCLUSIVE / NOT_EXECUTABLE_AS_INTENDED.

## Evidence package

Proposed location after authorization:

evidence/m2-01/<experiment-id>/

Proposed files:

- README.md
- input_identity.txt
- sha256.txt
- environment.txt
- commands.txt
- stream_metadata.json
- frames_run1.csv
- frames_run2.csv
- selected_samples.csv
- extracted/run1/*.png
- extracted/run2/*.png
- extracted_hashes_run1.txt
- extracted_hashes_run2.txt
- RESULT.md

RESULT.md must state exactly one:

PASS
FAIL
INCONCLUSIVE

and list:
- actual input identity,
- actual tools,
- deviations from proposal,
- observed anomalies,
- limitations.

## Evidence retention boundary

Prefer committing compact evidence:
- metadata,
- commands,
- hashes,
- selected lossless sample frames if acceptable,
- result summary.

Do not automatically commit the full native Air 3S video because of size/privacy/provenance concerns.

Input SHA-256 is sufficient to bind the experiment record to the retained source file.

## Cost

Software/license cost for the proposed experiment:
none expected from the already available toolchain.

Paid API:
none.

GPU:
none.

Additional installation:
none expected.

Repository implementation:
none.

Primary resource cost:
one short native Air 3S clip plus CPU/storage for probing and five lossless frame extracts.

## Risks / limitations

1. One clip proves only the tested recording profile, not all Air 3S modes.
2. FFmpeg installed binary is a Debian GPL-enabled build; this experiment records runtime identity but does not settle later product redistribution/licensing.
3. Frame ordinal and presentation timestamp are distinct concepts; RECHECK provenance should prefer recorded presentation time/timebase rather than assuming frame_number/fps arithmetic is universally exact.
4. Variable-frame-rate or unusual edit-list behavior may require adapting the evidence mapping while still using existing FFmpeg tooling.
5. No telemetry is tested.
6. No model/analyzer behavior is tested.
7. A generic substitute video cannot validate Air 3S compatibility.

## Proposed decision gate after M2-01

If PASS:
propose a minimal reusable Observation source-provenance record and decide whether to continue to M2-02 or M2-03.

If FAIL:
diagnose whether the cause is:
- source-file peculiarity,
- FFmpeg configuration,
- timestamp semantics,
- or need for another existing decoder/API.

Do not BUILD custom ingestion before that comparison.

If INCONCLUSIVE:
obtain a valid native Air 3S source and rerun only M2-01.

## HUMAN decision options

### AUTHORIZE_M2_01
Authorize execution of exactly this experiment after a native Air 3S clip is available.

This authorization would permit:
- probing one supplied native clip,
- extracting five lossless sample frames twice,
- creating the evidence package described above.

It would NOT permit:
- dependency installation,
- repository implementation code,
- M2-02 or later tests,
- model execution/training,
- architecture freeze,
- merge.

### ACCEPT_PLAN_ONLY
Accept the experiment design but do not authorize execution.

### REQUEST_CHANGES
Return requested changes to this experiment design.

### DEFER
Keep M2-01 pending.

## Current recommendation

Because the execution environment is already sufficient but the required native input is missing:

ACCEPT_PLAN_ONLY or AUTHORIZE_M2_01 conditional on supplying a native Air 3S clip are both operationally possible.

Execution must not begin until explicit HUMAN authorization is recorded.
