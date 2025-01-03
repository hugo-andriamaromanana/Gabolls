from dataclasses import dataclass
from enum import StrEnum, auto
from typing import TypeAlias

from gabolls.models.player import Player
from gabolls.models.round_end import RoundEndScenario


class RoundOverType(StrEnum):
    EMPTY_HAND = auto()
    WIN_CALLED = auto()
    EMPTY_DECK = auto()


@dataclass
class WinCalledResume:
    players: list[Player]


@dataclass
class EmptyHandResume:
    players: list[Player]


class EmptyDeckResume:
    pass


RoundOvers: TypeAlias = WinCalledResume | EmptyDeckResume | EmptyDeckResume


@dataclass
class RoundOver:
    type: RoundOverType
    scoring_scenario: RoundEndScenario
    resume: RoundOvers
