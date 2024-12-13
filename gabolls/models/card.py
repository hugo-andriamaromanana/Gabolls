from dataclasses import dataclass
from gabolls.models.rank import Rank
from gabolls.models.suit import Suit


@dataclass
class Card:
    rank: Rank
    suit: Suit
    value: int

    def peak(self) -> "Card":
        return self
