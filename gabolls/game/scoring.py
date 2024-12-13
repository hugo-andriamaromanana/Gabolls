from gabolls.models.round_end import RoundEnd, RoundEndType
from gabolls.models.rules import Rules


class RoundEndNotImplemented(NotImplementedError):
    pass


def infer_score_from_round_end(
    player_score: int, round_end: RoundEnd, rules: Rules
) -> int:

    if round_end.type is RoundEndType.SCORING:
        return round_end.points + player_score

    elif round_end.type is RoundEndType.DIFFERED_PENALTY:
        return player_score - rules.round_win_cap + rules.small_penalty_points

    elif round_end.type is RoundEndType.SMALL_PENALTY:
        return round_end.points + rules.small_penalty_points

    elif round_end.type is RoundEndType.LARGE_PENALTY:
        return round_end.points + rules.large_penalty_points

    elif round_end.type is RoundEndType.SAFE:
        return player_score

    elif round_end.type is RoundEndType.LARGE_COMEBACK:
        return rules.large_comeback_bonus

    elif round_end.type is RoundEndType.SMALL_COMEBACK:
        return rules.small_comeback_bonus

    raise RoundEndNotImplemented(f"Round end type: {round_end.type} not implemented.")
