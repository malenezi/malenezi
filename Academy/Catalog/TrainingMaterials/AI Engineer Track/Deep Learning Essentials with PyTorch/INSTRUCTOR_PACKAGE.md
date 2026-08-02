# Deep Learning Essentials with PyTorch
## أساسيات التعلم العميق باستخدام PyTorch

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Deep Learning Essentials with PyTorch |
| **Arabic Title** | أساسيات التعلم العميق باستخدام PyTorch |
| **Module Code** | SDA-AIE-112 |
| **Level** | Practitioner |
| **Duration** | 4 days × 5 learning hours = **20 hours** |
| **Audience** | Engineers who completed Applied ML; developers moving into deep learning |
| **Prerequisites** | SDA-AIE-111 |
| **Assessment** | Labs (60%) + model-training project (40%) |
| **Stackability** | Deep-learning badge · Gateway to all Specialist AI Engineer modules · Counts toward the AI Engineer Practitioner Certificate · Next: SDA-AIE-113 / SDA-AIE-211 |
| **Tools & Platforms** | PyTorch · torchvision · Weights & Biases · CUDA · Hugging Face Hub |

## Course Description

A practical introduction to neural networks that takes engineers from backpropagation mechanics to training real models on GPUs. Participants build, train, and debug networks in PyTorch, apply transfer learning, and manage experiments professionally. It is the gateway to NLP, computer vision, and generative-AI specialisations.

The course is built around a single evolving artefact: **"Tamr Vision"**, an image classifier that grades Saudi date varieties for a Qassim packing house. Participants first derive backpropagation by hand on a micro-network, then rebuild it with PyTorch autograd, grow it into a CNN trained on the course's date-fruit dataset, stabilise it with regularisation and learning-rate scheduling, supercharge it with a pretrained backbone, and finally train it on GPU with every run tracked in Weights & Biases. Every lab produces a component of the final model-training project, so by Day 4 each participant owns a tuned, reproducible, experiment-tracked image classifier — and the training discipline they will reuse in every Specialist module that follows.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Explain neural-network architectures, activation functions, and backpropagation
2. **LO2** — Implement feed-forward, convolutional, and recurrent networks in PyTorch
3. **LO3** — Develop robust training loops with proper loss functions and optimisers
4. **LO4** — Apply regularisation, normalisation, and learning-rate scheduling to stabilise training
5. **LO5** — Implement transfer learning with pretrained models for new tasks
6. **LO6** — Track, compare, and reproduce experiments using experiment-management tools

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | How networks learn | M1: Neural Networks, Activations & Backpropagation · M2 (part): Tensors & Autograd | 50% | 50% | Hand-derived gradients verified against autograd on a micro-network |
| **Day 2** | Training for real | M2: Training Loops · M3: CNNs for Images; RNNs & Sequence Basics | 45% | 55% | Reusable training-loop engine + first CNN trained on the date dataset |
| **Day 3** | Making training behave | M4: Regularisation, Normalisation & Optimisation · M5: Transfer Learning & Pretrained Models | 40% | 60% | Stabilised training run + fine-tuned pretrained backbone beating the from-scratch CNN |
| **Day 4** | Scale it, track it, ship it | M6: GPU Training & Experiment Tracking · Final model-training project | 25% | 75% | GPU-trained, W&B-tracked, tuned image classifier + project demo |

## Hour-by-Hour Breakdown

### Day 1 — How Networks Learn

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why deep learning** + course kickoff | Place deep learning relative to SDA-AIE-111's classical ML; recognise where depth wins (perception, sequence, representation learning) and where it doesn't | Interactive lecture + tabular-vs-image discussion | 80/20 |
| 2 | **Neurons, layers, activations** (M1) | Forward pass as matrix algebra; activation functions and their failure modes; loss functions as terrain | Lecture + whiteboard derivation | 70/30 |
| 3 | **Backpropagation mechanics** (M1) + **Lab 1a** | Chain rule as bookkeeping on the computational graph; derive gradients of a 2-layer network by hand | Guided derivation + paper-and-numpy exercise | 40/60 |
| 4 | **PyTorch tensors and autograd** (M2) | Tensors, dtypes, broadcasting, views; how autograd records the graph and replays it backward | Lecture + live REPL demo | 60/40 |
| 5 | **Lab 1b — Autograd verifies your algebra** | Rebuild the micro-network in PyTorch; match hand gradients to `.grad` within 1e-6; break the graph on purpose (`detach`, `no_grad`) | Guided lab (pairs) | 10/90 |

### Day 2 — Training for Real

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **The canonical training loop** (M2) | `nn.Module`, `Dataset`/`DataLoader`, optimiser step order, train/eval modes, checkpointing, seeding | Lecture + loop dissection on projector | 60/40 |
| 2 | **Lab 2 — Build the training engine** | Implement `engine.py`: full train/validate loop with metrics, checkpointing, overfit-one-batch self-test; train an MLP on Fashion-MNIST | Guided lab (pairs) | 10/90 |
| 3 | **Convolutions and CNN architectures** (M3) | Kernels, stride, padding, receptive fields, pooling; from LeNet to residual connections | Lecture + filter-visualisation demo | 70/30 |
| 4 | **Lab 3 — First CNN on Tamr-9** | Build a small CNN, wire torchvision transforms, train on the date-variety dataset with the Lab 2 engine | Guided lab (pairs) | 10/90 |
| 5 | **RNNs and sequence basics** (M3) | Hidden state, unrolling, vanishing gradients, LSTM/GRU gating; sorting-line sensor mini-exercise | Micro-lecture + mini-lab | 40/60 |

### Day 3 — Making Training Behave

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Diagnosing and regularising** (M4) | Read learning curves; weight decay (AdamW), dropout, label smoothing, augmentation, early stopping | Lecture + curve-reading clinic | 60/40 |
| 2 | **Normalisation and LR scheduling** (M4) | BatchNorm mechanics and pitfalls; LayerNorm/GroupNorm; warmup, cosine, OneCycle; the LR range test | Lecture + live schedule plots | 60/40 |
| 3 | **Lab 4 — Rescue the failing run** | Take a deliberately unstable/overfitting training config and stabilise it; produce an ablation table | Guided lab (pairs) | 10/90 |
| 4 | **Transfer learning and pretrained models** (M5) | Why transfer works; feature extraction vs fine-tuning; torchvision weights API; Hugging Face Hub model cards and licences | Lecture + Hub walkthrough | 70/30 |
| 5 | **Lab 5 — Fine-tune a pretrained backbone** | Fine-tune ResNet on Tamr-9; compare against the Day 2 from-scratch CNN; log both to the comparison table | Guided lab (pairs) | 10/90 |

### Day 4 — Scale It, Track It, Ship It

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **GPU training with CUDA** (M6) | Host/device model, transfers, DataLoader tuning, mixed precision (AMP), throughput measurement | Lecture + profiling demo | 60/40 |
| 2 | **Experiment tracking with W&B** (M6) + **Lab 6** | Runs, configs, artifacts, sweeps; reproducibility discipline; pushing models to Hugging Face Hub | Micro-lecture + lab | 30/70 |
| 3 | **Project build — tune the classifier** | Launch the W&B sweep; iterate on the Tamr Vision classifier against the frozen validation set | Project work | 0/100 |
| 4 | **Project assembly + final evaluation** | Select best run from W&B; retrain/confirm; single evaluation on the sealed test set; complete model card | Project work | 0/100 |
| 5 | **Project demos + assessment + wrap-up** | 5-minute demos with W&B evidence; rubric scoring; path to SDA-AIE-113 / SDA-AIE-211 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module advances the same artefact — the `tamr-vision` repository and its date-variety classifier. Never introduce a throwaway example project; Fashion-MNIST appears once (Lab 2) purely to keep the first training loop fast, and even that run is logged with the same engine the capstone uses.
- **Pace control:** Labs 3 and 5 are the most overrun-prone (first real images, first fine-tune). Publish checkpoint tags (`lab2-start`, `lab2-solution`, `lab3-start`, …) in the course repository so stragglers can fast-forward: `git checkout lab4-start`.
- **Pairing:** rotate pairs daily. Pair a strong-Python participant with a strong-maths participant on Day 1 (backprop derivation) and re-pair by GPU access on Day 4.
- **Environment strategy:** primary = shared GPU workstations or cloud GPU notebooks (one T4-class GPU per pair); fallback = Google Colab / Kaggle kernels with the course repo cloned. Days 1–2 run acceptably on CPU by design; Days 3–4 need GPU. Verify both environments the week before delivery.
- **Language:** deliver in English or Arabic; keep all code, identifiers, run names, and W&B project names in English (mixed-language experiment names break querying and grouping in tracking dashboards).
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day 4 afternoon is deliberately theory-light — sweeps run *during* the break so GPU time is never idle.
- **Assessment logistics:** rubric scoring happens live during Day 4 Hour 5 demos; collect W&B project URLs and repository links at the end of Hour 4 so run histories can be verified before demos begin. The sealed test-set labels stay with the instructor until Hour 4.

---

# Module 1 — Neural Networks, Activations, and Backpropagation

## Module Overview

**Purpose.** Everything in deep learning — every CNN, transformer, and diffusion model — is a differentiable function trained by gradient descent through backpropagation. Engineers who treat backprop as magic cannot debug it: they cannot explain a dead layer, a vanishing gradient, or why their loss sits at exactly `ln(10)`. This module builds the mechanical understanding — forward pass, activation behaviour, chain-rule bookkeeping, initialisation — that turns training failures from mysteries into diagnoses.

**Business relevance.** Saudi organisations are moving from consuming AI APIs to training and adapting their own models — Arabic NLP, medical imaging, industrial vision. The engineers who own those models must answer review-board questions like "why did the model stop improving?" with gradient-level evidence, not guesses. A practitioner who can read gradient statistics cuts failed-training turnaround from days to hours, which directly prices into GPU budgets.

**Industry use cases.**
- A national digitisation programme trains an Arabic handwritten-text recogniser; diagnosing why deeper variants train *worse* requires understanding gradient flow and initialisation.
- A bank's deep credit-risk model plateaus at random-guess loss; the on-call engineer recognises saturated sigmoids from activation histograms within minutes.
- An industrial-vision vendor tunes activation choices (ReLU vs SiLU) for edge-deployment latency and must reason about the accuracy trade-off, not cargo-cult it.

**Expected competencies.** After this module a participant can trace a forward pass by hand, choose and justify activation functions, derive the backward pass of a two-layer network with the chain rule, explain vanishing/exploding gradients and how initialisation controls them, and recognise the classic failure signatures (dead ReLUs, saturation, `ln(C)` plateau).

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Describe a feed-forward network as composed linear maps and nonlinearities, layer by layer | LO1 |
| 1.2 | Compare activation functions (sigmoid, tanh, ReLU, GELU/SiLU) and identify their failure modes | LO1 |
| 1.3 | Derive the backward pass of a two-layer network by hand using the chain rule | LO1 |
| 1.4 | Explain vanishing/exploding gradients and how Kaiming/Xavier initialisation mitigates them | LO1, LO4 |
| 1.5 | Diagnose classic training-failure signatures from loss values and gradient statistics | LO1, LO3 |

## Technical Content

### 1. From linear models to universal approximators

SDA-AIE-111 left participants with linear and tree-based models. A single linear layer `y = Wx + b` can only draw flat decision boundaries; stacking linear layers changes nothing, because a composition of linear maps is still linear: `W2(W1x) = (W2W1)x`. The entire point of a neural network is the **nonlinearity between layers**. With one hidden layer and enough units, an MLP can approximate any continuous function on a bounded domain (universal approximation) — but "can approximate" says nothing about "can be *found* by gradient descent with finite data". Depth matters in practice because deep networks build **hierarchies of features**: edges → textures → parts → objects in vision; characters → morphemes → phrases in text. Teach the framing that recurs all course: *architecture is a prior about the structure of the data* — convolutions encode translation locality (Module 3), recurrence encodes sequential dependence, and plain MLPs encode nothing, which is why they need the most data.

Anchor notation now and keep it for four days: layer ℓ computes `z⁽ℓ⁾ = W⁽ℓ⁾a⁽ℓ⁻¹⁾ + b⁽ℓ⁾`, then `a⁽ℓ⁾ = φ(z⁽ℓ⁾)`. Inputs are `a⁽⁰⁾ = x`; the final `z` values are **logits**.

### 2. Activation functions and their failure modes

Participants must know each activation's *derivative behaviour*, because that is what backprop multiplies by:

| Activation | Formula | Derivative range | Failure mode | Where it survives today |
|---|---|---|---|---|
| Sigmoid | 1/(1+e⁻ᶻ) | (0, 0.25] | Saturates both tails → vanishing gradients; not zero-centred | Output layer for binary probability — nowhere else |
| Tanh | (eᶻ−e⁻ᶻ)/(eᶻ+e⁻ᶻ) | (0, 1] | Still saturates, just zero-centred | Gates inside LSTMs/GRUs (Module 3) |
| ReLU | max(0, z) | {0, 1} | **Dead units**: a unit pushed into z<0 for all inputs gets zero gradient forever | Default for CNNs/MLPs; cheap, no saturation for z>0 |
| Leaky ReLU | max(αz, z) | {α, 1} | Mostly fixes dead units; α is one more knob | Alternative when dead-ReLU rate is high |
| GELU / SiLU | z·Φ(z) / z·σ(z) | smooth | Slightly costlier | Transformers, modern CNNs (EfficientNet uses SiLU) |

Two demonstrations that land: (1) plot sigmoid derivative — maximum 0.25 means every sigmoid layer multiplies the gradient by ≤ 0.25, so ten sigmoid layers shrink it by ≥ 10⁶; (2) train the Lab 1 micro-net with weights initialised at ±5 and watch sigmoid gradients flatline while ReLU survives.

**Softmax + cross-entropy** get special treatment because the capstone is a classifier: softmax turns logits into a distribution; cross-entropy `−log p(correct class)` penalises confident wrong answers hardest. The must-memorise diagnostic: an untrained C-class classifier's loss starts at `ln(C)` — for the 9-class date dataset, **2.197**. A model stuck near `ln(C)` has learned nothing; a model *starting* far above it usually has broken initialisation or unnormalised inputs. The combined gradient is beautifully simple: `∂L/∂z = softmax(z) − onehot(y)` — predicted minus true — which is why frameworks fuse them (`nn.CrossEntropyLoss` takes **logits**, never softmaxed outputs; feeding it probabilities is the single most common beginner bug and it *still trains, just badly* — a silent failure worth demonstrating).

### 3. Backpropagation: the chain rule as bookkeeping

Strip the mystique: backprop is the chain rule applied once per node of the computational graph, cached so nothing is recomputed. For the two-layer network `x → z1 = W1x + b1 → a1 = ReLU(z1) → z2 = W2a1 + b2 → L = CE(z2, y)`:

