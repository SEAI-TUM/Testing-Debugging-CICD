"""Exercise 3 — Generate tests with AI, then own the oracle.

Step 1  Use your AI assistant (Copilot, Cursor, Claude, ChatGPT, ...) to
        generate a pytest suite for final_price.
Step 2  Run them:   pytest tests/test_pricing_ai.py -v     (they should pass)
        and coverage: pytest --cov=src.pricing_ai --cov-report=term-missing
Step 3  Now read the SPEC in src/pricing_ai.py. Add ONE test for the
        boundary quantity == 10 that asserts the value the SPEC requires
        (not the value the code happens to return). Does it still pass?

The point: AI writes tests in seconds, but the oracle — what the code
SHOULD do — is yours to supply and verify.
"""
from src.pricing_ai import final_price


# --------------- AI-generated tests below ----------------------------------


# ---- Step 3: the spec-boundary test (you write this one yourself) ---------
# def test_boundary_10_units_gets_discount():
#     # SPEC: 10 or more units -> 10 % off.  10 * 100 = 1000, minus 10 % = 900.
#     assert final_price(100.0, 10) == 900.0
