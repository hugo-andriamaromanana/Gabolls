from sqlalchemy import ForeignKey, create_engine , String
from sqlalchemy.orm import (
    sessionmaker,
    Session,
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)
from icecream import ic
from typing import List, Optional
from decouple import config

_DB_USER = config("DB_USER")
_DB_PASSWORD = config("DB_PASSWORD")
_DB_HOST = config("DB_HOST")
_DB_NAME = config("DB_NAME")
_DB_TYPE = config("DB_TYPE")

_DATABASE_URL = f"{_DB_TYPE}://{_DB_USER}:{_DB_PASSWORD}@{_DB_HOST}/{_DB_NAME}"

def _generate_db_session() -> Session:
    engine = create_engine(_DATABASE_URL, echo=True)
    session = sessionmaker(bind=engine)
    return session()


db_session = _generate_db_session()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))
    user: Mapped[User] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

sandy = User(name="sandy", fullname="Sandy Cheeks")

db_session.add(sandy)
db_session.commit()

ic(db_session.query(User).all())
