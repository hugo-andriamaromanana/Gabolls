from dataclasses import dataclass
from uuid import UUID


@dataclass
class Profile:
    name: str
    id: UUID

    def __hash__(self) -> int:
        return hash(self.id)
