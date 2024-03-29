def fidelity_promotion(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promotion(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promotion(order):
    distinct_items = {item.quantity for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0
