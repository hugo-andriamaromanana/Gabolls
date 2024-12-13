from random import Random
from gabolls.models.card import Card
from gabolls.models.rank import Rank
from gabolls.models.suit import Suit


class Deck:
    cards: list[Card]

    def draw(self, number_of_cards: int) -> list[Card]:
        draw = []
        for _ in range(number_of_cards):
            draw.append(self.cards.pop(0))
        return draw

    def shuffle(self, random: Random) -> None:
        random.shuffle(self.cards)

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


def create_standard_cards() -> list[Card]:
    cards = [
        Card(Rank.KING, Suit.CLUB, BLACK_KING_RANK),
        Card(Rank.KING, Suit.SPADE, BLACK_KING_RANK),
        Card(Rank.KING, Suit.DIAMOND, RED_KING_RANK),
        Card(Rank.KING, Suit.HEART, RED_KING_RANK),
    ]
    for rank, value in STANDARD_RANK_SCORES.items():
        for suit in Suit:
            card = Card(rank, suit, value)
            cards.append(card)
    return cards
