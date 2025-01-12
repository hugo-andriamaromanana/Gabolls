from dataclasses import dataclass
from typing import Any, TypeAlias
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

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"decision_name": "InHandDiscardDecision", "card": self.card.short}


@dataclass
class InHandSwapDecision:
    owner_card: Card
    in_hand_card: Card

    @property
    def as_dict(self) -> dict[str, Any]:
        return {
            "decision_name": "InHandSwapDecision",
            "owner_card": self.owner_card.short,
            "in_hand_card": self.in_hand_card.short,
        }


@dataclass
class BlindExchangeCardDecision:
    player_card: Card
    other_player_card: PlayerCard

    @property
    def as_dict(self) -> dict[str, Any]:
        return {
            "decision_name": "BlindExchangeCardDecision",
            "player_card": self.player_card.short,
            "other_player_card": self.other_player_card.short,
        }


@dataclass
class ViewExchangeCardDecision:
    player_card: Card
    other_player_card: PlayerCard

    @property
    def as_dict(self) -> dict[str, Any]:
        return {
            "decision_name": "ViewExchangeCardDecision",
            "player_card": self.player_card.short,
            "other_player_card": self.other_player_card.short,
        }


@dataclass
class PeakDecision:
    player_card: PlayerCard

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"decision_name": "PeakDecision", "player_card": self.player_card}


class SkipViewExchangeDecision:
    def __init__(self) -> None:
        self.as_dict = {"decision_name": "SkipViewExchangeDecision"}


class SkipSpellDecision:
    def __init__(self) -> None:
        self.as_dict = {"decision_name": "SkipSpellDecision"}


class DrawFromDeckDecision:
    def __init__(self) -> None:
        self.as_dict = {"decision_name": "DrawFromDeckDecision"}


class DrawFromDiscardDecision:
    def __init__(self) -> None:
        self.as_dict = {"decision_name": "DrawFromDiscardDecision"}


class CallWinDecision:
    def __init__(self) -> None:
        self.as_dict = {"decision_name": "CallWinDecision"}


class CallCounterDecision:
    def __init__(self) -> None:
        self.as_dict = {"decision_name": "CallCounterDecision"}


@dataclass
class DiscardFromHandDecision:
    card: Card

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"decision_name": "DiscardFromHandDecision", "card": self.card.short}


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
    | DiscardFromHandDecision
)