1. **Forward:** compute and *store* `x, z1, a1, z2` (this storage is why training uses more memory than inference — the exact memory autograd trades in Module 6's AMP discussion).
2. **Backward, output first:** `δ2 = ∂L/∂z2 = softmax(z2) − onehot(y)`.
3. **Parameter gradients are local:** `∂L/∂W2 = δ2 · a1ᵀ`, `∂L/∂b2 = δ2`.
4. **Push through the linear map:** `∂L/∂a1 = W2ᵀ δ2`.
5. **Through the activation:** `δ1 = W2ᵀδ2 ⊙ ReLU′(z1)` — elementwise mask of which units were active.
6. **First layer:** `∂L/∂W1 = δ1 · xᵀ`, `∂L/∂b1 = δ1`.

Three insights to make explicit. First, every layer's backward needs only its *stored forward values* and the *incoming gradient* — locality is what makes autograd (Module 2) implementable as a graph walk. Second, gradients flow backward through the same weights used forward (`W2ᵀ`), so a badly scaled weight matrix corrupts both directions. Third, the ⊙ mask in step 5 is where dead ReLUs die: if `z1 < 0` everywhere, `δ1 = 0` forever, and `W1` never updates.

### 4. Gradient flow, initialisation, and depth

Multiply the layer-to-layer factor `W⁽ℓ⁾ᵀ · φ′` across 20 layers and the gradient either **vanishes** (factors < 1 → early layers learn nothing) or **explodes** (factors > 1 → NaN by step 300). Initialisation is the first-line control: **Xavier/Glorot** (variance 1/fan_avg) keeps activations and gradients at constant variance under tanh-like activations; **Kaiming/He** (variance 2/fan_in) compensates for ReLU zeroing half its inputs. PyTorch's `nn.Linear`/`nn.Conv2d` default to Kaiming-uniform — participants should know that the framework is already doing this for them, and what breaks when someone "helpfully" initialises with `torch.randn(...) * 5`. Preview honestly: initialisation alone stops working around 20–30 layers; the real cures are residual connections (Module 3) and normalisation layers (Module 4) — this module explains *why those cures exist*.

Gradient descent itself: `θ ← θ − η∇L`. Mini-batch SGD estimates the gradient from 32–512 samples — noisy, cheap, and the noise is partly a feature (escapes sharp minima). The learning rate η is the single most important hyperparameter in the course; Module 4 spends an hour on scheduling it. For now, the rule of thumb: loss diverging → η too high; loss crawling linearly → η too low.

### 5. Reading the failure signatures

Give participants the diagnostic table they will use in every later lab:

| Symptom | Likely cause | First check |
|---|---|---|
| Loss pinned at ~ln(C) from step 0 | Model learns nothing: lr ≈ 0, frozen params, labels shuffled | overfit-one-batch test (Module 2) |
| Loss starts far above ln(C) | Broken init or unnormalised inputs | input mean/std; logit magnitudes at init |
| Loss → NaN | Exploding gradients, log(0), lr too high | grad-norm plot; lower lr 10× |
| Train loss ↓, many units output 0 | Dying ReLUs | fraction of zero activations per layer |
| Deeper model trains worse than shallower | Vanishing gradients | per-layer grad-norm histogram |

**Instructor note:** run the "gradient autopsy" demo — a 10-layer sigmoid MLP on Fashion-MNIST with per-layer gradient norms printed; layer 1's norm is ~10⁻⁷ of layer 10's. Then swap sigmoid → ReLU + Kaiming and rerun. The two printouts side by side are the module's money shot.

### 6. Common mistakes & production considerations

1. Feeding softmaxed probabilities to `nn.CrossEntropyLoss` (which applies log-softmax internally) — trains, but with crushed gradients; accuracy quietly caps.
2. Forgetting the nonlinearity between layers — a 5-layer "network" that is secretly one linear map; spot it because it matches logistic-regression accuracy exactly.
3. Unnormalised inputs (pixel values 0–255 straight into the net) — huge activations, saturated units, giant first-layer gradients.
4. Initialising all weights to zero — every unit in a layer computes identical outputs and receives identical gradients forever (symmetry never breaks). Constant *bias* zero is fine; constant *weights* are fatal.
5. Judging architecture by training loss alone — memorisation reads as success; Module 4 formalises the validation discipline.
6. Treating `ln(C)` plateaus as "needs more epochs" — it needs a diagnosis, not patience.

Production considerations: activation choice affects inference latency and quantisation friendliness on edge hardware (plain ReLU quantises and fuses best — relevant to Saudi industrial edge deployments); derived gradients become impossible to hand-verify beyond toy scale, which is exactly why Lab 1 verifies *once* against autograd and then trusts the framework; document architecture decisions (depth, width, activation) with the same rigour as API contracts — the review board *will* ask.

## Code Examples

### The micro-network, forward and backward, in pure NumPy

```python
# src/tamr_vision/foundations/micro_net.py
"""A 2-layer MLP with hand-written forward AND backward passes.

Educational scaffolding for Lab 1: every line here corresponds to one
step of the whiteboard derivation. Lab 1b verifies these gradients
against PyTorch autograd to 1e-6 — after that, we never hand-derive again.
"""
import numpy as np


def relu(z: np.ndarray) -> np.ndarray:
    return np.maximum(0.0, z)


def softmax(z: np.ndarray) -> np.ndarray:
    z = z - z.max(axis=1, keepdims=True)      # numerical stability: shift-invariant
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)


def cross_entropy(probs: np.ndarray, y: np.ndarray) -> float:
    n = y.shape[0]
    return float(-np.log(probs[np.arange(n), y] + 1e-12).mean())


class MicroNet:
    """784 -> hidden -> 9 classifier. Kaiming init for the ReLU layer."""

    def __init__(self, n_in: int = 784, n_hidden: int = 128,
                 n_out: int = 9, seed: int = 42) -> None:
        rng = np.random.default_rng(seed)
        self.W1 = rng.normal(0, np.sqrt(2.0 / n_in), (n_hidden, n_in))
        self.b1 = np.zeros(n_hidden)
        self.W2 = rng.normal(0, np.sqrt(2.0 / n_hidden), (n_out, n_hidden))
        self.b2 = np.zeros(n_out)
        self.cache: dict[str, np.ndarray] = {}

    def forward(self, x: np.ndarray) -> np.ndarray:
        """x: (batch, 784). Stores intermediates — the memory cost of training."""
        z1 = x @ self.W1.T + self.b1
        a1 = relu(z1)
        z2 = a1 @ self.W2.T + self.b2
        self.cache = {"x": x, "z1": z1, "a1": a1}
        return z2                              # logits — loss applies softmax

    def backward(self, logits: np.ndarray, y: np.ndarray) -> dict[str, np.ndarray]:
        """The whiteboard derivation, verbatim. Returns grads keyed like params."""
        x, z1, a1 = self.cache["x"], self.cache["z1"], self.cache["a1"]
        n = y.shape[0]

        # Step 2: dL/dz2 = softmax(z2) - onehot(y)   (mean over batch)
        delta2 = softmax(logits)
        delta2[np.arange(n), y] -= 1.0
        delta2 /= n

        # Step 3: parameter grads are LOCAL to the layer
        gW2 = delta2.T @ a1
        gb2 = delta2.sum(axis=0)

        # Steps 4-5: push through W2, then mask by ReLU'(z1)
        delta1 = (delta2 @ self.W2) * (z1 > 0)   # <- dead units die on this line

        # Step 6: first-layer grads
        gW1 = delta1.T @ x
        gb1 = delta1.sum(axis=0)
        return {"W1": gW1, "b1": gb1, "W2": gW2, "b2": gb2}

    def sgd_step(self, grads: dict[str, np.ndarray], lr: float = 0.1) -> None:
        for name, g in grads.items():
            setattr(self, name, getattr(self, name) - lr * g)
```

### Verifying the algebra against autograd

```python
# tests/foundations/test_micro_net_grads.py
"""The one-time trust handshake: our hand gradients must equal autograd's.

Passing this test is the licence to never hand-derive gradients again.
"""
import numpy as np
import torch
import torch.nn.functional as F

from tamr_vision.foundations.micro_net import MicroNet


def test_hand_gradients_match_autograd():
    net = MicroNet(n_in=20, n_hidden=16, n_out=9, seed=7)
    rng = np.random.default_rng(0)
    x = rng.normal(size=(32, 20))
    y = rng.integers(0, 9, size=32)

    logits = net.forward(x)
    hand = net.backward(logits, y)

    # Same computation in PyTorch, gradients via autograd
    W1 = torch.tensor(net.W1, requires_grad=True)
    b1 = torch.tensor(net.b1, requires_grad=True)
    W2 = torch.tensor(net.W2, requires_grad=True)
    b2 = torch.tensor(net.b2, requires_grad=True)
    xt = torch.tensor(x)
    yt = torch.tensor(y)

    z2 = F.relu(xt @ W1.T + b1) @ W2.T + b2
    loss = F.cross_entropy(z2, yt)             # fused log-softmax + NLL
    loss.backward()

    for name, param in [("W1", W1), ("b1", b1), ("W2", W2), ("b2", b2)]:
        np.testing.assert_allclose(hand[name], param.grad.numpy(),
                                   atol=1e-6, err_msg=f"gradient mismatch: {name}")
```

### The gradient autopsy — per-layer gradient norms

```python
# scripts/gradient_autopsy.py
"""Demo: watch gradients vanish through 10 sigmoid layers, then survive ReLU.

Run:  python scripts/gradient_autopsy.py --activation sigmoid
      python scripts/gradient_autopsy.py --activation relu
"""
import argparse
import torch
import torch.nn as nn

def build(depth: int, width: int, act: str) -> nn.Sequential:
    acts = {"sigmoid": nn.Sigmoid, "relu": nn.ReLU}
    layers: list[nn.Module] = [nn.Flatten()]
    n_in = 28 * 28
    for _ in range(depth):
        linear = nn.Linear(n_in, width)
        if act == "relu":                       # Kaiming for ReLU (PyTorch default
            nn.init.kaiming_normal_(linear.weight, nonlinearity="relu")
        else:                                   # Xavier for saturating activations
            nn.init.xavier_normal_(linear.weight)
        layers += [linear, acts[act]()]
        n_in = width
    layers.append(nn.Linear(n_in, 10))
    return nn.Sequential(*layers)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--activation", choices=["sigmoid", "relu"], default="sigmoid")
    args = p.parse_args()

    torch.manual_seed(0)
    model = build(depth=10, width=256, act=args.activation)
    x, y = torch.randn(64, 1, 28, 28), torch.randint(0, 10, (64,))
    loss = nn.functional.cross_entropy(model(x), y)
    loss.backward()

    print(f"{'layer':<8}{'grad L2 norm':>14}")
    for i, m in enumerate(m for m in model if isinstance(m, nn.Linear)):
        print(f"{i:<8}{m.weight.grad.norm().item():>14.3e}")
    # sigmoid: layer 0 norm ~1e-7 of layer 9's.  relu: within ~1 order of magnitude.
```

## Hands-on Lab 1 — Backprop by Hand, Then by Autograd

| | |
|---|---|
| **Objective** | Derive, implement, and verify the full backward pass of a two-layer classifier; use it to train on a tiny dataset; reproduce two classic failure modes on purpose |
| **Duration** | 2 × 50 min (Day 1 H3 paper part + Day 1 H5 code part) |
| **Setup** | Python 3.12, `pip install numpy torch`, course repo cloned, `git checkout lab1-start` |

**Part A tasks (paper + NumPy, 50 min)**
1. *(10 min)* On paper, in pairs: derive `∂L/∂W2` and `∂L/∂W1` for the 2-layer net, matching the six whiteboard steps.
2. *(20 min)* Complete the `backward()` skeleton in `micro_net.py` (the forward pass and `sgd_step` are given).
3. *(10 min)* Train on the provided 500-sample digit subset for 200 steps; confirm loss falls from ≈2.30 (ln 10) to < 0.6.
4. *(10 min)* Failure reproduction #1: re-initialise all weights to zero; observe the frozen loss; explain the symmetry argument in one sentence in `OBSERVATIONS.md`.

**Part B tasks (PyTorch, 50 min)**
1. *(15 min)* Run `pytest tests/foundations/` — make the gradient-match test pass (fix the two planted sign/transpose bugs in your Part A code if it fails).
2. *(10 min)* Rebuild the micro-net in PyTorch tensors with `requires_grad=True`; single `loss.backward()`; print `.grad` norms.
3. *(10 min)* Break the graph on purpose: insert `.detach()` after the first layer, rerun, and explain in `OBSERVATIONS.md` why `W1.grad` is now `None`.
4. *(10 min)* Failure reproduction #2: scale initial weights ×10 and plot the loss for 200 steps (diverges); then lr ÷100 (crawls). Record both curves.
5. *(5 min)* Commit: `feat(foundations): verified hand-derived backprop against autograd`.

**Expected output**
```
$ python -m tamr_vision.foundations.train_micro
step   0  loss 2.301   (ln(10) = 2.303 — untrained baseline)
step 100  loss 0.918
step 200  loss 0.542
$ pytest tests/foundations/ -q
2 passed in 1.4s   (max |hand - autograd| = 3.1e-08)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Gradient test off by transpose | `gW2 = a1.T @ delta2` vs `delta2.T @ a1` shape confusion | Write shapes above every line: δ2 is (n, 9), a1 is (n, h), gW2 must be (9, h) |
| Gradients match ×batch_size | Forgot `delta2 /= n` (mean vs sum reduction) | `F.cross_entropy` defaults to mean; match it |
| Loss stuck at 2.303 with correct grads | lr too small or ReLU mask inverted (`z1 < 0`) | Check fraction of active units ≈ 0.5 at init |
| NaN in softmax | Missing max-subtraction stability trick | Use the shifted softmax as given |

**Instructor notes.** Part A's paper derivation is non-negotiable — participants who skip it never develop gradient intuition; walk the room and check step 5 (the ReLU mask) specifically, it is where most errors hide. The `delta2 /= n` mean-reduction mismatch is planted deliberately: it produces gradients that are *correct up to a scale factor*, which "kind of trains" — perfect for discussing why silent near-correctness is worse than a crash. Fast finishers: add a `tanh` option and show its gradient test also passes — generality of the chain rule.

## Mini Exercises

**Quiz (5 questions)**
1. Why does stacking linear layers without activations add no capacity? → composition of linear maps is linear.
2. A 9-class classifier shows initial loss 2.20. Healthy or broken? → healthy: ln(9) ≈ 2.197.
3. Which activation's derivative never exceeds 0.25, and what does that imply for depth? → sigmoid; gradients shrink ≥ 4× per layer.
4. What single condition makes a ReLU unit "dead", and which line of the backward pass shows it? → z < 0 for all inputs; the `* (z1 > 0)` mask zeroes δ1.
5. Why is initialising all weights to 0.01 (constant, not zero) still broken? → symmetry: identical units get identical gradients and never differentiate.

**Debugging exercise.** Branch `sim-softmax-twice`: a model applies `softmax` in `forward()` *and* uses `nn.CrossEntropyLoss`. It trains to 71% instead of 88%. Participants must find the double-softmax, explain the crushed-gradient mechanism, and fix it — then articulate why this bug is dangerous precisely because it doesn't crash.

**Derivation exercise.** Extend the hand derivation by one layer (3-layer net) and identify which terms are recomputed vs cached — connect to why autograd stores the forward graph.

**Discussion questions.**
- Your team lead says "we don't need to understand backprop, the framework does it." Give the two strongest counter-examples from today's failure table.
- For an Arabic OCR model deployed on low-power kiosk hardware, what would drive your activation choice besides accuracy? (quantisation friendliness, operator fusion, latency)

## Case Study — Arabic Handwritten-Digit Recognition for a National Archives Digitisation Programme

**Scenario.** A government digitisation contractor in Riyadh is building a recogniser for handwritten Arabic-Indic digits (٠–٩) appearing on 40 years of archived civil-registry forms. A junior team trained a 12-layer sigmoid MLP that plateaus at 11% accuracy — chance level — while a consultant's 3-layer ReLU baseline reaches 97% on the same data.

**Business context.** The digitisation programme processes 2.1 million forms; manual keying costs ≈ SAR 1.1 per field. The 12-layer model burned three weeks of engineer time and a GPU-cluster allocation before anyone questioned the architecture rather than the data.

**Technical challenge.** Explain the failure precisely, fix it minimally, and produce an evidence pack (plots, gradient statistics) that the programme's technical review board can follow.

**Constraints.** The review board mandates model decisions be justified in writing; the team may not simply copy the consultant's architecture without explaining why theirs failed; training data (120k digit crops) cannot leave the government network, so all diagnosis must run on modest internal hardware.

**Solution approach (facilitate, don't lecture).** (1) Reproduce the plateau; note loss pinned at ln(10) ≈ 2.303 from step 0. (2) Print per-layer gradient norms — layers 1–6 receive ~10⁻⁸-scale gradients: textbook vanishing through 12 sigmoid saturations, compounded by inputs left in [0, 255]. (3) Minimal fixes, applied one at a time to isolate effects: normalise inputs → loss starts falling but stalls; swap sigmoid → ReLU with Kaiming init → 95%+; reduce depth to 4 layers → equal accuracy, 3× faster inference. (4) Evidence pack: before/after gradient-norm histograms and the ablation table — the review board reads the table, not the code.

**Discussion questions.**
1. Which single fix would have unstuck training on its own, and how would you prove attribution?
2. The junior team argues "more layers = more capacity, so the deep model must eventually win." Rebut using the trainability-vs-capacity distinction.
3. What in this programme's review process caught the waste late, and what standing diagnostic (from today's failure table) would have caught it on day one?
4. Preview: what two later-course techniques would let a genuinely deep model train here? (residual connections — M3; normalisation layers — M4)

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Hand-vs-autograd gradient agreement | Correctness | max abs diff ≤ 1e-6 | `pytest tests/foundations/` |
| Micro-net loss after 200 steps (500-sample set) | Learning | ≤ 0.6 from 2.30 start | training script output |
| Failure-signature identification | Diagnostic skill | 4/5 symptoms correctly attributed | failure-table exercise sheet |
| Derivation completeness (paper) | Understanding | all 6 steps with correct shapes | instructor spot-check |
| Explanation quality in `OBSERVATIONS.md` | Communication | symmetry + detach effects each ≤ 3 sentences, correct | review |

**Example benchmark table (filled during lab):**

| Configuration | Initial loss | Loss @ 200 steps | Layer-1 grad norm | Verdict |
|---|---|---|---|---|
| ReLU + Kaiming (reference) | 2.301 | 0.542 | 2.1e-02 | healthy |
| Sigmoid ×10 depth | 2.303 | 2.302 | 8.7e-08 | vanishing |
| Zero-init weights | 2.303 | 2.303 | 0.0 | symmetry lock |
| Weights ×10 | 2.9e+01 | NaN | 4.4e+03 | exploding |

## Required Visuals and Training Assets

### Diagrams
1. **The computational graph of the micro-net** — *Purpose:* anchor image for backprop all week. *Elements:* nodes for x, W1, b1, z1, a1, W2, b2, z2, L; forward arrows left-to-right in blue; backward gradient arrows right-to-left in red, each labelled with its local derivative (e.g., `⊙ ReLU′(z1)`); cached values marked with a disk icon. *Style:* flat vector, two-colour arrow scheme, English labels with Arabic subtitles. *Designer description:* "Left-to-right DAG, nine nodes, mirrored red arrows beneath blue ones, small cache icons on z1/a1 nodes."
2. **Activation gallery** — *Purpose:* memorisable reference. *Elements:* 2×3 grid of sigmoid/tanh/ReLU/LeakyReLU/GELU function curves each with derivative curve beneath in lighter shade; failure-mode caption per cell ("saturates", "dies at z<0"). *Style:* small-multiples, printable A4.
3. **Vanishing-gradient waterfall** — *Purpose:* make depth-decay visceral. *Elements:* 10 stacked layer bars whose widths show gradient norm, shrinking log-scale from output to input; sigmoid vs ReLU side-by-side panels. *Style:* horizontal funnel pair.
4. **Loss-terrain cartoon** — *Purpose:* gradient descent intuition without false 2D promises. *Elements:* contour bowl with SGD's noisy path vs full-batch smooth path; annotated learning-rate-too-high overshoot spiral. *Style:* contour plot with three annotated trajectories.

### Images (screenshots)
1. **Terminal — gradient autopsy output (sigmoid vs relu)**: *why:* the module's evidence anchor; *content:* the two 10-row norm tables side by side, layer-0 values highlighted.
2. **Terminal — passing gradient-match test**: *why:* expected-state reference for Lab 1b; *content:* pytest output with `max |hand - autograd| = 3.1e-08` line visible.
3. **Loss-curve plot — healthy vs ×10-weights vs tiny-lr**: *why:* pattern recognition for Day 2+; *content:* three curves, annotated diverge/crawl/healthy.
4. **Paper worksheet photo — completed 6-step derivation**: *why:* exemplar for Part A; *content:* clean handwritten derivation with shapes annotated over every product.

### Simulations
1. **Dead-ReLU epidemic** — *Setup:* branch `sim-dead-relu` initialises biases at −3.0. *Expected behaviour:* ~90% of hidden units output zero for all inputs; loss barely moves; the per-layer active-fraction printout exposes it. *Learning objective:* the ReLU mask in the backward pass is a kill switch; initialisation controls it.
2. **The ln(C) plateau line-up** — *Setup:* three broken configs (lr=0, shuffled labels, frozen params) all showing identical flat 2.303 loss. *Expected behaviour:* participants must distinguish them using gradient norms and the overfit-one-batch probe — same symptom, three causes. *Learning objective:* symptoms need differential diagnosis, not pattern-matched fixes.

### Interactive Activities
- **Chain-rule relay (15 min):** six teams each own one node of the computational graph on the wall; a "gradient token" (card with the current δ value) passes backward, each team writes its local multiplication before passing on; instructor validates against the NumPy printout.
- **Failure-signature flash rounds (10 min):** instructor shows an anonymised loss curve or gradient histogram; pairs have 60 seconds to name the failure and the first check; five rounds.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `digits_500.npz` | Subsample of a public handwritten-digit set, preprocessed by course tooling | NumPy archive | 500 × 784 + labels | Micro-net training (CPU, seconds) |
| Failure-config bundle | Course repo (`sim-*` branches) | git branches | — | Failure reproduction exercises |

### Demo Requirements
- **Instructor demo:** the gradient autopsy, live, both activations, under 5 minutes — rehearse the argparse flip so the contrast lands in one screen.
- **Student demo:** one pair walks the class through their step-5 (ReLU mask) derivation on the whiteboard; class checks shapes.
- **Expected outputs:** all pairs green on the gradient-match test before Day 1 ends — it is the entry ticket to Day 2's training loops.

---

# Module 2 — PyTorch Tensors, Autograd, and Training Loops

## Module Overview

**Purpose.** Module 1 earned the right to trust autograd; Module 2 spends that trust. Participants move from NumPy to PyTorch's tensor library, understand exactly what autograd records and when, and then build the artefact they will reuse for the rest of the course and the rest of their careers: a correct, instrumented, checkpointed training loop. Most deep-learning failures in industry are not modelling failures — they are training-loop failures: a missing `zero_grad`, a model left in train mode during evaluation, a silent device mismatch, a validation set that leaks. This module makes the loop boring, and boring is the goal.

**Business relevance.** Every Saudi team adopting PyTorch writes a training loop in week one, and the quality of that loop determines everything downstream: whether results are reproducible for a regulator, whether a crashed 6-hour run can resume from a checkpoint instead of restarting, whether "the model got worse" can be traced to a code change or a data change. A disciplined loop with checkpointing and seeding is the difference between an experiment and an anecdote — and between billable GPU hours and wasted ones.

**Industry use cases.**
- A Riyadh fintech retrains its fraud model weekly; resumable checkpointing turns a pre-emptible-VM interruption from a lost night into a 3-minute resume.
- A telecom's Arabic chatbot team must reproduce a 4-month-old model for a dispute investigation; seeds, pinned versions, and saved optimiser state make the rerun bit-comparable.
- A government analytics unit reviews a vendor's training code before accepting a delivered model; the reviewer's checklist is essentially this module's loop anatomy.

**Expected competencies.** After this module a participant can manipulate tensors (dtypes, shapes, broadcasting, views) without shape-guessing, explain what `loss.backward()` does and why gradients accumulate, implement a `Dataset`/`DataLoader` pipeline, and write from memory a training loop with correct step order, train/eval mode handling, metric tracking, checkpointing, and the overfit-one-batch self-test.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Create and manipulate tensors: dtypes, devices, broadcasting, views vs copies, in-place pitfalls | LO2 |
| 2.2 | Explain how autograd builds the dynamic graph and control it with `requires_grad`, `detach`, `no_grad` | LO1, LO2 |
| 2.3 | Structure models as `nn.Module` subclasses and select appropriate loss functions and optimisers | LO2, LO3 |
| 2.4 | Build `Dataset`/`DataLoader` pipelines with correct splits, shuffling, and batching | LO3 |
| 2.5 | Implement a complete training/validation loop with checkpointing, seeding, and the overfit-one-batch self-test | LO3, LO6 |

## Technical Content

### 1. Tensors: the five properties that explain every error message

A tensor is data plus five pieces of metadata: **shape**, **dtype**, **device**, **layout/strides**, and **requires_grad**. Nearly every beginner error message names a mismatch in one of them (`expected Float but got Double`, `expected all tensors on the same device`, `shape mismatch`). Teach participants to read errors as metadata disagreements, not mysteries.

Key mechanics to demonstrate live in a REPL:

- **Dtypes.** `torch.float32` is the training default; NumPy defaults to `float64`, so `torch.tensor(np_array)` silently produces float64 — the classic source of "Double vs Float" crashes. Labels for classification must be `int64` (`long`), not float, or `nn.CrossEntropyLoss` refuses them.
- **Broadcasting.** Same rules as NumPy: align shapes from the right, size-1 dimensions stretch. Powerful and dangerous — `(N,) + (N,1)` broadcasts to `(N,N)` without complaint. The defensive habit: `assert` or comment expected shapes at function boundaries, exactly as Lab 1 wrote shapes above every gradient line.
- **Views vs copies.** `view`, `reshape`, `permute`, slicing return *views* sharing storage; mutating a view mutates the original. `permute`/`transpose` produce non-contiguous tensors that `view` rejects — hence `.contiguous()` or `.reshape()`. Show `t.storage().data_ptr()` equality to prove sharing.
- **In-place operations** (`add_`, `relu_`, `x += y`) save memory but can destroy values autograd needs for backward; PyTorch raises `RuntimeError: a leaf Variable that requires grad is being used in an in-place operation` or the subtler version-counter error. Rule for this course: no in-place ops on anything in the gradient path.

### 2. Autograd: a tape recorder, not a compiler

Autograd is **dynamic**: every forward operation on a `requires_grad` tensor appends a node to a graph built *at run time*; `loss.backward()` walks that graph in reverse, calling each node's stored backward function — mechanically identical to Lab 1's hand derivation, generalised. Three consequences participants must internalise:

1. **The graph is rebuilt every iteration.** Python control flow (`if`, loops) just works — the tape records whatever actually executed. This is PyTorch's core ergonomic win and why debugging with `print`/`pdb` inside `forward()` is normal practice.
2. **Gradients accumulate.** `.backward()` *adds* into `.grad`; it does not overwrite. This enables gradient accumulation across micro-batches (Module 6 uses it to simulate large batches) but means a forgotten `optimizer.zero_grad()` mixes stale gradients into every step — the model still trains, just wrongly. Another silent near-correctness bug, deliberately reproduced in Lab 2.
3. **You control graph membership.** `with torch.no_grad():` suspends recording (evaluation, inference — halves memory because nothing is cached); `.detach()` cuts one tensor out of the graph (metric logging, target networks); `param.requires_grad_(False)` freezes parameters (the mechanism behind Module 5's feature extraction).

Memory anatomy, previewed for Module 6: training memory = parameters + gradients + optimiser state (Adam keeps two extra buffers per parameter, roughly 3× parameter memory) + **cached activations** (dominates for CNNs, scales with batch size). This is why `no_grad` inference fits batches that training cannot.

### 3. `nn.Module`, losses, and optimisers: the contract

`nn.Module` is a container with three superpowers: it registers parameters recursively (`model.parameters()` finds everything, which is what the optimiser consumes), it moves as a unit (`model.to(device)`), and it carries a training-mode flag (`model.train()` / `model.eval()`) that switches the behaviour of dropout and batch-norm layers — behaviour changes, *not* gradient on/off, which is `no_grad`'s job. The two are orthogonal and confusing them is the most common eval-time bug in production code review.

Loss functions are chosen by task, and the logits rule from Module 1 carries over: `nn.CrossEntropyLoss` for multi-class (takes logits + integer labels), `nn.BCEWithLogitsLoss` for binary/multi-label (takes logits, never sigmoided outputs), `nn.MSELoss`/`nn.L1Loss`/`HuberLoss` for regression. The `WithLogits` fusions exist for numerical stability — separate sigmoid + BCE overflows in fp16, which matters the moment Module 6 enables mixed precision.

The optimiser step order is liturgy — five lines, always this order:

```
optimizer.zero_grad()      # clear last step's gradients
loss = criterion(model(x), y)
loss.backward()            # populate .grad
optimizer.step()           # θ ← θ − η·(update rule)
scheduler.step()           # if per-step scheduling (Module 4)
```

Start cohorts on `optim.AdamW(model.parameters(), lr=3e-4)` as the sane default; SGD-with-momentum and the *why* of the choice is Module 4's business. What `optimizer.step()` actually does — walk `param_groups`, apply the update rule using `.grad` and per-parameter state — is worth one whiteboard minute, because param groups return in Module 5 (discriminative learning rates).

### 4. `Dataset` and `DataLoader`: the input contract

A `Dataset` answers two questions — `__len__` and `__getitem__(i)` — and should do per-sample work (decode one image, apply transforms). The `DataLoader` industrialises it: batching, shuffling, parallel workers, pinned memory. Rules of thumb taught here and refined in Module 6:

- **Shuffle the training loader; never the validation loader.** Shuffling val wastes time and breaks comparability of per-batch metrics.
- **Split before augmenting; augment only train.** The validation transform is deterministic: resize, tensor, normalise. Applying random augmentation to val makes every evaluation a different exam.
- **Splits are made once and frozen.** For Tamr-9 the course repo ships `splits.json` (70/15/15 stratified by class) checked into git; participants never re-split, because a moving validation set makes every cross-day comparison meaningless — and the sealed test split's labels stay with the instructor until Day 4.
- `num_workers > 0` moves decoding off the training thread; `pin_memory=True` accelerates host→GPU copies. On Windows/macOS, worker processes are spawned, so Dataset code must be importable (no lambdas in transforms) — a portability point worth stating in a mixed-laptop classroom.

### 5. The canonical loop, instrumented: `engine.py`

Lab 2 builds the course's single most reused artefact. Anatomy of a professional epoch loop, beyond the five-line liturgy:

- **Two functions, symmetric:** `train_one_epoch(model, loader, criterion, optimizer, device)` and `evaluate(model, loader, criterion, device)`; the latter wrapped in `@torch.no_grad()` and `model.eval()`, restored to `model.train()` after. Metrics accumulated as running sums, divided once — never mean-of-batch-means with a ragged final batch.
- **Checkpointing:** save `model.state_dict()` *plus* `optimizer.state_dict()`, epoch, best-metric, and the RNG states. `state_dict` (weights only) is the portable artefact; a checkpoint (everything) is the resumable one. Keep `best.pt` and `last.pt` separately — best for deployment, last for resume.
- **Seeding:** one `set_seed(seed)` helper covering `random`, `numpy`, `torch`, CUDA. Honest framing: seeding gives *statistical* reproducibility on GPU (cuDNN nondeterminism exists; Module 6 covers determinism flags); it still catches 95% of "works on my machine".
- **The overfit-one-batch self-test:** before any real training, take one batch of 32 and train on it repeatedly; a correct pipeline drives loss to ~0 within a few hundred steps. If it cannot memorise 32 samples, something is broken — shuffled labels, missing `zero_grad`, wrong loss reduction, frozen params. This 30-second probe is the single highest-value debugging habit in the course; it becomes a permanent `--overfit-one-batch` flag in `engine.py` and a required checkpoint in every later lab.

### 6. Common mistakes & production considerations

1. **Forgetting `optimizer.zero_grad()`** — gradients accumulate across steps; loss falls, then plateaus high. The overfit-one-batch test exposes it in seconds (loss floors at a suspiciously high value).
2. **Evaluating in train mode** — dropout keeps dropping and BatchNorm keeps updating during validation; val metrics are noisy and *optimistic drift* contaminates BN statistics. Symmetric bug: fine-tuning in eval mode silently freezes BN updates.
3. **`loss.item()` vs holding the tensor** — accumulating raw loss tensors keeps every iteration's graph alive; memory climbs until OOM around epoch 3. `item()` (or `.detach()`) at the logging boundary.
4. **float64 tensors from NumPy** — dtype crash, or worse, a silent 2× memory/throughput tax if models are cast up to match.
5. **Validation-set leakage via transforms or re-splitting** — normalisation statistics computed on the full dataset including val/test, or a fresh random split each run. Freeze splits in a file; compute normalisation stats on train only.
6. **Trusting a green loop without a self-test** — a loop that runs without exceptions has proven nothing. Production framing: `engine.py` deserves code review and unit tests like any other software; the overfit-one-batch test *is* its smoke test, and Saudi teams subject to model-governance review (SAMA-regulated banks, PDPL-scoped data) should treat checkpoint + seed + split files as audit artefacts.

## Code Examples

### The course training engine

```python
# src/tamr_vision/engine.py
"""The training engine every later lab and the capstone reuses.

Design contract:
- pure functions over (model, loader, ...) — no globals, no hidden state
- returns plain dicts of floats -> printable, loggable, W&B-ready (Module 6)
- overfit_one_batch() is the mandatory self-test before any real run
"""
from __future__ import annotations

import random
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader


def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def train_one_epoch(model: nn.Module, loader: DataLoader, criterion: nn.Module,
                    optimizer: torch.optim.Optimizer, device: torch.device) -> dict[str, float]:
    model.train()
    total_loss, total_correct, total_n = 0.0, 0, 0
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()
        logits = model(x)
        loss = criterion(logits, y)
        loss.backward()
        optimizer.step()

        bs = y.size(0)
        total_loss += loss.item() * bs          # .item(): free the graph
        total_correct += (logits.argmax(1) == y).sum().item()
        total_n += bs
    return {"loss": total_loss / total_n, "acc": total_correct / total_n}


@torch.no_grad()
def evaluate(model: nn.Module, loader: DataLoader, criterion: nn.Module,
             device: torch.device) -> dict[str, float]:
    model.eval()                                 # dropout off, BN uses running stats
    total_loss, total_correct, total_n = 0.0, 0, 0
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        logits = model(x)
        total_loss += criterion(logits, y).item() * y.size(0)
        total_correct += (logits.argmax(1) == y).sum().item()
        total_n += y.size(0)
    return {"loss": total_loss / total_n, "acc": total_correct / total_n}


def save_checkpoint(path: Path, model: nn.Module, optimizer: torch.optim.Optimizer,
                    epoch: int, best_acc: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"model": model.state_dict(), "optimizer": optimizer.state_dict(),
                "epoch": epoch, "best_acc": best_acc,
                "rng": torch.get_rng_state()}, path)


def overfit_one_batch(model: nn.Module, loader: DataLoader, criterion: nn.Module,
                      device: torch.device, steps: int = 300) -> float:
    """Sanity probe: a correct pipeline memorises one batch. Returns final loss."""
    model.train()
    x, y = next(iter(loader))
    x, y = x.to(device), y.to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
    for _ in range(steps):
        opt.zero_grad()
        loss = criterion(model(x), y)
        loss.backward()
        opt.step()
    return loss.item()   # expect < 0.01; anything above ~0.5 means a broken pipeline
```

### A `Dataset` for Tamr-9 with frozen splits

```python
# src/tamr_vision/data.py
"""Tamr-9 dataset: 9 Saudi date varieties (Sukkari, Khalas, Ajwa, Barhi, Saqi,
Sagai, Mabroom, Khudri, Sufri), directory-per-class image folders.

Splits are FROZEN in splits.json (70/15/15, stratified). Never re-split:
the sealed test split's labels are held by the instructor until Day 4.
"""
import json
from pathlib import Path

