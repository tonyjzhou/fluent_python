from dataclasses import dataclass
from typing import Callable


@dataclass
class Customer:
    name: str
    fidelity: int


@dataclass
class LineItem:
    product: str
    quantity: float
    price: float

    def total(self):
        return self.price * self.quantity


@dataclass
class Order:
    customer: str
    cart: list
    promotion: Callable

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        return self.total() - self._discount()

    def _discount(self):
        return 0 if self.promotion is None else self.promotion(self)

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


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


promotions = [m for m in globals() if m.endswith("_promotion") and m != "best_promotion"]


def best_promotion(order: Order) -> int:
    return max(p(order) for p in promotions)
