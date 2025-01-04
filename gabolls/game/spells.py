from loguru import logger

from gabolls.api.round import (
    ask_player_exchange_valid,
    ask_player_self_card,
    select_player_card,
)
from gabolls.models.card import Card, CardView
from gabolls.models.decisions import (
    BlindExchangeCardDecision,
    PeakDecision,
    ViewExchangeCardDecision,
)
from gabolls.models.errors import NoTypeError
from gabolls.models.player import Player
from gabolls.models.player_action import (
    BlindExchangeCardAction,
    PeakCardAction,
    PlayerAction,
    ViewExchangeCardAction,
)
from gabolls.models.player_card import PlayerCard
from gabolls.models.rank import Rank
from gabolls.models.round import Round
from gabolls.models.spell import SPELL_CARDS, SpellType


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
        blind_swap_target: PlayerCard = await select_player_card(
            player, round.lobby.players
        )
        blind_self_card: Card = await ask_player_self_card(player)
        await player_exchange_cards(
            PlayerCard(player, blind_self_card), blind_swap_target
        )

        blind_swap_decision = BlindExchangeCardDecision(
            blind_self_card, blind_swap_target
        )
        blind_swap_action = BlindExchangeCardAction(blind_self_card, blind_swap_target)
        player_action = PlayerAction(player, blind_swap_decision, blind_swap_action)
        round.actions.append(player_action)

    elif spell_type is SpellType.VIEW_EXCHANGE:
        view_swap_target: PlayerCard = await select_player_card(
            player, round.lobby.players
        )
        view_card_view = CardView(view_swap_target.card, view_swap_target.player)
        player.view_card(view_card_view)

        other_players = round.lobby.players.difference([player])
        other_player_card = await select_player_card(player, other_players)
        other_peak_decision = PeakDecision(other_player_card)
        other_peak_action = PeakCardAction(other_player_card)
        player_action = PlayerAction(player, other_peak_decision, other_peak_action)
        round.actions.append(player_action)

        exchange_valid = await ask_player_exchange_valid(player)
        if exchange_valid:
            view_self_card: Card = await ask_player_self_card(player)
            self_player_card = PlayerCard(player, view_self_card)
            await player_exchange_cards(self_player_card, view_swap_target)

            view_swap_decision = ViewExchangeCardDecision(
                view_self_card, view_swap_target
            )
            view_swap_action = ViewExchangeCardAction(
                self_player_card.card, view_swap_target
            )
            player_action = PlayerAction(player, view_swap_decision, view_swap_action)
            round.actions.append(player_action)

    elif spell_type is SpellType.SELF_PEAK:
        peak_self_card = await ask_player_self_card(player)
        peak_card_view = CardView(peak_self_card, player)
        player.view_card(peak_card_view)

        self_player_card = PlayerCard(player, peak_self_card)
        self_peak_decision = PeakDecision(self_player_card)
        self_peak_action = PeakCardAction(self_player_card)
        player_action = PlayerAction(player, self_peak_decision, self_peak_action)
        round.actions.append(player_action)

    elif spell_type is SpellType.OTHER_PEAK:
        other_peak_target = await select_player_card(player, round.lobby.players)
        card_view = CardView(other_peak_target.card, other_peak_target.player)
        player.view_card(card_view)

        other_players = round.lobby.players.difference([player])
        other_player_card = await select_player_card(player, other_players)
        other_peak_decision = PeakDecision(other_player_card)
        other_peak_action = PeakCardAction(other_player_card)
        player_action = PlayerAction(player, other_peak_decision, other_peak_action)
        round.actions.append(player_action)

    else:
        raise NotImplementedError

    return round
