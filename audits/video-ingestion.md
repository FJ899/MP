# M1 Audit — Video Ingestion

execution_status: NOT_RUN
pipeline_compatibility: NOT_TESTED

## Problem

MP needs deterministic access from a post-flight video to frames/crops with reproducible timestamps. It does not currently need a general streaming framework or semantic scene-cut detector.

## Candidates inspected

### FFmpeg

repository: FFmpeg/FFmpeg
pinned_commit: 0eb6a369c698e532598b47b6d96a0c84abdfef1d

Source facts:
- mature command-line/library media decoder and filter pipeline;
- default combined FFmpeg license is LGPL-2.1+;
- enabling optional GPL parts changes effective license; nonfree combinations may become unredistributable.

MP input:
native video file.

MP-relevant output:
decoded frames, time/PTS metadata, extracted clips/images.

Compute:
CPU baseline; optional hardware decode is possible but not required for first smoke test.

Adapter:
THIN. Preserve source path, frame index, timestamp/PTS and extraction parameters.

### OpenCV

repository: opencv/opencv
pinned_commit: 237b3c2eac474f3e69b8abff4c47384be1a9e521
license: Apache-2.0

MP role:
frame/image operations after decode and simple video access where sufficient.

Adapter:
NONE-THIN.

### PySceneDetect

repository: Breakthrough/PySceneDetect
pinned_commit: 81c414cb4b706e58648f98efd381024790b1565f
license: BSD-3-Clause

Source facts:
- video cut/scene detection and analysis;
- can return scene start/end timecodes and save/split frames/video;
- latest README at inspected ref documents v0.7.1;
- ContentDetector / AdaptiveDetector are aimed at visual scene changes.

MP assessment:
PARK / LEARN.
Camera-motion or content cuts are not equivalent to defect/recheck events. It does not replace deterministic inspection sampling.

### PyAV

repository: PyAV-Org/PyAV
pinned_commit: b618b2d9802cb8c4ac368ff97fc2873de05aab89
license: BSD-3-Clause from pyproject
requires_python: >=3.12

Source fact:
Pythonic binding to FFmpeg containers/streams/packets/codecs/frames.
Its README explicitly notes that when the ffmpeg command already solves the job, PyAV can add complexity rather than remove it.

MP assessment:
PARK unless packet-level timestamp/control becomes necessary.

### VidGear

repository: abhiTronix/vidgear
pinned_commit: 549de2b1fb70f25e7a0e29fd55159256c3e0b4a4
license: Apache-2.0

Source fact:
multi-threaded/async framework over OpenCV, FFmpeg and other media/network backends.

MP assessment:
PARK. Broader than the first post-flight file-ingestion requirement.

## M1 proposed disposition

M2 baseline candidate:
FFmpeg + OpenCV.

Why:
- smallest mature path,
- timestamp/frame extraction is already solved,
- no evidence that a new ingestion framework increases RECHECK quality.

REPLACES WHAT?:
custom video ingestion framework.

## M2 question

Can a 30–60 second native Air 3S clip be decoded into a reproducible list of frame observations with monotonic timestamps and stable frame/time mapping?

No fixed 8 s / 10 s sampling cadence is approved by this audit.
