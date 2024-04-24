from typing import Dict
from fastapi import FastAPI
from h11 import Response

from data_objects.game import Game
from give_scores import give_gabo
from data_objects.player import Player

app = FastAPI()
game = Game()

def _retrieve_player_by_name(player_name: str) -> Player:
    return next(player for player in game.players if player.name == player_name)


@app.post("/")
def index() -> Game:
    return game


@app.post("/{player_name}")
def create_player(name: str, id: int) -> Dict[str,str]:
    """Adds a player to the game."""
    game.players.append(Player(name=name, id = id))
    return {"deleted_player_name": name}

@app.delete("/delete/{player_name}")
def delete_player(player_name: str) -> Dict[str,str]:
    player = _retrieve_player_by_name(player_name)
    game.players.remove(player)
    return {"deleted_player_name": player_name}

@app.put("/gabo/{player_name}")
def gabo(player_name: str) -> Dict[str,str]:
    player = _retrieve_player_by_name(player_name)
    give_gabo(player)
    return {"player_name": player_name}

# Scoreboard
