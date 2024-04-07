
from dataclasses import dataclass
from enum import Enum, auto



class ScoringType(Enum):
    Gabo = auto()
    Point = auto()
    BigPenalty = auto()
    SmallPenalty = auto()
    BigComeback = auto()
    SmallComeback = auto()


@dataclass(frozen=True, unsafe_hash=True)
class ScoringResult:
    score: int
    scoring_type: ScoringType

