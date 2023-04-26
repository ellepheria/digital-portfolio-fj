from server.domain.declarative_base import Base
from sqlalchemy import Column, Integer, Text, ForeignKey


class ProfileFile(Base):
    __tablename__ = "profile_files"

    username = Column(
        Text,
        ForeignKey("users.username"),
        primary_key=True,
    )

    photo_path = Column(
        Text,
        nullable=True,
    )

    cover_path = Column(
        Text,
        nullable=True,
    )

    def __str__(self):
        return f'username: {self.username}, photo_path: {self.photo_path}, cover_path: {self.cover_path}'
