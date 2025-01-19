from fastapi import APIRouter
from app.schemas.decisions import (
    BlindExchangeCardDecision,
    DrawDecisionType,
    InHandDecisionType,
    InHandDiscardDecision,
    InHandSwapDecision,
    ViewExchangeCardDecision,
)
from app.schemas.player import Player
from app.schemas.card import Card
from app.schemas.errors import NoDecisionsTaken
from app.schemas.player_card import PlayerCard
from app.schemas.spell import SpellType
from app.schemas.spell_response import SpellResponse

router = APIRouter()


@router.post("/submit_in_hand_decision/{decision}")
async def submit_in_hand_decision() -> InHandDecisionType:
    # Implement the logic to get player between options: SWAP, DISCARD
    return InHandDecisionType.DISCARD  # Example response


@router.post("/submit_player_draw_decision/")
async def submit_player_draw_decision(player: Player) -> DrawDecisionType:
    # Implement the logic to get player between options: FROM_DECK, FROM_DISCARD
    return DrawDecisionType.FROM_DECK  # Example response


@router.post("/submit_player_for_card_to_swap/")
async def submit_player_for_card_to_swap(player: Player, drawn_card: Card) -> Card:
    # Implement the logic for player to select one card from their hand to swap with the drawn card
    return drawn_card  # Example response


@router.post("/submit_player_in_hand_decision/")
async def submit_player_in_hand_decision(
    player: Player, card: Card
) -> InHandDiscardDecision | InHandSwapDecision:
    decision = await submit_in_hand_decision(player, card)
    if decision is InHandDecisionType.DISCARD:
        return InHandDiscardDecision(card)
    elif decision is InHandDecisionType.SWAP:
        card_to_exchange = await submit_player_for_card_to_swap(player, card)
        return InHandSwapDecision(card, card_to_exchange)
    else:
        raise NoDecisionsTaken


@router.post("/submit_hand_with_card_swap/")
async def submit_hand_with_card_swap(
    player: Player, card: Card
) -> ViewExchangeCardDecision | BlindExchangeCardDecision:
    # Implement the logic for player to select a card from another player's hand
    return BlindExchangeCardDecision(card)  # Example response


@router.get("/get_declared_wins/")
async def get_declared_wins() -> list[Player]:
    # Implement the logic to get players who have declared win
    return []  # Example response


@router.post("/submit_user_counter_proposal/")
async def submit_user_counter_proposal(players: list[Player]) -> Player | None:
    # Implement the logic to give users the option to counter the win declaration
    return None  # Example response


@router.post("/submit_player_exchange_valid/")
async def submit_player_exchange_valid(player: Player) -> bool:
    # Implement the logic to get player if they want to exchange the card
    return True  # Example response


@router.post("/submit_is_spell_played/")
async def submit_is_spell_played(
    player: Player, spell_type: SpellType
) -> SpellResponse:
    # Implement the logic to get player if they want to play the spell
    return SpellResponse(False, None)  # Example response


@router.post("/submit_player_self_card/")
async def submit_player_self_card(player: Player) -> Card:
    # Implement the logic to get player to select a card from their hand
    return Card()  # Example response


@router.post("/submit_selected_player_card/")
async def submit_selected_player_card(
    player: Player, other_players: list[Player]
) -> PlayerCard:
    # Implement the logic to get player to select a card from another player's hand
    return PlayerCard()  # Example response
