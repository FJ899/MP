# M1 Audit — Segmentation and Tracking

execution_status: NOT_RUN
pipeline_compatibility: NOT_TESTED

## Problem

After another mechanism identifies a suspicious region, MP may need to follow that region across adjacent frames, estimate persistence and avoid treating every frame as a separate event.

## SAM2

repository: facebookresearch/sam2
pinned_commit: 2b90b9f5ceec907a1c18123530e92e794ad901a4
license: Apache-2.0 for code and SAM2 model checkpoints per inspected README

Input:
video/frames plus point/box prompts or an initialized object region.

Output:
object masks/masklets propagated across frames with object IDs.

Source requirements:
- Python >=3.10;
- torch >=2.5.1;
- torchvision >=0.20.1;
- GPU installation documented/recommended;
- CUDA custom extension may be compiled; README states core use can continue if it fails with some post-processing limitations.

Checkpoint options:
SAM2.1 Tiny / Small / Base+ / Large.

Source benchmark context:
reported speed table is measured on A100, so it is not an MP hardware benchmark.

Adapter:
THIN-MODERATE:
candidate box -> prompt;
mask sequence -> track persistence/region evidence.

MP assessment:
strongest first smoke candidate.
Recommended smoke checkpoint: SAM2.1 Hiera Small, because it has an explicit published checkpoint, smaller footprint than Base+/Large and the same prompt/propagate interface.

## Cutie

repository: hkchengrex/Cutie
pinned_commit: ec5cdd4cf16f75c73ad785a2f96fb97dbad4125a
code_license: MIT
pretrained_weight_license: UNRESOLVED in inspected material

Source facts:
- video object segmentation;
- follow-up to XMem;
- first-frame mask then temporal propagation in scripting demo;
- Python >=3.8, PyTorch >=1.12;
- CUDA-oriented demo;
- dependencies include OpenCV, PyTorch ecosystem and downloaded pretrained models.

MP assessment:
EVALUATE/PARK as alternative if SAM2 fails materially.
Do not promote before weight terms are clear.

## XMem

repository: hkchengrex/XMem
pinned_commit: f3b841d50df058910bbf690229ddc15fb1aef7d6
code_license: MIT

Source facts:
long-term video object segmentation with memory; README claims very-long-video support and roughly 20 FPS hardware-dependent behavior.

MP assessment:
LEARN/PARK.
Cutie is its newer follow-up from the same author and is the more relevant alternative.

## DEVA

repository: hkchengrex/Tracking-Anything-with-DEVA
pinned_commit: 404a112df77f9644d5c7211811329ccd8174b8c3
license: UNRESOLVED at standard path

Source facts:
- decouples task-specific image segmentation/detection from generic temporal propagation;
- supports integration of an external image model;
- includes semi-online fusion of hypotheses across frames;
- source documents false-positive amplification as a temporal-propagation risk.

MP assessment:
REFERENCE_IMPLEMENTATION + LEARN.
Architecturally valuable for detector->temporal propagation, but dependency/license complexity is higher than SAM2 smoke.

## Track-Anything

repository: gaomingqi/Track-Anything
pinned_commit: 5e410c60e4101018b40ca98a5ec6749e364cd283
license: MIT

Source facts:
interactive SAM + XMem tracking/segmentation using user clicks.

MP assessment:
REFERENCE / PARK. Interaction model is less aligned with automatic candidate processing.

## M1 proposed disposition

M2 EVALUATE:
SAM2.1 Hiera Small only.

PARK:
Cutie, XMem, Track-Anything.

LEARN:
DEVA.

REPLACES WHAT?:
custom mask propagation / temporal region tracker.

## M2 question

Given one known candidate box in a 5–15 second clip, can SAM2 keep a useful region mask over enough frames to establish persistence without unacceptable drift from UAV camera motion/viewpoint change?
