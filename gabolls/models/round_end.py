from enum import StrEnum, auto


class RoundEndType(StrEnum):
    SAFE = auto()
    SCORING = auto()
    SMALL_PENALTY = auto()
    LARGE_PENALTY = auto()
    DIFFERED_PENALTY = auto()
    SMALL_COMEBACK = auto()
    LARGE_COMEBACK = auto()


class RoundEnd:
    points: int
    type = type
