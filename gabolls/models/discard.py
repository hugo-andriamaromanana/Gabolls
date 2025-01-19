from enum import StrEnum, auto
from typing import Any

from gabolls.models.pydantic_config import BaseModel
from gabolls.models.card import Card
from gabolls.models.player import Player


class DiscardResultType(StrEnum):
    SUCESS = auto()
    FAIL = auto()


class DiscardRequest(BaseModel):
    player: Player
    card: Card

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"player_id": self.player.id, "card": self.card.short}


class DiscardResponse(BaseModel):
    card: Card
    player: Player
    result: DiscardResultType


class DiscardRequests(BaseModel):
    queue: list[DiscardRequest]

    def add(self, request: DiscardRequest) -> None:
        self.queue.append(request)

    def clear(self) -> None:
        self.queue.clear()

    @property
    def as_list(self) -> list[dict[str, Any]]:
        return [request.as_dict for request in self.queue]
