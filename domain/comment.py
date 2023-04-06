from declarative_base import Base
from sqlalchemy import Column, Integer, Text, ForeignKey


class Comment(Base):
    __tablename__ = "comments"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False,
    )

    text = Column(
        Text,
        nullable=False,
    )

    user_id = Column(
        Integer,
        ForeignKey("profiles.user_id"),
        nullable=False,
    )

    username = Column(
        Text,
        ForeignKey("profiles.username"),
        nullable=False,
    )
