from typing import TypeAlias
from app.game.models.pydantic_config import BaseModel
from app.game.models.game_action import GameAction
from app.game.models.player_action import PlayerAction

RoundActions: TypeAlias = GameAction | PlayerAction


class RoundAction(BaseModel):
    action: RoundActions
