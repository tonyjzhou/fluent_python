import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from iterable"""

    @abc.abstractmethod
    def pick(self):
        """Remove an item at random and return it.

        Raise LookupError when the container is empty.
        """

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []

        while True:
            try:
                items.append(self.pick())
            except LookupError:
                self.load(items)
                break

        return items
