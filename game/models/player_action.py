from typing import TypeAlias

from game.models.pydantic_config import BaseModel
from game.models.card import Card
from game.models.decisions import PlayerDecisons
from game.models.player import Player
from game.models.player_card import PlayerCard
from game.models.spell import SpellType


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
