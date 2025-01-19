from app.schemas.action import RoundAction
from app.schemas.decisions import DiscardFromHandDecision
from app.schemas.discard import DiscardRequest, DiscardResponse, DiscardResultType
from app.schemas.errors import NoDecisionsTaken
from app.schemas.player_action import (
    DiscardFromHandAction,
    DrawPunishementCardAction,
    PlayerAction,
)
from app.schemas.round import Round


def resolve_discards(
    discards: list[DiscardRequest], round: Round
) -> list[DiscardResponse]:
    responses: list[DiscardResponse] = []
    for request in discards:
        result_type = (
            DiscardResultType.FAIL
            if request.card.rank != round.deck.top_card_view.card.rank
            else DiscardResultType.SUCESS
        )
        response = DiscardResponse(
            card=request.card, player=request.player, result=result_type
        )
        responses.append(response)
    return responses


async def solve_discard(round: Round, discard_requests: list[DiscardRequest]) -> Round:
    responses = resolve_discards(discard_requests, round)
    for response in responses:
        if response.result is DiscardResultType.FAIL:
            punishment_card = round.deck.draw_top_card()
            response.player.hand.add(punishment_card)

            failed_discard_decision = DiscardFromHandDecision(card=response.card)
            draw_punishement_action = DrawPunishementCardAction(card=punishment_card)
            player_action = PlayerAction(
                player=response.player,
                decision=failed_discard_decision,
                action=draw_punishement_action,
            )

        elif response.result is DiscardResultType.SUCESS:
            response.player.hand.discard(response.card)
            success_discard_decision = DiscardFromHandDecision(card=response.card)
            player_discard_from_hand_action = DiscardFromHandAction(card=response.card)
            player_action = PlayerAction(
                player=response.player,
                decision=success_discard_decision,
                action=player_discard_from_hand_action,
            )

        else:
            raise NoDecisionsTaken

        round_action = RoundAction(action=player_action)
        round.actions.append(round_action)

    return round
