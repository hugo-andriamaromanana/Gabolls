from dataclasses import dataclass
from gabolls.models.action import ActionType
from gabolls.models.deck import Deck
from gabolls.models.hand import Hand
from gabolls.models.profile import Profile
from gabolls.models.rules import Rules
from gabolls.models.score import Score


@dataclass
class Player:
    profile: Profile
    score: Score
    hand: Hand
    rules: Rules
    actions_history: list[ActionType]
    declared_win: bool = False

    def draw(self, deck: Deck, number_of_cards: int) -> None:
        deck.draw(number_of_cards)

    @property
    def lost(self) -> bool:
        return self.score.points > self.rules.round_win_cap
