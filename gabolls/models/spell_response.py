from dataclasses import dataclass
from typing import Any
from gabolls.models.spell import SpellType


@dataclass(slots=True)
class SpellResponse:
    ok: bool
    spell_type: SpellType | None

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"ok": self.ok, "spell_type": self.spell_type}