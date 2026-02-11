# Nano Banana CLI Reference

Full command reference for the Gemini CLI nanobanana extension.

## Installation

```bash
gemini extensions install https://github.com/gemini-cli-extensions/nanobanana
```

## Session Management

```bash
# First generation — starts fresh session
gemini --yolo "/generate 'blue circle on white background'"

# Subsequent generations — resume for warm cache
gemini --yolo --resume latest -p "/generate 'same circle but with red outline'"

# List sessions
gemini --list-sessions

# Start completely fresh
gemini --yolo "/generate 'new concept'"
```

**CRITICAL**: Always use `--resume latest -p "prompt"` for iterations. This keeps Gemini's KV cache warm.

Sessions are per-directory. Different directories = different visual memories.

## Common Flags

| Flag | Purpose |
|------|---------|
| `--yolo` | **Required.** Auto-approve tool actions |
| `--resume latest -p "..."` | Keep KV cache warm for iterations |
| `--preview` | Auto-open generated images |

## Commands

### /generate — Image Creation

```bash
/generate "prompt text"
```

| Flag | Values | Default |
|------|--------|---------|
| `--count` | 1-8 | 1 |
| `--styles` | photorealistic, watercolor, oil-painting, sketch, pixel-art, anime, vintage, modern, abstract, minimalist | — |
| `--variations` | lighting, angle, color-palette, composition, mood, season, time-of-day | — |
| `--format` | grid, separate | separate |
| `--seed` | integer | random |
| `--preview` | — | false |

**Examples:**
```bash
/generate "mountain landscape" --styles="watercolor" --count=3
/generate "product photo" --variations="lighting,angle" --format=grid
/generate "logo concept" --seed=42  # reproducible
```

### /edit — Image Modification

```bash
/edit image_file.png "edit instruction"
```

Modifies existing images using natural language. Respects session context.

### /restore — Image Enhancement

```bash
/restore old_photo.jpg "fix scratches and color fade"
```

Restores and enhances damaged or old photographs.

### /icon — Icon Generation

```bash
/icon "description"
```

| Flag | Values | Default |
|------|--------|---------|
| `--sizes` | comma-separated pixels | "16,32,64,128" |
| `--type` | app-icon, favicon, ui-element | app-icon |
| `--style` | flat, skeuomorphic, minimal, modern | flat |
| `--format` | png, jpeg | png |
| `--background` | transparent, white, black, color | transparent |
| `--corners` | rounded, sharp | rounded |

**Example:**
```bash
/icon "productivity app checkmark" --sizes="32,64,128,256" --style=minimal --corners=rounded
```

### /pattern — Pattern & Texture Creation

```bash
/pattern "description"
```

| Flag | Values | Default |
|------|--------|---------|
| `--size` | "WxH" pixels | "256x256" |
| `--type` | seamless, texture, wallpaper | seamless |
| `--style` | geometric, organic, abstract, floral, tech | geometric |
| `--density` | sparse, medium, dense | medium |
| `--colors` | mono, duotone, colorful | colorful |
| `--repeat` | tile, mirror | tile |

**Example:**
```bash
/pattern "hexagonal tech grid" --style=tech --density=dense --colors=mono
```

### /story — Sequential Image Generation

```bash
/story "narrative description"
```

| Flag | Values | Default |
|------|--------|---------|
| `--steps` | 2-8 | 4 |
| `--type` | story, process, tutorial, timeline | story |
| `--style` | consistent, evolving | consistent |
| `--layout` | separate, grid, comic | separate |
| `--transition` | smooth, dramatic, fade | smooth |

**Example:**
```bash
/story "coffee brewing process" --type=process --steps=6 --layout=grid
```

### /diagram — Technical Diagram Generation

```bash
/diagram "description"
```

| Flag | Values | Default |
|------|--------|---------|
| `--type` | flowchart, architecture, network, database, wireframe, mindmap, sequence | flowchart |
| `--style` | professional, clean, hand-drawn, technical | professional |
| `--layout` | horizontal, vertical, hierarchical, circular | vertical |
| `--complexity` | simple, detailed, comprehensive | detailed |
| `--colors` | mono, accent, categorical | accent |
| `--annotations` | minimal, detailed | minimal |

**Example:**
```bash
/diagram "user authentication flow" --type=flowchart --style=clean --layout=horizontal
```

### /nanobanana — Natural Language Interface

Open-ended command for flexible operations without specific syntax:

```bash
/nanobanana create a logo for my tech startup
/nanobanana I need 5 different versions of a cat illustration
/nanobanana make the previous image more vibrant
```

## Rate Limits

The CLI has a **separate, more generous quota pool** than the API:

- Google's stated goal: "deliver the best possible experience at the keyboard"
- Uses a dynamic blend of Pro and Flash models
- Dramatically higher free-tier limits than API

If you're hitting API limits, switch to CLI.
