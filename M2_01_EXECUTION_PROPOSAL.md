# M2-01 Execution Proposal — Video Timestamp Integrity

status:
HUMAN_DECISION_REQUIRED

proposal_revision:
2

experiment_id:
M2-01

execution_status:
NOT_STARTED / BLOCKED_BY_INPUT

execution_authorization:
NOT_GRANTED

implementation_authorization:
NOT_GRANTED

dependency_installation:
NOT_REQUIRED / NOT_AUTHORIZED

architecture_freeze:
NOT_AUTHORIZED

## Decision purpose

Determine whether one native DJI Air 3S MP4 can be mapped reproducibly from:

source file
→ exact video stream
→ decoded-frame enumeration
→ presentation timestamp identity
→ selected decoded pixels
→ human-reviewable evidence

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

## Current status before execution

Required native Air 3S input:
MISSING.

Therefore current experiment status is:

NOT_STARTED / BLOCKED_BY_INPUT.

INCONCLUSIVE is reserved for an experiment that was actually started but could not produce a decisive PASS or FAIL.

No M2 command has been executed under this proposal.

## Required input

One native, unedited DJI Air 3S MP4:
- target duration: 30–60 seconds,
- original camera file preferred,
- no social-media/export/transcode copy,
- retain original filename and metadata.

Repository FJ899/MP:
NO video file found.

Conversation + Library search performed during proposal preparation:
NO native Air 3S MP4 found.

A substitute MP4 may validate the generic measurement procedure only.
It must be labeled GENERIC_PROCEDURE_ONLY and cannot establish Air 3S compatibility.

## Available environment — previously observed, not execution authorization

Observed during proposal preparation:

ffmpeg:
7.1.5-0+deb13u1

ffprobe:
7.1.5-0+deb13u1

python:
3.13.5

OpenCV:
4.13.0

GPU:
NOT REQUIRED.

Minimal proposed path:
FFprobe + FFmpeg + standard file hashing.

Additional installation:
NONE expected.

Important:
tool versions must be re-recorded in the experiment evidence at actual execution time.
The installed binary is not assumed source-identical to the FFmpeg commit pinned during M1.

## Scope

One source file.
One explicitly selected video stream.
Two repeated probe runs.
Two repeated extraction runs for five selected frames.

No repository implementation code.
No dependency installation.
No adapter.
No model.
No approximate seek-based extraction.

## Terminology

### raw PTS

The frame field reported by ffprobe as:
pts

and converted using the selected stream time_base.

raw PTS is preserved separately.

### best-effort timestamp

The ffprobe field:
best_effort_timestamp

It is a decoder-derived estimated timestamp and must NEVER be labeled as original/raw PTS.

### selection timestamp kind

One basis is chosen for the whole frame-selection calculation:

RAW_PTS

or, only if raw PTS is not usable across the required frame set:

BEST_EFFORT_TIMESTAMP.

Do not mix timestamp kinds silently within one selection calculation.

### enumeration_ordinal

Zero-based ordinal in the decoded frame sequence emitted by the same FFmpeg decoding path represented by ffprobe -show_frames.

This ordinal is retained because FFmpeg select=n uses decoded-frame sequence order.

### presentation_ordinal

Zero-based ordinal after ordering the frame records by:

1. selected presentation timestamp ascending;
2. enumeration_ordinal ascending as the deterministic tie-breaker.

This is a derived evidence field.
It is not interchangeable with raw PTS.

## Step 0 — Input identity

Record:

- original filename,
- file size,
- SHA-256 of complete input file,
- source note: native Air 3S original vs substitute,
- experiment ID,
- execution date.

Do not automatically commit the full source video.

## Step 1 — Runtime identity

Persist exact output of:

    ffmpeg -version
    ffprobe -version

Also record:
- operating environment,
- complete commands actually executed.

## Step 2 — Discover streams and select exactly one video stream

Proposed command:

    ffprobe -v error       -show_entries stream=index,codec_type,codec_name,width,height,time_base,r_frame_rate,avg_frame_rate,start_time,duration,nb_frames:format=start_time,duration:stream_tags       -of json       "$INPUT"       > stream_metadata.json

