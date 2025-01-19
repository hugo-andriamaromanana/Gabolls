from gabolls_game.api.round import prompt_user_counter_proposal
from gabolls_game.models.action import RoundAction
from gabolls_game.models.decisions import CallCounterDecision
from gabolls_game.models.player_action import CounterAction, PlayerAction
from gabolls_game.models.round import Round


async def solve_counters(round: Round) -> tuple[Round, bool]:
    counter_called = await prompt_user_counter_proposal(round.declared_wins)

    counter_win_called = counter_called is not None

    if counter_called:
        player_action = PlayerAction(
            player=counter_called,
            decision=CallCounterDecision(),
            action=CounterAction(),
        )
        round_action = RoundAction(action=player_action)
        round.actions.append(round_action)

    return round, counter_win_called
