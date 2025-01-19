from app.schemas.pydantic_config import BaseModel
from app.schemas.card import Card
from app.schemas.player import Player


class PlayerCard(BaseModel):
    player: Player
    card: Card
