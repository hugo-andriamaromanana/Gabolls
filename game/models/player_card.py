from game.models.pydantic_config import BaseModel
from game.models.card import Card
from game.models.player import Player


class PlayerCard(BaseModel):
    player: Player
    card: Card
