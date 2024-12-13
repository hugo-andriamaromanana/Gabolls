from dataclasses import dataclass
from random import Random

from gabolls.models.player import Player
from gabolls.models.round import Round
from gabolls.models.rules import Rules


@dataclass(slots=True)
class Game:
    players: list[Player]
    random: Random
    rules: Rules
    rounds: list[Round]

    @property
    def is_over(self) -> bool:
        return any(player.lost for player in self.players)
