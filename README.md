# Skills

Research skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

```bash
claude plugin add cailmdaley/skills
```

## What's here

### ralph — Autonomous iteration loops

The key insight: **context rot kills autonomous agents.** When an LLM works too long in one context, it accumulates bias — confirming its own earlier choices, over-fitting to its own framing, losing the ability to see what's actually there.

Ralph solves this with *fresh-context loops*. Each iteration: survey the actual state of the system, contribute meaningful work, update state discoverably, exit. The next iteration starts clean — fresh eyes on the real state of things.

Give it a markdown spec describing the desired state (not a checklist), and it loops until reality matches the spec. Each pass uses ~50% of the context window for substantial work before exiting.

```bash
# Create a spec from the template
cp ~/.claude/plugins/skills/skills/ralph/templates/spec.md my-feature.md
# Edit the spec...
# Launch
~/.claude/plugins/skills/skills/ralph/scripts/ralph my-feature.md
```

### managing-bibliography — arXiv + ADS citation management

Read full paper source from arXiv, fetch BibTeX from NASA ADS, generate citation keys, append to your `.bib` file. Requires `$ADS_API_TOKEN`.

### data-visualization — Scientific figure design

A decision framework synthesizing Bertin, Cleveland, Tufte, Cairo, Wilke, and Knaflic. Routes from data type to visualization form, with cosmology-specific conventions (power spectra, covariance matrices, triangle plots, sky maps). Includes a visualization catalog, color palette reference (Porch Morning aesthetic + perceptually uniform options), and design system.

### implementing-code — Scientific coding philosophy

Opinionated approach to research code: conceptual density, concise conditionals, natural line breaking. Write it right the first time — clean, correct, no post-hoc cleanup needed.

### nano-banana — Image generation via Gemini CLI

Generate and edit images using Gemini CLI with persistent visual memory via KV cache warmth. Two warm caches (Gemini's KV cache + Claude's context) enable iterative refinement. Includes transparency extraction via difference matting.

Requires [Gemini CLI](https://github.com/google-gemini/gemini-cli) with the [nanobanana extension](https://github.com/gemini-cli-extensions/nanobanana).

### pocket-tts — Local text-to-speech

Speak text aloud using pocket-tts server with streaming audio. macOS only.

Requires: `pip install pocket-tts`, `brew install ffmpeg`, a voice file at `~/.config/pocket-tts/default-voice.wav`.

### anki-flashcards — Flashcard creation

Add cards to Anki via AnkiConnect while reading or studying. Extracts front/back content from context, suggests tags, creates cards.

Requires: Anki running with [AnkiConnect](https://ankiweb.net/shared/info/2055492159) addon installed.

## License

MIT
