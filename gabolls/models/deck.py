from dataclasses import dataclass
from random import Random

from gabolls.models.card import BLANK_CARD, Card
from gabolls.models.card_view import CardView
from gabolls.models.errors import CannotDrawFromEmptyDeck
from gabolls.models.rank import Rank
from gabolls.models.suit import Suit


@dataclass(slots=True)
class Deck:
    cards: list[Card]
    seed: int

    def draw(self, number_of_cards: int) -> list[Card]:
        draw: list[Card] = []
        for _ in range(number_of_cards):
            draw.append(self.cards.pop(0))
        return draw

    @property
    def top_card_view(self) -> CardView:
        if not self.is_empty:
            return CardView(self.cards[0], None)
        else:
            return CardView(BLANK_CARD, None)

    def add_to_top(self, card: Card) -> None:
        self.cards.insert(0, card)

    def shuffle(self) -> None:
        Random(self.seed).shuffle(self.cards)

    def draw_top_card(self) -> Card:
        top_card = self.cards.pop(0)
        if self.is_empty or not isinstance(top_card, Card):
            raise CannotDrawFromEmptyDeck
        return top_card

    @property
    def is_empty(self) -> bool:
        return len(self.cards) > 0

    @property
    def short(self) -> dict[str, list[str] | int]:
        return {"seed": self.seed, "cards": [card.short for card in self.cards]}
