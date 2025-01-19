from gabolls_game.models.pydantic_config import BaseModel
from gabolls_game.models.card import Card
from gabolls_game.models.player import Player


class PlayerCard(BaseModel):
    player: Player
    card: Card
