from dataclasses import dataclass
from typing import TypeAlias
from gabolls.models.card import Card
from gabolls.models.player_card import PlayerCard
from enum import StrEnum, auto


class InHandDecisionType(StrEnum):
    DISCARD = auto()
    SWAP = auto()


class DrawDecisionType(StrEnum):
    FROM_DECK = auto()
    FROM_DISCARD = auto()


@dataclass
class InHandDiscardDecision:
    card: Card


@dataclass
class InHandSwapDecision:
    owner_card: Card
    in_hand_card: Card


@dataclass
class BlindExchangeCardDecision:
    player_card: Card
    other_player_card: PlayerCard


@dataclass
class ViewExchangeCardDecision:
    player_card: Card
    other_player_card: PlayerCard


@dataclass
class PeakDecision:
    self_card: Card
    other_player_card: PlayerCard


class SkipViewExchangeDecision:
    pass


class SkipSpellDecision:
    pass


class DrawFromDeckDecision:
    pass


class DrawFromDiscardDecision:
    pass


class CallWinDecision:
    pass


class CallCounterDecision:
    pass

@dataclass
class DiscardFromHand:
    card: Card

PlayerDecisons: TypeAlias = (
    InHandDiscardDecision
    | InHandSwapDecision
    | BlindExchangeCardDecision
    | ViewExchangeCardDecision
    | PeakDecision
    | SkipViewExchangeDecision
    | SkipSpellDecision
    | DrawFromDeckDecision
    | DrawFromDiscardDecision
    | CallWinDecision
    | CallCounterDecision
    | DiscardFromHand
)
