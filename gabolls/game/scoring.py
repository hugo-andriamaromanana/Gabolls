from gabolls.models.errors import RoundEndNotImplemented
from gabolls.models.player import Player
from gabolls.models.round_end import RoundEnd, RoundEndType
from gabolls.models.rules import Rules


def infer_round_end_type_by_score(
    player_score: int, round_score: int, rules: Rules
) -> RoundEndType:
    potential_score = player_score + round_score
    if (
        potential_score in (rules.large_comeback_trigger, rules.small_comeback_trigger)
    ) and round_score == 0:
        return RoundEndType.SCORING
    elif potential_score == rules.large_comeback_trigger:
        return RoundEndType.LARGE_COMEBACK
    elif potential_score == rules.small_comeback_trigger:
        return RoundEndType.SMALL_COMEBACK
    else:
        return RoundEndType.SCORING


def infer_round_end_by_type(
    player: Player, hand_score: int, round_end_type: RoundEndType, rules: Rules
) -> RoundEnd:

    if round_end_type is RoundEndType.SCORING:
        new_points = player.score + hand_score

    elif round_end_type is RoundEndType.DIFFERED_PENALTY:
        new_points = player.score - rules.round_win_cap + rules.small_penalty_points

    elif round_end_type is RoundEndType.SMALL_PENALTY:
        new_points = player.score + rules.small_penalty_points

    elif round_end_type is RoundEndType.LARGE_PENALTY:
        new_points = player.score + rules.large_penalty_points

    elif round_end_type in (
        RoundEndType.SAFE,
        RoundEndType.COUNTER,
        RoundEndType.NEUTRAL_COUNTER,
    ):
        new_points = player.score

    elif round_end_type is RoundEndType.LARGE_COMEBACK:
        new_points = rules.large_comeback_bonus

    elif round_end_type is RoundEndType.SMALL_COMEBACK:
        new_points = rules.small_comeback_bonus

    else:
        raise RoundEndNotImplemented(
            f"Round end type: {round_end_type} not implemented."
        )

    round_end = RoundEnd(player, new_points, round_end_type)
    return round_end
