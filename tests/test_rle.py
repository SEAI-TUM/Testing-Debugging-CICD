"""Exercises 2 & 3 — Property-based testing and debugging.

This file contains a WEAK example-based test that passes and gives
100% line coverage of src/rle.py. That is exactly the trap from the
lecture: coverage tells you a line ran, not that the result was correct.

Exercise 2: add the property-based test below and watch it fail.
Exercise 3: use the failing (minimal!) example to debug and fix src/rle.py.

Run:  pytest tests/test_rle.py -v
"""
from src.rle import decode, encode


# ---- Provided: a weak example test. It PASSES with 100% coverage. ---------
def test_rle_small_example():
    assert encode("") == ""
    assert decode("") == ""
    assert encode("aaabb") == "a3b2"
    assert decode("a3b2") == "aaabb"
    assert decode(encode("aaabb")) == "aaabb"


# ---- TODO (Exercise 2): property-based round-trip test --------------------
# The oracle is the invariant  decode(encode(s)) == s  for ANY input s.
#
# Tip: plain random text almost never contains a run of 10+ identical
# characters, so a naive st.text() strategy would miss this bug entirely.
# A property test is only as good as the inputs it samples -- so we feed it
# runs of a single repeated character, with the length chosen by Hypothesis.

