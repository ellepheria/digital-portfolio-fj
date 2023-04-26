from server.domain.declarative_base import Base
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
        ForeignKey("users.user_id"),
        nullable=False,
    )

    username = Column(
        Text,
        ForeignKey("users.username"),
        nullable=False,
    )

    def __str__(self):
        return f'id: {self.id}, project_id: {self.project_id}, text: {self.text}, user_id: {self.user_id}, ' \
               f'username: {self.username}'
