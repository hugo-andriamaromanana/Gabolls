from dataclasses import dataclass

from ..renum import Renum, auto


class ScoringType(Renum):
    Gabo = auto()
    Point = auto()
    BigPenalty = auto()
    SmallPenalty = auto()
    BigComeback = auto()
    SmallComeback = auto()


@dataclass(frozen=True)
class Score:
    value: int
    type: ScoringType
