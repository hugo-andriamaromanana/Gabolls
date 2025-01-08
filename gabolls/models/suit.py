from enum import StrEnum, auto


class Suit(StrEnum):
    HEART = auto()
    SPADE = auto()
    DIAMOND = auto()
    CLUB = auto()
    NONE = auto()


SHORT_SUITS: dict[Suit, str] = {
    Suit.HEART: "H",
    Suit.SPADE: "S",
    Suit.DIAMOND: "D",
    Suit.CLUB: "C",
    Suit.NONE: "N",
}
