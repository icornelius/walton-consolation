#!/usr/bin/env python3
"""Interactive reference converter for Walton's Boethius line-number concordance."""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path

CONCORDANCE_FILE = Path(__file__).parent / "line-number-concordance.csv"


@dataclass(frozen=True)
class Source:
    label: str
    column: int  # index into a concordance row


SOURCES: dict[str, Source] = {
    "1": Source("Science (continuous stanzas)", 1),
    "2": Source("Science (stanzas by section)", 2),
    "3": Source("Myklebust (lines by book)", 3),
    "4": Source("Schümmer (continuous stanzas)", 4),
}


def load_concordance(path: Path) -> list[list[str]]:
    with path.open(newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        return list(reader)


def get_valid_input(prompt: str, options) -> str:
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        prompt = "Invalid input. Try again. "


def choose_source() -> str:
    print(
        "What reference system do you want to convert from?\n\n"
        "(1) Mark Science's continuous stanza numbering\n"
        "(2) Mark Science's numbering by book, section, and stanza\n"
        "(3) Nicholas Myklebust's numbering by book and line\n"
        "(4) Karl Schümmer's continuous stanza numbering\n"
    )
    return get_valid_input("Enter a number (1)-(4) from the options: ", SOURCES)


def prompt_query(source: str) -> str:
    if source in ("1", "4"):
        return input("Enter a stanza number: ")

    if source == "2":
        print(
            ' * For the translation proper, use the format, e.g., "3m9", '
            "for the ninth meter of the third book\n"
            " * For the translator's FIRST PREFACE (preceding the Prologue), "
            'enter "Pref1"\n'
            " * For the translator's PROLOGUE (preceding Book 1), enter "
            '"Prol"\n'
            " * For the translator's SECOND PREFACE (preceding Book 4), "
            'enter "Pref2"\n'
        )
        section = input("Enter a section code: ")
        stanza = input("Enter a stanza number: ")
        return f"{section}.{stanza}"

    # source == "3"
    section = input(
        'Enter a book number (for initial prefatory material, enter "P1"; '
        'for the second preface enter "P2"): '
    )
    line = int(input("Enter a line number: "))
    if section in ("P1", "1", "2", "3"):
        stanza = (line - 1) // 8 + 1
        floor_line = stanza * 8 - 7
    else:  # P2, 4, 5
        stanza = (line - 1) // 7 + 1
        floor_line = stanza * 7 - 6
    return f"{section}.{floor_line}"


def find_row(rows: list[list[str]], source: str, query: str) -> list[str] | None:
    column = SOURCES[source].column
    for row in rows:
        if row[column] == query:
            return row
    return None


def print_row(row: list[str]) -> None:
    for source in SOURCES.values():
        print(f"\t{source.label}:\t{row[source.column]}")


def main() -> None:
    print("Welcome to the reference converter for Walton's Boethius.\n")

    if not CONCORDANCE_FILE.exists():
        print("Source file not found.")
        sys.exit(1)

    rows = load_concordance(CONCORDANCE_FILE)
    source = choose_source()

    while True:
        query = prompt_query(source)
        row = find_row(rows, source, query)
        if row:
            print_row(row)
        else:
            print("Query term not found.")
        print()

        again = input(
            "Type 'q' to quit or any key to convert another reference from the same source. "
        ).lower()
        if again == "q":
            break

    print("Goodbye")


if __name__ == "__main__":
    main()
