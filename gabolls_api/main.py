from typing import Dict
from fastapi import FastAPI
from regex import D

from data_objects.game import Game
from give_scores import PenaltyType, give_gabo, give_penalty
from data_objects.player import Player

app = FastAPI()
game = Game()

def _retrieve_player_by_name(player_name: str) -> Player:
    return next(player for player in game.players if player.name == player_name)

@app.get("/")
def index() -> Game:
    return game

@app.put("/add/{player_name}")
def add_player(player_name: str) -> Dict[str,str]:
    game.players.append(Player(name=player_name))
    return {"player_name": player_name}

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