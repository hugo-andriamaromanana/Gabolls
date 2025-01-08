from dataclasses import dataclass
from gabolls.models.player import Player
from gabolls.models.rank import SHORT_RANKS, Rank
from gabolls.models.spell import SPELL_RANKS
from gabolls.models.suit import SHORT_SUITS, Suit


@dataclass
class Card:
    rank: Rank
    suit: Suit
    value: int

    @property
    def has_spell(self) -> bool:
        return self.rank in SPELL_RANKS

    @property
    def short(self) -> str:
        return SHORT_RANKS[self.rank] + SHORT_SUITS[self.suit]


@dataclass
class CardView:
    card: Card
    owner: Player | None

    @property
    def short(self) -> str:
        owner = self.owner.profile.id if self.owner is not None else "NONE"
        return f"{self.card.short}.{owner}"


BLANK_CARD = Card(Rank.NONE, Suit.NONE, 0)
