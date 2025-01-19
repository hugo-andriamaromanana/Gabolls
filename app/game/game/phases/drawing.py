from app.game.models.action import RoundAction
from app.game.models.card import Card
from app.game.models.decisions import DrawDecisionType, DrawFromDeckDecision
from app.game.models.errors import NoDecisionsTaken
from app.game.models.player import Player
from app.game.models.player_action import (
    DrawFromDeckAction,
    DrawFromDiscardAction,
    PlayerAction,
)
from app.game.models.round import Round


async def draw_phase(
    draw_decision: DrawDecisionType, round: Round, player: Player
) -> tuple[Round, Card]:

    if draw_decision is DrawDecisionType.FROM_DECK:

        drawn_card = round.deck.draw_top_card()

        deck_draw_action = DrawFromDeckAction(card=drawn_card)
        player_action = PlayerAction(
            player=player, decision=DrawFromDeckDecision(), action=deck_draw_action
        )

    elif draw_decision is DrawDecisionType.FROM_DISCARD:

        drawn_card = round.discard_pile.draw_top_card()

        discard_draw_action = DrawFromDiscardAction(card=drawn_card)
        player_action = PlayerAction(
            player=player, decision=DrawFromDeckDecision(), action=discard_draw_action
        )

    else:
        raise NoDecisionsTaken

    round_action = RoundAction(action=player_action)
    round.actions.append(round_action)

    return round, drawn_card
