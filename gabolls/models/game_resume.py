from dataclasses import dataclass

from gabolls.models.round_resume import RoundResume


@dataclass(slots=True)
class GameResume:
    round_resumes: list[RoundResume]
