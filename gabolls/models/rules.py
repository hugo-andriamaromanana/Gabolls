from dataclasses import dataclass


@dataclass
class Rules:
    starting_view: int
    start_hand_size: int
    loss_cap: int
    round_win_cap: int
    small_comeback_bonus: int
    large_comeback_bonus: int
    small_penalty_points: int
    large_penalty_points: int
    small_comeback_trigger: int
    large_comeback_trigger: int

    @property
    def as_dict(self) -> dict[str, int]:
        return {
            "start_hand_size": self.start_hand_size,
            "loss_cap": self.loss_cap,
            "round_win_cap": self.round_win_cap,
            "small_comeback_bonus": self.small_comeback_bonus,
            "large_comeback_bonus": self.large_comeback_bonus,
            "small_penalty_points": self.small_penalty_points,
            "large_penalty_points": self.large_penalty_points,
            "small_comeback_trigger": self.small_comeback_trigger,
            "large_comeback_trigger": self.large_comeback_trigger,
        }


DEFAULT_RULES_DICT = {
    "starting_view": 2,
    "start_hand_size": 4,
    "loss_cap": 120,
    "round_win_cap": 7,
    "small_comeback_bonus": 25,
    "large_comeback_bonus": 50,
    "small_penalty_points": 25,
    "large_penalty_points": 50,
    "small_comeback_trigger": 50,
    "large_comeback_trigger": 100,
}

DEFAULT_RULES = Rules(**DEFAULT_RULES_DICT)