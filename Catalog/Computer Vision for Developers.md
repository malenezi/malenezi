# Computer Vision for Developers
## رؤية الحاسب للمطورين

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Computer Vision for Developers |
| **Arabic Title** | رؤية الحاسب للمطورين |
| **Code** | SDA-AIE-212 |
| **Level** | Specialist |
| **Duration** | 5 days × 5 learning hours = **25 hours** |
| **Audience** | AI engineers specialising in vision applications |
| **Prerequisites** | SDA-AIE-112 |
| **Assessment** | Labs (60%) + vision-system project (40%) |
| **Stackability** | Vision specialisation badge · Elective within AI Engineer Specialist certificate · Next: SDA-AIE-216 |
| **Tools & Platforms** | PyTorch · torchvision · YOLO/Ultralytics · OpenCV · ONNX · ONNX Runtime · ByteTrack · FastAPI · Prometheus |

## Course Description

A specialist module for building production computer-vision capabilities. Participants develop image classification, object detection, and segmentation solutions using modern architectures and transfer learning. The module emphasises dataset curation, augmentation, and deployment of vision models to real applications.

The course is built around a single evolving artefact: **"Tamr Vision"**, a quality-inspection system for a date-packing plant in Al-Qassim. Participants build its input pipeline, fine-tune a grade classifier, train a defect detector and a surface-defect segmenter, curate and re-annotate its dataset, construct a rigorous evaluation harness, export and optimise the models for an edge box mounted over the conveyor, and finally take the system to video: tracking every fruit so it is decided once rather than forty times, serving it behind readiness gates, and monitoring it for the drift that quietly degrades every deployed vision system. Every lab produces a component of the final capstone, so by Day 5 each participant owns a complete, measured, deployable *and monitored* vision inspection system — the same shape of system they will operate at fleet scale in SDA-AIE-216 (MLOps).

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Implement image classification pipelines using CNNs and vision transformers
2. **LO2** — Develop object-detection and segmentation solutions with modern frameworks
3. **LO3** — Design dataset curation, labelling, and augmentation strategies
4. **LO4** — Apply transfer learning and fine-tuning to domain-specific vision tasks
5. **LO5** — Evaluate vision models using appropriate metrics such as mAP and IoU
6. **LO6** — Deploy optimised vision models to cloud and edge targets
7. **LO7** — Build multi-object tracking pipelines that turn per-frame detections into per-object decisions on video
8. **LO8** — Operate deployed vision systems: serve them safely, monitor for drift, and close the retraining loop

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Seeing like a machine | M1: Image Data, Preprocessing & Augmentation · M2: CNN Architectures & Vision Transformers | 45% | 55% | Working dates-qc input pipeline + fine-tuned grade classifier beating the frozen baseline |
| **Day 2** | Locate and delineate | M3: Object Detection with YOLO-Family Models · M4: Semantic & Instance Segmentation | 40% | 60% | Trained defect detector (mAP@0.5 ≥ 0.85) + surface-defect segmentation model |
| **Day 3** | Data is the system | M5: Dataset Curation & Annotation Workflows · M6: Model Evaluation for Vision Tasks | 40% | 60% | Curated dataset v2 + evaluation harness + written error-analysis report |
| **Day 4** | Ship it to the line | M7: Deployment & Edge Optimisation · Capstone assembly | 25% | 75% | ONNX-exported, benchmarked edge models + the assembled inspection pipeline running on sample footage |
| **Day 5** | Watch the line | M8: Video Analytics, Object Tracking & Production Monitoring · Capstone | 25% | 75% | Track-level decisions meeting the line's ejection budget, served and monitored + capstone demo of the full inspection system |

## Hour-by-Hour Breakdown

### Day 1 — Seeing Like a Machine

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why vision systems fail in production** + course kickoff | Recognise the gap between benchmark accuracy and line performance; meet the Tamr Vision scenario and the eight module themes | Interactive lecture + failure-story discussion | 80/20 |
| 2 | **Image data, preprocessing & augmentation** (M1) | Images as tensors; the preprocessing contract; augmentation as regularisation; input pipelines with torchvision + OpenCV | Lecture + live pipeline demo | 70/30 |
| 3 | **Lab 1 — Build the dates-qc input pipeline** | Custom Dataset, transforms v2 pipeline, augmentation visualisation, loader throughput measurement | Guided lab (pairs) | 10/90 |
| 4 | **CNN architectures & vision transformers** (M2) | Convolutional inductive bias; ResNet/EfficientNet families; ViT attention; transfer learning & fine-tuning strategy | Lecture + architecture walkthrough | 70/30 |
| 5 | **Lab 2a — Fine-tune the grade classifier** | Head-only vs full fine-tuning of ResNet-50 on dates-qc; log metrics per epoch | Guided lab (pairs) | 10/90 |

### Day 2 — Locate and Delineate

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Lab 2b — Classifier hardening + ViT comparison** | Discriminative learning rates, early stopping, test-time evaluation; swap in a ViT-B/16 and compare | Lab + micro-lecture | 20/80 |
| 2 | **Object detection with YOLO-family models** (M3) | Detection problem formulation; anchor-free single-stage detectors; Ultralytics training workflow; NMS and confidence tuning | Lecture + live training demo | 70/30 |
| 3 | **Lab 3 — Train the defect detector** | Train YOLO11s on the 5-class defect set; tune confidence/IoU thresholds against line requirements | Guided lab | 10/90 |
| 4 | **Semantic & instance segmentation** (M4) | Semantic vs instance vs panoptic; encoder-decoder and mask-head designs; YOLO-seg and Mask R-CNN; mask quality metrics | Lecture + mask visualisation demo | 70/30 |
| 5 | **Lab 4 — Segment surface defects** | Train YOLO11s-seg on defect masks; compute defect-area percentage per fruit; mIoU report | Guided lab | 10/90 |

### Day 3 — Data Is the System

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Dataset curation & annotation workflows** (M5) | Annotation specs and guidelines; inter-annotator agreement; active-learning loops; versioning datasets like code | Lecture + annotation-tool walkthrough | 60/40 |
| 2 | **Lab 5 — Audit and curate dataset v2** | Find label errors with model-assisted auditing; fix the annotation spec; produce versioned dates-qc v2 | Guided lab | 10/90 |
| 3 | **Model evaluation for vision tasks** (M6) | IoU, precision-recall, mAP@0.5 and mAP@0.5:0.95; confusion at the class and slice level; operating-point selection | Lecture + metric derivation on whiteboard | 70/30 |
| 4 | **Lab 6 — Build the evaluation harness** | Frozen eval split; per-class and per-slice metrics; error-analysis gallery; written findings | Guided lab | 10/90 |
| 5 | **Retrain on v2 + capstone kickoff** | Quantify the data-quality dividend (v1 vs v2 models); capstone requirements briefing; milestone M-A check | Lab + briefing | 20/80 |

### Day 4 — Ship It to the Line

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Deployment & edge optimisation** (M7) | ONNX export and graph verification; quantisation and input-size trade-offs; cloud vs edge targets; latency budgets | Lecture + export demo | 60/40 |
| 2 | **Lab 7 — Export, optimise, benchmark** | Export classifier + detector to ONNX; INT8 quantisation; measure latency/accuracy trade-off table | Guided lab | 10/90 |
| 3 | **Capstone assembly I** | Integrate classifier, detector, segmenter into the inspection pipeline; wire the decision logic | Project work | 0/100 |
| 4 | **Capstone assembly II + self-audit** | Complete the capstone checklist; fill BENCHMARKS.md from own runs; peer review round | Project work | 0/100 |
| 5 | **From stills to stream** (bridge to M8) | Camera geometry and the frames-per-fruit arithmetic; video decode throughput; extract and inspect the `dates-line-video` pack; milestone M-E gate | Micro-lecture + guided setup | 40/60 |

### Day 5 — Watch the Line

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Video analytics, object tracking & production monitoring** (M8) | Why per-frame decisions blow the ejection budget; tracking-by-detection and ByteTrack; track-level evidence; readiness gates and shadow→canary rollout; the drift layers and the runbook | Lecture + tracked-inference demo | 65/35 |
| 2 | **Lab 8 — Track, serve, and watch the line** | ByteTrack over the INT8 detector; track-level decision rule swept against the line spec; `/readyz` gates; drift replay; shadow rollout + review queue | Guided lab (pairs) | 10/90 |
| 3 | **Capstone assembly III** | Wire tracking, decision aggregation, and the drift monitor into the inspection system; run it end-to-end on line footage | Project work | 0/100 |
| 4 | **Capstone assembly IV + self-audit** | Complete the checklist and the extension; fill the remaining BENCHMARKS.md rows; peer review round; milestone M-G check | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 5-minute demos; rubric-based peer + instructor scoring; path to SDA-AIE-216 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module works on the same Tamr Vision inspection system and the same `dates-qc` dataset. Never introduce a throwaway dataset — always evolve the course artefact. This is what makes the capstone achievable in Day 4 Hours 3–4 and Day 5 Hours 3–4.
- **Pace control:** Labs 3 and 5 are the most overrun-prone (training time and annotation time respectively). Publish checkpoint weights and dataset snapshots (`lab3-start`, `lab3-best.pt`, `dates-qc-v2-reference`, ...) so stragglers can fast-forward without losing the thread.
- **Pairing:** rotate pairs each day. Pair a strong-PyTorch participant with a strong-domain-intuition participant; error analysis (Day 3) benefits most from mixed pairs.
- **Environment strategy:** primary = classroom workstations with NVIDIA GPUs (8 GB+ VRAM) or a provided cloud-notebook pool; fallback = CPU with reduced image size (320), reduced epochs, and provided pre-trained checkpoints for every lab. Verify both paths the week before delivery — a CV course with no working GPU plan collapses on Day 2.
- **Training-time discipline:** every lab caps training at ≤ 15 minutes wall-clock by design (small models, subset epochs, provided starting weights). If a pair's run exceeds it, they resume from the checkpoint — the learning is in the decisions, not the waiting.
- **Language:** deliver in English or Arabic; keep all code, identifiers, class names, and annotation labels in English (mixed-language label taxonomies break tooling and downstream regex-based reporting).
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day 3 Hour 2 (annotation lab) and the Day 4 and Day 5 afternoons are deliberately flexible for regional scheduling.
- **Assessment logistics:** rubric scoring happens live during Day 5 Hour 5 demos; collect repository URLs and BENCHMARKS.md at the end of Day 5 Hour 4 so evaluation-harness and monitoring results can be verified before demos begin.

---

# Module 1 — Image Data, Preprocessing, and Augmentation

## Module Overview

**Purpose.** Vision models are only as good as the tensors they see. This module builds the discipline that everything downstream depends on: understanding images as data (colour spaces, bit depth, resolution, memory), defining a preprocessing contract that is identical at train and inference time, and designing augmentation policies that encode domain knowledge instead of copying defaults. Participants leave with a measured, reproducible input pipeline for the course dataset.

**Business relevance.** Most production vision failures are input failures: a camera firmware update shifts white balance, a resize interpolation differs between the training script and the edge runtime, a BGR/RGB mix-up silently costs 8 points of accuracy. In Saudi industrial deployments — food processing, manufacturing QC, infrastructure inspection — imaging conditions are harsh and variable (dust, heat shimmer, mixed lighting), and augmentation is the cheapest robustness investment available. Getting the data layer right is also where PDPL exposure starts: images of people are personal data.

**Industry use cases.**
- A date-packing line where seasonal fruit colour variation between harvests degrades a classifier trained on one season — solved with photometric augmentation and per-batch normalisation audits.
- A hospital imaging group whose chest X-ray model collapsed on a new scanner model — root cause was a different DICOM windowing default, i.e., a preprocessing-contract violation.
- A smart-city traffic system where night/day and sandstorm conditions demand an augmentation policy tuned to Gulf conditions, not ImageNet defaults.

**Expected competencies.** After this module a participant can load and manipulate images correctly with OpenCV and torchvision, implement a custom PyTorch `Dataset` with transforms v2, compute dataset statistics for normalisation, design and visually verify an augmentation policy, and measure input-pipeline throughput so the GPU is never starved.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Explain image representation: colour spaces, channel order, bit depth, and tensor layout (NCHW) | LO1 |
| 1.2 | Implement a preprocessing contract shared by training and inference code | LO1, LO4 |
| 1.3 | Design an augmentation policy justified by domain invariances, and rule out invalid augmentations | LO3 |
| 1.4 | Build a custom torchvision Dataset/DataLoader pipeline and measure its throughput | LO1 |
| 1.5 | Detect data-quality problems: label noise, duplicates, leakage, and class imbalance | LO3 |

## Technical Content

### 1. Images as tensors

An 8-bit RGB image is a `H×W×3` array of integers in [0, 255]; PyTorch wants `N×C×H×W` float tensors, usually normalised. Everything in this chain is a potential bug:

- **Channel order:** OpenCV loads **BGR**; torchvision, PIL, and every pre-trained model expect **RGB**. A silent BGR/RGB swap does not crash — it just quietly degrades a fine-tuned model by 5–10 points. Rule: convert at the I/O boundary (`cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`) and never think about it again.
- **Dtype and range:** uint8 [0,255] → float32 [0,1] (`ToDtype(torch.float32, scale=True)`) → normalised by dataset (or ImageNet) mean/std. Feeding [0,255] floats to a model trained on [0,1] is the second-most-common silent bug.
- **Resolution and memory:** a 1280×1024 RGB frame is 3.9 MB as float32; a batch of 32 at 640×640 is ~157 MB *before* activations. Input size is the single biggest lever on both memory and latency — it is a *system* decision (M7 revisits it), not a training default.
- **Bit depth beyond 8:** industrial line-scan and medical sources produce 10–16-bit images; naive uint8 conversion destroys the dynamic range that carries the defect signal. Teach explicit windowing/scaling as part of the contract.

### 2. The preprocessing contract

Everything between the raw image and the model tensor is a versioned contract shared by training, evaluation, and deployment:

- **One function, imported by all three.** The course keeps `preprocess()` in `tamr_vision/data/transforms.py`; the training script, the eval harness (M6), and the ONNX inference wrapper (M7) all import it. Duplicated resize/normalise code is the vision equivalent of training/serving skew.
- **Resize semantics matter:** `bilinear` vs `nearest` vs `bicubic` interpolation, aspect-ratio-preserving letterbox (YOLO convention) vs plain stretch — each produces different tensors from the same image. Pin the choice and record it in the model card.
- **Normalisation statistics:** fine-tuning from ImageNet weights → use ImageNet mean/std; training from scratch on a narrow domain → compute the dataset's own statistics (Lab 1 does both and compares).
- **Determinism at inference:** augmentation is train-only. Eval and serving use the deterministic contract path — the reason transforms are split into `train_tf` and `eval_tf` from the first line of code.

### 3. Augmentation as encoded domain knowledge

Augmentation multiplies the effective dataset by transformations the model should be invariant to. The design question is always: *is this variation real on the line?*

- **Geometric:** horizontal/vertical flips, rotations, small scale/translation jitter. Dates on a conveyor arrive in any orientation → full rotation is valid. Chest X-rays do not arrive mirrored → horizontal flip is *invalid* there (it moves the heart). The validity test is domain, not fashion.
- **Photometric:** brightness/contrast jitter, hue/saturation shifts, simulated white-balance drift. This is the workhorse for industrial cameras whose exposure drifts with ambient light and lamp ageing.
- **Occlusion & noise:** random erasing, cutout, Gaussian/ISO noise, motion blur (conveyor speed!), dust simulation — directly modelling Gulf-environment degradations.
- **Detection/segmentation-aware:** geometric transforms must move boxes and masks with the pixels — torchvision transforms v2 and Ultralytics handle this natively; hand-rolled NumPy augmentation is where box/mask misalignment bugs breed. Mosaic and copy-paste (Ultralytics defaults) are detection-specific and covered in M3.
- **Policy strength:** augmentation is regularisation — too weak underfits robustness, too strong destroys label validity (a rotation that hides the mould spot changed the label). The visual-audit habit: render 32 augmented samples with labels and *look at them* before every training run.

### 4. Input pipelines that keep the GPU fed

- `Dataset.__getitem__` does I/O + decode + transform for one sample; `DataLoader` parallelises it across `num_workers` processes with `pin_memory=True` for fast host→GPU copies.
- **Measure, don't guess:** if GPU utilisation sawtooths, the pipeline is the bottleneck. Course rule of thumb targets: ≥ 400 img/s at 224², ≥ 150 img/s at 640² on classroom hardware.
- Decode cost dominates: JPEG decode of a 1280×1024 frame ≈ 8–12 ms on CPU. Mitigations in order: resize-on-disk to training resolution (dataset preparation step), more workers, and only then exotic solutions.
- **Deterministic loading for eval:** `shuffle=False`, fixed worker seeds, and a frozen file list — the eval harness (M6) must produce identical numbers run-to-run.

### 5. Data quality: the problems augmentation cannot fix

- **Label noise:** in industrial QC, 3–8% label error is typical at first annotation pass (M5 measures ours). Noise on the *reject* class is the expensive kind — it teaches the model that defects are acceptable.
- **Duplicates and near-duplicates:** consecutive conveyor frames of the same fruit leaking across train/val splits inflates every metric. Split by *fruit/session identity*, never by random frame.
- **Class imbalance:** rejects are (thankfully) rare — 2–4% of frames. Tools: weighted sampling, loss weighting, and honest per-class metrics (never accuracy alone; M6 formalises).
- **Leakage:** timestamps, camera-station watermarks, or background artefacts correlated with the label — the model learns the shortcut. Grad-CAM inspection (M2 lab stretch) is the detection tool.

### 6. Common mistakes & production considerations

1. BGR fed to an RGB-trained model — the classic silent killer; assert channel order at the I/O boundary.
2. Different resize interpolation in training (PIL bicubic) vs serving (OpenCV bilinear) — a real 2-point mAP loss; pin and test it.
3. Augmenting the validation set — metrics become noisy and optimistic; the train/eval transform split is non-negotiable.
4. Random train/val split over video-like frame sequences — near-duplicate leakage; split by session.
5. Normalising with ImageNet stats after training with dataset stats (or vice versa) — the contract must travel with the checkpoint.
6. Ignoring EXIF orientation — phones store rotation as metadata; PIL respects it, raw decoders may not; images silently arrive rotated 90°.

Production: preprocessing runs at inference too — its latency is part of the budget (M7); camera calibration and white-balance locking beat software correction; log a per-batch input-statistics fingerprint (mean/std/histogram) so input drift is detectable in monitoring (SDA-AIE-216 builds the alerting).

## Code Examples

### The preprocessing contract (single source of truth)

```python
# src/tamr_vision/data/transforms.py
"""THE preprocessing contract. Training, evaluation, and the ONNX
inference wrapper all import from here — never duplicate resize or
normalisation logic anywhere else in the codebase."""
import torch
from torchvision.transforms import v2

IMG_SIZE = 224                      # classifier input; detector uses 640 (M3)
IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)


def eval_tf() -> v2.Compose:
    """Deterministic path: eval harness AND production inference."""
    return v2.Compose([
        v2.Resize((IMG_SIZE, IMG_SIZE), interpolation=v2.InterpolationMode.BILINEAR),
        v2.ToDtype(torch.float32, scale=True),      # uint8 [0,255] -> float [0,1]
        v2.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
    ])


def train_tf() -> v2.Compose:
    """Augmentation policy for dates-qc. Every transform below is justified
    by a REAL line variation — see the policy table in the module content."""
    return v2.Compose([
        v2.Resize((IMG_SIZE, IMG_SIZE), interpolation=v2.InterpolationMode.BILINEAR),
        v2.RandomHorizontalFlip(p=0.5),             # conveyor has no left/right
        v2.RandomVerticalFlip(p=0.5),               # ...or up/down semantics
        v2.RandomRotation(degrees=180),             # fruit lands in any pose
        v2.ColorJitter(brightness=0.25, contrast=0.2,
                       saturation=0.2, hue=0.03),   # lamp ageing + exposure drift
        v2.RandomApply([v2.GaussianBlur(kernel_size=5)], p=0.15),  # motion blur
        v2.ToDtype(torch.float32, scale=True),
        v2.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
        v2.RandomErasing(p=0.15, scale=(0.02, 0.08)),  # partial occlusion by
    ])                                                 # neighbouring fruit
```

### Custom Dataset with correct I/O boundary

```python
# src/tamr_vision/data/dataset.py
"""dates-qc classification dataset. Images live under
data/dates-qc/images/, labels in a CSV manifest (one row per image,
split assigned by SESSION, not by frame — leakage defence)."""
from pathlib import Path

import cv2
import pandas as pd
import torch
from torch.utils.data import Dataset

GRADES = ["premium", "standard", "substandard", "reject"]  # frozen order


class DatesQCDataset(Dataset):
    def __init__(self, root: Path, split: str, transform=None):
        manifest = pd.read_csv(root / "manifest_v1.csv")
        self.rows = manifest[manifest["split"] == split].reset_index(drop=True)
        self.root, self.transform = root, transform

    def __len__(self) -> int:
        return len(self.rows)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, int]:
        row = self.rows.iloc[idx]
        img = cv2.imread(str(self.root / "images" / row["file"]))
        if img is None:                       # fail loudly, not with a black image
            raise FileNotFoundError(row["file"])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      # BGR->RGB at the boundary
        tensor = torch.from_numpy(img).permute(2, 0, 1)  # HWC uint8 -> CHW
        if self.transform:
            tensor = self.transform(tensor)
        return tensor, GRADES.index(row["grade"])
```

### Dataset statistics and loader throughput

```python
# scripts/dataset_stats.py
"""Compute per-channel mean/std and measure loader throughput.
Run BEFORE training: the numbers go into the model card."""
import time

import torch
from torch.utils.data import DataLoader
from torchvision.transforms import v2

from tamr_vision.data.dataset import DatesQCDataset

ds = DatesQCDataset(root="data/dates-qc", split="train",
                    transform=v2.Compose([
                        v2.Resize((224, 224)),
                        v2.ToDtype(torch.float32, scale=True)]))
loader = DataLoader(ds, batch_size=64, num_workers=8, pin_memory=True)

n, mean, sq = 0, torch.zeros(3), torch.zeros(3)
t0 = time.perf_counter()
for batch, _ in loader:
    n += batch.shape[0]
    mean += batch.mean(dim=(0, 2, 3)) * batch.shape[0]
    sq += (batch ** 2).mean(dim=(0, 2, 3)) * batch.shape[0]
elapsed = time.perf_counter() - t0
mean /= n
std = (sq / n - mean ** 2).sqrt()
print(f"mean={mean.tolist()}  std={std.tolist()}")
print(f"throughput: {n / elapsed:,.0f} img/s over {n:,} images")
```

### Augmentation visual audit (the habit that prevents label-destroying policies)

```python
# scripts/aug_audit.py
"""Render a 4x8 grid of augmented samples WITH labels. Look at it before
every training run: would a human still assign the same grade?"""
import matplotlib.pyplot as plt

from tamr_vision.data.dataset import GRADES, DatesQCDataset
from tamr_vision.data.transforms import IMAGENET_MEAN, IMAGENET_STD, train_tf

ds = DatesQCDataset(root="data/dates-qc", split="train", transform=train_tf())
fig, axes = plt.subplots(4, 8, figsize=(16, 8))
for ax in axes.flat:
    img, label = ds[int(torch.randint(len(ds), ()))]
    img = img * torch.tensor(IMAGENET_STD)[:, None, None] \
              + torch.tensor(IMAGENET_MEAN)[:, None, None]   # un-normalise
    ax.imshow(img.clamp(0, 1).permute(1, 2, 0))
    ax.set_title(GRADES[label], fontsize=8)
    ax.axis("off")
fig.savefig("reports/aug_audit.png", dpi=120, bbox_inches="tight")
```

## Hands-on Lab 1 — Build the dates-qc Input Pipeline

| | |
|---|---|
| **Objective** | Implement the Dataset + transforms contract, compute dataset statistics, visually audit the augmentation policy, and measure loader throughput |
| **Duration** | 50 minutes |
| **Setup** | Python 3.12, PyTorch ≥ 2.4, torchvision ≥ 0.19, OpenCV; course repo cloned; `dates-qc` bundle extracted; `git checkout lab1-start` |

**Instructions & tasks**

1. *(5 min)* Explore the bundle: `data/dates-qc/images/` (12,000 frames, 1280×1024) and `manifest_v1.csv`. Confirm the split column is assigned by `session_id`, and find how many sessions exist per split.
2. *(10 min)* Implement `DatesQCDataset` per the template; the starter contains a deliberate bug (`cv2.imread` output used without colour conversion) — find and fix it, then add an assertion test that a known red-flagged sample has `R > B` mean.
3. *(10 min)* Implement `train_tf()` / `eval_tf()` in `transforms.py`. For each augmentation, add a one-line comment naming the *line variation* it models — no comment, no transform.
4. *(10 min)* Run `scripts/dataset_stats.py`: record mean/std and throughput in `BENCHMARKS.md`. Vary `num_workers` in {0, 4, 8} and record all three throughputs.
5. *(10 min)* Run `scripts/aug_audit.py`; inspect the grid with your pair. Identify at least one sample where the policy is too strong (label no longer assignable) and adjust one parameter with justification.
6. *(5 min)* Commit: `feat(data): dates-qc pipeline with audited augmentation policy`.

