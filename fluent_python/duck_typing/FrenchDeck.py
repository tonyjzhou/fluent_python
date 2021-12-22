from dataclasses import dataclass


@dataclass
class Card:
    suite: str
    rank: str


class FrenchDeck:
    suites = [str(n) for n in range(2, 11)] + list("JQKA")
    ranks = ["Diamonds", "Clubs", "Hearts", "Spades"]

    def __init__(self):
        self.__cards = [Card(s, r) for s in self.suites for r in self.ranks]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, item):
        return self.__cards[item]
