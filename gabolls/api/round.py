from gabolls.models.decisions import (
    BlindExchangeCardDecision,
    DrawDecisionType,
    InHandDecisionType,
    InHandDiscardDecision,
    InHandSwapDecision,
    ViewExchangeCardDecision,
)
from gabolls.models.player import Player
from gabolls.models.card import Card
from gabolls.models.errors import NoDecisionsTaken
from gabolls.models.player_card import PlayerCard
from gabolls.models.spell import SpellType
from gabolls.models.spell_response import SpellResponse


async def ask_in_hand_decision(player: Player, card: Card) -> InHandDecisionType:
    raise NoDecisionsTaken


async def ask_player_draw_decision(player: Player) -> DrawDecisionType:
    raise NotImplementedError


async def ask_player_for_card_to_swap(player: Player, drawn_card: Card) -> Card:
    raise NotImplementedError


async def player_select_other_player_card(
    player: Player, other_players: list[Player]
) -> PlayerCard:
    raise NotImplementedError


async def ask_player_in_hand_decision(
    player: Player, card: Card
) -> InHandDiscardDecision | InHandSwapDecision:
    decision = await ask_in_hand_decision(player, card)

    if decision is InHandDecisionType.DISCARD:
        return InHandDiscardDecision(card)

    elif decision is InHandDecisionType.SWAP:
        card_to_exchange = await ask_player_for_card_to_swap(player, card)
        return InHandSwapDecision(card, card_to_exchange)
    else:
        raise NoDecisionsTaken


async def swap_hand_with_card(
    player: Player, card: Card
) -> ViewExchangeCardDecision | BlindExchangeCardDecision:

    raise NotImplementedError


async def get_declared_wins() -> list[Player]:
    raise NotImplementedError


async def prompt_user_counter_proposal(players: list[Player]) -> Player | None:
    raise NotImplementedError


async def ask_player_exchange_valid(player: Player) -> bool:
    raise NotImplementedError


async def ask_is_spell_played(player: Player, spell_type: SpellType) -> SpellResponse:
    raise NotImplementedError


async def ask_player_self_card(player: Player) -> Card:
    raise NotImplementedError


async def select_player_card(player: Player, other_players: set[Player]) -> PlayerCard:
    raise NotImplementedError
