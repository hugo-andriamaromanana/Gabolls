from gabolls.models.errors import RoundEndNotImplemented
from gabolls.models.round_end import RoundEndType
from gabolls.models.rules import Rules


def infer_score_from_round_end_type(
    player_score: int, round_end_type: RoundEndType, rules: Rules
) -> int:

    if round_end_type is RoundEndType.SCORING:
        return player_score + player_score

    elif round_end_type is RoundEndType.DIFFERED_PENALTY:
        return player_score - rules.round_win_cap + rules.small_penalty_points

    elif round_end_type is RoundEndType.SMALL_PENALTY:
        return player_score + rules.small_penalty_points

    elif round_end_type is RoundEndType.LARGE_PENALTY:
        return player_score + rules.large_penalty_points

    elif round_end_type is RoundEndType.SAFE:
        return player_score

    elif round_end_type is RoundEndType.LARGE_COMEBACK:
        return rules.large_comeback_bonus

    elif round_end_type is RoundEndType.SMALL_COMEBACK:
        return rules.small_comeback_bonus

    raise RoundEndNotImplemented(f"Round end type: {round_end_type} not implemented.")
