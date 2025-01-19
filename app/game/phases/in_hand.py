from loguru import logger
from app.game.questions import submit_is_spell_played, submit_player_in_hand_decision
from app.game.spells import infer_spell_type_from_rank
from app.schemas.action import RoundAction
from app.schemas.card import Card
from app.schemas.decisions import (
    InHandDiscardDecision,
    InHandSwapDecision,
    SkipSpellDecision,
)
from app.schemas.errors import NoDecisionsTaken
from app.schemas.player import Player
from app.schemas.player_action import (
    InHandDiscardToPileAction,
    InHandSwapAction,
    PlayerAction,
    SkipSpellAction,
)
from app.schemas.round import Round
from app.schemas.spell_response import SpellResponse


async def in_hand_phase(
    round: Round, player: Player, drawn_card: Card
) -> tuple[Round, SpellResponse]:
    spell_response = SpellResponse(ok=False, spell_type=None)
    in_hand_decision: InHandDiscardDecision | InHandSwapDecision = (
        await submit_player_in_hand_decision(player, drawn_card)
    )
    if isinstance(in_hand_decision, InHandSwapAction):
        player.hand.swap(in_hand_decision.owner_card, in_hand_decision.in_hand_card)

        player_in_hand_swap_decision = InHandSwapDecision(
            owner_card=in_hand_decision.owner_card,
            in_hand_card=in_hand_decision.in_hand_card,
        )
        player_in_hand_swap_action = InHandSwapAction(
            owner_card=in_hand_decision.owner_card,
            in_hand_card=in_hand_decision.in_hand_card,
        )
        player_action = PlayerAction(
            player=player,
            decision=player_in_hand_swap_decision,
            action=player_in_hand_swap_action,
        )
        round_action = RoundAction(action=player_action)
        round.actions.append(round_action)

    elif isinstance(in_hand_decision, InHandDiscardToPileAction):
        round.discard_pile.add_to_top(in_hand_decision.card)

        player_in_hand_discard_decision = InHandDiscardDecision(
            card=in_hand_decision.card
        )
        player_in_hand_discard_action = InHandDiscardToPileAction(
            card=in_hand_decision.card
        )
        player_action = PlayerAction(
            player=player,
            decision=player_in_hand_discard_decision,
            action=player_in_hand_discard_action,
        )
        round_action = RoundAction(action=player_action)
        round.actions.append(round_action)

        if in_hand_decision.card.has_spell:
            spell_type = infer_spell_type_from_rank(in_hand_decision.card.rank)
            spell_response = await submit_is_spell_played(player, spell_type)
            if spell_response.ok:
                return round, spell_response
            else:
                player_action = PlayerAction(
                    player=player,
                    decision=SkipSpellDecision(),
                    action=SkipSpellAction(spell_type=spell_type),
                )
                round_action = RoundAction(action=player_action)
                round.actions.append(round_action)
                logger.info(f"Player: {player} skipped spell: {spell_type}")
    else:
        raise NoDecisionsTaken

    return round, spell_response
