from loguru import logger

from app.game.questions import (
    submit_player_exchange_valid,
    submit_player_self_card,
    submit_selected_player_card,
)
from app.schemas.action import RoundAction
from app.schemas.card import Card
from app.schemas.card_view import CardView
from app.schemas.decisions import (
    BlindExchangeCardDecision,
    PeakDecision,
    ViewExchangeCardDecision,
)
from app.schemas.errors import NoTypeError
from app.schemas.player import Player
from app.schemas.player_action import (
    BlindExchangeCardAction,
    PeakCardAction,
    PlayerAction,
    ViewExchangeCardAction,
)
from app.schemas.player_card import PlayerCard
from app.schemas.rank import Rank
from app.schemas.round import Round
from app.schemas.spell import SPELL_CARDS, SpellType


async def player_exchange_cards(
    player_card: PlayerCard, other_player_card: PlayerCard
) -> None:
    player_card.player.hand.swap(player_card.card, other_player_card.card)
    other_player_card.player.hand.swap(other_player_card.card, player_card.card)
    logger.info(
        f"Player: {player_card.player} and Player: {other_player_card.player} swapped Card: {player_card.card} and Card: {other_player_card.card}"
    )


def infer_spell_type_from_rank(rank: Rank) -> SpellType:
    for type, ranks in SPELL_CARDS.items():
        if rank in ranks:
            return type
    raise NoTypeError(f"Couldn't find {rank} in SpellType")


async def play_spell(
    player: Player,
    spell_type: SpellType,
    round: Round,
) -> Round:

    if spell_type is SpellType.BLIND_EXCHANGE:
        blind_swap_target: PlayerCard = await submit_selected_player_card(
            player, round.lobby.players
        )
        blind_self_card: Card = await submit_player_self_card(player)
        await player_exchange_cards(
            PlayerCard(player=player, card=blind_self_card), blind_swap_target
        )

        blind_swap_decision = BlindExchangeCardDecision(
            player_card=blind_self_card, other_player_card=blind_swap_target
        )
        blind_swap_action = BlindExchangeCardAction(
            self_card=blind_self_card, other_player_card=blind_swap_target
        )
        player_action = PlayerAction(
            player=player, decision=blind_swap_decision, action=blind_swap_action
        )
        round_action = RoundAction(action=player_action)
        round.actions.append(round_action)

    elif spell_type is SpellType.VIEW_EXCHANGE:
        view_swap_target: PlayerCard = await submit_selected_player_card(
            player, round.lobby.players
        )
        view_card_view = CardView(
            card=view_swap_target.card, owner=view_swap_target.player.id
        )
        player.view_card(view_card_view)

        other_players = list(set(round.lobby.players).difference([player]))
        other_player_card = await submit_selected_player_card(player, other_players)
        other_peak_decision = PeakDecision(player_card=other_player_card)
        other_peak_action = PeakCardAction(player_card=other_player_card)
        player_action = PlayerAction(
            player=player, decision=other_peak_decision, action=other_peak_action
        )
        round_action = RoundAction(action=player_action)
        round.actions.append(round_action)

        exchange_valid = await submit_player_exchange_valid(player)
        if exchange_valid:
            view_self_card: Card = await submit_player_self_card(player)
            self_player_card = PlayerCard(player=player, card=view_self_card)
            await player_exchange_cards(self_player_card, view_swap_target)

            view_swap_decision = ViewExchangeCardDecision(
                player_card=view_self_card, other_player_card=view_swap_target
            )
            view_swap_action = ViewExchangeCardAction(
                player_card=self_player_card.card, other_player_card=view_swap_target
            )
            player_action = PlayerAction(
                player=player, decision=view_swap_decision, action=view_swap_action
            )
            round_action = RoundAction(action=player_action)
            round.actions.append(round_action)

    elif spell_type is SpellType.SELF_PEAK:
        peak_self_card = await submit_player_self_card(player)
        peak_card_view = CardView(card=peak_self_card, owner=player.id)
        player.view_card(peak_card_view)

        self_player_card = PlayerCard(player=player, card=peak_self_card)
        self_peak_decision = PeakDecision(player_card=self_player_card)
        self_peak_action = PeakCardAction(player_card=self_player_card)
        player_action = PlayerAction(
            player=player, decision=self_peak_decision, action=self_peak_action
        )
        round_action = RoundAction(action=player_action)
        round.actions.append(round_action)

    elif spell_type is SpellType.OTHER_PEAK:
        other_peak_target = await submit_selected_player_card(
            player, round.lobby.players
        )
        card_view = CardView(
            card=other_peak_target.card, owner=other_peak_target.player.id
        )
        player.view_card(card_view)

        other_players = list(set(round.lobby.players).difference([player]))
        other_player_card = await submit_selected_player_card(player, other_players)
        other_peak_decision = PeakDecision(player_card=other_player_card)
        other_peak_action = PeakCardAction(player_card=other_player_card)
        player_action = PlayerAction(
            player=player, decision=other_peak_decision, action=other_peak_action
        )
        round_action = RoundAction(action=player_action)
        round.actions.append(round_action)

    else:
        raise NotImplementedError

    return round