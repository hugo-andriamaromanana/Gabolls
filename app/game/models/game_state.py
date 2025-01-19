from app.game.models.pydantic_config import BaseModel

from app.game.models.lobby import Lobby
from app.game.models.phase import GamePhase
from app.game.models.round import Round
from app.game.models.rules import Rules
from app.game.models.seed import Seed


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
