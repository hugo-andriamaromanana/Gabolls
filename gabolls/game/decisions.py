from enum import StrEnum, auto


class InHandDecisionType(StrEnum):
    DISCARD = auto()
    SWAP = auto()


class DrawDecisionType(StrEnum):
    FROM_DECK = auto()
    FROM_DISCARD = auto()
