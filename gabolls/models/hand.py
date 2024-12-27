from dataclasses import dataclass
from gabolls.models.card import Card, CardView
from gabolls.models.errors import CardNotInPlayerHand


@dataclass
class Hand:
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
