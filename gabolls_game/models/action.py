from typing import TypeAlias
from gabolls_game.models.pydantic_config import BaseModel
from gabolls_game.models.game_action import GameAction
from gabolls_game.models.player_action import PlayerAction

RoundActions: TypeAlias = GameAction | PlayerAction


class RoundAction(BaseModel):
    action: RoundActions
