import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        if len(self._items) > 0:
            return self._items.pop()
        return None

    def __call__(self, *args, **kwargs):
        return self.pick()


if __name__ == "__main__":
    bc = BingoCage("hello")
    print(bc())
    print(bc())
    print(bc())
