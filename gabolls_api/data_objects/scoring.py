"""file that do stuff"""

from dataclasses import dataclass
from enum import Enum, auto


class ScoringType(Enum):
    """Hey i'm doing something"""

    Gabo = auto()
    Point = auto()
    BigPenalty = auto()
    SmallPenalty = auto()
    BigComeback = auto()
    SmallComeback = auto()


@dataclass(frozen=True, unsafe_hash=True)
class ScoringResult:
    """big object"""

    score: int
    scoring_type: ScoringType
