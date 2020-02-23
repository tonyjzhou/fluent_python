"""
>>> Vector()
Vector(0, 0)

>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1+v2
Vector(4, 5)

>>> v = Vector(3, 4)
>>> abs(v)
5.0

>>> v*3
Vector(9, 12)

>>> abs(v * 3)
15.0
"""


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
