from app.schemas.pydantic_config import BaseModel
from app.schemas.action import RoundAction
from app.schemas.card import Card
from app.schemas.deck import Deck
from app.schemas.discard import DiscardRequests
from app.schemas.errors import PlayerNotFoundInRoundError
from app.schemas.lobby import Lobby
from app.schemas.player import Player
from app.schemas.spell_response import SpellResponse


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
