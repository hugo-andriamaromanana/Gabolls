from gabolls.game.scoring import infer_score_from_round_end
from gabolls.models.round_end import RoundEnd
from gabolls.models.rules import Rules


class Score:
    points: int
    round_ends: list[RoundEnd]
    rules: Rules

    def update(self, round_end: RoundEnd) -> None:
        self.round_ends.append(round_end)
        self.points = infer_score_from_round_end(self.points, round_end, self.rules)
