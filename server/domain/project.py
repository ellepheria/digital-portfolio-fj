from server.domain.declarative_base import Base
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

    short_description = Column(
        Text,
        nullable=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
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
        default=lambda: 0,
    )

    cover_path = Column(
        Text,
        nullable=True
    )

    added_links = Column(
        ARRAY(Integer, dimensions=5),
        nullable=True,
    )

    def __str__(self):
        return f'id: {self.id}, title: {self.title}, user_id: {self.user_id}, description: {self.description}, ' \
               f'github: {self.github_link}, rating: {self.rating}, cover_path: {self.cover_path}, ' \
               f'added_links: {self.added_links}'
