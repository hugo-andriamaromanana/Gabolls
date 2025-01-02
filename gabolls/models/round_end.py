from dataclasses import dataclass
from enum import StrEnum, auto

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


@dataclass
class RoundEnd:
    player: Player
    new_points: int
    type: RoundEndType
