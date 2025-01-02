from loguru import logger
from gabolls.game.actions import ask_player_in_hand_decision
from gabolls.game.decisions import DrawDecisionType
from gabolls.game.scoring import infer_round_end_by_type, infer_round_end_type_by_score
from gabolls.models.action import InHandDiscardToPile, InHandSwapAction
from gabolls.models.deck import STANDARD_CARDS, Deck
from gabolls.models.discard import DiscardRequests, DiscardResponse, DiscardResultType
from gabolls.models.errors import NoDecisionsTaken
from gabolls.models.game import Game
from gabolls.models.lobby import Lobby
from gabolls.models.player import Player
from gabolls.models.round import Round
from gabolls.models.round_end import RoundEnd, RoundEndType
from gabolls.models.rules import Rules
from gabolls.models.seed import Seed
from gabolls.game.spells import (
    ask_is_spell_played,
    infer_spell_type_from_rank,
    play_spell,
)


async def ask_player_draw_type(player: Player) -> DrawDecisionType:
    raise NotImplementedError


def create_game(players: set[Player], rules: Rules, seed_source: int) -> Game:
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


def create_round(
    lobby: Lobby, deck_seed: int, hand_size: int, round_number: int
) -> Round:
    """
    A new round is
    creates cards
    add them to player hand
    """
    # creating deck shuffling it with seed
    deck = Deck(STANDARD_CARDS, deck_seed)
    deck.shuffle()
    discard_pile: Deck = Deck([], 0)

    declared_winners: list[Player] = []

    player_scores = {player: 0 for player in lobby.players}

    round = Round(
        round_number, lobby, discard_pile, deck, lobby.next_player, declared_winners, player_scores
    )

    # player draw hand size cards each
    for player in lobby.players:
        player.hand.add(deck.draw(hand_size))

    return round

async def get_declared_wins() -> list[Player]:
    raise NotImplementedError

async def prompt_user_counter_proposal(players: list[Player]) -> bool:
    raise NotImplementedError 


async def find_players_end_rounds(player: Player, round: Round, declared_wins: list[Player], counter_win_called: bool, rules: Rules) -> list[RoundEnd]:
    round_ends: list[RoundEnd] = []

    lowest_score = min(player.score for player in round.players_declared_win)

    normal_count: set[Player] = set()
    small_penalties: set[Player] = set(player for player in round.players_declared_win if not player.is_eligible)
    normal_winner: set[Player] = set(player for player in round.players_declared_win if player.is_eligible) if not counter_win_called else set()

    if counter_win_called:
        counter_winners: set[Player] = set(player for player in round.players_declared_win if player.score == lowest_score)
        big_penalties: set[Player] = set(player for player in round.players_declared_win if (player not in counter_winners) or (player not in small_penalties))
        normal_count

    normal_count: set[Player] = set()

    #"deck empty case" or "no win declared" case
    if round.deck.is_empty or len(declared_wins) < 1:
        normal_count: set[Player] = round.lobby.players
        
    
    elif counter_win_called:
        lowest_score = min(player.score for player in round.players_declared_win)
        counter_winners: set[Player] = set(player for player in round.players_declared_win if player.score == lowest_score)
        big_penalties: set[Player] = set(player for player in round.players_declared_win if (player not in counter_winners) or (player not in small_penalties))
        remaining_players: set[Player] = ((round.lobby.players - winners) - losers) - saves

    else:
        winners = set(player for player in round.players_declared_win if player.is_eligible)
        saves = round.lobby.players - winners
        remaining_players = (round.lobby.players - saves) - winners
    
    # counter
    elif counter_win_called:
        lowest_score = min(player.score for player in round.players_declared_win)

        winners = set(player for player in round.players_declared_win if player.score == lowest_score)
        for winner in winners:
            round_score = round.player_scores[winner]
            round_end = infer_round_end_by_type(winner, round_score, RoundEndType.COUNTER, rules)
            round_ends.append(round_end)
        
        saves = set(player for player in round.players_declared_win if not player.is_eligible)
        for save in saves:
            round_score = round.player_scores[save]
            round_end = infer_round_end_by_type(save,round_score, RoundEndType.SMALL_PENALTY, rules)
            round_ends.append(round_end)

        losers = set(player for player in round.players_declared_win if (player not in winners) or (player not in saves))
        for loser in losers:
            round_score = round.player_scores[loser]
            round_end = infer_round_end_by_type(loser,round_score, RoundEndType.LARGE_PENALTY, rules)
            round_ends.append(round_end)

        remaining_players = ((round.lobby.players - winners) - losers) - saves
        for player in remaining_players:
            round_score = round.player_scores[player]
            round_end_type = infer_round_end_type_by_score(player.score, round_score, rules)
            round_end = infer_round_end_by_type(player, round_score, round_end_type, rules)
            round_ends.append(round_end)
        return round_ends

    else:
        winners = set(player for player in round.players_declared_win if player.is_eligible)
        for winner in winners:
            round_score = round.player_scores[winner]
            round_end = infer_round_end_by_type(winner, round_score, RoundEndType.COUNTER, rules)
            round_ends.append(round_end)

        saves = round.lobby.players - winners
        for save in saves:
            round_score = round.player_scores[save]
            round_end = infer_round_end_by_type(save,round_score, RoundEndType.SMALL_PENALTY, rules)
            round_ends.append(round_end)
        
        remaining_players = (round.lobby.players - saves) - winners
        for player in remaining_players:
            round_score = round.player_scores[player]
            round_end_type = infer_round_end_type_by_score(player.score, round_score, rules)
            round_end = infer_round_end_by_type(player, round_score, round_end_type, rules)
            round_ends.append(round_end)
        return round_ends




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
            draw_decision = await ask_player_draw_type(player)
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
                    player_plays_spell = await ask_is_spell_played(player, spell_type)
                    if player_plays_spell:
                        round = await play_spell(player, spell_type, round)
                        logger.info(f"Player: {player} of type spell: {spell_type}")
                    else:
                        logger.info(f"Player: {player} skipped spell: {spell_type}")
            else:
                raise NoDecisionsTaken

            # clear discard
            responses = discard_requests.resolve(round)
            round = await solve_discard_from_reponse(responses, round)

        #resolve scores, counter phase
        counter_win_called = await prompt_user_counter_proposal(round.players_declared_win)
        round_ends = solve_end_rounds(round) 
        if counter_win_called:

        else:
            winners = []



        end_rounds = create_end_rounds()

    return game


# discard_responses = await listen_quick_throws(discard_requests, round)
# round.resolve_discards(discard_responses)

# peak_action = PeakCardAction(

#     round.current_player, ActionType.PEAK, holding_card, PeakOwner.DECK

# )
