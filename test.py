from .gabolls_api.data_objects.player import Player
from .gabolls_api.data_objects.game import Game


def test_game():
    player1  = Player(name="Hugo")
    
    game = Game()
