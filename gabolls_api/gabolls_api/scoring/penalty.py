
from enum import Enum
from typing import Dict


_SMALL_PENALTY = 25
_BIG_PENALTY = 50


class PenaltyType(Enum):
    Small = _SMALL_PENALTY
    Big = _BIG_PENALTY


_PENALTY_SCORING_MAP: Dict[PenaltyType, ScoringType] = {
    PenaltyType.Small: ScoringType.SmallPenalty,
    PenaltyType.Big: ScoringType.BigPenalty,
}
def _score_pen(penalty_type: PenaltyType, player_score: int) -> ScoringResult:
    return ScoringResult(
        score=player_score + penalty_type.value,
        scoring_type=_PENALTY_SCORING_MAP[penalty_type],
    )

def pen(player: Player, penalty_type: PenaltyType) -> Player:
    player.scores.append(_score_pen(penalty_type, player.current_score))
    return player
