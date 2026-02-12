# Crafting Ralph Loops Specs

Shape the spec interactively with the user. Draft first — an imperfect draft invites better feedback than an empty page.

## Workflow

1. **Study** — Read relevant files. Understand the codebase before asking questions.

2. **Draft** — Get clay on the wheel. Create a markdown file using the template:
   ```bash
   cp <base>/assets/spec.md my-spec.md
   ```
   Fill in what you can: goal, desired state, pointers. Don't wait until it's perfect.

3. **Refine** — Show the draft, get feedback, revise. The loop:
   - User marks up the spec (inline edits, comments, questions)
   - Read their feedback carefully — revise, discuss, or use AskUserQuestion for structured choices
   - Repeat until the spec feels solid

   What makes a solid spec:
   - What's the goal? (one sentence)
   - How do you know it's done by inspecting the system?
   - Which files/patterns should iterations follow?

   Describe the state well and scope becomes implicit. Write a constitution, not a rulebook — trust iterations to make good decisions.

Don't rush crystallization. A well-shaped spec runs itself.

## Launching

```bash
<base>/scripts/ralph <spec.md> [-- extra-flags...]
```

This creates a tmux session that loops while the spec's YAML frontmatter has `status: open` or `status: active`. Each iteration gets the spec as system prompt and activates the ralph-loops skill.

Session: `ralph-<spec-name>`. Attach: `tmux attach -t ralph-<spec-name>`.

**For visual work (UI, CSS, frontend):** Add `--chrome` so iterations can use the Claude Chrome extension to interact with the browser:
```bash
<base>/scripts/ralph my-spec.md -- --chrome
```

Without this, iterations can only check code — they can't see what it looks like.

## Writing Good Specs

**Point to existing patterns.** Reference actual implementations, not abstractions. Iterations that see real code build coherently on it. The more specific your pointers, the more organized the codebase stays.

**Watch and tune.** Attach to the session. When iterations drift or struggle, that's signal — update the spec. Each misstep teaches you something. Examine the spec, not the tool.

**Expect early stumbles.** The first iterations may bruise. That's tuning. Update the spec with clearer instructions, tighter constraints. Failures become predictable and addressable.

## Anti-patterns

**Checklists.** "1. Add X, 2. Add Y, 3. Test" — iterations race through without judgment. Instead: "The system should have X and Y, verified by tests."

**Snapshots.** "Currently 50 files need migration" — stale immediately. Instead: "Check `grep -r 'old_pattern'` for remaining work."

**Vague done.** "Make it better" — when does iteration stop? Instead: "All tests pass, no lint errors, coverage above 80%."

**Over-specification.** Prescribing how instead of what. Trust iterations to find good solutions.
