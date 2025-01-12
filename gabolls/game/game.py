from gabolls.game.game_state import update_game_state
from gabolls.models.action import RoundAction
from gabolls.models.card import BLANK_CARD
from gabolls.models.deck import STANDARD_CARDS, Deck
from gabolls.models.discard import DiscardRequests
from gabolls.models.game import GameState
from gabolls.models.lobby import Lobby
from gabolls.models.phase import GamePhase, GamePhaseType
from gabolls.models.player import Player
from gabolls.models.round import Round
from gabolls.models.rules import Rules
from gabolls.models.seed import Seed
from gabolls.models.spell_response import SpellResponse


def create_start_game_state(
    players: set[Player], rules: Rules, seed_source: int, first_player_id: int
) -> GameState:
    seed = Seed(seed_source, 0)
    lobby = Lobby(first_player_id, players)
    deck_seed = seed.next()
    round_nb = 0
    rounds: list[Round] = []
    round = create_round(lobby, deck_seed, round_nb, first_player_id)
    start_game_phase = GamePhase(
        lobby.get_player_by_id(first_player_id), GamePhaseType.DRAWING
    )
    game = GameState(lobby, round_nb, seed, rules, round, rounds, start_game_phase)
    return game


def create_round(
    lobby: Lobby,
    deck_seed: int,
    round_number: int,
    first_player_id: int,
) -> Round:

    deck = Deck(STANDARD_CARDS, deck_seed)
    deck.shuffle()
    discard_pile: Deck = Deck([], 0)
    declared_winners: list[Player] = []
    player_scores = {player.id: 0 for player in lobby.players}
    round_actions: list[RoundAction] = []
    discard_requests = DiscardRequests([])

    round = Round(
        round_number,
        lobby,
        discard_pile,
        deck,
        lobby.get_player_by_id(first_player_id),
        player_scores,
        round_actions,
        discard_requests,
        declared_winners,
        BLANK_CARD,
        SpellResponse(False, None),
        False,
    )
    return round


async def play_game(
    lobby: Lobby, rules: Rules, seed: Seed, first_player_id: int
) -> None:

    game_state = create_start_game_state(
        lobby.players, rules, seed.source, first_player_id
    )

    while not game_state.is_over:
        game_state = await update_game_state(game_state)
