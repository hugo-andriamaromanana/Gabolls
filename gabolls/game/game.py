from collections.abc import Iterable

from gabolls.game.cards import create_standard_cards
from gabolls.models.action import RoundAction
from gabolls.models.card import BLANK_CARD
from gabolls.models.deck import Deck
from gabolls.models.discard import DiscardRequests
from gabolls.models.game import GameState
from gabolls.models.hand import Hand
from gabolls.models.lobby import Lobby
from gabolls.models.phase import GamePhase, GamePhaseType
from gabolls.models.player import Player
from gabolls.models.profile import Profile
from gabolls.models.round import Round
from gabolls.models.rules import Rules
from gabolls.models.seed import Seed
from gabolls.models.spell_response import SpellResponse


def create_new_lobby(
    profiles: Iterable[Profile], first_player_id: int, rules: Rules
) -> Lobby:
    players = set()
    for profile in profiles:
        start_hand = Hand([], [])
        player = Player(profile, 0, start_hand, rules)
        players.add(player)
    lobby = Lobby(first_player_id, players)
    return lobby


def create_start_game_state(
    lobby: Lobby, rules: Rules, seed_source: int, first_player_id: int
) -> GameState:
    seed = Seed(seed_source, 0)
    deck_seed = seed.next()
    round_nb = 0
    rounds: list[Round] = []
    round = create_round(lobby, deck_seed, round_nb, first_player_id)
    start_game_phase = GamePhase(
        lobby.get_player_by_id(first_player_id), GamePhaseType.NEW_ROUND
    )
    game = GameState(lobby, round_nb, seed, rules, round, rounds, start_game_phase)
    return game


def create_round(
    lobby: Lobby,
    deck_seed: int,
    round_number: int,
    first_player_id: int,
) -> Round:

    deck = Deck(create_standard_cards(), deck_seed)
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
