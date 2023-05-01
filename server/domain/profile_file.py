from server.domain.declarative_base import Base
from sqlalchemy import Column, Integer, Text, ForeignKey


class ProfileFile(Base):
    __tablename__ = "profile_files"

    user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
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
        return f'user_id: {self.user_id}, photo_path: {self.photo_path}, cover_path: {self.cover_path}'
