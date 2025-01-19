from typing import TypeAlias

from app.schemas.pydantic_config import BaseModel
from app.schemas.card import Card
from app.schemas.decisions import PlayerDecisons
from app.schemas.player import Player
from app.schemas.player_card import PlayerCard
from app.schemas.spell import SpellType


class PeakCardAction(BaseModel):
    player_card: PlayerCard


class DrawFromDeckAction(BaseModel):
    card: Card


class DrawFromDiscardAction(BaseModel):
    card: Card


class InHandDiscardToPileAction(BaseModel):
    card: Card


class SkipSpellAction(BaseModel):
    spell_type: SpellType


class InHandSwapAction(BaseModel):
    owner_card: Card
    in_hand_card: Card


class BlindExchangeCardAction(BaseModel):
    self_card: Card
    other_player_card: PlayerCard


class ViewExchangeCardAction(BaseModel):
    player_card: Card
    other_player_card: PlayerCard


class DrawPunishementCardAction(BaseModel):
    card: Card


class DiscardFromHandAction(BaseModel):
    card: Card


class CounterAction(BaseModel):
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


class PlayerAction(BaseModel):
    player: Player
    decision: PlayerDecisons
    action: PlayerActions
