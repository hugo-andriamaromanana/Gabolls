from gabolls_game.models.pydantic_config import BaseModel


class Seed(BaseModel):
    source: int
    offset: int

    def next(self) -> int:
        new = self.source + self.offset
        self.offset += 1
        return new

    @property
    def as_dict(self) -> dict[str, int]:
        return {"source": self.source, "counter": self.offset}
