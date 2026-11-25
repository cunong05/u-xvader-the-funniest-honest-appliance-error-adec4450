"""The Funniest Honest Appliance Error — entry writer.

Writes the single-line error message to /output/entry.txt and prints it.
"""

import os


def build_entry():
    """Compose the error line from its parts so every word earns its place."""
    code = "Error 404: Ice not found."
    confession = "The freezer has been lying to you for weeks"
    punchline = "everything inside is now soup."
    return f"{code} {confession} — {punchline}"


ENTRY = build_entry()

# Sanity: the composed line must equal the fixed entry verbatim.
assert ENTRY == (
    "Error 404: Ice not found. The freezer has been lying to you for weeks"
    " — everything inside is now soup."
), "composed entry drifted from the fixed line"


def validate_entry(text):
    """Gate: UTF-8 text, 1-200 chars, a single non-blank line."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    text.encode("utf-8")
    return text


def main():
    entry = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
