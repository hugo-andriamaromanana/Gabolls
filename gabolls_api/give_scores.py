from enum import Enum, auto

from .data_objects.player import Player
from .data_objects.scoring import ScoringResult, ScoringType

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


def _score_penalty(penalty_type: PenaltyType, player_score: int) -> ScoringResult:
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

def _score_point(points: int, player_score: int) -> ScoringResult:
    score = _calc_score_with_comebacks(player_score + points)
    return ScoringResult(
        score, _determine_comeback(score) 
    )

def _score_gabo(player_score: int) -> ScoringResult:
    return ScoringResult(player_score, ScoringType.Gabo)


def give_points(player: Player, points: int) -> Player:
    player.scores.append(_score_point(points, player.current_score))
    return player

def give_penalty(player: Player, penalty_type: PenaltyType) -> Player:
    player.scores.append(_score_penalty(penalty_type, player.current_score))
    return player

def give_gabo(player: Player) -> Player:
    player.scores.append(_score_gabo(player.current_score))
    return player