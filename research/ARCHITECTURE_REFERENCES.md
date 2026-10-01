# ARCHITECTURE REFERENCES

These repositories are competitors/references for MP architecture, not automatic dependencies.

## Hawk-I — Arvoxis/hawk-i
Search type: VERTICAL

Why it matters:
- combines known/open-vocabulary detection,
- SAM2 segmentation,
- DINOv2 verification,
- Gemma 3/Ollama reporting,
- GPS/MAVLink,
- persistence/report/dashboard layers.

Questions for MP:
- Which integration boundaries are genuinely reusable?
- Which layers exist only because Hawk-I targets edge/GCS operation?
- Which claims are demonstrated by code/tests versus README narrative?
- Can MP reuse data contracts or failure-handling ideas without adopting its architecture?

Current disposition:
REFERENCE_IMPLEMENTATION + LEARN.

## AegisInspect — AritraAcherjee/autonomous-drone-infrastructure-inspection
Search type: VERTICAL

Why it matters:
- explicit measured/demonstrated/not-completed boundaries,
- persistent defect identities,
- repeated-observation aggregation,
- human review state,
- deterministic reporting,
- strong provenance chain from dataset to result artifact.

Questions for MP:
- Can event merger/deduplication borrow its persistent-observation ideas?
- Which evidence/provenance patterns should MP copy even if ROS/LiDAR are irrelevant?
- How does it separate mapping/localization evidence from defect evidence?

Current disposition:
REFERENCE_IMPLEMENTATION + LEARN.
Do not import ROS, LiDAR, SLAM or autonomy merely because the reference contains them.

## AI-Visual-Inspector — AliAbdien/AI-Visual-Inspector
Search type: HORIZONTAL with architectural relevance

Important pattern:
DETECTOR = authority for anomaly verdict.
VLM = descriptive/explanatory layer.
VLM contradiction is rejected rather than allowed to override detector verdict.

MP implication:
This is a strong candidate for the default authority model in the anomaly path, but remains a hypothesis to test on MP material.

Current disposition:
REFERENCE_IMPLEMENTATION + LEARN/EVALUATE.

## IIQC — fwan133/IIQC
Search type: HORIZONTAL with architectural relevance

Important pattern:
quality assessment is upstream of defect interpretation and can directly trigger image recollection.

MP implication:
Quality Gate should be researched as an existing subsystem before designing blur/exposure/quality/recollection logic from scratch.

Caution:
IIQC includes pose estimation and 3D/bridge-specific machinery, so "same problem" does not mean "drop-in component."

Current disposition:
REFERENCE_IMPLEMENTATION + LEARN.
