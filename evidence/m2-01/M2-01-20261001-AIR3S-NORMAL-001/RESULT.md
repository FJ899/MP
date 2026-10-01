# M2-01 Result — Video Timestamp Integrity

experiment_id: M2-01-20261001-AIR3S-NORMAL-001
result: PASS
proposal_revision: 3
input_file: Air3s_normal.MP4
input_size_bytes: 74451639
input_sha256: cc8ace8fc18280d09318d29f5b7dbcc1b7b44d986c2d83035d4421e0d927bcaa

## Scope

This result applies only to the supplied file, selected primary HEVC stream, observed runtime toolchain and recording profile.
It does not generalize to every DJI Air 3S mode, firmware or codec profile.

## Input identity observations

- Supplied by HUMAN as Air3s_normal.MP4.
- Main video stream: HEVC, 3840x2160, 30000/1001 fps, time_base 1/30000.
- Main stream duration: 11.244567 s; 337 frames.
- File also contains data streams named HAL meta and HAL dbgi plus an auxiliary MJPEG 960x540 attached-picture stream.
- Raw string inspection found identifiers including dvtm_Air3s.proto, DJI Air3s and DJI FC9113-.

These observations strongly support Air 3S identity for the supplied sample, but M2-01 does not establish an independent chain-of-custody proving the file is an untouched camera original.
The clip is shorter than the proposed target 30–60 s; this is recorded as a limitation, not hidden.

## Timestamp result

selection_timestamp_kind: RAW_PTS
frame_count_run1: 337
frame_count_run2: 337
probe_runs_identity_equal: true
probe_json_byte_equal: true
T_min_raw: 0
T_max_raw: 336336
T_min_time: 0.000000 s
T_max_time: 11.211200 s

Enumeration-order integrity in both runs:
- MISSING: 0
- DUPLICATE: 0
- REGRESSION: 0
- FORWARD transitions: 336

## Selected samples

| Sample | Enumeration ordinal | Raw PTS | PTS time (s) |
|---|---:|---:|---:|
| p10 | 34 | 34034 | 1.134467 |
| p30 | 101 | 101101 | 3.370033 |
| p50 | 168 | 168168 | 5.605600 |
| p70 | 235 | 235235 | 7.841167 |
| p90 | 302 | 302302 | 10.076733 |

For all five samples in both formal runs:
- showinfo PTS/time matched the selected enumerated frame;
- source RGB24 hash Run A == source RGB24 hash Run B;
- saved PNG decoded RGB24 hash == corresponding source RGB24 hash;
- saved PNG dimensions == source dimensions (3840x2160);
- PNG file SHA-256 Run A == PNG file SHA-256 Run B.

## PASS interpretation

For this supplied Air 3S sample in the tested environment, MP can reproducibly bind:

source SHA-256 -> selected video stream -> decoded-frame ordinal -> raw PTS/timebase -> exact extracted frame -> standardized RGB24 pixels -> saved PNG evidence.

This is sufficient evidence for the M2-01 provenance question.

## Non-authorizations

PASS does not authorize M2-02, model execution/training, implementation, dependency installation, merge, architecture freeze, flight/route execution or publish/release/deploy.
