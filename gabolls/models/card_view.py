from dataclasses import dataclass
from gabolls.models.card import Card


@dataclass
class CardView:
    card: Card
    owner: int | None

    @property
    def short(self) -> str:
        owner = self.owner if self.owner is not None else "NONE"
        return f"{self.card.short}.{owner}"
