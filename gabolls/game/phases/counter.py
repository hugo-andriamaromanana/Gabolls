from gabolls.api.round import prompt_user_counter_proposal
from gabolls.models.action import RoundAction
from gabolls.models.decisions import CallCounterDecision
from gabolls.models.player_action import CounterAction, PlayerAction
from gabolls.models.round import Round


async def solve_counters(round: Round) -> tuple[Round, bool]:
    counter_called = await prompt_user_counter_proposal(round.declared_wins)

    counter_win_called = counter_called is not None

    if counter_called:
        player_action = PlayerAction(
            counter_called, CallCounterDecision(), CounterAction()
        )
        round_action = RoundAction(player_action)
        round.actions.append(round_action)

    return round, counter_win_called
