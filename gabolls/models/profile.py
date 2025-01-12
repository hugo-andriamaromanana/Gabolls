from dataclasses import dataclass
from functools import cached_property
from uuid import UUID


@dataclass
class Profile:
    name: str
    uuid: UUID

    @cached_property
    def id(self) -> int:
        return hash(self.uuid)

    @property
    def as_dict(self) -> dict[str, str | UUID | int]:
        return {"name": self.name, "uuid": self.uuid, "id": self.id}
