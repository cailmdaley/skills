---
name: pocket-tts
description: >
  Speak text aloud using local TTS. Use when the user wants to hear something read out loud, spoken, voiced, narrated, or audibly rendered. Triggers on: "read this aloud", "say this", "speak", "out loud", "tell me [verbally]", "narrate", "voice this", "hear this", "read to me", "TTS", or any request to audibly render text.
---

# Pocket TTS

Local text-to-speech via pocket-tts server. Streams audio for low latency. **macOS only** (uses `afplay` as fallback).

## Prerequisites

```bash
pip install pocket-tts
brew install ffmpeg
```

## Quick Reference

```bash
# Ensure server is running (do this first)
curl -s http://localhost:8321/health > /dev/null 2>&1 || {
  pocket-tts serve --voice ~/.config/pocket-tts/default-voice.wav --port 8321 > /dev/null 2>&1 &
  sleep 4
}

# Speak with streaming playback (audio starts immediately)
curl -s -X POST http://localhost:8321/tts -F "text=Hello world" -o - | ffplay -nodisp -autoexit -loglevel quiet -

# Or with temp file (if ffplay unavailable)
curl -s -X POST http://localhost:8321/tts -F "text=Hello world" -o /tmp/speak.wav && afplay /tmp/speak.wav && rm /tmp/speak.wav
```

## Architecture

Always use the server — it keeps the model and voice embedding warm in memory.

**Port:** 8321 (avoids conflicts with common services)

**Default voice:** Loaded once at server start from `~/.config/pocket-tts/default-voice.wav`

**Streaming:** The `/tts` endpoint returns chunked WAV. With `ffplay`, audio starts playing while generation continues.

## Changing Voices

Per-request (server keeps default warm, but can generate with others):

```bash
curl -s -X POST http://localhost:8321/tts -F "text=Hello" -F "voice_url=jean" -o - | ffplay -nodisp -autoexit -loglevel quiet -
```

**Built-in voices:** alba, marius, javert, jean, fantine, cosette, eponine, azelma

**Custom:** Any http://, https://, or hf:// URL

To change the default, restart server with different `--voice`.

## Creating Custom Voices

```bash
# Extract 30s clip from source (pocket-tts truncates to 30s anyway)
ffmpeg -y -ss START_SECONDS -t 30 -i input.mp3 -ar 24000 -ac 1 ~/.config/pocket-tts/default-voice.wav
```

## Troubleshooting

**Server not responding:** Check if process died, restart with serve command

**Slow first response:** Server needs ~4s to load model on first start

**No audio:** Ensure ffplay (from ffmpeg) or afplay (macOS built-in) is available