import torch
from PIL import Image
from torch.utils.data import Dataset

CLASSES = ["ajwa", "barhi", "khalas", "khudri", "mabroom",
           "sagai", "saqi", "sufri", "sukkari"]


class Tamr9(Dataset):
    def __init__(self, root: str | Path, split: str, transform=None) -> None:
        assert split in {"train", "val", "test"}
        self.root = Path(root)
        self.transform = transform
        with open(self.root / "splits.json") as f:
            self.items: list[list[str]] = json.load(f)[split]  # [relpath, class]

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, i: int) -> tuple[torch.Tensor, int]:
        relpath, cls = self.items[i]
        img = Image.open(self.root / relpath).convert("RGB")
        if self.transform is not None:
            img = self.transform(img)
        return img, CLASSES.index(cls)
```

### Training script: engine + MLP on Fashion-MNIST

```python
# scripts/train_mlp_fmnist.py
"""Day 2 Lab 2 driver: prove the engine on a fast dataset before Tamr-9.

Run:  python scripts/train_mlp_fmnist.py --overfit-one-batch   # self-test first!
      python scripts/train_mlp_fmnist.py --epochs 5
"""
import argparse
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from tamr_vision import engine

p = argparse.ArgumentParser()
p.add_argument("--epochs", type=int, default=5)
p.add_argument("--overfit-one-batch", action="store_true")
args = p.parse_args()

engine.set_seed(42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tfm = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.2860,), (0.3530,))])
train_ds = datasets.FashionMNIST("data/", train=True, download=True, transform=tfm)
val_ds = datasets.FashionMNIST("data/", train=False, download=True, transform=tfm)
train_dl = DataLoader(train_ds, batch_size=128, shuffle=True, num_workers=2)
val_dl = DataLoader(val_ds, batch_size=256, shuffle=False, num_workers=2)

model = nn.Sequential(nn.Flatten(), nn.Linear(784, 256), nn.ReLU(),
                      nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, 10)).to(device)
criterion = nn.CrossEntropyLoss()

if args.overfit_one_batch:
    final = engine.overfit_one_batch(model, train_dl, criterion, device)
    print(f"overfit-one-batch final loss: {final:.4f}  (healthy: < 0.01)")
    raise SystemExit(0)

optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)
best_acc = 0.0
for epoch in range(1, args.epochs + 1):
    tr = engine.train_one_epoch(model, train_dl, criterion, optimizer, device)
    va = engine.evaluate(model, val_dl, criterion, device)
    if va["acc"] > best_acc:
        best_acc = va["acc"]
        engine.save_checkpoint(Path("runs/fmnist/best.pt"), model, optimizer, epoch, best_acc)
    engine.save_checkpoint(Path("runs/fmnist/last.pt"), model, optimizer, epoch, best_acc)
    print(f"epoch {epoch}  train loss {tr['loss']:.3f} acc {tr['acc']:.3f}"
          f"  |  val loss {va['loss']:.3f} acc {va['acc']:.3f}")
```

## Hands-on Lab 2 — Build the Training Engine

| | |
|---|---|
| **Objective** | Implement `engine.py` from a skeleton, validate it with the overfit-one-batch self-test, train an MLP to ≥ 88% on Fashion-MNIST, and prove resume-from-checkpoint works |
| **Duration** | 50 min (Day 2 H2) + threads through H1's loop dissection |
| **Setup** | Course repo, `git checkout lab2-start`; CPU is sufficient by design |

**Tasks**
1. *(10 min)* Complete `train_one_epoch` and `evaluate` in the skeleton (function signatures and metric bookkeeping given; the loop bodies are yours). Respect the five-line order.
2. *(5 min)* Run `--overfit-one-batch`. It will **fail** — the skeleton ships with `zero_grad()` deliberately commented out. Diagnose from the loss floor, fix, rerun, and record both floor values in `OBSERVATIONS.md`.
3. *(15 min)* Train 5 epochs on Fashion-MNIST; reach ≥ 88% val accuracy. Watch per-epoch prints for the train/val gap.
4. *(10 min)* Kill the run after epoch 2 (Ctrl-C). Implement `load_checkpoint` and `--resume runs/fmnist/last.pt`; confirm epoch numbering and metrics continue seamlessly.
5. *(5 min)* Break it on purpose: call `evaluate` without `model.eval()` on a dropout-augmented variant (`sim-eval-mode` branch); record the val-accuracy jitter across 3 identical evaluations.
6. *(5 min)* Commit: `feat(engine): training engine with self-test, checkpointing, resume`.

**Checkpoints**
- [ ] Overfit-one-batch loss < 0.01 after the fix (screenshot the before/after floors)
- [ ] Val accuracy ≥ 88% within 5 epochs
- [ ] Resume continues from epoch 3 with matching optimiser state (loss does not spike)
- [ ] `pytest tests/engine/` green (shape, metric-averaging, and checkpoint round-trip tests)

**Expected output**
```
$ python scripts/train_mlp_fmnist.py --overfit-one-batch
overfit-one-batch final loss: 1.8734  (healthy: < 0.01)     # before fix
overfit-one-batch final loss: 0.0021  (healthy: < 0.01)     # after fix
$ python scripts/train_mlp_fmnist.py --epochs 5
epoch 1  train loss 0.531 acc 0.812  |  val loss 0.442 acc 0.842
...
epoch 5  train loss 0.271 acc 0.899  |  val loss 0.331 acc 0.883
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `RuntimeError: expected scalar type Long` | float labels into CrossEntropyLoss | `y = y.long()` at the Dataset boundary |
| Loss floor ~1.9 in self-test | the planted missing `zero_grad` | restore it; explain accumulation in OBSERVATIONS.md |
| Memory climbs every epoch | accumulating loss tensors, not `.item()` | detach at the logging boundary |
| Resume restarts at epoch 1 | loaded model but not epoch/optimizer state | checkpoint dict, not bare state_dict |
| DataLoader hangs on Windows | `num_workers>0` with non-importable transform | guard with `if __name__ == "__main__"`, no lambdas |

**Instructor notes.** The planted `zero_grad` bug is the module's teaching centrepiece: it trains, loss falls, and *only* the self-test floor reveals it — walk the room and make every pair articulate why the floor is high before showing the fix. Task 4 (resume) is what separates engineers from notebook users; check that optimiser state is loaded by asking "why didn't your loss spike at epoch 3?" Fast finishers: add a `--limit-batches N` flag for fast CI runs of the engine tests.

## Mini Exercises

**Quiz (5 questions)**
1. `a = torch.ones(3); b = a.view(1, 3); b[0, 0] = 5`. What is `a[0]`? → 5.0 — views share storage.
2. Why does calling `.backward()` twice in a row without `zero_grad` double some gradients? → grads accumulate by design (enables gradient accumulation; requires explicit zeroing).
3. `model.eval()` vs `torch.no_grad()` — which affects dropout, which affects memory? → eval: layer behaviour (dropout/BN); no_grad: stops graph recording, saves activation memory.
4. Your val accuracy differs on every identical evaluation run. First suspect? → model left in train mode (active dropout / BN updates).
5. What goes into a *resumable* checkpoint beyond `model.state_dict()`? → optimizer state, epoch, best metric, RNG state.
6. Why must normalisation statistics be computed on the training split only? → computing on all data leaks val/test information into preprocessing.

**Prediction exercise.** Given `x = torch.randn(32, 10, requires_grad=True)` and `y = (x * 2).sum(); y.backward()`, predict `x.grad` before running. Then predict what a second `y.backward()` raises and why (graph freed; `retain_graph`).

**Refactoring exercise.** Convert the Module 1 NumPy `MicroNet` into an `nn.Module` (`nn.Linear`, `nn.ReLU`) and train it with `engine.py` — the exact bridge from Module 1's algebra to production PyTorch, in under 25 lines.

**Discussion questions.**
- Your teammate's notebook trains fine but their val accuracy is 4 points above yours on identical code. List three loop-level causes before blaming the data.
- A regulator asks you to reproduce last quarter's model. Which files from today's lab do you hand over, and what *can't* you promise bit-for-bit on GPU?

## Case Study — The Meter-Reading Model That "Trained Fine" at a Jeddah Utility Contractor

**Scenario.** A contractor digitising handwritten water-meter readings for a utility in Jeddah trained a digit-recognition model that reported 96% validation accuracy in the notebook, but scored 71% in the acceptance test on the utility's held-out data. The contractor's team insists "the model trained fine — the acceptance data must be different."

**Business context.** The contract covers 800,000 meter photos per quarter with a penalty clause below 90% field accuracy. The dispute is heading to a joint technical review; the utility's engineer (the participant's role) must audit the training code, not the model weights.

**Technical challenge.** The audit finds three compounding loop defects: (1) the train/val split was re-randomised on every notebook restart, and the "best epoch" was cherry-picked across restarts — effectively model selection on shifting validation sets; (2) normalisation statistics were computed over the *entire* dataset including validation; (3) evaluation ran with the model in train mode, and the reported 96% was the single luckiest of several dropout-noisy evaluations.

**Constraints.** The review must produce reproducible evidence within two days on the utility's modest on-prem hardware; the contractor's data cannot be modified, only the training procedure; findings must be explainable to a non-ML contract manager.

