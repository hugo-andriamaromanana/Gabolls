from gabolls.game.round import create_round
from gabolls.models.game import Game
from gabolls.models.lobby import Lobby
from gabolls.models.player import Player
from gabolls.models.rules import Rules
from gabolls.models.seed import Seed


def create_game(players: set[Player], rules: Rules, seed_source: int) -> Game:
    seed = Seed(seed_source, 0)
    lobby = Lobby(players)
    game = Game(lobby, seed, rules, [])
    return game


async def play_round(game: Game) -> Game:

    round_count = 0

    while not game.is_over:

        deck_seed = game.seed.next()
        round = create_round(
            game.lobby, deck_seed, game.rules.start_hand_size, round_count
        )
        round_ends = await play_round(game)

    return game
