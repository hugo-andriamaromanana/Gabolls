from itertools import cycle
from typing import Any

from gabolls.models.errors import PlayerNotFoundInRoundError
from gabolls.models.player import Player


class Lobby:

    def __init__(self, first_player_id: int, players: set[Player]) -> None:
        self.first_player_id = first_player_id
        self.players = players
        self.cycle = cycle(self.players)
        nb_of_players = len(self.players)
        # initializing cycle to first_player
        for _ in range(nb_of_players):
            player = next(self.cycle)
            if player.id == self.first_player_id:
                return None

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
