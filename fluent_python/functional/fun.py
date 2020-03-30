from functools import reduce
from operator import mul


def factorial2(n):
    """
        >>> factorial(1)
        1

        >>> factorial(2)
        2

        >>> factorial(3)
        6
    """
    return reduce(mul, range(1, n + 1))


def factorial(n):
    """
        >>> factorial(1)
        1

        >>> factorial(2)
        2

        >>> factorial(3)
        6
    """
    return reduce(lambda x, y: x * y, range(1, n + 1))
