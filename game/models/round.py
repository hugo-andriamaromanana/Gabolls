from game.models.pydantic_config import BaseModel
from game.models.action import RoundAction
from game.models.card import Card
from game.models.deck import Deck
from game.models.discard import DiscardRequests
from game.models.errors import PlayerNotFoundInRoundError
from game.models.lobby import Lobby
from game.models.player import Player
from game.models.spell_response import SpellResponse


class Round(BaseModel):
    number: int
    lobby: Lobby
    discard_pile: Deck
    deck: Deck
    current_player: Player
    player_scores: dict[int, int]
    actions: list[RoundAction]
    discard_requests: DiscardRequests
    declared_wins: list[Player]
    drawn_card: Card
    spell_response: SpellResponse
    counter_win_called: bool

    def get_player_score(self, player_id: int) -> int:
        score = self.player_scores.get(player_id)
        if score is None:
            raise PlayerNotFoundInRoundError(
                f"Player {player_id} was not found in the current round"
            )
        return score

    @property
    def is_over(self) -> bool:
        return len(self.declared_wins) > 0
