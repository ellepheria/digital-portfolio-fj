from declarative_base import Base
from sqlalchemy import Column, Integer, Text, ARRAY, ForeignKey


class Project(Base):
    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    title = Column(
        Text,
        nullable=False,
    )

    user_id = Column(
        Integer,
        ForeignKey("profiles.user_id"),
        nullable=False,
    )

    description = Column(
        Text,
        nullable=True,
    )

    github_link = Column(
        Text,
        nullable=True,
    )

    rating = Column(
        Integer,
        nullable=False,
    )

    cover_path = Column(
        Text,
        nullable=True
    )

    added_links = Column(
        ARRAY(Integer, dimensions=5),
        nullable=True,
    )
