import collections
from dataclasses import dataclass


@dataclass
class Card:
    suite: str
    rank: str


# ABC
class FrenchDeck2(collections.MutableSequence):
    suites = [str(n) for n in range(2, 11)] + list("JQKA")
    ranks = ["Diamonds", "Clubs", "Hearts", "Spades"]

    def __init__(self):
        self._cards = [Card(s, r) for s in self.suites for r in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, index, value) -> None:
        self._cards.insert(index, value)
