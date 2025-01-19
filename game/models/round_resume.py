from game.models.pydantic_config import BaseModel
from game.models.deck import Deck
from game.models.lobby import Lobby
from game.models.action import RoundAction
from game.models.round_end import RoundEnd, RoundEndScenario


class RoundResume(BaseModel):
    deck: Deck
    lobby: Lobby
    actions: list[RoundAction]
    scenario: RoundEndScenario
    round_ends: list[RoundEnd]
