from dataclasses import dataclass
from typing import TypeAlias
from gabolls.models.card import Card
from gabolls.models.decisions import DrawDecisionType, PlayerDecisons
from gabolls.models.player import Player
from gabolls.models.player_card import PlayerCard


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
class InHandDiscardToPile:
    card: Card


@dataclass
class SkipAction:
    pass


@dataclass
class InHandSwapAction:
    owner_card: Card
    in_hand_card: Card


@dataclass
class BlindExchangeCardAction:
    player_card: Card
    other_player: Player
    other_player_card: Card


@dataclass
class ViewExchangeCardAction:
    player_card: Card
    other_player: Player
    other_player_card: Card


@dataclass
class DrawPunishementCard:
    card: Card


PlayerActions: TypeAlias = (
    PeakCardAction
    | BlindExchangeCardAction
    | InHandSwapAction
    | SkipAction
    | InHandDiscardToPile
    | DrawFromDeckAction
    | DrawFromDiscardAction
    | ViewExchangeCardAction
    | DrawPunishementCard
)


@dataclass
class PlayerAction:
    player: Player
    decision: PlayerDecisons
    action: PlayerActions
