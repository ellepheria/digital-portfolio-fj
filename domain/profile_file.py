from declarative_base import Base
from sqlalchemy import Column, Integer, Text, ForeignKey


class ProfileFile(Base):
    __tablename__ = "profile_files"

    profile_id = Column(
        Integer,
        ForeignKey("profiles.user_id"),
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
