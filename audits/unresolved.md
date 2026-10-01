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
status: CANDIDATE_SET_FOUND / AIR3S_COMPATIBILITY_UNRESOLVED
candidates inspected or identified:
- FergusInLondon/dji_parse
- jetervaz/dji-telemetry
- AiryAir/dji-srt2csv
- aero-oli/DatCon
critical need:
inspect an actual Air 3S recording/log from the intended workflow and determine whether SRT/subtitle or other telemetry exposes the fields MP needs. Do not infer Air 3S compatibility from support for other DJI models.

## COLMAP
repository: colmap/colmap
status: SOURCE_FOUND / LATER
No reason to make it a dependency of first vision-value proof.
