from dataclasses import dataclass
from pydantic import BaseModel, EmailStr
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import List, TypedDict

from .player import Player


from ..db import BaseDbObject



class DbScoreBoard(BaseDbObject):
    __tablename__ = "score_boards"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    players = relationship("Player", back_populates="score_board")
