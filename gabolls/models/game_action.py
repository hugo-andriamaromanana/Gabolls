from dataclasses import dataclass
from typing import TypeAlias


class RoundOverAction:
    pass


GameActions: TypeAlias = RoundOverAction


SHORT_GAME_ACTIONS: dict[type[GameActions], str] = {RoundOverAction: "ROA"}


@dataclass
class GameAction:
    action: GameActions

    @property
    def short(self) -> str:
        return SHORT_GAME_ACTIONS[type(self.action)]
