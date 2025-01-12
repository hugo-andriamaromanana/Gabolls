from gabolls.api.round import ask_player_draw_decision
from gabolls.game.phases.counter import solve_counters
from gabolls.game.phases.discard import solve_discard
from gabolls.game.phases.drawing import draw_phase
from gabolls.game.phases.in_hand import in_hand_phase
from gabolls.game.game import create_round
from gabolls.game.spells import play_spell
from gabolls.models.card_view import CardView
from gabolls.models.errors import UnclearedSpellType
from gabolls.models.game import GameState
from gabolls.models.phase import GamePhaseType


async def update_game_state(game_state: GameState) -> GameState:

    if game_state.game_phase.type is GamePhaseType.NEW_ROUND:
        game_state.round_nb += 1
        deck_seed = game_state.seed.next()
        first_player = game_state.lobby.next_player
        game_state.round = create_round(
            game_state.lobby,
            deck_seed,
            game_state.round_nb,
            first_player.id,
        )

        # player draw hand size cards each
        for player in game_state.lobby.players:
            player.hand.add(
                game_state.round.deck.draw(game_state.rules.start_hand_size)
            )

        # each player looks their first 2 cards
        for player in game_state.lobby.players:
            for card in game_state.round.deck.cards[: game_state.rules.starting_view]:
                player.view_card(CardView(card, player.id))

        game_state.game_phase.type = GamePhaseType.DRAWING
        return game_state

    elif game_state.game_phase.type is GamePhaseType.DRAWING:
        draw_decision = await ask_player_draw_decision(game_state.game_phase.player)
        game_state.round, game_state.round.drawn_card = await draw_phase(
            draw_decision, game_state.round, game_state.game_phase.player
        )
        game_state.game_phase.type = GamePhaseType.DISCARDING_0
        return game_state

    elif game_state.game_phase.type is GamePhaseType.DISCARDING_0:
        game_state.round = await solve_discard(
            game_state.round, game_state.round.discard_requests.queue
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
            game_state.round, game_state.round.discard_requests.queue
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
