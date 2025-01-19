from typing import Any

from gabolls_game.models.pydantic_config import BaseModel
from gabolls_game.models.spell import SpellType


class SpellResponse(BaseModel):
    ok: bool
    spell_type: SpellType | None

    @property
    def as_dict(self) -> dict[str, Any]:
        return {"ok": self.ok, "spell_type": self.spell_type}