Selection rule:

- enumerate all streams first;
- select exactly one intended video stream;
- store its GLOBAL stream index as STREAM_INDEX;
- all later commands explicitly target that stream.

Do not assume the desired video stream is stream 0.

Record:
- STREAM_INDEX,
- codec,
- width/height,
- time_base,
- rates,
- stream start_time/duration when present,
- container start_time/duration separately.

## Step 3 — Enumerate decoded frames twice

For the chosen global stream index:

Run 1:

    ffprobe -v error       -select_streams "$STREAM_INDEX"       -show_frames       -show_entries frame=stream_index,pts,pts_time,best_effort_timestamp,best_effort_timestamp_time,pkt_dts,pkt_dts_time,pict_type,width,height       -of json       "$INPUT"       > frames_run1.json

Run 2:

    ffprobe -v error       -select_streams "$STREAM_INDEX"       -show_frames       -show_entries frame=stream_index,pts,pts_time,best_effort_timestamp,best_effort_timestamp_time,pkt_dts,pkt_dts_time,pict_type,width,height       -of json       "$INPUT"       > frames_run2.json

For every decoded frame derive/store:

- stream_index,
- enumeration_ordinal,
- raw pts,
- raw pts_time,
- stream time_base,
- best_effort_timestamp,
- best_effort_timestamp_time,
- pkt_dts / pkt_dts_time when available,
- pict_type,
- dimensions.

Never replace a missing raw PTS field with best_effort_timestamp under the same column/name.

## Step 4 — Choose one timestamp basis for sample selection

Selection-basis rule:

A. If raw pts/pts_time is present and usable for the frame population required by the experiment:
   selection_timestamp_kind = RAW_PTS.

B. Otherwise, if best_effort_timestamp is present and usable:
   selection_timestamp_kind = BEST_EFFORT_TIMESTAMP.

C. If neither provides a usable presentation-time basis:
   after an authorized run, result is INCONCLUSIVE unless the observed behavior itself satisfies a defined FAIL condition.

The selected kind is written into:
selected_samples.csv

and applies consistently to all five target samples.

## Step 5 — Derive actual timestamp range

Do NOT assume the video presentation timeline starts at zero.

For the chosen selection timestamp kind:

    T_min = minimum selected-stream frame timestamp_time
    T_max = maximum selected-stream frame timestamp_time

Require:

    T_max > T_min

The sample target for percentage p is:

    target(p) = T_min + p * (T_max - T_min)

for:

    p = 0.10
    p = 0.30
    p = 0.50
    p = 0.70
    p = 0.90

Thus 10/30/50/70/90% are relative to the observed frame timestamp range, not to zero and not blindly to container duration.

## Step 6 — Deterministic nearest-frame rule

For each target(p), choose the frame minimizing:

    abs(frame_selection_timestamp_time - target(p))

Tie-breaking:

1. choose the LOWER frame_selection_timestamp_time;
2. if multiple frames still have the same selected timestamp, choose the LOWER presentation_ordinal;
3. if needed for exact extraction bookkeeping, retain that frame's enumeration_ordinal.

For every selected sample retain:

- sample ID,
- percentage p,
- target timestamp time,
- timestamp kind used,
- stream index,
- enumeration_ordinal,
- presentation_ordinal,
- raw PTS,
- raw pts_time,
- stream time_base,
- best_effort_timestamp,
- best_effort_timestamp_time,
- DTS fields when available.

## Step 7 — Exact frame extraction from enumeration

Approximate seek is NOT used.

Prohibited as the identity mechanism:

    ffmpeg -ss <approximate-time> ...

because that alone does not prove extraction of the exact enumerated frame.

The extraction key is the selected frame's:
enumeration_ordinal.

For one selected sample with:

    N=<enumeration_ordinal>
    STREAM_INDEX=<global stream index>

