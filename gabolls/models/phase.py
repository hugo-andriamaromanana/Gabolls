from enum import StrEnum, auto

from gabolls.models.config import BaseModel

from gabolls.models.player import Player


class GamePhaseType(StrEnum):
    NEW_GAME = auto()
    NEW_ROUND = auto()
    DRAWING = auto()
    DISCARDING_0 = auto()
    IN_HAND = auto()
    PLAY_SPELL = auto()
    DISCARDING_1 = auto()
    CHECK_ROUND_OVER = auto()
    NEXT_PLAYER = auto()
    ROUND_OVER = auto()
    COUNTER = auto()
    UPDATE_PLAYER_SCORES = auto()
    CHECK_GAME_OVER = auto()
    GAME_OVER = auto()


class GamePhase(BaseModel):
    player: Player
    type: GamePhaseType
