---
name: ralph-loops
description: >
  High-throughput autonomous iteration. Survey → contribute → exit → repeat.
  Use when: (1) spec is well-defined, (2) work can be parallelized,
  (3) fresh perspective each iteration prevents bias accumulation.
  Triggers: "ralph-loops", "ralph", "autonomous", "loop", "iterate".
---

# Ralph Loops

Meditative iteration toward a desired state. Each pass: survey freely, work until you've used roughly half your context, update state discoverably, exit. The loop continues until the state is achieved.

## Two Modes

**If your system prompt contains a spec**, you're inside the loop — skip to [Iterating](#iterating) below.

**If not**, you're crafting or launching. Read [references/crafting-specs.md](references/crafting-specs.md) for how to shape specs, then launch with `<base>/scripts/ralph <spec-file>`.

## Iterating

Your spec is in the system prompt above. This section tells you how to work.

### Loop

1. **Survey** — Fresh eyes. Explore agents, git log, tests. You decide what to check.
2. **Contribute** — Work to improve the state. Use roughly 50% of your context window — substantial work, not quick fixes.
3. **Update** — Before exiting: update CLAUDE.md if warranted, commit your work.
4. **Exit** — `kill $PPID`

### Important

**State, not checklist.** The spec describes what "done" looks like. Survey reality, decide what's highest value, work on that. No prescribed phases.

**Discoverable updates.** Commits, test results, documentation — not notes or progress files. The next iteration finds what changed by inspecting the system.

**Pointers, not snapshots.** The spec says where to check state, not what the state currently is. If you learn something, update the spec's *context* or *desired state* sections — don't leave comments that bloat the prompt.

**You have authority.** Trust the spec, don't ask permission. Make substantial contributions and document them.

**Batch questions when stuck.** When you encounter genuine uncertainty — ambiguous requirements, competing approaches, places where user context would change your direction — note them and keep working on what you *can* resolve. Before exiting, batch accumulated questions into a single `AskUserQuestion` (up to 4 questions). These should be high-leverage: choices where user input redirects substantial work. Don't ask about things you can figure out; don't ask one-at-a-time. Collect, then batch, then exit.

### Exit Rules

If you **made substantial contributions,** surface any batched questions via `AskUserQuestion`, then `kill $PPID`. Do NOT close the spec — the loop continues. If you have not been able to find any contributions toward the state in this session, update the spec's YAML frontmatter to `status: closed` with a summary of what was accomplished.

## Creating a Spec

See [references/crafting-specs.md](references/crafting-specs.md).

---

Pattern adapted from [Ralph Wiggum](https://ghuntley.com/ralph/).
