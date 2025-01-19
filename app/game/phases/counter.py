from app.game.questions import submit_user_counter_proposal
from app.schemas.action import RoundAction
from app.schemas.decisions import CallCounterDecision
from app.schemas.player_action import CounterAction, PlayerAction
from app.schemas.round import Round


async def solve_counters(round: Round) -> tuple[Round, bool]:
    counter_called = await submit_user_counter_proposal(round.declared_wins)

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
