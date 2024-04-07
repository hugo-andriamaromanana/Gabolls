from typing import Dict, List, TypeVar
from pydantic import BaseModel, Field

from .player import Player


class Game(BaseModel):
    players: List[Player] = Field(default_factory=dict)

    @property
    def is_over(self) -> bool:
        return any(player.is_over for player in self.players)
    
    @property
    def winners(self) -> List[Player]:
        winners = []
        lowest_score = min(player.current_score for player in self.players)
        for player in self.players:
            if player == lowest_score:
                winners.append(player)
        return winners
    
    @property
    def player_scores(self) -> List[int]:
        return [player.current_score for player in self.players]
    
    @property
    def player_names(self) -> List[str]:
        return [player.name for player in self.players]
    

# Get all players = GET -> "/players"
# Create new player = POST -> "/players"
# Get player = GET -> "/players/{id}"
# Update player = PUT -> "/players/{id}"
# Delete player = DELETE -> "/players/{id}"
# 
# Get all games = GET -> "/games"
# Create new game = POST -> "/games"
# Get game = GET -> "/games/{id}"
# Update game = PUT -> "/games/{id}"
# Delete game = DELETE -> "/games/{id}"

