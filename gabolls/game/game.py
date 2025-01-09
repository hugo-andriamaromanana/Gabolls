from gabolls.game.round import create_round
from gabolls.models.game import GameState
from gabolls.models.lobby import Lobby
from gabolls.models.phase import GamePhase, GamePhaseType
from gabolls.models.player import Player
from gabolls.models.round import Round
from gabolls.models.rules import Rules
from gabolls.models.seed import Seed


def create_start_game_state(
    players: set[Player], rules: Rules, seed_source: int, first_player: Player
) -> GameState:
    seed = Seed(seed_source, 0)
    lobby = Lobby(players)
    deck_seed = seed.next()
    round_nb = 0
    rounds: list[Round] = []
    round = create_round(
        lobby, deck_seed, rules.start_hand_size, round_nb, first_player
    )
    start_game_phase = GamePhase(first_player, GamePhaseType.DRAWING)
    game = GameState(lobby, round_nb, seed, rules, round, rounds, start_game_phase)
    return game
