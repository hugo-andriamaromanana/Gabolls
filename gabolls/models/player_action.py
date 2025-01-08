from dataclasses import dataclass
from typing import TypeAlias
from gabolls.models.card import Card
from gabolls.models.decisions import PlayerDecisons
from gabolls.models.player import Player
from gabolls.models.player_card import PlayerCard
from gabolls.models.spell import SpellType


@dataclass
class PeakCardAction:
    player_card: PlayerCard


@dataclass
class DrawFromDeckAction:
    card: Card


@dataclass
class DrawFromDiscardAction:
    card: Card


@dataclass
class InHandDiscardToPileAction:
    card: Card


@dataclass
class SkipSpellAction:
    spell_type: SpellType


@dataclass
class InHandSwapAction:
    owner_card: Card
    in_hand_card: Card


@dataclass
class BlindExchangeCardAction:
    self_card: Card
    other_player_card: PlayerCard


@dataclass
class ViewExchangeCardAction:
    player_card: Card
    other_player_card: PlayerCard


@dataclass
class DrawPunishementCardAction:
    card: Card


@dataclass
class DiscardFromHandAction:
    card: Card


class CounterAction:
    pass


PlayerActions: TypeAlias = (
    PeakCardAction
    | BlindExchangeCardAction
    | InHandSwapAction
    | SkipSpellAction
    | InHandDiscardToPileAction
    | DrawFromDeckAction
    | DrawFromDiscardAction
    | ViewExchangeCardAction
    | DrawPunishementCardAction
    | DiscardFromHandAction
    | CounterAction
)


@dataclass
class PlayerAction:
    player: Player
    decision: PlayerDecisons
    action: PlayerActions
