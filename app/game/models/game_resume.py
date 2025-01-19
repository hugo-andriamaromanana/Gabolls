from app.game.models.pydantic_config import BaseModel
from app.game.models.round_resume import RoundResume


class GameResume(BaseModel):
    round_resumes: list[RoundResume]
