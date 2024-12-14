from dataclasses import dataclass
from gabolls.models.deck import Deck
from gabolls.models.lobby import Lobby
from gabolls.models.player import Player
from gabolls.models.turn import Turn


@dataclass
class Round:
    number: int
    lobby: Lobby
    discard_pile: Deck
    deck: Deck
    current_player: Player
    turns: list[Turn]

    @property
    def is_over(self) -> bool:
        return any(player.declared_win for player in self.lobby.players)
