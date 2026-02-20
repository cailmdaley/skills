---
name: confer
description: >
  Consult the other coding agent — Claude Code calls Codex, Codex calls Claude
  Code. Use for second opinions, code review, consensus, or dispatching tasks
  to the other agent. Two modes: one-shot for quick questions, tmux session for
  extended collaboration.
  Triggers: "confer", "ask claude", "ask codex", "second opinion", "get a
  review from", "use claude for", "use codex for", "dispatch to".
---

# Confer

Call the other agent. If you're Claude Code, call Codex. If you're Codex, call Claude Code.

## One-Shot

For quick questions, reviews, or dispatched tasks.

**Claude Code → Codex:**
```bash
codex exec --dangerously-bypass-approvals-and-sandbox "<prompt>"
```

**Codex → Claude Code:**
```bash
claude -p --dangerously-skip-permissions "<prompt>"
```

Both return output to stdout. Use this for:
- Second opinions on code or architecture
- Quick reviews ("review this diff for correctness")
- Dispatching a well-scoped task ("refactor X using pattern Y")

## Tmux Session

For extended collaboration where back-and-forth is needed.

```bash
tmux new-session -d -s confer -c "$(pwd)"
```

**Send a message (two steps — Enter must be separate):**
```bash
tmux send-keys -t confer "<command or prompt>" ""
tmux send-keys -t confer Enter
```

**Read the response:**
```bash
tmux capture-pane -t confer -p -S -50
```

Start the other agent in the session, then send follow-up prompts with send-keys. This mode suits open-ended collaboration: iterating on a design, working through a problem together, or anything that needs multiple exchanges.

## When to Use Which

**One-shot** — You have a clear question or task. Fire and forget.

**Tmux** — You need a conversation. Multiple rounds, evolving context, genuine collaboration.
