# Skills

Research skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Tools for autonomous iteration, scientific visualization, bibliography management, image generation, and more.

```bash
claude plugin add cailmdaley/skills
```

## What's here

### ralph-loops — Autonomous iteration loops

The key insight: **context rot kills autonomous agents.** When an LLM works too long in one context, it accumulates bias — confirming its own earlier choices, over-fitting to its own framing, losing the ability to see what's actually there.

Ralph solves this with *fresh-context loops*. Each iteration: survey the actual state of the system, contribute meaningful work, update state discoverably, exit. The next iteration starts clean — fresh eyes on the real state of things.

Give it a markdown spec describing the desired state (not a checklist), and it loops until reality matches the spec. Each pass uses ~50% of the context window for substantial work before exiting.

Tell Claude to "use the ralph-loops skill to help me write a spec for [your goal]." It will draft a spec from the template, refine it with you, then launch a tmux session that loops autonomously.

The pattern is adapted from [Geoffrey Huntley's Ralph Wiggum](https://ghuntley.com/ralph/) — named for the Simpsons character who cheerfully does his own thing, oblivious to context. Each iteration is Ralph: no memory of what came before, just fresh eyes on the current state.

### data-visualization — Scientific figure design

A decision framework synthesizing Bertin, Cleveland, Tufte, Cairo, Wilke, and Knaflic. Routes from data type to visualization form, with cosmology-specific conventions (power spectra, covariance matrices, triangle plots, sky maps). Includes a visualization catalog, color palette reference, and design system.

### implementing-code — Scientific coding standards

Opinionated approach to research code: conceptual density, concise conditionals, natural line breaking. Write it right the first time — clean, correct, no post-hoc cleanup needed.

### managing-bibliography — arXiv + ADS citation management

Read full paper source from arXiv, fetch BibTeX from NASA ADS, generate citation keys, append to your `.bib` file. Requires `$ADS_API_TOKEN`.

### nano-banana — Image generation via Gemini CLI

Generate and edit images using Gemini CLI with persistent visual memory via KV cache warmth. Two warm caches (Gemini's KV cache + Claude's context) enable iterative refinement. Includes transparency extraction via difference matting.

Requires [Gemini CLI](https://github.com/google-gemini/gemini-cli) with the [nanobanana extension](https://github.com/gemini-cli-extensions/nanobanana).

### pocket-tts — Local text-to-speech

Speak text aloud using pocket-tts server with streaming audio. macOS only.

Requires: `pip install pocket-tts`, `brew install ffmpeg`, a voice file at `~/.config/pocket-tts/default-voice.wav`.

## License

MIT