**Expected output**
```
$ python scripts/dataset_stats.py
mean=[0.412, 0.331, 0.247]  std=[0.201, 0.178, 0.154]
throughput: 118 img/s (workers=0) -> 465 img/s (workers=8)
reports/aug_audit.png written (32 samples, labels legible)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Grid images look blue/orange | BGR not converted | `cv2.cvtColor(..., COLOR_BGR2RGB)` at the I/O boundary |
| Throughput stuck at ~120 img/s | `num_workers=0` (default) | Raise workers; on Windows guard with `if __name__ == "__main__":` |
| `Normalize` error: expected float | `ToDtype` missing / order wrong | Convert dtype *before* Normalize |
| Val metrics change run-to-run later | Augmentation applied to val split | Use `eval_tf()` for val/test — check the loader wiring |

**Instructor notes.** The BGR bug is planted so that everyone experiences the most expensive silent bug in applied CV on Day 1 Hour 3, where it costs 5 minutes instead of a production incident. During the aug-audit debrief, ask each pair for one transform they *rejected* and why — the rejections show whether the domain-invariance idea landed. Fast finishers: compute stats at 640² and compare throughput — a preview of the detection-input cost in M3.

## Mini Exercises

**Quiz (5 questions)**
1. OpenCV loads channel order ___ ; torchvision models expect ___ → BGR; RGB.
2. Why must train and eval transforms be different objects? → augmentation is train-only regularisation; eval/serving need the deterministic contract.
3. Splitting conveyor frames randomly inflates metrics because ___ → near-duplicate frames of the same fruit leak across splits.
4. Which normalisation statistics for fine-tuning from ImageNet weights? → ImageNet mean/std (match the pre-training contract).
5. True/False: rotating a chest X-ray 180° is a valid augmentation because rotation is geometric. → **False** — validity is a domain question, not a category question.

**Debugging exercise.** Branch `sim-interp-skew`: training resized with bicubic (PIL), the provided "deployment" script resizes with nearest (OpenCV). Accuracy on the same split differs by 3.1 points. Participants must isolate the cause by diffing tensors from the two paths on one image, then unify via the contract module.

**Code-review exercise.** Review a PR that (a) normalises inside `__getitem__` with hard-coded stats, (b) applies `ColorJitter` to the val loader, and (c) splits train/val with `random_split` over frames. Three findings with the production consequence of each.

**Discussion questions.**
- The line manager offers to install diffuse lighting and lock camera exposure. Which augmentations could you then *remove*, and why is removing them good? (hardware fixes beat software compensation; weaker policy → faster convergence, tighter distribution)
- Your dataset contains workers' hands in frame. What does PDPL imply for storage, annotation vendor access, and augmentation? (personal data: minimise, mask/crop, restrict vendor exposure, retention policy)

## Case Study — Chest X-ray Preprocessing at a Riyadh Hospital Group

**Scenario.** A three-hospital group deploys a pneumonia-triage classifier trained on public datasets plus local scans. After a scanner fleet upgrade at one site, sensitivity drops from 0.91 to 0.74 — only at that site — and nobody notices for five weeks because aggregate metrics stay acceptable.

**Business context.** Radiology backlog is the reason the model exists; a silent per-site failure re-creates the backlog while showing green dashboards. The health regulator's AI guidance requires documented input-processing controls and post-deployment monitoring evidence.

**Technical challenge.** Diagnose the site-specific degradation and design a preprocessing contract + monitoring scheme that catches the next drift within a day, not five weeks.

**Constraints.** DICOM sources from three vendors with different bit depths and default windowing; no patient images may leave hospital premises (on-prem only); horizontal flip and aggressive intensity augmentation are clinically invalid; the fix must not require retraining from scratch.

**Solution approach (facilitate, don't lecture).** Root cause: the new scanner exports 12-bit DICOM with a different rescale slope; the ingestion code assumed 8-bit, crushing the intensity range. Fix: explicit windowing in a versioned preprocessing contract, applied identically in training and inference; add per-site input-statistics fingerprints (mean/std/histogram distance) with alerts; fine-tune on a small post-upgrade sample rather than full retrain; add scanner-model metadata to every prediction log for slice-level monitoring (M6 tie-in).

**Discussion questions.**
1. Why did aggregate metrics hide a 17-point per-site drop, and what reporting structure prevents this? (slice-level evaluation — M6)
2. Which augmentations are valid for chest X-rays, and who signs off — engineers or radiologists?
3. Design the input-fingerprint alert: which statistics, what baseline, what threshold?
4. The vendor offers a cloud preprocessing service. Argue the on-prem position under local health-data rules.

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Loader throughput (224², bs=64) | Performance | ≥ 400 img/s | `dataset_stats.py` |
| GPU utilisation during a training epoch | Performance | ≥ 85% mean | `nvidia-smi dmon` during Lab 2 |
| Train/eval transform separation | Code quality | Enforced (two functions, no shared mutation) | code review checklist |
| Session-based split integrity | Reliability | 0 sessions spanning splits | manifest audit script |
| Augmentation policy justification | Code quality | 100% of transforms commented with the modelled variation | review |
| Duplicate leakage across splits | Reliability | 0 near-duplicate pairs (pHash distance < 8) | provided audit script |

**Example benchmark table (filled during lab):**

| Configuration | Throughput (img/s) | Epoch time (12k imgs) | GPU util |
|---|---|---|---|
| workers=0 | 118 | 102 s | 31% |
| workers=4, pin_memory | 361 | 34 s | 78% |
| workers=8, pin_memory | 465 | 27 s | 91% |

## Required Visuals and Training Assets

### Diagrams
1. **The preprocessing contract** — *Purpose:* anchor image for the data layer. *Elements:* one `transforms.py` box feeding three consumers (training loop, eval harness, ONNX wrapper); a red "skew" variant with duplicated resize logic diverging. *Style:* hub-and-spoke, course palette, English labels with Arabic subtitles. *Designer description:* "Central module box with three arrows out; mirrored 'before' panel shows three separate boxes with slightly different parameter text highlighted in red."
2. **Image-to-tensor journey** — *Elements:* camera frame → BGR array → RGB → CHW uint8 → float [0,1] → normalised tensor, with dtype/shape annotated at every step and the two classic bugs (BGR, [0,255] floats) marked as red exits. *Style:* horizontal pipeline strip, printable A4.
3. **Augmentation validity matrix** — *Elements:* grid of transforms × three domains (dates line, chest X-ray, traffic cam) with ✓/✗ and a one-word reason per cell. *Style:* table poster — the module's discussion artefact.
4. **Split-by-session vs split-by-frame** — *Elements:* conveyor frame sequence coloured by session; correct split (whole sessions per split) vs leaking split (frames interleaved) with a metric-inflation callout. *Style:* before/after split panel.

### Images (screenshots)
1. **`aug_audit.png` reference grid** — *why:* participants compare their grid against it; *content:* 32 augmented date images with grade labels, one deliberately over-augmented sample circled.
2. **Terminal screenshot — `dataset_stats.py` output** — *why:* expected-output reference; *content:* mean/std + three throughput lines for worker counts.
3. **BGR-bug side-by-side** — *why:* make the silent bug visible; *content:* same date image rendered from BGR and RGB paths, colour cast obvious.
4. **`nvidia-smi dmon` during starved vs fed training** — *why:* connects pipeline throughput to GPU economics; *content:* sawtooth vs steady utilisation traces.

### Simulations
1. **Interpolation skew** — *Setup:* branch `sim-interp-skew` (bicubic-vs-nearest mismatch). *Expected behaviour:* 3-point accuracy gap on identical data; tensor diff localises it. *Learning objective:* the contract must include resize semantics, not just size.
2. **Leaky split** — *Setup:* branch `sim-leaky-split` re-splits the manifest by frame. *Expected behaviour:* val accuracy jumps ~4 points with no model change; pHash audit exposes duplicates. *Learning objective:* metric inflation via near-duplicate leakage.

### Interactive Activities
- **Augmentation courtroom (15 min):** instructor projects one transform at a time for the dates domain; pairs vote valid/invalid and must defend with a line-condition argument; the validity matrix poster is filled live.
- **Pipeline speed hunt (10 min):** pairs get a deliberately slow loader config (workers=0, no pin_memory, decode at full 1280×1024) and race to 3× throughput, documenting each change's contribution.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `dates-qc` v1 | Course team: staged captures + synthetic composites of date fruit on conveyor, Saudi packing-line conditions | JPEG + CSV manifest | 12,000 imgs (1280×1024), 4 grade classes | Golden-thread dataset, all modules |
| `manifest_v1.csv` | Course team | CSV | 12,000 rows | Session-based splits, grade labels |
| pHash duplicate index | Generated by audit script | parquet | — | Leakage audit exercise |

### Demo Requirements
- **Instructor demo:** live BGR/RGB comparison on the projector (same image, two colour casts, two model confidences); then the worker-count throughput ladder measured live.
- **Student demo:** two pairs present their augmentation grid and defend one transform they rejected.
- **Expected outputs:** every pair has a working pipeline, recorded stats, and an audited policy committed before Day 1 Hour 4.

---

# Module 2 — CNN Architectures and Vision Transformers

## Module Overview

**Purpose.** This module gives participants working command of the two architecture families that dominate applied vision — convolutional networks and vision transformers — not as trivia but as engineering choices with measurable consequences. The centrepiece skill is transfer learning: taking ImageNet-pre-trained backbones and fine-tuning them into domain specialists with hundreds, not millions, of labelled images.

**Business relevance.** Almost no Saudi enterprise trains vision models from scratch; the economics of the field are pre-train once (someone else), fine-tune everywhere (you). An engineer who can choose the right backbone, freeze the right layers, and set the right learning-rate schedule delivers a production-grade classifier in an afternoon on a few thousand images. Choosing wrongly wastes GPU budget and — worse — ships a model too heavy for the deployment target (M7 makes this concrete).

**Industry use cases.**
- The Tamr Vision grade classifier: ResNet-50 fine-tuned on 9,000 labelled dates reaches macro-F1 0.91 in 12 minutes of training — from-scratch training on the same data plateaus at 0.72.
- A government land-registry service classifying satellite tiles (built-up / agricultural / desert) with a ViT fine-tuned on 15k tiles — attention maps double as audit evidence for disputed classifications.
- An insurer's vehicle-damage triage model where an EfficientNet-B0 was chosen over a ViT-L purely on the 60 ms mobile latency budget.

**Expected competencies.** Participants can explain convolutional and attention-based inductive biases, select a torchvision backbone against accuracy/latency/data-size constraints, implement head-replacement and staged fine-tuning with discriminative learning rates, run a disciplined training loop with early stopping, and read training curves to diagnose over/underfitting.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Explain convolutional inductive bias (locality, weight sharing, hierarchy) and ViT global attention | LO1 |
| 2.2 | Select a backbone for a task using accuracy/params/latency trade-off data | LO1, LO6 |
| 2.3 | Implement transfer learning: head replacement, layer freezing, discriminative learning rates | LO4 |
| 2.4 | Run a reproducible training loop with checkpointing, early stopping, and metric logging | LO1, LO4 |
| 2.5 | Diagnose training pathologies (overfitting, LR too high, frozen-too-much) from curves | LO1, LO5 |

## Technical Content

### 1. Convolutional inductive bias

A convolution layer encodes three assumptions about images: **locality** (nearby pixels relate), **translation equivariance** (a defect is a defect anywhere in the frame), and **hierarchy** (edges → textures → parts → objects as depth grows). These assumptions are why CNNs learn from small datasets: the architecture already "knows" image structure the way a transformer must learn it from data.

Landmarks participants must recognise on sight:
- **ResNet (2015):** skip connections make 50–150-layer networks trainable by letting gradients bypass blocks. ResNet-50 remains the default fine-tuning workhorse — boring, robust, everywhere.
- **EfficientNet (2019):** compound scaling of depth/width/resolution; B0–B7 trade accuracy against compute smoothly — the family to reach for when the deployment budget is tight.
- **ConvNeXt (2022):** a CNN modernised with transformer-era training recipes; competitive with ViTs while keeping CNN deployment simplicity — a good "best of both" teaching point.

### 2. Vision transformers

ViT slices the image into 16×16 patches, embeds each as a token, and runs a standard transformer encoder: every patch attends to every patch from layer one. Consequences:

- **Global receptive field immediately** — long-range relations (two distant defects, whole-scene context) are natural, not built up through depth.
- **Weak inductive bias** — ViTs need large pre-training data (ImageNet-21k, LAION) to match CNNs; *fine-tuned from strong pre-training they excel; trained from scratch on 10k images they lose to ResNet decisively* (Lab 2b demonstrates exactly this trade).
- **Quadratic attention cost in tokens** — resolution scales badly; 640² inputs are expensive. Swin's shifted-window attention restores locality/hierarchy and is the common backbone inside detection/segmentation frameworks.
- **Attention maps as interpretability** — where the model looked, useful for audits and error analysis (M6 uses Grad-CAM for CNNs and attention rollout for ViTs).

**Selection heuristic taught in class:** < 10k images + tight latency → CNN (ResNet/EfficientNet). Large fine-tuning sets, global context, or multimodal roadmap → ViT family. Edge targets: check ONNX/quantisation support *first* (M7) — a model you cannot ship is a model you do not have.

### 3. Transfer learning mechanics

The course's staged recipe (Lab 2 implements it verbatim):

1. **Replace the head:** swap the 1000-class ImageNet classifier for a fresh `Linear(2048, 4)`; everything else keeps pre-trained weights.
2. **Stage 1 — head-only (freeze backbone):** train the new head 2–3 epochs at lr=1e-3. Cheap, stable, gets the head into the right region before backbone weights move.
3. **Stage 2 — unfreeze with discriminative LRs:** backbone at lr=1e-5–1e-4, head at 1e-3. Early layers hold generic features (edges/textures — keep them); later layers hold ImageNet-specific semantics (adapt them). Cosine decay + 1–2 warmup epochs.
4. **Stop by validation macro-F1** (not loss, not accuracy — imbalance!): patience 3, restore best checkpoint.

When does full fine-tuning beat head-only? When the domain gap is large (conveyor dates are far from ImageNet photos) and data is sufficient (thousands, not dozens). With < 500 images, freeze more; with heavy imbalance, weight the loss (`CrossEntropyLoss(weight=...)`) or oversample — both shown in the lab.

### 4. The training loop as an engineering artefact

Reproducibility discipline (carried from SDA-AIE-113 practices into vision):
- Seed everything (`torch.manual_seed`, loader workers, cudnn determinism flag for eval); log the seed.
- Every run writes: config snapshot, per-epoch metrics CSV, best checkpoint with the *preprocessing contract reference* and class order baked into the file.
- Mixed precision (`torch.autocast` + `GradScaler`) halves memory and speeds training ~1.7× on classroom GPUs — on by default in the course loop.
- Metric logging is per-class from day one: aggregate accuracy hides the reject class (2–4% of data, 90% of the business value).

### 5. Reading training curves

The diagnostic table participants memorise:

| Symptom | Likely cause | First fix |
|---|---|---|
| Train loss ↓, val F1 ↓ after epoch k | Overfitting | More augmentation, earlier stop, more freezing |
| Both losses plateau high | Underfitting / LR too low / frozen too much | Unfreeze stage 2, raise head LR |
| Loss spikes to NaN or oscillates | LR too high (esp. unfrozen backbone) | 10× lower backbone LR, add warmup |
| Val F1 noisy run-to-run > 2 pts | Tiny val set / augmented val / unseeded | Fix eval determinism (M1 rules) |
| Great val, poor line performance | Distribution shift or leakage | Slice evaluation (M6), audit splits |

### 6. Common mistakes & production considerations

1. Fine-tuning the whole network at lr=1e-3 — destroys pre-trained features in one epoch ("catastrophic forgetting" live demo, simulation 1).
2. Forgetting `model.eval()` at validation/inference — dropout and batch-norm in train mode corrupt every downstream number.
3. Reporting accuracy on 94%-majority data — the do-nothing classifier scores 0.94; macro-F1 or per-class recall is the honest headline.
4. Choosing the leaderboard-best architecture with no latency measurement — deployment target vetoes architecture (M7 closes the loop).
5. Batch-norm statistics corrupted by tiny batches (< 8) during fine-tuning — freeze BN layers or use larger batches.
6. Saving `state_dict` without class order and preprocessing reference — the checkpoint that cannot be served correctly.

Production: keep a **model card** per checkpoint (data version, contract version, metrics per class, intended operating point); version checkpoints alongside dataset versions (M5); a fine-tuned model inherits pre-training biases — probe with slice evaluation before regulated deployment.

## Code Examples

### Building the transfer model

```python
# src/tamr_vision/models/classifier.py
"""Grade classifier: ResNet-50 backbone, staged fine-tuning support."""
import torch
from torch import nn
from torchvision.models import ResNet50_Weights, resnet50

NUM_CLASSES = 4  # premium / standard / substandard / reject — frozen order


def build_model(pretrained: bool = True) -> nn.Module:
    weights = ResNet50_Weights.IMAGENET1K_V2 if pretrained else None
    model = resnet50(weights=weights)
    model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)  # new head
    return model


def freeze_backbone(model: nn.Module) -> None:
    """Stage 1: only the new head trains."""
    for name, p in model.named_parameters():
        p.requires_grad = name.startswith("fc.")


def param_groups(model: nn.Module, lr_backbone: float, lr_head: float):
    """Stage 2: discriminative learning rates."""
    backbone = [p for n, p in model.named_parameters()
                if not n.startswith("fc.") and p.requires_grad]
    head = [p for n, p in model.named_parameters() if n.startswith("fc.")]
    return [{"params": backbone, "lr": lr_backbone},
            {"params": head, "lr": lr_head}]
```

### The training loop (excerpt — full version in course repo)

```python
# src/tamr_vision/train/loop.py
"""Reproducible fine-tuning loop: AMP, per-class metrics, early stopping.
Every run writes runs/<name>/{config.json, metrics.csv, best.pt}."""
import torch
from torch import nn
from torch.amp import GradScaler, autocast


def train_epoch(model, loader, optimizer, scaler, device, class_weights):
    model.train()
    criterion = nn.CrossEntropyLoss(weight=class_weights.to(device))
    for imgs, labels in loader:
        imgs, labels = imgs.to(device, non_blocking=True), labels.to(device)
        optimizer.zero_grad(set_to_none=True)
        with autocast(device_type="cuda", dtype=torch.float16):
            loss = criterion(model(imgs), labels)
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()


@torch.no_grad()
def evaluate(model, loader, device, num_classes: int = 4):
    """Deterministic eval: model.eval() is NOT optional."""
    model.eval()
    confusion = torch.zeros(num_classes, num_classes, dtype=torch.long)
    for imgs, labels in loader:
        preds = model(imgs.to(device)).argmax(dim=1).cpu()
        for t, p in zip(labels, preds):
            confusion[t, p] += 1
    per_class_recall = confusion.diag() / confusion.sum(1).clamp(min=1)
    per_class_prec = confusion.diag() / confusion.sum(0).clamp(min=1)
    f1 = 2 * per_class_prec * per_class_recall / \
        (per_class_prec + per_class_recall).clamp(min=1e-8)
    return {"macro_f1": f1.mean().item(),
            "per_class_recall": per_class_recall.tolist(),
            "confusion": confusion.tolist()}
```

### Staged fine-tuning driver

```python
# scripts/train_classifier.py
"""Stage 1 (head-only) then Stage 2 (discriminative LRs), early stopping
on val macro-F1. Checkpoint embeds class order + contract version."""
import json

import torch
from torch.amp import GradScaler

from tamr_vision.data.dataset import GRADES, DatesQCDataset
from tamr_vision.data.transforms import eval_tf, train_tf
from tamr_vision.models.classifier import build_model, freeze_backbone, param_groups
from tamr_vision.train.loop import evaluate, train_epoch

torch.manual_seed(212)
device = "cuda" if torch.cuda.is_available() else "cpu"
model = build_model().to(device)
# class weights: inverse frequency, reject gets ~18x — the business class
weights = torch.tensor([0.6, 0.8, 2.4, 18.1])

# ---- Stage 1: head only, 2 epochs ----
freeze_backbone(model)
opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=1e-3)
scaler = GradScaler()
for _ in range(2):
    train_epoch(model, train_loader, opt, scaler, device, weights)

# ---- Stage 2: full network, discriminative LRs, patience 3 ----
for p in model.parameters():
    p.requires_grad = True
opt = torch.optim.AdamW(param_groups(model, lr_backbone=5e-5, lr_head=1e-3))
sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=10)
best_f1, patience = 0.0, 0
for epoch in range(10):
    train_epoch(model, train_loader, opt, scaler, device, weights)
    sched.step()
    metrics = evaluate(model, val_loader, device)
    print(f"epoch {epoch}: macro_f1={metrics['macro_f1']:.4f} "
          f"reject_recall={metrics['per_class_recall'][3]:.4f}")
    if metrics["macro_f1"] > best_f1:
        best_f1, patience = metrics["macro_f1"], 0
        torch.save({"state_dict": model.state_dict(),
                    "classes": GRADES,                 # order travels with weights
                    "contract": "transforms.py@v1",    # preprocessing reference
                    "val_metrics": metrics}, "runs/grade_resnet50/best.pt")
    else:
        patience += 1
        if patience >= 3:
            break
```

### ViT comparison (Lab 2b)

```python
# scripts/train_vit.py  (delta from the ResNet driver)
from torchvision.models import ViT_B_16_Weights, vit_b_16

model = vit_b_16(weights=ViT_B_16_Weights.IMAGENET1K_SWAG_E2E_V1)
model.heads.head = torch.nn.Linear(model.heads.head.in_features, 4)
# Same staged recipe; note: lower backbone LR (2e-5) — ViTs are LR-fragile,
# and batch size may need halving (attention memory at 224² is ~2x ResNet-50).
```

## Hands-on Lab 2 — Fine-tune and Harden the Grade Classifier

| | |
|---|---|
| **Objective** | Fine-tune ResNet-50 on dates-qc with the staged recipe, beat the frozen course baseline (macro-F1 0.86), then compare a ViT-B/16 under identical conditions |
| **Duration** | 2 × 50 min (Day 1 H5 + Day 2 H1) |
| **Setup** | Lab 1 pipeline; GPU (or CPU fallback: 320² inputs, provided stage-1 checkpoint); `git checkout lab2-start` |

**Part A tasks (50 min)**
1. Implement `build_model`, `freeze_backbone`, `param_groups` (10 min).
2. Run Stage 1 (head-only, 2 epochs); record val macro-F1 — expect ~0.78 (10 min).
3. Run Stage 2 with discriminative LRs and early stopping; target macro-F1 ≥ 0.88, reject recall ≥ 0.95 (20 min, training runs ~8 min).
4. Deliberately re-run Stage 2 with a uniform lr=1e-3 on everything; watch macro-F1 collapse below Stage 1; keep both curves for the debrief (10 min).

**Part B tasks (50 min)**
1. Plot per-epoch curves for both runs; annotate where forgetting happens (10 min).
2. Swap in ViT-B/16 with the same recipe; record macro-F1, epoch time, params, and peak VRAM alongside ResNet-50 in `BENCHMARKS.md` (20 min).
3. Evaluate both best checkpoints on the frozen test split with `eval_tf()`; confirm run-to-run determinism (two identical runs) (10 min).
4. Commit: `feat(model): staged fine-tuned grade classifier + ViT comparison` (10 min).

**Expected outputs**
```
Stage 1 (head-only):        val macro_f1 ≈ 0.78
Stage 2 (discriminative):   val macro_f1 ≈ 0.90, reject recall ≈ 0.96 (epoch 5–7)
Stage 2 (uniform 1e-3):     val macro_f1 ≈ 0.61 — catastrophic forgetting
ViT-B/16:                   val macro_f1 ≈ 0.91, epoch time ≈ 1.8x ResNet, VRAM ≈ 2x
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| CUDA OOM in Stage 2 | Batch 64 too large with gradients everywhere | Halve batch, keep AMP on; ViT may need bs=16 |
| Val F1 = 0 on reject class | Weights tensor omitted / wrong order | Pass `class_weights`; verify GRADES order |
| Metrics differ between "identical" eval runs | `model.eval()` missing or augmented val loader | Audit the eval path against M1 rules |
| Loss NaN in first Stage-2 epoch | Backbone LR too high with AMP | Backbone 5e-5, add 1 warmup epoch |
| CPU fallback exceeds time box | Full-resolution + 10 epochs | Use 320², 3 epochs, provided checkpoint |

**Instructor notes.** The uniform-LR collapse (Part A task 4) is the module's money demo — every pair must *see* forgetting on their own curves, not on a slide. In the Part B debrief, build the class-wide comparison table (ResNet vs ViT: F1, time, VRAM, params) on the shared board; it becomes the evidence base for the M7 deployment discussion. Fast finishers: Grad-CAM on five misclassified rejects — do the heatmaps point at defects or at the conveyor belt (leakage probe)?

## Mini Exercises

**Quiz.** (1) Name the three convolutional inductive biases. → locality, translation equivariance (weight sharing), hierarchical features. (2) Why do ViTs need more pre-training data than CNNs? → weak inductive bias; structure must be learned from data. (3) Order of staged fine-tuning and why. → head-only first (stabilise the new head), then unfreeze with discriminative LRs (protect generic early features). (4) Why is macro-F1 the headline metric here rather than accuracy? → 94%-majority imbalance makes accuracy hide the reject class. (5) What must be saved with a checkpoint for it to be servable? → class order + preprocessing-contract reference (+ metrics/config).

**Debugging exercise.** Branch `sim-eval-mode`: validation numbers oscillate ±4 points between identical runs. Cause: `model.eval()` missing, so dropout is live during eval. Participants must find it by bisecting determinism (fixed seed, fixed data → still varies → the model call is stochastic).

**Code-review exercise.** Review a PR that (a) fine-tunes everything at lr=1e-2, (b) reports overall accuracy only, and (c) saves `best.pt` containing just `state_dict`. Three findings, each with the failure it causes downstream.

**Discussion.** The plant asks: "Why not train from scratch on our own data — isn't that more *ours*?" Construct the answer covering data requirements, cost, and what pre-trained weights actually contain (and the licensing check that must accompany them).

## Case Study — Satellite Land-Use Classification for a National Registry

**Scenario.** A national geospatial agency classifies 512×512 satellite tiles into seven land-use classes to detect unlicensed development. A contractor delivers a ViT-L/16 at 94.1% accuracy; the agency's own team counters with EfficientNet-B3 at 92.8%. Procurement must choose.

**Business context.** The model back-fills 11 years of imagery (2.1 billion tiles) on a fixed on-prem GPU cluster, then runs monthly deltas. Disputed classifications feed legal enforcement, so every decision may be challenged and must be explainable to a review board.

**Technical challenge.** Frame the choice properly: it is not 94.1 vs 92.8 — it is throughput on the back-fill (ViT-L is 5.3× slower → 14 months vs 2.6 months of cluster time), per-class recall on the two legally sensitive classes, and evidence quality (attention rollout vs Grad-CAM) for the review board.

**Constraints.** Cluster capacity is fixed (budget cycle closed); the two sensitive classes have only 3,100 labelled tiles combined; desert glare and seasonal agriculture cause known confusions; all imagery is classified — no cloud processing.

**Solution approach.** Decision matrix over throughput, sensitive-class recall, VRAM, explainability artefact quality. Likely resolution: EfficientNet-B3 for the bulk back-fill; a ViT fine-tuned specifically on the two sensitive classes as a second-stage referee on flagged tiles only — a cascade that buys ViT quality where it matters at 4% of the compute. Class-imbalance handling via weighted loss + targeted augmentation; disputed-tile evidence pack standardised on heatmap + top-k similar training tiles.

**Discussion questions.** (1) What single number should procurement have asked for instead of accuracy? (2) Design the cascade's routing rule — which tiles go to the referee model? (3) The review board asks "why did the model say built-up?" — compare attention rollout and Grad-CAM as legal evidence. (4) How would you spend a budget of 5,000 new labels?

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| Val macro-F1 (ResNet-50 staged) | Model quality | ≥ 0.88 | eval harness |
| Reject-class recall | Model quality | ≥ 0.95 | per-class metrics |
| Training wall-clock (Stage 1+2) | Performance | ≤ 15 min classroom GPU | run logs |
| Epoch time ResNet-50 @224, bs=64 | Performance | ≤ 30 s | metrics.csv |
| Eval determinism (2 identical runs) | Reliability | Δ macro-F1 = 0.0000 | repeated eval |
| Checkpoint completeness | Code quality | classes + contract + metrics embedded | checkpoint inspection |

**Example benchmark table:**

| Model | Val macro-F1 | Reject recall | Epoch time | Peak VRAM | Params |
|---|---|---|---|---|---|
| ResNet-50 head-only | 0.78 | 0.88 | 18 s | 3.1 GB | 25.6 M |
| ResNet-50 staged | 0.90 | 0.96 | 27 s | 5.4 GB | 25.6 M |
| ResNet-50 uniform 1e-3 | 0.61 | 0.42 | 27 s | 5.4 GB | 25.6 M |
| ViT-B/16 staged | 0.91 | 0.96 | 49 s | 10.8 GB | 86.6 M |

## Required Visuals and Training Assets

### Diagrams
1. **CNN vs ViT information flow** — *Purpose:* the module's anchor. *Elements:* left panel — image through conv blocks with growing receptive-field circles; right panel — image sliced into patches, all-to-all attention lines from layer 1; captions "learns structure through depth" vs "sees everything, must learn structure from data". *Style:* split panel, course palette. *Designer note:* keep attention lines sparse enough to read; highlight one patch's connections.
2. **Staged fine-tuning timeline** — *Elements:* two stages on a time axis; backbone lock icon in stage 1; per-layer LR gradient bar (cool→warm from early layers to head) in stage 2; validation-F1 curve overlaid with the early-stop marker. *Style:* horizontal timeline with an inset curve.
3. **Backbone selection decision tree** — *Elements:* branches for data size, latency budget, context needs, edge-format support, landing on ResNet/EfficientNet/ConvNeXt/ViT/Swin leaves with one-line justifications. *Style:* compact flowchart, printable.
4. **Catastrophic forgetting curve** — *Elements:* val-F1 curves for staged vs uniform-LR runs from the lab, divergence shaded, "pre-trained features destroyed" callout. *Style:* single annotated chart, doubles as a slide.

### Images (screenshots)
1. **Training-curves screenshot (staged run)** — *why:* expected-state reference; *content:* loss + macro-F1 + reject-recall per epoch with early-stop point marked.
2. **Class-wide comparison board photo/screenshot** — *why:* the ResNet-vs-ViT evidence table participants build; *content:* filled table matching the benchmark reference.
3. **Grad-CAM grid on misclassified rejects** — *why:* interpretability + leakage probing; *content:* 6 heatmaps, one clearly attending to the belt background (planted leakage sample).
4. **`nvidia-smi` during ViT vs ResNet training** — *why:* memory trade-off made visible; *content:* side-by-side VRAM readings.

### Simulations
1. **Catastrophic forgetting** — *Setup:* scripted in Lab 2 Part A task 4 (uniform lr=1e-3). *Expected:* macro-F1 collapse below the head-only baseline within 2 epochs. *Learning objective:* discriminative LRs protect pre-trained features.
2. **Eval-mode nondeterminism** — *Setup:* branch `sim-eval-mode` (missing `model.eval()`). *Expected:* ±4-point metric jitter across identical runs. *Learning objective:* train/eval mode discipline; determinism as a debugging axis.
3. **Background leakage** — *Setup:* a planted subset where reject-grade images were captured at one station with a distinctive belt scratch. *Expected:* Grad-CAM highlights the scratch, not the fruit; per-station slice metrics expose it. *Learning objective:* models learn shortcuts; interpretability + slicing find them (bridges to M6).

### Interactive Activities
- **Backbone auction (15 min):** four deployment briefs (edge camera, hospital on-prem, cloud batch, mobile app) are auctioned; pairs bid an architecture + justification; class votes on the best-argued fit.
- **Curve clinic (10 min):** instructor projects six anonymised training-curve sets from past cohorts; pairs diagnose each using the pathology table before the reveal.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `dates-qc` v1 (from M1) | Course bundle | JPEG + manifest | 12,000 imgs | Fine-tuning + comparison |
| Frozen course baseline checkpoint | Course team | .pt | 98 MB | The bar to beat (macro-F1 0.86) |
| Planted leakage subset index | Course team | CSV | 214 rows | Grad-CAM leakage probe |

### Demo Requirements
- **Instructor demo:** launch the staged run live at the start of Lab 2 and narrate the first curves; then trigger the uniform-LR run and let both race on the projector.
- **Student demo:** one pair presents their ResNet-vs-ViT table; one pair presents a Grad-CAM finding.
- **Expected outputs:** every pair enters Day 2 with a checkpoint beating macro-F1 0.86 and a filled comparison row in `BENCHMARKS.md`.

---

# Module 3 — Object Detection with YOLO-Family Models

## Module Overview

**Purpose.** Classification answers "what grade is this frame?"; the line needs "*where* is the defect, on *which* fruit, with *what* confidence?". This module moves participants from whole-image labels to localised predictions: the detection problem formulation, the anatomy of modern single-stage anchor-free detectors, the Ultralytics training workflow that has become the industry's fastest path from labelled boxes to a working model, and — the part most courses skip — the post-processing and threshold engineering that turns raw detections into line decisions.

**Business relevance.** Detection is the workhorse task of applied vision in the Kingdom: PPE compliance on construction megaprojects, vehicle and licence-plate detection at industrial-city gates, foreign-object detection on food lines, palm-pest spotting from drones. In every one of these, the deliverable is not mAP — it is a *thresholded decision* with an agreed miss rate and false-alarm rate. Engineers who can train a detector but cannot defend a confidence threshold against a line requirement ship systems that either stop the conveyor forty times an hour or wave mould through. The Ultralytics stack matters commercially too: it compresses detector development from weeks to hours, but its licensing (AGPL-3.0 vs commercial) is a procurement question participants must be able to answer.

**Industry use cases.**
- Tamr Vision's defect detector: YOLO11s trained on 4,200 box-annotated frames finds five defect types per fruit at 62 FPS on the line's GPU, replacing a whole-frame classifier that could not say *which* fruit to eject.
- A Jubail construction contractor detecting hard-hat and harness violations across 46 site cameras, where the safety officer's requirement was expressed as "no more than 1 missed violation in 20" — a recall constraint, not an accuracy number.
- A poultry processor near Al-Kharj detecting foreign objects (glove fragments, plastic) where a single escape triggers a retailer audit — the operating point lives at extreme recall and the false alarms are budgeted per shift.

**Expected competencies.** After this module a participant can formulate a task as detection (vs classification vs segmentation), prepare data in YOLO format with a correct dataset YAML, train and resume Ultralytics models with deliberate hyperparameter and augmentation choices, explain what the detector's losses optimise, tune confidence and NMS-IoU thresholds against explicit line requirements, and read a per-class PR curve well enough to know *which* threshold conversation to have with the business.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Formulate detection tasks: boxes, classes, confidence; choose detection over classification/segmentation deliberately | LO2 |
| 3.2 | Explain single-stage anchor-free detector anatomy: backbone, neck (FPN/PAN), decoupled head, and the loss components | LO2 |
| 3.3 | Prepare detection datasets in YOLO format and train with Ultralytics using justified hyperparameters | LO2, LO4 |
| 3.4 | Apply detection-specific augmentation (mosaic, copy-paste) and know when to disable it | LO3, LO4 |
| 3.5 | Tune confidence and NMS thresholds against explicit recall/false-alarm requirements | LO2, LO5 |

## Technical Content

### 1. The detection problem, formulated honestly

A detector maps an image to a *set* of `(box, class, confidence)` triples. Three consequences follow that shape everything else:

