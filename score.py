from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Callable, Dict, List, Protocol
from icecream import ic

from dataclasses import dataclass, field

from traitlets import default

_SMALL_PENALTY = 25
_BIG_PENALTY = 50

_SMALL_COMEBACK_TRIGGER = 50
_SMALL_COMEBACK_SCORING = 25
_BIG_COMEBACK_TRIGGER = 100
_BIG_COMEBACK_SCORING = 50

_COMEBACKS = {
    _SMALL_COMEBACK_TRIGGER: _SMALL_COMEBACK_SCORING,
    _BIG_COMEBACK_TRIGGER: _BIG_COMEBACK_SCORING
}

class Scoring(Protocol):
    player_score: int
    score: int

class PenaltyType(Enum):
    Small = auto()
    Big = auto()

class Scoring    


_PENALTY_SCORINGS = {
    PenaltyType.Small: _SMALL_PENALTY,
    PenaltyType.Big: _BIG_PENALTY
}

@dataclass(frozen=True,unsafe_hash=True)
class Result:
    player_score: int
    penalty_type: PenaltyType

Scorer = Callable[[Scoring], Result]

SCORING_MAP: Dict[Scorer,Result] = {
    
}


def _calc_score_with_comebacks(points: int) -> int:
    if points in _COMEBACKS:
        return _COMEBACKS[points]
    return points 

@dataclass
class PointScoring(Scoring):
    points: int
    
    @property
    def score(self) -> int:
        self.points = self.player_score+self.points
        return _calc_score_with_comebacks(self.points)
    
@dataclass
class GaboScoring(Scoring):
    def get(self) -> int:
        return self.player_score


class ScoringType(Enum):
    Gabo = auto()
    Point = auto()
    BigPenalty = auto()
    SmallPenalty = auto()
    BigComeback = auto()
    SmallComeback = auto()

@dataclass
class Player:
    score: int = 0
    # score_table: Dict[ScoringType, int] = field(default_factory=dict)
    
@dataclass
class Game:
    players: List[Player] = field(default_factory=list)
    

def test_score():
    player = Player()
    player.score = PointScoring(10, player.score).get()
    player.score = PointScoring(10, player.score).get()
    ic(player.score)
    player.score = PenaltyScoring(penalty_type=PenaltyType.Big, player_score=player.score).get()
    ic(player.score)
    player.score = PointScoring(points=30, player_score=player.score).get()
    ic(player.score)
    player.score = PointScoring(points=10, player_score=player.score).get()


if __name__ == "__main__":
    test_score()


def get_updated_player_score(player: Player, scoring: Scoring) -> int:
    return scoring.get()