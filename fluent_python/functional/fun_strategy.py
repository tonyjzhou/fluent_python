import inspect
from dataclasses import dataclass
from typing import Callable

from fluent_python.functional import promotions


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


ps = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]


def best_promotion(order: Order) -> int:
    return max(p(order) for p in ps)
