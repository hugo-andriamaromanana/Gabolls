from gabolls.models.pydantic_config import BaseModel
from gabolls.models.round_resume import RoundResume


class GameResume(BaseModel):
    round_resumes: list[RoundResume]
