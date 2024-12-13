from dataclasses import dataclass
from enum import StrEnum, auto

from gabolls.models.card import Card


class ActionType(StrEnum):
    DRAW = auto()
    THROW = auto()
    DISCARD = auto()
    GABO = auto()
    EXCHANGE = auto()


@dataclass
class PlayerAction:
    type: ActionType


@dataclass
class Draw(PlayerAction):
    card: Card


@dataclass
class Throw(PlayerAction):
    card: Card


@dataclass
class Exchange(PlayerAction):
    entree_card: Card
    exit_card: Card
