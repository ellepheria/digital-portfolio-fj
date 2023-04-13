from domain.declarative_base import Base
from sqlalchemy import Column, Integer, ForeignKey


class LikedProject(Base):
    __tablename__ = "liked_projects"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("profiles.user_id"),
    )

    liked_project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False,
    )

    def __str__(self):
        return f'id: {self.id}, user_id: {self.user_id}, liked_project_id: {self.liked_project_id}'
