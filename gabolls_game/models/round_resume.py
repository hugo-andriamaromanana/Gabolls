from gabolls_game.models.pydantic_config import BaseModel
from gabolls_game.models.deck import Deck
from gabolls_game.models.lobby import Lobby
from gabolls_game.models.action import RoundAction
from gabolls_game.models.round_end import RoundEnd, RoundEndScenario


class RoundResume(BaseModel):
    deck: Deck
    lobby: Lobby
    actions: list[RoundAction]
    scenario: RoundEndScenario
    round_ends: list[RoundEnd]
