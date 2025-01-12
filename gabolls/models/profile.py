from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Profile:
    name: str
    uuid: UUID

    @property
    def id(self) -> int:
        return hash(self.uuid)

    @property
    def as_dict(self) -> dict[str, str | UUID | int]:
        return {"name": self.name, "uuid": self.uuid, "id": self.id}
