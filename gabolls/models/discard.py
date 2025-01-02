from dataclasses import dataclass
from enum import StrEnum, auto
from gabolls.models.card import Card
from gabolls.models.player import Player
from gabolls.models.round import Round


class DiscardResultType(StrEnum):
    SUCESS = auto()
    FAIL = auto()


@dataclass
class DiscardRequest:
    player: Player
    card: Card


@dataclass
class DiscardResponse:
    card: Card
    player: Player
    result: DiscardResultType


@dataclass
class DiscardRequests:
    queue: list[DiscardRequest]

    def resolve(self, round: Round) -> list[DiscardResponse]:
        responses: list[DiscardResponse] = []
        for request in self.queue:
            result_type = (
                DiscardResultType.FAIL
                if request.card.rank != round.deck.top_card_view.card.rank
                else DiscardResultType.SUCESS
            )
            response = DiscardResponse(request.card, request.player, result_type)
            responses.append(response)
        return responses

    def add(self, request: DiscardRequest) -> None:
        self.queue.append(request)

    def clear(self) -> None:
        self.queue.clear()
