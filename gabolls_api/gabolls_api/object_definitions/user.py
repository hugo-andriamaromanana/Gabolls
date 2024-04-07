from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from .user_creation import MAX_TOTAL_USERNAME_LENGTH
from ..db import DeclarativeBase


class DbUser(DeclarativeBase):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    tag: Mapped[str] = mapped_column(String(MAX_TOTAL_USERNAME_LENGTH))
    mail: Mapped[str] = mapped_column(String)
    hashed_pw: Mapped[str] = mapped_column(String)
    disabled: Mapped[bool] = mapped_column(Boolean, default=False)

class DbPlayer(DeclarativeBase):
    __tablename__ = "players"
    tag: Mapped[str] = mapped_column(String(MAX_TOTAL_USERNAME_LENGTH))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user_account.id"))
    user = relationship("DbUser", back_populates="player")
    scores = relationship("DbScore", back_populates="player")

class DbScore(DeclarativeBase):
    __tablename__ = "scores"
    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[int] = mapped_column(Integer)
    type: Mapped[str] = mapped_column(String)
    player_id: Mapped[int] = mapped_column(Integer, ForeignKey("players.tag"))
    player = relationship("DbPlayer", back_populates="scores")

class DbScoreBoard(DeclarativeBase):
    __tablename__ = "score_boards"
    id: Mapped[int] = mapped_column(primary_key=True)
    players = relationship("DbPlayer", back_populates="score_board")
    
class User(BaseModel):
    tag: str

class Score(BaseModel):
    value: int
    type: str

class Player(BaseModel):
    tag: str
    user: User
    scores: List[Score] = Field(default_factory=list)

class ScoreBoard(BaseModel):
    players: List[Player] = Field(default_factory=list)
    