from dataclasses import dataclass
from itertools import cycle

from gabolls.models.player import Player


@dataclass
class Lobby:
    players: set[Player]

    def __post_init__(self) -> None:
        self.cycle = cycle(self.players)

    @property
    def player_points(self) -> list[int]:
        return [player.score for player in self.players]

    @property
    def leading_score(self) -> int:
        return max(self.player_points)

    @property
    def leaders(self) -> list[Player]:
        return [player for player in self.players if player.score == self.leading_score]

    @property
    def next_player(self) -> Player:
        return next(self.cycle)