proposed extraction command:

    ffmpeg -hide_banner -loglevel info       -copyts       -i "$INPUT"       -map 0:"$STREAM_INDEX"       -vf "select='eq(n\,$N)',showinfo"       -fps_mode passthrough       -frames:v 1       -an -sn -dn       -c:v png       "$OUT_PNG"       2> "$OUT_LOG"

Repeat the same command structure for all five samples.

Then repeat the full five-frame extraction as independent Run B.

Why these options are explicit:

- -map 0:STREAM_INDEX chooses the exact source stream;
- select=eq(n,N) chooses one exact decoded-frame ordinal, not an approximate seek time;
- -fps_mode passthrough avoids intentional CFR duplication/drop behavior;
- -frames:v 1 limits output to the selected frame;
- -copyts avoids deliberately rebasing timestamps to zero;
- showinfo records the selected decoded frame's runtime PTS/time evidence.

The showinfo record must be compared with the selected frame record.
Any mismatch is evidence, not something to normalize away.

## Step 8 — Decoded-pixel hash

PNG file bytes are not the primary pixel-identity proof.

For the same selected frame, calculate a hash of a standardized decoded pixel representation.

Proposed command:

    ffmpeg -v error       -copyts       -i "$INPUT"       -map 0:"$STREAM_INDEX"       -vf "select='eq(n\,$N)',format=rgb24"       -fps_mode passthrough       -frames:v 1       -an -sn -dn       -f hash       -hash sha256       -

Record the returned SHA-256 as:

decoded_rgb24_sha256

for Run A and Run B.

This tests decoded pixel equality independently of PNG container/encoder bytes.

## Step 9 — PNG file hash

Also compute:

    sha256sum "$OUT_PNG"

Record:

png_file_sha256

This is a secondary reproducibility measure.

Different PNG SHA-256 values do NOT automatically mean different decoded pixels.

## Step 10 — Three separate comparisons

### A. Source → stream → frame → timestamp identity

Compare Run A / Run B:

- input SHA-256,
- exact STREAM_INDEX,
- frame counts relevant to enumeration,
- enumeration_ordinal,
- presentation_ordinal,
- raw PTS,
- pts_time,
- time_base,
- best-effort fields,
- timestamp kind used,
- selected target mapping,
- showinfo PTS/time for extracted frame.

This is the primary provenance test.

### B. Decoded-pixel equality

Compare:

decoded_rgb24_sha256

for each corresponding sample.

Matching hashes mean the standardized decoded pixels are identical for that sample under the compared runs.

### C. PNG byte equality

Compare:

png_file_sha256.

Interpretation:

- A same + B same + C same:
  strongest reproducibility observation.

- A same + B same + C different:
  do NOT claim a different source frame;
  investigate PNG encoding/metadata/output-byte differences.

- A same + B different:
  decoded-pixel reproducibility problem requiring diagnosis.

- A different:
  source/frame/timestamp mapping reproducibility problem regardless of PNG hash.

## PASS criteria

PASS for one native Air 3S input requires:

1. input SHA-256 recorded;
2. one intended video stream explicitly selected by global stream index;
3. stream time_base recorded;
4. raw PTS and best-effort fields preserved separately;
5. the selected timestamp kind explicitly recorded;
6. T_min/T_max derived from actual selected-stream frame timestamps, not assumed zero;
7. both probe runs reproduce the relevant source→stream→frame→timestamp mapping;
8. selected presentation timestamps do not reverse after applying the declared presentation ordering;
9. all five target percentages choose the same frame identities in both probe runs;
10. exact extraction by enumeration_ordinal yields showinfo evidence consistent with the selected frame;
11. Run A and Run B decoded_rgb24_sha256 match for all five samples;
12. any PNG-byte mismatch with matching decoded pixels is separately diagnosed and does not by itself fail frame identity;
13. every sample is traceable to:
    input SHA-256
    + stream index
    + enumeration ordinal
    + presentation ordinal
    + raw PTS if present
    + time_base
    + declared timestamp kind
    + extraction command.

PASS means only:

for this exact native Air 3S file, selected stream, toolchain and recording profile, the tested source→timestamp→frame→pixel path is reproducible.

PASS does NOT generalize to every Air 3S mode, firmware, codec profile or future tool version.

