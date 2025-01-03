from dataclasses import dataclass
from enum import StrEnum, auto
from typing import TypeAlias

from gabolls.models.game import Game


class GameActionType(StrEnum):
    ROUND_OVER = auto()


GameActions: TypeAlias = GameActionType


@dataclass
class GameAction:
    game: Game
    action: GameActions
    type: GameActionType
