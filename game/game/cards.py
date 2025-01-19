from game.models.card import Card
from game.models.rank import Rank
from game.models.suit import Suit


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
    Card(rank=Rank.KING, suit=Suit.CLUB, value=BLACK_KING_RANK),
    Card(rank=Rank.KING, suit=Suit.SPADE, value=BLACK_KING_RANK),
    Card(rank=Rank.KING, suit=Suit.DIAMOND, value=RED_KING_RANK),
    Card(rank=Rank.KING, suit=Suit.HEART, value=RED_KING_RANK),
]

STANDARD_SUITS = [Suit.CLUB, Suit.DIAMOND, Suit.HEART, Suit.SPADE]


def create_standard_cards() -> list[Card]:
    deck = []
    for rank, value in STANDARD_RANK_SCORES.items():
        for suit in STANDARD_SUITS:
            deck.append(Card(rank=rank, suit=suit, value=value))
    return deck + BLACK_KINGS
