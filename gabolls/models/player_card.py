from dataclasses import dataclass

from gabolls.models.card import Card
from gabolls.models.player import Player


@dataclass
class PlayerCard:
    player: Player
    card: Card

    @property
    def short(self) -> dict[str, int | str]:
        return {"player_id": self.player.id, "card": self.card.short}
