from dataclasses import dataclass
from gabolls.models.spell import SpellType


@dataclass
class SpellResponse:
    ok: bool
    spell_type: SpellType | None
