from random import choice
from string import ascii_uppercase, digits


def create_random_key(key_len: int) -> str:
    chars = ascii_uppercase + digits
    key = ""
    for _ in range(key_len):
        key += choice(chars)
    return key


def create_seed(key: str) -> int:
    return hash(key)
