from gabolls.game.scoring import infer_round_end_by_type
from gabolls.models.errors import RoundEndNotImplemented
from gabolls.models.player import Player
from gabolls.models.round import Round
from gabolls.models.round_end import RoundEnd, RoundEndScenario, RoundEndType
from gabolls.models.rules import Rules


def determine_scoring_scenario(
    round: Round, counter_win_called: bool
) -> RoundEndScenario:

    if any(player.hand.is_empty for player in round.lobby.players):
        return RoundEndScenario.EMPTY_HAND

    elif round.deck.is_empty:
        return RoundEndScenario.EMPTY_DECK

    elif counter_win_called:
        lowest_score = min(player.score for player in round.players_declared_win)
        counter_winners = set(
            player
            for player in round.players_declared_win
            if player.score == lowest_score
        )
        if len(counter_winners) > 1:
            return RoundEndScenario.COUNTER_NULL
        else:
            return RoundEndScenario.COUNTER_SUCCESS

    else:
        return RoundEndScenario.CLASSIC


def _create_round_ends_for_group(
    round: Round,
    group: set[Player],
    round_end_type: RoundEndType,
    scenario: RoundEndScenario,
    rules: Rules,
) -> list[RoundEnd]:
    round_ends: list[RoundEnd] = []
    for player in group:
        round_score = round.get_player_score(player)
        round_end = infer_round_end_by_type(
            player, round_score, round_end_type, scenario, rules
        )
        round_ends.append(round_end)
    return round_ends


def find_player_end_rounds(
    round: Round, declared_wins: set[Player], scenario: RoundEndScenario, rules: Rules
) -> list[RoundEnd]:
    players = round.lobby.players
    small_penalty_players = set(
        player
        for player in players
        if player in declared_wins and not player.is_eligible
    )
    small_penalty_end_rounds = _create_round_ends_for_group(
        round, small_penalty_players, RoundEndType.SMALL_PENALTY, scenario, rules
    )

    if scenario is RoundEndScenario.EMPTY_HAND and round.deck.is_empty:
        empty_handed_players = set(player for player in players if player.hand.is_empty)
        leftover_players = players - empty_handed_players

        empty_handed_players_round_ends = _create_round_ends_for_group(
            round,
            empty_handed_players,
            RoundEndType.EMPTY_HAND,
            RoundEndScenario.EMPTY_HAND,
            rules,
        )
        leftover_players_round_ends = _create_round_ends_for_group(
            round,
            leftover_players,
            RoundEndType.SCORING,
            RoundEndScenario.EMPTY_HAND,
            rules,
        )

        return (
            empty_handed_players_round_ends
            + leftover_players_round_ends
            + small_penalty_end_rounds
        )

    if scenario is RoundEndScenario.EMPTY_DECK:
        empty_handed_players = set(player for player in players if player.hand.is_empty)
        others = players - empty_handed_players

        empty_handed_players_round_ends = _create_round_ends_for_group(
            round,
            empty_handed_players,
            RoundEndType.EMPTY_HAND,
            RoundEndScenario.EMPTY_HAND,
            rules,
        )
        leftover_players_round_ends = _create_round_ends_for_group(
            round,
            others,
            RoundEndType.SCORING,
            RoundEndScenario.EMPTY_HAND,
            rules,
        )

        return (
            empty_handed_players_round_ends
            + leftover_players_round_ends
            + small_penalty_end_rounds
        )

    elif scenario is RoundEndScenario.COUNTER_NULL:
        counter_winners = declared_wins - small_penalty_players
        counter_losers = declared_wins - (small_penalty_players | counter_winners)
        others = players - (counter_winners | counter_losers)

        counter_winners_round_ends = _create_round_ends_for_group(
            round, counter_winners, RoundEndType.COUNTER, scenario, rules
        )

        counter_losers_round_ends = _create_round_ends_for_group(
            round, counter_losers, RoundEndType.LARGE_PENALTY, scenario, rules
        )

        others_round_ends = _create_round_ends_for_group(
            round, others, RoundEndType.SCORING, scenario, rules
        )

        return (
            counter_winners_round_ends
            + counter_losers_round_ends
            + others_round_ends
            + small_penalty_end_rounds
        )

    elif scenario is RoundEndScenario.COUNTER_NULL:
        counter_winners = declared_wins - small_penalty_players
        counter_losers = declared_wins - (small_penalty_players | counter_winners)
        others = players - (counter_winners | counter_losers)

        counter_winners_round_ends = _create_round_ends_for_group(
            round, counter_winners, RoundEndType.NEUTRAL_COUNTER, scenario, rules
        )

        counter_losers_round_ends = _create_round_ends_for_group(
            round, counter_losers, RoundEndType.LARGE_PENALTY, scenario, rules
        )

        others_round_ends = _create_round_ends_for_group(
            round, others, RoundEndType.SCORING, scenario, rules
        )

        return (
            counter_winners_round_ends
            + counter_losers_round_ends
            + others_round_ends
            + small_penalty_end_rounds
        )

    elif scenario is RoundEndScenario.CLASSIC:
        winners = declared_wins - small_penalty_players
        others = players - (winners | small_penalty_players)

        winners_end_rounds = _create_round_ends_for_group(
            round, winners, RoundEndType.SAFE, scenario, rules
        )

        others_round_end = _create_round_ends_for_group(
            round, others, RoundEndType.SCORING, scenario, rules
        )

        return winners_end_rounds + others_round_end + small_penalty_end_rounds

    else:
        raise RoundEndNotImplemented
