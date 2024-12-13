from dataclasses import dataclass


@dataclass
class Rules:
    start_hand_size: int
    loss_cap: int
    round_win_cap: int
    small_comeback_bonus: int
    large_comeback_bonus: int
    small_penalty_points: int
    large_penalty_points: int
    small_comeback_trigger: int
    large_comeback_trigger: int