- **Sets, not vectors:** the output count varies per image, so evaluation needs a *matching* step (which prediction corresponds to which ground truth?) — IoU-based matching is the primitive under mAP, and M6 builds it by hand.
- **Localisation and classification are jointly learned but separately wrong:** a detector can find the fruit and mislabel the defect, or label correctly with a sloppy box. Error analysis must separate these (M6's error taxonomy).
- **Class definitions must be *boxable*:** "poor overall appearance" is a classification label; "skin_split" with visible extent is a detection label. Tamr Vision's defect taxonomy — `mould`, `skin_split`, `insect_damage`, `sugaring`, `foreign_object` — was designed so every class has a locatable extent. This is an annotation-spec decision (M5) made *before* any training.

When is detection the wrong tool? If the question is frame-level ("is this station dirty?") a classifier is cheaper; if the question is area-based ("what fraction of the surface is mouldy?") segmentation (M4) is needed. The course rule: *choose the cheapest task formulation that answers the business question.*

### 2. Anatomy of a modern single-stage detector

The YOLO family (You Only Look Once, 2016 → YOLO11, 2024) won industry adoption by doing detection in one forward pass. Participants must be able to sketch the three-part anatomy:

- **Backbone** — a CNN (CSP-based in modern YOLOs) that extracts feature maps at strides 8, 16, 32. Everything from M2 transfers: it is pre-trained, fine-tunable, and swap-able.
- **Neck** — feature pyramid aggregation (FPN top-down + PAN bottom-up): deep, semantically rich features are fused with shallow, spatially precise ones so that small objects (a 14-pixel mould spot at 640²) get both context and localisation.
- **Head** — modern YOLOs are **anchor-free** and **decoupled**: each feature-map cell predicts class scores and box coordinates directly (as distances to box edges, learned via distribution focal loss), rather than offsets from pre-defined anchor boxes. Anchor-free removed a whole class of tuning bugs (anchors mismatched to the dataset's box-shape distribution) that plagued YOLOv5-era deployments.

**Loss = box + classification + distribution.** CIoU loss aligns predicted and true boxes (penalising centre distance and aspect-ratio mismatch, not just overlap); binary cross-entropy scores classes; distribution focal loss (DFL) sharpens box-edge regression. Participants do not implement these, but they must recognise them in training logs — a plateauing `box_loss` with falling `cls_loss` means localisation, not recognition, is the bottleneck (usually an annotation-quality signal → M5).

**Two-stage detectors** (Faster R-CNN family) still matter as vocabulary: a region-proposal stage followed by per-region classification. They trade speed for slightly better small-object and crowded-scene performance and remain common in academic baselines and some medical tooling. The course teaches the trade-off table, then uses single-stage throughout — at Tamr Vision's 62 FPS requirement the choice makes itself.

### 3. The Ultralytics training workflow

Ultralytics collapsed the detection pipeline into three artefacts participants must control deliberately, not by copy-paste:

- **Label format:** one `.txt` per image; each line `class cx cy w h`, all normalised to [0,1]. The most common corruption is pixel coordinates written un-normalised — values > 1 that some versions silently clip. Lab 3's converter validates every line.
- **Dataset YAML:** paths to train/val images, class names *in frozen order*. The class-order rule from M2 applies with more teeth: reordering names in the YAML after training silently relabels every prediction.
- **Training call:** `model.train(data=..., epochs=..., imgsz=640, ...)`. The defaults are strong, which is exactly why participants must know the five that matter: `imgsz` (the latency/accuracy lever, revisited in M7), `batch`, `lr0` + `optimizer` (fine-tuning from COCO weights wants the default schedule; tiny datasets want lower LR), `patience` (early stopping), and the augmentation group.

**Detection-specific augmentation.** Mosaic (four images stitched into one training sample) and copy-paste (instances pasted across images) are Ultralytics defaults and are *why* small datasets work at all: they multiply object-context combinations and small-object exposure. Two disciplines: mosaic is disabled for the final ~10 epochs automatically (`close_mosaic`) because it distorts the global-layout statistics the model will see at inference; and copy-paste must respect physics — pasting a `foreign_object` mid-air above the conveyor teaches hallucination. The M1 visual-audit habit applies: render augmented batches with boxes *drawn* and look.

**Transfer learning positioning:** COCO-pre-trained weights already know "object on background"; fine-tuning teaches them "date defects specifically". On the course dataset, from-scratch training reaches mAP@0.5 ≈ 0.58 where COCO-initialised reaches ≈ 0.87 in the same 40 epochs — the M2 lesson, restated with boxes.

### 4. Post-processing: from raw predictions to line decisions

The raw head output at 640² is ~8,400 candidate boxes per image. Two filters produce the final set, and both are *tunable business decisions*:

- **Confidence threshold (`conf`):** discard candidates below it. Lower → more recall, more false alarms. The default 0.25 is a demo setting, not a production one.
- **Non-maximum suppression (`iou`):** among overlapping same-class boxes, keep the most confident; suppress others whose IoU with it exceeds the threshold. Too low → duplicate detections merged wrongly on touching fruit; too high → double-counting. Crowded conveyor scenes are exactly the hard case: dates touch, and NMS at `iou=0.45` vs `0.7` changes per-frame counts by ~9%.

**Operating-point engineering** is the module's capstone skill. The line requirement arrives in business language: *"mould escapes ≤ 1%, and ≤ 3 false ejections per 1,000 fruit."* The translation procedure: (1) sweep `conf` on the validation split; (2) plot per-class recall and false-positives-per-image against `conf`; (3) find the threshold band satisfying both constraints — or *prove no single threshold does*, forcing either per-class thresholds (supported: pass a dict) or a data conversation ("mould recall saturates at 0.93; we need 400 more hard mould examples" → M5's active learning). Participants leave knowing that "the model has mAP 0.87" and "the line meets its escape budget" are different claims, connected only by this procedure.

### 5. Common mistakes & production considerations

1. Evaluating at the demo threshold — reporting metrics at `conf=0.25` and deploying at 0.6 (or vice versa); the deployed operating point is the only one that matters, and it goes in the model card.
2. Un-normalised or class-shifted labels after format conversion — always run the converter's validation pass and visually spot-check 20 frames with boxes rendered.
3. Training at 640 and deploying at 320 to "save latency" without re-measuring — resolution is part of the contract (M1); small defects vanish at 320, and the mAP drop is class-dependent (mould −0.02, insect_damage −0.11 on course data).
4. Random split over conveyor sessions — the M1 leakage rule applies identically to detection; the course manifest's session split carries over.
5. Ignoring background/empty frames — a training set with no defect-free frames teaches the model that *something* must always be found; keep ~10% empty frames.
6. Treating Ultralytics licensing as a non-issue — AGPL-3.0 obligations or a commercial licence are a legal decision; the alternative (training a detector in raw PyTorch/torchvision) costs weeks. Flag it to procurement early, in writing.

Production: log every detection (class, box, confidence, frame id) even below the acting threshold — threshold retuning without re-inference needs the raw scores; NMS behaviour under load is deterministic but *count* metrics drift with camera changes, so per-shift detection-count control charts are the cheapest drift alarm (SDA-AIE-216 formalises); and eject-gate hardware latency means the *end-to-end* budget is camera→decision→actuator, of which model inference is only one term (M7).

## Code Examples

### Dataset conversion with validation

```python
# scripts/manifest_to_yolo.py
"""Convert dates-qc detection manifest (CSV with pixel boxes) to YOLO
format. Validates every line: normalised, in-range, known class."""
from pathlib import Path

import pandas as pd

DEFECTS = ["mould", "skin_split", "insect_damage", "sugaring", "foreign_object"]
IMG_W, IMG_H = 1280, 1024

manifest = pd.read_csv("data/dates-qc/detections_v1.csv")
for split in ["train", "val", "test"]:
    rows = manifest[manifest["split"] == split]
    for file, grp in rows.groupby("file"):
        lines = []
        for _, r in grp.iterrows():
            cls = DEFECTS.index(r["defect"])          # KeyError = unknown class: fail loudly
            cx = (r["x1"] + r["x2"]) / 2 / IMG_W
            cy = (r["y1"] + r["y2"]) / 2 / IMG_H
            w = (r["x2"] - r["x1"]) / IMG_W
            h = (r["y2"] - r["y1"]) / IMG_H
            assert all(0.0 <= v <= 1.0 for v in (cx, cy, w, h)), f"bad box in {file}"
            lines.append(f"{cls} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}")
        out = Path(f"data/dates-det/labels/{split}/{Path(file).stem}.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines))
```

```yaml
# data/dates-det/dates-det.yaml — class order is FROZEN, like GRADES in M1
path: data/dates-det
train: images/train
val: images/val
names:
  0: mould
  1: skin_split
  2: insect_damage
  3: sugaring
  4: foreign_object
```

### Training the defect detector

```python
# scripts/train_detector.py
"""Fine-tune YOLO11s from COCO weights on the dates defect set.
Classroom budget: ~40 epochs ≈ 11 min on an 8 GB GPU."""
from ultralytics import YOLO

model = YOLO("yolo11s.pt")                    # COCO-pre-trained — never from scratch
results = model.train(
    data="data/dates-det/dates-det.yaml",
    epochs=40,
    imgsz=640,                                # the latency/accuracy lever (M7)
    batch=16,
    patience=10,                              # early stop on val mAP@0.5:0.95
    close_mosaic=10,                          # last 10 epochs see real layouts
    copy_paste=0.1,                           # instances are physically pasteable here
    degrees=180, flipud=0.5, fliplr=0.5,      # M1 policy: conveyor has no orientation
    project="runs/detect", name="defect_y11s",
    seed=212, deterministic=True,
)
metrics = model.val(split="test")             # frozen test split, once
print(f"mAP@0.5={metrics.box.map50:.3f}  mAP@0.5:0.95={metrics.box.map:.3f}")
print({n: f"{ap:.3f}" for n, ap in zip(metrics.names.values(), metrics.box.maps)})
```

### Operating-point sweep against line requirements

```python
# scripts/tune_operating_point.py
"""Sweep confidence thresholds; find the band satisfying the line spec:
mould recall >= 0.99 AND false positives per image <= 0.003 * fruit/frame."""
import numpy as np
from ultralytics import YOLO

REQ = {"mould_recall": 0.99, "fp_per_image": 0.05}

model = YOLO("runs/detect/defect_y11s/weights/best.pt")
rows = []
for conf in np.arange(0.10, 0.91, 0.05):
    m = model.val(split="val", conf=float(conf), iou=0.5, verbose=False)
    mould_recall = m.box.r[0]                 # class 0 = mould (frozen order)
    rows.append((conf, mould_recall, m.box.mp, m.box.mr))
    print(f"conf={conf:.2f}  mould_recall={mould_recall:.3f}  "
          f"mean_precision={m.box.mp:.3f}  mean_recall={m.box.mr:.3f}")

feasible = [r for r in rows if r[1] >= REQ["mould_recall"]]
print("feasible band:", [f"{r[0]:.2f}" for r in feasible] or
      "NONE — escalate: per-class thresholds or more mould data (M5)")
```

### Inference wrapper with the contract baked in

```python
# src/tamr_vision/detect/infer.py
"""Detection inference for the line. Thresholds come from CONFIG, never
hard-coded — the operating point is a versioned business decision."""
from dataclasses import dataclass

from ultralytics import YOLO


@dataclass(frozen=True)
class OperatingPoint:
    conf: dict[str, float]          # per-class thresholds, from the sweep
    nms_iou: float = 0.5
    imgsz: int = 640


class DefectDetector:
    def __init__(self, weights: str, op: OperatingPoint):
        self.model, self.op = YOLO(weights), op

    def __call__(self, frame):     # frame: RGB ndarray — M1 boundary rule upheld
        res = self.model.predict(frame, imgsz=self.op.imgsz,
                                 conf=min(self.op.conf.values()),
                                 iou=self.op.nms_iou, verbose=False)[0]
        out = []
        for box in res.boxes:
            name = res.names[int(box.cls)]
            if float(box.conf) >= self.op.conf[name]:   # per-class gate
                out.append({"class": name, "conf": float(box.conf),
                            "xyxy": box.xyxy[0].tolist()})
        return out                  # ALL raw scores also logged upstream
```

## Hands-on Lab 3 — Train the Defect Detector

| | |
|---|---|
| **Objective** | Convert the box manifest to YOLO format, fine-tune YOLO11s to mAP@0.5 ≥ 0.85, and derive a defensible operating point from the line requirements |
| **Duration** | 50 minutes |
| **Setup** | Ultralytics ≥ 8.3 installed; `git checkout lab3-start`; GPU (CPU fallback: `imgsz=320`, 12 epochs, provided `lab3-best.pt` for the tuning tasks) |

**Instructions & tasks**

1. *(8 min)* Run `manifest_to_yolo.py`; it fails on three planted bad rows (one unknown class, two un-normalised boxes). Fix the *data*, not the assertions, and note the failure modes in `BENCHMARKS.md`.
2. *(5 min)* Render 20 random training frames with boxes drawn (`scripts/draw_labels.py`); confirm box/label alignment with your pair before any training.
3. *(15 min)* Launch training per `train_detector.py`. While it runs: inspect the mosaic batches Ultralytics writes to `runs/detect/defect_y11s/train_batch*.jpg` and identify one physically impossible copy-paste composite.
4. *(10 min)* Validate on the frozen test split; record overall and per-class mAP@0.5 in `BENCHMARKS.md`. Which class is weakest, and does its `box_loss`-vs-`cls_loss` history say localisation or recognition?
5. *(10 min)* Run the operating-point sweep against the line spec (mould recall ≥ 0.99, FP/image ≤ 0.05). If no single threshold is feasible, configure per-class thresholds and document the residual gap as a data request.
6. *(2 min)* Commit: `feat(detect): YOLO11s defect detector + operating point v1`.

**Expected output**
```
$ python scripts/train_detector.py
40 epochs completed in 0.19 hours.
mAP@0.5=0.872  mAP@0.5:0.95=0.641
{'mould': '0.921', 'skin_split': '0.884', 'insect_damage': '0.798',
 'sugaring': '0.861', 'foreign_object': '0.897'}
$ python scripts/tune_operating_point.py
conf=0.30  mould_recall=0.993  ...
feasible band: ['0.20', '0.25', '0.30']
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `train: WARNING ... corrupt image/label` | Un-normalised boxes survived conversion | Re-run converter; assert range before write |
| mAP@0.5 stuck ≈ 0.55 | Trained from scratch (`yolo11s.yaml` not `.pt`) | Load COCO weights; restart from `lab3-start` |
| Every fruit detected twice | NMS `iou` too high for touching fruit | Lower to 0.45–0.5; re-sweep counts |
| GPU OOM at batch 16 | 8 GB card + other notebooks open | `batch=8` or `imgsz=512`; close notebooks |
| Val numbers change between runs | Non-deterministic val or wrong split | `seed=212, deterministic=True`; check YAML paths |

**Instructor notes.** The planted conversion failures are the module's first checkpoint — pairs that silence the assertions instead of fixing data must be caught at task 2's rendering step (their boxes will be visibly wrong). Task 5 is where the module's thesis lands: at least one class (insect_damage, by design) cannot meet the spec at any threshold, forcing the per-class-threshold + data-request conversation. Collect each pair's "residual gap" sentence — they become the motivation for M5. Fast finishers: sweep `imgsz` ∈ {320, 512, 640} on the val split and start the latency/accuracy table that M7 completes.

## Mini Exercises

**Quiz (5 questions)**
1. Name the three structural parts of a modern YOLO and one job of each. → backbone (features), neck (multi-scale fusion), head (per-cell class + box, anchor-free).
2. What does NMS do, and what goes wrong on touching fruit if its IoU threshold is too low? → suppresses overlapping same-class boxes; merges two real, adjacent fruit into one detection.
3. Why keep ~10% defect-free frames in the training set? → otherwise the model learns "always find something"; background frames calibrate the confidence.
4. `box_loss` plateaus while `cls_loss` falls. Diagnosis? → localisation bottleneck — usually annotation-quality (sloppy boxes), not recognition.
5. True/False: the confidence threshold used at deployment must equal the one metrics were reported at. → **True** — otherwise the reported numbers describe a different system.

**Debugging exercise.** Branch `sim-class-shift`: the dataset YAML lists classes in alphabetical order while the labels were written in taxonomy order. mAP looks plausible (~0.71) but the per-class table is absurd (`foreign_object` AP 0.91 on a class with 40 instances). Participants must catch it by rendering predictions against ground truth and diffing class distributions.

**Code-review exercise.** Review a PR that (a) hard-codes `conf=0.25` in the inference wrapper, (b) evaluates on the training split "because the val set is small", and (c) reorders YAML class names cosmetically. Three findings with the production consequence of each.

**Discussion questions.**
- The line manager asks for "zero mould escapes". Using the PR curve, explain why "zero" is a request for a different system (100% ejection or human inspection tier) and negotiate a number.
- Ultralytics is AGPL-3.0. The plant's software will not be open-sourced. What are the three options, and who decides? (commercial licence; AGPL compliance; rebuild on permissive stack — legal/procurement decides, engineering costs the options.)

## Case Study — PPE Compliance Detection on a Jubail Construction Megaproject

**Scenario.** A contractor deploys hard-hat, hi-vis, and harness detection across 46 fixed cameras on a petrochemical construction site. The pilot's headline mAP@0.5 of 0.88 impressed management, but in month one the safety office logs 31 missed harness violations at height — and simultaneously complains that gate cameras raise ~400 false hard-hat alarms per day at shift change.

**Business context.** Safety-violation statistics feed the client's incentive scheme; missed harness events at height are contractually reportable. Meanwhile alarm fatigue is real: after two weeks the control room stopped acknowledging hard-hat alerts entirely, making the system's true recall irrelevant.

**Technical challenge.** Diagnose why one deployment produces both misses and floods, and re-engineer the operating points per class and per camera zone.

**Constraints.** Cameras are fixed but heterogeneous (gate close-ups vs tower-crane wide shots — harness instances are 18–30 px there); no new cameras this budget year; retraining is allowed but labelling budget is 6,000 boxes; alerts route to one control room that can act on at most ~50/day.

**Solution approach (facilitate, don't lecture).** Separate the failure modes: harness misses are a *small-object + data-scarcity* problem (wide shots, 210 harness instances in training) — spend most of the 6,000-box budget there, prioritising wide-shot frames via model-uncertainty sampling (M5 preview), and evaluate at the *zone* level, not the fleet level. Hard-hat floods are an *operating-point* problem: shift-change crowds raise per-frame candidate counts, so per-camera thresholds plus a temporal filter (violation must persist ≥ N frames) cut alarms ~8× at negligible recall cost. Redefine acceptance per class: harness recall ≥ 0.95 in crane zones; hard-hat alerts ≤ 50/day fleet-wide. mAP stays on the engineer's dashboard; the contract speaks recall and alarm budgets.

**Discussion questions.**
1. Why did a single fleet-wide mAP number fail to predict either problem? (aggregation across classes, zones, and object sizes — the M6 slicing argument.)
2. Design the labelling-budget split across the three classes with justification.
3. The temporal persistence filter trades latency for precision. Where is it wrong to apply the same trick? (fall detection, intrusion — events that are themselves brief.)
4. The client requests raw footage retention for audit. What does PDPL imply for a site where workers are identifiable? (retention limits, access control, purpose limitation, worker notification.)

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| mAP@0.5 (test split) | Model quality | ≥ 0.85 | `model.val(split="test")` |
| mAP@0.5:0.95 (test split) | Model quality | ≥ 0.60 | same |
| Mould recall at deployed operating point | Model quality | ≥ 0.99 | operating-point sweep |
| Training wall-clock (40 epochs, GPU) | Performance | ≤ 15 min | run logs |
| Label-format validation | Reliability | 0 corrupt labels reported by trainer | Ultralytics scan output |
| Operating point documented | Code quality | per-class `conf` + `iou` + rationale in model card | review |

**Example benchmark table (filled during lab):**

| Class | Instances (train) | AP@0.5 | Recall @ deployed conf | Notes |
|---|---|---|---|---|
| mould | 1,860 | 0.921 | 0.993 @ 0.30 | meets line spec |
| skin_split | 1,410 | 0.884 | 0.958 @ 0.35 | — |
| insect_damage | 640 | 0.798 | 0.902 @ 0.20 | data request filed (M5) |
| sugaring | 980 | 0.861 | 0.941 @ 0.35 | — |
| foreign_object | 310 | 0.897 | 0.971 @ 0.25 | high-severity class |

## Required Visuals and Training Assets

### Diagrams
1. **Detector anatomy** — *Purpose:* the module's anchor image. *Elements:* backbone → three-scale feature maps → FPN/PAN neck arrows (top-down + bottom-up) → decoupled head emitting (class, box, conf) per cell; strides 8/16/32 annotated with "small/medium/large objects". *Style:* horizontal architecture strip, course palette, English labels with Arabic subtitles.
2. **Raw candidates → NMS → decisions** — *Elements:* one conveyor frame shown three times: ~8,400 raw candidates (heat haze), post-confidence-threshold (~40 boxes), post-NMS (7 boxes); threshold dials drawn under each transition. *Style:* three-panel filmstrip. *Designer note:* the middle panel must visibly contain duplicate boxes on the same defect.
3. **Operating-point map** — *Elements:* per-class recall and FP/image curves vs confidence on one chart; the line-requirement band shaded; the feasible region (or its absence for insect_damage) highlighted. *Style:* annotated chart, doubles as the Lab 3 debrief slide.
4. **One-stage vs two-stage trade-off** — *Elements:* YOLO vs Faster R-CNN pipelines side by side with latency/small-object/complexity scorecard. *Style:* comparison panel, printable A4.

### Images (screenshots)
1. **`train_batch0.jpg` mosaic sheet** — *why:* participants must recognise mosaic/copy-paste composites; *content:* Ultralytics training-batch render with one physically impossible paste circled.
2. **Rendered ground truth vs predictions** — *why:* the visual-audit habit for detection; *content:* 8 frames, GT in green, predictions in red, one class-shift error visible.
3. **Training console output** — *why:* expected-state reference; *content:* per-epoch box/cls/dfl losses + val mAP table at epoch 40.
4. **Operating-point sweep terminal output** — *why:* Lab 3 task 5 reference; *content:* the conf ladder with the feasible band.

### Simulations
1. **Class-order shift** — *Setup:* branch `sim-class-shift` (YAML alphabetised after labelling). *Expected behaviour:* plausible aggregate mAP, absurd per-class table, wrong names on rendered predictions. *Learning objective:* class order is part of the contract; renders beat metrics for catching it.
2. **Threshold mismatch** — *Setup:* branch `sim-conf-mismatch`: metrics reported at conf=0.25, the provided "line simulator" runs the wrapper at 0.6. *Expected behaviour:* line-simulator escape rate ~5× the reported one. *Learning objective:* deployed operating point = reported operating point, always.

### Interactive Activities
- **Threshold negotiation role-play (15 min):** one pair plays plant management ("zero escapes!"), one plays engineering with the real PR curve; they must sign a one-line operating agreement with numbers. Debrief on which side moved and why.
- **NMS by hand (10 min):** pairs get 12 printed candidate boxes with confidences on one frame and execute NMS with IoU 0.5 using a transparent overlay grid; then compare against the code's output.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `dates-det` v1 | Course team: box annotations over dates-qc frames | YOLO txt + YAML | 4,200 annotated frames, 5 defect classes, 5,200 boxes | Detector training |
| `detections_v1.csv` | Course team | CSV (pixel boxes) | 5,203 rows (3 planted bad) | Conversion exercise |
| Line-requirement spec sheet | Course handout | MD | 1 page | Operating-point tuning |
| `lab3-best.pt` | Course team | .pt | 19 MB | CPU-fallback checkpoint |

### Demo Requirements
- **Instructor demo:** live training launch with the mosaic batch renders projected; then the operating-point sweep run live, ending on the insight that insect_damage has no feasible threshold.
- **Student demo:** one pair presents their operating agreement from the role-play; one pair shows the class-shift render catch.
- **Expected outputs:** every pair enters Day 2 Hour 4 with a trained detector ≥ 0.85 mAP@0.5 and a documented operating point in `BENCHMARKS.md`.

---

# Module 4 — Semantic and Instance Segmentation

## Module Overview

**Purpose.** Boxes answer "where"; masks answer "exactly which pixels". This module adds pixel-level prediction to the toolkit: the three segmentation task types and how to choose between them, the architecture patterns behind encoder-decoder and mask-head models, training an instance segmenter with the Ultralytics workflow already mastered in M3, and — the applied payoff — turning masks into calibrated business measurements. For Tamr Vision that measurement is *defect-area percentage per fruit*, the number the grading standard actually references.

**Business relevance.** A surprising amount of vision value in the Kingdom is measurement, not recognition: what fraction of this date's surface is sugared (grading standards specify area thresholds), how many square metres of road surface are cracked (maintenance budgets are priced per m²), how much of a palm canopy shows pest stress (treatment dosage), what area of a solar panel is soiled (cleaning-schedule optimisation at scale). Boxes cannot produce these numbers; masks can — *if* the pixel-to-real-world calibration is engineered, which is where most segmentation pilots quietly fail. Segmentation also costs 5–10× more per annotation than boxes, so the decision to use it must be earned by the business question.

**Industry use cases.**
- Tamr Vision's surface-defect segmenter: YOLO11s-seg masks sugaring and mould regions so the grader can apply the standard's "reject if defect area > 8% of visible surface" rule — a rule the M3 detector's boxes systematically overstate (a box around a crescent-shaped defect includes mostly healthy skin).
- A Riyadh municipality quantifying road-crack area from vehicle-mounted cameras, where the repair contractor is paid per verified m² — masks are the invoice evidence.
- A solar operator near Sakaka estimating per-panel soiling fraction from drone sweeps to trigger cleaning only where economically justified.

**Expected competencies.** After this module a participant can choose between semantic, instance, and panoptic formulations from the business question; explain encoder-decoder (U-Net/DeepLab) and mask-head (Mask R-CNN, YOLO-seg) designs and their trade-offs; train and evaluate an instance segmentation model on a custom dataset; compute mIoU and mask mAP and know what each hides; and convert masks into calibrated area measurements with documented pixel-to-mm assumptions.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Select semantic vs instance vs panoptic segmentation from the business question and annotation budget | LO2, LO3 |
| 4.2 | Explain encoder-decoder and mask-head architectures and their speed/quality trade-offs | LO2 |
| 4.3 | Train an instance segmentation model (YOLO11s-seg) on custom polygon annotations | LO2, LO4 |
| 4.4 | Evaluate masks with mIoU and mask mAP; diagnose boundary vs region errors | LO5 |
| 4.5 | Convert masks into calibrated real-world measurements with documented assumptions | LO2, LO6 |

## Technical Content

### 1. Three tasks, one word

"Segmentation" covers three distinct formulations; choosing wrongly wastes annotation money:

- **Semantic segmentation:** every pixel gets a class label; instances are not separated. Two overlapping mould patches are one "mould" region. Right when the question is *total area per class* (road-crack m², soiling fraction) and instance identity is irrelevant.
- **Instance segmentation:** each *object* gets its own mask + class + confidence — detection with pixel-accurate extents. Right when per-object measurements matter: Tamr Vision needs defect area *per fruit*, so defects must be attributed to instances.
- **Panoptic segmentation:** the union — every pixel labelled, countable things also instanced. Rich, expensive, and rarely the applied answer; taught as vocabulary.

The cost gradient is real: a box takes an annotator ~7 seconds, a decent polygon 35–90 seconds. The course rule from M3 extends: *choose the cheapest formulation that produces the required number* — and note that model-assisted polygon tools (M5, SAM-based) have cut the gap substantially.

### 2. Architecture patterns

**Encoder-decoder (semantic).** The encoder is a familiar backbone downsampling to rich, low-resolution features; the decoder upsamples back to full resolution. The defining trick is **skip connections** (U-Net, 2015): shallow, high-resolution encoder features are concatenated into the decoder so boundaries stay sharp — without them, masks look like melted wax. DeepLab's contribution is **atrous (dilated) convolution**: enlarged receptive fields without losing resolution, plus multi-scale pooling (ASPP). U-Net variants still dominate medical and industrial semantic tasks because they train well on small datasets.

**Mask heads on detectors (instance).** Mask R-CNN (2017) extends the two-stage detector: for each detected region, a small FCN predicts a per-instance binary mask; **RoIAlign** (bilinear sampling instead of quantised pooling) is the detail that made pixel-accurate masks possible and is a favourite interview question. Single-stage equivalents — YOLO-seg — predict a set of **prototype masks** for the whole image plus per-instance coefficients that linearly combine them (the YOLACT idea): near-detector speed, slightly softer boundaries. Course positioning: YOLO11s-seg for the golden thread (speed, one workflow), Mask R-CNN as the two-stage reference participants must be able to discuss.

**Transformers in segmentation** get one honest paragraph: Mask2Former-style universal architectures win benchmarks and SAM (Segment Anything) changed *annotation* economics forever — but as deployed line models they are heavier than the task usually needs. SAM's real course role is in M5 as an annotation assistant.

### 3. Training mechanics and losses

- **Label format:** Ultralytics segmentation labels are polygons — `class x1 y1 x2 y2 ...` normalised, one instance per line. Conversion pitfalls mirror M3's, plus two new ones: self-intersecting polygons and holes (a ring-shaped defect needs either multi-polygon support or an annotation-spec decision — the course spec says "annotate outer boundary; holes ignored", an explicit, documented simplification).
- **Losses:** per-pixel binary cross-entropy on masks, plus everything from M3 for the detection part. For semantic models, **Dice loss** matters: with a defect occupying 2% of pixels, plain BCE reaches 98% pixel accuracy by predicting "no defect" everywhere; Dice optimises overlap directly and is the standard imbalance defence (usually summed with BCE).
- **Resolution discipline:** masks are resolution-hungry — a 3-pixel-wide skin split at 1280² becomes sub-pixel noise at 320². The course trains at 640 and documents the minimum defect width that survives (≈ 6 px at capture resolution), a number that goes in the model card and constrains M7's optimisation choices.
- **Augmentation:** geometric transforms must warp masks with pixels — Ultralytics handles it; the M1 warning about hand-rolled augmentation goes double for polygons. Copy-paste is *stronger* for segmentation (masked instances composite cleanly) and is on by default.

### 4. Evaluating masks

- **Mask IoU** replaces box IoU as the matching primitive: intersection and union are computed over pixels. Mask mAP then works exactly as in M3 — participants reuse the mental machinery.
- **mIoU** (semantic): per-class IoU averaged over classes — the standard semantic headline. What it hides: boundary quality (a mask 3 px too fat everywhere scores well but breaks area measurement by 15% on small defects) and per-image variance (great average, terrible worst case).
- **Boundary-aware checks:** the course harness (M6) adds a boundary-F1 spot metric and, more importantly, the *measurement-level* test: does predicted defect-area % match ground-truth area % within tolerance? That is the metric the business actually consumes — models with identical mask mAP can differ 2× in area error on thin defects.
- **Confidence semantics differ:** an instance's confidence describes the *detection*, not mask quality; low-quality masks on confident detections are a distinct, auditable failure mode.

### 5. From masks to measurements

The applied payoff, and where pilots fail:

1. **Attribution:** intersect defect masks with fruit instance masks — every defect pixel is assigned to exactly one fruit (largest-overlap rule; ties logged).
2. **Area ratio:** defect-area % = defect pixels ∩ fruit ÷ fruit pixels. This ratio is *scale-free* — no calibration needed — which is exactly why Tamr Vision's grading rule was negotiated as a percentage.
3. **Absolute measurements** (the road-crack m² case) need calibration: pixels→mm via known geometry (fixed camera height + lens model) or a reference object in frame; document the assumption, its error bound, and the revalidation trigger (any camera move).
4. **The visible-surface caveat:** a camera sees one hemisphere of the fruit; the standard's "8% of surface" is operationalised as "8% of *visible* surface, single view" — an explicitly documented approximation the plant signed off. Teaching point: every vision measurement embeds such an approximation; write them down or they become disputes.

### 6. Common mistakes & production considerations

1. Reporting pixel accuracy on imbalanced masks — the 98%-by-predicting-nothing trap; mIoU or Dice, always.
2. Using boxes' area as a proxy for defect area — overestimates crescent/elongated defects by 2–4×; this is the money argument for the module's existence.
3. Downsampling until thin structures vanish, then blaming the model — check minimum-feature-width survival at the training resolution first.
4. Annotation specs without boundary rules — "where does the sugaring end?" answered differently by each annotator yields boundary noise no model can learn through (M5 measures this with inter-annotator IoU).
5. Ignoring mask holes and multi-part instances in the spec — decide, document, and enforce in the converter.
6. Measurement without calibration governance — a camera bumped 5 cm changes every m² invoice; calibration checks belong in the deployment runbook (M7).

Production: masks are heavy — store run-length encodings, not PNGs, in logs; area measurements should be logged with the *mask*, not just the number, so disputes are auditable; and per-class area-error control charts complement M3's count charts in monitoring (SDA-AIE-216).

## Code Examples

### Training the surface-defect segmenter

```python
# scripts/train_segmenter.py
"""Fine-tune YOLO11s-seg on polygon-annotated defects. Same workflow as
M3 — segmentation adds masks to the head, not complexity to your day."""
from ultralytics import YOLO

model = YOLO("yolo11s-seg.pt")                 # COCO-seg pre-trained
model.train(
    data="data/dates-seg/dates-seg.yaml",      # classes: fruit + 5 defects
    epochs=40, imgsz=640, batch=12,            # masks cost VRAM: 12, not 16
    patience=10, close_mosaic=10, copy_paste=0.3,
    degrees=180, flipud=0.5, fliplr=0.5,
    project="runs/seg", name="defect_y11s_seg",
    seed=212, deterministic=True,
)
m = model.val(split="test")
print(f"box mAP@0.5={m.box.map50:.3f}   MASK mAP@0.5={m.seg.map50:.3f}")
```

### Defect-area percentage per fruit (the business number)

```python
# src/tamr_vision/seg/measure.py
"""Turn instance masks into the grading standard's number:
defect-area %% of visible fruit surface, attributed per fruit."""
import numpy as np

DEFECT_CLASSES = {"mould", "skin_split", "insect_damage", "sugaring"}


def defect_area_report(result) -> list[dict]:
    """result: one Ultralytics predict() result with masks.
    Returns one dict per fruit instance with per-class area ratios."""
    names = result.names
    masks = result.masks.data.cpu().numpy().astype(bool)     # (n, H, W)
    classes = [names[int(c)] for c in result.boxes.cls]
    fruit_idx = [i for i, c in enumerate(classes) if c == "fruit"]
    defect_idx = [i for i, c in enumerate(classes) if c in DEFECT_CLASSES]

    report = []
    for fi in fruit_idx:
        fruit_px = masks[fi].sum()
        if fruit_px == 0:
            continue                                  # degenerate mask: log upstream
        areas = {c: 0.0 for c in DEFECT_CLASSES}
        for di in defect_idx:
            overlap = (masks[di] & masks[fi]).sum()
            if overlap / max(masks[di].sum(), 1) >= 0.5:      # attribution rule:
                areas[classes[di]] += overlap / fruit_px       # majority-overlap fruit
        report.append({
            "fruit_id": fi,
            "visible_area_px": int(fruit_px),
            "defect_pct": {c: round(100 * v, 2) for c, v in areas.items()},
            "total_defect_pct": round(100 * sum(areas.values()), 2),
        })
    return report      # grading rule applied downstream: reject if total > 8.0
```

### Measurement-level evaluation (what mask mAP hides)

```python
# scripts/eval_area_error.py
"""Compare predicted vs ground-truth defect-area %% per fruit on the val
split. THIS is the metric the plant consumes — report it alongside mAP."""
import numpy as np
from ultralytics import YOLO

from tamr_vision.seg.measure import defect_area_report
from tamr_vision.seg.gt import gt_area_report          # same logic on GT polygons

model = YOLO("runs/seg/defect_y11s_seg/weights/best.pt")
errors = []
for frame, gt in val_frames_with_gt():                  # provided iterator
    pred = defect_area_report(model.predict(frame, imgsz=640, verbose=False)[0])
    for p, g in match_fruit(pred, gt_area_report(gt)):  # match by mask overlap
        errors.append(p["total_defect_pct"] - g["total_defect_pct"])

errors = np.array(errors)
print(f"area error: mean={errors.mean():+.2f} pp  "
      f"MAE={np.abs(errors).mean():.2f} pp  p95={np.percentile(np.abs(errors), 95):.2f} pp")
print(f"grading disagreement rate (8% rule): "
      f"{(np.sign(errors_flip_decision(errors))).mean():.3%}")   # provided helper
```

### Mask overlay for the visual audit

```python
# scripts/draw_masks.py
"""Render predictions vs ground truth: GT contours green, predicted masks
filled at 40% alpha, per-fruit defect %% printed. The M1 habit, masked."""
import cv2

def overlay(frame_bgr, result, report):
    canvas = frame_bgr.copy()
    for mask, cls in iter_masks(result):                    # provided helper
        color = CLASS_COLORS[cls]
        canvas[mask] = (0.6 * canvas[mask] + 0.4 * np.array(color)).astype("uint8")
        cnts, _ = cv2.findContours(mask.astype("uint8"),
                                   cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(canvas, cnts, -1, color, 1)
    for fruit in report:
        x, y = fruit_centroid(result, fruit["fruit_id"])
        cv2.putText(canvas, f'{fruit["total_defect_pct"]:.1f}%', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    return canvas
```

## Hands-on Lab 4 — Segment Surface Defects

| | |
|---|---|
| **Objective** | Train YOLO11s-seg on the polygon set, reach mask mAP@0.5 ≥ 0.80, and produce a per-fruit defect-area report whose measurement error is quantified |
| **Duration** | 50 minutes |
| **Setup** | `git checkout lab4-start`; `dates-seg` polygon bundle extracted; GPU (CPU fallback: `imgsz=320`, provided `lab4-best.pt`) |

**Instructions & tasks**

1. *(5 min)* Inspect three annotated frames in the polygon viewer; find the annotation-spec decision about mask holes written in `ANNOTATION_SPEC.md` §4 and state what the converter therefore does with ring-shaped sugaring.
2. *(15 min)* Launch training per `train_segmenter.py`. While it runs, hand-compute mask IoU for two provided 8×8 toy masks and check against `torchmetrics` — the M6 primitive, internalised early.
3. *(8 min)* Validate on the frozen test split; record box mAP@0.5 *and* mask mAP@0.5 per class in `BENCHMARKS.md`. Which class has the biggest box-vs-mask gap, and why? (Expected: skin_split — thin structure, boundary-dominated.)
4. *(12 min)* Implement the attribution rule in `measure.py` (majority-overlap); run `eval_area_error.py` and record MAE and the grading-disagreement rate against the 8% rule.
5. *(8 min)* Render 12 overlay frames with `draw_masks.py`; find one fruit where the *box* would have flipped the grading decision but the mask does not; save it for the debrief.
6. *(2 min)* Commit: `feat(seg): surface-defect segmenter + area measurement v1`.

**Expected output**
```
$ python scripts/train_segmenter.py
box mAP@0.5=0.858   MASK mAP@0.5=0.823
$ python scripts/eval_area_error.py
area error: mean=+0.31 pp  MAE=1.12 pp  p95=3.40 pp
grading disagreement rate (8% rule): 2.1%
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `WARNING ... segment ... < 3 points` | Degenerate polygons from conversion | Filter polygons with < 3 vertices; re-run converter |
| Mask mAP ≈ box mAP exactly | Evaluating boxes twice (wrong metric object) | Read `m.seg.*`, not `m.box.*` |
| CUDA OOM at batch 12 | Prototype masks + 8 GB card | `batch=8`; keep `imgsz=640` before sacrificing resolution |
| Area MAE huge (> 10 pp) | Attribution rule assigns defects to wrong fruit | Check majority-overlap logic; render the failing frames |
| Masks look blocky/staircased | Rendering at low res then upsampling | Overlay at native resolution; masks scale with `retina_masks=True` |

**Instructor notes.** Task 5 is the module's money moment — the frame where box-area would reject a fruit that mask-area passes (or vice versa) is the whole business case for segmentation, found by each pair in their own output. Collect two or three of these frames for the class debrief and ask: "what does this disagreement cost per day at 40,000 fruit?" Task 2's hand-computed IoU is deliberately placed here so M6's matching lecture lands on prepared ground. Fast finishers: set `retina_masks=True`, re-run the area evaluation, and quantify the boundary-quality dividend.

## Mini Exercises

**Quiz (5 questions)**
1. Semantic vs instance segmentation — which one can produce "defect area per fruit" and why? → instance: attribution needs object identity, semantic masks merge instances.
2. What do U-Net skip connections preserve that a plain encoder-decoder loses? → high-resolution spatial detail; sharp boundaries.
3. Why does Dice loss beat plain BCE on a 2%-of-pixels defect class? → BCE is dominated by the easy negative pixels; Dice optimises overlap directly.
4. A detection's confidence is high; can the mask still be poor? → yes — confidence scores the detection; mask quality is a separate, auditable axis.
5. True/False: converting defect masks to a percentage of fruit area requires pixel-to-mm calibration. → **False** — ratios are scale-free; absolute areas (m²) need calibration.

**Debugging exercise.** Branch `sim-fat-mask`: a preprocessing "fix" applied morphological dilation to all training masks (an annotator's script leaked into the pipeline). Mask mAP@0.5 barely moves (−0.015) but area MAE triples and the grading-disagreement rate hits 9%. Participants must find why the headline metric was insensitive and which metric caught it — the module's evaluation lesson, made concrete.

**Code-review exercise.** Review a PR that (a) computes defect ratio against the *frame* area instead of the fruit area, (b) reports pixel accuracy as the headline, and (c) hard-codes the 8% grading threshold inside `measure.py`. Three findings with consequences.

**Discussion questions.**
- The plant asks to also grade the *hidden* hemisphere. Options? (second camera + mirror rig, rollers between two stations, accept single-view approximation with a documented bias factor — engineering economics discussion.)
- Annotating polygons costs 6× boxes. For which of the five defect classes would you *keep* box-only annotation, and what does that imply for the product? (classes never used in area rules — pure presence/absence classes.)

## Case Study — Road-Crack Quantification for a Riyadh Municipality

**Scenario.** A municipality contracts vehicle-mounted camera surveys of 4,100 km of roads. The maintenance contractor is paid per m² of verified crack repair, and the previous manual survey process was both slow and disputed — the contractor and the municipality's inspectors disagreed on measured areas by up to 40%. A semantic segmentation model (crack / patch / joint / background) is proposed as the neutral measurement instrument.

**Business context.** Annual road-maintenance budgets here run to hundreds of millions of riyals; a 10% systematic measurement bias is real money in one direction or the other. Both parties must trust the number, so the *measurement pipeline* — not just the model — will be audited.

**Technical challenge.** Design the segmentation and calibration pipeline so that reported m² carries a defensible error bound, and decide what happens when model confidence is low.

**Constraints.** Camera height varies with vehicle load (±4 cm) and lens distortion is non-trivial at frame edges; surveys run at 50 km/h (motion blur); thin cracks (< 3 mm) sit at the sensor's resolution limit; disputes must be resolvable from stored evidence; summer asphalt glare and shadow edges are known false-positive sources.

**Solution approach (facilitate, don't lecture).** Semantic (not instance) formulation — total area per class is the deliverable. Calibration: per-frame ground sampling distance from camera geometry + IMU-corrected height, validated weekly against painted reference plates; error budget propagated to the m² figure (±6% documented). Thin-crack limit made explicit: cracks under 3 mm are contractually "detected but not billable" — an honest capability statement instead of a silent failure. Shadow/glare false positives attacked with targeted augmentation and a hard-negative mining round (M5). Every billed segment stores frame + mask + calibration record — the dispute-resolution evidence pack. Low-confidence regions route to human review, budgeted at 4% of frames.

**Discussion questions.**
1. Why semantic rather than instance segmentation here, and what would change if the contract paid per *crack* rather than per m²?
2. Construct the error budget: which term dominates — mask boundary error, calibration error, or sampling (frame overlap) error?
3. Both parties want to audit the model. What artefacts constitute the audit pack? (frozen eval set + harness, calibration logs, versioned model + spec — M5/M6 vocabulary.)
4. The contractor proposes fine-tuning the model on their own annotations. Governance response? (measurement instruments need neutral custody; joint annotation spec, third-party eval split.)

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Mask mAP@0.5 (test split) | Model quality | ≥ 0.80 | `model.val()` seg metrics |
| Defect-area MAE per fruit | Measurement quality | ≤ 1.5 pp | `eval_area_error.py` |
| Grading-disagreement rate (8% rule) | Business quality | ≤ 3% | same |
| Training wall-clock | Performance | ≤ 15 min classroom GPU | run logs |
| Degenerate polygons after conversion | Reliability | 0 | converter validation pass |
| Attribution rule documented + tested | Code quality | majority-overlap rule with unit test | review |

**Example benchmark table (filled during lab):**

| Class | Box AP@0.5 | Mask AP@0.5 | Box−Mask gap | Area MAE (pp) |
|---|---|---|---|---|
| fruit | 0.941 | 0.928 | 0.013 | — |
| mould | 0.903 | 0.871 | 0.032 | 0.8 |
| skin_split | 0.862 | 0.744 | 0.118 | 2.1 |
| insect_damage | 0.781 | 0.752 | 0.029 | 1.0 |
| sugaring | 0.855 | 0.819 | 0.036 | 1.3 |

## Required Visuals and Training Assets

### Diagrams
1. **The segmentation task family** — *Purpose:* anchor image. *Elements:* one conveyor frame rendered four ways — classification label, boxes, semantic masks (instances merged), instance masks (per-fruit colours) — with the business question each can answer underneath. *Style:* four-panel strip, course palette, English labels with Arabic subtitles.
2. **Encoder-decoder with skip connections** — *Elements:* U-shape with resolution annotated per level, skip arrows crossing the U, and a "no-skip" ghost output (blurred boundary) vs real output. *Style:* classic U-Net diagram, decluttered, printable A4.
3. **Prototype-mask assembly (YOLO-seg)** — *Elements:* 4 prototype masks × per-instance coefficients → assembled instance mask; caption "detection speed, pixel output". *Style:* small-multiples row with a weighted-sum symbol.
4. **Box-area vs mask-area** — *Elements:* crescent-shaped sugaring defect with its bounding box; shaded areas compared numerically (box 11.2% vs mask 4.6% of fruit); grading threshold line at 8%. *Style:* single annotated illustration — the module's business case in one image.

### Images (screenshots)
1. **Overlay reference frame** — *why:* expected output for `draw_masks.py`; *content:* GT contours green, predicted masks filled, per-fruit percentages printed.
2. **Training console with seg metrics** — *why:* participants must read `seg.map50` vs `box.map50`; *content:* epoch table + final per-class val output.
3. **`sim-fat-mask` evidence pair** — *why:* headline-metric insensitivity made visible; *content:* near-identical mAP lines vs tripled area-MAE line, side by side.
4. **Polygon annotation tool screenshot** — *why:* M5 preview; *content:* CVAT/Label Studio polygon session on a dates frame with the spec's boundary rule visible in the guidelines panel.

### Simulations
1. **Fat masks** — *Setup:* branch `sim-fat-mask` (dilated training masks). *Expected behaviour:* mask mAP ~stable, area MAE 3×, disagreement rate 9%. *Learning objective:* choose metrics at the measurement level, not just the benchmark level.
2. **Resolution collapse** — *Setup:* branch `sim-res-320`: identical training at `imgsz=320`. *Expected behaviour:* skin_split mask AP drops ~0.19 while mould barely moves; minimum-feature-width table explains it. *Learning objective:* resolution is a per-class decision with a documented survival threshold.

### Interactive Activities
- **Task-formulation triage (15 min):** eight one-line business questions on cards (per-fruit area, total m², count of cracks, "is the panel dirty?", ...); pairs assign classification/detection/semantic/instance + annotation-cost estimate; class reconciles against the cost gradient.
- **Boundary court (10 min):** three annotators' polygons for the same sugaring patch projected; pairs must write a one-sentence boundary rule for the spec that would have made them agree — feeds directly into M5.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `dates-seg` v1 | Course team: polygon annotations (fruit + 5 defect classes) over dates-qc frames | YOLO-seg txt + YAML | 2,600 annotated frames, 9,800 polygons | Segmenter training |
| Toy IoU mask pair | Course handout | npy | 2 × 8×8 | Hand-computed IoU exercise |
| GT area reports | Generated from GT polygons | parquet | 2,600 rows | Measurement-level evaluation |
| `lab4-best.pt` | Course team | .pt | 21 MB | CPU-fallback checkpoint |

### Demo Requirements
- **Instructor demo:** live prediction + overlay on five frames, then the box-vs-mask area comparison on the crescent-defect frame; end with the `sim-fat-mask` reveal.
- **Student demo:** two pairs present their grading-flip frame from task 5 with the per-day cost estimate.
- **Expected outputs:** every pair ends Day 2 with a segmenter ≥ 0.80 mask mAP, an area-error figure in `BENCHMARKS.md`, and both models (M3 + M4) checkpointed for the capstone.

---

# Module 5 — Dataset Curation and Annotation Workflows

## Module Overview

**Purpose.** By Day 3 participants have trained three models on data they were handed; this module hands them the data problem itself. In production vision, the dataset is not an input — it is *the* system component with the highest leverage and the least engineering discipline applied to it. Participants learn to write annotation specifications that survive contact with real annotators, measure label quality with inter-annotator agreement, hunt label errors with the models they have already trained, decide what to label next with active-learning economics, and version datasets with the same rigour SDA-AIE-113 taught them to version code.

**Business relevance.** Label budgets are the dominant cost line in most vision projects — typically 40–70% of total build cost — and they are routinely wasted: ambiguous specs produce noisy labels that cap model quality no architecture can rescue; random sampling labels thousands of easy frames while the hard 2% stays unlabelled; and unversioned datasets make every metric claim unreproducible. Saudi organisations increasingly outsource annotation to vendors, which converts the spec from an internal document into a *contract* — and PDPL turns annotation access into a data-protection question whenever people appear in frame. The engineers who control these levers ship better models for less money; the M3 "insect_damage cannot meet spec" gap gets closed in this module, with data, not architecture.

**Industry use cases.**
- Tamr Vision's v2 dataset: model-assisted auditing finds ~4% label errors in v1 (concentrated in the sugaring/skin_split boundary), the spec gains three boundary rules, and 800 actively-selected new frames lift insect_damage AP by 0.09 — more than any architecture change tried in M2–M4.
- A palm-plantation health survey in Al-Ahsa where drone imagery is annotated by an offshore vendor: the first batch came back with "pest stress" and "drought stress" systematically swapped because the spec had no reference images — a 60,000-riyal relabelling lesson.
- A retail-shelf monitoring product whose weekly active-learning loop labels only the 300 most-informative frames from 2M captured, keeping annotation spend flat while the SKU catalogue grows.

**Expected competencies.** After this module a participant can write an annotation spec with class definitions, boundary rules, and worked edge cases; set up and run an annotation round in CVAT or Label Studio with model pre-labelling; compute and interpret inter-annotator agreement for boxes and classes; rank a dataset for likely label errors using model disagreement; design an uncertainty-based active-learning round with a measurable acceptance target; and publish a versioned dataset release with manifest, hash, and changelog.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Write an annotation specification: taxonomy, boundary rules, edge-case gallery, QA procedure | LO3 |
| 5.2 | Measure label quality with inter-annotator agreement (class kappa, box/mask IoU agreement) | LO3, LO5 |
| 5.3 | Detect label errors at scale with model-assisted auditing | LO3, LO5 |
| 5.4 | Design active-learning rounds: uncertainty + diversity sampling against a labelling budget | LO3 |
| 5.5 | Version datasets: immutable releases, manifests, hashes, changelogs, and split freezes | LO3 |

## Technical Content

### 1. The annotation spec is the real model architecture

A vision model can never be more consistent than the labels it learns from; the spec is where consistency is manufactured. A production-grade spec contains:

- **Taxonomy with decision rules, not just names:** "sugaring: crystalline white/amber surface deposit; if deposit coexists with dark discolouration, label *both* sugaring and mould as separate instances" — the sugaring/mould co-occurrence rule that v1 lacked, and the source of a third of its label errors.
- **Boundary rules:** where does the defect end? (v2 rule: "boundary at the last pixel of clearly abnormal colouration; do not include the halo".) M4's boundary court showed why: three honest annotators, three boundaries, one rule fixes it.
- **Edge-case gallery:** 20–40 worked examples *with the correct label and one sentence of reasoning*, including deliberate near-misses. Annotators learn from examples, not prose; the gallery is the highest-ROI page in the document.
- **Negative definitions:** what is *not* a defect (natural wrinkling, harmless bloom) — absence of negative rules produces over-labelling drift.
- **QA procedure:** sampling rate for review (course default: 10% double-annotated), the agreement threshold that triggers retraining of *annotators* (kappa < 0.75), and the escalation path for genuinely ambiguous items (a queue the domain expert clears weekly — those items become spec updates).

Spec versioning matters exactly like code: v2 labels made under v2 rules must not be mixed silently with v1 labels — the manifest carries `spec_version` per annotation.

### 2. Annotation tooling and the pre-labelling loop

CVAT and Label Studio dominate the open-source tier; both support boxes, polygons, video interpolation, multi-annotator workflows, and — critically — **model pre-labelling**: the current model's predictions are loaded as draft annotations that humans correct rather than create.

- **Economics:** correcting a decent draft box takes ~2 s vs ~7 s drawing; polygon correction with SAM-assisted tools (click the object, get a mask, adjust vertices) cuts polygon cost 3–5×. Pre-labelling turns every model version into an annotation-productivity upgrade — the flywheel that makes the golden thread literal.
- **The bias trap:** annotators anchor on drafts and under-correct — systematic model errors get *confirmed* into the dataset, and the next model learns its own mistakes harder. Defences: pre-label with confidence floors (only show drafts the model is sure of), rotate a fraction of frames as from-scratch annotation (course default 15%), and monitor correction rates per annotator (a 0% correction rate is a red flag, not a compliment).
- **Task design:** small batches (200–400 frames) with per-batch QA beats one giant task; annotator-specific queues enable per-person agreement tracking without public shaming — the metric goes to the QA lead, feedback goes privately.

### 3. Measuring label quality

"Are the labels good?" is answerable with numbers:

- **Class agreement — Cohen's kappa** on double-annotated items: agreement corrected for chance. Course thresholds: κ ≥ 0.85 healthy; 0.75–0.85 spec-clarification territory; < 0.75 stop labelling, fix the spec. Per-class-pair confusion between annotators localises *which* rule is ambiguous (v1's sugaring↔skin_split cell was the tell).
- **Localisation agreement — IoU between annotators' boxes/masks** on matched instances: median IoU ≥ 0.85 for boxes, ≥ 0.75 for polygons is the course bar. Low localisation agreement with high class agreement means boundary rules, not taxonomy, need work.
- **Gold tasks:** expert-labelled items seeded invisibly into the queue measure each annotator against ground truth (not just against each other — two annotators sharing the same misunderstanding agree perfectly and are both wrong).
- **The honest baseline:** measure agreement *before* training anything ambitious; a model asked to beat κ=0.7 labels is being asked to out-agree its own teachers. Label noise sets the ceiling on every metric in M6 — this number belongs in the model card next to mAP.

### 4. Model-assisted error hunting and active learning

The trained models from M2–M4 are the best label auditors available:

- **Disagreement ranking:** run the model on its own training set; rank items by *loss* (or by confident-prediction-vs-label mismatch). Label errors concentrate violently at the top of this ranking — in the course dataset, the top 300 loss-ranked items contain ~70% of all planted-and-real label errors. This is the cleanlab idea taught mechanically: cross-validated predictions beat in-sample where feasible, but even in-sample ranking finds the concentrated mass.
- **Triage discipline:** each flagged item is *label error / model error / genuinely ambiguous* — the third category feeds the spec's edge-case gallery. Never let the auditing engineer silently "fix" labels; changes go through the same QA as new annotation (auditor bias is real).
- **Active learning — what to label next:** with a budget of B new labels, random sampling wastes most of B on frames the model already handles. Uncertainty sampling (lowest max-confidence, or detection-entropy for detectors) targets the decision boundary; diversity constraints (cluster embeddings, cap per-cluster picks) stop the batch collapsing onto one failure mode; and *targeted* acquisition (M3's "400 more hard mould examples") is active learning driven by slice-level evaluation instead of raw uncertainty. Course evidence: 800 actively-selected frames lift insect_damage AP by 0.09; the matched random-selection control lifts it by 0.03 — the experiment every stakeholder deck should contain.
- **Stopping rule:** active learning rounds continue while marginal AP per 100 labels exceeds an agreed floor; below it, the money moves to a different class or to hard-negative mining (the M4 case study's glare/shadow false positives are acquired this way — *negatives* are labelled data too).

### 5. Dataset versioning and governance

The M1 manifest grows into a release discipline:

- **Immutable releases:** `dates-qc-v2` is a tag over (image set hash, manifest, spec version, changelog) — never edited after release; v3 supersedes it. Metrics without a dataset version attached are anecdotes.
- **Content hashing:** a manifest row carries each file's SHA-256; the release hash covers the manifest — cheap to verify, impossible to silently mutate. DVC and similar tools productionise this; the course implements the 30-line version so the mechanism is understood before the tool is adopted.
- **Split freezes:** the test split is *frozen at v1* and only ever gains items (never re-shuffled) — otherwise cross-version metric comparisons are meaningless. New sessions are assigned to splits at ingestion by hash of `session_id`, making assignment deterministic and argument-free.
- **Changelogs that answer "why did the metric move?":** each release lists items added/removed/relabelled per class, spec-version bumps, and known issues. When v2 lifts mAP by 0.04, the changelog says how much came from cleaning vs new data (the course measures both separately — a discipline that pays off in every retrospective).
- **PDPL and vendor governance:** frames containing workers' hands/faces are personal data — minimise capture (camera framing), mask before vendor export where feasible, restrict vendor access contractually (purpose limitation, no retention after delivery), and log who accessed which release. The annotation contract names the spec version, QA thresholds, agreement targets, and rework terms — quality clauses, not just price per box.

### 6. Common mistakes & production considerations

1. Labelling before the spec has an edge-case gallery — every ambiguous item becomes a per-annotator coin flip; the gallery costs a day and saves a relabelling round.
2. Measuring model quality but never label quality — training a model to beat κ=0.72 labels and blaming the architecture.
3. Pre-labelling without correction-rate monitoring — model errors laundered into ground truth, compounding each round.
4. Active learning on uncertainty alone — the batch collapses onto one pathological cluster (motion-blurred frames), starving other failure modes; add diversity constraints.
5. "Fixing" the test split — the moment the frozen split is edited to remove "unfair" items, every historical comparison dies; additions only, flagged in the changelog.
6. Vendor contracts priced per label with no agreement clause — the incentive is speed, and speed at κ=0.7 costs more in rework than the discount saved.

Production: the dataset release process runs *continuously* after deployment — production frames flow back (with consent/PDPL controls), get triaged by the same uncertainty ranking, and feed quarterly releases; annotation is an operating cost, not a project phase; and dataset lineage (which release trained the deployed model) is an audit requirement in regulated deployments (SDA-AIE-216 wires it into the registry).

## Code Examples

### Model-assisted label audit

```python
# scripts/audit_labels.py
"""Rank training items by classification loss under the current model.
Label errors concentrate at the top; triage the top-N by hand."""
import torch
from torch import nn
from torch.utils.data import DataLoader

from tamr_vision.data.dataset import GRADES, DatesQCDataset
from tamr_vision.data.transforms import eval_tf
from tamr_vision.models.classifier import build_model

model = build_model()
ckpt = torch.load("runs/grade_resnet50/best.pt", map_location="cuda")
model.load_state_dict(ckpt["state_dict"]); model.eval().cuda()

ds = DatesQCDataset(root="data/dates-qc", split="train", transform=eval_tf())
loader = DataLoader(ds, batch_size=64, num_workers=8)
criterion = nn.CrossEntropyLoss(reduction="none")

records = []
with torch.no_grad():
    for i, (imgs, labels) in enumerate(loader):
        logits = model(imgs.cuda())
        losses = criterion(logits, labels.cuda())
        confs, preds = logits.softmax(1).max(1)
        for j in range(len(labels)):
            records.append({
                "idx": i * 64 + j,
                "file": ds.rows.iloc[i * 64 + j]["file"],
                "label": GRADES[labels[j]],
                "pred": GRADES[preds[j]],
                "conf": float(confs[j]),
                "loss": float(losses[j]),
            })

records.sort(key=lambda r: -r["loss"])
# Top-300 go to the triage sheet: label error / model error / ambiguous
import pandas as pd
pd.DataFrame(records[:300]).to_csv("reports/audit_top300.csv", index=False)
print(f"top item: {records[0]['file']}  label={records[0]['label']} "
      f"pred={records[0]['pred']} ({records[0]['conf']:.2f})")
```

### Inter-annotator agreement

```python
# scripts/agreement.py
"""Class kappa + localisation IoU on the double-annotated QA sample."""
import numpy as np
from sklearn.metrics import cohen_kappa_score, confusion_matrix

from tamr_vision.data.qa import load_double_annotations, match_boxes

pairs = load_double_annotations("data/dates-det/qa_double.csv")  # (a1, a2) per item

# --- class agreement on matched instances ---
a1_cls, a2_cls, ious = [], [], []
for item in pairs:
    for b1, b2, iou in match_boxes(item.ann1, item.ann2, iou_floor=0.3):
        a1_cls.append(b1.cls); a2_cls.append(b2.cls); ious.append(iou)

kappa = cohen_kappa_score(a1_cls, a2_cls)
print(f"class kappa on matched instances: {kappa:.3f}  (bar: >= 0.85)")
print(f"localisation: median IoU={np.median(ious):.3f}  (bar: >= 0.85)")
print("annotator confusion (rows=A1, cols=A2):")
print(confusion_matrix(a1_cls, a2_cls))          # the ambiguous-rule detector
```

### Uncertainty + diversity sampling for the next labelling round

```python
# scripts/select_next_batch.py
"""Pick B frames to label next: detector uncertainty, diversity-capped.
Control group (random) selected alongside — ALWAYS run the experiment."""
import numpy as np
from sklearn.cluster import KMeans
from ultralytics import YOLO

B, N_CLUSTERS, CAP = 800, 40, 30
model = YOLO("runs/detect/defect_y11s/weights/best.pt")

pool = load_unlabelled_pool("data/dates-qc/unlabelled_manifest.csv")  # 18k frames
scores, embeds = [], []
for frame in pool:
    r = model.predict(frame.path, imgsz=640, conf=0.05, verbose=False)[0]
    conf = r.boxes.conf.cpu().numpy()
    # uncertainty: detections hovering near the decision boundary
    scores.append(float(np.sum(1.0 - np.abs(2 * conf - 1))) if len(conf) else 0.1)
    embeds.append(embed(frame))                  # backbone GAP features, provided

order = np.argsort(scores)[::-1]                 # most uncertain first
clusters = KMeans(N_CLUSTERS, random_state=212).fit_predict(np.array(embeds))
picked, per_cluster = [], np.zeros(N_CLUSTERS, int)
for i in order:                                  # greedy with diversity cap
    if per_cluster[clusters[i]] < CAP:
        picked.append(i); per_cluster[clusters[i]] += 1
    if len(picked) == B:
        break
export_labelling_task(pool, picked, name="round2_uncertain")
export_labelling_task(pool, np.random.default_rng(212).choice(len(pool), B, replace=False),
                      name="round2_random_control")
```

### Dataset release with manifest hash

```python
# scripts/release_dataset.py
"""Cut an immutable dataset release: manifest + SHA-256 + changelog stub.
The 30-line version of what DVC productionises."""
import hashlib
import json
from pathlib import Path

import pandas as pd

VERSION = "dates-qc-v2"
manifest = pd.read_csv("data/dates-qc/manifest_v2.csv")

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()

manifest["sha256"] = [sha256(Path("data/dates-qc/images") / f)
                      for f in manifest["file"]]
manifest.to_csv(f"releases/{VERSION}/manifest.csv", index=False)

release_hash = hashlib.sha256(
    Path(f"releases/{VERSION}/manifest.csv").read_bytes()).hexdigest()
json.dump({
    "version": VERSION,
    "spec_version": "annotation-spec-v2",
    "release_hash": release_hash,
    "counts_by_class": manifest["grade"].value_counts().to_dict(),
    "changelog": {
        "relabelled": 447, "added": 800, "removed_duplicates": 61,
        "notes": "sugaring/mould co-occurrence rule; insect_damage AL round 2",
    },
}, open(f"releases/{VERSION}/RELEASE.json", "w"), indent=2)
print(f"{VERSION} released: {release_hash[:12]}…  (test split UNCHANGED from v1)")
```

## Hands-on Lab 5 — Audit and Curate Dataset v2

| | |
|---|---|
| **Objective** | Find and triage label errors with model-assisted auditing, fix the annotation spec, run agreement analysis on the QA sample, and cut the versioned `dates-qc-v2` release |
| **Duration** | 50 minutes |
| **Setup** | M2 classifier + M3 detector checkpoints present; `git checkout lab5-start`; CVAT/Label Studio instance reachable (offline fallback: provided triage CSV workflow) |

**Instructions & tasks**

1. *(10 min)* Run `audit_labels.py`; open the top-300 sheet. Triage the top 40 with your pair into label error / model error / ambiguous (target rate: expect ~60% label errors — the set contains 25 planted errors plus v1's real ones).
2. *(8 min)* For the "ambiguous" pile, draft one new boundary rule and one edge-case gallery entry for `ANNOTATION_SPEC.md`; PR it against the course spec repo.
3. *(8 min)* Run `agreement.py` on the double-annotated QA sample; identify from the annotator confusion matrix which class pair drives disagreement and check it matches your spec fix.
4. *(12 min)* Relabel your triaged label errors in the annotation tool (pre-labelling ON; note your own correction rate). Offline fallback: corrections recorded in the triage CSV.
5. *(8 min)* Run `select_next_batch.py` to generate the round-2 task and its random control; then cut the release with `release_dataset.py`. Verify the test split is byte-identical to v1 (`scripts/verify_split_freeze.py`).
6. *(4 min)* Commit: `feat(data): dates-qc-v2 — audited, spec v2, AL round 2 selected`. Retraining on v2 happens in Day 3 Hour 5 — record the v1 baseline numbers now.

**Expected output**
```
$ python scripts/audit_labels.py
top item: s041_f0187.jpg  label=standard pred=reject (0.97)
$ python scripts/agreement.py
class kappa on matched instances: 0.792  (bar: >= 0.85)
localisation: median IoU=0.872
$ python scripts/release_dataset.py
dates-qc-v2 released: 9e4f21c07ab3…  (test split UNCHANGED from v1)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Audit top-40 looks like all model errors | Loaded the wrong (early/underfit) checkpoint | Load `best.pt`; verify val F1 first |
| Kappa suspiciously = 1.0 | Comparing an annotator against themselves (join bug) | Check annotator IDs in the QA join |
| CVAT tasks empty | Export path/format mismatch | Re-export as YOLO 1.1; check task assignment |
| Release hash differs between pair machines | Line-ending mutation in manifest CSV | Write with `newline=""`; hash bytes, not text |
| Split-freeze verify fails | v2 manifest re-assigned a session | Restore split column from v1 for shared sessions |

**Instructor notes.** The triage discipline is the assessable behaviour: pairs that mark everything "label error" and mass-fix without the QA step have missed the auditor-bias point — ask them who audits the auditor. Task 3's confusion matrix is engineered to point at the sugaring/skin_split cell so the spec-fix loop closes visibly. The retrain-on-v2 comparison in Hour 5 is the emotional payoff of the whole day; make each pair predict their v2 delta *before* the run and confront the prediction after. Fast finishers: compute per-annotator kappa against gold tasks and draft the (private) feedback note for the weakest performer.

## Mini Exercises

**Quiz (5 questions)**
1. Why does Cohen's kappa beat raw percent agreement? → corrects for chance agreement; imbalanced classes make raw agreement flattering.
2. Two annotators agree perfectly with each other but both fail gold tasks. Diagnosis? → shared misunderstanding of the spec; agreement measures consistency, not correctness.
3. Name the three triage categories for a loss-ranked audit item and where the third one goes. → label error / model error / ambiguous → spec edge-case gallery.
4. Why must the test split never be re-shuffled between releases? → cross-version metric comparisons become meaningless; freeze + additions only.
5. True/False: pre-labelling always improves dataset quality because it speeds annotation. → **False** — without correction-rate monitoring it launders model errors into ground truth.

**Debugging exercise.** Branch `sim-anchor-bias`: dataset v2b was produced with pre-labelling at `conf=0.05` (every model guess shown as draft). The retrained model's val mAP *rises* but the frozen-test mAP *falls*. Participants must explain the divergence (val split was relabelled with anchored drafts; test stayed honest) and propose the two defences (confidence floor, from-scratch fraction).

**Code-review exercise.** Review a dataset PR that (a) edits three "unfair" test-split labels, (b) bumps the spec without re-annotating affected classes, and (c) has no changelog entry separating cleaning from additions. Three findings with the downstream cost of each.

**Discussion questions.**
- The vendor offers −30% per box if QA sampling drops from 10% to 2%. Price the offer using the module's numbers (rework rate at κ<0.75, relabelling round cost).
- Production frames from the plant contain workers' hands. Design the flow-back pipeline's PDPL controls (masking before vendor export, purpose limitation, retention, access log) and name who signs off.

## Case Study — Drone-Based Palm Health Survey in Al-Ahsa

**Scenario.** An agricultural services company surveys 2.4 million date palms yearly by drone for a government sustainability programme. Trees are classified per-canopy as healthy / pest-stressed (red palm weevil suspects) / drought-stressed / dead. The first annotation round — 40,000 canopies by an offshore vendor — comes back on time and on budget; the model trained on it performs beautifully on validation and embarrassingly in the field: agronomists reject 31% of its pest-stress flags.

**Business context.** Pest-stress flags trigger physical inspections costing ~180 SAR each; false flags burn the inspection budget, and missed weevil infestations spread to neighbouring farms — the programme's entire justification. The ministry requires evidence of survey quality before renewing the mandate.

**Technical challenge.** Diagnose whether the failure is model, labels, or spec — with numbers — and design the second annotation round to fix it within a 55,000-canopy budget.

**Constraints.** Ground-truth verification requires a field visit (expensive, slow — only 600 canopies verifiable per round); pest and drought stress look similar in RGB (the distinguishing signs are subtle: frond-base boreholes vs uniform browning); the vendor contract has a rework clause only if agreement metrics were specified — they were not; imagery of private farms carries access restrictions.

**Solution approach (facilitate, don't lecture).** Instrument before blaming: double-annotate a 2,000-canopy sample internally — result (per the case pack) κ=0.58 on pest-vs-drought, near-perfect on healthy/dead: the taxonomy is under-specified, not the vendor lazy. Field-verify 600 canopies stratified by model confidence: labels wrong on 24% of pest flags — the model faithfully learned a confused spec. Fix: spec v2 with a reference-image gallery shot by agronomists (boreholes, frond patterns), a "pest-suspect — needs field check" *uncertain* class (routing ambiguity to humans instead of forcing a coin flip), and gold tasks embedded in every future batch. Spend the 55,000 budget as: 8,000 relabels of the confused region (selected by model disagreement), 2,000 gold-task creations with field photos, 45,000 new canopies with uncertainty sampling stratified across farm regions. Contract v2 names κ ≥ 0.8 on the pest/drought pair with rework at vendor cost. The renewal evidence pack is the agreement dashboard plus the field-verification confusion matrix — label quality as a first-class deliverable.

**Discussion questions.**
1. The model's validation metrics were excellent throughout. Reconstruct exactly why that was compatible with 31% field rejection. (val shared the labels' confusion — the ceiling argument from §3.)
2. Was adding the "uncertain" class an admission of failure? Argue both sides with the inspection-budget numbers.
3. Which 600 canopies should get field verification? Design the stratification.
4. The vendor asks for the full-resolution imagery to "improve their tooling". Response under the farm-access restrictions and PDPL-adjacent confidentiality terms?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Label errors found in top-300 audit ranking | Process quality | ≥ 70% of planted errors recovered | triage sheet vs answer key |
| Triage categorisation accuracy (top 40) | Process quality | ≥ 80% match to reference triage | instructor key |
| Class kappa on QA sample (post-spec-fix round) | Label quality | ≥ 0.85 | `agreement.py` |
| Test-split freeze integrity v1→v2 | Reliability | byte-identical | `verify_split_freeze.py` |
| Release completeness | Code quality | manifest + hashes + spec version + changelog | release checklist |
| v2 retrain delta (measured Day 3 H5) | Model quality | insect_damage AP +0.05 or better vs v1 | frozen-test comparison |

**Example benchmark table (filled during lab):**

| Item | v1 | v2 | Delta | Attribution |
|---|---|---|---|---|
| Grade classifier macro-F1 | 0.90 | 0.92 | +0.02 | 447 relabels |
| Detector mAP@0.5 | 0.872 | 0.903 | +0.031 | cleaning + 800 AL frames |
| insect_damage AP@0.5 | 0.798 | 0.887 | +0.089 | AL round (control: +0.031) |
| Class kappa (QA sample) | 0.792 | 0.861 | +0.069 | spec v2 boundary rules |

## Required Visuals and Training Assets

### Diagrams
1. **The data flywheel** — *Purpose:* anchor image. *Elements:* circular flow — deploy → capture → uncertainty triage → annotate (pre-labelled) → QA/agreement → versioned release → retrain → deploy; PDPL gate drawn on the capture→annotate edge. *Style:* cycle diagram, course palette, English labels with Arabic subtitles.
2. **Where label budgets die** — *Elements:* Sankey from "100% budget" into: easy frames (random sampling), rework (ambiguous spec), anchored errors (unmonitored pre-labelling), value; a second Sankey with the module's defences applied. *Style:* before/after Sankey pair — the module's economics argument.
3. **Loss-ranked audit concentration** — *Elements:* curve of cumulative label errors found vs number of items reviewed, loss-ranked vs random order; the "top 300 = 70%" region shaded. *Style:* single chart, doubles as a stakeholder slide.
4. **Release lineage** — *Elements:* v1 → v2 → v3 boxes with hashes, spec versions, frozen-test lane running unchanged underneath, model checkpoints hanging off each release. *Style:* git-graph-like horizontal timeline.

### Images (screenshots)
1. **CVAT/Label Studio session with pre-labels** — *why:* tool orientation; *content:* dates frame with draft boxes, correction in progress, guidelines panel showing spec v2 boundary rule.
2. **Triage sheet reference** — *why:* expected working state for Lab 5 task 1; *content:* top-40 CSV with the three-way triage column part-filled.
3. **Annotator confusion matrix output** — *why:* the ambiguous-rule detector made visible; *content:* terminal output with the sugaring↔skin_split cell highlighted.
4. **RELEASE.json** — *why:* release-completeness reference; *content:* the v2 release record with hash, counts, changelog.

### Simulations
1. **Anchor bias** — *Setup:* branch `sim-anchor-bias` (pre-labelling with no confidence floor). *Expected behaviour:* val improves, frozen test degrades; correction-rate log shows near-zero corrections. *Learning objective:* pre-labelling defences are mandatory, not optional.
2. **Spec drift** — *Setup:* branch `sim-spec-drift`: half the v2 labels made under v1 rules, mixed silently. *Expected behaviour:* agreement metrics fine within each half, poor across; per-`spec_version` slicing exposes it. *Learning objective:* spec version travels with every annotation.

### Interactive Activities
- **Spec-writing sprint (15 min):** pairs receive 10 genuinely ambiguous dates images and must write boundary rules + gallery entries that make a *different* pair label all 10 identically; the receiving pair's agreement score is the grade.
- **Budget allocation game (10 min):** teams get a virtual 50k-SAR labelling budget and the v1 per-class AP table; they must allocate across relabelling, gold tasks, AL rounds, and QA sampling, then defend the split against the instructor's marginal-value questioning.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Audit answer key | Course team (25 planted errors + verified v1 errors) | CSV | 300 rows | Triage scoring |
| `qa_double.csv` | Course team: 400 items double-annotated | CSV | 800 annotations | Agreement analysis |
| Unlabelled pool | Course team | JPEG + manifest | 18,000 frames | Active-learning selection |
| Gold-task set | Course team, expert-labelled | CVAT export | 120 items | Annotator calibration exercise |

### Demo Requirements
- **Instructor demo:** run the audit live and open the #1 ranked item on the projector (a planted, obvious label error — the gasp moment); then the agreement matrix pointing at the ambiguous class pair.
- **Student demo:** one pair presents their spec fix and the receiving pair's agreement score from the spec-writing sprint.
- **Expected outputs:** every pair has a triaged audit, a merged spec PR, the v2 release cut, and v1 baseline numbers recorded for the Hour-5 retrain comparison.

---

# Module 6 — Model Evaluation for Vision Tasks

## Module Overview

**Purpose.** Every module so far has consumed metrics; this one makes participants produce them from first principles and — more importantly — distrust them intelligently. Participants implement IoU matching and mAP by hand once (so the numbers stop being framework magic), then build the course's evaluation harness: frozen splits, deterministic runs, per-class and per-slice reporting, a detection error taxonomy, and operating-point analysis. The harness is itself a deliverable — it becomes the capstone's referee and the regression gate that SDA-AIE-216 will automate.

**Business relevance.** Vision systems get bought, renewed, and litigated on numbers. An engineer who can only say "mAP is 0.87" cannot answer the questions that decide contracts: *what is the escape rate on the defect class that triggers retailer audits? does the system degrade at night, at shift change, on the smallest fruit? did last month's retrain make the model better or just different?* Aggregate metrics systematically hide minority-slice failures — the M1 hospital case (five weeks of green dashboards over a 17-point per-site drop) is the canonical shape of this failure, and slice-level evaluation is its only reliable defence. In procurement settings across the region, a rigorous, reproducible evaluation harness is increasingly a contractual artefact: it is what "acceptance testing" means for a vision system.

**Industry use cases.**
- Tamr Vision's harness: per-class, per-session, per-fruit-size slices over the frozen v1 test split; it is what proved the v2 dataset's insect_damage gain was real (+0.089) and not test-set drift, and what sets the capstone's acceptance numbers.
- A Riyadh smart-traffic programme where fleet-wide vehicle-detection mAP of 0.91 concealed 0.62 recall on motorcycles at night — found only when the evaluation was sliced by class × time-of-day, after two collision-warning misses.
- A regional bank's document-vision system where the acceptance test is a frozen 5,000-document harness run witnessed by both vendor and bank — disagreements resolved by the error-gallery, not by argument.

**Expected competencies.** After this module a participant can implement IoU-based matching and compute AP/mAP from raw predictions; explain precisely what mAP@0.5 vs mAP@0.5:0.95 reward; design slice taxonomies and read per-slice reports; classify detection errors (miss, misclassification, localisation, duplicate, background) and prioritise fixes by error mass; select operating points from PR curves against business constraints; and run regression comparisons between model versions on frozen splits with honest significance judgement.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Implement IoU matching and AP/mAP computation from raw predictions | LO5 |
| 6.2 | Interpret mAP variants, per-class AP, and PR curves; choose operating points against constraints | LO5, LO2 |
| 6.3 | Design slice-based evaluation and detect minority-slice failures hidden by aggregates | LO5, LO3 |
| 6.4 | Classify detection errors into a taxonomy and prioritise remediation by error mass | LO5 |
| 6.5 | Build a deterministic, versioned evaluation harness usable as a regression gate | LO5, LO6 |

## Technical Content

### 1. IoU and the matching problem

Detection evaluation begins with a question classification never faces: *which prediction corresponds to which ground truth?* The procedure, implemented by hand in Lab 6:

1. Sort predictions by confidence, descending.
2. For each prediction, compute IoU against all unmatched ground-truth boxes of the same class in the same image.
3. If the best IoU ≥ threshold (0.5 for mAP@0.5), it is a **true positive** and that GT is consumed; otherwise a **false positive**.
4. Unconsumed ground truths are **false negatives**.

Every subtlety that trips practitioners lives here: greedy matching by confidence order (a confident sloppy box can steal the GT from a later precise one), the same-class constraint (a perfect box with the wrong class is a false positive *and* leaves a false negative — double punishment, correctly), and the IoU threshold as a *definition of correct*, not a tuning knob. Mask IoU substitutes pixel overlap and everything else carries over — M4's hand exercise was this primitive.

### 2. Precision, recall, and average precision

From the matched predictions, sweep confidence from high to low and trace the **PR curve**: each prediction added either extends recall (TP) or drops precision (FP). **AP** is the area under this curve (with interpolation smoothing the sawtooth); **mAP** averages AP over classes — and that innocuous averaging is where dashboards go to lie, because a 310-instance `foreign_object` class weighs exactly as much as an 1,860-instance `mould` class.

- **mAP@0.5** asks "does the detector find and roughly localise things?" — the applied headline for tasks where presence matters more than pixel-perfect boxes.
- **mAP@0.5:0.95** (COCO-style: averaged over IoU thresholds 0.5→0.95) additionally rewards tight localisation. Tamr Vision cares because eject-gate targeting uses box centres; the road-crack case (M4) cares because area is money. Rule taught: report both, know which one the *use case* pays for.
- **AP is threshold-free; deployment is not.** AP summarises all operating points; the line runs at exactly one. The M3 sweep (recall/FP-per-image vs confidence) is the bridge, and it belongs *in* the harness, not in a notebook that disappears.

### 3. Slices: the aggregate is always hiding something

A slice is any subset with a reason to differ: class (already standard), **session/station** (camera drift, the M2 planted-leakage probe), **object size** (COCO's small/medium/large convention — small objects fail first and matter most on wide shots), **lighting/time bucket**, **dataset release** (v1-original vs v2-added items), and — in deployment — **date of capture**. Harness design rules:

- Slices are *declared in config*, not improvised per analysis — improvised slicing after seeing results is p-hacking with extra steps; the taxonomy is reviewed like code.
- Every slice report carries **n** — a 0.71 recall on a 14-item slice is a hypothesis, not a finding. The course threshold: slices under 50 instances render greyed-out in the report.
- The headline table is *worst-slice*, not average: "min per-class recall across sessions" catches what the mean launders. The M1 hospital case, restated: the model that is fine on average and broken at one site is broken.

### 4. The detection error taxonomy

"mAP dropped 3 points" is not actionable; *where the error mass sits* is. The harness classifies every non-TP event (TIDE-style, simplified to five buckets the class can hold in mind):

| Error type | Definition | Typical root cause | Typical fix |
|---|---|---|---|
| **Miss** | GT with no prediction at any confidence | small objects, rare class, occlusion | data acquisition (M5), resolution (M7 trade-off) |
| **Misclassification** | right place (IoU ≥ 0.5), wrong class | confusable classes, label noise | spec/boundary rules (M5), targeted relabels |
| **Localisation** | right class, 0.1 ≤ IoU < 0.5 | sloppy annotation, thin/elongated objects | annotation QA, DFL behaviour at extreme aspect ratios |
| **Duplicate** | second+ match to a consumed GT | NMS threshold vs touching objects | NMS tuning (M3), crowd-aware post-processing |
| **Background** | FP with no GT overlap (IoU < 0.1) | hard negatives (glare, belt marks) | hard-negative mining (M5) |

The payoff is a *ranked remediation plan*: on dates-qc v1, misclassification (sugaring↔skin_split) carried 41% of error mass — which is why M5's spec fix, not a bigger model, was the right spend. Participants compute this table for their own models and write the plan; it is the written deliverable of Day 3.

### 5. The harness as an engineering artefact

Everything above ships as `tamr_vision/eval/` with the disciplines the template course (SDA-AIE-113) taught applied to evaluation:

- **Frozen inputs:** test split pinned by release hash (M5); predictions cached to parquet so re-analysis never re-runs inference; the eval config (thresholds, slices, IoU definitions) versioned alongside.
- **Determinism:** two runs of the harness on the same (model, split, config) triple produce byte-identical reports — the M1/M2 determinism rules, now enforced by a CI-style check.
- **Regression mode:** `compare(model_a, model_b)` emits per-class and per-slice deltas with n, flags any slice that degraded ≥ 2 points even if the aggregate improved, and renders the error-gallery diff (frames where the verdicts changed). This ran in Day 3 Hour 5 for v1-vs-v2 and referees the capstone.
- **The error gallery:** for every error bucket, the k worst frames rendered with GT vs prediction overlays. Galleries settle arguments that tables start; they are also the artefact non-technical stakeholders actually read.
- **Honest deltas:** with a 1,400-instance test split, per-class AP has meaningful run-to-run and split-resampling noise; the course rule of thumb — treat |ΔAP| < 0.01 as noise, 0.01–0.03 as "probably real, check the gallery", > 0.03 as real — plus the bootstrap CI script for when it matters contractually.

### 6. Common mistakes & production considerations

1. Reporting mAP at `conf=0.001` (framework default sweep) while the product runs at 0.35, then wondering why field precision disappoints — always report the deployed operating point alongside AP.
2. Comparing models across *different* test splits or releases — the number moved because the exam changed; frozen splits or silence.
3. Slicing after peeking — declaring slices post hoc to explain a result invites false discoveries; the taxonomy precedes the run.
4. Ignoring n on slices — small-slice panic (or comfort) drives bad retrains; grey out under-powered slices.
5. Averaging away class imbalance — macro-mAP treats `foreign_object` (310 instances, audit-triggering) equal to `mould`; the harness reports per-class always, and the *business-weighted* summary is a separate, documented row.
6. Evaluating only the model, never the measurement — M4's area-MAE and grading-disagreement rate live in the same harness; a vision *system* is graded on its output numbers, not its intermediate tensors.

Production: the harness is the regression gate for every retrain (SDA-AIE-216 wires it into CI/CD); a *shadow* harness over sampled production frames with delayed human labels closes the loop on real drift (M8 builds exactly this); and acceptance tests with customers should hand over the harness + frozen split, not a PDF of numbers — reproducibility is the trust mechanism.

## Code Examples

### IoU matching and AP from first principles

```python
# src/tamr_vision/eval/matching.py
"""The primitive under every detection metric. Implemented once, by hand,
so mAP stops being framework magic. Vectorised enough to be honest."""
import numpy as np


def iou_matrix(pred: np.ndarray, gt: np.ndarray) -> np.ndarray:
    """pred (P,4), gt (G,4) as xyxy -> IoU (P,G)."""
    px1, py1, px2, py2 = pred[:, 0, None], pred[:, 1, None], pred[:, 2, None], pred[:, 3, None]
    gx1, gy1, gx2, gy2 = gt[None, :, 0], gt[None, :, 1], gt[None, :, 2], gt[None, :, 3]
    iw = np.clip(np.minimum(px2, gx2) - np.maximum(px1, gx1), 0, None)
    ih = np.clip(np.minimum(py2, gy2) - np.maximum(py1, gy1), 0, None)
    inter = iw * ih
    union = ((px2 - px1) * (py2 - py1)) + ((gx2 - gx1) * (gy2 - gy1)) - inter
    return inter / np.clip(union, 1e-9, None)


def match_image(preds, gts, iou_thr: float = 0.5):
    """Greedy matching in confidence order. Returns per-prediction TP flags
    and the set of unmatched (missed) GT indices."""
    order = np.argsort(-preds["conf"])
    tp = np.zeros(len(order), bool)
    consumed = np.zeros(len(gts["boxes"]), bool)
    iou = iou_matrix(preds["boxes"], gts["boxes"]) if len(gts["boxes"]) else None
    for rank, p in enumerate(order):
        if iou is None:
            break
        same_cls = gts["cls"] == preds["cls"][p]
        cand = np.where(same_cls & ~consumed)[0]
        if len(cand) == 0:
            continue
        best = cand[np.argmax(iou[p, cand])]
        if iou[p, best] >= iou_thr:
            tp[rank], consumed[best] = True, True
    return tp[np.argsort(order)], np.where(~consumed)[0]


def average_precision(tp: np.ndarray, conf: np.ndarray, n_gt: int) -> float:
    """AP with 101-point interpolation (COCO convention)."""
    order = np.argsort(-conf)
    cum_tp = np.cumsum(tp[order])
    cum_fp = np.cumsum(~tp[order])
    recall = cum_tp / max(n_gt, 1)
    precision = cum_tp / np.clip(cum_tp + cum_fp, 1, None)
    ap = 0.0
    for r in np.linspace(0, 1, 101):
        p = precision[recall >= r]
        ap += (p.max() if len(p) else 0.0) / 101
    return float(ap)
```

### The slice report

```python
# src/tamr_vision/eval/slices.py
"""Per-slice metrics with n. Slices are DECLARED in eval config —
never improvised after seeing results."""
SLICES = {                                    # eval_config.yaml mirrors this
    "class": lambda item: item.cls_name,
    "session": lambda item: item.session_id,
    "size": lambda item: ("small" if item.gt_area < 32**2
                          else "large" if item.gt_area > 96**2 else "medium"),
    "release": lambda item: item.added_in,    # v1-original vs v2-added
}
MIN_N = 50                                    # under-powered slices render greyed


def slice_report(matched_items) -> dict:
    report = {}
    for name, keyfn in SLICES.items():
        groups = {}
        for item in matched_items:
            groups.setdefault(keyfn(item), []).append(item)
        report[name] = {
            key: {
                "n": len(items),
                "recall": recall_of(items),
                "ap50": ap_of(items, iou_thr=0.5),
                "powered": len(items) >= MIN_N,
            } for key, items in sorted(groups.items())
        }
    # the headline is the WORST powered slice, not the mean
    worst = min((s for g in report.values() for s in g.values() if s["powered"]),
                key=lambda s: s["recall"])
    report["_headline"] = {"worst_powered_slice_recall": worst["recall"]}
    return report
```

### Error taxonomy and regression comparison

```python
# scripts/eval_report.py
"""Full harness run: metrics + slices + error taxonomy + gallery.
Regression mode compares two checkpoints on the same frozen split."""
import argparse

from tamr_vision.eval import harness

parser = argparse.ArgumentParser()
parser.add_argument("--model", required=True)
parser.add_argument("--baseline")                 # enables regression mode
parser.add_argument("--split", default="test@dates-qc-v1")   # release-pinned
args = parser.parse_args()

run = harness.evaluate(args.model, split=args.split,
                       config="configs/eval_v1.yaml")   # thresholds, slices, seeds
run.save("reports/eval")                          # parquet cache + HTML report

print(f"mAP@0.5={run.map50:.3f}  mAP@0.5:0.95={run.map5095:.3f}")
print("error mass:", run.error_taxonomy())
# {'miss': 0.23, 'misclassification': 0.41, 'localisation': 0.14,
#  'duplicate': 0.07, 'background': 0.15}

if args.baseline:
    diff = harness.compare(args.baseline, args.model, split=args.split)
    for slice_name, delta, n in diff.degraded(threshold=0.02):
        print(f"REGRESSION  {slice_name}: {delta:+.3f}  (n={n})")
    diff.render_gallery("reports/eval/verdict_changes/")   # frames that flipped
```

### Bootstrap confidence interval (for when a delta is money)

```python
# scripts/bootstrap_ci.py
"""Is v2 really better, or did we get lucky? Resample images with
replacement; report the 95% CI on the AP delta."""
import numpy as np

def bootstrap_delta(per_image_a, per_image_b, n_boot=2000, seed=212):
    rng = np.random.default_rng(seed)
    n = len(per_image_a)
    deltas = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        deltas.append(ap_from_images([per_image_b[i] for i in idx])
                      - ap_from_images([per_image_a[i] for i in idx]))
    lo, hi = np.percentile(deltas, [2.5, 97.5])
    print(f"ΔAP 95% CI: [{lo:+.4f}, {hi:+.4f}]"
          + ("  — crosses zero: NOT established" if lo < 0 < hi else "  — real"))
```

## Hands-on Lab 6 — Build the Evaluation Harness

| | |
|---|---|
| **Objective** | Implement matching + AP by hand, validate against Ultralytics, produce the slice report and error taxonomy for your own M3 detector, and write the ranked remediation plan |
| **Duration** | 50 minutes (plus the Hour-5 v1-vs-v2 regression run) |
| **Setup** | M3/M4 checkpoints + cached predictions provided; `git checkout lab6-start`; no GPU needed (inference is pre-cached to parquet) |

**Instructions & tasks**

1. *(12 min)* Implement `iou_matrix` and `match_image`; pass the provided unit tests (12 cases including the confidence-order steal, the wrong-class perfect box, and the empty-GT image).
2. *(8 min)* Implement `average_precision`; validate your per-class AP@0.5 against the Ultralytics values for the same predictions — agreement within ±0.005 required; investigate any gap (the usual culprit: matching order).
3. *(10 min)* Run the slice report on your detector. Record the worst powered slice in `BENCHMARKS.md` and check whether it was visible in the aggregate (it will not be: session s09 — evening captures — is planted to underperform).
4. *(10 min)* Run the error taxonomy; render the gallery for your two largest buckets. With your pair, write the five-line ranked remediation plan (error mass → root cause → fix → cost).
5. *(8 min)* Determinism check: run the harness twice; diff the reports (must be byte-identical). Then run once with `--seed 999` and note which numbers legitimately may not move (all of them — inference is cached; the point lands).
6. *(2 min)* Commit: `feat(eval): harness v1 + error analysis report`.

**Hour-5 continuation (retrain + regression).** After the v2 retrain, run regression mode v1-vs-v2: confirm the insect_damage gain, check no powered slice degraded ≥ 2 points, and run the bootstrap CI on the headline delta. Paste the regression summary into the day's error-analysis report — this document is a graded deliverable.

**Expected output**
```
$ pytest tests/eval/ -q
12 passed in 1.84s
$ python scripts/eval_report.py --model runs/detect/defect_y11s/weights/best.pt
mAP@0.5=0.872  mAP@0.5:0.95=0.641
error mass: {'miss': 0.23, 'misclassification': 0.41, 'localisation': 0.14,
             'duplicate': 0.07, 'background': 0.15}
worst powered slice: session=s09 recall=0.71 (n=142)   # invisible in aggregate
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| AP off by 0.02–0.05 vs Ultralytics | Matching not in confidence order / GT re-use | Sort predictions first; consume matched GT |
| AP > validated value on empty-GT images | FPs on empty images not counted | Empty-GT images still contribute FPs |
| Reports differ between two "identical" runs | Timestamp inside the report file | Exclude generated-at fields from the diff (or fix the template) |
| Slice report all greyed out | Slice keys too fine (per-frame sessions) | Check slice key functions against the manifest |
| Bootstrap CI absurdly wide | Resampling instances, not images | Resample at the image level (correlated instances) |

**Instructor notes.** Task 3's planted s09 slice is the module's thesis in one row: every pair sees a healthy aggregate hiding a 0.71-recall slice they would have shipped. Ask each pair to say aloud what dashboard would have caught it in production (per-session control charts — the SDA-AIE-216 hook). The remediation plan from task 4 is the best predictor of capstone quality; grade it formatively now. The taxonomy's dominant bucket (misclassification) should visibly connect back to M5's spec fix — draw the arrow on the board. Fast finishers: implement mAP@0.5:0.95 (loop the matcher over thresholds) and reconcile with the framework.

## Mini Exercises

**Quiz (5 questions)**
1. A perfect box with the wrong class counts as what in matching? → a false positive *and* leaves a false negative — double punishment, by design.
2. mAP@0.5 vs mAP@0.5:0.95 — which does eject-gate targeting care about and why? → 0.5:0.95; box centres drive actuation, so tight localisation is paid for.
3. Why must slices be declared before the run? → post-hoc slicing is multiple-comparison fishing; the taxonomy is reviewed like code.
4. Error mass is 41% misclassification between two specific classes. First fix? → annotation spec/boundary rules and targeted relabels (M5), not a bigger model.
5. True/False: a model whose aggregate mAP improved cannot have regressed on any slice. → **False** — regression mode exists precisely because this happens routinely.

**Debugging exercise.** Branch `sim-threshold-report`: the harness reports metrics computed at `conf=0.001` while the model card claims the deployed 0.35 operating point. Field precision complaints arrive. Participants must find the mismatch, add the "deployed operating point" row to the report, and explain the 0.31 precision gap between the two views.

**Code-review exercise.** Review an evaluation PR that (a) re-shuffles the test split "for freshness", (b) reports only macro-mAP with no per-class table, and (c) claims v3 > v2 from a +0.008 delta with no CI. Three findings with the decision each would corrupt.

**Discussion questions.**
- The plant manager wants "one number" for the weekly report. Which one do you give — and what second number do you insist travels with it? (worst powered slice recall + n; or the business-weighted summary with its definition.)
- A vendor's acceptance test is a live demo on frames they chose. Rewrite the acceptance clause using this module's vocabulary. (frozen split under buyer custody, harness handover, per-slice floors, error gallery review.)

## Case Study — Night-Slice Failure in a Riyadh Traffic Vision Programme

**Scenario.** A city-scale traffic programme runs vehicle detection on 900 intersections for signal optimisation and incident alerts. The vendor's quarterly report shows fleet mAP@0.5 of 0.91, stable for a year. Then two incident-detection misses in one month — both involving motorcycles, both between 22:00 and 03:00 — trigger an engineering review with the vendor's numbers on one side and two near-collisions on the other.

**Business context.** The programme's renewal is before the budget committee; the vendor contract specifies "mAP ≥ 0.88 quarterly" and nothing else. The city's traffic-safety KPI counts motorcycle incidents separately — they are 4% of vehicles and 28% of fatalities in the corridor under review.

**Technical challenge.** Reconstruct how a contractually green system missed the failures, quantify the real slice-level performance, and rewrite the acceptance criteria so the contract measures what the KPI cares about.

**Constraints.** The vendor controls the model; the city controls the cameras and a 20,000-frame labelled archive; night frames are 18% of traffic but 6% of the vendor's test set (inherited from a daytime-heavy public dataset); motorcycle instances at night in the vendor's test set: 41. Neither party wants a procurement dispute; both want renewal with defensible terms.

**Solution approach (facilitate, don't lecture).** The review team builds an independent harness over the city's archive with declared slices: class × time-bucket × intersection type. Findings (per the case pack): motorcycles-at-night recall 0.62 (n=1,340) against fleet mAP 0.91 — the aggregate was arithmetically true and operationally meaningless; the vendor's own test set could never have seen it (n=41, under-powered and greyed out by any honest report). Remediation follows the error taxonomy: misses dominate (small, low-light, headlight bloom), so the fix is data acquisition — 6,000 night-motorcycle frames via targeted mining of the archive plus hard-negative bloom examples — not architecture. Contract v2: per-slice floors (motorcycle night recall ≥ 0.85 with n ≥ 500), the city's frozen split as referee, harness handover with byte-identical reproducibility, and quarterly regression mode with a no-degraded-slice clause. The renewal deck leads with the error gallery: eight frames of missed motorcycles convince the committee faster than any table.

**Discussion questions.**
1. The vendor's 0.91 was honest arithmetic. List every methodological choice that still made it misleading, in order of culpability.
2. Design the slice taxonomy for this system. Which slices are declared, and what are their n requirements?
3. Who should own the frozen split in a buyer/vendor relationship, and what does "handover of the harness" mean legally? (acceptance-test custody — connect to the bank example.)
4. The city could demand mAP ≥ 0.95 instead. Why is that the wrong fix? (aggregate floors don't bind slices; also pays for over-performance nobody needs on cars-at-noon.)

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Matching + AP unit tests | Code quality | 12/12 passing | pytest |
| AP agreement vs framework | Correctness | within ±0.005 per class | validation script |
| Harness determinism | Reliability | byte-identical repeat reports | diff |
| Worst-slice detection | Analysis quality | s09 slice found and reported | `BENCHMARKS.md` |
| Error-taxonomy report + remediation plan | Analysis quality | 5-line ranked plan, costed | instructor review |
| v1-vs-v2 regression summary (Hour 5) | Analysis quality | delta + CI + no-degraded-slice check | report review |

**Example benchmark table (filled during lab):**

| View | Value | n | Verdict |
|---|---|---|---|
| Aggregate mAP@0.5 | 0.872 | 1,412 inst. | green — and insufficient |
| Worst powered slice (session s09) | recall 0.71 | 142 | the real headline |
| Deployed operating point (mould) | recall 0.993 / FP-img 0.041 | — | meets line spec |
| v2 delta (insect_damage AP) | +0.089, CI [+0.061, +0.114] | 640→1,320 | real improvement |
| Error mass leader | misclassification 41% | — | route to M5 spec fix |

## Required Visuals and Training Assets

### Diagrams
1. **The matching procedure** — *Purpose:* anchor image. *Elements:* one frame with 4 GT and 6 predictions; confidence-ordered arrows attempting matches; TP/FP/FN verdicts stamped; the "confident sloppy box steals the GT" case highlighted. *Style:* step-numbered storyboard, course palette, English labels with Arabic subtitles.
2. **PR curve to AP** — *Elements:* sawtooth PR curve built point-by-point as confidence descends; interpolated envelope shaded; the deployed operating point pinned as a dot with its (precision, recall) coordinates. *Style:* three-stage build, animatable as slides.
3. **The aggregate iceberg** — *Elements:* headline mAP above the waterline; below it, per-class, per-session, per-size slice rows with s09 in red; caption "the mean launders the worst slice". *Style:* iceberg cutaway — the module's poster.
4. **Error-taxonomy flow** — *Elements:* every non-TP event routed through the five-bucket decision tree (IoU and class tests at the branches), each leaf annotated with its typical fix and owning module (M3/M5/M7). *Style:* compact flowchart, printable A4.

### Images (screenshots)
1. **Harness HTML report** — *why:* expected-state reference; *content:* metrics header, slice table with greyed under-powered rows, s09 in red.
2. **Error gallery page** — *why:* the artefact stakeholders actually read; *content:* worst-8 misclassification frames, GT green vs prediction red, confidences printed.
3. **Regression diff output** — *why:* Hour-5 reference; *content:* v1→v2 per-slice deltas with the REGRESSION lines absent and the insect_damage gain highlighted.
4. **Unit-test run** — *why:* task 1 reference; *content:* 12 matching/AP tests passing with the three named edge cases visible.

### Simulations
1. **Planted slice failure** — *Setup:* session s09 (evening captures) engineered to 0.71 recall while aggregates stay green. *Expected behaviour:* invisible in mAP, obvious in the slice report. *Learning objective:* worst-powered-slice is the headline.
2. **Threshold-mismatch report** — *Setup:* branch `sim-threshold-report` (metrics at conf=0.001, deployment at 0.35). *Expected behaviour:* 0.31 precision gap between report and field. *Learning objective:* the deployed operating point is a first-class report row.

### Interactive Activities
- **mAP by hand (15 min):** pairs receive 10 predictions + 6 GT boxes on paper with confidences and IoUs pre-computed; they execute matching, build the PR table, and compute AP@0.5 by hand; answers reconciled against the code — disagreements are always the matching order.
- **Acceptance-clause rewrite (10 min):** pairs get the traffic case's original contract line ("mAP ≥ 0.88 quarterly") and rewrite it in ≤ 4 sentences using slices, floors, n, custody, and regression mode; best rewrite is adopted as the class's reference clause.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Cached predictions (M3 detector, frozen test) | Generated by course team | parquet | 1,412 instances | Harness work without GPU |
| Matching unit-test fixtures | Course team | JSON | 12 cases | Task 1 |
| Paper mAP exercise pack | Course handout | PDF | 1 page/pair | By-hand activity |
| Traffic case pack | Course team | MD + CSV | slice tables, n counts | Case study |

### Demo Requirements
- **Instructor demo:** run the harness live; scroll past the green aggregate to the red s09 row in silence, then ask the room what they would have shipped; end with the error gallery for the misclassification bucket.
- **Student demo:** one pair presents their remediation plan; one pair presents their acceptance-clause rewrite.
- **Expected outputs:** every pair has a validated harness, a slice report naming s09, an error-analysis report with ranked plan, and (after Hour 5) the v1-vs-v2 regression summary — the complete Day 3 deliverable.

---

# Module 7 — Deployment and Edge Optimisation

## Module Overview

**Purpose.** A model that lives in a notebook inspects nothing. This module carries the Tamr Vision models across the last mile: exporting from PyTorch to ONNX with verified numerical parity, optimising for the target (quantisation, input-size engineering, execution providers), benchmarking honestly (percentiles, warm-up, end-to-end budgets), and assembling the edge inference pipeline that runs over the conveyor. The M1 preprocessing contract completes its journey here: the same `transforms.py` semantics, now reimplemented and *tested for equivalence* in the deployment wrapper.

**Business relevance.** Cloud-versus-edge is an economics and sovereignty decision before it is a technical one. Streaming 30 FPS of 1280×1024 video to a cloud endpoint costs more in bandwidth than the edge box costs in capex; round-trip latency breaks actuation deadlines (the eject gate fires 380 ms after the camera sees the fruit); and many Saudi deployments — government sites, industrial plants, anything under data-residency expectations — simply cannot ship frames off-premises. The engineering counterpart: an INT8-quantised model at 416² on a 900-riyal edge board frequently replaces a cloud GPU subscription, *if* someone does the trade-off work this module teaches. The failure mode it prevents is the most common one in regional pilots: a model that demos at 31 FPS on the data scientist's RTX card and delivers 4 FPS on the plant's actual hardware.

**Industry use cases.**
- Tamr Vision's edge box: classifier + detector exported to ONNX, INT8-quantised, running under ONNX Runtime on an industrial PC over the conveyor — 62 FPS detection at 416², decision-to-actuation inside the 380 ms gate budget, no frame ever leaving the plant.
- An industrial-city gate ANPR system where the 200 ms barrier-open budget forced edge inference; the cloud is used only for the plate-number lookup, not the vision.
- A retail chain's shelf-monitoring cameras running quantised detectors on in-store boxes, syncing only structured detections (not video) to the cloud — a bandwidth bill cut 40× and a PDPL posture the DPO signed without a meeting.

**Expected competencies.** After this module a participant can export classification and detection models to ONNX with parity tests; apply dynamic and static INT8 quantisation with a calibration set and quantify the accuracy cost; choose input size, batch, and execution provider against a written latency budget; benchmark with warm-up, percentiles, and end-to-end (capture→decision) measurement; and assemble a monitored edge inference loop with the fallback behaviours a production line requires.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Export PyTorch and Ultralytics models to ONNX and verify numerical parity | LO6 |
| 7.2 | Apply post-training quantisation (dynamic, static INT8) and measure the accuracy/latency trade | LO6, LO5 |
| 7.3 | Engineer input size and execution-provider choices against a written latency budget | LO6, LO2 |
| 7.4 | Benchmark inference honestly: warm-up, percentiles, end-to-end pipeline measurement | LO6, LO5 |
| 7.5 | Design the edge inference loop: preprocessing parity, fallbacks, monitoring hooks | LO6, LO1 |

## Technical Content

### 1. Choosing the target: cloud, edge, or both

The decision is a table, not a preference:

| Factor | Cloud GPU endpoint | Edge box on the line |
|---|---|---|
| Latency | network RTT (60–150 ms regional) + queue | local, deterministic (< 20 ms) |
| Bandwidth | full video stream up — expensive | structured events only |
| Data residency / PDPL | frames leave premises — review needed | frames stay on site |
| Scaling | elastic, per-request cost forever | capex once per line, fixed |
| Model updates | trivial (redeploy endpoint) | fleet update mechanism needed |
| Hardware | managed | yours: thermal, dust, power, physical security |

Tamr Vision's numbers make the choice: the eject gate is 1.9 m downstream of the camera at 0.3 m/s belt speed → **380 ms** total budget for capture → preprocess → detect → decide → actuate; regional cloud RTT alone eats a third of it with no jitter allowance. Edge wins; the cloud's role becomes fleet telemetry, retraining, and the M5 data flywheel. The hybrid pattern (edge inference + cloud learning loop) is the default architecture participants should reach for — and is exactly the seam where SDA-AIE-216 picks up.

### 2. ONNX: the interchange discipline

ONNX freezes the model as a dataflow graph with a pinned **opset**, decoupling training framework from serving runtime (ONNX Runtime, TensorRT, OpenVINO). The export ritual, with the two rules that prevent 90% of incidents:

- **Rule 1 — export is a code change; parity is its test.** After export, run N validation images through PyTorch and ONNX Runtime; assert max absolute difference below tolerance (1e-4 for FP32) *and* — the stronger, cheaper test — identical downstream decisions (same grades, same detections at the operating point). Parity failures localise to: unsupported ops silently decomposed, training-mode layers exported (`model.eval()` before export — M2's lesson, again), or preprocessing drift (Rule 2).
- **Rule 2 — the preprocessing contract crosses with the model.** The ONNX graph expects exactly what `eval_tf()` produced: RGB, float32 [0,1], ImageNet-normalised, bilinear-resized. The deployment wrapper reimplements this (often in OpenCV, on a box without torchvision) and *must be equivalence-tested* against the training-side contract on real images — the M1 interpolation-skew simulation was rehearsal for precisely this moment.
- **Dynamic axes** (batch, and for detectors sometimes spatial dims) are declared at export; fixed shapes enable more aggressive runtime optimisation — on a single-camera line, fix them.
- Ultralytics wraps all of this (`model.export(format="onnx")`), including detector-specific post-processing choices: exporting with NMS inside the graph simplifies the consumer but freezes thresholds into the artefact; the course exports *without* NMS and keeps the operating point in config, where M3 established it belongs.

### 3. Making it fast: the optimisation ladder

Applied in order of effort-to-payoff:

1. **Input size** — latency scales roughly quadratically with edge length: the course detector at 640² → 416² is a 2.3× speed-up for −0.021 mAP@0.5 (and −0.06 on insect_damage — per-class, per the M4 resolution lesson; check the *slices*, not the aggregate, before accepting).
2. **Quantisation** — FP32→INT8 shrinks the model ~4× and speeds CPU inference 2–3.5×. **Dynamic** quantisation (weights INT8, activations quantised on the fly) is one line and safe for a first pass; **static** quantisation additionally pre-computes activation ranges from a **calibration set** (200–500 *representative* images — season, lighting, and defect mix matter; a calibration set of daytime frames quantises away the evening tail that s09 taught us to watch). Accuracy cost on course models: classifier −0.4 F1 points, detector −0.011 mAP@0.5 — measured, not assumed, by re-running the M6 harness on the quantised artefact. FP16 is the near-free intermediate on GPUs.
3. **Execution providers** — ONNX Runtime delegates subgraphs to the best available backend: TensorRT (NVIDIA), OpenVINO (Intel CPUs/iGPUs, common in industrial PCs), CoreML, or default CPU. One artefact, provider chosen per box — this is the practical payoff of the ONNX detour.
4. **Structural surgery** — pruning and distillation buy further multiples but cost retraining loops; taught as a map (what they are, when the ladder's earlier rungs are exhausted), not a lab.

The discipline uniting the ladder: **every rung is re-evaluated with the M6 harness before adoption.** The trade-off table (config × latency × per-class metrics) is the module's central artefact; a speed-up whose per-slice cost nobody measured is not an optimisation, it is a gamble.

### 4. Benchmarking without lying to yourself

- **Warm-up:** first inferences pay one-time costs (allocation, JIT, provider graph compilation — TensorRT can take minutes); discard ≥ 20 warm-up runs before timing.
- **Percentiles, not means:** the eject gate misses on p99, not on average. Report p50/p95/p99 over ≥ 500 timed runs; on a shared box, measure under realistic co-load.
- **End-to-end or it didn't happen:** camera capture (~12 ms), decode, preprocess (~6 ms in OpenCV at 416²), inference, post-processing/NMS (~3 ms), decision logic, actuation signal — the budget is consumed by the *pipeline*, and inference is often under half of it. The course benchmark harness times each stage separately; the classic surprise is preprocessing rivalling inference after INT8 (Amdahl's law, live).
- **Throughput ≠ latency:** batching raises FPS and worsens per-frame latency; a real-time line wants batch=1 latency, an overnight archive job wants max-batch throughput — same model, opposite configurations, both in the table.
- **Thermals:** industrial boxes in Gulf ambient temperatures throttle; a 10-minute sustained-load run belongs in acceptance testing (the benchmark that passes in the air-conditioned lab and fails above the conveyor in August is a course legend for a reason).

### 5. The edge inference loop as production software

The deployed artefact is a *service* (SDA-AIE-113 practices, on a box):

- **Pipeline shape:** capture thread → ring buffer (drop-oldest under pressure: stale frames are worthless on a moving belt) → preprocess → infer → decide → actuate; structured JSON log per decision (frame id, per-class scores at the raw level, decision, stage latencies, model + dataset + config versions).
- **Fallback ladder, agreed with the plant before go-live:** model unhealthy → line keeps moving + operator alert + frames spooled for later scoring? or line stops? (A food-safety judgement, not an engineering one — the engineer's job is to force the conversation and implement the answer.) Watchdog on inference latency and on input-statistics fingerprints (the M1 drift hook, now armed).
- **Update mechanism:** models arrive as versioned bundles (ONNX + config + contract version + harness report); staged rollout (shadow mode → one line → fleet); rollback is a config flip, not an SSH session. M8 turns this paragraph into a lab; SDA-AIE-216 turns it into a fleet-wide practice.
- **Security & residency:** the box holds no raw-frame retention beyond a bounded incident buffer; telemetry is structured events; physical ports locked down — the checklist item auditors ask about first in regulated plants.

### 6. Common mistakes & production considerations

1. Exporting without parity tests — the silently-decomposed op that costs 2 mAP points and three days of confusion; parity is a unit test, run in CI on every export.
2. Reimplementing preprocessing in the wrapper "from memory" — interpolation/normalisation drift; equivalence-test the deployment preprocessing against `eval_tf()` on 50 real images (max pixel-path divergence < 1e-3).
3. Calibrating static quantisation on unrepresentative frames — daytime calibration, evening collapse; the calibration set is sampled with the same slice-awareness as the test set.
4. Benchmarking the model instead of the pipeline — 9 ms inference inside a 70 ms pipeline; time every stage.
5. Baking NMS thresholds into the exported graph — the operating point becomes un-tunable without re-export; keep it in config.
6. No thermal soak test — Gulf-summer throttling discovered in production; sustained-load benchmarking is part of acceptance.

Production: fleet telemetry should carry stage latencies and input fingerprints per box so drift and degradation are visible centrally; keep the previous model bundle on-box for instant rollback; and the harness report shipped *inside* the model bundle is what makes a field engineer's "which model is this box running and how good is it?" answerable in one command — the operational hygiene SDA-AIE-216 builds monitoring upon.

## Code Examples

### Export with parity verification

```python
# scripts/export_onnx.py
"""Export the grade classifier to ONNX; parity-test against PyTorch.
Export without a passing parity test is not an export."""
import numpy as np
import onnxruntime as ort
import torch

from tamr_vision.data.transforms import eval_tf
from tamr_vision.models.classifier import build_model

ckpt = torch.load("runs/grade_resnet50/best.pt", map_location="cpu")
model = build_model(pretrained=False)
model.load_state_dict(ckpt["state_dict"])
model.eval()                                        # export in eval mode. Always.

dummy = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy, "dist/grade_resnet50.onnx",
                  opset_version=17,
                  input_names=["image"], output_names=["logits"],
                  dynamic_axes=None)                # single-camera line: fix shapes

# ---- parity test on REAL validation images, not random tensors ----
sess = ort.InferenceSession("dist/grade_resnet50.onnx",
                            providers=["CPUExecutionProvider"])
tf = eval_tf()
max_diff, decision_flips = 0.0, 0
for img, _ in parity_sample(n=100):                 # provided iterator, val images
    x = tf(img).unsqueeze(0)
    with torch.no_grad():
        ref = model(x).numpy()
    out = sess.run(None, {"image": x.numpy()})[0]
    max_diff = max(max_diff, float(np.abs(ref - out).max()))
    decision_flips += int(ref.argmax() != out.argmax())
assert max_diff < 1e-4 and decision_flips == 0, (max_diff, decision_flips)
print(f"parity OK: max|Δlogit|={max_diff:.2e}, decision flips=0/100")
```

```python
# scripts/export_detector.py
"""Ultralytics export: NMS stays OUTSIDE the graph — the operating point
lives in config (M3), not baked into the artefact."""
from ultralytics import YOLO

model = YOLO("runs/detect/defect_y11s/weights/best.pt")
model.export(format="onnx", imgsz=416, opset=17, nms=False, dynamic=False)
# parity: run model.val() vs the ONNX path via the M6 harness — decisions,
# not just tensors, must match at the deployed operating point.
```

### Static INT8 quantisation with a representative calibration set

```python
# scripts/quantize_int8.py
"""Post-training static quantisation. The calibration set is sampled
slice-aware (sessions, lighting) — remember s09."""
import numpy as np
from onnxruntime.quantization import CalibrationDataReader, QuantType, quantize_static

from tamr_vision.data.transforms import eval_tf


class CalibReader(CalibrationDataReader):
    def __init__(self, files):                      # 300 frames, stratified by
        self.batches = iter(                        # session + time bucket
            [{"image": eval_tf()(load_rgb(f)).unsqueeze(0).numpy()} for f in files])

    def get_next(self):
        return next(self.batches, None)


quantize_static(
    model_input="dist/grade_resnet50.onnx",
    model_output="dist/grade_resnet50.int8.onnx",
    calibration_data_reader=CalibReader(stratified_calibration_files(n=300)),
    weight_type=QuantType.QInt8,
    activation_type=QuantType.QInt8,
)
# Then: re-run the M6 harness on the INT8 artefact. The accuracy cost is
# a measured row in the trade-off table, never an assumption.
```

### The honest benchmark

```python
# scripts/bench.py
"""Stage-by-stage latency: preprocess / inference / postprocess.
Warm-up, then p50/p95/p99 over 500 runs. Means are for brochures."""
import time

import numpy as np
import onnxruntime as ort

from tamr_vision.deploy.preprocess import preprocess_cv2   # equivalence-tested vs eval_tf

sess = ort.InferenceSession("dist/defect_y11s.int8.onnx",
                            providers=["OpenVINOExecutionProvider",
                                       "CPUExecutionProvider"])
frames = load_bench_frames(n=50)                    # real captures, cycled

for _ in range(20):                                 # warm-up: JIT, allocs, provider
    sess.run(None, {"images": preprocess_cv2(frames[0])})

stages = {"pre": [], "infer": [], "post": []}
for i in range(500):
    f = frames[i % len(frames)]
    t0 = time.perf_counter()
    x = preprocess_cv2(f)
    t1 = time.perf_counter()
    raw = sess.run(None, {"images": x})
    t2 = time.perf_counter()
    dets = decode_and_nms(raw, op_config)           # NMS in code, not in graph
    t3 = time.perf_counter()
    stages["pre"].append(t1 - t0); stages["infer"].append(t2 - t1)
    stages["post"].append(t3 - t2)

for k, v in stages.items():
    ms = np.array(v) * 1000
    print(f"{k:>6}: p50={np.percentile(ms, 50):5.1f}  "
          f"p95={np.percentile(ms, 95):5.1f}  p99={np.percentile(ms, 99):5.1f} ms")
total = np.array(stages["pre"]) + np.array(stages["infer"]) + np.array(stages["post"])
print(f" TOTAL: p99={np.percentile(total * 1000, 99):5.1f} ms  "
      f"(budget: 380 ms end-to-end incl. capture+actuation)")
```

### The edge inference loop (shape of the real thing)

```python
# src/tamr_vision/deploy/loop.py
"""Edge inference loop: ring buffer, watchdog, structured decision logs.
Fallback behaviour is CONFIG, agreed with the plant — never improvised."""
import json
import time
from collections import deque


def run(camera, session, op, cfg, actuator, logger):
    ring = deque(maxlen=cfg.ring_size)              # drop-oldest: stale frames
    fingerprint = InputFingerprint(window=500)      # M1 drift hook, armed
    while True:
        frame = camera.grab(timeout_ms=cfg.grab_timeout)
        if frame is None:
            logger.event("camera_timeout"); continue
        ring.append(frame)
        t0 = time.perf_counter()
        x = preprocess_cv2(ring.popleft())
        dets = decode_and_nms(session.run(None, {"images": x}), op)
        latency_ms = (time.perf_counter() - t0) * 1000
        decision = decide(dets, cfg.grading_rules)  # the 8% rule et al., versioned
        actuator.apply(decision)
        fingerprint.update(x)
        logger.decision(json.dumps({
            "frame_id": frame.id, "decision": decision.name,
            "detections": [d.compact() for d in dets],       # raw scores too (M3)
            "latency_ms": round(latency_ms, 1),
            "model": cfg.model_version, "dataset": cfg.dataset_version,
            "op": cfg.op_version, "fingerprint_drift": fingerprint.score(),
        }))
        if latency_ms > cfg.latency_alert_ms or fingerprint.score() > cfg.drift_alert:
            logger.alert("watchdog", latency_ms=latency_ms)
            if cfg.fallback == "spool":             # plant's signed-off choice
                spool_for_later(ring)
```

## Hands-on Lab 7 — Export, Optimise, Benchmark

| | |
|---|---|
| **Objective** | Export classifier and detector to ONNX with passing parity tests, quantise to INT8, and produce the accuracy/latency trade-off table that selects the line configuration |
| **Duration** | 50 minutes |
| **Setup** | `git checkout lab7-start`; onnxruntime + onnxruntime quantisation tools installed; M2/M3 checkpoints and the M6 harness present; runs on CPU by design (the edge box is a CPU) |

**Instructions & tasks**

1. *(10 min)* Export the classifier per `export_onnx.py`. The starter omits `model.eval()` — the parity test fails with decision flips; diagnose from the flip pattern (dropout randomness), fix, re-export, and record max|Δlogit| in `BENCHMARKS.md`.
2. *(8 min)* Export the detector at 416² without in-graph NMS; verify decision-level parity at the deployed operating point via the M6 harness (provided wiring).
3. *(10 min)* Quantise both models: dynamic first (one line), then static INT8 with the stratified 300-frame calibration set. Re-run the harness on each artefact; record per-class deltas — check insect_damage and session s09 specifically.
4. *(12 min)* Run `bench.py` for the four detector configs (FP32/INT8 × 640/416) — stage-by-stage percentiles into the trade-off table. Identify which stage dominates after INT8 (expected: preprocessing) and apply one mitigation (resize before normalise; measure again).
5. *(8 min)* Select the line configuration against the written budget (p99 pipeline ≤ 90 ms, leaving margin in the 380 ms end-to-end); justify in two sentences in `BENCHMARKS.md`, including the per-slice accuracy cost you are accepting.
6. *(2 min)* Commit: `feat(deploy): ONNX + INT8 artefacts, benchmarked, line config selected`.

**Expected output**
```
$ python scripts/export_onnx.py
parity OK: max|Δlogit|=3.1e-05, decision flips=0/100
$ python scripts/bench.py     # INT8 @ 416, OpenVINO EP, classroom CPU
   pre: p50=  5.8  p95=  7.1  p99=  9.4 ms
 infer: p50= 11.2  p95= 13.0  p99= 16.8 ms
  post: p50=  2.1  p95=  2.9  p99=  3.7 ms
 TOTAL: p99= 28.9 ms  (budget: 380 ms end-to-end incl. capture+actuation)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Parity decision flips, diff pattern random | Exported in train mode | `model.eval()` before export (the planted bug) |
| Parity max diff ~1e-2, systematic | Wrapper preprocessing drift (interpolation/normalise) | Equivalence-test `preprocess_cv2` vs `eval_tf()`; fix the wrapper |
| INT8 accuracy collapse on one slice | Calibration set unrepresentative | Re-stratify calibration by session/time bucket |
| First benchmark run 10× slower | No warm-up (provider graph compilation) | Discard ≥ 20 warm-up runs |
| OpenVINO EP not found | Package variant without OpenVINO | Fall back to CPUExecutionProvider; note it in the table |

**Instructor notes.** Task 1's planted train-mode export is the module's rite of passage — the flip pattern (random, not systematic) versus task 4's preprocessing drift (systematic) teaches the two diagnostic signatures side by side. Task 4's "preprocessing dominates after INT8" is the Amdahl moment; make pairs say the fraction out loud before and after mitigation. Task 5's selection must cite a *slice* cost, not just the aggregate — pairs that write "−0.011 mAP, acceptable" get the s09 question. Fast finishers: sustained-load run (10 min loop) and plot the latency drift, or export FP16 and add the row.

## Mini Exercises

**Quiz (5 questions)**
1. What two artefact-level tests must pass before an ONNX export is "done"? → tensor parity within tolerance on real images + zero decision flips at the operating point.
2. Static vs dynamic quantisation — what does static add and what does it therefore need? → pre-computed activation ranges → a representative calibration set.
3. Why report p99 rather than mean latency for the eject gate? → the gate misses on tail latency; means hide the misses.
4. Why did the course export the detector *without* in-graph NMS? → the operating point stays tunable in config (M3); re-export shouldn't be needed to retune a threshold.
5. True/False: a 2.3× inference speed-up from 640→416 yields ~2.3× pipeline speed-up. → **False** — Amdahl: capture/preprocess/post don't shrink; measure the pipeline.

**Debugging exercise.** Branch `sim-calib-day`: the INT8 detector's aggregate mAP drops only 0.013, but the M6 slice report shows session s09 recall down 0.11. Cause: the calibration set was sampled from daytime sessions only. Participants must find it via the slice report (not the aggregate), re-stratify, re-quantise, and show the recovery — M5, M6, and M7 in one loop.

**Code-review exercise.** Review a deployment PR that (a) reimplements normalisation with mean 0.5/std 0.5 "close enough", (b) benchmarks with a single timed run after no warm-up, and (c) hard-codes `conf=0.25` into the exported graph via `nms=True`. Three findings with the incident each one becomes.

**Discussion questions.**
- The integrator proposes streaming all frames to a Riyadh cloud region "for simplicity". Using the 380 ms budget and the bandwidth arithmetic, construct the rejection — then name the two workloads that *should* go to the cloud (retraining, fleet analytics).
- The plant asks what happens when the model crashes mid-shift. Walk the fallback ladder and identify which choice is engineering's and which is food-safety's.

## Case Study — ANPR at an Industrial-City Gate

**Scenario.** An industrial city operates 14 vehicle gates with automatic number-plate recognition feeding access control. The incumbent system sends every gate-camera frame to a cloud API; monthly costs are climbing with traffic, and worse, the barrier-open decision intermittently exceeds its 200 ms budget — queues form at shift change, and tailgating incidents rise when guards manually override the slow barrier.

**Business context.** The operator wants cost predictability and a hard latency guarantee; the security department wants zero degradation in plate-read accuracy (misreads create both wrongful denials and wrongful admissions); and the city's data-governance office has flagged that gate imagery — faces visible through windshields — is leaving the country via the cloud API's regional routing.

**Technical challenge.** Migrate detection + plate reading to edge boxes at each gate within the 200 ms budget, at parity accuracy, with a fleet update mechanism for 14 sites — and produce the evidence pack that convinces security to switch.

**Constraints.** Gate boxes are fanless industrial PCs (Intel CPU, no discrete GPU — OpenVINO territory); summer ambient at the gates exceeds 45 °C (thermal soak is mandatory acceptance); plates include both Saudi formats and visiting GCC formats (slice taxonomy!); the cloud API's accuracy is the incumbent baseline and its vendor will not share a test set — the operator must build its own frozen split from gate archives; night and sandstorm frames are the known hard slices.

**Solution approach (facilitate, don't lecture).** Build the referee first: a 12,000-frame frozen split from the operator's own archives, sliced by gate × time × plate format × weather, double-annotated (M5 discipline) — this neutral harness scores *both* the incumbent API and every candidate. Edge candidate: plate detector (YOLO-family, 416², INT8, OpenVINO EP) + recogniser, exported with parity tests; calibration set stratified across the declared slices — the night slice is where naive calibration fails, exactly as in `sim-calib-day`. Benchmark end-to-end at the gate (camera → barrier signal), p99 under thermal soak: the acceptance run is 30 minutes at 46 °C ambient, not a bench test in the office. Fleet mechanics: versioned model bundles, shadow mode per gate for a week (edge decisions logged, cloud still deciding), then cutover gate-by-gate with instant rollback; frames never leave the site — the governance finding resolves architecturally rather than contractually. Evidence pack for security: per-slice parity table (edge vs incumbent on the frozen split), the shadow-mode disagreement gallery, and the p99 latency traces — the M6 acceptance-clause pattern, applied.

**Discussion questions.**
1. Why must the operator's own frozen split — not the vendor's claims — referee the migration? Connect to the M6 custody discussion.
2. Design the calibration set for the INT8 recogniser. Which slices must be represented, and what goes wrong per missing slice?
3. Shadow mode doubles inference cost for a month. Argue its worth in terms of what *only* it can measure (real-traffic disagreement, tail latency under true load).
4. The cloud vendor counters with "we'll add a regional endpoint". Which of the operator's three problems does that solve, and which two remain? (latency partially; cost and residency remain — and residency only if routing is contractual.)

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Classifier parity (FP32 ONNX) | Correctness | max|Δlogit| < 1e-4, 0 decision flips /100 | `export_onnx.py` |
| Detector decision parity at operating point | Correctness | identical detections /200 frames | M6 harness on ONNX path |
| INT8 accuracy cost (detector, aggregate) | Model quality | ≥ −0.02 mAP@0.5, no slice worse than −0.03 | harness re-run |
| Pipeline p99 (INT8 @ 416, CPU) | Performance | ≤ 90 ms (pre+infer+post) | `bench.py` |
| Artefact size (detector) | Efficiency | ≤ 12 MB INT8 | filesystem |
| Trade-off table completeness | Analysis quality | 4 configs × stages × per-class deltas | `BENCHMARKS.md` review |

**Example benchmark table (filled during lab):**

| Config | mAP@0.5 | insect AP | s09 recall | infer p99 (ms) | pipeline p99 (ms) | Size |
|---|---|---|---|---|---|---|
| FP32 @ 640 | 0.903 | 0.887 | 0.84 | 74.2 | 96.1 | 38 MB |
| FP32 @ 416 | 0.882 | 0.829 | 0.82 | 33.5 | 51.0 | 38 MB |
| INT8 @ 640 | 0.895 | 0.879 | 0.83 | 31.8 | 52.7 | 10 MB |
| **INT8 @ 416 (selected)** | 0.871 | 0.821 | 0.81 | 16.8 | 28.9 | 10 MB |

## Required Visuals and Training Assets

### Diagrams
1. **The last mile** — *Purpose:* anchor image. *Elements:* training world (PyTorch, GPU, dates-qc releases) → export gate (parity tests as a checkpoint barrier) → artefact bundle (ONNX + config + contract + harness report) → edge box over the conveyor with the 380 ms budget drawn as a ruler from camera to eject gate. *Style:* left-to-right journey, course palette, English labels with Arabic subtitles.
2. **The optimisation ladder** — *Elements:* four rungs (input size, quantisation, execution provider, structural surgery) each annotated with typical gain, cost, and "re-run the harness" stamps between rungs. *Style:* ladder with effort/payoff badges, printable A4.
3. **Cloud vs edge decision table** — *Elements:* the §1 factor table rendered as a poster with the Tamr Vision numbers filled in and the hybrid pattern (edge inference + cloud learning) drawn underneath. *Style:* decision poster — the procurement-conversation artefact.
4. **End-to-end budget waterfall** — *Elements:* 380 ms bar decomposed: capture 12 → preprocess 6 → infer 17 → post 4 → decide 2 → actuate 45 → margin; a second, red bar showing the cloud path blowing the budget on RTT + jitter. *Style:* waterfall pair.

### Images (screenshots)
1. **Parity test output** — *why:* task 1 reference for both failure and success states; *content:* failing run (decision flips, random pattern) beside the passing run.
2. **Netron graph view** — *why:* participants should see inside an ONNX artefact once; *content:* the exported detector's graph with input shape and opset visible, NMS notably absent.
3. **`bench.py` output** — *why:* expected-state reference; *content:* the stage-by-stage percentile table for INT8 @ 416.
4. **Thermal-soak latency plot** — *why:* the Gulf-summer lesson; *content:* p99 trace over a 10-minute sustained run on a fanless box, throttling step visible.

### Simulations
1. **Train-mode export** — *Setup:* planted in `lab7-start` (missing `model.eval()`). *Expected behaviour:* random-pattern decision flips in parity. *Learning objective:* export is a code change with tests; flip patterns are diagnostic.
2. **Daytime calibration** — *Setup:* branch `sim-calib-day`. *Expected behaviour:* aggregate barely moves, s09 recall −0.11. *Learning objective:* calibration sets are sampled slice-aware; the harness — not the aggregate — signs off quantisation.
3. **Preprocessing drift in the wrapper** — *Setup:* branch `sim-wrapper-drift` (nearest-neighbour resize in `preprocess_cv2`). *Expected behaviour:* systematic parity diff ~1e-2, 3 decision flips /100. *Learning objective:* the contract crosses with the model; equivalence tests are mandatory (M1's arc completes).

### Interactive Activities
- **Budget negotiation (15 min):** pairs receive the waterfall with a new constraint (belt speed doubled → 190 ms budget) and must find the milliseconds: which rungs of the ladder, at what measured slice cost, and what they refuse to cut (parity tests, per-slice sign-off).
- **Config auction (10 min):** four deployment briefs (this line, the ANPR gate, drone survey batch, hospital on-prem) auctioned; pairs bid a full config (precision, size, EP, batch, fallback) and defend it against the instructor's "what breaks first?" question.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Parity sample | Frozen val subset | JPEG list | 100/200 frames | Export verification |
| Stratified calibration set | Sampled by session/time bucket | JPEG list | 300 frames | Static INT8 |
| Bench frame pack | Real captures, cycled | JPEG | 50 frames | Latency benchmarking |
| Gate/ANPR case pack | Course team | MD + CSV | slice tables, cost model | Case study |

### Demo Requirements
- **Instructor demo:** the failing parity run (train-mode export) live, then the fix; then `bench.py` on the classroom machine with the Amdahl reveal (preprocessing share before/after INT8).
- **Student demo:** one pair defends their selected line configuration citing a slice cost; one pair presents the budget-negotiation outcome.
- **Expected outputs:** every pair enters the capstone hours with parity-tested ONNX artefacts, a filled trade-off table, and a selected, justified line configuration — the deployment leg of the capstone is already done.

---

# Module 8 — Video Analytics, Object Tracking, and Production Monitoring

## Module Overview

**Purpose.** Everything so far graded *frames*. The line grades *fruit*. This module closes that gap and then keeps the closed system alive: multi-object tracking so each date is observed forty times and decided once, track-level evidence aggregation that finally satisfies the line's false-ejection budget, an inference service with real health and readiness gates in front of the M7 edge loop, safe rollout of new model bundles on a running line (shadow → canary → full), and the monitoring that catches vision drift — a new lamp, a new harvest, a dusty lens — before the night shift catches it for you. It also absorbs the catalogue's video-analytics and real-world-application topics, which the earlier modules touched only through still frames.

**Business relevance.** The arithmetic that justifies this module fits on one line. The M3 operating point was negotiated per *image*: 3 false positives per 1,000 fruit observations. A fruit crosses the field of view in 1.33 s and is therefore observed ~40 times, so a naive "any frame says reject → reject" rule gives a false-ejection rate of 1 − 0.997⁴⁰ = **11.3%** against a line budget of 0.3%. At 259,200 fruit per 8-hour shift and 8 g per fruit, the difference between 11.3% and 6.2% is 106 kg of good premium dates ejected per shift — about **SAR 2,330 a shift, SAR 1.4 m a year** across two shifts. No architecture change recovers that; object identity does. The second half of the module is the other half of the money: vision models decay quietly. A packing line changes variety three times a season, a maintenance team replaces a failed 4,100 K lamp with whatever 6,500 K unit is in the store, and a lens above a conveyor collects dust every single day. Nobody files a ticket for any of these; the reject rate simply drifts, and by the time quality control notices, a week of grading decisions is suspect.

**Industry use cases.**
- Tamr Vision on video: ByteTrack over the M7 INT8 detector at 30 FPS, one decision per physical fruit from ~40 observations, false ejections down from 11.3% to 2.4 per 1,000 and mould escapes held at 0.6% — both line constraints met simultaneously for the first time in the course.
- A beverage bottling line counting and inspecting caps, where per-frame counting double-counted bottles at lane merges until tracking made the count auditable against the filler's own counter.
- A municipal traffic programme whose detector decayed after streetlight retrofitting changed night colour temperature city-wide — caught by an image-level drift monitor nine days before the first complaint.

**Expected competencies.** After this module a participant can attach a multi-object tracker to a deployed detector and evaluate it with IDF1, MOTA, and ID-switch counts; aggregate per-track evidence into a single auditable per-fruit decision and prove it against a business budget; serve the pipeline behind liveness/readiness checks with a golden-set gate; roll a new model bundle onto a live line through shadow and canary stages with a config-flip rollback; instrument image-level, confidence-level, and outcome-level drift detectors with defensible thresholds; and operate the review queue and feedback loop that turn production frames back into the M5 flywheel.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 8.1 | Explain why per-frame decisions fail on a moving line, and quantify the multiplication of false positives over an object's lifetime | LO7, LO5 |
| 8.2 | Implement multi-object tracking (ByteTrack/BoT-SORT) and evaluate it with IDF1, MOTA, ID switches, and count accuracy | LO7, LO2 |
| 8.3 | Aggregate track-level evidence into one auditable decision per object, including best-view selection for area measurement | LO7, LO5 |
| 8.4 | Serve the tracked pipeline with liveness/readiness gates and roll bundles out safely: shadow → canary → full, rollback by config | LO8, LO6 |
| 8.5 | Instrument image-, confidence-, and outcome-level drift detectors and set thresholds from a reference window | LO8, LO3 |
| 8.6 | Operate the review queue, the labelled-feedback loop, and the night-shift runbook | LO8, LO3 |

## Technical Content

### 1. From frames to fruit: identity is a requirement, not a feature

The camera runs at 30 FPS over a 0.40 m stretch of a 0.3 m/s belt, three lanes wide, roughly 12 fruit visible per frame. Two numbers follow and both matter:

- **Line throughput** = 12 × (0.3 / 0.40) = **9 fruit/second** = 32,400 fruit/hour = 259,200 per 8-hour shift.
- **Observations per fruit** = 0.40 / 0.3 × 30 = **40 frames**.

The second number is the trap. A detector evaluated per frame at M6's operating point has a per-observation false-positive rate of about 0.003 and a per-observation mould recall of 0.993. Compound them over 40 independent-ish looks under the "any frame fires → eject" rule:

| Rule | Mould escape rate | False-ejection rate | Meets line spec (≤ 1% escape, ≤ 3 per 1,000)? |
|---|---|---|---|
| Per-frame, any-frame-fires | ~0.0% | 11.3% | No — precision collapses |
| Per-frame, last-frame-only | 0.7% | 0.3% | Marginal, and non-reproducible (which frame is "last"?) |
| Track-level, ≥ 25% of in-zone observations | 0.6% | 0.24% | **Yes** |

The third row is the module's thesis: the model did not improve, the *decision unit* changed. Note also what the per-frame rules cannot do at all — count. The plant reconciles its ejection log against its own throughput counter every shift; a system that reports 32 mould events per hour when it saw 8 mouldy fruit eight times each is not merely imprecise, it is unauditable.

Three concepts carry the rest of the module. A **track** is a sequence of detections asserted to be the same physical object. The **decision zone** is the belt region where a track is eligible to be decided — the middle 60% of the frame, because objects entering or leaving are partially visible and their masks (and therefore M4's area ratio) are wrong. A track is **closed** when it leaves the decision zone or goes unseen for `max_age` frames; closure is when the decision is emitted, logged, and — 1.9 m downstream — actuated.

### 2. Tracking mechanics: association, motion, appearance

Tracking-by-detection has three moving parts: **predict** each existing track's next position (constant-velocity Kalman filter — a conveyor is the friendliest motion model in computer vision), **associate** new detections to predicted tracks (Hungarian assignment over an IoU or appearance cost matrix), and **manage lifecycle** (confirm a track after `n_init` hits, kill after `max_age` misses). The differences between trackers are entirely in what goes into the cost matrix and what happens to unmatched low-confidence detections.

| Tracker | Association signal | Added p99 latency (12 objects/frame) | ID switches / 1,000 tracks | Choose when |
|---|---|---|---|---|
| SORT | Kalman motion + IoU | 0.6 ms | 34 | Sparse, fast, non-crossing objects; a baseline you can explain in five minutes |
| **ByteTrack** | Motion + second association pass over *low-confidence* boxes | **1.4 ms** | **6** | Dense but non-occluding scenes with brief confidence dips — the conveyor |
| BoT-SORT | Motion + camera-motion compensation + ReID embedding | 9.3 ms | 3 | Occlusion, crossing paths, a moving or vibrating camera |
| DeepSORT | Appearance embedding first, motion second | 11.5 ms | 5 | Re-identification after long gaps or across cameras |

ByteTrack's idea is worth the two minutes it takes to teach: conventional trackers discard detections below the confidence threshold, but a *momentarily occluded or motion-blurred* object usually produces a low-confidence box rather than none. ByteTrack matches high-confidence detections first, then offers the surviving unmatched tracks a second association pass against the leftovers. On the conveyor, a date passing under the lamp glare band drops to 0.19 confidence for three frames; ByteTrack keeps the identity, SORT starts a new track and the fruit is counted twice.

**Evaluating a tracker** needs its own metrics, and the class must not conflate them with detection metrics:

- **ID switches** — how often a track's identity changes hands. The count that maps directly to double-counting.
- **MOTA** — one number combining misses, false positives, and switches. Dominated by detection quality; useful for regression, poor for diagnosis.
- **IDF1** — F1 over identity assignments across the whole sequence. The honest headline for "did we track the *same thing* the whole way".
- **Count accuracy** — tracks closed in the decision zone versus the human count on the reference clip. The number the plant actually asks for.

Course reference on `line-clip-01` (90 s, 2,700 frames, 812 human-verified fruit): IDF1 0.94, MOTA 0.91, 5 ID switches, 806 counted → **99.3% count accuracy**.

**Track-level evidence aggregation** is where detection, segmentation, and tracking finally meet. For each closed track: collect per-observation class scores; apply the decision rule (≥ 25% of in-zone observations above the per-class operating point — a rule with a *tunable* threshold, swept exactly as M3 swept confidence); select the **best view** for the M4 area rule as the observation with the largest visible fruit-mask area, and take the median area ratio across the top three views, which drops area MAE from 1.5 pp to **1.1 pp** because the worst rotational occlusions are averaged out. The decision record carries the track id, the observation count, the evidence fraction, the best-view frame ids, and every model/config version — the audit trail a food-safety investigator will ask for.

### 3. Serving the line: health, readiness, and safe rollout

The M7 loop is the engine; this is the chassis. Wrap it in an HTTP service (FastAPI in the course; gRPC where the PLC vendor's SDK prefers it — the shape is identical, and on a single box the transport is the least interesting decision) and give it the two endpoints that operations teams live by:

- **Liveness (`/healthz`)** — is the process alive and is the capture thread's heartbeat fresh (< 2 s)? Failing liveness restarts the container. It must be cheap and must *not* touch the model, or a slow GPU will trigger restart loops.
- **Readiness (`/readyz`)** — is this instance allowed to actuate? Four gates, all four required: model bundle hash matches the config; preprocessing-contract version matches what the bundle declares (M1's contract, enforced at boot); execution provider initialised and warm-up complete; and the **golden set** passes — 20 frames stored on the box with expected decisions, verified in about 900 ms. Readiness fails *before* the actuator is wired, which is the entire point: a box that came up with last month's bundle and this month's contract never gets to eject anything.

**Safe rollout on a line that cannot stop.** Model updates are not deployments of code that either works or 500s; they are changes to a decision boundary, and their failure mode is silent. Three stages, each with an exit criterion agreed in advance:

1. **Shadow** (typically one week): the candidate runs on the same frames as the champion; only the champion actuates. The candidate's decisions are logged and diffed. Exit criterion: disagreement rate below the agreed ceiling *and* every disagreement gallery reviewed. This is the only stage that measures the candidate on true production distribution with true production load — the cost is one extra inference per frame (on the course box: pipeline p99 30.3 → 47.1 ms, still inside budget, which is why the headroom in M7's trade-off table was worth defending).
2. **Canary**: the candidate becomes champion on one line (or one shift) out of three. Exit criterion: reject rate, per-class mix, and throughput within control limits versus the untouched lines for 3 consecutive shifts — a *comparison*, which is why canarying one line is worth more than canarying all lines at 10% of frames.
3. **Full**: fleet-wide flip. The previous bundle stays on the box; rollback is `champion_bundle: <hash>` and a service restart — under a minute, executable by the night shift, no SSH into a Python environment at 02:00.

Where the tracker runs is a small procurement question with a clear answer, and it is worth doing on the board:

| Option | Cost (SAR) | Pipeline p99 | Verdict |
|---|---|---|---|
| Existing fanless IPC, ByteTrack on CPU | 0 — already capitalised | 30.3 ms | **Selected**: association is 1.4 ms; there was never a compute problem |
| Add a Jetson-class edge module per line, TensorRT engine, BoT-SORT + ReID | 2,600 one-off per line | 21.7 ms | Buys latency headroom the 380 ms budget does not need; accuracy delta measured at −0.004 mAP on the M6 harness (engine rebuild), ID switches 6 → 3 |
| Cloud GPU endpoint, Riyadh region | 2,850 / month / line ≈ 102,600 over 3 years | 118 ms | Fits the latency budget, fails on bandwidth (9 Mbit/s per line, continuous) and residency |

The lesson participants should take away is not "edge wins" — M7 taught that — but that once tracking is on the table people assume it needs new hardware, and 1.4 ms says otherwise. Measure before you procure.

### 4. Drift and model decay in vision

A vision model does not decay; the world in front of the lens does. Three drifts are certain on a date-packing line, and each has a different signature and a different fix:

- **Seasonal variety change.** Sukkari gives way to Khalas mid-season: colour, size, and the visual grammar of "sugaring" all shift. This is genuine covariate shift plus a mild concept shift, it is *predictable from a calendar*, and it is the one drift you should pre-empt with data (M5's flywheel, an AL round scheduled before the variety switch), not detect after the fact.
- **A changed lamp.** Maintenance replaces a failed 4,100 K lamp with a 6,500 K unit from the store at 23:40. Every frame's white balance shifts within one minute. The model's photometric augmentation (M1) absorbs some of it; `sugaring`, which is a colour judgement, absorbs none of it.
- **A dusty lens.** Continuous, monotonic, invisible day to day: contrast falls, small defects blur out first, tracks fragment because detections flicker. The clean-lens SOP exists; whether anyone follows it is what the monitor is for.

Detection is layered, cheapest first. Nothing here needs labels — which is the whole point, because production labels arrive days late if at all:

| Layer | Signal | Method | Reference / alert | Catches |
|---|---|---|---|---|
| Image | Channel means, brightness, saturation | PSI vs reference window, 1-in-30 frames, 500-frame window | PSI > 0.25 | Lamp change, exposure drift |
| Image | Colour temperature off the grey fiducial on the belt guard | White-patch estimate | 4,100 K ± 400 | Lamp change (unambiguously) |
| Image | Sharpness on a fixed ROI (belt-edge fiducial) | Variance of Laplacian | baseline 148, alert < 95 | Dusty lens, defocus, condensation |
| Feature | 256-d backbone embeddings | MMD vs frozen-split reference, PCA-16 | 3 consecutive windows > reference bootstrap p99 | Anything the pixel statistics miss — new variety, new supplier crate |
| Confidence | Fraction of detections in the 0.20–0.45 uncertain band | Rolling proportion | baseline 8.1%, alert > 12% | The model losing conviction, whatever the cause |
| Outcome | Reject rate/hour, class mix, mean fruit/frame, track-length distribution | Control limits (mean ± 3σ from 30 shifts) | reject rate 6.2% ± 1.4 pp; median track length 40 ± 6 frames | Everything, last and loudest |

Two disciplines make this work rather than merely exist. **Every alert names a suspect**: an alert that says "drift detected" trains people to mute it; an alert that says `sharpness 88 (< 95) — suspect dusty lens or condensation; runbook R-04` gets acted on at 02:00 by a technician with no ML background. And **thresholds come from a reference window, not from intuition**: the reference is 30 shifts of known-good production, the alert levels are percentiles of that reference's own variation, and the false-alarm budget is stated out loud (the course target: ≤ 1 false alert per line per week — above that, muting begins and the monitor is worse than nothing).

The loop that closes it: low-confidence detections and champion/shadow disagreements go to a **review queue** capped at 200 items per shift (roughly one hour of a QC operator's time, agreed with the plant, and the cap is what makes the queue survive contact with reality — an uncapped queue is abandoned in week two). Reviewed items become labelled data with provenance, feed the M5 release process as a targeted batch, and the retrain is refereed by the M6 harness on the *unchanged* frozen split plus the new production slice. PDPL applies with full force here: frames pulled for review may contain workers' hands and faces, so the queue stores crops where a crop suffices, applies the retention window agreed with the DPO (the course default: 30 days for reviewed items, 7 days for unreviewed), and logs every export.

### 5. Real-world walkthrough: the night the model rejected everything

Narrate this in five minutes with the runbook on screen; it is the module's memory hook.

**02:14.** The night-shift supervisor at the Al-Qassim plant sees the reject chute filling. The dashboard says reject rate 41% against a 6.2% baseline. The line is producing scrap at four times the normal rate and there is no engineer on site until 07:00.

**02:15.** The alert has already fired — twice, in fact, eleven minutes earlier: `colour_temp 6,480 K (outside 4,100 ± 400) — suspect lamp replacement; runbook R-02` and `reject_rate 39.8% (> 10.4% control limit) — runbook R-01`. Nobody was looking at the dashboard; the alerts also went to the shift phone.

**02:17.** The supervisor runs the one command the runbook gives her: `make golden`. The on-box golden set returns 6/20 — four `standard` fruit graded `reject`, all four on colour-driven classes. The system is not broken in the software sense; it is being lied to about colour.

**02:19.** R-02's decision tree asks: was maintenance on the line in the last 8 hours? The log says lamp L3 replaced at 23:40. Suspect confirmed without any ML expertise being applied.

**02:22.** R-02's remedy, in order: (1) switch the line to the plant-agreed fallback — here `spool`, meaning the line keeps moving, grading is suspended, frames are spooled to disk for later scoring, and 100% manual QC sampling starts, a food-safety decision signed off long before tonight; (2) if a matching 4,100 K lamp is in the store, fit it and re-run `make golden`; (3) if not, hold the fallback until 07:00 and escalate.

**02:41.** A matching lamp is fitted. `make golden` returns 20/20; colour temperature reads 4,180 K; the reject rate settles at 6.4% within one hour. Spooled frames from 23:40–02:41 are scored the next morning against the restored configuration, and the 3,900 fruit ejected during the incident are re-inspected as a batch rather than written off. **The following week**, the post-incident actions are all engineering and none heroic: the lamp specification becomes a procurement constraint with the part number in the maintenance SOP; the drift alert gains a page-the-shift-phone route rather than dashboard-only; 1,200 frames from the 6,500 K window go through the review queue into the next dataset release, so the model gains genuine 6,500 K robustness; and the golden set grows from 20 to 26 frames with six colour-stress cases. Note what did *not* happen: nobody retrained a model at 02:00, and nobody disabled the rejector — the two most common real-world responses, both of which turn a four-hour incident into a quality investigation spanning a fortnight.

### 6. Common mistakes & production considerations

1. Re-initialising the tracker every frame (`persist=False` in a loop) — every frame yields fresh IDs, counts explode, and because *detections* look perfect nobody suspects tracking; planted in `lab8-start`.
2. Deciding per frame and calling tracking a "nice-to-have" — the 11.3% arithmetic; the decision unit is a design choice with a price tag.
3. Deciding tracks that are still entering the frame — partial masks give wrong area ratios and premature ejections; the decision zone exists for this reason.
4. Readiness probes that return 200 as soon as the process starts — the box actuates with a mismatched bundle or contract; readiness must gate on bundle hash, contract version, warm-up, and golden set.
5. Monitoring only the model, never the outcome — the cheapest, most reliable drift detector on any line is its own reject rate against control limits; teams skip it because it feels unsophisticated.
6. Alert thresholds picked by intuition, then muted — set them from a reference window, state the false-alarm budget, name a suspect and a runbook in every alert.
7. An uncapped review queue — it is abandoned within a fortnight and the feedback loop dies with it; cap it, and let the cap force prioritisation.

Production: run the drift monitor in the same process as inference but on sampled frames (1-in-30 costs 0.10 ms per frame amortised) so it cannot be silently switched off by someone restarting only "the monitoring container"; ship the reference window inside the model bundle so thresholds travel with the model they were computed for; keep 30 shifts of decision logs on-box and stream only aggregates centrally (PDPL and bandwidth agree for once); and rehearse the runbook — an unrehearsed runbook is documentation, and documentation does not fix a line at 02:00. SDA-AIE-216 turns this section into pipelines: automated retraining triggers, drift-gated promotion, and the on-call rotation this module can only rehearse.

## Code Examples

### Tracking the fruit, not the frame

```python
# src/tamr_vision/track/tracker.py
"""Tracked inference: detections -> persistent tracks -> closed tracks.

The tracker is stateful. `persist=True` is not an optimisation, it IS the
tracker: without it every frame starts a new set of IDs and counts explode.
Tracks are decided only inside the decision zone (middle 60% of the frame),
because entering/leaving fruit have partial masks and wrong area ratios (M4).
"""
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Track:
    track_id: int
    obs: list = field(default_factory=list)     # per-observation evidence dicts
    last_seen: int = 0                          # frame index of last match
    in_zone: int = 0                            # observations inside decision zone


class LineTracker:
    def __init__(self, model, cfg):
        self.model = model                      # Ultralytics model (M7 artefact)
        self.cfg = cfg
        self.tracks: dict[int, Track] = {}
        self.closed: list[Track] = []

    def _zone(self, frame_w):                   # decision zone along the belt axis
        margin = (1.0 - self.cfg.zone_fraction) / 2
        return margin * frame_w, (1.0 - margin) * frame_w

    def step(self, frame, frame_idx):
        # persist=True keeps tracker state across calls; tracker config is a file
        # so the operating point and the association params are both versioned.
        res = self.model.track(frame, persist=True, tracker="cfg/bytetrack.yaml",
                               conf=self.cfg.conf, iou=self.cfg.nms_iou,
                               verbose=False)[0]
        lo, hi = self._zone(frame.shape[1])
        seen = set()
        for box in res.boxes:
            if box.id is None:                  # unconfirmed track: no ID yet
                continue
            tid = int(box.id.item())
            seen.add(tid)
            t = self.tracks.setdefault(tid, Track(track_id=tid))
            cx = float(box.xywh[0][0])
            inside = lo <= cx <= hi
            t.obs.append({"frame": frame_idx, "cls": int(box.cls.item()),
                          "conf": float(box.conf.item()), "in_zone": inside,
                          "mask_area": mask_area(res, box)})   # M4 masks
            t.in_zone += int(inside)
            t.last_seen = frame_idx

        # Close tracks that left the zone or went unseen for max_age frames.
        for tid, t in list(self.tracks.items()):
            aged_out = frame_idx - t.last_seen > self.cfg.max_age
            left_zone = tid not in seen and t.in_zone > 0
            if aged_out or left_zone:
                self.closed.append(self.tracks.pop(tid))
        return res
```

```python
# src/tamr_vision/track/decide.py
"""One decision per physical fruit, from ~40 observations.

Why not "any frame fires -> eject": with a per-observation false-positive rate
of 0.003 and 40 observations, P(at least one FP) = 1 - 0.997**40 = 0.113.
The line budget is 3 per 1,000. The evidence rule below measures 0.0024.
"""
import statistics

from tamr_vision.detect.infer import DEFECTS


def decide_track(track, op, rules):
    """Return a decision record for a closed track. Auditable by construction."""
    zone_obs = [o for o in track.obs if o["in_zone"]]
    if len(zone_obs) < rules.min_observations:          # too brief to judge
        return {"track_id": track.track_id, "decision": "review",
                "reason": "insufficient_observations", "n_obs": len(zone_obs)}

    # ---- evidence per defect class: fraction of in-zone observations firing ----
    evidence = {}
    for cls_idx, name in enumerate(DEFECTS):
        fired = [o for o in zone_obs
                 if o["cls"] == cls_idx and o["conf"] >= op.conf_for(name)]
        evidence[name] = len(fired) / len(zone_obs)

    # ---- best-view area rule (M4): median ratio over the 3 largest views ----
    best = sorted(zone_obs, key=lambda o: o["mask_area"]["fruit_px"],
                  reverse=True)[:3]
    area_pct = statistics.median(o["mask_area"]["defect_pct"] for o in best)

    hits = [n for n, frac in evidence.items() if frac >= rules.evidence_fraction]
    if hits or area_pct > rules.area_reject_pct:        # the 8% rule, on best views
        decision = "reject"
    elif max(evidence.values()) >= rules.review_fraction:
        decision = "review"                             # -> human queue, not the chute
    else:
        decision = "pass"

    return {"track_id": track.track_id, "decision": decision,
            "n_obs": len(zone_obs), "evidence": evidence,
            "defect_area_pct": round(area_pct, 2),
            "best_view_frames": [o["frame"] for o in best],
            "triggered": hits, "rules_version": rules.version}
```

### The inference service: liveness, readiness, and the rollout role

```python
# src/tamr_vision/serve/app.py
"""FastAPI front end for the edge loop.

Liveness answers "restart me?"; readiness answers "may I actuate?".
They are different questions and conflating them is how a box comes up with
last month's bundle and ejects good fruit for a shift.
"""
import time

from fastapi import FastAPI, Response

from tamr_vision.serve.state import STATE          # holds loop, cfg, golden results
from tamr_vision.serve.util import sha256_file     # streamed hash of the bundle

app = FastAPI(title="tamr-vision-edge", version=STATE.cfg.service_version)


@app.get("/healthz")
def healthz():
    """Cheap. Never touches the model — a slow GPU must not cause restart loops."""
    stale = time.monotonic() - STATE.capture_heartbeat
    if stale > STATE.cfg.heartbeat_timeout_s:      # capture thread wedged
        return Response(f"capture stale {stale:.1f}s", status_code=503)
    return {"status": "ok", "uptime_s": round(time.monotonic() - STATE.started, 1)}


@app.get("/readyz")
def readyz():
    """Four gates. All four, or this instance does not actuate."""
    checks = {
        "bundle_hash": sha256_file(STATE.cfg.bundle_path) == STATE.cfg.expected_hash,
        "contract_version": STATE.bundle.contract_version == STATE.cfg.contract_version,
        "provider_warm": STATE.warmup_done,        # >= 20 warm-up runs (M7)
        "golden_set": STATE.golden_passed == STATE.golden_total,
    }
    body = {"role": STATE.cfg.role, "model": STATE.bundle.model_version,
            "dataset": STATE.bundle.dataset_version, "checks": checks,
            "golden": f"{STATE.golden_passed}/{STATE.golden_total}"}
    return Response(content=str(body),
                    status_code=200 if all(checks.values()) else 503)


@app.post("/decide")
def decide(frame_ref: str):
    """Score one frame. In `shadow` role the actuator is a no-op and the
    decision is written to the diff log against the champion's."""
    record = STATE.loop.step(frame_ref)
    if STATE.cfg.role == "shadow":
        STATE.difflog.append(record)               # compared to champion offline
    else:
        STATE.actuator.apply(record["decision"])
    return record


@app.get("/metrics")
def metrics():
    """Prometheus exposition: latencies, reject rate, drift scores, queue depth."""
    return Response(STATE.registry.render(), media_type="text/plain")
```

### The drift monitor

```python
# src/tamr_vision/monitor/drift.py
"""Image-, confidence-, and outcome-level drift detection. No labels required.

Every alert names a suspect and a runbook. "Drift detected" trains people to
mute alerts; "sharpness 88 (< 95) - suspect dusty lens - runbook R-04" gets
a technician to act at 02:00 without knowing what an embedding is.
"""
import cv2
import numpy as np

# psi: Population Stability Index (> 0.25 = material shift); mmd_pca16: kernel
# two-sample distance on PCA-16 embeddings; white_patch_kelvin: colour temp
# from the grey fiducial printed on the belt guard.
from tamr_vision.monitor.stats import mmd_pca16, psi, white_patch_kelvin

REFERENCE = np.load("bundles/current/reference_window.npz")   # ships IN the bundle


class DriftMonitor:
    """Runs in-process on 1 frame in 30: 3.1 ms sampled = 0.10 ms per frame."""

    def __init__(self, cfg, window=500):
        self.cfg, self.window = cfg, window
        self.brightness, self.embeddings, self.uncertain = [], [], []

    def observe(self, frame, embedding, detections):
        self.brightness.append(float(frame.mean()))
        self.embeddings.append(embedding)                     # 256-d, backbone
        band = [d for d in detections if 0.20 <= d.conf < 0.45]
        self.uncertain.append(len(band) / max(len(detections), 1))
        if len(self.brightness) >= self.window:
            return self.evaluate(frame)
        return []

    def evaluate(self, frame):
        alerts = []
        b = psi(REFERENCE["brightness"], np.array(self.brightness))
        if b > 0.25:
            alerts.append(("brightness_psi", b, "exposure or lamp change", "R-02"))

        kelvin = white_patch_kelvin(frame, self.cfg.fiducial_roi)   # grey fiducial
        if abs(kelvin - 4100) > 400:
            alerts.append(("colour_temp", kelvin, "lamp replaced", "R-02"))

        roi = frame[self.cfg.sharpness_roi]
        sharp = float(cv2.Laplacian(cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY),
                                    cv2.CV_64F).var())
        if sharp < 95:                                          # baseline 148
            alerts.append(("sharpness", sharp, "dusty lens or condensation", "R-04"))

        d = mmd_pca16(REFERENCE["embeddings"], np.stack(self.embeddings))
        if d > REFERENCE["mmd_p99"]:                            # 3 windows required
            self.cfg.mmd_strikes += 1
            if self.cfg.mmd_strikes >= 3:
                alerts.append(("embedding_mmd", d, "new variety or supplier", "R-03"))
        else:
            self.cfg.mmd_strikes = 0

        u = float(np.mean(self.uncertain))
        if u > 0.12:                                            # baseline 0.081
            alerts.append(("uncertain_band", u, "model losing conviction", "R-01"))

        self.brightness, self.embeddings, self.uncertain = [], [], []
        return alerts
```

### Review queue and the labelled-feedback loop

```python
# src/tamr_vision/monitor/review.py
"""The human-in-the-loop queue that feeds the M5 flywheel.

Capped at 200 items/shift (~1 hour of a QC operator). An uncapped queue is
abandoned in week two, and the feedback loop dies with it. PDPL: crops where a
crop suffices; 30-day retention reviewed, 7-day unreviewed; every export logged.
"""
import json
from datetime import datetime, timedelta

PRIORITY = {"shadow_disagreement": 0, "outcome_anomaly": 1, "low_confidence": 2}


def enqueue(record, queue, cap=200):
    """Priority-ordered, capped. Cap forces prioritisation instead of despair."""
    reason = classify_reason(record)                 # None if nothing to review
    if reason is None:
        return queue
    queue.append({"track_id": record["track_id"], "reason": reason,
                  "priority": PRIORITY[reason], "decision": record["decision"],
                  "evidence": record["evidence"], "model": record["model_version"],
                  "frames": record["best_view_frames"], "captured_at": record["ts"]})
    queue.sort(key=lambda i: (i["priority"], -max(i["evidence"].values())))
    return queue[:cap]                               # lowest-value items fall off


def export_batch(queue, out_path, dpo_log):
    """Reviewed items -> a labelled batch with provenance, for the M5 release."""
    reviewed = [i for i in queue if i.get("human_label")]
    batch = {"created": datetime.utcnow().isoformat(timespec="seconds"),
             "source": "production_review_queue",
             "retention_until": (datetime.utcnow() + timedelta(days=30)).date().isoformat(),
             "items": [{"crop_ref": i["crop_ref"], "label": i["human_label"],
                        "model_said": i["decision"], "reason": i["reason"],
                        "model_version": i["model"], "spec_version": i["spec_version"]}
                       for i in reviewed]}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)
    dpo_log.write(f"{batch['created']} exported {len(reviewed)} crops -> {out_path}\n")
    # Next: this batch enters release_dataset.py (M5) as a targeted AL round,
    # and the retrain is refereed by the M6 harness on the UNCHANGED frozen split
    # plus a new `production_2026H1` slice. Never merge without both.
    return batch
```

## Hands-on Lab 8 — Track, Serve, and Watch the Line

| | |
|---|---|
| **Objective** | Turn the frame-level inspection pipeline into a fruit-level one with ByteTrack, serve it behind readiness gates, arm the drift monitor against three replayed failures, and run a shadow rollout that produces a review batch |
| **Duration** | 50 minutes |
| **Setup** | `git checkout lab8-start`; Lab 7 ONNX/INT8 artefacts present; `pip install fastapi uvicorn` (pinned in `requirements.txt`); `dates-line-video` pack extracted (`line-clip-01.mp4` + `tracks_gt.json`, three drift replay clips, `golden/` 20 frames); runs on CPU by design |

**Instructions & tasks**

1. *(8 min)* Run `python -m tamr_vision.track.tracker --clip line-clip-01.mp4`. The starter calls `model.track(..., persist=False)` — the count comes out around 24,000 against a ground truth of 812. Diagnose from the ID histogram (every ID seen exactly once), fix, re-run, and record count accuracy, IDF1, and ID switches in `BENCHMARKS.md`.
2. *(10 min)* Implement `decide_track()`'s evidence rule and best-view area selection. Sweep `evidence_fraction` ∈ {0.10, 0.25, 0.50} and record false-ejection rate and mould-escape rate for each against `tracks_gt.json`. Compare row-for-row with the any-frame rule (provided) and write the one sentence that justifies your chosen operating rule.
3. *(8 min)* Start the service (`uvicorn tamr_vision.serve.app:app`). Confirm `/readyz` returns 503 until the golden set passes; break it deliberately by pointing `contract_version` at `v1` and confirm the gate catches it. Then run the provided load script and record p99 and throughput.
4. *(10 min)* Arm `DriftMonitor` and replay the three drift clips (`drift-season.mp4`, `drift-lamp-6500k.mp4`, `drift-dusty.mp4`). For each, record which detectors fire, in what order, and how many frames elapse before the first alert. One clip fires only the outcome-level detector — identify it and explain why the image-level ones stay silent.
5. *(10 min)* Run shadow mode: champion = your INT8 @ 416 bundle, candidate = the provided `v2.1-candidate` bundle. Produce the disagreement gallery, route low-confidence tracks and disagreements into the review queue, label 10 items from the gallery, and export the feedback batch. State the promote/hold decision in one sentence with the number that supports it.
6. *(4 min)* Commit: `feat(monitor): track-level decisions, readiness gates, drift watch, shadow rollout`.

**Expected output**
```
$ python -m tamr_vision.track.tracker --clip line-clip-01.mp4
tracks closed in zone: 806   gt: 812   count accuracy: 99.3%
IDF1: 0.94   MOTA: 0.91   ID switches: 5   median track length: 40 frames
$ python -m tamr_vision.track.decide --rule evidence --fraction 0.25
false ejections: 2.4 / 1000   (any-frame rule: 113.0 / 1000)
mould escapes:   0.6 %        (line spec: <= 1.0 %)   area MAE: 1.1 pp
$ curl -s localhost:8000/readyz | head -1
503  golden_set 6/20  contract_version False   -> instance will not actuate
$ python -m tamr_vision.monitor.drift --replay drift-lamp-6500k.mp4
[frame 1500] colour_temp 6483 K (4100 +/- 400) suspect=lamp replaced runbook=R-02
[frame 1500] brightness_psi 0.41 (> 0.25)      suspect=exposure or lamp change R-02
[frame 4380] reject_rate 0.392 (> 0.104 UCL)   suspect=see image alerts   R-01
```

**Acceptance criteria**
- Count accuracy ≥ 98% and ID switches ≤ 10 per 1,000 tracks on `line-clip-01`, with IDF1 recorded.
- A track-level rule that meets *both* line constraints (≤ 3 false ejections per 1,000 and ≤ 1% mould escape), with the sweep table that chose it in `BENCHMARKS.md`.
- `/readyz` demonstrably fails on a bundle-hash, contract-version, or golden-set violation and passes when all four gates are green.
- All three drift clips detected, each with the firing detector, its latency in frames, and a named suspect; plus a shadow-mode promote/hold decision backed by a disagreement number and an exported feedback batch.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Track count in the tens of thousands | `persist=False` — tracker state discarded each frame (the planted bug) | `persist=True` and keep one model instance for the whole clip |
| Counts ~15% high, IDs otherwise sane | Tracks closed outside the decision zone; entering/leaving fruit counted twice | Apply the zone rule; only close on zone exit or `max_age` |
| Every track decided "review" | `min_observations` above the real track length (video decoded at 15 FPS) | Check the clip's FPS; observations per fruit scale with it |
| `/readyz` always 200 | Readiness returning process state, not the four gates | Gate on bundle hash, contract version, warm-up, golden set |
| Drift monitor never fires on the season clip | Window not filled (500 frames) or MMD strike counter reset each window | Check window arithmetic; the MMD rule needs 3 *consecutive* windows |

**Instructor notes.** Task 1 is the single most valuable ten seconds in the module: project the count `24,180` next to the ground truth `812` and let the room sit with it, because the *detections* are perfect and everything the class has learned so far says the model is fine. Task 2 is where the course's line spec is finally met — write the any-frame rule's 113/1,000 on the board next to the evidence rule's 2.4/1,000 and ask which model change would have achieved that (none). In task 4 the season clip is the quiet one: pixel statistics barely move because a new variety is a *content* change, not a lighting change, so the embedding and outcome layers carry it — this is the argument for layered monitoring, and pairs should say it out loud. Walk the room during task 5 and check who promotes on aggregate agreement alone without opening the gallery; that instinct is what shadow mode exists to correct. Fast finishers: add a `max_age` sweep and plot ID switches against fragmentation, or implement the control-limit calculation from the 30-shift reference and compare their limits to the shipped ones.

## Mini Exercises

**Quiz (5 questions)**
1. A fruit is observed 40 times and the per-observation false-positive rate is 0.003. What is the false-ejection rate under an "any frame fires" rule? → 1 − 0.997⁴⁰ ≈ 11.3% — 38× the line budget.
2. What does ByteTrack do that SORT does not, and which line phenomenon does it fix? → a second association pass over low-confidence detections; fruit passing through the lamp glare band keep their identity instead of being counted twice.
3. Liveness vs readiness — which one gates actuation, and what are its four checks here? → readiness; bundle hash, contract version, provider warm-up, golden set.
4. Name a drift a pixel-statistics monitor cannot see, and the layer that catches it. → a new date variety (content, not lighting) — caught by embedding MMD and by the outcome-level reject rate.
5. True/False: the correct night-shift response to a 41% reject rate is to retrain the model. → **False** — switch to the agreed fallback, run the golden set, follow the runbook to a suspect; retraining at 02:00 is how an incident becomes an investigation.

**Debugging exercise.** Branch `sim-zone-off`: the decision zone is set to 100% of the frame. Aggregate metrics look *better* (more observations per track), but the area MAE rises to 2.6 pp and false ejections triple. Participants must connect the two — partially visible fruit produce partial masks, so the M4 area ratio is computed against a truncated denominator — and recover by restoring the zone. The discussion it opens: which other course metric silently assumes a fully visible object?

**Design exercise.** The plant adds a second camera 4 m downstream to catch defects on the underside after a flip bar. Design the identity strategy: is this a re-identification problem (appearance embeddings, BoT-SORT/DeepSORT territory), a timing problem (belt speed × distance gives an arrival window), or both? Specify what you would log to make the join auditable, and what you would do when the two cameras disagree on the same fruit.

**Discussion questions.**
- Shadow mode doubles inference cost for a week and the plant manager asks why the candidate cannot just be switched on for a shift and watched. Argue both sides honestly — then name the one thing only shadow mode gives you (the same frames scored by both models, so the disagreement is attributable to the model and not to the day).
- Who owns the drift alert thresholds: the vision engineer who computed them, the quality department that lives with the false alarms, or plant operations who get paged at 02:00? Defend your answer in terms of where the false-alarm budget is spent.

## Case Study — Bottle Counting and Model Decay at "Salsabeel" (سلسبيل)

**Scenario.** Salsabeel bottles drinking water at a Jeddah plant on four lines running 24/6. A vision system inspects cap seating and fill level and counts output for reconciliation against the filler's mechanical counter. It has run for fourteen months. Over the last quarter the daily reconciliation gap has grown from ±0.2% to −3.1% — the vision count is now materially below the mechanical counter — and the cap-defect rate reported by the system has halved, which finance likes and the quality manager does not believe.

**Business context.** The vision count feeds production reporting and the shift bonus calculation, so a systematic undercount is not an engineering curiosity, it is a payroll dispute. Meanwhile a halved defect rate either means the capper was overhauled (it was not) or the model has stopped seeing defects. Salsabeel's contract with its retail customers carries a cap-integrity clause; a missed defect batch is a recall conversation. There is no ML engineer on site, and the vendor that installed the system 14 months ago no longer answers quickly.

**Technical challenge.** Establish, without labelled production data and without stopping the lines, whether the system is undercounting, under-detecting, or both; localise the cause; and put in place monitoring that would have caught it in week one instead of quarter three.

**Constraints.** No labelled data since commissioning. The lines cannot stop for more than the 20-minute changeover window. The four lines are nominally identical, which is the single most useful fact available. Bottles are transparent and touching at the merge point, so occlusion is constant. The plant's cameras record only aggregate counts centrally — raw frames are retained on-box for 48 hours only, which is both a PDPL-friendly design and an evidence problem. The original vendor's model bundle has no reference window and no golden set.

**Solution approach (facilitate, don't lecture).** Start with the free comparison: four nominally identical lines are each other's control. Plot reject rate, count-per-shift, and mean detection confidence per line over the quarter; if all four drifted together, suspect a shared cause (a product change — and indeed the preform supplier changed in month eleven, giving a slightly bluer bottle tint); if one line drifted, suspect that line's hardware. At Salsabeel three lines drifted mildly and line 2 drifted hard, which says *both* causes are present and separable. Next, reconstruct a reference: pull 48 hours of frames now, plus the commissioning acceptance set the vendor left behind, and compute the image statistics, sharpness, and embedding distributions for each — line 2's sharpness ROI reads 61 against the other lines' 130–150, and a maintenance photograph shows the lens housing gasket has perished, letting in a fine mist of condensation. Then attack the count: instrument track lengths and ID switches at the merge point and discover that touching transparent bottles at reduced contrast fragment into multiple short tracks that are then discarded by the minimum-observation rule — a *silent* undercount that grows exactly as contrast falls. The remedy is layered and unglamorous: replace the gasket and clean the optics (line 2's count gap closes to −0.4% overnight); retune the tracker for occlusion (BoT-SORT with appearance, since transparent touching bottles are precisely the case motion-only association loses); add the preform-tint frames to a targeted labelled batch through a review queue; and — the part that matters for the next fourteen months — ship a reference window, a golden set per line, control limits computed from 30 known-good shifts, and a monitor whose first alert would have fired in week two of the quarter with the suspect named. The vendor question resolves itself: the acceptance contract for the next system requires the reference window, the golden set, and the harness, handed over as artefacts.

**Discussion questions.**
1. Salsabeel had four lines and used none of them as a control for fourteen months. What does a fleet of nominally identical deployments give you for free, and what must be true about their configuration for the comparison to be valid?
2. The undercount was invisible because the failing signal was *inside* the tracker (fragmented tracks discarded by a minimum-observation rule), not in the detector. Which monitor from this module's layered table catches it, and why do the image-level detectors alone leave you blind here?
3. Argue the case for spending a 20-minute changeover window on a golden-set capture per line at commissioning, to a plant manager who measures everything in bottles per hour.
4. The defect rate halved and finance was pleased. Design one control that makes a *falling* defect rate as alarming as a rising one, and decide who receives it.

## Benchmarks and Evaluation

| Metric | Category | Target after M8 | How measured |
|---|---|---|---|
| Count accuracy on `line-clip-01` | Correctness | ≥ 98% vs 812 human-verified fruit | `tracker.py --clip` |
| Identity quality | Model quality | IDF1 ≥ 0.90, ID switches ≤ 10 / 1,000 tracks | `tracker.py` metrics block |
| Track-level false-ejection rate | Business outcome | ≤ 3 per 1,000 fruit | `decide.py` vs `tracks_gt.json` |
| Track-level mould escape rate | Business outcome | ≤ 1.0% | `decide.py` vs `tracks_gt.json` |
| Added pipeline latency (tracking + monitor) | Performance | ≤ 2.5 ms p99; pipeline p99 ≤ 35 ms | `bench.py` (M7 harness, tracking enabled) |
| Drift detection coverage | Reliability | 3/3 replay clips detected, each with a named suspect | `drift.py --replay` |
| Rollout evidence | Process quality | disagreement gallery + promote/hold decision with a number | `BENCHMARKS.md` |

**Example benchmark table (filled during lab):**

| Decision rule | False ejections / 1,000 | Mould escapes | Area MAE | Verdict |
|---|---|---|---|---|
| Per-frame, any-frame-fires | 113.0 | 0.0% | 1.5 pp | Unusable — 38× the budget |
| Track-level, evidence ≥ 0.10 | 8.7 | 0.2% | 1.1 pp | Still over budget |
| **Track-level, evidence ≥ 0.25 (selected)** | **2.4** | **0.6%** | **1.1 pp** | Meets both line constraints |
| Track-level, evidence ≥ 0.50 | 0.9 | 1.9% | 1.1 pp | Escape budget breached — precision bought with food safety |

## Required Visuals and Training Assets

### Diagrams
1. **Forty looks, one decision** — *Purpose:* anchor image. *Elements:* a filmstrip of one date crossing the frame over 40 frames, per-frame confidences plotted underneath with two spurious spikes, the decision zone shaded, and a single decision record emitted at zone exit; the 11.3% vs 0.24% figures called out on the two candidate rules. *Style:* filmstrip over a timeline, course palette, English labels with Arabic subtitles.
2. **Tracking-by-detection loop** — *Elements:* predict (Kalman) → associate (cost matrix, Hungarian) → lifecycle (confirm/age-out), with ByteTrack's second low-confidence association pass drawn as the extra branch and an occluded fruit travelling through it. *Style:* cycle diagram with one worked frame pair, printable A4.
3. **The monitoring stack** — *Elements:* the six-layer table rendered vertically (image → feature → confidence → outcome), each layer showing what it catches, its latency to detect, and its cost; the three certain drifts (season, lamp, dust) drawn as arrows entering at the layer that catches them first. *Style:* layered poster — the artefact that goes on the plant wall.
4. **Rollout ladder** — *Elements:* shadow → canary → full with exit criteria on each rung, the rollback path drawn as a single config flip back to the retained previous bundle, and the readiness gate drawn as a barrier before the actuator on every rung. *Style:* ladder with gates, matching the M7 optimisation-ladder poster visually.

### Images (screenshots)
1. **The count explosion** — *why:* task 1 reference for the planted bug; *content:* terminal showing 24,180 tracks against 812 ground truth beside the fixed run's 806, with the ID histogram alongside.
2. **Disagreement gallery** — *why:* the artefact shadow mode exists to produce; *content:* six frames where champion and candidate differ, decisions and confidences overlaid, one obvious candidate improvement and one obvious regression visible.
3. **Drift dashboard during the lamp incident** — *why:* the walkthrough made concrete; *content:* colour temperature, brightness PSI, and reject-rate panels over the 23:00–03:00 window with the alert markers and the recovery step.
4. **`/readyz` failing and passing** — *why:* the readiness gate is abstract until seen; *content:* two curl outputs side by side, `golden_set 6/20` versus all four checks green.

### Simulations
1. **Tracker amnesia** — *Setup:* planted in `lab8-start` (`persist=False`). *Expected behaviour:* ~24,000 tracks, every ID seen once, detections perfect. *Learning objective:* tracking state is the tracker; detection metrics cannot see a tracking failure.
2. **The 6,500 K lamp** — *Setup:* branch/clip `drift-lamp-6500k`. *Expected behaviour:* colour-temperature and brightness-PSI alerts within one window, reject rate breaching its control limit ~48 s later. *Learning objective:* image-level monitors buy you the minutes before the outcome-level one shouts.
3. **New harvest, same lamp** — *Setup:* clip `drift-season`. *Expected behaviour:* pixel statistics quiet, embedding MMD trips after 3 windows, reject-rate drift mild but persistent. *Learning objective:* content drift is invisible to pixel statistics; layers are not redundancy, they are coverage.
4. **Dust accumulation** — *Setup:* clip `drift-dusty` (progressive blur). *Expected behaviour:* sharpness falls below 95, tracks fragment, median track length drops 40 → 31. *Learning objective:* one physical cause shows up in three unrelated-looking metrics; correlated alerts are a diagnosis, not noise.

### Interactive Activities
- **Runbook rehearsal (15 min):** in threes — supervisor, technician, instructor as the line. The instructor reads out symptoms from a sealed card (one of: dusty lens, wrong lamp, stale bundle after a power cut, genuinely bad batch of fruit); the team must reach the right action using only the runbook and `make golden`, out loud, in under five minutes. Score on whether the fallback was invoked before the diagnosis, which is the correct order.
- **Alert budget auction (10 min):** pairs receive the six monitoring layers with their measured false-alarm rates and a budget of one alert per line per week. They must buy a monitoring set, defend what they left uncovered, and answer "which drift are you now blind to, and how long until the outcome layer tells you?"

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `line-clip-01` + `tracks_gt.json` | Course team: staged line capture, auto-tracked then human-verified | MP4 30 FPS + JSON | 90 s, 2,700 frames, 812 fruit tracks | Tracking, counting, decision-rule sweep |
| Drift replay pack | Course team: `drift-season`, `drift-lamp-6500k`, `drift-dusty` | MP4 | 3 × 60 s | Drift-monitor arming and comparison |
| Reference window | Computed from 30 known-good shifts | NPZ (ships inside the bundle) | ~4 MB | Drift thresholds and control limits |
| Golden set | Course team, expected decisions frozen | JPEG + JSON | 20 frames | Readiness gate, `make golden` |
| `v2.1-candidate` bundle | Course team (trained on a later release) | ONNX + config | 10 MB | Shadow-mode comparison |
| Salsabeel case pack | Course team | MD + CSV | 4 lines × 90 shifts of counts, rates, confidences | Case study |

### Demo Requirements
- **Instructor demo:** run the broken tracker live and project `24,180` beside `812`; fix it in one keyword and re-run. Then replay the lamp clip with the dashboard on screen and let the class watch the image-level alert fire 48 seconds before the reject rate does.
- **Student demo:** one pair defends their evidence-fraction choice using their own sweep table; one pair presents the runbook rehearsal outcome, specifically whether they invoked the fallback before diagnosing.
- **Expected outputs:** every pair enters the capstone hours with a tracked pipeline meeting both line constraints, a service that refuses to actuate when it should, an armed drift monitor with named suspects, and one exported feedback batch — the monitoring leg of the capstone is already done.

---

# Final Capstone Project

## Title: Tamr Vision — A Complete Edge Inspection System for the Date-Packing Line

## Project Scenario

You are the vision engineer for **"Tamr Vision" (رؤية تمر)**, the quality-inspection system of a date-packing plant in Al-Qassim. Over five days you have built every component: the input pipeline and augmentation policy (M1), the fine-tuned grade classifier (M2), the defect detector with its negotiated operating point (M3), the surface-defect segmenter and area measurement (M4), the curated v2 dataset (M5), the evaluation harness that referees everything (M6), the exported, quantised, benchmarked edge artefacts (M7), and the tracked, served, monitored line system (M8). The capstone is the integration plus your own engineering judgement: one system that watches the conveyor, decides each physical fruit once against the plant's rules, proves its own quality with a harness report, and tells you when it has started to drift. This is the vision-system project named in the course assessment — it absorbs the "vision application project" topic as the course's final integrated build.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Input pipeline and contract (LO1, LO3):** the versioned preprocessing contract used identically by training, harness, and the deployment wrapper, with the equivalence test passing; augmentation policy documented with per-transform justification.
2. **Classification (LO1, LO4):** staged fine-tuned classifier (v2 data) with macro-F1 ≥ 0.90 and reject recall ≥ 0.95 on the frozen test split; checkpoint embeds class order, contract reference, and metrics.
3. **Detection (LO2, LO4, LO5):** detector at mAP@0.5 ≥ 0.88 (v2), with a documented per-class operating point derived from the line spec and the feasibility analysis for any class that cannot meet it.
4. **Segmentation and measurement (LO2, LO5):** segmenter at mask mAP@0.5 ≥ 0.80; per-fruit defect-area report with MAE ≤ 1.5 pp and the grading-disagreement rate against the 8% rule reported.
5. **Dataset curation (LO3):** the v2 release artefacts (audit triage, spec PR, agreement numbers, release JSON with hash and changelog, split-freeze verification) and the measured v1→v2 delta with attribution.
6. **Evaluation harness (LO5):** deterministic harness with per-class and per-slice reports, error taxonomy with a ranked remediation plan, and the v1-vs-v2 regression summary with bootstrap CI on the headline delta.
7. **Deployment (LO6):** parity-tested ONNX artefacts, INT8 quantisation with slice-checked accuracy cost, the four-config trade-off table, a selected line configuration justified against the 380 ms budget, and the assembled decision pipeline (classifier + detector + segmenter + grading rules) running on sample footage with structured decision logs.
8. **Tracking, serving and monitoring (LO7, LO8):** ByteTrack over the deployed detector with count accuracy ≥ 98% and IDF1 recorded on `line-clip-01`; a track-level decision rule that meets *both* line constraints (≤ 3 false ejections per 1,000 fruit and ≤ 1% mould escape) with the sweep table that selected it; the service with working liveness/readiness gates including the golden-set check; an armed drift monitor that detects all three replay clips with a named suspect per alert; and a shadow-mode run producing a disagreement gallery, a promote/hold decision, and one exported review batch.

**One extension (choose at least one):**
- Live webcam/video-file demo of the full pipeline with on-screen overlays and decisions
- Active-learning round 3: select, justify, and (with provided labels) measure a further targeted improvement
- Grad-CAM/attention error-gallery integration in the harness report
- Sustained-load benchmark (10 min) with thermal/latency plot and an alerting threshold proposal
- Per-class threshold auto-tuner: given a line spec YAML, emit the feasible operating-point set or a data request

## Architecture (target state)

```
                        ┌── training world (GPU) ──────────────────────────┐
 dates-qc releases ──>  │ classifier (M2)  detector (M3)  segmenter (M4)   │
 v1 ─ v2 (M5)           │        └──── evaluation harness (M6) ────┘       │
   │  frozen test split │                    │  regression + slices        │
   │                    └────── export gate: parity + INT8 (M7) ───────────┘
   │                                          │  versioned bundle
   ▼                                          ▼
 audit/AL loop <── review queue <── EDGE BOX: capture → preprocess (contract)
 (M5 flywheel)     (M8)               → detect + segment + classify → TRACK (M8)
      ▲                               → track-level decision (evidence + best view)
      │                               → eject gate  [380 ms end-to-end budget]
 drift alerts <── monitor (M8): image / feature / confidence / outcome layers
 (runbook R-01..R-04)                 served behind /healthz + /readyz gates
```

## Deliverables

1. Repository URL with full history: `tamr_vision/` package, scripts, configs, tests
2. `BENCHMARKS.md` with every course benchmark table filled from *your* runs (pipeline throughput, model comparison, operating points, area MAE, v1→v2 deltas, trade-off table)
3. The harness report pack: HTML report, slice tables, error gallery, regression summary with CI
4. The v2 release folder: `RELEASE.json`, manifest with hashes, spec PR link, agreement numbers
5. Deployment bundle: ONNX artefacts + config + parity evidence + selected line configuration + reference window, golden set, and tracker config (the M8 additions that make the bundle operable)
6. 5-minute demo: line-footage run with track-level decisions and logs, one harness insight (your worst slice), one trade-off defended (your selected config), one drift alert fired live with its named suspect, and your remediation plan's top line
7. `DECISIONS.md`: five one-paragraph engineering decisions with rationale (e.g., operating-point choice, 416² acceptance, calibration stratification, evidence-fraction rule, drift thresholds, fallback behaviour)

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: pipeline + classifier + detector integrated (Labs 1–3) | End Day 2 H3 | instructor spot-check |
| M-B: segmentation + measurement wired (Lab 4) | End Day 2 | area report on 20 frames |
| M-C: v2 release cut + retrain + regression run (Labs 5–6) | Day 3 H5 | regression summary posted |
| M-D: exported, quantised, benchmarked, config selected (Lab 7) | Day 4 H2 | trade-off table complete |
| M-E: assembled decision pipeline running on sample footage | Day 4 H5 | structured decision logs produced |
| M-F: tracked, served, monitored (Lab 8) | Day 5 H2 | both line constraints met; three drift clips detected |
| M-G: full system + self-audit + extension | Day 5 H4 | capstone checklist green |
| M-H: demo + submission | Day 5 H5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Model quality (classifier, detector, segmenter vs targets) | 17 | All targets met on frozen split; per-class numbers honest and reproducible | One target narrowly missed with credible analysis | Targets missed without analysis; eval on wrong split |
| Data curation & v2 evidence | 13 | Audit triaged correctly, spec fix merged, release complete, delta attributed (clean vs new data) | Release complete but attribution thin | Test split touched, no changelog, or fabricated triage |
| Evaluation harness & analysis | 17 | Deterministic, validated matching, slices declared, taxonomy + costed remediation plan, CI on deltas | Harness works; analysis shallow (no plan or no slices) | Framework numbers copied; no per-slice view |
| Deployment & optimisation | 17 | Parity-tested artefacts, slice-checked INT8, complete trade-off table, budget-justified config | Exported and benchmarked; slice check or justification missing | No parity tests; benchmark without warm-up/percentiles |
| Tracking, serving & monitoring | 15 | Count accuracy ≥ 98% with IDF1; decision rule meets both line constraints with its sweep table; readiness gates enforced; three drift clips detected with named suspects; shadow decision backed by a number | Tracking works and one monitoring layer armed; rule justified on aggregate only, or drift coverage partial | Per-frame decisions retained; readiness returns 200 unconditionally; monitoring absent or thresholds invented |
| System integration & decision logic | 13 | Full pipeline on footage; grading rules versioned; structured logs with versions and latencies | Runs but logs thin or rules hard-coded | Components never assembled |
| Demo & decisions doc | 8 | Crisp demo; DECISIONS.md shows trade-off literacy across data/eval/deploy/operations | Demo works; rationale thin | Cannot run own system; no decisions doc |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the repository and harness report first*, demo second — reproducible evidence is the course's thesis; a slick demo with an untouched frozen split beats nothing.
- Verify one number live per participant: re-run their harness on the frozen split and compare to their `BENCHMARKS.md`; any mismatch triggers a full check.
- Anti-pattern flags that cap a criterion at 70%: metrics reported at undeployed thresholds; test-split modifications; INT8 adopted with no slice check; parity "tested" on random tensors only; regression deltas claimed without n or CI; drift thresholds asserted rather than computed from the reference window; a shadow candidate promoted on aggregate agreement without opening the disagreement gallery.
- The DECISIONS.md is where judgement shows: reward participants who *rejected* something defensible (a config, an augmentation, an extension) with reasons.
- Where targets are narrowly missed, grade the analysis: a participant who shows *why* insect_damage stalls and files the correct data request has learned more than one who lucked past the bar.

## Bonus Tasks (for early finishers / distinction seekers)

1. TensorRT or OpenVINO-native engine build with a measured comparison row against ONNX Runtime
2. `sim-drift` reproduction: replay the input-fingerprint drift scenario, show the watchdog alert firing, write the 10-line runbook entry
3. Cross-camera re-identification: join the M8 tracks to a simulated second camera 4 m downstream (appearance embeddings + an arrival window from belt speed) and report the join accuracy and the disagreement-handling rule
4. A one-page "acceptance test" document for a fictional buyer: frozen-split custody, per-slice floors, harness handover — the M6 clause, productised

---

# Assessment Package

## Quiz Bank (23 questions — use 12 per cohort, 15 min, closed book)

**Q1.** OpenCV loads images in which channel order, and what is the cost of forgetting? → BGR; a silent 5–10-point accuracy loss against RGB-trained weights.
**Q2.** Why must train and eval transforms be separate code paths? → augmentation is train-only regularisation; eval/serving need the deterministic contract.
**Q3.** Why split conveyor data by session rather than by frame? → near-duplicate frames leak across splits and inflate every metric.
**Q4.** Name the three convolutional inductive biases. → locality, translation equivariance (weight sharing), hierarchical features.
**Q5.** Why do ViTs need more pre-training data than CNNs to compete? → weak inductive bias — image structure must be learned from data.
**Q6.** Describe the staged fine-tuning recipe and what the stages protect. → head-only first (stabilise new head), then unfreeze with discriminative LRs (protect generic early features from catastrophic forgetting).
**Q7.** What must be embedded in a checkpoint for it to be servable? → class order + preprocessing-contract reference (+ metrics/config).
**Q8.** In a modern YOLO, what do the backbone, neck, and head each do? → features; multi-scale fusion (FPN/PAN); per-cell anchor-free class + box prediction.
**Q9.** What does NMS do and which parameter governs it? → suppresses overlapping same-class detections, keeping the most confident; the IoU threshold.
**Q10.** A perfect box with the wrong class scores as what under mAP matching? → false positive plus an unmatched ground truth (false negative).
**Q11.** mAP@0.5 vs mAP@0.5:0.95 — what does the second additionally reward? → tight localisation across stricter IoU thresholds.
**Q12.** When is instance segmentation required over semantic? → when measurements must be attributed per object (e.g., defect area per fruit).
**Q13.** Why does Dice loss suit thin/rare mask classes better than plain BCE? → BCE is dominated by easy negative pixels; Dice optimises overlap directly.
**Q14.** Two annotators agree with each other but both fail gold tasks — what does this mean? → shared spec misunderstanding; agreement measures consistency, not correctness.
**Q15.** What are the three triage buckets for loss-ranked audit items, and where does the third feed? → label error / model error / ambiguous → the spec's edge-case gallery.
**Q16.** Why is the frozen test split never re-shuffled between dataset releases? → cross-version metric comparisons would become meaningless; additions only.
**Q17.** Why must slices be declared before an evaluation run rather than after? → post-hoc slicing is multiple-comparison fishing; the taxonomy is reviewed like code.
**Q18.** What two tests define ONNX export "done"? → tensor parity within tolerance on real images and zero decision flips at the deployed operating point.
**Q19.** Static INT8 quantisation failed only on the evening slice — most likely cause? → calibration set not representative (sampled from daytime frames).
**Q20.** Why report p99 latency rather than the mean for an actuated line? → actuation deadlines are missed in the tail; means hide the misses.
**Q21.** A fruit is observed 40 times at a per-observation false-positive rate of 0.003 — what is the false-ejection rate under an "any frame fires" rule, and what fixes it? → 1 − 0.997⁴⁰ ≈ 11.3%; deciding once per *track* on aggregated evidence.
**Q22.** What are the four gates a readiness probe must pass before an edge instance may actuate? → bundle hash, preprocessing-contract version, provider warm-up, golden-set pass.
**Q23.** Which drift does a pixel-statistics monitor miss, and which layers catch it? → content drift such as a new date variety; embedding-level (MMD) and outcome-level (reject rate against control limits).

## Practical Assessments

**PA-1 (30 min, Day 2):** Given a broken detection project (BGR feed into the wrapper, class-shifted dataset YAML, metrics reported at conf=0.001), produce a correct evaluation at a defensible operating point. Scored on: diagnosis notes (40%), fixes (40%), verification evidence (20%).

**PA-2 (30 min, Day 3):** Given a dataset PR (three test-split edits, a spec bump without re-annotation, no changelog) and its "improved" metrics, write the review: what may merge, what must change, what the metric claims are worth. Scored against the model review (triage correctness 50%, review actionability 30%, governance reasoning 20%).

**PA-3 (30 min, Day 5):** Given a deployed line whose reject rate has climbed from 6.2% to 24% over three shifts, plus its decision logs, drift-monitor series, and bundle history, produce the incident note: which layer fired first (or should have), the named suspect, the runbook action in the correct order (fallback before diagnosis), and the two follow-up actions that prevent recurrence. Scored on: correct suspect and evidence chain (40%), action ordering and fallback discipline (30%), prevention actions incl. one monitoring change (30%).

**PA-4:** Capstone (rubric above) — 40% of course grade. Labs completion + PA-1/PA-2/PA-3 + quiz — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (8 labs) | 35% | checkpoint commits + expected outputs + `BENCHMARKS.md` entries |
| PA-1 + PA-2 + PA-3 | 15% | artefacts + notes + incident note |
| Quiz | 10% | 10-question selection |
| Vision-system project (capstone) | 40% | rubric, repository-and-harness-first |

Badge issuance (Vision specialisation badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical harness reports or benchmark tables across repositories are checked).

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone course org repos; push checkpoint tags (`lab1-start` … `lab8-start`) and all `sim-*` branches (`sim-interp-skew`, `sim-leaky-split`, `sim-eval-mode`, `sim-class-shift`, `sim-conf-mismatch`, `sim-fat-mask`, `sim-res-320`, `sim-anchor-bias`, `sim-spec-drift`, `sim-threshold-report`, `sim-calib-day`, `sim-wrapper-drift`, `sim-zone-off`)
- [ ] Verify the `dates-qc` bundle (v1 images, manifests, detection/segmentation labels, unlabelled pool, QA double-annotations, audit answer key) on the shared drive; check SHA-256s against the release records
- [ ] Regenerate all reference checkpoints (`lab2`–`lab7-best.pt`, frozen baseline macro-F1 0.86) against the pinned PyTorch/Ultralytics versions; re-run the M6 harness and confirm reference numbers within ±0.005
- [ ] Dry-run all 8 labs end-to-end on a classroom GPU workstation **and** on the CPU-fallback path (320², reduced epochs, provided checkpoints) — a CV course without a verified GPU plan collapses on Day 2
- [ ] Stage the `dates-line-video` pack (`line-clip-01.mp4` + `tracks_gt.json`, the three drift replay clips, the 20-frame golden set) and verify video decode on the classroom machines — check ffmpeg/OpenCV codec support and that the clips play at their declared 30 FPS; a clip that decodes at 15 FPS silently halves every observations-per-fruit number in Lab 8
- [ ] Regenerate the M8 artefacts against the pinned versions: `reference_window.npz` (30 known-good shifts), the golden-set expected decisions, and the `v2.1-candidate` shadow bundle; confirm `make golden` returns 20/20 on a clean box and 6/20 on the deliberately mismatched one
- [ ] Stand up the CVAT/Label Studio instance with the Lab 5 tasks pre-loaded; test the offline triage-CSV fallback
- [ ] Verify GPU drivers, `nvidia-smi`, and VRAM (8 GB+) on every workstation; pre-download all pre-trained weights (ResNet-50, ViT-B/16, yolo11s, yolo11s-seg) to a local cache — do not depend on classroom internet at 9 am
- [ ] Print A4 posters: preprocessing contract, augmentation validity matrix, detector anatomy, aggregate iceberg, optimisation ladder, cloud-vs-edge table
- [ ] Prepare the shared leaderboard (`BENCHMARKS.md` comparison rows: classifier F1, detector mAP, area MAE, pipeline p99)
- [ ] Confirm the Ultralytics licensing position for the classroom and note the AGPL talking points for M3
- [ ] Confirm classroom network allows pypi, github.com, and the weights CDN (or local mirror configured)

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + git + a GitHub account with SSH or PAT auth
- [ ] NVIDIA driver + CUDA-enabled PyTorch ≥ 2.4 and torchvision ≥ 0.19 (`torch.cuda.is_available()` must print `True` on classroom hardware; CPU-only participants follow the fallback notes)
- [ ] `pip install ultralytics opencv-python onnx onnxruntime fastapi uvicorn pandas scikit-learn matplotlib pytest` (ByteTrack ships with Ultralytics; no separate install)
- [ ] VS Code + Python extension (or preferred IDE)
- [ ] Clone course repo; run `make doctor` (validates versions, GPU, weight cache, dataset bundle hashes and prints ✓/✗)
- [ ] Download the `dates-qc` bundle from the shared drive and run `scripts/verify_bundle.py`

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| CUDA/driver mismatch or `cuda.is_available()=False` | High | Pre-session email + first-hour floater support; CPU fallback path for Day 1, fix during breaks |
| Training runs exceed the 15-minute cap | High | Enforce checkpoint fast-forward (`labN-best.pt`); the learning is in decisions, not waiting |
| BGR/RGB and dtype bugs resurfacing in later labs | High | It's the design — route back to the M1 contract; the planted bugs make it a 5-minute fix, not a mystery |
| Windows DataLoader hangs with `num_workers>0` | Medium | `if __name__ == "__main__":` guard; taught in Lab 1 troubleshooting |
| CUDA OOM (ViT, segmenter, batch sizes) | Medium | Halve batch, keep AMP; per-lab fallback batch sizes documented |
| CVAT instance unreachable / accounts confused | Medium | Offline triage-CSV workflow (fully equivalent for assessment); fix accounts at the break |
| Ultralytics version drift changing default hyperparameters | Medium | Pin the version in `requirements.txt`; `make doctor` checks it |
| Participants "improve" the frozen test split | Low | It's a teachable moment — route to the M5/M6 governance lesson; restore from the release hash |
| onnxruntime provider packages (OpenVINO) missing | Low | CPUExecutionProvider fallback; note the EP in the trade-off table |
| Lab 8 track counts absurd (tens of thousands) or IDs unstable | High | The planted `persist=False`; if already fixed, check they hold one model instance across the clip rather than constructing it per frame |
| Port 8000 already bound / `uvicorn` unreachable from the browser | Medium | Corporate proxy or a stale process; assign per-seat ports (8000 + seat number) and curl from the same machine rather than across the classroom LAN |
| Video decodes at 15 FPS, so every per-fruit number halves | Medium | Codec/backend fallback in OpenCV; verify with `cv2.CAP_PROP_FPS` in `make doctor` before Day 5 |

## Timing Recommendations

- Protect Labs 3 and 5 at full length (training time and annotation time make them the overrun-prone pair); compress M4 theory if behind — mask mechanics land through the lab.
- Day 3 Hour 5 (v2 retrain + regression) is the course's emotional payoff; never sacrifice it. If cohort is behind, pre-compute the v2 training run and have pairs run only the regression comparison.
- If a cohort is strong: pull the sustained-load benchmark and the threshold auto-tuner extension into main scope on Day 4.
- Day 5 Hour 1 must reach the false-ejection arithmetic (11.3% vs 2.4 per 1,000) within its first fifteen minutes — everything else in M8 is motivated by that number; if the lecture runs long, cut the tracker comparison table to ByteTrack versus SORT and let the rest land in the lab.
- If a cohort is weak: make Lab 6 tasks 1–2 (matching/AP by hand) a guided walkthrough, but never drop task 3 (the s09 slice discovery) — it is the course's thesis made visible.
- Hard rule: capstone assembly (Day 4 Hour 3 and Day 5 Hour 3) starts on time; cut discussion, not build time.

## Discussion Prompts (use during transitions)

1. "What is the most expensive silent bug you can now name in a vision pipeline — and at which module would you have caught it a year ago?"
2. "Your model's mAP is 0.91. Name three questions that number cannot answer about whether the line should trust it."
3. "Who should own the operating point — engineering, quality, or plant management? What does your answer imply about where the threshold lives in the code?"
4. "The dataset improved the system more than any architecture change this week. Why does your organisation's budget say the opposite?"
5. "Which decision from your DECISIONS.md would you defend in front of a food-safety auditor — and which one are you least sure of?"

## Wrap-up (Day 5 final 15 minutes)

- Map each capstone requirement to the module that taught it (one slide: eight requirements, eight modules — M1 contract, M2 classifier, M3 detector, M4 measurement, M5 dataset, M6 harness, M7 deployment, M8 tracking/serving/monitoring).
- Forward pointer: SDA-AIE-216 (MLOps & AI Reliability) operates *exactly* what was built today — the versioned bundles, harness-as-regression-gate, input fingerprints, and fleet telemetry become deployment pipelines, monitoring, and alerting; the vision badge plus AIE-216 sits inside the AI Engineer Specialist certificate (Specialist = Practitioner Certificate + AIE-216 + any 3 of AIE-211/212/213/214/215).
- Collect: repository URLs, `BENCHMARKS.md`, `DECISIONS.md`, and harness report packs; issue badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.12, PyTorch ≥ 2.4, torchvision ≥ 0.19, Ultralytics ≥ 8.3 (ByteTrack/BoT-SORT tracker configs included), OpenCV ≥ 4.10, onnxruntime ≥ 1.19, FastAPI ≥ 0.115 with uvicorn ≥ 0.30, and a Prometheus-compatible scraper for the `/metrics` endpoint. Verify pinned versions in the course lock file before each delivery.*
