from game.api.round import prompt_user_counter_proposal
from game.models.action import RoundAction
from game.models.decisions import CallCounterDecision
from game.models.player_action import CounterAction, PlayerAction
from game.models.round import Round


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
