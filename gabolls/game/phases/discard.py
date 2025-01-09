from gabolls.models.action import RoundAction
from gabolls.models.decisions import DiscardFromHandDecision
from gabolls.models.discard import DiscardRequests, DiscardResultType
from gabolls.models.errors import NoDecisionsTaken
from gabolls.models.player_action import (
    DiscardFromHandAction,
    DrawPunishementCardAction,
    PlayerAction,
)
from gabolls.models.round import Round


async def solve_discard(round: Round, discard_requests: DiscardRequests) -> Round:
    responses = discard_requests.resolve(round)
    for response in responses:
        if response.result is DiscardResultType.FAIL:
            punishment_card = round.deck.draw_top_card()
            response.player.hand.add(punishment_card)

            failed_discard_decision = DiscardFromHandDecision(response.card)
            draw_punishement_action = DrawPunishementCardAction(punishment_card)
            player_action = PlayerAction(
                response.player, failed_discard_decision, draw_punishement_action
            )

        elif response.result is DiscardResultType.SUCESS:
            response.player.hand.discard(response.card)
            success_discard_decision = DiscardFromHandDecision(response.card)
            player_discard_from_hand_action = DiscardFromHandAction(response.card)
            player_action = PlayerAction(
                response.player,
                success_discard_decision,
                player_discard_from_hand_action,
            )

        else:
            raise NoDecisionsTaken

        round_action = RoundAction(player_action)
        round.actions.append(round_action)

    return round
