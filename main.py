#!/usr/bin/env python3
"""texts-from-future-self: one funny text message your future self sends you.

Entry for make.fun's "Texts From Your Future Self" bounty: a single message,
under 200 characters, funny by itself with no setup and no context.
"""

LINE = "It is you from 2036. Stop buying the course, start doing the thing. Also the plant is dead. It was dead in 2026 too. Let it go."

MAX_CHARS = 200


def message():
    """Return the text from the future self, inside the bounty's 200-char cap."""
    assert len(LINE) < MAX_CHARS, f"line is {len(LINE)} chars, cap is under {MAX_CHARS}"
    return LINE


def main():
    print(message())


if __name__ == "__main__":
    main()
