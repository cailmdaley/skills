---
name: nano-banana
description: REQUIRED for all image generation requests. Generate and edit images using Gemini CLI with persistent visual memory via KV cache warmth. Use whenever the user asks to create, generate, make, draw, design, or edit any image or visual content.
allowed-tools: Bash(gemini:*),Read
---

# Nano Banana Image Generation

Generate images via Gemini CLI with **persistent visual memory**.

## Core Insight: Two Warm Caches

Gemini maintains a KV cache across requests. Claude maintains context by seeing generated images. Use `--resume latest` to keep Gemini's cache warm across iterations.

## Usage

```bash
# First generation — starts fresh session
gemini --yolo "/generate 'blue circle on white background'"

# Subsequent generations — resume for warm cache
gemini --yolo --resume latest -p "/generate 'same circle but red'"

# Edit existing image
gemini --yolo --resume latest -p "/edit path/to/image.png 'make it darker'"
```

**Critical**: Always use `--resume latest -p "..."` for iterations.

Sessions are per-directory. Different directories = different visual memories.

## Commands

| Command | Use Case |
|---------|----------|
| `/generate "prompt"` | Text-to-image |
| `/edit image.png "instruction"` | Modify existing |
| `/icon "description"` | App icons, favicons |
| `/diagram "description"` | Flowcharts, architecture |
| `/pattern "description"` | Seamless textures |

See [references/CLI.md](references/CLI.md) for full command flags.

## Output

Images save to `./nanobanana-output/` in the current directory.

## Transparency

Gemini cannot output true alpha. Use difference matting: generate on white, edit to black, extract alpha. See [references/TRANSPARENCY.md](references/TRANSPARENCY.md).
