from app.schemas.pydantic_config import BaseModel
from app.schemas.round_resume import RoundResume


class GameResume(BaseModel):
    round_resumes: list[RoundResume]
