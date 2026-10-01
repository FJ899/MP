# REPO RADAR

Purpose: prevent MP from rebuilding solved problems without first inspecting existing implementations.

## Required fields
Every serious candidate must record:
NAME, URL, SEARCH TYPE, PROBLEM SOLVED, INPUT, OUTPUT, LICENSE, LAST ACTIVE, TESTS, DOCUMENTATION, GPU/CPU, MATURITY, INTEGRATION COST, WHAT WE CAN LEARN, REPLACES WHAT?, INTEGRATION ROLE, DECISION, WHY, EVIDENCE.

Source facts and MP assessments are separate. MATURITY and INTEGRATION COST below are working assessments unless execution evidence exists.

## Initial reconnaissance — 2026-10-01

| Name | Search | Problem solved | Input -> Output | License | Last active | Tests/evidence seen | MP maturity assessment | Integration cost | Replaces what? | Role | Decision | Why |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IIQC | HORIZONTAL | rapid UAV inspection image-quality assessment + recollection feedback | UAV images + bridge/pose context -> quality assessment / recollection feedback | UNKNOWN; README License section is empty | 2023-11-15 | README reports simulation + real-world validation; MP has not executed it | research prototype | HIGH as direct component; MEDIUM as reference | custom quality-metric architecture | REFERENCE_IMPLEMENTATION | LEARN | Very close problem, but stack includes ROS, pose estimation, OctoMap, PCL and bridge-specific context; inspect algorithms before reuse |
| Framework-for-UAV-image-quality | HORIZONTAL | computes quality metrics for UAV image folders | image folder -> flight quality metrics | UNKNOWN | NOT YET PINNED | README gives runnable workflow only | small utility / research code | LOW-MEDIUM | custom first-pass image quality metrics | COMPONENT candidate | EVALUATE | Simpler alternative to IIQC worth comparing before writing a quality gate |
| AI-Visual-Inspector | HORIZONTAL | anomaly verdict + constrained VLM explanation | image -> anomaly score/heatmap/verdict -> explanation | LICENSE NOT FOUND at standard paths | 2026-09-11 | README reports real training and end-to-end runs; tests directory documented | working prototype with reported execution | MEDIUM | ad-hoc Anomalib+VLM fusion | REFERENCE_IMPLEMENTATION / COMPONENT candidate | LEARN / EVALUATE | Explicit authority split: detector decides, VLM explains and cannot override |
| Hawk-I | VERTICAL | drone infrastructure inspection stack | camera/detections/GPS -> masks/verification/report/dashboard | MIT per README badge/license link | 2026-09-30 | README documents tests, verified environment, limitations; MP has not independently executed | integrated prototype | HIGH if reused wholesale; LOW-MEDIUM as reference | portions of detector->SAM->verification->report integration | REFERENCE_IMPLEMENTATION | LEARN | Very close whole-system architecture; useful competitor/reference, not target by default |
| AegisInspect | VERTICAL | integrated infrastructure-inspection prototype with mapping, persistence, review and evidence discipline | detections/sensors -> persistent mapped findings/reports | LICENSE NOT FOUND at standard paths | 2026-09-30 | README records measured/demonstrated/frozen-pending states and provenance | mature research/capstone prototype | HIGH as dependency; LOW as reference | custom provenance, persistent IDs, observation aggregation patterns | REFERENCE_IMPLEMENTATION | LEARN | Strong reference for evidence boundaries, persistent defect identity and aggregation; avoid importing ROS/LiDAR scope |
| WayPoint | HORIZONTAL | DJI Fly waypoint mission planning and KMZ export | planned waypoints/polygons -> DJI Fly KMZ | MIT | 2026-09-05 | runnable static application documented; MP has not tested Air 3S | active utility | MEDIUM | custom DJI KMZ generator | COMPONENT candidate | EVALUATE | README explicitly lists Air 3S and supports spacing, overlap, heading, gimbal, zoom, import/export |
| DroneRoute | HORIZONTAL | DJI WPML/KMZ mission planner + controller upload | route/POI/actions -> WPML KMZ/controller mission slot | MIT per README | 2026-07-13 | CI badge + documented app/CLI; MP has not executed | active application | MEDIUM | custom WPML generator/controller transfer | COMPONENT / REFERENCE_IMPLEMENTATION | EVALUATE | Strong feature set, but README supported-drone list does NOT currently include Air 3S; compatibility must not be assumed |
| drone-mission-planning | HORIZONTAL | research on DJI Fly mission format for Air 3S | DJI Fly dummy mission / model -> template.kml + waylines.wpml workflow | UNKNOWN | 2026-05-10 | file-format research says calibration awaits an Air 3S dummy mission | early research/prototype | LOW as reference | reverse-engineering DJI Fly WPML format | REFERENCE_IMPLEMENTATION | LEARN | Useful Air 3S-specific format research; explicitly not validated until calibrated on a real dummy mission |
| BFD-UAV2K | HORIZONTAL / BENCHMARK | full-frame UAV facade defect detection benchmark | 2,000 UAV facade images -> benchmark detections/metrics | LICENSE PENDING per README | 2026-06-10 | benchmark results reported for YOLO/RT-DETR/Faster/Cascade R-CNN | benchmark release | LOW for comparison; license blocks use assumptions | "choose YOLO because familiar" | BENCHMARK | EVALUATE | Closest verified facade/UAV benchmark found; lets detector choice be evidence-led |
| FBD Dataset + ensemble code | HORIZONTAL / BENCHMARK | facade defect image classification | close-range facade crops/images -> defect class | LICENSE NOT FOUND at standard paths | dataset 2025-09-24 | paper-linked code for ViT/Swin/ConvNeXt ensembles | research benchmark | MEDIUM | untested assumption that detection is the only useful supervised framing | BENCHMARK | PARK / LEARN | Useful classification evidence, but task differs from full-frame UAV detection and should not be conflated with BFD-UAV2K |
| InsPLAD | HORIZONTAL / BENCHMARK | UAV asset detection + supervised/unsupervised fault analysis | 10,607 power-line UAV images -> asset/fault/anomaly benchmark | TO VERIFY | NOT YET PINNED | published dataset/benchmark documented | mature dataset/benchmark | LOW as benchmark | lack of real-UAV anomaly benchmark | BENCHMARK | LEARN | Different infrastructure domain, but strong evidence about UAV scale/viewpoint/clutter and anomaly workflows |
| UAV crack benchmark (KangchengLiu) | HORIZONTAL / BENCHMARK | crack detection + segmentation dataset for UAV inspection | crack images -> detection/segmentation benchmark | TO VERIFY | NOT YET PINNED | publication-linked dataset and example results | established research dataset | LOW as benchmark | generic crack-data sourcing | BENCHMARK | PARK | Useful secondary crack/segmentation reference; older and broader than facade-specific BFD-UAV2K |
| FergusInLondon/dji_parse | HORIZONTAL | parse DJI MP4 subtitle telemetry | MP4 with subtitle telemetry -> CSV/JSON/GPX with time/GPS/altitude/velocity | permissive MIT text in LICENSE | 2022-12-31 | CI badges; parser behavior documented | small focused utility | LOW | custom timestamp->GPS parser | COMPONENT candidate | EVALUATE | Directly matches simple timestamp->telemetry path if Air 3S records compatible subtitle telemetry; Air 3S compatibility unverified |
| jetervaz/dji-telemetry | HORIZONTAL | parse per-frame DJI SRT telemetry + time lookup | SRT -> structured frames/CSV/JSON/GPX/overlay | MIT per README | NOT YET PINNED | tested with DJI Neo 2 per README | small active-looking utility | LOW | custom SRT parser/time lookup | COMPONENT candidate | EVALUATE | Provides get_frame_at_time and camera/GPS fields; Air 3S compatibility unverified |
| aero-oli/DatCon | HORIZONTAL | decode DJI .DAT flight logs | unencrypted .DAT -> high-rate CSV/KML/logs | permissive; full text in LICENSE.md | NOT YET PINNED | developer fork of DatCon 3.5 behavior | legacy-capability reference | MEDIUM-HIGH | binary flight-log parser | REFERENCE_IMPLEMENTATION / COMPONENT candidate | PARK | Richer telemetry possible, but README warns newer/encrypted DJI logs may fail; do not assume Air 3S support |

## Search log — first pass

VERTICAL queries attempted:
- drone inspection infrastructure
- UAV inspection

HORIZONTAL queries attempted:
- image quality UAV
- facade defect detection
- DJI telemetry parser
- DJI waypoint KMZ

Some broad natural-language GitHub searches returned no results; simpler repository-search terms produced useful candidates. Search failure is recorded rather than interpreted as absence of solutions.

## Rule
No candidate becomes a dependency or architecture choice from README similarity alone. EVALUATE means inspect more and, where justified, run the cheapest discriminating test.
