from dataclasses import dataclass
from gabolls.models.card import Card


@dataclass
class Hand:
    cards: list[Card]

    def add(self, draw: list[Card] | Card) -> None:
        if isinstance(draw, Card):
            self.cards.append(draw)
        else:
            self.cards = draw + self.cards

    @property
    def is_empty(self) -> bool:
        return len(self.cards) == 0
