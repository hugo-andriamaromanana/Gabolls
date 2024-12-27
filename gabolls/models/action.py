from dataclasses import dataclass
from enum import StrEnum, auto
from gabolls.game.decisions import DrawDecisionType, InHandDecisionType
from gabolls.models.card import Card
from gabolls.models.player import Player


class ActionType(StrEnum):
    SWAP = auto()
    DRAW = auto()
    THROW = auto()
    DISCARD = auto()
    GABO = auto()
    EXCHANGE = auto()
    PEAK = auto()


class PeakOwner(StrEnum):
    SELF = auto()
    OTHER = auto()
    DISCARD = auto()
    DECK = auto()


@dataclass
class PlayerAction:
    player: Player
    type: ActionType


@dataclass
class PeakCardAction(PlayerAction):
    card: Card
    owner: PeakOwner


@dataclass
class DrawFromDeckAction(PlayerAction):
    decision_type: DrawDecisionType


@dataclass
class DrawFromDiscardAction(PlayerAction):
    decision_type: DrawDecisionType


@dataclass
class InHandDiscardToPile(PlayerAction):
    decision_type: InHandDecisionType
    card: Card


@dataclass
class SkipAction(PlayerAction):
    pass


@dataclass
class InHandSwapAction(PlayerAction):
    decision_type: InHandDecisionType
    owner_card: Card
    in_hand_card: Card


@dataclass
class BlindExchangeCardAction(PlayerAction):
    player_card: Card
    other_player: Player
    other_player_card: Card


@dataclass
class ViewExchangeCardAction(PlayerAction):
    player_card: Card
    other_player: Player
    other_player_card: Card
