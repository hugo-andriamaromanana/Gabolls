from app.schemas.pydantic_config import BaseModel
from app.schemas.deck import Deck
from app.schemas.lobby import Lobby
from app.schemas.action import RoundAction
from app.schemas.round_end import RoundEnd, RoundEndScenario


class RoundResume(BaseModel):
    deck: Deck
    lobby: Lobby
    actions: list[RoundAction]
    scenario: RoundEndScenario
    round_ends: list[RoundEnd]
