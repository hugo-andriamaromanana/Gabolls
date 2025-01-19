from app.game.models.pydantic_config import BaseModel
from app.game.models.card import Card
from app.game.models.player import Player


class PlayerCard(BaseModel):
    player: Player
    card: Card
