from gabolls_game.models.pydantic_config import BaseModel
from gabolls_game.models.card import Card
from gabolls_game.models.card_view import CardView

from gabolls_game.models.errors import CardNotInPlayerHand


class Hand(BaseModel):
    cards: list[Card]
    card_views: list[CardView]

    def discard(self, card: Card) -> None:
        self.cards.remove(card)

    def add(self, draw: list[Card] | Card) -> None:
        if isinstance(draw, Card):
            self.cards.append(draw)
        else:
            self.cards = draw + self.cards

    @property
    def size(self) -> int:
        return len(self.cards)

    @property
    def indexes(self) -> list[int]:
        return list(range(self.size))

    def swap(self, self_card: Card, other_card: Card) -> Card:
        if self_card not in self.cards:
            raise CardNotInPlayerHand(f"card: {self_card}, not in player Hand")
        player_card_index = self.cards.index(self_card)
        self.cards[player_card_index] = other_card
        return self_card

    @property
    def is_empty(self) -> bool:
        return len(self.cards) == 0

    @property
    def short(self) -> str:
        return f"{".".join(card.short for card in self.cards)}/{".".join(card.short for card in self.card_views)}"
