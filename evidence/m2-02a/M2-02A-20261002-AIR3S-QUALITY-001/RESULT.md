# M2-02A Result — Model-Free Quality Signal Sanity Check

experiment_id: M2-02A-20261002-AIR3S-QUALITY-001
result: PASS
proposal_revision: 2
authorized_subject_version: 0fdebf44fc5241163f6dee47fcb189e07c5a9586
authorization_decision: HUMAN-M2-02A-AUTH-001

## Source provenance

source: Air3s_normal.MP4
source_sha256: cc8ace8fc18280d09318d29f5b7dbcc1b7b44d986c2d83035d4421e0d927bcaa

Accepted M2-01 source-frame hashes were independently reconstructed in both runs:
- p10 ordinal 34: 0d93db5b47abe64cff7ac5bd1655c1a152f6232862f456f7e583ba81c085dd42
- p50 ordinal 168: 5d51447c5db413e2e49037e3802076c06b6b369ed8bc6fed998ca36d16e0f1cc
- p90 ordinal 302: dd59b335099a9173fa66525be80f86cdecb1bf0d13c2c345ae113ea08a71ac4b

All six source reconstruction commands exited 0.

## Runtime

- Python 3.13.5
- OpenCV 4.13.0
- NumPy 2.3.5
- FFmpeg 7.1.5-0+deb13u1
- no new installation
- no pretrained model
- transient script SHA-256: 5303411470dc64baed474c719880bf8b3e1a30bc75675435342e9accdd699523

## Frozen transforms

- ORIGINAL: identity
- BLUR_SIGMA4: cv2.GaussianBlur(... sigmaX=4.0, sigmaY=4.0, borderType=cv2.BORDER_DEFAULT)
- DARK_MINUS96: uint8 -> int16 -> subtract 96 -> clip 0..255 -> uint8
- BRIGHT_PLUS96: uint8 -> int16 -> add 96 -> clip 0..255 -> uint8

No parameter was changed after results were observed.

## Reproducibility

Run A: 12 states, exit 0.
Run B: 12 states, exit 0.

After excluding only run_id, there were zero field differences between corresponding Run A and Run B metric rows.
This includes source identity, derived RGB24 SHA-256, dimensions, runtime versions, raw clipping counts and all metric values.

## Directional results

### p10
- Laplacian variance: 258.1664827912528 -> BLUR 1.3808717930152166
- mean gray intensity: 73.49754171489198 -> DARK 19.012452256944446; BRIGHT 160.90248758198302
- black count/fraction: 793888 / 0.095713734567901235 -> DARK 6344779 / 0.76494731385030867
- white count/fraction: 504320 / 0.060802469135802471 -> BRIGHT 973547 / 0.11737401138117284
- black clipping: EXERCISED_CONFIRMED
- white clipping: EXERCISED_CONFIRMED

### p50
- Laplacian variance: 259.44819342657763 -> BLUR 1.3803216628057933
- mean gray intensity: 73.393879846643514 -> DARK 18.941924430941359; BRIGHT 160.82400233892747
- black count/fraction: 783401 / 0.094449387538580246 -> DARK 6349221 / 0.76548285590277776
- white count/fraction: 501429 / 0.060453920717592591 -> BRIGHT 970909 / 0.11705596547067901
- black clipping: EXERCISED_CONFIRMED
- white clipping: EXERCISED_CONFIRMED

### p90
- Laplacian variance: 259.39372157700217 -> BLUR 1.3974620225588481
- mean gray intensity: 75.940783299575614 -> DARK 19.978889130015432; BRIGHT 163.04578993055554
- black count/fraction: 718724 / 0.086651716820987656 -> DARK 6176516 / 0.74466097608024695
- white count/fraction: 531184 / 0.064041280864197525 -> BRIGHT 1007883 / 0.12151367187500001
- black clipping: EXERCISED_CONFIRMED
- white clipping: EXERCISED_CONFIRMED

## PASS gate

- reproducibility: PASS
- blur direction on p10/p50/p90: PASS
- dark mean-gray direction on p10/p50/p90: PASS
- bright mean-gray direction on p10/p50/p90: PASS
- black fraction no-decrease: PASS
- black clipping exercised: PASS on p10/p50/p90
- white fraction no-decrease: PASS
- white clipping exercised: PASS on p10/p50/p90
- provenance: PASS

Overall: PASS.

## Meaning

PASS establishes only that the selected classical metrics are deterministic on these tested inputs and react in the expected direction to the three frozen controlled transformations, while preserving M2-01 provenance.

PASS does NOT establish:
- natural good/bad Air 3S quality discrimination,
- operator usefulness,
- production thresholds,
- false-positive/false-negative behavior,
- a quality gate,
- equivalence of synthetic blur/exposure transforms to natural capture failures,
- superiority over BRISQUE.

The next materially useful evidence, if separately authorized, should use naturally degraded Air 3S frames plus HUMAN quality judgment rather than multiplying synthetic sanity checks.

## Non-authorization

This result does not authorize BRISQUE, dependency installation, pretrained models, training, production thresholds, quality-gate implementation, M2-03+, BUILD orchestrator, merge, architecture freeze, flight/route execution or publish/release/deploy.
