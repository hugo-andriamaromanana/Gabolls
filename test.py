from gabolls_api.data_objects.player import Player
from gabolls_api.data_objects.game import Game
from icecream import ic

from gabolls_api.give_scores import PenaltyType, give_gabo, give_penalty


def test_game():
    player1  = Player(name="Hugo")
    player2 = Player(name="Enzo")
    all_players = [player1, player2]
    game = Game(players = all_players)
    give_gabo(player1)
    give_penalty(player2, PenaltyType.Big)
    game.player_scores
    ic(game)
    
test_game() 
    