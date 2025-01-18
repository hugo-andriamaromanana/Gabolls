from typing import TypeAlias
from gabolls.models.config import BaseModel
from gabolls.models.game_action import GameAction
from gabolls.models.player_action import PlayerAction

RoundActions: TypeAlias = GameAction | PlayerAction


class RoundAction(BaseModel):
    action: RoundActions
