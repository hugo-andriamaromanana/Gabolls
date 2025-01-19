from enum import StrEnum, auto
from more_itertools import flatten

from game.models.rank import Rank


class SpellType(StrEnum):
    SELF_PEAK = auto()
    OTHER_PEAK = auto()
    BLIND_EXCHANGE = auto()
    VIEW_EXCHANGE = auto()
    SKIP_VIEW_EXCHANGE = auto()


SPELL_CARDS: dict[SpellType, list[Rank]] = {
    SpellType.BLIND_EXCHANGE: [Rank.JACK],
    SpellType.OTHER_PEAK: [Rank.NINE, Rank.TEN],
    SpellType.VIEW_EXCHANGE: [Rank.QUEEN],
    SpellType.SELF_PEAK: [Rank.EIGHT, Rank.SEVEN],
}

SPELL_RANKS: list[Rank] = list(flatten(SPELL_CARDS.values()))
