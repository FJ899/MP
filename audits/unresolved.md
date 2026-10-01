# M1 Material Unresolved Items

These are current unresolved facts after the M1 reconnaissance pass.
They are not historical TODOs and must not be silently inferred.

## Known-defect checkpoint / weights

framework_candidate:
ultralytics/ultralytics@9b790cf26ffce6809723873a2547160085329b92

framework_code_license:
AGPL-3.0

status:
TASK_RELEVANT_WEIGHTS_UNRESOLVED

Critical need before detector smoke:
- identify an actual facade/structural-defect checkpoint or deliberately authorized training path;
- pin checkpoint identity;
- verify weights/model terms;
- verify classes/task match.

Generic pretrained detection weights are not evidence for crack/spalling/facade-defect capability.

## BFD-UAV2K data/checkpoints

repository:
Real-world-UAV-Structural-Defects/BFD-UAV2K@18a4a3a1ed3d8eac308e85d7a03de9144123175e

status:
BENCHMARK_SOURCE_INSPECTED / USE_LICENSE_PENDING

Source README states license information will be added with official public release.

Do not infer dataset/checkpoint reuse permission.

## PatchCore pretrained backbone

repository:
open-edge-platform/anomalib@1f503a6c3614e2637472cdb6d9ca21054c83ac26

anomalib_code_license:
Apache-2.0

status:
EXACT_BACKBONE_ARTIFACT_AND_TERMS_TO_PIN_BEFORE_M2

PatchCore source defaults to a pretrained backbone.
The exact backbone/model artifact and its applicable terms should be recorded before execution.

## Cutie / alternative VOS weights

repository:
hkchengrex/Cutie@ec5cdd4cf16f75c73ad785a2f96fb97dbad4125a

code_license:
MIT

status:
PRETRAINED_WEIGHT_TERMS_UNRESOLVED

This does not block first M2 because Cutie is PARKED behind SAM2.

## Reference-repository licenses

Status:
REFERENCE_ONLY / DIRECT_CODE_REUSE_NOT_AUTHORIZED

No clear top-level license found in inspected material for some useful references, including:
- AliAbdien/AI-Visual-Inspector
- Arvoxis/hawk-i
- AritraAcherjee/autonomous-drone-infrastructure-inspection
- mercwrite/tank-inspection-uav
- EdwinTSalcedo/RDMO-DigitalTwin
- hkchengrex/Tracking-Anything-with-DEVA

Their mechanisms may inform design.
Their code must not be treated as an approved dependency without resolved terms.

## VLM model artifact

Ollama runtime:
ollama/ollama@3b1999d1d915b4c98338f5b7247e9e3120bae024
runtime_license:
MIT

model:
UNRESOLVED / PARKED

Critical need only if VLM later becomes active:
- exact model/variant,
- vision capability,
- model license/terms,
- hardware footprint.

VLM is not part of the first proposed M2 executable set.

## DJI telemetry / Air 3S compatibility

status:
CANDIDATE_SET_FOUND / AIR3S_COMPATIBILITY_UNRESOLVED

Pinned candidates are recorded in research/PINNED_SOURCES.md.

Critical later test:
inspect one actual Air 3S recording/log from the intended workflow and identify available SRT/subtitle/FlightRecord/DAT data.

Do not infer compatibility from another DJI model.

This is NON-BLOCKING for the first vision-value proof.

## Quality thresholds

status:
UNRESOLVED_BY_DESIGN

M1 identified existing quality mechanisms/signals.
It did not define:
- acceptable BRISQUE threshold,
- blur threshold,
- exposure threshold,
- final quality score formula.

These require MP footage and a human-inspection relevance test.

## CandidateEvent merger semantics

status:
OPEN_INTEGRATION_HYPOTHESIS

Existing sources solve parts:
- WBF: same-frame box fusion;
- Norfair/SAM2/DEVA: temporal continuity;
- mapped-coordinate references: later spatial dedup.

Still unresolved:
the minimal provenance-preserving Observation -> CandidateEvent semantics MP actually needs.

This is not a BUILD authorization.

## Runtime evidence

For all first proposed M2 candidates:

INSTALL:
NOT_RUN

SMOKE_TEST:
NOT_RUN

PIPELINE_COMPATIBILITY:
NOT_TESTED

This is expected at the M1 review boundary.
