from dataclasses import dataclass
from itertools import cycle
from typing import Any

from gabolls.models.errors import FirstPlayerNotInPLayers, PlayerNotFoundInRoundError
from gabolls.models.player import Player


@dataclass
class Lobby:
    first_player_id: int
    players: set[Player]

    def __post_init__(self) -> None:
        self.cycle = cycle(self.players)
        nb_of_players = len(list(self.cycle))

        # initializing cycle to first_player
        for _ in range(nb_of_players):
            player = next(self.cycle)
            if player.id == self.first_player_id:
                return None

        raise FirstPlayerNotInPLayers

    @property
    def next_player(self) -> Player:
        return next(self.cycle)

    def get_player_by_id(self, id: int) -> Player:
        for player in self.players:
            if player.id == id:
                return player
        raise PlayerNotFoundInRoundError(f"Player:{id} not found in players")

    @property
    def as_dict(self) -> dict[str, Any]:
        return {
            "first_player": self.first_player_id,
            "players": [player.as_dict for player in self.players],
        }
