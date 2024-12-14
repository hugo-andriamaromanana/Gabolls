from dataclasses import dataclass
from gabolls.models.card import Card
from gabolls.models.errors import CardNotInPlayerHand


@dataclass
class Hand:
    cards: list[Card]

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

    def swap(self, card: Card, other_card: Card) -> Card:
        if card not in self.cards:
            raise CardNotInPlayerHand(f"card: {card}, not in player Hand")
        player_card_index = self.cards.index(card)
        self.cards[player_card_index] = other_card
        return card

    @property
    def is_empty(self) -> bool:
        return len(self.cards) == 0
