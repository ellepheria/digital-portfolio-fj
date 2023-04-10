from domain.declarative_base import Base
from sqlalchemy import Column, Integer, Text, ForeignKey


class ProjectFile(Base):
    __tablename__ = "project_files"

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

    file_path = Column(
        Text,
        unique=True,
    )
