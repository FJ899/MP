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
| DJI telemetry candidates | FergusInLondon/dji_parse; jetervaz/dji-telemetry; AiryAir/dji-srt2csv; aero-oli/DatCon | timestamp -> flight metadata candidates | source candidates found; Air 3S compatibility UNRESOLVED |
| IIQC | fwan133/IIQC | quality-gate architecture/reference | source inspected |
| UAV image-quality framework | GattuPriyanka/Framework-for-UAV-image-quality | quality-metrics candidate | source inspected |
| AI-Visual-Inspector | AliAbdien/AI-Visual-Inspector | anomaly+VLM authority reference | source inspected |
| WayPoint | BanaanKiamanesh/WayPoint | DJI Fly KMZ route candidate | source inspected |
| DroneRoute | fcsonline/droneroute | WPML/KMZ route candidate/reference | source inspected |
| Air 3S mission-format research | jamiepinkham/drone-mission-planning | Air 3S WPML/KMZ reference | source inspected |
| BFD-UAV2K | Real-world-UAV-Structural-Defects/BFD-UAV2K | UAV facade detector benchmark | source inspected; license pending |
| FBD dataset | Malga-Vision/FBD-Dataset | facade classification benchmark | source inspected |
| InsPLAD | andreluizbvs/InsPLAD | UAV inspection benchmark/reference | source inspected |
| AegisInspect | AritraAcherjee/autonomous-drone-infrastructure-inspection | vertical architecture/evidence reference | source inspected |

## Rules
- Do not treat a repository name as proof of runtime behavior.
- Pin branch/tag/commit before execution evidence is attached.
- Model/checkpoint licenses are separate from repository code licenses when applicable.
- "DJI Telemetry" is not yet a resolved component identity.


## Technology reconnaissance
Detailed candidate evaluation lives in `research/REPO_RADAR.md`.
Search results are not architecture decisions. A source enters CURRENT BUILD SCOPE only through an explicit later decision.
