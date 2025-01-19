from typing import TypeAlias

from gabolls_game.models.pydantic_config import BaseModel
from gabolls_game.models.card import Card
from gabolls_game.models.player_card import PlayerCard
from enum import StrEnum, auto


class InHandDecisionType(StrEnum):
    DISCARD = auto()
    SWAP = auto()


class DrawDecisionType(StrEnum):
    FROM_DECK = auto()
    FROM_DISCARD = auto()


class InHandDiscardDecision(BaseModel):
    card: Card


class InHandSwapDecision(BaseModel):
    owner_card: Card
    in_hand_card: Card


class BlindExchangeCardDecision(BaseModel):
    player_card: Card
    other_player_card: PlayerCard


class ViewExchangeCardDecision(BaseModel):
    player_card: Card
    other_player_card: PlayerCard


class PeakDecision(BaseModel):
    player_card: PlayerCard


class SkipViewExchangeDecision(BaseModel):
    pass


class SkipSpellDecision(BaseModel):
    pass


class DrawFromDeckDecision(BaseModel):
    pass


class DrawFromDiscardDecision(BaseModel):
    pass


class CallWinDecision(BaseModel):
    pass


class CallCounterDecision(BaseModel):
    pass


class DiscardFromHandDecision(BaseModel):
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
    | DiscardFromHandDecision
)


class Config:
    arbitrary_types_allowed = True
    use_enum_values = True
