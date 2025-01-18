from gabolls.models.config import BaseModel
from gabolls.models.card import Card
from gabolls.models.player import Player


class PlayerCard(BaseModel):
    player: Player
    card: Card
