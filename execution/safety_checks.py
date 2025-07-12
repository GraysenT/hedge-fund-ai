def sanity_check_order(order):
    errors = []

    if not order.get("symbol") or not order.get("qty"):
        errors.append("Missing symbol or quantity")

    if order.get("qty", 0) <= 0:
        errors.append("Quantity must be positive")

    if order.get("confidence", 0) < 0.1:
        errors.append("Low confidence signal")

    if order.get("price") and order.get("price") <= 0:
        errors.append("Price must be positive")

    if errors:
        return False, errors
    return True, []