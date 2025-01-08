from dataclasses import dataclass
from gabolls.models.action import RoundAction
from gabolls.models.deck import Deck
from gabolls.models.errors import PlayerNotFoundInRoundError
from gabolls.models.lobby import Lobby
from gabolls.models.player import Player


@dataclass
class Round:
    number: int
    lobby: Lobby
    discard_pile: Deck
    deck: Deck
    current_player: Player
    players_declared_win: list[Player]
    player_scores: dict[Player, int]
    actions: list[RoundAction]

    def get_player_score(self, player: Player) -> int:
        score = self.player_scores.get(player)
        if score is None:
            raise PlayerNotFoundInRoundError(
                f"Player {player} was not found in the current round"
            )
        return score

    @property
    def is_over(self) -> bool:
        return len(self.players_declared_win) > 0
