from gabolls_game.models.pydantic_config import BaseModel
from gabolls_game.models.round_resume import RoundResume


class GameResume(BaseModel):
    round_resumes: list[RoundResume]
