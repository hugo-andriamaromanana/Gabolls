from gabolls.models.pydantic_config import BaseModel
from gabolls.models.card import Card


class CardView(BaseModel):
    card: Card
    owner: int | None

    @property
    def short(self) -> str:
        owner = self.owner if self.owner is not None else "NONE"
        return f"{self.card.short}.{owner}"
