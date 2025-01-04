from loguru import logger
from gabolls.api.round import (
    ask_is_spell_played,
    ask_player_draw_decision,
    ask_player_in_hand_decision,
    prompt_user_counter_proposal,
)
from gabolls.game.discard import solve_discard
from gabolls.models.decisions import (
    CallCounterDecision,
    DrawDecisionType,
    DrawFromDeckDecision,
    InHandDiscardDecision,
    InHandSwapDecision,
    SkipSpellDecision,
)
from gabolls.models.deck import STANDARD_CARDS, Deck
from gabolls.models.discard import DiscardRequests
from gabolls.models.errors import NoDecisionsTaken
from gabolls.models.lobby import Lobby
from gabolls.models.player import Player
from gabolls.models.round import Round
from gabolls.game.spells import (
    infer_spell_type_from_rank,
    play_spell,
)
from gabolls.game.scenario import determine_scoring_scenario, find_player_end_rounds
from gabolls.models.player_action import (
    CounterAction,
    DrawFromDeckAction,
    DrawFromDiscardAction,
    InHandDiscardToPileAction,
    InHandSwapAction,
    PlayerAction,
    SkipSpellAction,
)
from gabolls.models.round_resume import RoundResume
from gabolls.models.rules import Rules
from gabolls.models.player_action import RoundActions


def create_round(
    lobby: Lobby, deck_seed: int, hand_size: int, round_number: int
) -> Round:

    deck = Deck(STANDARD_CARDS, deck_seed)
    deck.shuffle()
    discard_pile: Deck = Deck([], 0)
    declared_winners: list[Player] = []
    player_scores = {player: 0 for player in lobby.players}
    round_actions: list[RoundActions] = []

    round = Round(
        round_number,
        lobby,
        discard_pile,
        deck,
        lobby.next_player,
        declared_winners,
        player_scores,
        round_actions,
    )

    # player draw hand size cards each
    for player in lobby.players:
        player.hand.add(deck.draw(hand_size))

    return round


async def play_round(round: Round, rules: Rules) -> RoundResume:

    discard_requests = DiscardRequests([])
    declared_wins: list[Player] = []

    while not round.is_over:
        # select player
        player = round.current_player

        # drawing phase
        draw_decision = await ask_player_draw_decision(player)

        if draw_decision is DrawDecisionType.FROM_DECK:

            drawn_card = round.deck.draw_top_card()

            deck_draw_action = DrawFromDeckAction(drawn_card)
            player_action = PlayerAction(
                player, DrawFromDeckDecision(), deck_draw_action
            )

        elif draw_decision is DrawDecisionType.FROM_DISCARD:

            drawn_card = round.discard_pile.draw_top_card()

            discard_draw_action = DrawFromDiscardAction(drawn_card)
            player_action = PlayerAction(
                player, DrawFromDeckDecision(), discard_draw_action
            )

        else:
            raise NoDecisionsTaken

        round.actions.append(player_action)

        # clear discard
        round = solve_discard(round, discard_requests)

        # in hand decision
        in_hand_decision: InHandSwapDecision | InHandDiscardDecision = (
            await ask_player_in_hand_decision(player, drawn_card)
        )
        if isinstance(in_hand_decision, InHandSwapAction):
            player.hand.swap(in_hand_decision.owner_card, in_hand_decision.in_hand_card)

            player_in_hand_swap_decision = InHandSwapDecision(
                in_hand_decision.owner_card, in_hand_decision.in_hand_card
            )
            player_in_hand_swap_action = InHandSwapAction(
                in_hand_decision.owner_card, in_hand_decision.in_hand_card
            )
            player_action = PlayerAction(
                player, player_in_hand_swap_decision, player_in_hand_swap_action
            )
            round.actions.append(player_action)

        elif isinstance(in_hand_decision, InHandDiscardToPileAction):
            round.discard_pile.add_to_top(in_hand_decision.card)

            player_in_hand_discard_decision = InHandDiscardDecision(
                in_hand_decision.card
            )
            player_in_hand_discard_action = InHandDiscardToPileAction(
                in_hand_decision.card
            )
            player_action = PlayerAction(
                player, player_in_hand_discard_decision, player_in_hand_discard_action
            )
            round.actions.append(player_action)

            if in_hand_decision.card.has_spell:
                spell_type = infer_spell_type_from_rank(in_hand_decision.card.rank)
                player_plays_spell = await ask_is_spell_played(player, spell_type)
                if player_plays_spell:
                    round = await play_spell(player, spell_type, round)
                    logger.info(f"Player: {player} of type spell: {spell_type}")
                else:
                    player_action = PlayerAction(
                        player, SkipSpellDecision(), SkipSpellAction(spell_type)
                    )
                    round.actions.append(player_action)
                    logger.info(f"Player: {player} skipped spell: {spell_type}")
        else:
            raise NoDecisionsTaken

    round = solve_discard(round, discard_requests)

    # resolve scores, counter phase
    counter_called = await prompt_user_counter_proposal(round.players_declared_win)

    counter_win_called = counter_called is not None

    if counter_called:
        player_action = PlayerAction(
            counter_called, CallCounterDecision(), CounterAction()
        )
        round.actions.append(player_action)

    round_end_scenario = determine_scoring_scenario(round, counter_win_called)
    round_ends = find_player_end_rounds(round, declared_wins, round_end_scenario, rules)

    round_resume = RoundResume(
        round.deck, round.lobby, round.actions, round_end_scenario, round_ends
    )
    return round_resume
