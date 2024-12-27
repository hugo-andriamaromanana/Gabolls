from dataclasses import dataclass
from gabolls.models.player import Player
from gabolls.models.rank import Rank
from gabolls.models.spell import SPELL_RANKS
from gabolls.models.suit import Suit


@dataclass
class Card:
    rank: Rank
    suit: Suit
    value: int

    @property
    def has_spell(self) -> bool:
        return self.rank in SPELL_RANKS


@dataclass
class CardView:
    card: Card
    owner: Player | None


BLANK_CARD = Card(Rank.NONE, Suit.NONE, 0)
