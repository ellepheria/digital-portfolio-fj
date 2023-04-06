from declarative_base import Base
from sqlalchemy import Column, Integer, Text, ForeignKey


class Profile(Base):
    __tablename__ = "profiles"

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        primary_key=True,
    )

    username = Column(
        Text,
        unique=True,
        nullable=False
    )

    name = Column(
        Text,
        nullable=False,
    )

    surname = Column(
        Text,
        nullable=True,
    )

    about = Column(
        Text,
        nullable=True,
    )

    technologies = Column(
        Text,
        nullable=True,
    )

    age = Column(
        Integer,
        nullable=True,
    )

    phone_number = Column(
        Text,
        unique=True,
        nullable=True,
    )

    education = Column(
        Text,
        nullable=True,
    )

    social_networks = Column(
        Text,
        nullable=True,
    )
