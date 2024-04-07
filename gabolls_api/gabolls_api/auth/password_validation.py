from typing import Callable, Dict
from pydantic import SecretStr, validator

_MIN_PASSWORD_LENGTH = 8

def _is_too_short(value: str) -> bool:
    return len(value) < _MIN_PASSWORD_LENGTH

def _has_lowercase(value: str) -> bool:
    return any(char.islower() for char in value)

def _has_uppercase(value: str) -> bool:
    return any(char.isupper() for char in value)

def _has_digit(value: str) -> bool:
    return any(char.isdigit() for char in value)

MATCH_ERROR_MAP: Dict[Callable,ValueError] = {
    _is_too_short: ValueError("Password must be at least 8 characters long"),
    _has_lowercase: ValueError("Password must have at least one lowercase letter"),
    _has_uppercase: ValueError("Password must have at least one uppercase letter"),
    _has_digit: ValueError("Password must have at least one digit"),
} 

class PasswordStr(SecretStr):
    @validator("get_secret_value")
    def validate_password(cls, value):
        for check, error in MATCH_ERROR_MAP.items():
            if check(value):
                raise error
        return value
        
    