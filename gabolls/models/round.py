from gabolls.models.card import Card
from gabolls.models.deck import Deck
from gabolls.models.player import Player


class Round:
    players: list[Player] 
    discard_pile: list[Card] 
    deck: Deck 

    @property
    def is_over(self) -> bool:
        return any(player.declared_win for player in self.players)
