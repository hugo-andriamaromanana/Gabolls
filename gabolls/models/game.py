from dataclasses import dataclass
from typing import Any

from gabolls.models.lobby import Lobby
from gabolls.models.phase import GamePhase
from gabolls.models.round import Round
from gabolls.models.rules import Rules
from gabolls.models.seed import Seed


@dataclass(slots=True)
class GameState:
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

    @property
    def to_dict(self) -> dict[str, Any]:
        return {
            "lobby": self.lobby.as_dict,
            "round_nb": self.round_nb,
            "seed": self.seed.as_dict,
            "rules": self.rules.as_dict,
            "round": self.round.as_dict,
            "rounds": [round.as_dict for round in self.rounds],
            "game_phase": self.game_phase.as_dict,
        }
