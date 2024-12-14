from dataclasses import dataclass
from uuid import UUID


@dataclass
class Profile:
    name: str
    id: UUID
