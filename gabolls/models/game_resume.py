from dataclasses import dataclass

from gabolls.models.round_resume import RoundResume


@dataclass
class GameResume:
    round_resumes: list[RoundResume]
