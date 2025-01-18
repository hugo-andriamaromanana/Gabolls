from typing import TypeAlias

from gabolls.models.config import BaseModel


class RoundOverAction(BaseModel):
    pass


GameActions: TypeAlias = RoundOverAction


class GameAction(BaseModel):
    action: GameActions
