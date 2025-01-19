from typing import TypeAlias
from game.models.pydantic_config import BaseModel
from game.models.game_action import GameAction
from game.models.player_action import PlayerAction

RoundActions: TypeAlias = GameAction | PlayerAction


class RoundAction(BaseModel):
    action: RoundActions
