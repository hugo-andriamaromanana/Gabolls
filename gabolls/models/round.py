from gabolls.models.pydantic_config import BaseModel
from gabolls.models.action import RoundAction
from gabolls.models.card import Card
from gabolls.models.deck import Deck
from gabolls.models.discard import DiscardRequests
from gabolls.models.errors import PlayerNotFoundInRoundError
from gabolls.models.lobby import Lobby
from gabolls.models.player import Player
from gabolls.models.spell_response import SpellResponse


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
