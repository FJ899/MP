# M1 Pinned Sources

Snapshot date: 2026-10-01

Purpose: bind M1 source-derived claims to exact repository identities. A pinned source is not an implementation decision and does not prove runtime compatibility.

| Area | Repository | Branch | Pinned commit | M1 role | Code/license status |
|---|---|---|---|---|---|
| Video decode | FFmpeg/FFmpeg | master | 0eb6a369c698e532598b47b6d96a0c84abdfef1d | dependency candidate | LGPL-2.1+ default build; optional configuration can change effective license |
| Video/frame CV | opencv/opencv | 4.x | 237b3c2eac474f3e69b8abff4c47384be1a9e521 | dependency candidate | Apache-2.0 |
| Scene detection | Breakthrough/PySceneDetect | main | 81c414cb4b706e58648f98efd381024790b1565f | reference / park | BSD-3-Clause |
| FFmpeg Python binding | PyAV-Org/PyAV | master | b618b2d9802cb8c4ac368ff97fc2873de05aab89 | park | BSD-3-Clause from pyproject |
| Video framework | abhiTronix/vidgear | master | 549de2b1fb70f25e7a0e29fd55159256c3e0b4a4 | park | Apache-2.0 |
| UAV quality reference | fwan133/IIQC | master | b60ddf0aebe8bdafcdbf2e0122d51c63b60462c8 | reference implementation | project-wide license UNRESOLVED; package.xml says TODO and source contains mixed inherited notices |
| UAV quality metrics | GattuPriyanka/Framework-for-UAV-image-quality | main | 9344d90ca9f56bf7bd54623b090c794c8c68d3f9 | reference / park | no LICENSE found |
| BRISQUE quality score | rehanguha/brisque | master | 42c854ef9278f09d047abb8600d5204f779eca52 | M2 evaluation candidate | code Apache-2.0; bundled svm.txt + normalize.pickle provenance/terms UNRESOLVED |
| Anomaly | open-edge-platform/anomalib | main | 1f503a6c3614e2637472cdb6d9ca21054c83ac26 | M2 evaluation candidate | Apache-2.0 code; pretrained backbone weights license remains transitive/model-specific |
| Anomaly+VLM pattern | AliAbdien/AI-Visual-Inspector | main | 100f7468ca110b9e8bee65a2b4767b8eda198cc4 | reference implementation | no LICENSE found |
| Sliced inference | obss/sahi | main | 80ebdb699851facf87def03c0597e1aeb87a9a2d | optional M2 mode | MIT |
| Detector framework | ultralytics/ultralytics | main | 9b790cf26ffce6809723873a2547160085329b92 | candidate framework | AGPL-3.0 code; defect-model weights/license unresolved |
| UAV facade benchmark | Real-world-UAV-Structural-Defects/BFD-UAV2K | main | 18a4a3a1ed3d8eac308e85d7a03de9144123175e | benchmark | README says license pending official release |
| Facade classification data | Malga-Vision/FBD-Dataset | main | 40cdabd5cb344aa1a563c3e9b4823bc64d462507 | benchmark / park | license not established in M1 |
| FBD ensemble implementation | Malga-Vision/Ensembles-of-deep-neural-networks-for-the-automatic-detection-of-building-facade-defects-from-images | main | 78ab865e65c2fb7de4e12a7f7eb64bec7959c3ab | learn / park | license not established in M1 |
| UAV inspection benchmark | andreluizbvs/InsPLAD | main | 1b713698d7e97836b41a62dfa3314c20f3acda70 | benchmark / learn | TO VERIFY before direct reuse |
| UAV crack dataset | KangchengLiu/Crack-Detection-and-Segmentation-Dataset-for-UAV-Inspection | master | ddcacf4f001f1333f3152fe5088068c51c6ac034 | benchmark / park | TO VERIFY before direct reuse |
| Prompted video masks | facebookresearch/sam2 | main | 2b90b9f5ceec907a1c18123530e92e794ad901a4 | M2 evaluation candidate | Apache-2.0 code and SAM2 checkpoints per README |
| Video object segmentation | hkchengrex/Cutie | main | ec5cdd4cf16f75c73ad785a2f96fb97dbad4125a | alternative / park | MIT code; pretrained-model license not separately established |
| Long-term VOS | hkchengrex/XMem | main | f3b841d50df058910bbf690229ddc15fb1aef7d6 | learn / park | MIT code; weights terms not separately established |
| Detector-to-temporal fusion | hkchengrex/Tracking-Anything-with-DEVA | main | 404a112df77f9644d5c7211811329ccd8174b8c3 | reference implementation | no LICENSE found at standard path |
| Interactive VOS | gaomingqi/Track-Anything | master | 5e410c60e4101018b40ca98a5ec6749e364cd283 | reference / park | MIT |
| Same-frame box fusion | ZFTurbo/Weighted-Boxes-Fusion | master | 96880f3df8d45ac21dce8d243fcfab420cadda47 | M2 evaluation candidate | MIT |
| Temporal association | tryolabs/norfair | master | e517b4236f6b67a6ecf342f5df1fccb7788dbc54 | M2 evaluation candidate | BSD-3-Clause |
| MOT alternative | FoundationVision/ByteTrack | main | d1bf0191adff59bc8fcfeaa0b33d3d1642552a99 | park | MIT |
| Whole inspection system | Arvoxis/hawk-i | master | 0af5ec508631544596dd1ab6926fd2337c34452c | reference implementation | UNRESOLVED; no LICENSE file/license text found in inspected root/README |
| Evidence/persistence reference | AritraAcherjee/autonomous-drone-infrastructure-inspection | main | 816a28619010ce1e42331bb215620f52d18a7d31 | reference implementation | no LICENSE found |
| Spatial dedup reference | mercwrite/tank-inspection-uav | main | 9883295959f04a4ae3a0e1061653f23b9a84fb56 | reference implementation | no LICENSE found |
| Targeted re-inspection | carloscs04/uav-vision-pipeline-inspection | main | 5d4389b19c4dd237e456842d80b969135fcfe74d | reference implementation | MIT |
| Revisit strategy benchmark | EdwinTSalcedo/RDMO-DigitalTwin | main | 1152268834a4a1bac541867d4be463677c827e6f | reference / benchmark | no LICENSE found |
| Human annotation | cvat-ai/cvat | develop | cde80590ce4a61a54722c13786b7430682403901 | later / optional | MIT |
| Local VLM runtime | ollama/ollama | main | 3b1999d1d915b4c98338f5b7247e9e3120bae024 | later / optional | MIT runtime; model license separate |
| 3D reconstruction | colmap/colmap | main | 25ff12a86ccda7e518bf626ce8bfd16f344f3ead | later | license not needed for M2; verify before use |
| DJI MP4 telemetry | FergusInLondon/dji_parse | main | 4650bc8300cfd14910aa4e8b592ea684cc193668 | later candidate | permissive MIT text |
| DJI SRT telemetry | jetervaz/dji-telemetry | main | 05d15f703958fc2136536913281932c432c94aeb | later candidate | MIT |
| DJI SRT conversion | AiryAir/dji-srt2csv | main | f75ec8fb645d2e3fe5c6d269ca3cee9a3b9f071a | later candidate | TO VERIFY before use |
| DJI DAT decoding | aero-oli/DatCon | master | 0f8ed8b35617185ddb03a78e0a67addb738b623d | later / park | TO VERIFY before use; newer encrypted logs may be unsupported |
| DJI Fly mission planner | BanaanKiamanesh/WayPoint | main | 74f16952476ac12a47621f8ec02380cf32c6d982 | later candidate | MIT |
| WPML/KMZ planner | fcsonline/droneroute | main | 2b27ac2d9ff9647bdae3fad9da807bd59d3ef646 | later reference/candidate | MIT; current supported list does not establish Air 3S |
| Air 3S mission format research | jamiepinkham/drone-mission-planning | main | e367dc8d33c865dd37d4c2c5e113056136a0a63a | later reference | license TO VERIFY; Air 3S calibration explicitly pending |

