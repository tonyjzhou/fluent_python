from functools import partial
from operator import mul

triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1, 10))))

half = partial(mul, 0.5)
print(half(6))
