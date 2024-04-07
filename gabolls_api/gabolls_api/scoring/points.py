from enum import Enum
from typing import Dict
from data_objects.player import Player
from data_objects.scoring import ScoringResult, ScoringType

_SMALL_COMEBACK_TRIGGER = 50
_SMALL_COMEBACK_SCORING = 25
_BIG_COMEBACK_TRIGGER = 100
_BIG_COMEBACK_SCORING = 50

_COMEBACKS: Dict[int, int] = {
    _SMALL_COMEBACK_TRIGGER: _SMALL_COMEBACK_SCORING,
    _BIG_COMEBACK_TRIGGER: _BIG_COMEBACK_SCORING,
}


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
    return ScoringResult(score, _determine_comeback(score))


def give_points(player: Player, points: int) -> Player:
    player.scores.append(_score_point(points, player.current_score))
    return player

