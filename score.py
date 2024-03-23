from abc import ABC, abstractmethod
from enum import Enum, auto
from icecream import ic

from dataclasses import dataclass

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

@dataclass
class Scoring(ABC):
    player_score: int
    @abstractmethod
    def get(self) -> int:
        return -1

class PenaltyType(Enum):
    Small = auto()
    Big = auto()

_PENALTY_ScoringS = {
    PenaltyType.Small: _SMALL_PENALTY,
    PenaltyType.Big: _BIG_PENALTY
}


@dataclass
class PenaltyScoring(Scoring):
    penalty_type: PenaltyType
    def get(self):
        return self.player_score+_PENALTY_ScoringS[self.penalty_type]
    
@dataclass
class PointScoring(Scoring):
    points: int
    
    def _update_scoring_with_comebacks(self) -> int:
        if self.points in _COMEBACKS:
            return _COMEBACKS[self.points]
        return self.points 

    def get(self) -> int:
        self.points = self.player_score+self.points
        return self._update_scoring_with_comebacks()
    
@dataclass
class GaboScoring(Scoring):
    def get(self) -> int:
        return self.player_score

@dataclass
class Player:
    score: int = 0


def test_score():
    player = Player()
    player.score = PointScoring(points=10, player_score=player.score).get()
    player.score = PointScoring(points=10, player_score=player.score).get()
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