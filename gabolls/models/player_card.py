from dataclasses import dataclass

from gabolls.models.card import Card
from gabolls.models.player import Player


@dataclass
class PlayerCard:
    player: Player
    card: Card
