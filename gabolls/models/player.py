from typing import Any

from gabolls.models.config import BaseModel
from gabolls.models.card_view import CardView
from gabolls.models.hand import Hand
from gabolls.models.profile import Profile
from gabolls.models.rules import Rules


class Player(BaseModel):
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

    @property
    def id(self) -> int:
        return self.profile.id

    @property
    def as_dict(self) -> dict[str, Any]:
        return {
            "profile": self.profile.as_dict,
            "score": self.score,
            "hand": self.hand.short,
        }

    def __hash__(self) -> int:
        return self.profile.id
