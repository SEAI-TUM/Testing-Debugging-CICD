"""Exercise 1 — Unit-testing basics with pytest.

Run just this file:    pytest tests/test_cart.py -v
Run with coverage:     pytest --cov=src --cov-report=term-missing

ONE worked example is given below to show the Arrange–Act–Assert shape.
Complete the TODOs. Aim for meaningful assertions, not just lines executed.
"""
import pytest

from src.cart import Item, apply_discount, cart_total, line_total


# ---- Worked example: the Arrange–Act–Assert pattern -----------------------
def test_line_total_basic():
    # Arrange
    item = Item(name="Coffee", price=2.50, quantity=3)
    # Act
    result = line_total(item)
    # Assert
    assert result == 7.50


# ---- TODO 1: discount happy path ------------------------------------------
# Write a test that checks apply_discount(100.0, 20) == 80.0
def test_apply_discount_basic():
    ...  # TODO: replace with Arrange–Act–Assert


# ---- TODO 2: boundary values ----------------------------------------------
# Use @pytest.mark.parametrize to check 0% (no change) and 100% (free).
# @pytest.mark.parametrize("price,percent,expected", [...])
# def test_apply_discount_boundaries(price, percent, expected): ...


# ---- TODO 3: error handling -----------------------------------------------
# apply_discount should reject percent < 0 and percent > 100.
# Use `with pytest.raises(ValueError): ...`
def test_apply_discount_rejects_out_of_range():
    ...  # TODO


# ---- TODO 4: aggregation + empty cart -------------------------------------
# cart_total([]) must be 0.0; cart_total of a few Items with a discount
# should equal the discounted subtotal.
def test_cart_total():
    ...  # TODO
