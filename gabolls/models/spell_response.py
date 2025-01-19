from typing import Any

from gabolls.models.pydantic_config import BaseModel
from gabolls.models.spell import SpellType


class SpellResponse(BaseModel):
    ok: bool
    spell_type: SpellType | None

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"ok": self.ok, "spell_type": self.spell_type}
