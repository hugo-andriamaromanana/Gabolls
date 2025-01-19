from itertools import cycle
from typing import Any

from app.schemas.pydantic_config import BaseModel

from app.schemas.errors import PlayerNotFoundInRoundError
from app.schemas.player import Player


class Lobby(BaseModel):
    first_player_id: int
    players: list[Player]
    cycle: cycle

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
