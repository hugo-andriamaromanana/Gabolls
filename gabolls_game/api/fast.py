from fastapi import FastAPI, HTTPException, Header
from gabolls_game.models.game_state import GameState

app = FastAPI()

game_state_storage: dict[str, GameState] = {}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/save_game_state/")
def save_game_state(game_state: GameState, x_token: str = Header(None)):
    if x_token != "expected_token":
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    try:
        game_state_storage["game_state"] = game_state
        return {"status": "Game state saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/load_game_state/")
def load_game_state(x_token: str = Header(None)):
    if x_token != "expected_token":
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    try:
        game_state = game_state_storage.get("game_state")
        if game_state is None:
            raise HTTPException(status_code=404, detail="No game state found")
        return game_state
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
