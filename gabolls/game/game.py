from gabolls.game.round import create_round, play_round
from gabolls.models.game import Game
from gabolls.models.lobby import Lobby
from gabolls.models.player import Player
from gabolls.models.round import Round
from gabolls.models.round_end import RoundEnd
from gabolls.models.rules import Rules
from gabolls.models.seed import Seed


def create_game(players: set[Player], rules: Rules, seed_source: int) -> Game:
    seed = Seed(seed_source, 0)
    lobby = Lobby(players)
    game = Game(lobby, seed, rules, [])
    return game


async def play_game(game: Game) -> GameResume:

    round_count = 0
    player_end_rounds: dict[Player, list[RoundEnd]] = {
        player: [] for player in game.lobby.players
    }

    while not game.is_over:

        deck_seed = game.seed.next()
        round: Round = create_round(
            game.lobby, deck_seed, game.rules.start_hand_size, round_count
        )
        round_ends: list[RoundEnd] = await play_round(round, game.rules)
        for round_end in round_ends:
            player_end_rounds[round_end.player].append(round_end)

    return game
