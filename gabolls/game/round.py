from gabolls.game.phases.counter import solve_counters
from gabolls.game.phases.discard import solve_discard
from gabolls.game.phases.drawing import draw_phase
from gabolls.game.phases.in_hand import in_hand_phase
from gabolls.game.spells import play_spell
from gabolls.models.action import RoundAction
from gabolls.models.card import BLANK_CARD
from gabolls.models.deck import STANDARD_CARDS, Deck
from gabolls.models.discard import DiscardRequests
from gabolls.models.errors import UnclearedSpellType
from gabolls.models.game import GameState
from gabolls.models.lobby import Lobby
from gabolls.models.phase import GamePhaseType
from gabolls.models.player import Player
from gabolls.models.round import Round


from gabolls.models.spell_response import SpellResponse


def create_round(
    lobby: Lobby,
    deck_seed: int,
    hand_size: int,
    round_number: int,
    first_player: Player,
) -> Round:

    deck = Deck(STANDARD_CARDS, deck_seed)
    deck.shuffle()
    discard_pile: Deck = Deck([], 0)
    declared_winners: list[Player] = []
    player_scores = {player: 0 for player in lobby.players}
    round_actions: list[RoundAction] = []
    discard_requests = DiscardRequests([])

    round = Round(
        round_number,
        lobby,
        discard_pile,
        deck,
        first_player,
        player_scores,
        round_actions,
        discard_requests,
        declared_winners,
        BLANK_CARD,
        SpellResponse(False, None),
        False,
    )

    # player draw hand size cards each
    for player in lobby.players:
        player.hand.add(deck.draw(hand_size))

    return round


async def play_game(game_state: GameState) -> GameState:

    if game_state.game_phase.type is GamePhaseType.NEW_ROUND:
        game_state.round_nb += 1
        deck_seed = game_state.seed.next()
        first_player = game_state.lobby.next_player
        game_state.round = create_round(
            game_state.lobby,
            deck_seed,
            game_state.rules.start_hand_size,
            game_state.round_nb,
            first_player,
        )
        return game_state

    elif game_state.game_phase.type is GamePhaseType.DRAWING:
        game_state.round, game_state.round.drawn_card = await draw_phase(
            game_state.round, game_state.game_phase.player
        )
        game_state.game_phase.type = GamePhaseType.DISCARDING_0
        return game_state

    elif game_state.game_phase.type is GamePhaseType.DISCARDING_0:
        game_state.round = await solve_discard(
            game_state.round, game_state.round.discard_requests
        )
        game_state.round.discard_requests.clear()
        game_state.game_phase.type = GamePhaseType.IN_HAND
        return game_state

    elif game_state.game_phase.type is GamePhaseType.IN_HAND:
        game_state.round, game_state.round.spell_response = await in_hand_phase(
            game_state.round, game_state.game_phase.player, game_state.round.drawn_card
        )
        if game_state.round.spell_response.ok:
            game_state.game_phase.type = GamePhaseType.PLAY_SPELL
        else:
            game_state.game_phase.type = GamePhaseType.DISCARDING_1
        return game_state

    elif game_state.game_phase.type is GamePhaseType.PLAY_SPELL:
        if (game_state.round.spell_response.spell_type is None) or (
            not game_state.round.spell_response.ok
        ):
            raise UnclearedSpellType()
        game_state.round = await play_spell(
            game_state.game_phase.player,
            game_state.round.spell_response.spell_type,
            game_state.round,
        )
        game_state.game_phase.type = GamePhaseType.DISCARDING_1
        return game_state

    elif game_state.game_phase.type is GamePhaseType.DISCARDING_1:
        game_state.round = await solve_discard(
            game_state.round, game_state.round.discard_requests
        )
        game_state.round.discard_requests.clear()
        game_state.game_phase.type = GamePhaseType.CHECK_ROUND_OVER
        return game_state

    elif game_state.game_phase.type is GamePhaseType.CHECK_ROUND_OVER:
        if game_state.round.is_over:
            game_state.game_phase.type = GamePhaseType.ROUND_OVER
        else:
            game_state.game_phase.type = GamePhaseType.NEXT_PLAYER
        return game_state

    elif game_state.game_phase.type is GamePhaseType.NEXT_PLAYER:
        game_state.game_phase.player = game_state.lobby.next_player
        game_state.game_phase.type = GamePhaseType.DRAWING
        return game_state

    elif game_state.game_phase.type is GamePhaseType.ROUND_OVER:
        game_state.round, game_state.round.counter_win_called = await solve_counters(
            game_state.round
        )
        if game_state.round.counter_win_called:
            game_state.game_phase.type = GamePhaseType.COUNTER
        else:
            game_state.game_phase.type = GamePhaseType.UPDATE_PLAYER_SCORES
        return game_state

    elif game_state.game_phase.type is GamePhaseType.CHECK_GAME_OVER:
        if game_state.is_over:
            game_state.game_phase.type = GamePhaseType.GAME_OVER
        else:
            game_state.game_phase.type = GamePhaseType.NEW_ROUND
        return game_state

    else:
        raise NotImplementedError