**Solution approach (facilitate, don't lecture).** (1) Freeze splits in a committed `splits.json`; rerun training with seeds — honest val accuracy lands at 88%. (2) Recompute normalisation on train only — negligible change here, but the point is procedural: it *could* have mattered and the audit must close it. (3) Fix eval mode — the evaluation variance collapses from ±2.5 points to ±0.1. (4) Deliver an evidence pack: the three diffs, before/after metric tables across 5 seeded runs, and a one-page procedural checklist the utility now attaches to all ML deliverables.

**Discussion questions.**
1. Rank the three defects by how much of the 96% → 71% gap each explains, and design the experiment that proves your ranking.
2. The contractor proposes fixing the gap by training longer. Why does no amount of training fix any of these three defects?
3. Which artefacts from Lab 2 (`splits.json`, seeds, checkpoints, self-test output) would have prevented the dispute entirely if contractually required?
4. Draft the two-sentence acceptance-test clause you would add to the next ML procurement contract.

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Overfit-one-batch final loss | Pipeline correctness | < 0.01 in ≤ 300 steps | `--overfit-one-batch` flag |
| Fashion-MNIST val accuracy (MLP, 5 epochs) | Learning | ≥ 88% | training script output |
| Resume integrity | Engineering | loss continuity within 0.02 at resume epoch | before/after epoch prints |
| Engine unit tests | Correctness | `pytest tests/engine/` all green | CI / local pytest |
| Eval-mode variance (3 identical evals) | Discipline | ≤ 0.1 pp spread | sim-eval-mode exercise |
| Loop liturgy from memory | Fluency | 5 lines, correct order, closed book | Day 2 exit ticket |

## Required Visuals and Training Assets

### Diagrams
1. **Anatomy of one training step** — *Purpose:* the loop as a cycle, not a script. *Elements:* circular flow: batch → forward → loss → backward → step → zero_grad, with autograd's cached activations shown as a growing/cleared stack beside forward/backward; annotations marking where `.item()`, `no_grad`, and eval mode intervene. *Style:* circular flowchart, two-colour (data blue, gradient red), English labels.
2. **Tensor metadata card** — *Purpose:* error-message decoder. *Elements:* one tensor drawn as a box with five labelled tabs (shape, dtype, device, strides, requires_grad), each tab paired with the error message its mismatch produces. *Style:* flat vector reference card, printable A4.
3. **Views vs copies memory map** — *Purpose:* make storage sharing visible. *Elements:* one storage bar; three view windows (`view`, slice, `permute`) pointing into it; a `.clone()` box with its own bar. *Style:* memory-layout diagram.
4. **Checkpoint contents vs state_dict** — *Purpose:* resumable vs portable. *Elements:* nested-box diagram: state_dict inside checkpoint alongside optimizer state, epoch, RNG; arrows to "deploy" (state_dict) and "resume" (checkpoint). *Style:* nested containers.

### Images (screenshots)
1. **REPL session — broadcasting surprise**: *why:* the (N,)+(N,1)→(N,N) trap live; *content:* shapes printed before and after, highlighted.
2. **Terminal — self-test before/after the zero_grad fix**: *why:* the module's evidence anchor; *content:* both loss floors side by side.
3. **Terminal — resumed run**: *why:* expected state for Lab 2 task 4; *content:* Ctrl-C at epoch 2, restart, epoch 3 continuing with continuous loss.
4. **`torchviz` render of the MLP's backward graph**: *why:* the "tape" made visible once; *content:* graph for one loss computation with node names.

### Simulations
1. **The accumulating-gradient slow poison** — *Setup:* branch `sim-no-zero-grad` (Lab 2's planted bug, kept as a named branch). *Expected behaviour:* loss falls fast then floors ~4× above healthy; self-test exposes it in 30 s. *Learning objective:* silent near-correctness; the self-test as smoke test.
2. **Leaky evaluation** — *Setup:* branch `sim-eval-mode`: dropout model evaluated in train mode. *Expected behaviour:* val accuracy varies run to run; fixing `model.eval()` collapses variance. *Learning objective:* eval mode is behavioural, not optional.
3. **The graph-hoarding logger** — *Setup:* branch `sim-oom-logging` accumulates raw loss tensors into a list. *Expected behaviour:* RSS climbs ~linearly; OOM on 8 GB machines by epoch 3. *Learning objective:* `.item()` at the logging boundary; memory anatomy preview for Module 6.

### Interactive Activities
- **Loop-order scramble (10 min):** pairs receive the five liturgy lines plus three distractors (`model.eval()`, `loss.item()`, `scheduler.step()`) on cards; assemble the correct training step and justify each rejection; instructor validates against `engine.py`.
- **Error-message triage (15 min):** six real PyTorch error messages on the projector; teams have 90 seconds each to name the mismatched tensor property and the one-line fix; scored as a leaderboard.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Fashion-MNIST | torchvision built-in download | idx/gz | 60k + 10k, 28×28 grey | Fast engine validation (CPU-friendly) |
| Tamr-9 (introduced) | Course bundle (curated date-variety photos) | JPEG folders + `splits.json` | ~9k images, 9 classes | Dataset class built now, trained on in M3 |
| `sim-*` branches | Course repo | git branches | — | Failure reproductions |

### Demo Requirements
- **Instructor demo:** live loop dissection in H1 — delete `zero_grad` on the projector, run the self-test, restore it, rerun; under 4 minutes.
- **Student demo:** one pair demonstrates kill-and-resume with continuous metrics; class inspects their checkpoint dict keys.
- **Expected outputs:** every pair's engine passes `pytest tests/engine/` before Day 2 H3 — the CNN lab imports it unchanged.

---

# Module 3 — CNNs for Images; RNNs and Sequence Basics

## Module Overview

**Purpose.** Module 1 planted the framing: *architecture is a prior about the structure of the data*. This module cashes it in twice. Convolutional networks encode the priors of images — locality, translation, hierarchy — and turn a hopeless MLP problem (a 224×224 RGB image is 150,528 inputs) into a tractable one. Recurrent networks encode the prior of sequences — order and state. Participants build the first real Tamr Vision CNN, wire a proper image pipeline with torchvision, and get a working, honest introduction to RNNs: enough to use an LSTM/GRU on sensor data and to understand *why* gating exists, without pretending this is an NLP course (that is SDA-AIE-113's job).

**Business relevance.** Vision is the most immediately deployable deep-learning capability in the Saudi industrial economy — quality inspection, safety compliance, document processing, agriculture. Sequence models cover the second wave: sensor telemetry, transaction streams, demand signals. An engineer who can select the right architectural prior for the data — and articulate why a CNN needs 100× less data than an MLP for the same image task — makes the build-vs-buy conversation an engineering decision instead of a vendor pitch.

**Industry use cases.**
- A date-packing house in Qassim (the course's golden thread) grades fruit varieties on a conveyor at 10 items/second — a CNN task with hard latency and accuracy floors.
- A Yanbu industrial operator monitors pump-vibration telemetry for early bearing-failure signatures — a sequence-classification task where an LSTM beats threshold rules.
- A Riyadh bank's document-intake pipeline classifies scanned forms (national ID, IBAN letter, salary certificate) before OCR routing — small CNNs at high throughput.

**Expected competencies.** After this module a participant can compute output shapes and receptive fields of conv/pool stacks, design a small CNN with justified architectural choices (channel progression, pooling, global average pooling, residual awareness), build train/val transform pipelines correctly, train the CNN on Tamr-9 with the Module 2 engine, and implement a GRU/LSTM classifier for a sensor sequence while explaining vanishing gradients through time and why gates mitigate them.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Explain convolution as a learned, weight-shared local filter and contrast its parameter count with a dense layer | LO1, LO2 |
| 3.2 | Compute output spatial dimensions and receptive fields for conv/pool stacks (kernel, stride, padding) | LO2 |
| 3.3 | Implement and train a CNN on Tamr-9 using torchvision transforms and the Module 2 engine | LO2, LO3 |
| 3.4 | Explain residual connections as the architectural fix for depth-related gradient decay | LO1 |
| 3.5 | Implement a GRU/LSTM sequence classifier and explain vanishing gradients through time and gating | LO1, LO2 |

## Technical Content

### 1. Why dense layers fail on images — and what convolution keeps

Concretely: a single dense layer from a 224×224×3 image to 1,024 hidden units costs **154 million parameters** — before the second layer. Worse than the count is what dense layers *don't know*: that a date fruit in the top-left corner is the same object as one in the centre. An MLP must re-learn every feature at every position from data; shift the image two pixels and its input vector is scrambled.

Convolution imports three priors. **Locality:** each output pixel looks at a small neighbourhood (a k×k kernel), because nearby pixels are correlated and distant ones mostly aren't. **Weight sharing:** the *same* kernel slides across the whole image — one edge detector serves every location, collapsing 154 M parameters to k×k×C_in×C_out (a 3×3 conv from 3 to 64 channels is 1,792 parameters including bias). **Translation equivariance:** shift the input, the feature map shifts with it; the *what* is decoupled from the *where* until pooling deliberately discards the where. A conv layer is not a different kind of learning — it is a linear layer with almost all weights tied and most set to zero, which is why everything from Modules 1–2 (backprop, initialisation, the training loop) applies unchanged.

Channels carry the semantics: layer 1's 32 channels might learn edge orientations and colour blobs; deeper layers combine them into textures (date-skin wrinkle patterns), then parts (crown, body sheen), then varieties — the feature hierarchy Module 1 promised, now with an address.

### 2. Convolution arithmetic and receptive fields

The one formula participants must own: `out = ⌊(in + 2·padding − kernel) / stride⌋ + 1`. Drill it until reflexive, because shape errors are the #1 CNN build failure. Standard vocabulary:

- **Padding** `same`-style (`padding = kernel//2` for odd kernels, stride 1) preserves spatial size — the default for "keep resolution, grow channels" stages.
- **Stride 2** halves resolution and is the modern downsampler of choice; **max pooling** 2×2 is the classic alternative and survives where a cheap, parameter-free reduction is wanted. Either way, the canonical CNN rhythm is: *halve the spatial size, double the channels* — total activation volume shrinks gently while semantic depth grows.
- **Receptive field** — the input region influencing one output unit — grows with every layer: RF ← RF + (kernel−1)×∏(previous strides). Three stacked 3×3 convs see 7×7 with 27·C² weights vs one 7×7 conv's 49·C² — deeper-and-thinner wins on parameters *and* adds two extra nonlinearities (the VGG insight). Practical rule for the lab: the final receptive field must cover the discriminative structure. Date-variety cues (skin texture, shape) span most of a 128×128 crop, so the Tamr CNN needs 4–5 downsampling stages — participants verify this by computing RF by hand in Lab 3.
- **Global average pooling (GAP)** replaces the giant flatten-then-dense head of older CNNs: average each final channel to one number, then a single linear layer to logits. It slashes parameters, tolerates variable input sizes, and is standard in every modern backbone participants will meet in Module 5.

### 3. From LeNet to ResNet: the architecture arc participants need

Teach the arc as three ideas, not a history lesson. **LeNet/AlexNet:** conv-pool stacks work; depth beats width; ReLU makes depth trainable (Module 1's story, empirically). **VGG:** uniform 3×3 blocks, doubling channels per stage — the "rhythm" above, still the template for hand-built CNNs like Lab 3's. **ResNet:** the fix for the Module 1 cliff-hanger. Plain nets *degrade* past ~20 layers — worse *training* loss, so it's optimisation, not overfitting. The residual block computes `y = F(x) + x`: layers learn a *correction* to identity instead of a full mapping, and the skip connection gives gradients an unattenuated highway backward — `∂y/∂x = ∂F/∂x + I`, so the gradient always has a "+ I" path. That one equation explains why 50- and 101-layer networks train, and it is why every pretrained backbone in Module 5 is residual. Lab 3's CNN stays plain (5 conv stages — shallow enough not to need skips), but participants add one optional residual block as a stretch task to see the mechanics.

BatchNorm appears in these architectures at every conv; this module places it in the diagram and defers the mechanics to Module 4 — tell participants explicitly that the deferral is deliberate.

### 4. The image pipeline: torchvision transforms done right

The Tamr-9 pipeline, and the reasoning participants must be able to reconstruct:

- **Train transforms:** `RandomResizedCrop(128, scale=(0.7, 1.0))` (frames vary on the packing line), `RandomHorizontalFlip()` (dates have no canonical left/right), `ColorJitter(brightness=0.2, contrast=0.2)` (warehouse lighting varies), `ToTensor()`, `Normalize(mean, std)` with statistics computed *on the train split* (Module 2's rule). Augmentation is regularisation-by-invariance: each transform asserts "this variation does not change the label." The negative example matters: **no vertical flips or 90° rotations for documents/digits** — an augmentation that changes semantics poisons training. Augment train only; val/test get the deterministic `Resize(146) → CenterCrop(128) → ToTensor → Normalize`.
- **Tensor layout:** PyTorch images are **CHW**, PIL/NumPy are HWC; `ToTensor()` does the permutation *and* scales to [0,1]. The classic symptom of layout confusion is a model that trains but plateaus low, or a garish matplotlib render — show both.
- Debug ritual before any training run: pull one batch, print `shape`, `dtype`, `min/max`, and render an 8-image grid with labels. Thirty seconds that catches label misalignment, broken normalisation, and over-aggressive augmentation. This ritual is a required checkpoint in Lab 3 and stays mandatory through the capstone.

### 5. Sequences: hidden state, BPTT, and why gates exist

An RNN processes a sequence step by step, carrying a **hidden state**: `h_t = tanh(W_x x_t + W_h h_{t−1} + b)` — a loop in time, sharing weights across steps exactly as a conv shares them across space (same prior, different axis). Training unrolls the loop and backpropagates **through time**: the gradient at step t reaching step t−k passes through k multiplications by `W_hᵀ · tanh′` — Module 1's vanishing/exploding product, now with the *same* matrix every step, which makes the geometric decay ruthless. Practical horizon for plain RNNs: ~10–20 steps.

**LSTM/GRU** fix it with gates: a cell state updated *additively* (`c_t = f_t ⊙ c_{t−1} + i_t ⊙ c̃_t`) — the residual-connection idea, in time — with sigmoid gates learning what to keep, write, and expose. Participants do not memorise the six LSTM equations; they must be able to say *additive cell path = gradient highway; gates = learned, data-dependent forgetting*, and know the GRU as the 2-gate lighter variant that is the sensible default for modest sequence tasks. Practicalities that actually bite in the mini-lab: `nn.GRU(batch_first=True)` (default is seq-first — the #1 silent shape bug), take `h_n` (last hidden state) or masked mean over outputs for classification, clip gradient norm to 1.0 (exploding gradients are *routine* in RNNs, and `clip_grad_norm_` is the standard guard).

Close with honest positioning: transformers have displaced RNNs across NLP and much of sequence modelling (SDA-AIE-113 and the Specialist modules take over there), but small GRUs remain genuinely competitive for low-latency sensor/telemetry classification on edge hardware — which is exactly the mini-lab's use case, and exactly the deployment profile of Saudi industrial IoT.

### 6. Common mistakes & production considerations

1. **Shape-blind architecture building** — stacking convs until `RuntimeError: mat1 and mat2 shapes cannot be multiplied` at the classifier head. Compute shapes by hand first (Lab 3 requires the filled shape table); or use GAP and stop caring about the exact spatial size.
2. **Normalising with the wrong statistics** — ImageNet stats on Tamr-9 from-scratch training (harmless-looking, but train-split stats are the honest default), or forgetting `Normalize` entirely (inputs in [0,1] train slower and clash with init assumptions).
3. **Augmenting validation** — every evaluation becomes a different exam; model selection turns to noise. The transform split from Module 2, violated visually.
4. **Semantics-changing augmentation** — vertical flips on digits/documents, hue shifts on tasks where colour *is* the label (date varieties differ by colour — participants must justify their ColorJitter ranges in Lab 3, a deliberate judgement call).
5. **`batch_first` confusion in RNNs** — the model trains on transposed nonsense and lands at chance; the batch-grid ritual has no RNN equivalent, so assert shapes at the module boundary.
6. **Forgetting `clip_grad_norm_` on recurrent models** — intermittent NaNs hours into training. Clip by default on any recurrent net.

Production considerations: throughput at the packing line is 10 items/s — measure inference latency (CPU vs GPU, batch 1 vs 32) before promising real-time; smaller inputs (128² not 224²) quarter the compute of one downsampling stage; decode-and-augment CPU cost often bottlenecks GPU training (Module 6 profiles this properly); and archive the *exact* transform code with every trained model — a model is only reproducible with its preprocessing, a point that returns as the "preprocessing contract" in Module 5.

## Code Examples

### The Tamr Vision CNN

```python
# src/tamr_vision/models/cnn.py
"""TamrCNN: hand-built VGG-rhythm CNN for 128x128 date-variety crops.

Five stages, halve-space/double-channels, GAP head. Deliberately plain
(no residuals needed at this depth) — Module 5 replaces it with a
pretrained backbone and must BEAT it to justify the swap.
"""
import torch
import torch.nn as nn


def conv_block(c_in: int, c_out: int) -> nn.Sequential:
    """3x3 conv (same padding) -> BN -> ReLU -> 2x2 maxpool: halves H,W."""
    return nn.Sequential(
        nn.Conv2d(c_in, c_out, kernel_size=3, padding=1, bias=False),
        nn.BatchNorm2d(c_out),                # mechanics in Module 4
        nn.ReLU(inplace=True),
        nn.MaxPool2d(2),
    )


class TamrCNN(nn.Module):
    def __init__(self, n_classes: int = 9, width: int = 32) -> None:
        super().__init__()
        w = width
        self.features = nn.Sequential(        # 128 -> 64 -> 32 -> 16 -> 8 -> 4
            conv_block(3, w),
            conv_block(w, w * 2),
            conv_block(w * 2, w * 4),
            conv_block(w * 4, w * 8),
            conv_block(w * 8, w * 8),
        )
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),          # GAP: (B, 256, 4, 4) -> (B, 256, 1, 1)
            nn.Flatten(),
            nn.Linear(w * 8, n_classes),      # -> logits, never softmax (Module 1)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.head(self.features(x))
```

### Transforms and loaders for Tamr-9

```python
# src/tamr_vision/transforms.py
"""Train vs eval pipelines for Tamr-9. Stats computed on the TRAIN split
by scripts/compute_stats.py — never on val/test (Module 2's rule)."""
from torchvision import transforms

TAMR9_MEAN = [0.5312, 0.4483, 0.3122]   # train-split statistics
TAMR9_STD = [0.2211, 0.2035, 0.1912]

train_tfms = transforms.Compose([
    transforms.RandomResizedCrop(128, scale=(0.7, 1.0)),
    transforms.RandomHorizontalFlip(),
    # ColorJitter ranges are a JUDGEMENT CALL here: variety cues include
    # colour, so ranges must stay small. Justify yours in OBSERVATIONS.md.
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.1),
    transforms.ToTensor(),
    transforms.Normalize(TAMR9_MEAN, TAMR9_STD),
])

eval_tfms = transforms.Compose([          # deterministic: same exam every time
    transforms.Resize(146),
    transforms.CenterCrop(128),
    transforms.ToTensor(),
    transforms.Normalize(TAMR9_MEAN, TAMR9_STD),
])
```

### GRU classifier for sorting-line vibration windows

```python
# src/tamr_vision/models/sensor_gru.py
"""GRU classifier for 200-step, 3-axis accelerometer windows from the
packing-line conveyor: {normal, imbalance, bearing-wear}.

The RNN mini-lab model. batch_first=True is NOT the default — the
seq-first trap is the #1 silent RNN shape bug.
"""
import torch
import torch.nn as nn


class SensorGRU(nn.Module):
    def __init__(self, n_features: int = 3, hidden: int = 64,
                 n_classes: int = 3, num_layers: int = 1) -> None:
        super().__init__()
        self.gru = nn.GRU(n_features, hidden, num_layers=num_layers,
                          batch_first=True)          # (B, T, F) in, not (T, B, F)
        self.head = nn.Linear(hidden, n_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        assert x.dim() == 3, f"expected (B, T, F), got {tuple(x.shape)}"
        _, h_n = self.gru(x)                          # h_n: (layers, B, hidden)
        return self.head(h_n[-1])                     # last layer's final state


# In the training step, clip before optimizer.step() — exploding gradients
# are ROUTINE in recurrent nets:
#   loss.backward()
#   torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
#   optimizer.step()
```

## Hands-on Lab 3 — First CNN on Tamr-9 (plus the RNN Mini-Lab)

| | |
|---|---|
| **Objective** | Build TamrCNN from a skeleton, verify shapes and receptive field by hand, wire the transform pipeline, train to ≥ 80% val accuracy on Tamr-9 with the Lab 2 engine, and read the confusion matrix; then (H5) train the GRU on sensor windows |
| **Duration** | 50 min (Day 2 H4) + 30 min mini-lab (Day 2 H5) |
| **Setup** | `git checkout lab3-start`; GPU preferred, CPU acceptable at width=16 with `--limit-batches` |

**Tasks (CNN)**
1. *(5 min)* Fill in the shape table: for each of the five stages write (C, H, W) and the cumulative receptive field; verify against `torchinfo.summary(model, (1, 3, 128, 128))`.
2. *(5 min)* Batch-grid ritual: render 8 augmented training images with labels; tune ColorJitter down if varieties become visually ambiguous; justify ranges in `OBSERVATIONS.md`.
3. *(5 min)* `--overfit-one-batch` with TamrCNN — the engine is imported unchanged from Lab 2. Must reach < 0.05 before proceeding.
4. *(20 min)* Train 15 epochs (AdamW, lr 3e-4, batch 64). Expect ≈ 0.80–0.84 val accuracy. Checkpoint best/last as in Lab 2.
5. *(10 min)* Generate the 9×9 confusion matrix; identify the two most-confused variety pairs and hypothesise why (colour vs texture cues) in `OBSERVATIONS.md`.
6. *(5 min)* Commit: `feat(cnn): TamrCNN baseline — val acc 0.8X`. Record the number: **Module 5 must beat it.**

**Tasks (RNN mini-lab, H5)**
1. *(10 min)* Complete `SensorGRU.forward`; assert the (B, T, F) contract; run the planted `sim-seq-first` variant and record how a transposed input reaches only chance accuracy without crashing.
2. *(15 min)* Train on the sensor-window dataset (5 epochs, with `clip_grad_norm_`); reach ≥ 90% val accuracy across the 3 classes.
3. *(5 min)* Ablate: remove gradient clipping, raise lr ×10, observe the NaN; restore.

**Checkpoints**
- [ ] Shape table matches `torchinfo` exactly (instructor spot-check)
- [ ] Batch grid rendered and augmentation justified
- [ ] CNN self-test < 0.05; val accuracy ≥ 0.80; confusion matrix committed
- [ ] GRU ≥ 0.90 val accuracy with clipping enabled

**Expected output**
```
$ python scripts/train_tamr_cnn.py --epochs 15
epoch 1   train loss 1.842 acc 0.352  |  val loss 1.606 acc 0.446
epoch 8   train loss 0.598 acc 0.792  |  val loss 0.664 acc 0.771
epoch 15  train loss 0.331 acc 0.887  |  val loss 0.548 acc 0.816
best val acc 0.822 @ epoch 14 -> runs/tamr_cnn/best.pt
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `mat1 and mat2 shapes cannot be multiplied` at the head | shape table wrong / missing GAP | recompute stage shapes; AdaptiveAvgPool2d(1) |
| Val acc stuck ~0.45 with healthy train acc | over-aggressive ColorJitter erasing colour cues | tune ranges down; re-render the batch grid |
| Loss NaN at epoch ~1 (GRU) | no gradient clipping + high lr | `clip_grad_norm_(…, 1.0)` |
| GRU at chance (33%) forever | seq-first/batch-first transposition | `batch_first=True` + the shape assert |
| Epoch time > 4 min on GPU | decode bottleneck: `num_workers=0` | workers 4, `pin_memory=True` (full story in M6) |

**Instructor notes.** The shape table (task 1) is where the module's arithmetic becomes muscle memory — check it per pair before allowing training. Task 5's confusion-matrix reading is the first *model-quality* conversation of the course; steer pairs from "more epochs" toward "what cue distinguishes these two varieties, and does our augmentation preserve it?" The recorded baseline number is load-bearing for Module 5's transfer-learning payoff — make every pair write it on the shared leaderboard. The RNN mini-lab is intentionally tightly scoped; resist cohort pressure to extend it — point enthusiasts at SDA-AIE-113.

## Mini Exercises

**Quiz (6 questions)**
1. Output size of a 3×3 conv, stride 2, padding 1 on 128×128? → 64×64.
2. Parameters in `Conv2d(64, 128, 3)` with bias? → 3·3·64·128 + 128 = 73,856.
3. Why do three 3×3 convs beat one 7×7 at equal receptive field? → fewer weights (27C² vs 49C²) + two extra nonlinearities.
4. What does `y = F(x) + x` guarantee about the gradient? → an identity path: ∂y/∂x = ∂F/∂x + I, so gradient never fully attenuates.
5. Which augmentation is *wrong* for Arabic document classification and why? → horizontal flip — mirrored text changes semantics.
6. Why is the additive LSTM cell update the "residual connection in time"? → gradient flows through the + path without repeated matrix multiplication, deferring vanishing.

**Arithmetic drill.** Given a 5-layer stack (3×3 s1 p1 → pool2 → 3×3 s1 p1 → 3×3 s2 p1 → pool2) on 96×96 input: compute final (H, W) and receptive field on paper; verify with `torchinfo`.

**Debugging exercise.** Branch `sim-hwc`: a custom Dataset returns HWC uint8 tensors without `ToTensor()`. The model trains to 30% and plateaus. Find the layout+scale bug from the batch-grid render (the images look wrong in a specific, diagnostic way).

**Design exercise.** Sketch (layers + shape table, no code) a CNN for 32×32 traffic-sign crops for a Riyadh road-survey vehicle, justifying number of stages via receptive field.

**Discussion questions.**
- The packing house offers to buy a 4× higher-resolution camera. Walk through what changes in your architecture, compute cost, and whether variety-grading accuracy plausibly improves.
- When would you still choose a GRU over a small transformer for the pump-telemetry task in 2026? (latency floor, tiny data, edge deployment, engineering simplicity)

## Case Study — PPE Compliance Detection at a Yanbu Industrial Contractor

**Scenario.** An industrial-services contractor at Yanbu deployed a CNN to flag missing hard hats and safety vests on CCTV frames from a fabrication yard. The vendor's model reports 94% accuracy in testing yet misses most violations beyond ~15 metres from the camera; the HSE manager has lost confidence and reverted to manual spot checks.

**Business context.** The yard runs 1,200 workers across shifts; a single reportable head-injury incident triggers a client-mandated stand-down costing ≈ SAR 400k/day. The contractor's engineering team (participants' role) must diagnose the vendor model and specify the fix before the quarterly HSE audit.

**Technical challenge.** Distant workers occupy 20–35 pixels in the 1080p frame. The vendor pipeline resizes full frames to 224×224, shrinking a distant hard hat to ~4 pixels — beneath the effective receptive-field granularity of any classifier and destroyed entirely by the early downsampling stages. The 94% figure came from a test set dominated by near-camera imagery. Additionally, the training augmentation included aggressive `RandomResizedCrop(scale=(0.3, 1.0))`, teaching the model that heavily cropped (i.e., near-camera) views are the norm.

**Constraints.** Cameras cannot be moved (ATEX zoning); inference budget is one edge GPU per four streams at 5 FPS; retraining data is limited to 6,000 labelled frames; any solution must be explainable to HSE auditors who are not ML practitioners.

**Solution approach (facilitate, don't lecture).** (1) Quantify the failure: bucket test accuracy by worker-bounding-box size; the 94% collapses to 38% below 40 pixels — the evidence slide for the auditors. (2) Reframe: full-frame classification is the wrong decomposition; tile the frame into overlapping 256×256 crops (or adopt a detection model — acknowledged as the Specialist-track answer) so distant workers keep usable resolution. (3) Fix the data: stratify train/test by distance bucket; constrain the crop-scale augmentation to match deployment geometry. (4) Verify against the constraint: measure tiles/second on the edge GPU; trade tile overlap against the 5 FPS budget. (5) Ship the honest metric: per-distance-bucket recall, not a single accuracy number.

**Discussion questions.**
1. Connect the failure to this module's arithmetic: at what input resolution does a 20-pixel hard hat survive four stride-2 stages, and what does that imply about resize-first pipelines?
2. Was the vendor's 94% a lie? Distinguish test-set construction failure from model failure, and assign responsibility.
3. Which single evidence artefact (of the ones you produced) does the HSE auditor actually need, and how does that shape your reporting format?
4. The client asks for "at least 99% detection". Draft the two-sentence reply that reframes the request into per-bucket recall targets with a monitoring plan.

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Shape table correctness | Arithmetic fluency | 5/5 stages incl. receptive field | instructor spot-check vs torchinfo |
| TamrCNN val accuracy (15 epochs) | Learning | ≥ 0.80 | engine output; leaderboard entry |
| Self-test on TamrCNN | Pipeline correctness | < 0.05 in ≤ 300 steps | `--overfit-one-batch` |
| Confusion-matrix analysis | Model reading | top-2 confused pairs identified with plausible cue hypothesis | OBSERVATIONS.md review |
| SensorGRU val accuracy | Sequence learning | ≥ 0.90 (3-class) | mini-lab output |
| Epoch time (GPU, batch 64, workers 4) | Efficiency | ≤ 90 s | timed run |

**Example benchmark table (filled during lab):**

| Model | Params | Val acc | Epoch time | Notes |
|---|---|---|---|---|
| MLP on flattened 128² (reference, provided) | 12.9 M | 0.51 | 41 s | no spatial prior — the point |
| TamrCNN width 16 (CPU cohort) | 0.42 M | 0.78 | 6 min CPU | acceptable fallback |
| TamrCNN width 32 (reference) | 1.66 M | 0.82 | 74 s | **the number M5 must beat** |
| TamrCNN + 1 residual block (stretch) | 1.96 M | 0.83 | 79 s | mechanics demo |

## Required Visuals and Training Assets

### Diagrams
1. **Convolution mechanics, annotated** — *Purpose:* one image that carries kernel/stride/padding/channels. *Elements:* 8×8 input grid with a 3×3 kernel shown at three slide positions; padding ring dashed; one output cell traced back to its input patch; channel depth drawn as stacked sheets. *Style:* isometric grid, two-colour, English labels with Arabic subtitles.
2. **TamrCNN stage map** — *Purpose:* the lab's shape table as a picture. *Elements:* five stage blocks with (C, H, W) at each boundary, receptive-field number growing beneath, GAP + linear head at the end; parameter count per stage. *Style:* left-to-right pipeline, widths proportional to activation volume.
3. **Receptive-field growth cone** — *Purpose:* make "what one output sees" visceral. *Elements:* one unit in the final map with its cone traced back through all stages onto the input date image; side ruler in pixels. *Style:* layered transparency overlay on a real Tamr-9 photo.
4. **Residual block gradient highway** — *Purpose:* why deep nets train. *Elements:* F(x) branch vs identity skip; red backward arrows showing the "+ I" path unattenuated; a 34-layer plain-vs-residual training-loss inset. *Style:* circuit-style block diagram.
5. **RNN unrolled in time** — *Purpose:* weight sharing across time; where BPTT decays. *Elements:* 6 unrolled steps with the same W_h labelled at each arrow; gradient arrow thinning per step backward; LSTM cell inset with the additive c-path highlighted. *Style:* horizontal timeline, decay shown by arrow weight.

### Images (screenshots)
1. **Batch-grid ritual output**: *why:* the mandatory pre-training check; *content:* 8 augmented Tamr-9 crops with labels, one deliberately over-jittered example marked.
2. **torchinfo summary of TamrCNN**: *why:* shape-table verification reference; *content:* full layer list with output shapes and param counts.
3. **9×9 confusion matrix heatmap**: *why:* the model-reading exercise anchor; *content:* matrix with the two confused variety pairs circled.
4. **First-layer filters after training**: *why:* the feature-hierarchy claim, evidenced; *content:* 32 learned 3×3 kernels showing edge/colour structure.
5. **GRU NaN moment**: *why:* exploding-gradient recognition; *content:* loss log with the NaN step and the grad-norm spike above it.

### Simulations
1. **The MLP that couldn't** — *Setup:* provided script trains the 12.9 M-param MLP on Tamr-9. *Expected behaviour:* plateaus ~0.51 while the 1.7 M-param CNN reaches 0.82. *Learning objective:* priors beat parameters; architecture is data-structure knowledge.
2. **Augmentation poison** — *Setup:* branch `sim-vflip-digits` adds vertical flips to a digit task. *Expected behaviour:* 6/9 confusion appears; accuracy caps. *Learning objective:* augmentations are semantic claims about labels.
3. **Seq-first silent failure** — *Setup:* branch `sim-seq-first` feeds (T, B, F) into a batch_first GRU. *Expected behaviour:* trains without error at chance accuracy. *Learning objective:* shape asserts at module boundaries; silent bugs beat loud ones.

### Interactive Activities
- **Human convolution (15 min):** a 6×6 grid taped on the floor/wall, one team is the 3×3 kernel and physically slides with stride 1 then stride 2, calling out output positions; padding added with sticky notes; class predicts output size before each pass.
- **Receptive-field auction (10 min):** instructor shows a discriminative cue (date-skin wrinkle patch, ~40 px); teams bid the *minimum* architecture (stages/kernels) whose RF covers it; cheapest correct bid wins.
- **Augmentation courtroom (10 min):** each pair is assigned one transform and must defend it for Tamr-9 in 60 seconds; class votes keep/tune/reject; verdicts go into the lab's transform config.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Tamr-9 | Course bundle (from M2) | JPEG folders + splits.json | ~9k images, 9 classes, 128² crops | CNN training — the golden thread |
| `conveyor_vibration.npz` | Synthetic generator calibrated on public bearing-fault datasets | NumPy archive | 6k windows × 200 steps × 3 axes | GRU mini-lab |
| MLP-baseline script | Course repo | Python | — | The priors-beat-parameters demo |

### Demo Requirements
- **Instructor demo:** live filter visualisation on the trained TamrCNN — first-layer kernels plus feature-map activations for one Sukkari image walked through all five stages; under 6 minutes.
- **Student demo:** one pair defends their confusion-matrix hypothesis to the class; a second pair shows the seq-first failure and its one-line fix.
- **Expected outputs:** every pair's baseline number on the leaderboard by end of Day 2 — Module 5's transfer-learning comparison depends on it.

---

# Module 4 — Regularisation, Normalisation, and Optimisation

## Module Overview

**Purpose.** Modules 1–3 got models *training*; Module 4 gets them *behaving*. Real training runs overfit, oscillate, stall, and diverge — and the difference between a practitioner and a script-runner is a disciplined response: read the learning curves first, name the failure, apply the *one* matching intervention, and measure it with an ablation. This module delivers the stabilisation toolkit — weight decay, dropout, label smoothing, augmentation-as-regularisation, early stopping, BatchNorm and its siblings, learning-rate schedules, gradient clipping — and, more importantly, the decision procedure for when each applies.

**Business relevance.** Tuning is where GPU budgets die. Teams without a diagnostic method re-run "one more experiment" for weeks; teams with one converge in days. In Saudi enterprises this is now a governance question too: model-risk reviews at SAMA-regulated institutions ask *why* a hyperparameter was chosen, and "the ablation table says so" is an acceptable answer where "the intern felt it" is not. The ablation discipline taught here is the direct precursor to Module 6's experiment tracking — first learn to change one thing at a time, then learn to log it.

**Industry use cases.**
- A Riyadh health-tech startup trains a skin-condition classifier on 4,200 images; without regularisation discipline it memorises the training set by epoch 6 and fails clinical validation.
- A logistics firm's demand-forecast retraining oscillates weekly between good and terrible models; a proper LR schedule and early-stopping criterion make retraining unattended and boring.
- An Aramco-ecosystem vendor must justify every training decision in a model card for procurement review; the ablation table is the evidence backbone.

**Expected competencies.** After this module a participant can read learning curves and name the regime (underfit/overfit/unstable/plateau), apply and correctly order the regularisation toolkit, explain BatchNorm's train/eval duality and its batch-size failure mode, choose and wire LR schedules (warmup, cosine, OneCycle) with an LR range test, and produce a one-variable-at-a-time ablation table that attributes every improvement.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Diagnose underfitting, overfitting, and instability from train/val learning curves | LO3, LO4 |
| 4.2 | Apply weight decay, dropout, label smoothing, augmentation, and early stopping with correct placement and typical ranges | LO4 |
| 4.3 | Explain BatchNorm mechanics (train vs eval), its failure modes, and when to use LayerNorm/GroupNorm instead | LO4 |
| 4.4 | Select and implement learning-rate schedules (warmup, cosine, OneCycle) and run an LR range test | LO3, LO4 |
| 4.5 | Design one-variable-at-a-time ablations that attribute performance changes to specific interventions | LO4, LO6 |

## Technical Content

### 1. Learning curves: the four regimes and their signatures

Every tuning decision starts with the same two curves — train loss and val loss per epoch — and the honest question: *which regime am I in?*

| Regime | Train loss | Val loss | First interventions |
|---|---|---|---|
| **Underfitting** | high, still falling or flat-high | high, tracks train | bigger/deeper model, train longer, raise lr, check pipeline (self-test!) |
| **Overfitting** | falling toward 0 | falls, then *rises* — the gap opens | more data/augmentation, weight decay, dropout, early stopping |
| **Instability** | oscillates or spikes/NaN | erratic | lower lr, warmup, gradient clipping, check batch size vs BN |
| **Plateau** | flat at a non-trivial value | flat | LR schedule (it's often just time to decay), revisit architecture |

Two rules that save cohorts weeks of confusion. First, **some train/val gap is normal and healthy** — the crime is a *growing* gap while val degrades, not the gap's existence. Second, **the val curve picks the model, the test set never does**: early stopping *is* model selection on val (keep `best.pt` by val metric — already built into the Lab 2 engine), and every peek at test for a tuning decision silently converts test into a second validation set. Tamr Vision's sealed test split exists to make this rule physical: the labels are not even on the participants' machines.

Also name the deep-learning wrinkle honestly: classical bias-variance intuition ("bigger model = more overfitting") is a guide, not a law — modern over-parameterised networks with strong regularisation and enough data often generalise *better* as they grow. The practical takeaway stands: diagnose from curves, not from parameter counts.

### 2. The regularisation toolkit, in order of application

Teach the toolkit as a **priority order**, because participants otherwise apply everything at once and learn nothing:

1. **More/better data and augmentation** — the highest-leverage regulariser, already half-built in Module 3. Augmentation adds invariance knowledge; check its aggressiveness against the batch-grid ritual before blaming anything else.
2. **Weight decay** — penalise weight magnitude, biasing toward simpler functions. Critical modern detail: in Adam, L2-in-the-loss and true weight decay differ; **AdamW decouples decay from the adaptive step** and is the course default (`weight_decay=0.01–0.05` for CNNs). Norm layers and biases are conventionally excluded from decay — show the param-groups pattern once.
3. **Dropout** — randomly zero activations at rate p during training (train mode only — Module 2's eval discipline, now with mechanism). Forces redundant representations; ensemble interpretation optional. Modern placement: in classifier heads (p = 0.2–0.5); *not* interleaved with BatchNorm in conv stacks — the variance-shift interaction between the two is a classic silent degrader.
4. **Label smoothing** — targets of 0.9/0.0125… instead of 1/0 (`label_smoothing=0.1` in `nn.CrossEntropyLoss`). Stops the "infinitely confident logits" chase, improves calibration — relevant when Tamr Vision's confidence thresholds route borderline fruit to human graders.
5. **Early stopping** — stop when val hasn't improved for `patience` epochs; with best-checkpointing already in the engine, this is a loop condition, not new machinery.

### 3. Normalisation layers: BatchNorm's power and its fine print

**BatchNorm** normalises each channel to zero-mean/unit-variance *across the batch*, then re-scales with learned γ, β. Effects: dramatically smoother optimisation (tolerates ~10× higher lr), some regularisation from batch noise, and reduced sensitivity to initialisation — it is in every modern CNN (TamrCNN included, on credit since Module 3; the debt is paid here).

The fine print is where production bugs live:

- **Two personalities.** Train mode: normalise with *batch* statistics, update running averages. Eval mode: use *running* statistics, frozen. This is exactly why Module 2 drilled `model.train()/eval()` — a model evaluated in train mode leaks batch statistics; a model fine-tuned in eval mode never adapts its stats (both `sim-` branches exist).
- **Small-batch collapse.** Batch statistics from 2–4 samples are noise; BN-heavy models degrade badly at tiny batch sizes (the case study turns on this). Alternatives that don't cross the batch dimension: **LayerNorm** (per-sample, across features — the transformer default, and what SDA-AIE-113 will assume), **GroupNorm** (per-sample, channel groups — the drop-in CNN fix for small batches, e.g. `GroupNorm(8, C)`).
- **Ordering:** the course convention is Conv → BN → ReLU (as in TamrCNN); `bias=False` on the conv because BN's β subsumes it.

### 4. Learning-rate schedules: the highest-leverage hyperparameter, scheduled

A constant lr is almost never optimal: early training wants a large lr to traverse the landscape; late training wants a small one to settle. The standard repertoire:

- **Warmup** (linear 0 → lr over 1–5 epochs): protects the fragile early phase — random init + adaptive optimisers + BN statistics all stabilising at once. Mandatory reflex for fine-tuning (Module 5) and large-batch work (Module 6).
- **Cosine annealing** (`CosineAnnealingLR`): smooth decay to ~0 over the run; the modern default when the epoch budget is known. Warmup + cosine is the course's standard recipe.
- **OneCycle** (`OneCycleLR`): up then down within a single run, stepped **per batch, not per epoch** — the classic wiring bug, planted in Lab 4. Excellent for short budgets like classroom labs.
- **ReduceLROnPlateau**: reactive ÷10 when val stalls; fine for unattended retraining jobs; note `scheduler.step(val_loss)` takes an argument, unlike the others.
- **The LR range test**: sweep lr exponentially over a few hundred steps, plot loss vs lr, pick ~10× below the divergence point. Ten minutes that replaces a day of guessing; implemented in the lab as `scripts/lr_finder.py`.

Scheduler wiring in the engine follows Module 2's liturgy: per-epoch schedulers step after the epoch; OneCycle steps after every `optimizer.step()`. Log the current lr every epoch — a schedule that isn't logged isn't real (Module 6 makes this automatic).

### 5. Gradient clipping and the ablation discipline

**Clipping** (`clip_grad_norm_(params, 1.0)`) rescales the gradient when its norm exceeds a threshold — a seatbelt against loss spikes from rare bad batches, mandatory for RNNs (Module 3), cheap insurance elsewhere. Log the pre-clip norm: a *rising* clip frequency is an early instability alarm.

The **ablation discipline** converts the toolkit from folklore into evidence: start from the recorded baseline (Lab 3's number), change exactly one variable per run, use identical seeds and splits, and record every run in a table — configuration, val metric, delta vs baseline. Two honest caveats: interventions interact (weight decay's best value shifts under a different schedule — ablate the big rocks first: lr and schedule, then decay, then dropout), and single-seed deltas under ~0.5 pp are noise (run 3 seeds before believing small effects). The ablation table produced in Lab 4 is the direct ancestor of the W&B comparison dashboard in Module 6 — same discipline, better tooling.

### 6. Common mistakes & production considerations

1. **Shotgun tuning** — changing lr, decay, dropout, and augmentation in one run; the improvement is real but unattributable, so the next project relearns everything. The ablation table is the antidote and the deliverable.
2. **OneCycle stepped per epoch** — lr crawls through a tiny fraction of its schedule; training underperforms mysteriously. Planted in Lab 4; diagnosed by *plotting the actual lr* per step.
3. **Dropout/BN interleaved in conv stacks** — variance shift between train and eval quietly costs accuracy; keep dropout in the head.
4. **Weight decay on norm parameters and biases** — over-regularises the wrong parameters; use param groups.
5. **Early stopping with patience 1–2** — stops at the first noisy dip; val curves are noisy, patience 5–10 for short runs.
6. **Tuning on test** — every "just checking" peek erodes the only honest number left; institutionally, this is why Tamr Vision's test labels live with the instructor.

Production considerations: retraining pipelines must encode the *schedule*, not just the lr (a config that says `lr=0.001` is incomplete without `schedule=cosine, warmup=2`); calibration matters when thresholds route decisions to humans (label smoothing + a reliability check before shipping confidence scores); and regulators reviewing model updates read ablation evidence — archive the table with the model artefact, a habit Module 6 automates with W&B.

## Code Examples

### Param groups, scheduler, and clipping wired into the engine

```python
# src/tamr_vision/optim.py
"""Optimiser/scheduler factory for Tamr Vision.

Conventions:
- AdamW with decay EXCLUDED from norm layers and biases (param groups)
- warmup + cosine as the course-standard schedule
- per-epoch vs per-batch stepping is the caller's contract: OneCycle steps
  per BATCH — the classic wiring bug is stepping it per epoch (sim-onecycle).
"""
import torch
import torch.nn as nn


def make_param_groups(model: nn.Module, weight_decay: float = 0.05) -> list[dict]:
    decay, no_decay = [], []
    for name, p in model.named_parameters():
        if not p.requires_grad:
            continue
        # biases and all norm-layer params (weight=gamma, bias=beta) skip decay
        if p.ndim == 1 or name.endswith(".bias"):
            no_decay.append(p)
        else:
            decay.append(p)
    return [{"params": decay, "weight_decay": weight_decay},
            {"params": no_decay, "weight_decay": 0.0}]


def make_optimizer_and_scheduler(model: nn.Module, lr: float, epochs: int,
                                 warmup_epochs: int = 2, weight_decay: float = 0.05):
    optimizer = torch.optim.AdamW(make_param_groups(model, weight_decay), lr=lr)
    warmup = torch.optim.lr_scheduler.LinearLR(
        optimizer, start_factor=0.01, total_iters=warmup_epochs)
    cosine = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer, T_max=epochs - warmup_epochs)
    scheduler = torch.optim.lr_scheduler.SequentialLR(
        optimizer, [warmup, cosine], milestones=[warmup_epochs])
    return optimizer, scheduler   # per-EPOCH stepping; log lr every epoch
```

### The LR range test

```python
# scripts/lr_finder.py
"""LR range test: sweep lr exponentially over ~300 steps, record loss,
pick ~10x below the divergence point. Ten minutes that replaces a day.

Run:  python scripts/lr_finder.py --min-lr 1e-6 --max-lr 1 --steps 300
"""
import math

import torch


def lr_range_test(model, loader, criterion, device,
                  min_lr: float = 1e-6, max_lr: float = 1.0,
                  steps: int = 300) -> list[tuple[float, float]]:
    model.train()
    optimizer = torch.optim.AdamW(model.parameters(), lr=min_lr)
    gamma = (max_lr / min_lr) ** (1 / steps)      # exponential sweep
    history, it = [], iter(loader)
    for step in range(steps):
        try:
            x, y = next(it)
        except StopIteration:
            it = iter(loader)
            x, y = next(it)
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()
        loss = criterion(model(x), y)
        loss.backward()
        optimizer.step()
        lr = optimizer.param_groups[0]["lr"]
        history.append((lr, loss.item()))
        if not math.isfinite(loss.item()) or loss.item() > 4 * history[0][1]:
            break                                  # diverged — we have our answer
        for g in optimizer.param_groups:
            g["lr"] *= gamma
    return history   # plot log-lr vs loss; choose ~10x below the cliff
```

### Regularised training config and the ablation runner

```python
# scripts/ablate.py
"""One-variable-at-a-time ablation runner. Every run: same seed, same
splits, ONE config delta vs baseline. Appends to runs/ablation.csv —
the table IS the deliverable (and Module 6 replaces this CSV with W&B).
"""
import csv
import dataclasses
from pathlib import Path


@dataclasses.dataclass(frozen=True)
class TrainConfig:
    lr: float = 3e-4
    epochs: int = 15
    weight_decay: float = 0.05
    dropout: float = 0.0          # head dropout; NOT in conv stacks (BN interaction)
    label_smoothing: float = 0.0
    schedule: str = "warmup_cosine"
    clip_norm: float | None = 1.0
    seed: int = 42

BASELINE = TrainConfig()

ABLATIONS = {                      # each run changes EXACTLY ONE field
    "baseline": BASELINE,
    "wd_0": dataclasses.replace(BASELINE, weight_decay=0.0),
    "dropout_0.3": dataclasses.replace(BASELINE, dropout=0.3),
    "smooth_0.1": dataclasses.replace(BASELINE, label_smoothing=0.1),
    "no_schedule": dataclasses.replace(BASELINE, schedule="constant"),
    "lr_3e-3": dataclasses.replace(BASELINE, lr=3e-3),
}


def record(name: str, cfg: TrainConfig, val_acc: float, path=Path("runs/ablation.csv")):
    new = not path.exists()
    with open(path, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["run", *dataclasses.asdict(cfg).keys(), "val_acc"])
        w.writerow([name, *dataclasses.asdict(cfg).values(), f"{val_acc:.4f}"])
```

## Hands-on Lab 4 — Rescue the Failing Run

| | |
|---|---|
| **Objective** | Take a deliberately mis-configured Tamr-9 training setup, diagnose each defect from its curves, fix defects one at a time, and produce an ablation table attributing every recovered point of accuracy |
| **Duration** | 50 min (Day 3 H3), building on H1–H2 theory |
| **Setup** | `git checkout lab4-start` — ships `config_broken.yaml` and pre-generated learning curves of the broken run |

**The broken config (participants discover, not told):** lr 10× too high with no warmup; OneCycle stepped per epoch; dropout 0.5 inside conv blocks; weight decay applied to BN params; no augmentation; patience-1 early stopping that halts at epoch 3.

**Tasks**
1. *(10 min)* **Diagnose before touching.** From the provided curves and logs alone, write a defect list in `OBSERVATIONS.md` with the regime each symptom indicates (instability spike → lr/warmup; lr plot flat-low → scheduler wiring; train/val both mediocre with slow train → conv dropout…). Minimum 4 of 6 found before editing.
2. *(25 min)* **Fix one at a time.** For each fix: one config change, one run (8-epoch budget, width 16 for speed), one row in `ablation.csv` via `scripts/ablate.py`. Order matters — big rocks first (lr + warmup, scheduler wiring), then placement bugs, then regularisation tuning.
3. *(5 min)* Run the LR range test on the fixed setup; confirm your final lr sits ~10× below the cliff; attach the plot.
4. *(5 min)* Full 15-epoch run with the rescued config; target ≥ baseline + 2 pp (≈ 0.84).
5. *(5 min)* Commit: `fix(training): rescued run — ablation attached`. Update the leaderboard.

**Checkpoints**
- [ ] Defect list: ≥ 4/6 identified from evidence before edits
- [ ] `ablation.csv`: ≥ 5 rows, one variable per row, deltas computed
- [ ] LR-range plot with chosen lr marked
- [ ] Final val accuracy ≥ 0.84 (width-32 rerun or scaled expectation for width-16 cohorts)

**Expected output**
```
$ python scripts/ablate.py --run all --epochs 8
run              delta_vs_broken   val_acc
broken           —                 0.412
fix_lr_warmup    +0.229            0.641
fix_onecycle     +0.078            0.719
fix_dropout_pos  +0.041            0.760
fix_wd_groups    +0.012            0.772
add_augment      +0.048            0.820
$ python scripts/train_tamr_cnn.py --config config_rescued.yaml --epochs 15
best val acc 0.847 @ epoch 13
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| "Fixed" run still spikes at epoch 1 | warmup missing though lr lowered | 2-epoch linear warmup |
| lr plot shows sawtooth microscopic range | OneCycle per-epoch stepping persists | step per batch, or switch to warmup+cosine |
| Ablation deltas don't sum to total gain | interactions between fixes | expected — discuss; order by marginal gain, don't force additivity |
| Two runs with same config differ by 1 pp | seed noise at 8-epoch budget | 3 seeds for small effects; report mean |
| Early stopping fires at epoch 4 again | patience still 1 | patience 5; keep best.pt semantics |

**Instructor notes.** This is the course's diagnostic capstone-in-miniature and the most transferable hour of the week — protect it at full length (mirror of the template's timing rule). Enforce the diagnose-first discipline hard: pairs who start editing configs in the first ten minutes must be sent back to the curves. The non-additivity of deltas (troubleshooting row 3) is a feature — it seeds the best discussion of the day. Fast finishers: 3-seed variance study on their smallest ablation delta, reported as mean ± range.

## Mini Exercises

**Quiz (6 questions)**
1. Train loss 0.05, val loss rising since epoch 7. Regime and first two interventions? → overfitting; augmentation/weight decay + early stop at best val.
2. Why AdamW rather than Adam + L2-in-the-loss? → decoupled decay: L2 in the loss gets rescaled by Adam's adaptive step; AdamW applies true decay.
3. BatchNorm at batch size 2 degrades badly — why, and what's the drop-in fix? → batch statistics are noise at n=2; GroupNorm.
4. Which scheduler steps per batch, and what happens when it's stepped per epoch? → OneCycle; lr traverses a sliver of its cycle, run underperforms silently.
5. What does an LR range test output, and how do you pick from it? → loss vs lr sweep; pick ~10× below the divergence cliff.
6. Your ablation shows +0.3 pp from label smoothing, single seed. Believe it? → no — under noise threshold; 3 seeds first.
7. Why exclude BN γ/β and biases from weight decay? → they set scale/shift, not function complexity; decaying them over-regularises the wrong thing.

**Curve-reading drill.** Six anonymised train/val curve pairs (provided deck); for each, 60 seconds to name the regime and one intervention. Reuses Module 1's flash-round format at higher difficulty.

**Config review exercise.** A one-page YAML from a fictional colleague: lr 0.01 constant, dropout 0.6 everywhere, decay 0.3, patience 1, no warmup, no augmentation. Write the review comment ranking the three changes to make *first* and the evidence you'd demand for the rest.

**Discussion questions.**
- Your ablation table shows augmentation helping (+4.8 pp) far more than dropout (+0.4). Your teammate wants to keep dropout "because it's standard". Adjudicate with evidence and cost.
- A model-risk reviewer at a bank asks: "why is your learning rate 3e-4?" Contrast the answer this module equips you to give with the answer most teams give.

## Case Study — Stabilising a Skin-Lesion Triage Model at a Riyadh Health-Tech Startup

**Scenario.** A Riyadh health-tech startup building a tele-dermatology triage tool trains a lesion classifier on 4,200 clinician-labelled images from two partner hospitals. Training accuracy reaches 99% by epoch 6; validation peaks at 71% then decays. A second attempt with heavy dropout everywhere and decay 0.3 undershoots at 62% train/61% val. The team has burned five weeks alternating between the two failure modes, and their clinical-validation deadline with the pilot hospital is in three weeks.

**Business context.** The pilot agreement requires a documented, frozen model with ≥ 80% balanced accuracy on the hospital's held-out set before any patient-facing use. Every week of delay pushes the pilot behind a hospital-committee review cycle that meets monthly. Compute is one workstation GPU — small batches are a fact of life.

**Technical challenge.** The team oscillates between the overfitting and underfitting regimes because each response was a *blanket* intervention rather than a diagnosis. Compounding defects: batch size 8 with BatchNorm (noisy statistics), no augmentation despite obvious invariances (rotation-safe dermoscopy crops), decay applied uniformly including norm layers, constant lr with no schedule, and model selection by *final-epoch* rather than best-val checkpoint.

**Constraints.** 4,200 images and no near-term prospect of more (clinician labelling is the bottleneck); batch size capped at 8 by GPU memory; the clinical reviewer requires an auditable record of what was changed and why; class imbalance (three rare lesion types) means balanced accuracy, not raw accuracy, is the contract metric.

**Solution approach (facilitate, don't lecture).** (1) Curves first: regime named per attempt, defect list written — the five-week oscillation reframed as two undiagnosed regimes. (2) Structural fixes before knobs: GroupNorm for batch-8, best-val checkpointing, stratified splits re-verified. (3) Data leverage first (toolkit order): dermoscopy-safe augmentation (rotations, flips, mild colour) — the single biggest gain. (4) Then the knobs, one at a time, ablation table growing per run: warmup+cosine, decay 0.05 with param groups, head-only dropout 0.3, label smoothing for calibrated triage thresholds. (5) Result trajectory (representative): 71% → 76% (augmentation) → 79% (schedule) → 81.5% (decay/dropout tuning), balanced. The ablation table goes into the clinical-validation dossier as-is.

**Discussion questions.**
1. The team's first instinct after the 99/71 run was "get more data". Given the constraint, rank the module's toolkit by expected value *for this case* and defend the top pick.
2. Why is BatchNorm specifically dangerous at batch size 8 *in a clinical setting* — connect the train/eval statistics gap to a silent deployment-time behaviour change.
3. The committee asks whether the model is "done improving". Use the ablation table to answer without overclaiming.
4. What in this module's discipline transfers directly to the dossier requirements of a SAMA or SFDA-style review, and what additional evidence would Module 6's tooling add?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Defect identification (broken config) | Diagnosis | ≥ 4/6 from evidence, pre-edit | OBSERVATIONS.md timestamped vs first commit |
| Rescued val accuracy (15 epochs) | Outcome | ≥ 0.84 (≥ baseline + 2 pp) | leaderboard entry |
| Ablation table quality | Discipline | ≥ 5 single-variable rows with deltas | ablation.csv review |
| LR range test | Method | plot produced; chosen lr ~10× below cliff | attached plot |
| Curve-reading drill | Fluency | ≥ 5/6 regimes named correctly | drill score sheet |
| Regularisation placement | Correctness | dropout in head only; decay param-grouped | config review |

**Example benchmark table (filled during lab):** the `ablation.csv` output shown in the lab's expected output serves as this module's benchmark table — every pair's version is committed and compared on the leaderboard.

## Required Visuals and Training Assets

### Diagrams
1. **The four-regime curve atlas** — *Purpose:* the module's diagnostic anchor. *Elements:* 2×2 grid of train/val curve pairs (underfit, overfit, unstable, plateau), each annotated with its signature and first interventions; printable as the participants' desk reference. *Style:* small-multiples line charts, consistent axes, English labels with Arabic subtitles.
2. **Regularisation toolkit priority ladder** — *Purpose:* order of application. *Elements:* five rungs (data/augmentation → weight decay → dropout → label smoothing → early stopping) with typical ranges and placement notes per rung. *Style:* vertical ladder infographic.
3. **BatchNorm's two personalities** — *Purpose:* the train/eval duality. *Elements:* split-panel: train mode computing batch stats + updating running averages; eval mode reading frozen running stats; a red mismatch arrow showing the batch-size-2 noise case; LayerNorm/GroupNorm inset showing which axes each normalises over. *Style:* split panel with axis-shading cubes (the N/C/HW cube convention).
4. **Schedule gallery** — *Purpose:* shape recognition. *Elements:* lr-vs-step curves for constant, step decay, warmup+cosine, OneCycle, ReduceLROnPlateau; the per-batch vs per-epoch OneCycle bug shown as the sawtooth-sliver overlay. *Style:* five aligned sparkline panels.
5. **Ablation workflow loop** — *Purpose:* the discipline as a process. *Elements:* baseline → one change → run (fixed seed/splits) → record row → compare → next; a forbidden "shotgun" path crossed out. *Style:* cyclic flowchart.

### Images (screenshots)
1. **The broken run's curves + lr plot**: *why:* Lab 4's diagnostic starting material; *content:* loss spike at epoch 1, flat-sliver lr plot, early-stop truncation visible.
2. **LR range test plot**: *why:* method reference; *content:* loss vs log-lr with the cliff and the chosen lr marked.
3. **ablation.csv rendered as a table**: *why:* the deliverable's expected shape; *content:* six rows with deltas, one variable changed per row highlighted.
4. **Before/after rescued curves**: *why:* the module's payoff image; *content:* broken vs rescued val curves on shared axes.

### Simulations
1. **OneCycle-per-epoch** — *Setup:* branch `sim-onecycle`. *Expected behaviour:* run trains but underperforms ~8 pp; only the lr-vs-step plot reveals why. *Learning objective:* log and plot the actual lr; schedulers have stepping contracts.
2. **BN at batch size 2** — *Setup:* branch `sim-bn-tiny-batch` trains TamrCNN at batch 2. *Expected behaviour:* erratic val metrics, train/eval gap; swapping to GroupNorm stabilises. *Learning objective:* BN's batch-statistics dependency and its drop-in alternative.
3. **The patience-1 stopper** — *Setup:* early stopping with patience 1 on a noisy val curve. *Expected behaviour:* halts at epoch 3–4, 6+ pp below achievable. *Learning objective:* val noise vs signal; patience as a statistical guard.

### Interactive Activities
- **Regime triage rounds (15 min):** the curve-atlas format live — six anonymised curve pairs, pairs vote regime + intervention on cards, instructor reveals; running leaderboard score.
- **Fix-order debate (10 min):** given the Lab 4 defect list, teams commit to a fix order and defend it; compare against marginal-gain results after the lab — whose order was most efficient?
- **The knob auction (10 min):** teams get a budget of 3 "runs" to spend on the toolkit for a described scenario (small data, batch 8, deadline); best expected-value spend wins; connects directly to the case study.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Tamr-9 | Course bundle (unchanged) | JPEG + splits.json | ~9k images | All ablation runs — comparability with the M3 baseline |
| Broken-run artefacts | Course repo (`lab4-start`) | YAML + PNG curves + logs | — | Diagnosis-before-edit material |
| Curve-atlas drill deck | Course handout | PNG deck | 6 pairs | Regime-reading drill |

### Demo Requirements
- **Instructor demo:** the LR range test live on TamrCNN — sweep, cliff, pick, and a 3-epoch confirmation run; under 8 minutes total.
- **Student demo:** one pair walks the class through their ablation table, defending one non-obvious delta; class challenges attribution.
- **Expected outputs:** every pair's rescued config and ablation.csv committed by end of Day 3 H3 — Module 5 fine-tunes on top of the rescued recipe.

---

# Module 5 — Transfer Learning and Pretrained Models

## Module Overview

**Purpose.** Almost nobody in industry trains vision models from scratch anymore, and after this module participants will know exactly why — because they will beat three days of their own from-scratch work in twenty minutes of fine-tuning. Transfer learning reuses representations learned on massive datasets (ImageNet's 1.28 M images) as the starting point for new tasks, converting "we don't have enough data" from a project-killer into a routine engineering condition. The module covers the two canonical recipes (feature extraction and fine-tuning), the preprocessing contracts that pretrained weights impose, and the professional hygiene of sourcing models from torchvision and the Hugging Face Hub — model cards, licences, and pinned revisions.

**Business relevance.** Transfer learning is the single highest-ROI technique in applied deep learning: it cuts data requirements by 10–100×, training time by similar factors, and it is the delivery mechanism for nearly every commercial vision and NLP system. For Saudi organisations, the labelled-data constraint is usually the binding one — Arabic documents, local imagery, domain-specific defects have no giant public datasets — so the ability to adapt pretrained models to small local datasets *is* the ability to do applied AI here. The licensing and provenance skills matter equally: a model with an unusable licence or unverifiable origin fails procurement, no matter its accuracy.

**Industry use cases.**
- The Qassim packing house (golden thread): a ResNet pretrained on ImageNet fine-tuned on 9k date images beats the from-scratch CNN by a wide margin — with less training.
- A conservation team at a Saudi royal reserve classifies camera-trap wildlife from a few hundred images per species — impossible from scratch, routine with a pretrained backbone.
- A ministry's document-intake system adapts a pretrained vision model to classify Arabic form types from 300 examples per class, clearing procurement because every upstream model licence and revision is documented.

**Expected competencies.** After this module a participant can choose between feature extraction and fine-tuning based on dataset size and domain gap, load torchvision backbones with their weights and *matching preprocessing transforms*, replace and train classification heads, apply discriminative learning rates with warmup for stable fine-tuning, evaluate models from the Hugging Face Hub for licence and provenance, and pin model revisions for reproducibility.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Explain why ImageNet features transfer and predict when transfer will fail (domain gap, layer specificity) | LO1, LO5 |
| 5.2 | Implement feature extraction: frozen backbone, new head, correct BN handling | LO5 |
| 5.3 | Implement full fine-tuning with discriminative learning rates and warmup | LO3, LO4, LO5 |
| 5.4 | Honour the preprocessing contract of pretrained weights (input size, normalisation) | LO5 |
| 5.5 | Source models from the Hugging Face Hub with licence review and pinned revisions | LO5, LO6 |

## Technical Content

### 1. Why transfer works — and when it doesn't

Module 3 showed the feature hierarchy: edges → textures → parts → objects. The transfer insight is that the *early and middle* rungs of that ladder are largely **task-agnostic**: edge detectors and texture filters learned on ImageNet's dogs and cars are the same ones a date-variety classifier needs. Only the top of the network — the layers that compose parts into *ImageNet's* categories — is task-specific. So: keep the generic bottom, replace the specific top, and let the small local dataset spend its information budget only on what is genuinely new.

The corollary is the **layer-specificity gradient**: transferability decays with depth. This predicts the failure modes. Transfer weakens when the *low-level statistics* of the target domain differ from natural photographs — X-ray, ultrasound, spectrograms, seismic sections — because then even the early features mismatch; it still usually beats random initialisation, but expect to fine-tune deeper and gain less. Give participants the two-axis decision picture: **dataset size × domain gap**. Small data + similar domain → feature extraction. Large data + similar domain → fine-tune. Small data + far domain → fine-tune carefully (strong regularisation, Module 4's toolkit) and manage expectations. Large data + far domain → pretraining helps least; from-scratch becomes defensible.

Vocabulary to anchor: the pretrained network minus its classifier is the **backbone**; its output vector is an **embedding**; the new classifier is the **head**. This vocabulary carries directly into every Specialist module — and into the modern *foundation-model* framing, where the same pattern (giant pretrained model + light adaptation) is the organising idea of the entire field. Say this explicitly: fine-tuning a ResNet today is the same motion as adapting an LLM in SDA-AIE-113 — this module is where the pattern is learned cheaply.

### 2. Recipe 1 — feature extraction: the frozen backbone

Freeze everything, replace the head, train only the head:

1. Load backbone with weights (`ResNet50_Weights.IMAGENET1K_V2`).
2. `for p in model.parameters(): p.requires_grad_(False)` — Module 2's graph-membership control, now at scale.
3. Replace the head: `model.fc = nn.Linear(model.fc.in_features, 9)` — the new layer's fresh parameters have `requires_grad=True` by default.
4. Train with the Module 2 engine, passing only trainable params to the optimiser.

Two subtleties that separate correct implementations from lucky ones. **BatchNorm in a frozen backbone:** freezing `requires_grad` stops *gradient* updates but train mode still updates BN *running statistics* — silently shifting the "frozen" backbone's behaviour toward the small target dataset's statistics with every epoch. The clean policy for feature extraction: keep BN layers in eval mode during training (`model.backbone.eval()` inside the train loop, or set BN modules individually). This is Module 2's train/eval discipline meeting Module 4's BN mechanics — the course's two most-drilled details, colliding exactly where real codebases get it wrong. **Speed trick:** with a fully frozen backbone, embeddings are constant per image — precompute them once (`no_grad`, one pass over the dataset), then train the head on cached vectors; epochs drop from minutes to seconds. Worth showing because it changes what is *interactively explorable* in the lab.

### 3. Recipe 2 — fine-tuning: discriminative learning rates and warmup

Fine-tuning unfreezes the backbone and trains everything — highest ceiling, easiest to botch. The core tension: the backbone holds carefully learned features; the fresh head is random noise. At step 1, the head's large gradients flow *backward through the backbone* (Module 1: gradients traverse the same weights), scrambling good features before the head has learned anything. Two guards, both mandatory in Lab 5:

- **Discriminative learning rates** via param groups (Module 4's machinery): head at lr, backbone at lr/10 (or a per-stage geometric taper). The head moves fast; the backbone drifts gently.
- **Warmup** (Module 4): protect the first epochs while the head organises itself. A common professional variant staged in the lab: freeze-train the head for 1–2 epochs, *then* unfreeze and fine-tune — sequencing instead of balancing.

Expectations to set with real numbers: on Tamr-9, feature extraction reaches ~0.88–0.90 in minutes; full fine-tuning reaches ~0.93–0.95; the from-scratch Lab 3 baseline was ~0.82. The gap *widens* as data shrinks — a provided ablation at 10% of Tamr-9 shows from-scratch collapsing to ~0.55 while fine-tuning holds ~0.85. That single table is the module's business case.

**Catastrophic forgetting** gets named honestly: aggressive fine-tuning on a narrow task erodes the general features (visible as degraded performance if the model is later reused for a second task). For single-task deployments like Tamr Vision this is acceptable; for shared-backbone platforms it is why teams keep the pretrained original and adapt *copies* — and it foreshadows parameter-efficient methods (adapters/LoRA) participants will meet in the Specialist modules.

### 4. The preprocessing contract

Pretrained weights are only meaningful with the preprocessing they were trained under. For torchvision's ImageNet weights: RGB, resize/crop to 224×224 (or the weight-variant's documented size), scale to [0,1], normalise with ImageNet statistics (`mean=[0.485, 0.456, 0.406]`, `std=[0.229, 0.224, 0.225]`). Feed anything else and the model still runs — logits come out, accuracy is quietly mediocre. This is the transfer-learning version of Module 1's "silent near-correctness" theme, and `sim-wrong-norm` reproduces it: Tamr-9 statistics instead of ImageNet's costs ~4–6 pp and *no error message*.

The modern API makes the contract explicit and participants must use it: `weights = ResNet50_Weights.IMAGENET1K_V2; preprocess = weights.transforms()` — the transforms travel *with* the weights. Note the consequence for Tamr Vision: input size moves from 128² (Lab 3) to 224², epoch cost rises ~3×, and the train-split normalisation statistics from Module 3 are *retired* for the fine-tuned model. A model artefact is weights **plus** preprocessing; Lab 5's model card records both.

### 5. Sourcing models professionally: torchvision and the Hugging Face Hub

torchvision covers the classic vision backbones with clean weight enums and per-weight metadata (`weights.meta["_metrics"]` for reference accuracy). The **Hugging Face Hub** is the industry's model registry — vastly broader, community-populated, and therefore requiring professional scepticism. The evaluation checklist drilled in the lab:

1. **Model card** — intended use, training data, evaluation results, limitations. A model without a card is a model without documentation; treat like an unlabelled chemical.
2. **Licence** — apache-2.0/MIT (permissive) vs various restricted or research-only licences vs "openish" licences with acceptable-use restrictions. Commercial deployment at the packing house requires a licence that permits it; participants check this *before* downloading, and record the licence in the model card.
3. **Provenance and security** — organisation-verified sources preferred; prefer **safetensors** over pickle-based formats (pickle can execute arbitrary code on load — a genuine supply-chain vector); download counts and community reports as weak signals.
4. **Pin the revision** — `from_pretrained(model_id, revision="<commit-sha>")`. Hub repos are git repos; `main` moves. An unpinned model reference is an unpinned dependency, and Module 6 records the pinned revision in every W&B run config.

Uploading is the reverse contract: Lab 5's stretch task pushes the fine-tuned Tamr Vision model to a (private) Hub repo with a written model card — intended use, data description, per-class metrics, licence — which becomes a capstone deliverable in Module 6.

### 6. Common mistakes & production considerations

1. **Violating the preprocessing contract** — wrong normalisation or input size; silent 4–6 pp loss. Always `weights.transforms()`; never hand-copy magic numbers.
2. **Fine-tuning at a from-scratch learning rate** — 3e-4 uniform scrambles the backbone in the first epochs; val accuracy *starts* worse than feature extraction and recovers slowly or never. Discriminative LRs + warmup.
3. **Frozen backbone, drifting BN statistics** — the feature extractor that isn't actually frozen; BN modules to eval during training.
4. **Head replaced but optimiser fed all parameters** with weight decay dragging frozen params' momenta — harmless-looking, occasionally pathological; pass only trainable params.
5. **Unpinned Hub revisions and unread licences** — irreproducible builds and procurement failures; pin the SHA, record the licence.
6. **Choosing the biggest backbone by default** — a ResNet-152 where a ResNet-50 (or an efficient mobile backbone) meets the accuracy floor burns inference budget forever; the packing line's 10 items/s makes this concrete in the lab's latency measurement.

Production considerations: inference latency and model size are chosen *here*, at backbone selection, not later; domain-gap risk deserves a pilot evaluation before committing a project plan to "transfer will work"; licence and provenance review is part of procurement, not an afterthought — several Saudi public-sector buyers now require a model bill-of-materials; and the pretrained-then-adapted pattern means *upstream model updates are supply-chain events* — pinning revisions is change control.

## Code Examples

### Feature extraction with correct BN handling and cached embeddings

```python
# src/tamr_vision/models/transfer.py
"""Transfer-learning builders for Tamr Vision.

Two recipes:
  build_feature_extractor -> frozen ResNet-50 backbone + new 9-class head
  build_finetune          -> fully trainable, discriminative-LR param groups
Both honour the PREPROCESSING CONTRACT: use weights.transforms(), not
the Module 3 Tamr-9 statistics.
"""
import torch
import torch.nn as nn
from torchvision.models import resnet50, ResNet50_Weights

WEIGHTS = ResNet50_Weights.IMAGENET1K_V2      # preprocessing travels WITH weights
preprocess_eval = WEIGHTS.transforms()         # 224 crop + ImageNet normalisation


def build_feature_extractor(n_classes: int = 9) -> nn.Module:
    model = resnet50(weights=WEIGHTS)
    for p in model.parameters():
        p.requires_grad_(False)                # stops gradients...
    model.fc = nn.Linear(model.fc.in_features, n_classes)  # fresh head trains

    # ...but NOT BatchNorm running-stat updates. Freeze those too:
    def freeze_bn(module: nn.Module) -> None:
        if isinstance(module, nn.BatchNorm2d):
            module.eval()                      # use pretrained running stats
    model.freeze_bn = lambda: model.apply(freeze_bn)   # call after every .train()
    return model


def build_finetune(n_classes: int = 9, lr: float = 1e-4) -> tuple[nn.Module, list[dict]]:
    model = resnet50(weights=WEIGHTS)
    model.fc = nn.Linear(model.fc.in_features, n_classes)
    param_groups = [                            # discriminative LRs: head fast,
        {"params": model.fc.parameters(), "lr": lr},           # backbone gentle
        {"params": [p for n, p in model.named_parameters()
                    if not n.startswith("fc.")], "lr": lr / 10},
    ]
    return model, param_groups


@torch.no_grad()
def cache_embeddings(backbone: nn.Module, loader, device) -> tuple[torch.Tensor, torch.Tensor]:
    """Frozen backbone => constant embeddings. One pass, then head training
    runs in seconds per epoch instead of minutes."""
    backbone.eval()
    feats, labels = [], []
    for x, y in loader:
        z = backbone(x.to(device))             # (B, 2048) from the GAP layer
        feats.append(z.cpu())
        labels.append(y)
    return torch.cat(feats), torch.cat(labels)
```

### Pinned, licence-checked download from the Hugging Face Hub

```python
# scripts/pull_backbone.py
"""Download a candidate backbone from the Hugging Face Hub — the
professional way: licence checked, revision pinned, safetensors only.

Run:  python scripts/pull_backbone.py --model-id microsoft/resnet-50 \
          --revision <commit-sha>
"""
import argparse

from huggingface_hub import HfApi, hf_hub_download

ALLOWED_LICENCES = {"apache-2.0", "mit", "bsd-3-clause"}   # packing house =
                                                           # commercial use

p = argparse.ArgumentParser()
p.add_argument("--model-id", required=True)
p.add_argument("--revision", required=True, help="commit SHA — 'main' moves")
args = p.parse_args()

info = HfApi().model_info(args.model_id, revision=args.revision)
licence = (info.card_data or {}).get("license", "UNDECLARED")
if licence not in ALLOWED_LICENCES:
    raise SystemExit(f"BLOCKED: licence '{licence}' not approved for "
                     f"commercial deployment. Escalate before use.")

files = [s.rfilename for s in info.siblings]
weight_file = next((f for f in files if f.endswith(".safetensors")), None)
if weight_file is None:
    raise SystemExit("BLOCKED: no safetensors weights — pickle formats can "
                     "execute code on load. Find a safetensors source.")

path = hf_hub_download(args.model_id, weight_file, revision=args.revision)
print(f"OK  licence={licence}  revision={args.revision[:8]}  -> {path}")
# Record model-id, revision, licence in the model card AND the run config (M6).
```

### The fine-tuning driver

```python
# scripts/finetune_tamr.py
"""Lab 5 driver: staged fine-tune of ResNet-50 on Tamr-9.

Stage 1 (2 epochs): head only, backbone frozen, BN frozen.
Stage 2 (6 epochs): everything trainable, discriminative LRs + warmup.
Must BEAT the Lab 3 leaderboard number — that is the module's thesis.
"""
import torch
from torch.utils.data import DataLoader

from tamr_vision import engine
from tamr_vision.data import Tamr9
from tamr_vision.models.transfer import (WEIGHTS, build_finetune,
                                         preprocess_eval)
from tamr_vision.optim import make_optimizer_and_scheduler

engine.set_seed(42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Preprocessing contract: the weights' own transforms (224², ImageNet stats).
# Train transforms wrap the same normalisation with M3-style augmentation.
train_ds = Tamr9("data/tamr9", "train", transform=WEIGHTS.transforms())  # see repo
val_ds = Tamr9("data/tamr9", "val", transform=preprocess_eval)           # for the
train_dl = DataLoader(train_ds, batch_size=32, shuffle=True,             # augmented
                      num_workers=4, pin_memory=True)                    # variant
val_dl = DataLoader(val_ds, batch_size=64, shuffle=False, num_workers=4)

model, param_groups = build_finetune(n_classes=9, lr=1e-4)
model = model.to(device)
criterion = torch.nn.CrossEntropyLoss(label_smoothing=0.1)   # M4 carries over

# Stage 1: head only
for n, p in model.named_parameters():
    p.requires_grad_(n.startswith("fc."))
head_opt = torch.optim.AdamW(model.fc.parameters(), lr=1e-3)
for epoch in range(1, 3):
    tr = engine.train_one_epoch(model, train_dl, criterion, head_opt, device)
    print(f"[stage1] epoch {epoch}  train acc {tr['acc']:.3f}")

# Stage 2: everything, gently
for p in model.parameters():
    p.requires_grad_(True)
optimizer = torch.optim.AdamW(param_groups, weight_decay=0.05)
_, scheduler = make_optimizer_and_scheduler(model, lr=1e-4, epochs=6,
                                            warmup_epochs=1)
for epoch in range(1, 7):
    tr = engine.train_one_epoch(model, train_dl, criterion, optimizer, device)
    va = engine.evaluate(model, val_dl, criterion, device)
    scheduler.step()
    print(f"[stage2] epoch {epoch}  train acc {tr['acc']:.3f}  val acc {va['acc']:.3f}")
```

## Hands-on Lab 5 — Fine-Tune a Pretrained Backbone

| | |
|---|---|
| **Objective** | Beat the Lab 3 from-scratch baseline twice — first with feature extraction, then with staged fine-tuning — while honouring the preprocessing contract; evaluate one Hub-sourced model for licence and provenance; write the model card |
| **Duration** | 50 min (Day 3 H5), building on H4's theory |
| **Setup** | `git checkout lab5-start`; GPU strongly recommended (Colab fallback rehearsed); ImageNet weights pre-downloaded to the classroom cache |

**Tasks**
1. *(10 min)* **Feature extraction.** Build the frozen ResNet-50 + new head; cache embeddings with `cache_embeddings`; train the head on cached vectors (seconds per epoch). Record val accuracy — expect ≈ 0.88–0.90. Confirm BN freezing by asserting a BN layer's `running_mean` is bit-identical before/after an epoch.
2. *(15 min)* **Staged fine-tune.** Run `finetune_tamr.py`: 2 head-only epochs, then 6 full epochs with discriminative LRs + warmup. Target ≥ 0.92 and **> your Lab 3 leaderboard number + 8 pp**.
3. *(5 min)* **Break the contract.** Run the `sim-wrong-norm` variant (Tamr-9 stats instead of ImageNet's); record the silent 4–6 pp cost in `OBSERVATIONS.md`.
4. *(5 min)* **The scramble.** Rerun stage 2 with uniform lr 3e-4, no warmup, for 2 epochs; watch val start *below* feature extraction. Restore. One sentence on why.
5. *(10 min)* **Hub hygiene.** Use `pull_backbone.py` on an instructor-assigned model id: read the model card, verify the licence against the packing-house deployment, pin the revision. One assigned model per cohort has a *non-commercial licence* — the pairs holding it must correctly refuse it in writing.
6. *(5 min)* Write `MODEL_CARD.md` for your fine-tuned model: base weights + revision, preprocessing, data, per-class metrics, licence, intended use. Commit: `feat(transfer): fine-tuned resnet50 — val acc 0.9X, beats scratch by Y pp`.

**Checkpoints**
- [ ] BN running stats bit-identical across a frozen-backbone epoch
- [ ] Feature extraction ≥ 0.88; fine-tune ≥ 0.92; leaderboard updated with both
- [ ] Contract-violation cost recorded; scramble reproduced and explained
- [ ] Licence verdict correct for the assigned Hub model (including the planted refusal)
- [ ] MODEL_CARD.md complete — this file rides into the capstone

**Expected output**
```
$ python scripts/finetune_tamr.py
[stage1] epoch 1  train acc 0.861
[stage1] epoch 2  train acc 0.893
[stage2] epoch 1  train acc 0.902  val acc 0.911
[stage2] epoch 6  train acc 0.968  val acc 0.943
best val acc 0.943 — Lab 3 baseline 0.822 — delta +12.1 pp
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Feature extraction stuck ~0.75 | wrong normalisation (Tamr-9 stats) | `weights.transforms()` — the contract |
| "Frozen" run's val drifts run-to-run | BN running stats updating in train mode | freeze BN modules to eval; re-assert bit-identity |
| Fine-tune *starts* below feature extraction | uniform high lr scrambling the backbone | discriminative LRs + warmup; staged unfreeze |
| CUDA OOM at 224² batch 32 | 3× activation cost vs 128² | batch 16 + gradient accumulation (M6 preview), or cache-embedding recipe |
| Hub download blocked in classroom | proxy/firewall | pre-seeded classroom cache; `HF_HUB_OFFLINE=1` with local mirror |

**Instructor notes.** The emotional beat of this lab is the leaderboard moment — three days of from-scratch work beaten in twenty minutes — so make the comparison public and explicit; it is the strongest argument the course makes. Task 5's planted non-commercial licence is the professional-judgement check: pairs who download and fine-tune it anyway get the procurement-failure conversation, gently and publicly. Watch task 1's BN assertion — it is the module's most commonly faked checkpoint (pairs skip the assert and claim success); spot-check two pairs' actual tensor comparisons. Fast finishers: swap ResNet-50 for a mobile-class backbone, log the accuracy-vs-latency trade against the 10 items/s line rate.

## Mini Exercises

**Quiz (6 questions)**
1. Which layers of an ImageNet-pretrained CNN transfer best to date-variety grading and why? → early/middle (edges, textures — task-agnostic); late layers encode ImageNet-specific composition.
2. Feature extraction vs fine-tuning: which for 400 images of a similar domain? For 50k images of X-rays? → frozen backbone for the former; careful deep fine-tune for the latter (domain gap reaches early layers).
3. Why can a "frozen" backbone still change behaviour during training? → BN running statistics update in train mode regardless of requires_grad.
4. What two guards stop a fresh head from scrambling pretrained features? → discriminative learning rates; warmup (or staged head-first training).
5. Why prefer safetensors over pickle-based weight files? → pickle deserialisation can execute arbitrary code; safetensors is data-only.
6. What breaks if you fine-tune with your own dataset's normalisation statistics? → the input distribution mismatches what the weights were trained under; silent accuracy loss — the preprocessing contract.

**Estimation exercise.** The packing house's sister facility wants a defect detector (not variety grading) with 600 labelled images. Using the two-axis decision picture, choose the recipe, predict a realistic accuracy band relative to Tamr-9 results, and name the biggest risk to your estimate.

**Reading exercise.** Given three (instructor-curated) Hub model cards, rank the models for a commercial Saudi government deployment and justify each ranking in one sentence — licence, provenance, evaluation evidence.

**Discussion questions.**
- Your CTO asks: "if pretrained models are this good, why did we spend two days training from scratch?" Give the pedagogical *and* the engineering answers (you can only debug what you understand; some domains have no usable pretrain).
- The Hub model you shipped gets a security advisory against its pickle weights. Walk through what your pinned revision and model card let you do in the next hour that an unpinned team cannot.

## Case Study — Camera-Trap Wildlife Monitoring at a Saudi Royal Reserve

**Scenario.** The conservation team at a Saudi royal reserve operates 140 camera traps monitoring reintroduced species — Arabian oryx, sand gazelle, ostrich, and predators including the Arabian wolf. Rangers manually review ~90,000 triggered images per month, of which two-thirds are empty frames or livestock incursions. The team wants automated species classification, but its labelled archive is small and unbalanced: 8 species with counts ranging from 2,400 (oryx) down to 180 (wolf).

**Business context.** The reserve reports species-population indicators quarterly to national biodiversity programmes; review latency currently runs 5–6 weeks, making the indicators stale. The team has one ML engineer (the participant's role), one workstation GPU, and a mandate: usable triage within a quarter, with methods documented well enough for an external scientific audit.

**Technical challenge.** From-scratch training is hopeless at 180 images per rare class. Transfer learning is the only viable path, but the domain has real quirks: infrared night captures (grayscale, low contrast), motion blur, animals partially out of frame, and severe class imbalance. A pilot fine-tune must also honour licensing — outputs feed government reporting, so every upstream model needs a documented, permissive licence.

**Constraints.** 90k images/month at the edge of one GPU's batch-inference budget; night-capture domain gap from ImageNet's daylight photographs; class imbalance demands per-class recall reporting (a wolf missed is costlier than a gazelle mislabelled); scientific audit requires pinned model revisions and a full model card.

**Solution approach (facilitate, don't lecture).** (1) Recipe selection with the two-axis picture: small data, moderate domain gap → staged fine-tune of a pretrained backbone, strong Module 4 regularisation, augmentation tuned to the domain (brightness/contrast for IR, *no* hue jitter on grayscale night frames). (2) Attack imbalance before architecture: a two-stage design — a cheap "empty/animal" filter (feature extraction, huge easy dataset since empties are abundant) removes two-thirds of the volume, then the species classifier runs on the remainder; class-weighted loss and per-class recall as the contract metric. (3) Preprocessing contract kept via `weights.transforms()`; IR frames replicated to 3 channels rather than retraining stem convolutions — pragmatic, measured, documented. (4) Provenance: licence-checked, revision-pinned backbone; model card recording data composition, per-class recall, and known failure modes (blur, partial frames) — the audit artefact. (5) Realistic outcome band: overall ~0.90 with wolf recall ~0.75 flagged for a human-review lane — the *system* meets the latency mandate even where the *model* is honest about its weakest class.

**Discussion questions.**
1. Why does the empty-frame filter change the economics of the whole system more than 3 pp of classifier accuracy would? Quantify with the two-thirds figure.
2. The wolf class has 180 images. Rank: collect more wolf images, oversample, class-weight the loss, merge wolf into "predator" — by expected value *and* by scientific-reporting acceptability.
3. What exactly goes in the model card to survive an external audit — list five fields and the question each answers.
4. Night-vision cameras will be upgraded next year, shifting the input distribution. Using this module's vocabulary, what is that event, and what does your pinned-and-carded setup let you do about it?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Feature-extraction val accuracy | Transfer basics | ≥ 0.88 | leaderboard entry |
| Fine-tuned val accuracy | Transfer mastery | ≥ 0.92 and ≥ Lab 3 baseline + 8 pp | leaderboard entry |
| BN-freeze verification | Correctness | running stats bit-identical over an epoch | asserted in lab; spot-checked |
| Contract-violation cost measured | Discipline | delta recorded from sim-wrong-norm | OBSERVATIONS.md |
| Licence verdicts | Professional judgement | correct accept/refuse incl. the planted refusal | instructor review |
| MODEL_CARD.md completeness | Documentation | all six fields (base+revision, preprocessing, data, metrics, licence, intended use) | rubric check |

**Example benchmark table (filled during lab):**

| Recipe | Data used | Val acc | Train time (T4) | Delta vs scratch |
|---|---|---|---|---|
| Lab 3 TamrCNN (scratch) | 100% Tamr-9 | 0.822 | ~19 min | — |
| Feature extraction (cached) | 100% | 0.893 | ~3 min | +7.1 pp |
| Staged fine-tune | 100% | 0.943 | ~14 min | +12.1 pp |
| Scratch @ 10% data (provided) | 10% | 0.551 | ~4 min | the small-data collapse |
| Fine-tune @ 10% data (provided) | 10% | 0.861 | ~5 min | the business case |

## Required Visuals and Training Assets

### Diagrams
1. **The transfer surgery** — *Purpose:* the module's anchor image. *Elements:* pretrained ResNet drawn as backbone + head; scissors at the boundary; ImageNet head discarded; fresh 9-class head attached; freeze icons (padlocks) on backbone layers for recipe 1, dial icons (lr, lr/10) for recipe 2. *Style:* flat vector, padlock/dial iconography, English labels with Arabic subtitles.
2. **Layer-specificity gradient** — *Purpose:* why early layers transfer. *Elements:* backbone stages coloured on a generic→specific gradient; beneath each stage, its visualised features (edges → textures → parts → ImageNet objects); transferability curve overlaid. *Style:* horizontal gradient bar with feature thumbnails.
3. **The two-axis decision picture** — *Purpose:* recipe selection. *Elements:* dataset-size × domain-gap quadrant chart with the four recipes placed; course datasets (Tamr-9, camera-trap, X-ray example) plotted as points. *Style:* quadrant chart.
4. **The preprocessing contract** — *Purpose:* weights + transforms as one artefact. *Elements:* a sealed package containing weights and transforms together; a red "torn contract" variant showing wrong normalisation feeding the same weights, with the silent accuracy drop labelled. *Style:* package/contract metaphor, two panels.
5. **Hub sourcing checklist card** — *Purpose:* professional hygiene reference. *Elements:* four-step card — model card read → licence vs use → safetensors → pin revision — each with pass/block outcomes. *Style:* checklist card, printable A4.

### Images (screenshots)
1. **The leaderboard moment**: *why:* the module's thesis in one image; *content:* scratch 0.822 vs fine-tune 0.943 rows side by side with train times.
2. **`weights.transforms()` printed**: *why:* the contract made concrete; *content:* the transform pipeline repr showing 224 crop + ImageNet stats.
3. **Hub model card page**: *why:* reading reference; *content:* an exemplary card with licence, data, metrics sections annotated.
4. **The blocked download**: *why:* expected output of the planted refusal; *content:* `pull_backbone.py` exiting with the licence BLOCKED message.
5. **10%-data ablation table**: *why:* the business case; *content:* scratch collapse vs fine-tune resilience at 10% data.

### Simulations
1. **The torn contract** — *Setup:* branch `sim-wrong-norm` fine-tunes with Tamr-9 normalisation statistics. *Expected behaviour:* trains cleanly, lands 4–6 pp low, no error anywhere. *Learning objective:* preprocessing is part of the model; silent near-correctness, transfer edition.
2. **The scramble** — *Setup:* uniform lr 3e-4, no warmup, full unfreeze. *Expected behaviour:* val accuracy initially *below* feature extraction; slow partial recovery. *Learning objective:* fresh-head gradients destroy pretrained features; sequencing and discriminative LRs exist for a reason.
3. **The unfrozen freeze** — *Setup:* branch `sim-bn-drift`: requires_grad frozen, BN left in train mode, trained 10 epochs; then evaluated against a bit-frozen twin. *Expected behaviour:* diverging running stats and a measurable eval gap. *Learning objective:* freezing has two halves; verify with tensors, not intentions.

### Interactive Activities
- **Recipe triage (10 min):** six one-line scenarios (data size + domain) on the projector; pairs commit to a quadrant-picture recipe on cards; instructor reveals and the class debates the two contested ones.
- **Licence courtroom (15 min):** three Hub model cards, one per team-cluster; each cluster must deliver a deploy/refuse verdict for the packing house with a one-sentence justification; instructor plays procurement officer and cross-examines.
- **Model-card speed review (10 min):** pairs swap MODEL_CARD.md files and audit against the six-field checklist; two findings per review, majlis-style feedback round.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Tamr-9 | Course bundle (unchanged splits) | JPEG + splits.json | ~9k images | Fine-tuning target — comparability with Labs 3–4 |
| Tamr-9 @ 10% | Derived, stratified, frozen file | splits_10pct.json | ~900 images | The small-data business case |
| Curated Hub model list | Instructor handout | MD table | 3–4 models | Licence/provenance exercises (incl. one planted non-commercial) |
| ImageNet-pretrained weights | torchvision / classroom cache | pth/safetensors | ~100 MB | Pre-seeded to survive classroom bandwidth |

### Demo Requirements
- **Instructor demo:** the scramble, live — two fine-tune launches side by side (uniform-lr vs staged), val accuracy after 2 epochs projected; the worse start tells the whole story in 6 minutes.
- **Student demo:** the pair holding the planted non-commercial model presents their refusal memo; a second pair shows their BN bit-identity assertion passing.
- **Expected outputs:** every pair's fine-tuned checkpoint + MODEL_CARD.md committed by end of Day 3 — Module 6 wraps this exact model in experiment tracking, and the capstone tunes it.

---

# Module 6 — GPU Training and Experiment Tracking

## Module Overview

**Purpose.** The course's final module turns competent training into *professional* training. Two capabilities define the difference. First, **using the hardware properly**: understanding the host/device model, feeding the GPU fast enough to keep it busy, and using mixed precision to double throughput — because a GPU running at 30% utilisation is money on fire. Second, **experiment management**: every run logged with its config, metrics, environment, and artefacts, so that "which model is best and how was it made?" is a query, not an archaeology project. Weights & Biases replaces Lab 4's `ablation.csv` with the industrial version of the same discipline, and the Hugging Face Hub becomes the shipping dock for the finished model.

**Business relevance.** GPU time is the dominant cost of deep-learning development — in the Kingdom, cloud GPU capacity and on-prem clusters (including national research infrastructure) are allocated resources that teams must justify. Throughput literacy routinely recovers 2–5× from the same hardware. Experiment tracking is the other half of the cost story: untracked experiments get repeated, best models get lost, and regulated deployments (SAMA model risk, PDPL data governance) increasingly require exactly the audit trail that a tracking tool produces as a by-product. This module is also the course's hand-off to production: SDA-AIE-211 deploys what is tracked and reproducible here.

**Industry use cases.**
- The Qassim packing house (golden thread): the capstone's hyperparameter sweep runs overnight on one GPU; W&B's comparison table picks the winner and its full lineage ships with the model.
- A Saudi research group shares a university GPU cluster; per-run W&B logging ends the "who trained the good checkpoint in March?" archaeology that cost them a paper deadline.
- A bank's model-risk team audits a credit model update; the W&B run — config, data version, metrics, environment — *is* the reproducibility evidence pack.

**Expected competencies.** After this module a participant can move models and data between host and device correctly, diagnose input-pipeline vs compute bottlenecks, enable mixed-precision training with AMP safely, apply gradient accumulation when memory binds, configure reproducibility (seeds, determinism flags, environment capture) with honest limits, instrument training with W&B (runs, configs, artifacts), launch a hyperparameter sweep, and publish a model with its card to the Hugging Face Hub.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Explain the host/device model and write device-correct, transfer-efficient training code | LO2, LO3 |
| 6.2 | Diagnose whether a training run is input-bound or compute-bound and fix the pipeline accordingly | LO3 |
| 6.3 | Apply automatic mixed precision and gradient accumulation correctly | LO3, LO4 |
| 6.4 | Configure reproducibility: seeds, determinism flags, environment and data-version capture | LO6 |
| 6.5 | Track, compare, and reproduce experiments with W&B runs, configs, artifacts, and sweeps | LO6 |
| 6.6 | Publish a model and its card to the Hugging Face Hub as a versioned artefact | LO5, LO6 |

## Technical Content

### 1. The host/device model: two computers, one program

A CUDA-equipped machine is two computers: the **host** (CPU + RAM) and the **device** (GPU + VRAM), joined by a PCIe bus that is slow relative to both. Every performance rule in this module follows from that picture:

- **Placement is explicit.** `model.to(device)`, `x.to(device)` — an operation requires all its tensors on one device, and the mixed-device `RuntimeError` is the most common Day 4 crash. Course convention since Module 2: a single `device` variable threaded through the engine, never hard-coded `"cuda"` (CPU fallback must keep working — it is the classroom's own contingency plan).
- **Transfers are expensive; batch them.** One `(B, C, H, W)` copy beats B small copies; `pin_memory=True` on the DataLoader plus `x.to(device, non_blocking=True)` lets the copy overlap compute.
- **CUDA is asynchronous.** Kernel launches return immediately; naive `time.time()` around a forward pass measures launch time, not compute. Correct timing brackets with `torch.cuda.synchronize()` — the course's benchmark scripts do this and participants must know why.
- **VRAM anatomy** (Module 2's preview, now with numbers): parameters + gradients + optimiser state (AdamW ≈ 3× params) + **activations** (scales with batch size — the knob that OOMs). `torch.cuda.memory_allocated()` and the OOM message's "tried to allocate" line are the first diagnostics; the fixes, in order: smaller batch, AMP, gradient accumulation.

### 2. Feeding the beast: input-pipeline throughput

The commonest GPU-utilisation failure is not the model — it is the DataLoader. If Python decodes and augments images on one thread while the GPU waits, `nvidia-smi` shows sawtooth utilisation: burst, starve, burst. The diagnostic sequence taught in the lab:

1. **Measure a baseline**: images/second over a fixed 50-batch window (the engine gains a `throughput` metric).
2. **Isolate the pipeline**: iterate the DataLoader *without* the model — if that alone is slower than the GPU step, the pipeline is the bottleneck by definition.
3. **Fix in order of cheapness**: `num_workers=4–8` (parallel decode), `pin_memory=True`, `persistent_workers=True` (skip worker respawn per epoch), and only then bigger guns (pre-resized image cache on disk — decode cost scales with source resolution, and Tamr-9's raw photos are 3–5× larger than the 224² the model consumes).

Rule of thumb for the classroom T4s: TamrCNN at 128² should exceed 900 img/s; the ResNet-50 fine-tune at 224² with AMP should exceed 350 img/s. Participants tune until they clear the bar, and every change lands as a row in W&B — the module eats its own dog food from the first hour.

### 3. Mixed precision and gradient accumulation

**AMP (automatic mixed precision)** runs eligible operations in half precision (fp16 on the classroom T4s; bf16 on newer silicon) while keeping precision-sensitive operations (losses, reductions, norm statistics) in fp32. Two objects and three lines: `autocast()` wraps the forward + loss; `GradScaler` scales the loss up before backward so small gradients survive fp16's narrow range, then unscales before the optimiser step and skips steps whose gradients overflowed. Benefits on the course workloads: ~1.7–2× throughput and ~40% activation-memory savings — measured, not asserted, in Lab 6. The fine print: fused `WithLogits` losses (Module 2's rule) exist precisely because separate sigmoid+BCE overflows in fp16; if `clip_grad_norm_` is used with AMP, gradients must be **unscaled first** (`scaler.unscale_(optimizer)`) or the clip threshold is meaningless — a planted bug in the lab.

**Gradient accumulation** trades time for memory: run N micro-batches, `loss/N` each, `backward()` each (gradients *accumulate* — Module 2's "feature, not bug", now cashed in), step once. Effective batch = N × micro-batch. It is the standard answer to "the paper used batch 256 and I OOM at 64", and the AMP + accumulation combination is how the capstone's ResNet sweep fits the classroom GPUs.

### 4. Reproducibility: honest guarantees

The reproducibility ladder, from cheap to strict — participants must know which rung a claim stands on:

1. **Seeds** (Module 2's `set_seed`): statistical reproducibility — same distribution of outcomes, not identical numbers on GPU (cuDNN picks algorithms nondeterministically; atomics reorder float additions).
2. **Determinism flags**: `torch.use_deterministic_algorithms(True)` + `cudnn.benchmark=False` (+ the documented env var for cuBLAS): bit-level runs on identical hardware/software, at a measurable speed cost (typically 5–15%). Use for audits and debugging heisenbugs, not routine training.
3. **Environment capture**: exact package versions, CUDA/driver, GPU model, git commit of the code, and the *data version* (Tamr-9's `splits.json` hash). Without this rung the other two are theatre — the biggest real-world reproducibility failures are "different data, different code", not RNG. W&B captures most of it automatically (git state, pip freeze, hardware), which is a major and underrated reason to use a tracker.

Frame it as a contract question: when a regulator, a customer, or your own future team asks "can you reproduce the production model?", the honest answers are rung-labelled — and rung 3 is the one that matters most and costs least.

### 5. Experiment tracking with Weights & Biases — and shipping to the Hub

The discipline is Lab 4's ablation table; the tool industrialises it. Core objects, mapped to what participants already do:

- **Run** = one training execution: `wandb.init(project="tamr-vision", config=asdict(cfg))`. The config *is* the run's identity — everything needed to re-launch it, including the pinned backbone revision from Module 5.
- **Metrics**: `wandb.log({"train/loss": …, "val/acc": …, "lr": …, "throughput": …}, step=epoch)` — the engine gains an optional logger callback rather than W&B calls scattered through the loop (the engine stays tool-agnostic; the integration is 15 lines).
- **Artifacts**: versioned files with lineage — the dataset splits, the best checkpoint, the model card. Lineage answers the audit question "which data produced this model?" mechanically.
- **Sweeps**: declarative hyperparameter search (the capstone uses Bayesian search over lr, weight decay, label smoothing, augmentation strength) with an agent that pulls configurations — the classroom pattern is one sweep, many participants' agents, which also teaches the shared-cluster etiquette of tagging runs with owner names.
- **Reports/comparison**: the parallel-coordinates and run-table views replace `ablation.csv` for the capstone's model-selection decision, and the exported comparison table is a required capstone deliverable.

Shipping: the selected model goes to the **Hugging Face Hub** (`upload_folder` to a private repo) with the Module 5 model card, the preprocessing contract, and the W&B run URL cross-referenced — closing the loop: anyone holding the model can walk back to the exact run, config, data version, and code commit that produced it. Offline note for restricted networks: `WANDB_MODE=offline` logs locally and syncs later — rehearsed as the classroom fallback.

### 6. Common mistakes & production considerations

1. **Hard-coded `"cuda"`** — crashes on CPU-only machines and breaks the classroom fallback; thread a `device` variable, always.
2. **Timing without synchronisation** — async CUDA makes naive timers lie by 10–100×; `torch.cuda.synchronize()` around benchmark brackets.
3. **Starving the GPU** — `num_workers=0` on an image task; the sawtooth utilisation pattern. Measure images/second before and after; never tune blind.
4. **Clipping scaled gradients under AMP** — the planted Lab 6 bug: `clip_grad_norm_` before `scaler.unscale_` clips against a meaningless threshold; training destabilises intermittently and looks like Module 4 material.
5. **Tracking noise instead of signal** — logging every batch's loss at step granularity while forgetting the config, the data hash, or the git commit; a run you cannot re-launch is a pretty chart, not an experiment.
6. **Sweeping before stabilising** — launching a 40-run sweep on an untested config burns the GPU night on garbage; the sweep inherits Lab 4's rescued recipe, and the self-test gate (Module 2) runs before any sweep starts.

Production considerations: GPU allocation on shared/national infrastructure is justified with utilisation and throughput numbers — the habits here are the application form; experiment metadata is governance evidence (model-risk reviews ask for exactly a run's lineage); W&B-hosted logging sends metadata to a SaaS — for data-sovereignty-sensitive Saudi deployments know the self-hosted and offline options, and never log raw data samples from PDPL-scoped datasets (log *hashes and counts*, not contents); and the tracked-artefact handoff (Hub model + W&B lineage) is precisely what SDA-AIE-211's deployment pipeline consumes next.

## Code Examples

### The engine grows AMP, accumulation, throughput, and a logger callback

```python
# src/tamr_vision/engine_v2.py
"""Engine v2 = Lab 2's engine + device performance + tracking hooks.

New, all optional and default-off (CPU path unchanged):
  - AMP via autocast + GradScaler (fp16 on T4-class GPUs)
  - gradient accumulation (effective batch = accum * batch)
  - images/second throughput metric (synchronised timing)
  - logger callback: engine stays tool-agnostic; W&B lives outside
"""
from __future__ import annotations

import time
from typing import Callable, Protocol

import torch
import torch.nn as nn
from torch.utils.data import DataLoader


class Logger(Protocol):
    def __call__(self, metrics: dict[str, float], step: int) -> None: ...


def train_one_epoch_v2(model: nn.Module, loader: DataLoader, criterion: nn.Module,
                       optimizer: torch.optim.Optimizer, device: torch.device,
                       *, epoch: int, scaler: torch.amp.GradScaler | None = None,
                       accum_steps: int = 1, clip_norm: float | None = 1.0,
                       log: Logger | None = None) -> dict[str, float]:
    model.train()
    use_amp = scaler is not None and device.type == "cuda"
    total_loss, total_correct, total_n = 0.0, 0, 0
    if device.type == "cuda":
        torch.cuda.synchronize()               # honest timing under async CUDA
    t0 = time.perf_counter()

    optimizer.zero_grad()
    for i, (x, y) in enumerate(loader):
        x = x.to(device, non_blocking=True)    # overlaps with pinned memory
        y = y.to(device, non_blocking=True)

        with torch.autocast(device_type=device.type, enabled=use_amp):
            logits = model(x)
            loss = criterion(logits, y) / accum_steps   # mean over micro-batches

        (scaler.scale(loss) if use_amp else loss).backward()

        if (i + 1) % accum_steps == 0:
            if use_amp:
                scaler.unscale_(optimizer)     # BEFORE clipping — else the
            if clip_norm is not None:          # threshold is meaningless
                nn.utils.clip_grad_norm_(model.parameters(), clip_norm)
            if use_amp:
                scaler.step(optimizer)         # skips step on inf/nan grads
                scaler.update()
            else:
                optimizer.step()
            optimizer.zero_grad()

        bs = y.size(0)
        total_loss += loss.item() * accum_steps * bs
        total_correct += (logits.argmax(1) == y).sum().item()
        total_n += bs

    if device.type == "cuda":
        torch.cuda.synchronize()
    metrics = {"loss": total_loss / total_n, "acc": total_correct / total_n,
               "img_per_s": total_n / (time.perf_counter() - t0),
               "lr": optimizer.param_groups[0]["lr"]}
    if log is not None:
        log({f"train/{k}": v for k, v in metrics.items()}, step=epoch)
    return metrics
```

### W&B integration: run, artifacts, lineage

```python
# scripts/train_tracked.py
"""Every capstone run goes through here: config-complete, artifact-linked.

Run:  python scripts/train_tracked.py --config configs/rescued.yaml
Offline classrooms:  WANDB_MODE=offline  (sync later with `wandb sync`)
"""
import dataclasses
import hashlib
import subprocess
from pathlib import Path

import wandb

from tamr_vision.config import TrainConfig, load_config  # Lab 4's dataclass, grown


def data_fingerprint(splits_path: Path) -> str:
    """Data version = hash of the frozen splits. Log the HASH, never samples
    (PDPL discipline: metadata to SaaS, data stays home)."""
    return hashlib.sha256(splits_path.read_bytes()).hexdigest()[:12]


cfg: TrainConfig = load_config()
run = wandb.init(
    project="tamr-vision",
    job_type="finetune",
    tags=[cfg.backbone, "capstone"],
    config={**dataclasses.asdict(cfg),
            "backbone_revision": cfg.backbone_revision,   # M5's pinned SHA
            "data_version": data_fingerprint(Path("data/tamr9/splits.json")),
            "git_commit": subprocess.check_output(
                ["git", "rev-parse", "--short", "HEAD"]).decode().strip()},
)

# ... training loop calls engine_v2 with log=lambda m, step: wandb.log(m, step=step)
# ... on new best val acc:

def log_best_checkpoint(ckpt_path: Path, val_acc: float) -> None:
    art = wandb.Artifact("tamr-classifier", type="model",
                         metadata={"val_acc": val_acc})
    art.add_file(str(ckpt_path))
    art.add_file("MODEL_CARD.md")              # the M5 card rides along
    run.log_artifact(art)                       # lineage: run -> data -> model
```

### The capstone sweep

```yaml
# configs/sweep.yaml — launch:  wandb sweep configs/sweep.yaml
#                      agents:  wandb agent <sweep-id>   (one per pair)
program: scripts/train_tracked.py
method: bayes                # Bayesian search: spends the GPU night wisely
metric: {name: val/acc, goal: maximize}
parameters:
  lr:                {distribution: log_uniform_values, min: 1.0e-5, max: 1.0e-3}
  weight_decay:      {values: [0.01, 0.05, 0.1]}
  label_smoothing:   {values: [0.0, 0.1]}
  aug_strength:      {values: [light, medium, strong]}
  epochs:            {value: 8}          # sweep budget; winner retrains at 15
early_terminate:     {type: hyperband, min_iter: 3}   # kill hopeless runs early
```

## Hands-on Lab 6 — Make It Fast, Make It Tracked

| | |
|---|---|
| **Objective** | Take the Module 5 fine-tune from untracked-and-slow to instrumented-and-fast: diagnose the input pipeline, enable AMP correctly, wire W&B with full config/lineage, and launch the capstone sweep |
| **Duration** | 50 min (Day 4 H2), building on H1's GPU theory; the sweep runs into H3 |
| **Setup** | `git checkout lab6-start`; one T4-class GPU per pair (Colab fallback with `WANDB_MODE=offline` rehearsed); W&B team project `tamr-vision-<cohort>` pre-created |

**Tasks**
1. *(10 min)* **Baseline and diagnose.** Run the provided deliberately slow config (`num_workers=0`, no AMP): record img/s and the `nvidia-smi` sawtooth. Iterate the DataLoader without the model to prove the pipeline is the bottleneck. Fix: workers 4, pin_memory, persistent_workers. Record the new img/s.
2. *(10 min)* **AMP, correctly.** Enable autocast + GradScaler via `engine_v2`. The skeleton ships the planted bug — clipping before `scaler.unscale_` — which the intermittent grad-norm spikes expose; fix it and record throughput and memory before/after (expect ~1.7–2× img/s, ~40% activation memory).
3. *(10 min)* **Track everything.** Wire `train_tracked.py`: config (including backbone revision + data hash + git commit), per-epoch metrics, best-checkpoint artifact with the model card attached. Verify in the W&B UI that a teammate could re-launch your run from its config alone — the pair *swaps machines* and actually tries.
4. *(5 min)* **Accumulate.** OOM the 224² run on purpose at batch 64; recover with micro-batch 16 × accum 4; confirm the val metric matches the batch-64 run within noise.
5. *(10 min)* **Launch the sweep.** Start one agent per pair against the cohort sweep; verify runs appear tagged with your pair name; hyperband kills a hopeless run before your eyes.
6. *(5 min)* Commit: `feat(tracking): engine v2 + W&B — img/s 3.4x baseline`. The sweep keeps running through the break (the Day 4 plan's "GPU time is never idle").

**Checkpoints**
- [ ] Bottleneck proven by measurement (loader-only vs full-step timing), not guessed
- [ ] AMP clip bug found and fixed; before/after throughput and memory recorded
- [ ] Machine-swap re-launch from config succeeds
- [ ] Accumulation run matches large-batch metrics within noise
- [ ] Sweep agent contributing runs to the cohort project

**Expected output**
```
$ python scripts/benchmark_pipeline.py
config                          img/s     GPU util
workers=0, no AMP                 96      31% (sawtooth)
workers=4 + pinned               241      68%
+ AMP (fixed clip order)         412      93%
$ wandb agent <sweep-id>
wandb: Agent starting run tamr-sweep-17 with config: lr=2.3e-4, wd=0.05, ...
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `Expected all tensors on the same device` | criterion weights or a metric tensor left on CPU | audit every tensor creation; thread `device` |
| AMP run intermittently spikes/NaNs | the planted clip-before-unscale bug | `scaler.unscale_(optimizer)` first — read the skeleton comment |
| img/s unchanged after adding workers | Windows/macOS spawn + non-importable transform (M2's lesson) | module-level transforms; `if __name__ == "__main__"` |
| W&B login fails in classroom network | proxy blocks SaaS | `WANDB_MODE=offline`; sync after class |
| Sweep agent idles | agent pointed at personal project, not cohort sweep id | copy the sweep id from the shared board |
| OOM during sweep | aug_strength=strong + batch 32 on 224² | sweep config caps batch at 16 with accum 2 — verify you pulled latest |

**Instructor notes.** Task 3's machine-swap is the module's teeth — a run is only reproducible if *someone else* can re-launch it, and the swap makes that a live test instead of a claim. Keep the benchmark leaderboard (img/s) public and slightly competitive; throughput tuning is the rare topic where gamification works cleanly. The sweep must be launched before the H2/H3 boundary — its overnight-style economics are simulated by letting it run through the break, and H3's project work consumes its results. Fast finishers: profile with `torch.profiler` and attribute the remaining 7% idle time; or add a `deterministic` flag to engine_v2 and measure rung-2's speed cost.

## Mini Exercises

**Quiz (6 questions)**
1. Why does `time.time()` around a CUDA forward pass under-measure? → kernel launches are asynchronous; synchronize before reading the clock.
2. GPU utilisation sawtooths between 90% and 5%. First diagnostic? → iterate the DataLoader without the model; if slow, the input pipeline is starving the GPU.
3. What does GradScaler actually do, and why does fp16 need it? → scales loss up so small gradients survive fp16's range, unscales before stepping, skips overflowed steps.
4. Effective batch size of micro-batch 16 with accum_steps 4 — and which Module 2 fact makes accumulation work? → 64; gradients accumulate in `.grad` across backward calls.
5. Name the three reproducibility rungs and which one prevents "different data, different code". → seeds; determinism flags; environment/data capture — the third.
6. Why log the *hash* of splits.json to W&B rather than the images themselves? → data version travels, data stays home — sovereignty/PDPL discipline plus lineage.

**Estimation exercise.** Your sweep needs 40 runs × 8 epochs × 74 s/epoch on one T4. Can it finish overnight (10 hours)? Show the arithmetic, then recompute with AMP's measured 1.8× and hyperband killing 30% of runs at epoch 3.

**Audit exercise.** Given a screenshot of a W&B run page (provided) with config, metrics, and artifacts, answer a model-risk reviewer's four questions: what data version, what code commit, what base model revision, and can the result be re-launched — citing the exact field for each.

**Discussion questions.**
- Your team's GPU cluster request was rejected for "insufficient utilisation justification". Which three numbers from this module's lab do you put on the resubmission?
- A colleague says experiment tracking is bureaucracy that slows research. Using the March-checkpoint archaeology story, argue the opposite — then concede the one situation where they have a point (throwaway explorations), and how tags/projects solve it.

## Case Study — The Vanished Model at a Shared University GPU Cluster in Thuwal

**Scenario.** A computer-vision research group at a university on the Red Sea coast shares an 8-GPU cluster across eleven graduate students. In March, someone trained a red-tide detection model on coastal satellite imagery that reached 0.91 F1 — the best ever. In September, preparing a journal revision and a pilot with an environmental agency, the group cannot reproduce it: the best surviving checkpoint scores 0.84, the student who ran the March job has graduated, and the cluster's home directories hold 240 checkpoint files named variants of `best_model_final_v2_REAL.pt`.

**Business context.** The journal revision deadline is six weeks out; the environmental agency's pilot requires a documented, reproducible model as a condition of data access to its higher-resolution imagery. The group's cluster allocation is also up for renewal, and the renewal committee asks for evidence of effective utilisation.

**Technical challenge.** Reconstruct or surpass the March result under a deadline, and install a tracking discipline that prevents recurrence — across eleven users who share GPUs, disks, and a healthy scepticism of process overhead.

**Constraints.** No W&B SaaS for the agency-restricted imagery (data-sovereignty condition) — self-hosted or offline tracking only; the cluster's scheduler kills jobs at 24 h, so runs must checkpoint-resume (Module 2's machinery) and sweeps must tolerate preemption; eleven users mean any convention must be *cheaper to follow than to ignore*.

**Solution approach (facilitate, don't lecture).** (1) Triage the archaeology: script a scan of all 240 checkpoints — load each, evaluate on the frozen val split, record git metadata if any. Best found: 0.87, still short; the March run is genuinely gone. Timebox the dig to one week and call it — the lesson is its cost, roughly SAR 30k of student time. (2) Rebuild forward instead: the group's Lab-4-style ablation on the 0.87 recipe plus a 30-run offline-tracked sweep recovers 0.90 in nine days — *faster than the archaeology*, which is the case study's punchline. (3) Install the floor: self-hosted tracking server on the cluster head node; a shared `train_tracked.py` wrapper that auto-captures config, git commit, data hash, and owner tag — compliance by default, not by policy memo. (4) The renewal committee gets the utilisation dashboards as a by-product; the agency gets rung-3 reproducibility evidence; the journal gets exact seeds and configs in the artifact.
 
**Discussion questions.**
1. Price the vanished model: list every cost line the group paid for not tracking (student time, deadline risk, agency trust, allocation renewal), and which single W&B field would have prevented each.
2. Why is "rebuild forward" often cheaper than "reproduce backward" once tracking discipline exists — and what does that imply about where reproducibility effort should be spent?
3. Design the minimal convention set for eleven sceptical users: what is mandatory (auto-captured), what is optional, and why does auto-capture beat a written policy?
4. The agency forbids SaaS telemetry. Map the module's tracking stack onto that constraint: what changes (offline mode, self-hosting), and what is lost?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Pipeline throughput (ResNet-50, 224², T4) | Performance | ≥ 350 img/s with AMP (≥ 3× the broken baseline) | benchmark script (synchronised) |
| GPU utilisation during training | Performance | ≥ 85% sustained | nvidia-smi / W&B system metrics |
| AMP correctness | Correctness | clip-after-unscale verified; no NaN steps over 8 epochs | run logs |
| Accumulation equivalence | Correctness | batch-64 vs 16×4 val acc within 0.5 pp | comparison runs |
| Machine-swap re-launch | Reproducibility | teammate re-launches from config alone, succeeds | live test in lab |
| Sweep participation | Tracking | ≥ 5 completed runs per pair in the cohort sweep | W&B project table |

**Example benchmark table (filled during lab):** the `benchmark_pipeline.py` output (96 → 241 → 412 img/s progression) is committed per pair and posted to the throughput leaderboard; the cohort sweep's parallel-coordinates view is exported as the module's collective benchmark artefact.

## Required Visuals and Training Assets

### Diagrams
1. **Two computers, one program** — *Purpose:* the module's anchor mental model. *Elements:* host (CPU/RAM) and device (GPU/VRAM) as two machines; PCIe bridge drawn deliberately narrow; tensors as labelled parcels crossing it; a pinned-memory fast lane; the `.to(device)` toll booth. *Style:* flat vector, bridge metaphor, English labels with Arabic subtitles.
2. **VRAM anatomy at training time** — *Purpose:* what OOMs and why. *Elements:* stacked bar of params / gradients / optimiser state (3× tag for AdamW) / activations, with the activations segment scaling as batch size grows; AMP shown shrinking the activation band ~40%. *Style:* stacked bar with a batch-size slider annotation.
3. **The starved GPU** — *Purpose:* bottleneck recognition. *Elements:* two aligned timelines — DataLoader (decode/augment blocks) and GPU (compute bursts + idle gaps) — before and after workers/pinning; the sawtooth utilisation trace above. *Style:* dual swim-lane timing diagram.
4. **AMP data flow** — *Purpose:* where fp16 and fp32 live. *Elements:* forward/backward path coloured by precision; GradScaler's scale-up/unscale points marked; the clip-after-unscale checkpoint flagged in red. *Style:* precision-coloured flow diagram.
5. **The lineage graph** — *Purpose:* tracking as connected evidence. *Elements:* nodes for code commit, config, data artifact (splits hash), run, metrics, model artifact, Hub repo — arrows showing the walk from a deployed model back to everything that made it. *Style:* provenance DAG.

### Images (screenshots)
1. **nvidia-smi sawtooth vs sustained**: *why:* the diagnostic pattern participants must recognise on sight; *content:* utilisation traces before/after the pipeline fix, side by side.
2. **W&B run page, annotated**: *why:* the audit-exercise reference; *content:* config panel (revision, data hash, git commit circled), metric charts, artifact tab.
3. **Sweep parallel-coordinates view**: *why:* model-selection reference for the capstone; *content:* 30+ runs, lr axis dominating, best-run band highlighted.
4. **The OOM message, decoded**: *why:* turn panic into reading; *content:* a real CUDA OOM with "tried to allocate", reserved/allocated fields annotated with the fix ladder.
5. **Hub model repo with card**: *why:* the shipping-dock end state; *content:* private repo showing safetensors weights, MODEL_CARD.md, and the W&B run URL cross-reference.

### Simulations
1. **The starved GPU** — *Setup:* branch `sim-starved` (`num_workers=0`, full-resolution decode). *Expected behaviour:* 96 img/s, 31% sawtooth utilisation; fixes triple it. *Learning objective:* measure, isolate, fix in cheapness order.
2. **The meaningless clip** — *Setup:* branch `sim-scaled-clip`: clipping before unscale under AMP. *Expected behaviour:* intermittent instability that mimics a Module 4 lr problem; grad-norm logs reveal clipping never engages meaningfully. *Learning objective:* AMP changes the order of operations; read the scaler contract.
3. **The unlaunchable run** — *Setup:* a provided W&B run logged with metrics but no config, no data hash, no commit. *Expected behaviour:* the machine-swap test fails — the partner cannot re-launch it. *Learning objective:* metrics without config is a chart, not an experiment.

### Interactive Activities
- **Bottleneck bingo (10 min):** instructor shows six utilisation/timing traces; pairs diagnose input-bound vs compute-bound vs transfer-bound and name the first fix; leaderboard scored.
- **The reproducibility interrogation (15 min):** one pair plays model-risk reviewer with the four audit questions, the other defends using only their W&B run page; swap roles; the class scores which fields answered which question.
- **Sweep-budget planning (10 min):** teams get the estimation exercise's arithmetic live — a GPU-night budget, epoch costs with/without AMP, hyperband survival rates — and must commit a sweep design (runs × epochs × params) before the reveal of the reference plan.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Tamr-9 (+ raw high-res originals) | Course bundle | JPEG folders + splits.json | ~9k images (~3 GB raw) | Pipeline-throughput reality: decode cost is real |
| `sim-*` branches | Course repo | git branches | — | Starved GPU, scaled clip, unlaunchable run |
| Cohort W&B project | Pre-created by instructor | SaaS/self-hosted project | — | Shared sweep + comparison views |

### Demo Requirements
- **Instructor demo:** the full diagnostic arc live — sawtooth on `nvidia-smi`, loader-only timing proving the bottleneck, fixes applied, 3× throughput — in under 8 minutes; then a 2-minute W&B tour of last cohort's sweep.
- **Student demo:** one pair performs the machine-swap re-launch in front of the class; one pair presents their before/after benchmark table.
- **Expected outputs:** every pair tracked, fast, and contributing sweep runs by the end of H2 — H3's project work opens with each pair reading their own sweep results.

---

# Final Capstone Project

## Title: Tamr Vision — Build and Tune a Production-Ready Image Classifier

## Project Scenario

You are the ML engineer for **"Tamr Vision" (رؤية التمر)**, the automated grading system of a date-packing house in Qassim. The plant processes nine premium varieties and currently pays trained sorters to grade fruit visually at the line; misgraded batches trigger buyer complaints and re-sorting costs. Management has approved a pilot: a camera above the conveyor and a model that classifies each fruit's variety at line speed. Everything you built in Labs 1–6 is a component; the capstone is the integration plus a disciplined tuning campaign — take your fine-tuned classifier, sweep it, select the winner *with evidence*, evaluate it exactly once on the sealed test set, and ship it with a model card and full experiment lineage.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Working training pipeline (LO2, LO3):** the course engine (v2) training your model end-to-end on Tamr-9 with the frozen `splits.json`; overfit-one-batch self-test green before any tuning run; checkpointing with best/last semantics and demonstrated resume.
2. **Architecture and transfer decision (LO1, LO2, LO5):** a pretrained backbone fine-tuned with the staged recipe (discriminative LRs + warmup), *justified against* your from-scratch Lab 3 baseline — both numbers on the comparison table. Preprocessing contract honoured via `weights.transforms()`.
3. **Stabilised training recipe (LO4):** regularisation, normalisation handling, and LR schedule chosen deliberately; every non-default choice traceable to an ablation row or sweep evidence — no folklore settings.
4. **Tuning campaign (LO4, LO6):** ≥ 12 completed sweep runs (cohort sweep or your own) over at least lr, weight decay, and augmentation strength; hyperband or an explicit early-kill rule; winner selected from the W&B comparison view on the frozen **validation** split.
5. **Experiment tracking and reproducibility (LO6):** every run config-complete (config, git commit, data hash, backbone revision); the machine-swap test passes on your winning run; best-model artifact with lineage.
6. **Sealed-test evaluation (LO3, LO6):** exactly **one** evaluation of the selected model on the sealed test split (labels released by the instructor at Day 4 H4); report accuracy and per-class recall; the confusion matrix analysed — weakest variety pair identified with a hypothesis and a proposed next step.
7. **Shipping (LO5, LO6):** model pushed to a private Hugging Face Hub repo — safetensors weights, complete `MODEL_CARD.md` (base weights + pinned revision, preprocessing, data version, per-class metrics, licence, intended use, known limitations), and the W&B run URL cross-referenced.

**One extension (choose at least one):**
- **Line-speed check:** measured inference latency (batch 1 and batch 32, synchronised timing, CPU and GPU) against the 10 items/s line rate, with a backbone-size recommendation
- **Calibration lane:** reliability diagram + confidence threshold that routes low-confidence fruit to human graders, with the routed fraction quantified
- **Robustness probe:** evaluation under simulated line conditions (motion blur, exposure shift) with per-corruption accuracy deltas
- **10%-data study:** repeat your winning recipe at 10% of Tamr-9; report the transfer-learning resilience curve
- **Grad-CAM evidence:** class-activation visualisations for three correct and three confused examples, connected to your confusion-matrix hypothesis

## Architecture (target state)

```
Tamr-9 (frozen splits.json, hash-versioned)
      │
      ▼
DataLoader (workers, pinned) ──► engine_v2 (AMP, accum, clip-after-unscale)
      │                                │
      │                        wandb.init(config: lr, wd, aug,
      │                                  git commit, data hash,
      ▼                                  backbone revision)
ResNet-50 (pretrained, staged fine-tune,          │
           discriminative LRs + warmup)           ▼
      │                                  W&B sweep (bayes + hyperband)
      ▼                                           │
best.pt ◄────── winner selected on VAL ◄──────────┘
      │
      ├──► ONE sealed-test evaluation (Day 4 H4) ──► per-class report
      ▼
HF Hub (private): safetensors + MODEL_CARD.md + W&B run URL
      └──► consumed by SDA-AIE-211 (deployment) / SDA-AIE-113 (next module)
```

## Deliverables

1. Repository link (course org) with full commit history across Labs 1–6 and the capstone
2. W&B project link: the sweep, the winning run (config-complete), and the exported comparison table
3. `best.pt` + Hub repo link with `MODEL_CARD.md`
4. `RESULTS.md`: baseline-vs-final table, sealed-test metrics with per-class recall, confusion-matrix analysis, extension results
5. 5-minute demo: live inference on 5 instructor-supplied images (including one deliberately ambiguous fruit), W&B lineage walkthrough, one question answered *from the tracking data alone*

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: Engine v2 + fine-tuned model tracked (Labs 5–6 integrated) | End Day 4 H2 | machine-swap test passes |
| M-B: Sweep complete, ≥ 12 runs, winner selected on val | End Day 4 H3 | comparison table exported |
| M-C: Winner confirmed/retrained; model card complete | Day 4 H4 (first half) | instructor releases sealed-test labels |
| M-D: ONE sealed-test evaluation + RESULTS.md | End Day 4 H4 | test-eval script run once, logged |
| M-E: Demo + submission | Day 4 H5 | rubric scoring live |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Training pipeline correctness | 15 | Self-test green, checkpoints + resume demonstrated, device-clean code | Loop correct; resume or self-test evidence thin | Broken loop symptoms; no self-test; hard-coded device |
| Transfer decision & model quality | 20 | Fine-tune beats scratch baseline by ≥ 8 pp; staged recipe; contract honoured; sealed-test acc ≥ 0.90 | Beats baseline; minor recipe flaws; test acc 0.85–0.90 | No baseline comparison; contract violated; test acc < 0.85 |
| Stabilisation & tuning evidence | 20 | Every non-default setting traced to ablation/sweep evidence; ≥ 12 informative runs; principled selection on val | Sweep run but selection partly folklore; some untraced settings | Shotgun configs; selection on test; < 6 runs |
| Tracking & reproducibility | 20 | Config-complete runs; machine-swap passes; data hash + revision + commit on every run; artifact lineage intact | Tracked but one lineage field missing; swap passes with help | Untracked runs; unlaunchable winner; no lineage |
| Evaluation discipline & analysis | 15 | Exactly one test eval; per-class recall; confusion pair analysed with hypothesis and next step | Test discipline kept; analysis shallow | Multiple test peeks; accuracy-only reporting |
| Shipping & demo | 10 | Hub repo complete (card, licence, cross-reference); crisp demo; answers from tracking data | Shipped with a thin card; demo works | No card; cannot run own model cold |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope scores ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade from **run evidence first** (W&B project, config completeness, sweep history), demo second — the course's thesis is that the tracking data speaks.
- The sealed-test single-evaluation rule is enforced technically: the test-eval script logs to the cohort project on first run; a second logged test eval caps the evaluation-discipline criterion at 70% absent a documented, legitimate reason (e.g., a broken checkpoint discovered mid-eval).
- Anti-pattern flags that cap the relevant criterion at 70%: val-set selection contaminated by test peeks; sweep runs that all share one seed *and* identical configs (run-count padding); model card copied from the template without per-class metrics; `main`-pinned (unpinned) backbone revision.
- Verify one reproducibility claim live per pair: pick a random run from their project and ask them to state, from the page alone, its data version and code commit.
- Expected score distribution mirrors the labs: pairs who kept the leaderboard discipline through Modules 3–6 typically land 80+; pairs who skipped OBSERVATIONS.md entries struggle on the evidence criteria — this is by design and worth saying out loud on Day 1.

## Bonus Tasks (for early finishers / distinction seekers)

1. **Two-backbone bake-off:** repeat the winning recipe on a mobile-class backbone; deliver the accuracy-vs-latency frontier chart against the 10 items/s line rate
2. **Preemption-proof sweep:** demonstrate a sweep agent surviving a mid-run kill via checkpoint-resume, with the W&B run showing the seam
3. **Determinism audit:** rung-2 reproduction of the winning run (determinism flags), reporting the bit-level match and the measured speed cost
4. **The handover pack:** a one-page README addressed to the SDA-AIE-211 cohort explaining exactly how to consume your Hub artefact for deployment — tested on a classmate

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** Why does stacking linear layers without nonlinearities add no capacity? → composition of linear maps is linear.
**Q2.** A 9-class classifier's loss starts at 2.20. Diagnose. → healthy — ln(9) ≈ 2.197 is the untrained baseline.
**Q3.** Which line of the two-layer backward pass kills dead ReLUs, and why? → the `⊙ ReLU′(z1)` mask — z1 < 0 everywhere zeroes δ1 forever.
**Q4.** `nn.CrossEntropyLoss` expects what as input, and what silently degrades if you feed softmax outputs? → logits; gradients get crushed by the double softmax — trains, but caps low.
**Q5.** What does `optimizer.zero_grad()` prevent, and which PyTorch design choice makes it necessary? → mixing stale gradients into the step; `.backward()` accumulates into `.grad` by design.
**Q6.** `model.eval()` vs `torch.no_grad()` — one sentence each. → eval switches layer behaviour (dropout/BN); no_grad stops graph recording and saves memory.
**Q7.** What belongs in a *resumable* checkpoint beyond model weights? → optimizer state, epoch, best metric, RNG state.
**Q8.** The overfit-one-batch test: what does passing prove, and what does it not prove? → the pipeline can learn (wiring correct); nothing about generalisation.
**Q9.** Parameters in `Conv2d(64, 128, kernel_size=3)` with bias? → 3·3·64·128 + 128 = 73,856.
**Q10.** Why do three stacked 3×3 convs beat one 7×7 at equal receptive field? → fewer parameters (27C² vs 49C²) plus two extra nonlinearities.
**Q11.** What does `y = F(x) + x` guarantee about gradient flow? → an identity path — ∂y/∂x = ∂F/∂x + I — so depth stops killing gradients.
**Q12.** Name one augmentation that is correct for date fruit and wrong for Arabic documents, and why. → horizontal flip — dates have no canonical orientation; mirrored text changes semantics.
**Q13.** Train loss 0.05, val loss rising since epoch 7 — regime and first two interventions? → overfitting; augmentation/weight decay + early stopping at best-val checkpoint.
**Q14.** Why does BatchNorm fail at batch size 2, and what is the drop-in fix? → batch statistics are noise at n=2; GroupNorm (per-sample, channel groups).
**Q15.** OneCycle underperforms mysteriously — the classic wiring bug and its diagnostic? → stepped per epoch instead of per batch; plot the actual lr vs step.
**Q16.** Feature extraction vs fine-tuning: pick for 400 similar-domain images, and name the BN trap in the frozen recipe. → feature extraction; BN running stats still update in train mode — freeze BN to eval.
**Q17.** What is the "preprocessing contract" and what happens when it is violated? → pretrained weights require their training-time transforms (size, normalisation); violations train and silently lose accuracy.
**Q18.** Why pin a Hugging Face model revision, and why prefer safetensors? → `main` moves — unpinned models are unpinned dependencies; pickle formats can execute code on load.
**Q19.** GPU utilisation sawtooths 90%→5% — the one-step diagnostic and the first fix? → time the DataLoader without the model; `num_workers` + pinned memory.
**Q20.** Under AMP, why must `clip_grad_norm_` come after `scaler.unscale_`? → otherwise the clip threshold applies to scaled gradients and is meaningless.

## Practical Assessments

**PA-1 — Rescue under the clock (30 min, Day 3, after Lab 4):** Given a fresh broken training config (different defects from Lab 4's — drawn from the course defect pool: lr/warmup, scheduler wiring, BN/batch-size, augmentation poison, eval-mode leak), produce a defect list from the curves, fix the top two by marginal gain, and show the improvement. Scored on: evidence-first diagnosis (40%), fix correctness and ordering (40%), ablation-row documentation (20%).

**PA-2 — The reproducibility interrogation (20 min, Day 4, after Lab 6):** Given another pair's W&B project, answer the model-risk reviewer's questions: which run produced the best model, on what data version, from what code, with what base model — and re-launch it from its config. Scored on: correct lineage reading (50%), successful re-launch (30%), audit-quality write-up (20%).

**PA-3 — Capstone:** the model-training project (rubric above) — the summative assessment of the course.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Labs (Labs 1–6, checkpoints + leaderboard entries + OBSERVATIONS.md) | 45% | checkpoint commits, expected outputs, instructor spot-checks |
| PA-1 + PA-2 | 10% | artefacts + notes |
| Quiz (10-question selection) | 5% | closed-book score |
| Model-training project (capstone) | 40% | rubric, evidence-first |

Labs + practical assessments + quiz constitute the catalog's **Labs** component (60%); the capstone is the catalog's **model-training project** component (40%). Badge issuance (Deep-learning badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical sweep histories or copied model cards across pairs are checked). The badge counts toward the AI Engineer Practitioner Certificate and unlocks SDA-AIE-113 / SDA-AIE-211.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone the course org repo; push all checkpoint tags (`lab1-start` … `lab6-start`) and every `sim-*` branch (`sim-softmax-twice`, `sim-dead-relu`, `sim-no-zero-grad`, `sim-eval-mode`, `sim-oom-logging`, `sim-hwc`, `sim-seq-first`, `sim-vflip-digits`, `sim-onecycle`, `sim-bn-tiny-batch`, `sim-wrong-norm`, `sim-bn-drift`, `sim-starved`, `sim-scaled-clip`)
- [ ] Verify the Tamr-9 bundle: images, `splits.json` (+ 10% variant), train-split statistics reproduce; **keep the sealed test labels off the shared drive** — they are released at Day 4 H4 only
- [ ] Dry-run all six labs end-to-end on one classroom GPU workstation **and** on the Colab/Kaggle fallback; confirm Days 1–2 run acceptably on CPU
- [ ] Pre-download ImageNet weights (torchvision cache) and the curated Hub models to the classroom cache; test `HF_HUB_OFFLINE=1` against the local mirror
- [ ] Create the cohort W&B team project `tamr-vision-<cohort>`; create the capstone sweep; test `WANDB_MODE=offline` + `wandb sync` for restricted networks
- [ ] Verify classroom network access (or mirrors) for: pypi, github.com, huggingface.co, wandb.ai; pre-pull everything that cannot be guaranteed live
- [ ] Print A4 posters: the four-regime curve atlas, the loop liturgy, the Hub sourcing checklist card, the two-computers bridge diagram
- [ ] Prepare the shared leaderboard (val accuracy per module, img/s) and the demo image set for Day 4 H5 (including the deliberately ambiguous fruit)
- [ ] Rehearse the four flagship demos: gradient autopsy (M1), zero_grad self-test flip (M2), filter/feature-map walk (M3), the throughput diagnostic arc (M6)

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + git + a GitHub account (SSH or PAT auth) + a free W&B account + a free Hugging Face account
- [ ] `pip install torch torchvision --index-url` per the course lock file (CUDA build matching classroom GPUs; CPU build acceptable for Days 1–2 self-study)
- [ ] `pip install wandb huggingface_hub numpy matplotlib pytest torchinfo pillow`
- [ ] Clone the course repo; run `make doctor` (validates versions, CUDA visibility, W&B/HF login, dataset checksum — prints ✓/✗ per line)
- [ ] Verify GPU access path: classroom workstation credentials **or** Colab account tested with the provided smoke notebook
- [ ] Optional but recommended: VS Code + Python extension; `nvidia-smi` familiarity note attached

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| CUDA build/driver mismatch on personal laptops | High | Steer to classroom workstations or Colab; never debug driver stacks in class time |
| Maths anxiety at the Day 1 derivation | High | Pairing strategy (strong-maths with strong-Python); the six-step scaffold; emphasise it is done *once*, then autograd owns it |
| `Expected all tensors on the same device` | High | The M6 threading rule taught early: one `device` variable; audit tensor creation sites |
| DataLoader hangs/errors on Windows (`num_workers>0`) | Medium | `if __name__ == "__main__"` guard, importable transforms — M2's lesson; workers=0 as temporary fallback on Days 1–2 |
| W&B/Hub blocked by network or proxy | Medium | `WANDB_MODE=offline` + later sync; local HF mirror; both rehearsed at T-minus 1 week |
| Colab session resets losing state | Medium | The engine's checkpoint-resume *is* the fix — turn it into a teaching moment |
| Pairs skipping the self-test/batch-grid rituals to "save time" | Medium | Make both hard gates for lab sign-off; they repay their cost by Day 3 |
| OOM panic during fine-tuning/sweeps | Medium | The fix ladder poster: batch down → AMP → accumulation; decoded-OOM screenshot in M6 assets |
| Fast cohorts finishing labs early | Low | Every lab ships a fast-finisher task; bonus tasks queue for the capstone |
| Sealed-test labels leaking early via well-meaning sharing | Low | Labels exist only on the instructor machine until Day 4 H4; the eval script logs first use |

## Timing Recommendations

- **Protect at full length:** Lab 1 Part A (the derivation — the course's foundation), Lab 4 (the diagnostic hour — the most transferable skill), and capstone assembly (Day 4 H3–H4). Cut discussion, not build time.
- **Compressible under pressure:** M3's RNN hour can shrink to 30 minutes (mini-lab intact, gating theory compressed — SDA-AIE-113 re-covers sequences); M6's GPU theory lands through the lab and can lose 15 minutes of lecture.
- **Overrun-prone:** Labs 3 and 5 (first real images; first fine-tune) — publish checkpoint tags so stragglers fast-forward (`git checkout lab5-start`), and enforce the pairing rotation so no pair is stuck alone.
- **Hard rule:** the sweep must launch by end of Day 4 H2 so it runs through the break; and sealed-test evaluation happens in H4, never earlier — the discipline is the lesson.
- For strong cohorts: pull the calibration-lane extension into mandatory scope and deepen the M5 licence exercise with a second contested model. For weak cohorts: run Lab 4's diagnosis as a guided whole-class exercise, never drop the ablation table itself.

## Discussion Prompts (use during transitions)

1. "What is the most expensive model your organisation ever trained — and could anyone reproduce it today?"
2. "Your model is 94% accurate. The sorter it replaces is 91% but explains her decisions. What does the packing house actually buy when it buys your model?"
3. "Which failure from this course's sim- branches have you already shipped to production without knowing it?"
4. "A pretrained model is someone else's training run. What do you owe the person who consumes *yours*?"
5. "GPU hours are budget. Which habit from this week saves the most riyals per month — and which merely feels productive?"
6. "If the regulator can query your W&B project, what does it testify about your team?"

## Wrap-up (final day, last 15 minutes)

- Map each capstone rubric criterion to the module that taught it (one slide): pipeline ← M1/M2, model ← M3/M5, recipe ← M4, tracking ← M6 — the course was one project all along.
- Forward pointers: **SDA-AIE-113** (Natural Language Processing) assumes the tensors/training/transfer fluency built here and re-meets fine-tuning at LLM scale; **SDA-AIE-211** (MLOps & Deployment) consumes *exactly* the Hub artefact + lineage shipped today. The deep-learning badge is the gateway to all Specialist AI Engineer modules.
- Collect: repo URLs, W&B project links, Hub repo links, RESULTS.md; issue badge recommendations within 5 working days.
- Close on the golden thread: Day 1 was a hand-derived gradient on paper; Day 4 is a swept, tracked, shipped classifier. The distance between those two artefacts is the course — and every step of it is in their own git history.

---

*End of instructor package. All code samples target Python 3.12, PyTorch ≥ 2.3, torchvision ≥ 0.18, wandb ≥ 0.17, huggingface_hub ≥ 0.23. Verify pinned versions in the course lock file before each delivery; regenerate throughput reference numbers when classroom GPU hardware changes.*
