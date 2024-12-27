from dataclasses import dataclass
from random import Random

from gabolls.models.card import BLANK_CARD, Card, CardView
from gabolls.models.errors import CannotDrawFromEmptyDeck
from gabolls.models.rank import Rank
from gabolls.models.suit import Suit


@dataclass
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


STANDARD_RANK_SCORES: dict[Rank, int] = {
    Rank.ACE: 1,
    Rank.TWO: 2,
    Rank.THREE: 3,
    Rank.FOUR: 4,
    Rank.FIVE: 5,
    Rank.SIX: 6,
    Rank.SEVEN: 7,
    Rank.EIGHT: 8,
    Rank.NINE: 9,
    Rank.TEN: 10,
    Rank.JACK: 11,
    Rank.QUEEN: 12,
}

BLACK_KING_RANK = 13
RED_KING_RANK = 0

BLACK_KINGS = [
    Card(Rank.KING, Suit.CLUB, BLACK_KING_RANK),
    Card(Rank.KING, Suit.SPADE, BLACK_KING_RANK),
    Card(Rank.KING, Suit.DIAMOND, RED_KING_RANK),
    Card(Rank.KING, Suit.HEART, RED_KING_RANK),
]


def _create_standard_cards() -> list[Card]:
    deck = []
    for rank, value in STANDARD_RANK_SCORES.items():
        for suit in Suit:
            card = Card(rank, suit, value)
    return deck + BLACK_KINGS


STANDARD_CARDS: list[Card] = _create_standard_cards()
