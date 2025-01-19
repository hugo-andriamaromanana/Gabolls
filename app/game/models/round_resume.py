from app.game.models.pydantic_config import BaseModel
from app.game.models.deck import Deck
from app.game.models.lobby import Lobby
from app.game.models.action import RoundAction
from app.game.models.round_end import RoundEnd, RoundEndScenario


class RoundResume(BaseModel):
    deck: Deck
    lobby: Lobby
    actions: list[RoundAction]
    scenario: RoundEndScenario
    round_ends: list[RoundEnd]
