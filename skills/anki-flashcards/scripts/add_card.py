#!/usr/bin/env python3
"""Add a flashcard to Anki via AnkiConnect API."""

import argparse
import json
import urllib.request


def anki_request(action: str, **params) -> dict:
    """Send request to AnkiConnect."""
    request_data = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request("http://localhost:8765", request_data)
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read())
    if result.get("error"):
        raise Exception(result["error"])
    return result.get("result")


def add_card(deck: str, front: str, back: str, tags: list[str] | None = None) -> int:
    """Add a basic card to a deck. Returns note ID."""
    note = {
        "deckName": deck,
        "modelName": "Basic",
        "fields": {"Front": front, "Back": back},
        "options": {"allowDuplicate": False},
        "tags": tags or [],
    }
    return anki_request("addNote", note=note)


def ensure_deck(deck: str) -> None:
    """Create deck if it doesn't exist."""
    anki_request("createDeck", deck=deck)


def main():
    parser = argparse.ArgumentParser(description="Add flashcard to Anki")
    parser.add_argument("--deck", "-d", required=True, help="Deck name")
    parser.add_argument("--front", "-f", required=True, help="Front of card")
    parser.add_argument("--back", "-b", required=True, help="Back of card")
    parser.add_argument("--tags", "-t", nargs="*", default=[], help="Tags for the card")
    args = parser.parse_args()

    ensure_deck(args.deck)
    note_id = add_card(args.deck, args.front, args.back, args.tags)
    print(f"Added card (ID: {note_id})")
    print(f"  Deck: {args.deck}")
    print(f"  Front: {args.front}")
    print(f"  Back: {args.back}")
    if args.tags:
        print(f"  Tags: {', '.join(args.tags)}")


if __name__ == "__main__":
    main()