## FAIL criteria

FAIL if an authorized run produces a repeatable defect that undermines auditable mapping, for example:

- repeated probe runs produce different frame/timestamp identities;
- selected sample rules choose different frame identities across identical runs;
- exact ordinal extraction does not correspond to the enumerated selected frame;
- presentation identity reverses/corrupts in a way that cannot support RECHECK provenance;
- identical mapped frame identity produces different decoded_rgb24_sha256 values without an explainable environment/input change;
- the source cannot be decoded sufficiently to preserve auditable frame identity.

Different PNG file SHA alone is NOT sufficient for FAIL when decoded pixels match.

FAIL does not authorize custom BUILD.

## INCONCLUSIVE criteria

INCONCLUSIVE exists only after execution has started.

Examples:

- supplied file turns out to be edited/transcoded and native-source status cannot be established;
- input is corrupted/truncated;
- timestamp fields are insufficient but evidence cannot distinguish source peculiarity from procedure/tool configuration;
- environment identity changed between repeated runs;
- procedure defect invalidated the comparison.

Current pre-execution condition is NOT INCONCLUSIVE.

Current condition is:

NOT_STARTED / BLOCKED_BY_INPUT.

## Evidence package

After explicit authorization:

    evidence/m2-01/<experiment-id>/

Proposed files:

- README.md
- input_identity.txt
- sha256.txt
- environment.txt
- commands.txt
- stream_metadata.json
- frames_run1.json
- frames_run2.json
- selected_samples.csv
- extracted/runA/*.png
- extracted/runB/*.png
- extraction_showinfo_runA/*.log
- extraction_showinfo_runB/*.log
- decoded_pixel_hashes_runA.txt
- decoded_pixel_hashes_runB.txt
- png_hashes_runA.txt
- png_hashes_runB.txt
- RESULT.md

RESULT.md after an executed attempt must state exactly one:

PASS
FAIL
INCONCLUSIVE

and preserve:
- actual input identity,
- actual runtime tool identity,
- exact commands,
- deviations,
- anomalies,
- limitations.

## Cost

Additional software/license cost:
none expected.

Paid API:
none.

GPU:
none.

Additional installation:
none expected.

Repository implementation:
none.

Primary resource:
one short native Air 3S clip plus CPU/storage for complete frame probing and ten PNG extracts.

## Preserved limitations

1. One clip tests one recording profile only.
2. Runtime FFmpeg package identity must be preserved; M1 source pin is not runtime identity.
3. best_effort_timestamp is explicitly an estimated field and is not raw PTS.
4. Frame ordinal, PTS, best-effort timestamp and timebase are separate evidence fields.
5. Variable frame rate or timestamp irregularity is observed, not silently normalized.
6. No telemetry is tested.
7. No AI model is tested.
8. Substitute video cannot validate Air 3S compatibility.

## Decision after M2-01

If PASS:
propose the next smallest decision based on evidence.
Do not automatically start M2-02.

If FAIL:
diagnose existing tooling/configuration/source behavior before any custom BUILD.

If INCONCLUSIVE:
fix only the unresolved experimental condition and rerun M2-01 if authorized.

## HUMAN decision options

### AUTHORIZE_M2_01

Authorize exactly this revised M2-01 after a native Air 3S clip is available.

Permits:
- probing one supplied native clip,
- two frame enumerations,
- selecting five frames using the declared T_min/T_max rule,
- two exact ordinal-based extraction runs,
- decoded-pixel hashes,
- PNG hashes,
- evidence package.

Does NOT permit:
- dependency installation,
- repository implementation,
- M2-02+,
- AI model execution/training,
- merge,
- architecture freeze.

### ACCEPT_PLAN_ONLY

Accept revision 2 as the experiment design.
Execution remains NOT_AUTHORIZED.

### REQUEST_CHANGES

Return specific plan changes.

### DEFER

Keep M2-01 pending.

## Current recommendation

The plan can be reviewed/accepted now.

Actual execution remains blocked by missing native Air 3S input and requires separate HUMAN authorization.
