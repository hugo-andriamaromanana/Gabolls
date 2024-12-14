from dataclasses import dataclass

from gabolls.models.lobby import Lobby
from gabolls.models.round import Round
from gabolls.models.rules import Rules
from gabolls.models.seed import Seed


@dataclass
class Game:
    lobby: Lobby
    seed: Seed
    rules: Rules
    rounds: list[Round]

    @property
    def is_over(self) -> bool:
        return any(player.lost for player in self.lobby.players)
