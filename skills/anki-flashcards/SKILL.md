---
name: anki-flashcards
description: Add flashcards to Anki via AnkiConnect API. Use when the user asks to save vocabulary, concepts, definitions, or any front/back card information while reading or studying. Triggers on "add to anki", "flashcard", "remember this", "save this word", or similar requests to save content for later review. Requires AnkiConnect addon installed (code 2055492159) in Anki and the Anki application running.
model: claude-haiku-4-5
---

# Anki Flashcards

Add cards to Anki decks via AnkiConnect (localhost:8765).

## Workflow

When a user wants to save content as a flashcard:

1. **Extract content**: Get front (prompt/term) and back (answer/definition) from context
2. **Determine deck**: Use deck name from context if clear, otherwise ask the user. Default deck is "Default"
3. **Suggest tags**: Recommend tags based on content (language, topic, source)
4. **Execute**: Run the script with the determined values
5. **Confirm**: Report success with the card details

## Usage Examples

**Vocabulary:**
- User: "add 'garnement' to anki"
- Front: garnement | Back: rascal, scamp (archaic)
- Deck: French (or ask)
- Tags: french, vocabulary

**Concept:**
- User: "flashcard: celui qui = the one who"
- Front: celui qui | Back: the one who (demonstrative + relative pronoun)
- Deck: French (or ask)
- Tags: french, grammar

**Auto-tagging:** Infer tags from context (language, topic, material source)

## Quick Command

```bash
python3 <base>/scripts/add_card.py -d "Deck Name" -f "front" -b "back" -t tag1 tag2
```

## Important Notes

- AnkiConnect addon must be installed (code: 2055492159)
- Anki application must be running
- Script auto-creates deck if it doesn't exist
- Duplicates are rejected by default
- If API fails, ask user to verify Anki is running
