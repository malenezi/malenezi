# Enhanced_Photos

60 graduate portraits from `assets/` restored and upscaled. **Originals are untouched.**
Filenames and file formats are identical to the source, so these are drop-in replacements.

## What was and was not processed

| | count | |
|---|---|---|
| Portraits enhanced | 60 | see `included_portraits.jpg` |
| Logos / wordmarks skipped | 117 | see `excluded_logos_1.jpg`, `excluded_logos_2.jpg` |

Selection was by face detection (OpenCV YuNet), not by filename — many files named after a
person are that person's **personal brand logo**, not a photo, and were correctly left alone.
Two niqab portraits that face detection cannot box (`rawan-althubyani`, `rayah-aldawsari`)
were added by visual review.

## Pipeline (deterministic — no generative AI, every pixel derives from the original)

1. **Orientation** — EXIF transpose applied, then stripped; aspect ratio preserved exactly.
2. **Noise / artifact reduction** — non-local-means, strength set per image from a measured
   noise estimate and JPEG bits-per-pixel. 28% of the original grain is deliberately kept.
3. **White balance** — cast estimated from near-neutral pixels only (not gray-world, which
   drags skin tones), applied at 55% strength and hard-capped at ±11% per channel.
4. **Dynamic range** — black/white point recovered at 55% strength with a soft highlight
   shoulder, so nothing clips.
5. **Upscale** — 2x Lanczos performed in **linear light** (gamma-correct, so no edge darkening
   or halos), capped at 1600px on the long side.
6. **Local contrast** — mild CLAHE (clip 1.25) on the L channel only, blended 45%, and
   attenuated by a further 55% over detected faces.
7. **Sharpening** — edge-masked unsharp on luminance only. Flat areas (skin, backgrounds) are
   masked out, overshoot is hard-limited to prevent halos, and the amount is reduced 42% over
   faces. Colour channels are never sharpened.
8. **Save** — JPEG q95 with no chroma subsampling / PNG / WebP q95, matching the source.

Faces are detected **only to reduce processing over facial skin** — never to reconstruct,
reshape, or synthesise any facial detail.

## Verification (`enhancement_report.csv`)

Each output was resampled back to source dimensions and compared to the original over the
detected face region:

- **Face SSIM** — median 0.973, minimum 0.905 (structure essentially identical)
- **Face colour delta (dE76)** — median 3.26, max 6.65 (tone/contrast, not a colour rewrite)
- **Skin tone drift (a*b*)** — median 1.11, max 3.27 (imperceptible)
- **New clipped highlights** — max 0.08 percentage points
- **Aspect ratio / orientation / format preserved** — 60/60

`before_after_all.jpg` shows every pair; `face_crops_1to1.jpg` shows 1:1 face crops of the
six images that changed most.
