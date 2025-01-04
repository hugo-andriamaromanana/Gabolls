from dataclasses import dataclass
from gabolls.models.deck import Deck
from gabolls.models.lobby import Lobby
from gabolls.models.player_action import RoundActions
from gabolls.models.round_end import RoundEnd, RoundEndScenario


@dataclass
class RoundResume:
    deck: Deck
    lobby: Lobby
    actions: list[RoundActions]
    scenario: RoundEndScenario
    round_ends: list[RoundEnd]
