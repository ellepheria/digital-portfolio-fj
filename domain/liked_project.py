from declarative_base import Base
from sqlalchemy import Column, Integer, ForeignKey


class LikedProject(Base):
    __tablename__ = "liked_projects"

    user_id = Column(
        Integer,
        ForeignKey("profiles.user_id"),
        primary_key=True,
    )

    liked_project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False,
    )
