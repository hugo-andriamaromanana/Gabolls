from dataclasses import dataclass
from typing import Any, TypeAlias


class RoundOverAction:
    def __init__(self) -> None:
        self.as_dict = {"action_name": "RoundOverAction"}


GameActions: TypeAlias = RoundOverAction


@dataclass(slots=True)
class GameAction:
    action: GameActions

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"game_action": self.action.as_dict}
