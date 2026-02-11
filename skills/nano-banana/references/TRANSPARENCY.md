# Transparency via Difference Matting

Gemini cannot output true alpha transparency. Asking for "transparent PNG background" gives you a white, black, or checkered background baked in.

The workaround: **difference matting** using the edit capability.

## The Workflow

### Step 1: Generate on White

Generate the asset with a standard prompt:

```bash
gemini --yolo "/generate 'A complex futuristic UI, HUD-like, with different components, on a pure solid white #FFFFFF background'"
```

### Step 2: Edit to Black

Take that output and feed it back with an edit request:

```bash
gemini --yolo --resume latest -p "/edit nanobanana-output/your_image.png 'Change the white background to a solid pure black #000000. Keep everything else exactly unchanged.'"
```

Because the model tries to preserve the subject during edits, you end up with two perfectly aligned images: one on white, one on black.

### Step 3: Apply Difference Matting

Use both images to create the final transparent image:

```bash
python <base>/scripts/extract_alpha.py input-white.png input-black.png output.png
```

## How It Works

The math compares pixels between the two images:

- **100% opaque pixels** look identical on white and black (distance = 0)
- **100% transparent pixels** show the background exactly (distance = max)
- **Semi-transparent pixels** fall between, allowing alpha recovery

The formula:
```
alpha = 1 - (pixelDistance / maxBackgroundDistance)
```

Color recovery uses the black version, dividing by alpha to un-premultiply.

## Results

- **Shadows work**: Preserved as low-alpha black pixels
- **Glass/transparency**: Semi-transparent areas come out correctly
- **No halo**: Unlike chroma keying, no colored fringe

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Noisy transparent areas | Asset changed between edits — prompt more explicitly |
| Partial transparency wrong | Check that both images are same dimensions |
| Subject changed during edit | Use stronger language: "ONLY change background, keep EVERYTHING else identical" |
