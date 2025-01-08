from dataclasses import dataclass
from typing import TypeAlias

from gabolls.models.game_action import GameAction
from gabolls.models.player_action import PlayerAction

RoundActions: TypeAlias = GameAction | PlayerAction


@dataclass
class RoundAction:
    action: RoundActions

