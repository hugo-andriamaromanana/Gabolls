from pydantic import BaseModel, EmailStr, Field

from ..auth.password_validation import PasswordStr

_MIN_USERNAME_LENGTH = 3
_MAX_USERNAME_LENGTH = 10
MAX_TOTAL_USERNAME_LENGTH = _MAX_USERNAME_LENGTH + 4

class CreateUser(BaseModel):
    username: str = Field(
        ..., min_length=_MIN_USERNAME_LENGTH, max_length=_MAX_USERNAME_LENGTH
    )
    email: EmailStr
    password: PasswordStr
    tag: int = Field(..., ge=0, le=1000)

    @property
    def nametag(self):
        return f"{self.username}#{self.tag}"
