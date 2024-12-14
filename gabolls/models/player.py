from dataclasses import dataclass
from gabolls.models.hand import Hand
from gabolls.models.profile import Profile
from gabolls.models.rules import Rules
from gabolls.models.score import Score
from gabolls.models.turn import Turn


@dataclass
class Player:
    profile: Profile
    score: Score
    hand: Hand
    rules: Rules
    turns: list[Turn]
    declared_win: bool = False

    @property
    def lost(self) -> bool:
        return self.score.points > self.rules.round_win_cap

    @property
    def true_score(self) -> int:
        return sum(card.value for card in self.hand.cards)

    @property
    def is_eligible(self) -> bool:
        return self.true_score <= self.rules.round_win_cap
