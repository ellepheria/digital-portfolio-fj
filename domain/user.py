from declarative_base import Base
from sqlalchemy import Column, Integer, Text


class User(Base):
    __tablename__ = "users"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    username = Column(
        Text,
        unique=True,
        nullable=False
    )

    email = Column(
        Text,
        unique=True,
        nullable=False
    )

    surname = Column(
        Text,
        nullable=True,
    )

    password = Column(
        Text,
        nullable=True,
    )
