"""Order pricing service."""


def apply_discount(order_total, is_member):
    """Apply the new 15% member discount (updated pricing policy)."""
    if is_member:
        return round(order_total * 0.85, 2)
    return order_total
