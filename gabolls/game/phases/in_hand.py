from loguru import logger
from gabolls.api.round import ask_is_spell_played, ask_player_in_hand_decision
from gabolls.game.spells import infer_spell_type_from_rank
from gabolls.models.action import RoundAction
from gabolls.models.card import Card
from gabolls.models.decisions import (
    InHandDiscardDecision,
    InHandSwapDecision,
    SkipSpellDecision,
)
from gabolls.models.errors import NoDecisionsTaken
from gabolls.models.player import Player
from gabolls.models.player_action import (
    InHandDiscardToPileAction,
    InHandSwapAction,
    PlayerAction,
    SkipSpellAction,
)
from gabolls.models.round import Round
from gabolls.models.spell_response import SpellResponse


async def in_hand_phase(
    round: Round, player: Player, drawn_card: Card
) -> tuple[Round, SpellResponse]:
    spell_response = SpellResponse(False, None)
    in_hand_decision: InHandDiscardDecision | InHandSwapDecision = (
        await ask_player_in_hand_decision(player, drawn_card)
    )
    if isinstance(in_hand_decision, InHandSwapAction):
        player.hand.swap(in_hand_decision.owner_card, in_hand_decision.in_hand_card)

        player_in_hand_swap_decision = InHandSwapDecision(
            in_hand_decision.owner_card, in_hand_decision.in_hand_card
        )
        player_in_hand_swap_action = InHandSwapAction(
            in_hand_decision.owner_card, in_hand_decision.in_hand_card
        )
        player_action = PlayerAction(
            player, player_in_hand_swap_decision, player_in_hand_swap_action
        )
        round_action = RoundAction(player_action)
        round.actions.append(round_action)

    elif isinstance(in_hand_decision, InHandDiscardToPileAction):
        round.discard_pile.add_to_top(in_hand_decision.card)

        player_in_hand_discard_decision = InHandDiscardDecision(in_hand_decision.card)
        player_in_hand_discard_action = InHandDiscardToPileAction(in_hand_decision.card)
        player_action = PlayerAction(
            player, player_in_hand_discard_decision, player_in_hand_discard_action
        )
        round_action = RoundAction(player_action)
        round.actions.append(round_action)

        if in_hand_decision.card.has_spell:
            spell_type = infer_spell_type_from_rank(in_hand_decision.card.rank)
            spell_response = await ask_is_spell_played(player, spell_type)
            if spell_response.ok:
                return round, spell_response
            else:
                player_action = PlayerAction(
                    player, SkipSpellDecision(), SkipSpellAction(spell_type)
                )
                round_action = RoundAction(player_action)
                round.actions.append(round_action)
                logger.info(f"Player: {player} skipped spell: {spell_type}")
    else:
        raise NoDecisionsTaken

    return round, spell_response
