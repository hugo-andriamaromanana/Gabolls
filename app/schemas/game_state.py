from app.schemas.pydantic_config import BaseModel

from app.schemas.lobby import Lobby
from app.schemas.phase import GamePhase
from app.schemas.round import Round
from app.schemas.rules import Rules
from app.schemas.seed import Seed


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
