from enum import Enum, auto
from typing import List
from icecream import ic

from dataclasses import dataclass, field

_SMALL_PENALTY = 25
_BIG_PENALTY = 50

_SMALL_COMEBACK_TRIGGER = 50
_SMALL_COMEBACK_SCORING = 25
_BIG_COMEBACK_TRIGGER = 100
_BIG_COMEBACK_SCORING = 50

_COMEBACKS = {
    _SMALL_COMEBACK_TRIGGER: _SMALL_COMEBACK_SCORING,
    _BIG_COMEBACK_TRIGGER: _BIG_COMEBACK_SCORING,
}


class PenaltyType(Enum):
    Small = auto()
    Big = auto()


_PENALTY_SCORINGS = {PenaltyType.Small: _SMALL_PENALTY, PenaltyType.Big: _BIG_PENALTY}


class ScoringType(Enum):
    Gabo = auto()
    Point = auto()
    BigPenalty = auto()
    SmallPenalty = auto()
    BigComeback = auto()
    SmallComeback = auto()


@dataclass(frozen=True, unsafe_hash=True)
class ScoringResult:
    score: int
    scoring_type: ScoringType


def score_penalty(penalty_type: PenaltyType, player_score: int) -> ScoringResult:
    return ScoringResult(
        score=player_score + _PENALTY_SCORINGS[penalty_type],
        scoring_type=(
            ScoringType.BigPenalty
            if penalty_type == PenaltyType.Big
            else ScoringType.SmallPenalty
        ),
    )


def _calc_score_with_comebacks(points: int) -> int:
    if points in _COMEBACKS:
        return _COMEBACKS[points]
    return points


def _determine_comeback(points: int) -> ScoringType:
    if points == _SMALL_COMEBACK_SCORING:
        return ScoringType.SmallComeback
    if points == _BIG_COMEBACK_SCORING:
        return ScoringType.BigComeback
    return ScoringType.Point

def score_point(points: int, player_score: int) -> ScoringResult:
    score = _calc_score_with_comebacks(player_score + points)
    return ScoringResult(
        score, _determine_comeback(score) 
    )


def score_gabo(player_score: int) -> ScoringResult:
    return ScoringResult(player_score, ScoringType.Gabo)


@dataclass
class Player:
    name: str
    scores: List[ScoringResult] = field(default_factory=list)

    @property
    def current_score(self) -> int:
        if not self.scores:
            return 0
        return self.scores[-1].score

    @property
    def is_over(self) -> bool:
        return self.current_score > 120

    def _will_score(self, score: ScoringResult) -> None:
        self.scores.append(score)

    def give_gabo(self) -> None:
        self._will_score(score_gabo(self.current_score))

    def give_points(self, points: int) -> None:
        self._will_score(score_point(points, self.current_score))

    def give_penalty(self, penalty_type: PenaltyType) -> None:
        self._will_score(score_penalty(penalty_type, self.current_score))


# @dataclass
# class Game:
#     players: List[Player] = field(default_factory=list)
#     @property
#     def is_over(self) -> bool:
#         ic(self.players)
#         return any(player.is_over for player in self.players)

def give(player: Player, score: ScoringResult) -> Player:
    player.scores.append(score)
    return player


def test_scores():
    player1 = Player("player1")
    player1.give_points(49)
    player1.give_points(1)
    player1.give_penalty(PenaltyType.Big)
    player1.give_penalty(PenaltyType.Small)
    player1.give_points(21)
    player1.give_gabo()
    ic(player1)
    ic(player1.is_over)


if __name__ == "__main__":
    test_scores()
    # game = Game([Player("player1"), Player("player2")])
    # ic(game.is_over)
