from gabolls.models.deck import Deck, create_standard_cards
from gabolls.models.lobby import Lobby
from gabolls.models.round import Round


def create_round(
    lobby: Lobby, deck_seed: int, hand_size: int, round_number: int
) -> Round:
    """
    A new round is
    creates cards
    add them to player hand
    """
    # creating
    deck = Deck(create_standard_cards(), deck_seed)
    deck.shuffle()
    discard_pile: Deck = Deck([], 0)
    round = Round(round_number, lobby, discard_pile, deck, lobby.next_player, [])
    for player in lobby.players:
        player.hand.add(deck.draw(hand_size))
    return round
