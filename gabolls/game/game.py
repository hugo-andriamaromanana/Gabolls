from collections.abc import Iterable
from itertools import cycle

from gabolls.game.cards import create_standard_cards
from gabolls.models.action import RoundAction
from gabolls.models.card import BLANK_CARD
from gabolls.models.deck import Deck
from gabolls.models.discard import DiscardRequests
from gabolls.models.game_state import GameState
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
    cycle_profiles = cycle(profiles)
    for profile in profiles:
        start_hand = Hand(cards=[], card_views=[])
        player = Player(profile=profile, score=0, hand=start_hand, rules=rules)
        players.add(player)
    lobby = Lobby(
        first_player_id=first_player_id, players=list(players), cycle=cycle_profiles
    )
    return lobby


def create_start_game_state(
    lobby: Lobby, rules: Rules, seed_source: int,   first_player_id: int
) -> GameState:
    seed = Seed(source=seed_source, offset=0)
    deck_seed = seed.next()
    round_nb = 0
    rounds: list[Round] = []
    round = create_round(lobby, deck_seed, round_nb, first_player_id)
    start_game_phase = GamePhase(
        player=lobby.get_player_by_id(first_player_id), type=GamePhaseType.NEW_ROUND
    )
    game = GameState(
        lobby=lobby,
        round_nb=round_nb,
        seed=seed,
        rules=rules,
        round=round,
        rounds=rounds,
        game_phase=start_game_phase,
    )
    return game


def create_round(
    lobby: Lobby,
    deck_seed: int,
    round_number: int,
    first_player_id: int,
) -> Round:

    deck = Deck(cards=create_standard_cards(), seed=deck_seed)
    deck.shuffle()
    discard_pile: Deck = Deck(cards=[], seed=0)
    declared_winners: list[Player] = []
    player_scores = {player.id: 0 for player in lobby.players}
    round_actions: list[RoundAction] = []
    discard_requests = DiscardRequests(queue=[])

    round = Round(
        number=round_number,
        lobby=lobby,
        discard_pile=discard_pile,
        deck=deck,
        current_player=lobby.get_player_by_id(first_player_id),
        player_scores=player_scores,
        actions=round_actions,
        discard_requests=discard_requests,
        declared_wins=declared_winners,
        drawn_card=BLANK_CARD,
        spell_response=SpellResponse(ok=False, spell_type=None),
        counter_win_called=False,
    )
    return round






