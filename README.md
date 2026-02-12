# Skills

Agent skills for research work — autonomous iteration, scientific visualization, bibliography management, image generation, and more. Currently packaged as a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin, but the skills themselves are just markdown files that any coding agent can use.

**Read each skill before you run it.** These skills shape how your agent works — some, like ralph-loops, run agents with full permissions in autonomous loops. Understand what a skill does before activating it.

**These reflect one person's workflow, not universal best practices.** Fork the repo, delete what doesn't fit, rewrite what almost fits. The best skills are the ones you've made your own.

```bash
# Claude Code
claude plugin marketplace add cailmdaley/skills
claude plugin install research-skills
```

## What's here

### ralph-loops — Autonomous iteration loops

Fresh-context loops: survey, contribute, exit, repeat. Each iteration gets the spec as system prompt and starts clean. Give it a markdown spec describing the desired state, and it loops in a tmux session until reality matches — attach to watch, steer, or update the spec mid-run.

Tell Claude to "use the ralph-loops skill to help me write a spec for [your goal]." Pattern adapted from [Geoffrey Huntley's Ralph Wiggum](https://ghuntley.com/ralph/).

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
