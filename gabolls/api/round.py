from gabolls.models.player import Player
from gabolls.game.decisions import DrawDecisionType, InHandDecisionType
from gabolls.models.action import (
    ActionType,
    InHandDiscardToPile,
    InHandSwapAction,
    ViewExchangeCardAction,
    BlindExchangeCardAction,
)
from gabolls.models.card import Card
from gabolls.models.errors import NoDecisionsTaken


async def ask_in_hand_decision(card: Card) -> InHandDecisionType:
    raise NotImplementedError


async def ask_player_for_card_to_swap(player: Player, drawn_card: Card) -> Card:
    raise NotImplementedError


async def ask_player_in_hand_decision(
    player: Player, card: Card
) -> InHandSwapAction | InHandDiscardToPile:
    decision = await ask_in_hand_decision(card)
    if decision is InHandDecisionType.DISCARD:
        return InHandDiscardToPile(
            player, ActionType.DISCARD, InHandDecisionType.DISCARD, card
        )
    elif decision is InHandDecisionType.SWAP:
        card_to_exchange = await ask_player_for_card_to_swap(player, card)
        return InHandSwapAction(
            player, ActionType.SWAP, InHandDecisionType.SWAP, card_to_exchange, card
        )
    else:
        raise NoDecisionsTaken


async def swap_hand_with_card(
    player: Player, card: Card
) -> ViewExchangeCardAction | BlindExchangeCardAction:

    raise NotImplementedError


async def get_declared_wins() -> list[Player]:
    raise NotImplementedError


async def prompt_user_counter_proposal(players: list[Player]) -> bool:
    raise NotImplementedError


async def ask_player_draw_type(player: Player) -> DrawDecisionType:
    raise NotImplementedError
