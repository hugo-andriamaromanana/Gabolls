from dataclasses import dataclass
from gabolls.models.card import CardView
from gabolls.models.hand import Hand
from gabolls.models.profile import Profile
from gabolls.models.rules import Rules


@dataclass
class Player:
    profile: Profile
    score: int
    hand: Hand
    rules: Rules

    def view_card(self, card: CardView) -> None:
        self.hand.card_views.append(card)

    @property
    def lost(self) -> bool:
        return self.score > self.rules.round_win_cap

    @property
    def true_score(self) -> int:
        return sum(card.value for card in self.hand.cards)

    @property
    def is_eligible(self) -> bool:
        return self.true_score <= self.rules.round_win_cap

    def __hash__(self) -> int:
        return hash(self.profile)
