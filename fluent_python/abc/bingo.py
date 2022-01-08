import random

from fluent_python.abc.tombola import Tombola


class Bingo(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, iterable):
        self._items.extend(iterable)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("Picked from empty BingoCage")

    def __call__(self, *args, **kwargs):
        self.pick()
