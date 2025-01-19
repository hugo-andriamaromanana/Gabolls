from os import environ
from typing import Any

from game.models.errors import EnvVarNotFound


def unpack_env_var(key: str) -> Any:
    env_var = environ.get(key)
    if env_var is None:
        raise EnvVarNotFound(f"Couldn't locate {key} in .env")


SEED_LEN = unpack_env_var("SEED_LEN")
HAND_SIZE = unpack_env_var("HAND_SIZE")
LOSS_CAP = unpack_env_var("LOSS_CAP")
ROUND_WIN_CAP = unpack_env_var("ROUND_WIN_CAP")
SMALL_COMEBACK_BONUS = unpack_env_var("SMALL_COMEBACK_BONUS")
LARGE_COMEBACK_BONUS = unpack_env_var("LARGE_COMEBACK_BONUS")
SMALL_PENATLY_POINTS = unpack_env_var("SMALL_PENATLY_POINTS")
LARGE_PENATLY_POINTS = unpack_env_var("LARGE_PENATLY_POINTS")
SMALL_COMEBACK_TRIGGER = unpack_env_var("SMALL_COMEBACK_TRIGGER")
LARGE_COMEBACK_TRIGGER = unpack_env_var("LARGE_COMEBACK_TRIGGER")
