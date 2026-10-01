# M1 Audit — Quality Gate

execution_status: NOT_RUN
pipeline_compatibility: NOT_TESTED

## Problem

Before defect/anomaly interpretation, MP must know whether a frame is usable enough to support inspection. Blur, over/underexposure and general degradation may otherwise create false anomalies or hide real defects.

## IIQC

repository: fwan133/IIQC
pinned_commit: b60ddf0aebe8bdafcdbf2e0122d51c63b60462c8

Source-derived role:
rapid in-flight UAV inspection image-quality assessment with feedback for recollection.

Source constraints:
- bridge/pose context;
- OpenCV plus 3D/pose/ROS/PCL/OctoMap-related machinery;
- no top-level LICENSE found;
- package.xml contains license TODO;
- inspected source includes inherited files carrying different license notices.

MP assessment:
REFERENCE_IMPLEMENTATION + LEARN.

REPLACES WHAT?:
inventing the quality→recollection architecture from zero.

Reason not to use directly now:
integration scope and licensing are disproportionate/unclear for a small post-flight quality gate.

## Framework-for-UAV-image-quality

repository: GattuPriyanka/Framework-for-UAV-image-quality
pinned_commit: 9344d90ca9f56bf7bd54623b090c794c8c68d3f9
license: no LICENSE found

Actual inspected metrics.py behavior:
- DFT blur metric;
- DCT blur metric;
- counts of near-white pixels >=250;
- counts of near-black pixels <=5;
- NIQE;
- BRISQUE;
- folder-level metric aggregation.

Dependencies include OpenCV, SciPy/scikit-image, libsvm and pybrisque.

MP assessment:
LEARN / PARK as code dependency.
It proves the metric family is not novel, but unclear licensing and older dependency stack make direct reuse unattractive.

## BRISQUE component

repository: rehanguha/brisque
pinned_commit: 42c854ef9278f09d047abb8600d5204f779eca52

Code license:
Apache-2.0.

Bundled default model artifacts:
- brisque/models/svm.txt
  - git blob: 19237f04eae11398a2a41b91a7ef8ad2bfc084d5
- brisque/models/normalize.pickle
  - git blob: 18ed3adf6991d0feba7b3cb832a247209f9f5cf1

Source behavior:
BRISQUE.__init__() uses these artifacts by default:
- svm_load_model(svm.txt)
- pickle.load(normalize.pickle)

The constructor also accepts a custom model_path with separate SVM and normalization artifacts.

Artifact history:
both default model files first appear in repository history in commit
10e2dd2a23ee597e788761b161bec1c60aa046fd
("Made a package out of the code and added the models.")

Model-artifact provenance/license status:
UNRESOLVED.

M1 does not establish:
- where the bundled SVM model was trained,
- what dataset/quality labels produced it,
- the independent origin of normalize.pickle,
- whether the repository Apache-2.0 terms are intended to cover these bundled model/data artifacts.

M1 also does not claim that Apache-2.0 excludes them.

Input:
image ndarray or URL.

Output:
no-reference BRISQUE quality score.

Dependencies:
NumPy, scikit-image, SciPy, libsvm-official, requests; OpenCV is required but selectable as an optional variant.

Compute:
CPU-suitable image metric; no GPU requirement stated.

Adapter:
THIN: image/frame -> numeric quality observation + provenance.

MP assessment:
EVALUATE in M2 as one quality signal, not as the complete gate.

Execution precondition:
Before M2-02 uses the default BRISQUE model, either:
1. resolve the provenance/terms applicable to svm.txt + normalize.pickle, or
2. use a custom BRISQUE model whose model/data provenance and terms are explicitly pinned and acceptable.

No training is authorized by this condition.

## Critical boundary

BRISQUE is not itself a defect detector and a high/low score is not automatically a RECHECK decision.

M1 does not define operational thresholds for:
- acceptable blur,
- acceptable exposure,
- BRISQUE pass/fail.

Thresholds need MP footage and human-inspection relevance.

## M1 proposed disposition

LEARN from IIQC architecture.
EVALUATE BRISQUE code (Apache-2.0) plus simple measurable blur/exposure signals in M2, subject to the separate model-artifact precondition above.
Do not adopt IIQC as a runtime dependency yet.

REPLACES WHAT?:
a bespoke image-quality model.

## M2 question

On a small set of visibly good/bad Air 3S frames, do existing no-reference/blur/exposure signals separate obviously unusable material well enough to justify a simple quality gate?
