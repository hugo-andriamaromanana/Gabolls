from dataclasses import dataclass
from typing import Any, TypeAlias
from gabolls.models.card import Card
from gabolls.models.decisions import PlayerDecisons
from gabolls.models.player import Player
from gabolls.models.player_card import PlayerCard
from gabolls.models.spell import SpellType


@dataclass(slots=True)
class PeakCardAction:
    player_card: PlayerCard

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"action_name": "PeakCardAction", "player_card": self.player_card}


@dataclass(slots=True)
class DrawFromDeckAction:
    card: Card

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"action_name": "DrawFromDeckAction", "card": self.card.short}


@dataclass(slots=True)
class DrawFromDiscardAction:
    card: Card

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"action_name": "DrawFromDiscardAction", "card": self.card.short}


@dataclass(slots=True)
class InHandDiscardToPileAction:
    card: Card

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"action_name": "InHandDiscardToPileAction", "card": self.card.short}


@dataclass(slots=True)
class SkipSpellAction:
    spell_type: SpellType

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"action_name": "SkipSpellAction", "spell_type": self.spell_type}


@dataclass(slots=True)
class InHandSwapAction:
    owner_card: Card
    in_hand_card: Card

    @property
    def as_dict(self) -> dict[str, Any]:
        return {
            "action_name": "InHandSwapAction",
            "owner_card": self.owner_card.short,
            "in_hand_card": self.in_hand_card.short,
        }


@dataclass(slots=True)
class BlindExchangeCardAction:
    self_card: Card
    other_player_card: PlayerCard

    @property
    def as_dict(self) -> dict[str, Any]:
        return {
            "action_name": "BlindExchangeCardAction",
            "self_card": self.self_card.short,
            "other_player_card": self.other_player_card.short,
        }


@dataclass(slots=True)
class ViewExchangeCardAction:
    player_card: Card
    other_player_card: PlayerCard

    @property
    def as_dict(self) -> dict[str, Any]:
        return {
            "action_name": "ViewExchangeCardAction",
            "player_card": self.player_card.short,
            "other_player_card": self.other_player_card.short,
        }


@dataclass(slots=True)
class DrawPunishementCardAction:
    card: Card

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"action_name": "DrawPunishementCardAction", "card": self.card.short}


@dataclass(slots=True)
class DiscardFromHandAction:
    card: Card

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"action_name": "DiscardFromHandAction", "card": self.card.short}


class CounterAction:
    def __init__(self) -> None:
        self.as_dict = {"action_name": "CounterAction"}


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


@dataclass(slots=True)
class PlayerAction:
    player: Player
    decision: PlayerDecisons
    action: PlayerActions

    @property
    def as_dict(self) -> dict[str, Any]:
        return {
            "player_id": self.player.id,
            "decision": self.decision.as_dict,
            "action": self.action.as_dict,
        }
