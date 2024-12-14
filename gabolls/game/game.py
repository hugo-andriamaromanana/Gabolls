from loguru import logger
from gabolls.game.actions import ask_player_in_hand_decision
from gabolls.game.decisions import DrawDecisionType
from gabolls.game.phases.draw import post_draw_question
from gabolls.game.phases.round import create_round
from gabolls.models.action import InHandDiscardToPile, InHandSwapAction
from gabolls.models.discard import DiscardRequests, DiscardResponse, DiscardResultType
from gabolls.models.errors import NoDecisionsTaken
from gabolls.models.game import Game
from gabolls.models.lobby import Lobby
from gabolls.models.player import Player
from gabolls.models.round import Round
from gabolls.models.rules import Rules
from gabolls.models.seed import Seed
from gabolls.models.spell import infer_spell_type_from_rank


def create_game(players: list[Player], rules: Rules, seed_source: int) -> Game:
    seed = Seed(seed_source, 0)
    lobby = Lobby(players)
    game = Game(lobby, seed, rules, [])
    return game


async def solve_discard_from_reponse(
    responses: list[DiscardResponse], round: Round
) -> Round:
    for response in responses:
        if response.result is DiscardResultType.FAIL:
            punishment_card = round.deck.draw_top_card()
            response.player.hand.add(punishment_card)
        elif response.result is DiscardResultType.SUCESS:
            response.player.hand.discard(response.card)
        else:
            raise NoDecisionsTaken
    return round


async def play_round(game: Game) -> Game:

    round_count = 0
    discard_requests = DiscardRequests([])

    while not game.is_over:

        deck_seed = game.seed.next()
        round = create_round(
            game.lobby, deck_seed, game.rules.start_hand_size, round_count
        )

        while not round.is_over:

            # select player
            player = round.current_player

            # drawing phase
            draw_decision = await post_draw_question(player)
            if draw_decision is DrawDecisionType.FROM_DECK:
                drawn_card = round.deck.draw_top_card()
            elif draw_decision is DrawDecisionType.FROM_DISCARD:
                drawn_card = round.discard_pile.draw_top_card()
            else:
                raise NoDecisionsTaken

            # clear discard
            responses = discard_requests.resolve(round)
            round = await solve_discard_from_reponse(responses, round)

            # in hand decision
            in_hand_decision: InHandSwapAction | InHandDiscardToPile = (
                await ask_player_in_hand_decision(player, drawn_card)
            )
            if isinstance(in_hand_decision, InHandSwapAction):
                player.hand.swap(
                    in_hand_decision.owner_card, in_hand_decision.in_hand_card
                )
            elif isinstance(in_hand_decision, InHandDiscardToPile):
                round.discard_pile.add_to_top(in_hand_decision.card)
                if in_hand_decision.card.has_spell:
                    spell_type = infer_spell_type_from_rank(in_hand_decision.card.rank)
                    round = await play_spell(player, spell, round)
                    logger.info(f"Player: {player} played spell: {spell}")
            else:
                raise NoDecisionsTaken

            # end of round check
            if round.is_over:
                if game.is_over:
                    return game
                else:
                    logger.info(f"Starting new round {round_count}")
                    continue

            # clear discard
            responses = discard_requests.resolve(round)
            round = await solve_discard_from_reponse(responses, round)

    return game


#     discard_responses = await listen_quick_throws(discard_requests, round)
# round.resolve_discards(discard_responses)

# peak_action = PeakCardAction(

#     round.current_player, ActionType.PEAK, holding_card, PeakOwner.DECK

# )
