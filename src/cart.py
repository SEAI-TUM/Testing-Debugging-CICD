"""A tiny shopping-cart pricing library.

The code here should be correct. Your job is to prove it with tests.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Item:
    """A single line in a shopping cart."""

    name: str
    price: float      # price per unit, in EUR
    quantity: int     # how many units


def line_total(item: Item) -> float:
    """Return the total price for one line item, rounded to cents.

    Raises:
        ValueError: if price or quantity is negative.
    """
    if item.price < 0:
        raise ValueError("price must not be negative")
    if item.quantity < 0:
        raise ValueError("quantity must not be negative")
    return round(item.price * item.quantity, 2)


def apply_discount(price: float, percent: float) -> float:
    """Apply a percentage discount to a price.

    Args:
        price: the original price (>= 0).
        percent: discount percentage in the closed interval [0, 100].

    Returns:
        The discounted price, rounded to cents.

    Raises:
        ValueError: if percent is outside [0, 100].
    """
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


def cart_total(items: list[Item], discount_percent: float = 0.0) -> float:
    """Sum all line totals and apply an optional cart-wide discount.

    An empty cart has a total of 0.0.
    """
    subtotal = sum(line_total(i) for i in items)
    return apply_discount(subtotal, discount_percent)
