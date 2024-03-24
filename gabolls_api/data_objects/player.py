from typing import List

from pydantic import BaseModel, Field

from .scoring import ScoringResult

DEFAULT_STARTING_POINTS = 0
DEFAULT_ENDING_POINTS = 120

class Player(BaseModel):
    name: str
    scores: List[ScoringResult] = Field(default_factory=list)

    @property
    def current_score(self) -> int:
        if not self.scores:
            return DEFAULT_STARTING_POINTS
        return self.scores[-1].score

    @property
    def is_over(self) -> bool:
        return self.current_score >= DEFAULT_ENDING_POINTS

