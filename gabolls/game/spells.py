from loguru import logger

from gabolls.models.card import Card, CardView
from gabolls.models.errors import NoTypeError
from gabolls.models.player import Player
from gabolls.models.player_card import PlayerCard
from gabolls.models.rank import Rank
from gabolls.models.round import Round
from gabolls.models.spell import SPELL_CARDS, SpellType


async def ask_player_exchange_valid(player: Player) -> bool:
    raise NotImplementedError


async def ask_is_spell_played(player: Player, spell_type: SpellType) -> bool:
    raise NotImplementedError


async def ask_player_self_card(player: Player) -> Card:
    raise NotImplementedError


async def select_player_card(player: Player, other_players: set[Player]) -> PlayerCard:
    raise NotImplementedError


async def player_exchange_cards(
    player: Player, card: Card, other_player: Player, other_card: Card
) -> None:
    player.hand.swap(card, other_card)
    other_player.hand.swap(other_card, card)
    logger.info(
        f"Player: {player} and Player: {other_player} swapped Card: {card} and Card: {other_card}"
    )


def infer_spell_type_from_rank(rank: Rank) -> SpellType:
    for type, ranks in SPELL_CARDS.items():
        if rank in ranks:
            return type
    raise NoTypeError(f"Couldn't find {rank} in SpellType")


async def play_spell(player: Player, spell_type: SpellType, round: Round) -> Round:

    if spell_type is SpellType.BLIND_EXCHANGE:
        blind_swap_target: PlayerCard = await select_player_card(player, round.lobby.players)
        blind_self_card: Card = await ask_player_self_card(player)
        await player_exchange_cards(
            player, blind_self_card, blind_swap_target.player, blind_swap_target.card
        )
        return round

    elif spell_type is SpellType.VIEW_EXCHANGE:
        view_swap_target: PlayerCard = await select_player_card(player, round.lobby.players)
        view_card_view = CardView(view_swap_target.card, view_swap_target.player)
        player.view_card(view_card_view)
        exchange_valid = await ask_player_exchange_valid(player)
        if exchange_valid:
            view_self_card: Card = await ask_player_self_card(player)
            await player_exchange_cards(
                player, view_self_card, view_swap_target.player, view_swap_target.card
            )
        return round

    elif spell_type is SpellType.SELF_PEAK:
        peak_self_card: Card = await ask_player_self_card(player)
        peak_card_view = CardView(peak_self_card, player)
        player.view_card(peak_card_view)

    elif spell_type is SpellType.OTHER_PEAK:
        other_peak_target = await select_player_card(player, round.lobby.players)
        card_view = CardView(other_peak_target.card, other_peak_target.player)
        player.view_card(card_view)

    else:
        raise NotImplementedError

    return round