## Interpretation rules

- Pinned commit = identity for M1 source inspection, not an approved dependency.
- UNRESOLVED is intentional evidence state, not permission to guess.
- Code license and model/checkpoint/data license are separate facts.
- A repository with no clear license may still be used as a reference for mechanisms, but should not become a code dependency until terms are resolved.


## BRISQUE bundled model artifacts

Repository:
rehanguha/brisque

Pinned code commit:
42c854ef9278f09d047abb8600d5204f779eca52

Default runtime artifacts loaded by BRISQUE.__init__():
- brisque/models/svm.txt
  - git blob: 19237f04eae11398a2a41b91a7ef8ad2bfc084d5
- brisque/models/normalize.pickle
  - git blob: 18ed3adf6991d0feba7b3cb832a247209f9f5cf1

Both artifacts first appear in repository history in commit:
10e2dd2a23ee597e788761b161bec1c60aa046fd
("Made a package out of the code and added the models.")

Status:
MODEL_ARTIFACT_PROVENANCE_AND_TERMS_UNRESOLVED.

M1 does not independently establish whether the root Apache-2.0 terms cover or exclude these bundled model/data artifacts.

M2-02 must not use the default model until this boundary is resolved or a custom model with acceptable pinned provenance/terms is supplied.


## BRISQUE bundled model artifacts

Repository: rehanguha/brisque

Pinned code commit: 42c854ef9278f09d047abb8600d5204f779eca52

Default runtime artifacts loaded by BRISQUE.__init__():
- brisque/models/svm.txt — git blob 19237f04eae11398a2a41b91a7ef8ad2bfc084d5
- brisque/models/normalize.pickle — git blob 18ed3adf6991d0feba7b3cb832a247209f9f5cf1

Both artifacts first appear in repository history in commit 10e2dd2a23ee597e788761b161bec1c60aa046fd ("Made a package out of the code and added the models.").

Status: MODEL_ARTIFACT_PROVENANCE_AND_TERMS_UNRESOLVED.

M1 does not independently establish whether the root Apache-2.0 terms cover or exclude these bundled model/data artifacts.

M2-02 must not use the default model until this boundary is resolved or a custom model with acceptable pinned provenance/terms is supplied.
