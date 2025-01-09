from gabolls.api.round import ask_player_draw_decision
from gabolls.models.action import RoundAction
from gabolls.models.card import Card
from gabolls.models.decisions import DrawDecisionType, DrawFromDeckDecision
from gabolls.models.errors import NoDecisionsTaken
from gabolls.models.player import Player
from gabolls.models.player_action import (
    DrawFromDeckAction,
    DrawFromDiscardAction,
    PlayerAction,
)
from gabolls.models.round import Round


async def draw_phase(round: Round, player: Player) -> tuple[Round, Card]:
    draw_decision = await ask_player_draw_decision(player)

    if draw_decision is DrawDecisionType.FROM_DECK:

        drawn_card = round.deck.draw_top_card()

        deck_draw_action = DrawFromDeckAction(drawn_card)
        player_action = PlayerAction(player, DrawFromDeckDecision(), deck_draw_action)

    elif draw_decision is DrawDecisionType.FROM_DISCARD:

        drawn_card = round.discard_pile.draw_top_card()

        discard_draw_action = DrawFromDiscardAction(drawn_card)
        player_action = PlayerAction(
            player, DrawFromDeckDecision(), discard_draw_action
        )

    else:
        raise NoDecisionsTaken

    round_action = RoundAction(player_action)
    round.actions.append(round_action)

    return round, drawn_card
