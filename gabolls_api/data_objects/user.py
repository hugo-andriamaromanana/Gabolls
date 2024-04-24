from typing import Dict, List, Tuple, TypedDict

from pydantic import UUID4

class User(TypedDict):
    user_id: UUID4
    name: str
    
class Player(TypedDict):
    player_id: UUID4
    user_id: UUID4

class GabollsGame(TypedDict):
    game_id: UUID4
    player_id: List[str]

class ScoreBoard(TypedDict):
    scoreboard_id: UUID4
    game_id: UUID4
    round_id: UUID4
    scores: Dict[UUID4, Tuple[int, str]]

class PlayerRound(TypedDict):
    round_id: UUID4
    game_id: UUID4
    player_id: UUID4
    score: int
    scoring_type: str


def get_user_from_db(user_id: UUID4, fake_name: str) -> User:
    return {
        "user_id": user_id,
        "name": fake_name
    }

def get_player_from_db(player_id: UUID4, fake_user_id: UUID4) -> Player:
    return {
        "player_id": player_id,
        "user_id": fake_user_id
    }

def get_game_from_db(game_id: UUID4, fake_player_ids: List[str]) -> GabollsGame:
    return {
        "game_id": game_id,
        "player_id": fake_player_ids
    }

def get_scoreboard_from_db(scoreboard_id: UUID4, game_id: UUID4, round_id: UUID4, scores: Dict[UUID4, Tuple[int, str]]) -> ScoreBoard:
    return {
        "scoreboard_id": scoreboard_id,
        "game_id": game_id,
        "round_id": round_id,
        "scores": scores
    }

