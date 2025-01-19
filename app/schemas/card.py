from app.schemas.pydantic_config import BaseModel
from app.schemas.rank import SHORT_RANKS, Rank
from app.schemas.spell import SPELL_RANKS
from app.schemas.suit import SHORT_SUITS, Suit


class Card(BaseModel):
    rank: Rank
    suit: Suit
    value: int

    @property
    def has_spell(self) -> bool:
        return self.rank in SPELL_RANKS

    @property
    def short(self) -> str:
        return SHORT_RANKS[self.rank] + SHORT_SUITS[self.suit]


BLANK_CARD = Card(rank=Rank.NONE, suit=Suit.NONE, value=0)