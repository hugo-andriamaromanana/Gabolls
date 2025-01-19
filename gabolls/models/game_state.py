from gabolls.models.pydantic_config import BaseModel

from gabolls.models.lobby import Lobby
from gabolls.models.phase import GamePhase
from gabolls.models.round import Round
from gabolls.models.rules import Rules
from gabolls.models.seed import Seed


class GameState(BaseModel):
    lobby: Lobby
    round_nb: int
    seed: Seed
    rules: Rules
    round: Round
    rounds: list[Round]
    game_phase: GamePhase

    @property
    def is_over(self) -> bool:
        return any(player.lost for player in self.lobby.players)
