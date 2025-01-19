from typing import TypeAlias

from gabolls_game.models.pydantic_config import BaseModel


class RoundOverAction(BaseModel):
    pass


GameActions: TypeAlias = RoundOverAction


class GameAction(BaseModel):
    action: GameActions
