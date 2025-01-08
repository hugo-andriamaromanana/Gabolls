from dataclasses import dataclass
from gabolls.models.deck import Deck
from gabolls.models.lobby import Lobby
from gabolls.models.action import RoundAction
from gabolls.models.round_end import RoundEnd, RoundEndScenario


@dataclass
class RoundResume:
    deck: Deck
    lobby: Lobby
    actions: list[RoundAction]
    scenario: RoundEndScenario
    round_ends: list[RoundEnd]
