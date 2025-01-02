from dataclasses import dataclass
from gabolls.models.deck import Deck
from gabolls.models.lobby import Lobby
from gabolls.models.player import Player


@dataclass
class Round:
    number: int
    lobby: Lobby
    discard_pile: Deck
    deck: Deck
    current_player: Player
    players_declared_win: list[Player]
    player_scores: dict[Player, int]

    @property
    def is_over(self) -> bool:
        return len(self.players_declared_win) > 0
