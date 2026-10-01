# SOURCES

This file records source identities only. Functional claims belong in audit files and must cite inspected source material.

| Component | Exact source | Current audit role | Status |
|---|---|---|---|
| Anomalib / PatchCore | open-edge-platform/anomalib | anomaly detection candidate | source found |
| Ultralytics | ultralytics/ultralytics | detector framework candidate | source found |
| SAHI | obss/sahi | sliced-inference layer | source found |
| SAM2 | facebookresearch/sam2 | segmentation / temporal propagation candidate | source found |
| CVAT | cvat-ai/cvat | annotation / human verification support | source found |
| Ollama | ollama/ollama | local model runtime | source found |
| Gemma 3 | model identity to pin separately | VLM/LLM candidate | unresolved model artifact |
| COLMAP | colmap/colmap | later spatial reconstruction | source found / LATER |
| Hawk-I | Arvoxis/hawk-i | integration reference | source found |
| DJI telemetry parser | unresolved | timestamp -> flight metadata | UNRESOLVED |

## Rules
- Do not treat a repository name as proof of runtime behavior.
- Pin branch/tag/commit before execution evidence is attached.
- Model/checkpoint licenses are separate from repository code licenses when applicable.
- "DJI Telemetry" is not yet a resolved component identity.
