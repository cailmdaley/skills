# Skills

Agent skills for research work — autonomous iteration, scientific visualization, bibliography management, image generation, and more. Currently packaged as a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin, but the skills themselves are just markdown files that any coding agent can use.

**Read each skill before you run it.** These skills shape how your agent works. **ralph-loops and confer run agents with no permission gates** — they bypass all approval checks and sandboxing. Understand what a skill does before activating it.

**These reflect one person's workflow, not universal best practices.** Fork the repo, delete what doesn't fit, rewrite what almost fits. The best skills are the ones you've made your own.

```bash
# Claude Code
claude plugin marketplace add cailmdaley/skills
claude plugin install research-skills

# Codex (no plugin system — symlink the skills directory)
git clone https://github.com/cailmdaley/skills.git ~/.local/share/skills
ln -s ~/.local/share/skills/skills/* ~/.agents/skills/
```

## What's here

### constitution + ralph-loops — Autonomous iteration

Two skills that work together. **constitution** is the design document — a markdown spec describing the desired state, written to outlast any single iteration. **ralph-loops** is the execution engine — fresh-context loops that survey reality, contribute, and exit, repeating until the constitution is satisfied.

Use the **constitution** skill to draft a spec: "use the constitution skill to help me write a spec for [your goal]." Then launch with the included `ralph` script, which runs in a tmux session with support for both Claude Code and Codex backends. Attach to watch, steer, or update the spec mid-run.

Pattern adapted from [Geoffrey Huntley's Ralph Wiggum](https://ghuntley.com/ralph/).

### confer — Cross-agent collaboration

Consult the other coding agent — Claude Code calls Codex, Codex calls Claude Code. One-shot mode for quick questions, reviews, or dispatched tasks; tmux session mode for extended back-and-forth collaboration.

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
