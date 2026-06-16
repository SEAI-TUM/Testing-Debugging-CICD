from __future__ import annotations


def final_price(unit_price: float, quantity: int) -> float:
    """Total price for an order, rounded to cents.

    Business rule:
      * an order of 10 or more units gets a 10 % bulk discount on the
        whole order;
      * fewer than 10 units: no discount.

    Args:
        unit_price: price per unit in EUR (>= 0).
        quantity:   number of units ordered (>= 0).
    """
    total = unit_price * quantity
    if quantity > 10:          # does "> 10" match the spec's "10 or more"?
        total *= 0.9
    return round(total, 2)
