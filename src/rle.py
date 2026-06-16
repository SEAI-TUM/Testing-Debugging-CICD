"""Run-length encoding (RLE)

    encode("aaabb")  -> "a3b2"
    decode("a3b2")   -> "aaabb"

Assumption: the input text contains letters only (no digits), so the
encoded form can interleave characters and their run-counts unambiguously.

There is a deliberate bug in this module.
A single example-based test passes and even reaches 100% line coverage,
yet the round-trip property `decode(encode(s)) == s` does NOT always hold.
"""
from __future__ import annotations


def encode(text: str) -> str:
    """Run-length encode `text` (letters only) into the form 'a3b2'."""
    if not text:
        return ""
    result: list[str] = []
    prev = text[0]
    count = 1
    for ch in text[1:]:
        if ch == prev:
            count += 1
        else:
            result.append(prev + str(count))
            prev = ch
            count = 1
    result.append(prev + str(count))
    return "".join(result)


def decode(encoded: str) -> str:
    """Decode an RLE string of the form 'a3b2' back to 'aaabb'."""
    result: list[str] = []
    i = 0
    while i < len(encoded):
        ch = encoded[i]
        count = int(encoded[i + 1])
        result.append(ch * count)
        i += 2
    return "".join(result)