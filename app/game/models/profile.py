from uuid import UUID
from app.game.models.pydantic_config import BaseModel


class Profile(BaseModel):
    name: str
    uuid: UUID

    @property
    def id(self) -> int:
        return hash(self.uuid)

    @property
    def as_dict(self) -> dict[str, str | UUID | int]:
        return {"name": self.name, "uuid": self.uuid, "id": self.id}
