from game.models.pydantic_config import BaseModel

from game.models.lobby import Lobby
from game.models.phase import GamePhase
from game.models.round import Round
from game.models.rules import Rules
from game.models.seed import Seed


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
