# Unresolved / not-yet-audited candidates

These entries deliberately do not receive inferred capabilities.

## Ultralytics
repository: ultralytics/ultralytics
status: SOURCE_FOUND / FUNCTIONAL_AUDIT_PENDING
critical need:
identify exact model/weights capable of relevant defect classes. Framework presence alone does not establish crack/spalling/corrosion detection.

## CVAT
repository: cvat-ai/cvat
status: SOURCE_FOUND / FUNCTIONAL_AUDIT_PENDING
expected question:
is it needed for M1/M2 operator verification, or only later dataset building?

## Ollama
repository: ollama/ollama
status: SOURCE_FOUND / FUNCTIONAL_AUDIT_PENDING
critical need:
separate runtime capability from exact Gemma 3 model artifact and vision support.

## Gemma 3
status: MODEL_ARTIFACT_UNRESOLVED
critical need:
pin exact model variant and model license before execution.

## DJI telemetry
status: SOURCE_IDENTITY_UNRESOLVED
critical need:
identify actual Air 3S-compatible log source/parser and available fields.

## COLMAP
repository: colmap/colmap
status: SOURCE_FOUND / LATER
No reason to make it a dependency of first vision-value proof.
