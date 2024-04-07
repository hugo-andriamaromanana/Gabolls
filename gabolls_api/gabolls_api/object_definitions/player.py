from typing import List
from idna import valid_contextj
from numpy import place
from pydantic import UUID4, BaseModel, Field
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column


from ..db import BaseDbObject


from dataclasses import dataclass
from enum import Enum, auto


class ScoringType(Enum):
    Gabo = "Gabo"
    Point = "Point"
    BigPenalty = "BigPenalty"
    SmallPenalty = "SmallPenalty"
    BigComeback = "BigComeback"
    SmallComeback = "SmallComeback"


class DbScoreboard(BaseDbObject):
    __tablename__ = 'scoreboard'



class Score(BaseModel):
    value: int
    type: ScoringType
    
class Player(BaseModel):
    tag: str
    scores: List[Score] = Field(default_factory=list)


class ScoreBoard(BaseModel):
    players: List[Player] = Field(default_factory=list)
