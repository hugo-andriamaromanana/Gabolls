from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any

from more_itertools import flatten

from gabolls.models.card import Card
from gabolls.models.errors import NoTypeError
from gabolls.models.player import Player
from gabolls.models.rank import Rank
from gabolls.models.round import Round

class SpellType(StrEnum):
    SELF_PEAK = auto()
    OTHER_PEAK = auto()
    BLIND_EXCHANGE = auto()
    VIEW_EXCHANGE = auto()

SPELL_CARDS: dict[SpellType, list[Rank]] = {
    SpellType.BLIND_EXCHANGE: [Rank.JACK],
    SpellType.OTHER_PEAK: [Rank.NINE, Rank.TEN],
    SpellType.VIEW_EXCHANGE: [Rank.QUEEN],
    SpellType.SELF_PEAK: [Rank.EIGHT, Rank.SEVEN]
}

SPELL_RANKS: list[Rank] = list(flatten(SPELL_CARDS.values()))

@dataclass
class Spell:
    type: SpellType
    effect: Any

def infer_spell_type_from_rank(rank: Rank) -> SpellType:
    for type, ranks in SPELL_CARDS.items():
        if rank in ranks:
            return type
    raise NoTypeError(f"Couldn't find {rank} in SpellType")

def play_spell(Player: Player, spell: SpellType, round: Round) -> Round:
    raise NotImplementedError

async def blind_exchange(player: Player, other_player: Player, card: Card, other_card: Card) -> tuple[Player, Player]:
    raise NotImplementedError