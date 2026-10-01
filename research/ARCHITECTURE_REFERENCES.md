# ARCHITECTURE REFERENCES — M1

These repositories are references/competitors for mechanisms. They are not automatic dependencies and do not define MP Architecture v0.1.

## Hawk-I

repository:
Arvoxis/hawk-i

pinned_commit:
0af5ec508631544596dd1ab6926fd2337c34452c

search:
VERTICAL

Useful mechanisms:
- fixed/open-vocabulary detection,
- per-class NMS,
- SAM2 segmentation after detection,
- verification,
- LLM reporting,
- GPS/report/dashboard integration.

MP lesson:
many originally imagined integration steps have existing precedent.

Boundary:
Hawk-I targets a substantially larger edge/GCS system.
Do not clone its architecture wholesale.

License:
UNRESOLVED in inspected source; no LICENSE file/license text found in root/README.

Disposition:
REFERENCE_IMPLEMENTATION + LEARN.

## AegisInspect

repository:
AritraAcherjee/autonomous-drone-infrastructure-inspection

pinned_commit:
816a28619010ce1e42331bb215620f52d18a7d31

search:
VERTICAL

Useful mechanisms:
- explicit supported/measured/demonstrated/pending boundaries,
- persistent defect IDs,
- repeated-observation aggregation,
- human review state,
- deterministic reporting,
- provenance from dataset/version/checkpoint/commit/config/environment to result.

MP lesson:
event/persistence layers should preserve evidence and distinguish demonstrated from inferred capability.

Boundary:
ROS/LiDAR/SLAM/autonomy are not pulled into MP merely because this reference contains them.

License:
UNRESOLVED / no LICENSE found.

Disposition:
REFERENCE_IMPLEMENTATION + LEARN.

## AI-Visual-Inspector

repository:
AliAbdien/AI-Visual-Inspector

pinned_commit:
100f7468ca110b9e8bee65a2b4767b8eda198cc4

search:
HORIZONTAL with architectural relevance.

Mechanism:
Anomalib detector produces deterministic anomaly verdict/heatmap.
VLM is invoked afterward for explanation.
Contradictory VLM text is discarded rather than allowed to override detector evidence.

MP lesson:
detector authority + descriptive VLM is a more disciplined default hypothesis than detector/VLM voting.

License:
no LICENSE found.

Disposition:
REFERENCE_IMPLEMENTATION + LEARN.
VLM runtime remains PARK for first M2.

## IIQC

repository:
fwan133/IIQC

pinned_commit:
b60ddf0aebe8bdafcdbf2e0122d51c63b60462c8

search:
HORIZONTAL with architectural relevance.

Mechanism:
inspection image quality is upstream of defect interpretation and can trigger recollection.

MP lesson:
Quality Gate is a real subsystem, not an afterthought.

Boundary:
IIQC includes bridge/pose/3D/ROS/PCL/OctoMap machinery that MP does not need for first post-flight proof.

License:
project-wide terms unresolved; package.xml contains license TODO.

Disposition:
REFERENCE_IMPLEMENTATION + LEARN.

## DEVA

repository:
hkchengrex/Tracking-Anything-with-DEVA

pinned_commit:
404a112df77f9644d5c7211811329ccd8174b8c3

search:
HORIZONTAL.

Mechanism:
task-specific image model is decoupled from general temporal propagation and semi-online fusion.

Source limitation:
temporal propagation can amplify false positives.

MP lesson:
candidate generation and temporal continuity can remain separate responsibilities.

License:
UNRESOLVED at standard path.

Disposition:
REFERENCE_IMPLEMENTATION + LEARN.

## tank-inspection-uav

repository:
mercwrite/tank-inspection-uav

pinned_commit:
9883295959f04a4ae3a0e1061653f23b9a84fb56

search:
VERTICAL + HORIZONTAL mechanism reference.

Inspected code mechanism:
defect_aggregator stores mapped observations and deduplicates new defects within a configurable Euclidean 3D radius.

MP lesson:
after trustworthy coordinates exist, spatial dedup can be very thin.

Boundary:
first MP proof intentionally lacks 3D/mapped coordinates.

License:
UNRESOLVED.

Disposition:
REFERENCE_IMPLEMENTATION + LEARN.

## Dual-UAV pipeline inspection

repository:
carloscs04/uav-vision-pipeline-inspection

pinned_commit:
5d4389b19c4dd237e456842d80b969135fcfe74d

search:
VERTICAL / reinspection.

Mechanism:
primary inspection logs flagged findings/telemetry; a second UAV consumes flagged target coordinates for targeted reinspection.

MP lesson:
CandidateEvent → durable recheck target is established engineering precedent.

Boundary:
Tello control/autonomous flight is outside first MP scope.

License:
MIT.

Disposition:
REFERENCE_IMPLEMENTATION + LEARN.

## RDMO Digital Twin

repository:
EdwinTSalcedo/RDMO-DigitalTwin

pinned_commit:
1152268834a4a1bac541867d4be463677c827e6f

search:
VERTICAL / recheck-policy reference.

Mechanisms compared:
- Baseline,
- Hover,
- Micro reposition,
- Skip and revisit.

Outputs include recovery coverage, time and energy.

MP lesson:
RECHECK is a policy choice with information/cost trade-offs, not one universal flight action.

Boundary:
simulation/pavement/autonomy are later concerns.

License:
UNRESOLVED / no LICENSE found.

Disposition:
BENCHMARK / REFERENCE + LEARN.

## Cross-reference conclusion

Architecture references reduce custom invention in:
- quality/recollection logic,
- detector→segmentation ordering,
- detector/VLM authority,
- persistent IDs/provenance,
- spatial dedup,
- event→reinspection handoff.

They do NOT justify importing:
- autonomy,
- ROS/LiDAR,
- edge deployment,
- 3D reconstruction,
- GCS/dashboard/product infrastructure

into the first MP proof.
