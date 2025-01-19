from game.models.errors import RoundEndNotImplemented
from game.models.player import Player
from game.models.round_end import RoundEnd, RoundEndScenario, RoundEndType
from game.models.rules import Rules


def solve_scoring_type(
    player_score: int, round_score: int, rules: Rules
) -> RoundEndType:
    potential_score = player_score + round_score
    cap_reached = (
        potential_score in (rules.large_comeback_trigger, rules.small_comeback_trigger)
        and round_score == 0
    )
    if not cap_reached:
        if potential_score == rules.large_comeback_trigger:
            return RoundEndType.LARGE_COMEBACK
        elif potential_score == rules.small_comeback_trigger:
            return RoundEndType.SMALL_COMEBACK
    return RoundEndType.SCORING


def infer_round_end_by_type(
    player: Player,
    hand_score: int,
    round_end_type: RoundEndType,
    scenario: RoundEndScenario,
    rules: Rules,
) -> RoundEnd:

    if round_end_type is RoundEndType.SCORING:
        scoring_type = solve_scoring_type(hand_score, player.score, rules)
        if scoring_type is RoundEndType.LARGE_COMEBACK:
            new_points = rules.large_comeback_bonus
        elif scoring_type is RoundEndType.SMALL_COMEBACK:
            new_points = rules.small_comeback_bonus
        else:
            new_points = player.score + hand_score

    if round_end_type is RoundEndType.SAVED_FROM_DICKHEAD:
        new_points = player.score + min(rules.small_penalty_points, hand_score)

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
        RoundEndType.EMPTY_HAND,
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

    round_end = RoundEnd(
        player=player, new_points=new_points, type=round_end_type, scenario=scenario
    )
    return round_end
