from enum import StrEnum, auto

from gabolls.models.pydantic_config import BaseModel

from gabolls.models.player import Player


class RoundEndType(StrEnum):
    SAFE = auto()
    NEUTRAL_COUNTER = auto()
    COUNTER = auto()
    SCORING = auto()
    SMALL_PENALTY = auto()
    LARGE_PENALTY = auto()
    DIFFERED_PENALTY = auto()
    SMALL_COMEBACK = auto()
    LARGE_COMEBACK = auto()
    EMPTY_HAND = auto()
    SAVED_FROM_DICKHEAD = auto()


class RoundEndScenario(StrEnum):
    DICKHEAD = auto()
    EMPTY_DECK = auto()
    EMPTY_HAND = auto()
    COUNTER_SUCCESS = auto()
    COUNTER_NULL = auto()
    CLASSIC = auto()


class RoundEnd(BaseModel):
    player: Player
    new_points: int
    type: RoundEndType
    scenario: RoundEndScenario
