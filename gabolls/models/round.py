from dataclasses import dataclass
from typing import Any
from gabolls.models.action import RoundAction
from gabolls.models.card import Card
from gabolls.models.deck import Deck
from gabolls.models.discard import DiscardRequests
from gabolls.models.errors import PlayerNotFoundInRoundError
from gabolls.models.lobby import Lobby
from gabolls.models.player import Player
from gabolls.models.spell_response import SpellResponse


@dataclass(slots=True)
class Round:
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

    @property
    def as_dict(self) -> dict[str, Any]:
        return {
            "number": self.number,
            "discard_pile": self.discard_pile.short,
            "deck": self.deck.short,
            "current_player_id": self.current_player.id,
            "player_scores": self.player_scores,
            "actions": [action.action.as_dict for action in self.actions],
            "discard_requests": self.discard_requests.as_list,
            "declared_wins_id": [player.id for player in self.declared_wins],
            "drawn_card": self.drawn_card.short,
            "spell_response": self.spell_response.as_dict,
            "counter_win_called": self.counter_win_called,
        }
