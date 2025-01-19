from typing import TypeAlias
from app.schemas.pydantic_config import BaseModel
from app.schemas.game_action import GameAction
from app.schemas.player_action import PlayerAction

RoundActions: TypeAlias = GameAction | PlayerAction


class RoundAction(BaseModel):
    action: RoundActions
