from gabolls.game.decisions import DrawDecisionType
from gabolls.models.player import Player


async def post_draw_question(player: Player) -> DrawDecisionType:
    raise NotImplementedError
