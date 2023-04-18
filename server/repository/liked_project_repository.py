from server.domain import db_session
from server.domain.liked_project import LikedProject
from abc import ABC, abstractmethod


class ILikedObjectRepository(ABC):
    @abstractmethod
    def get_all_users_like(self, user_id: int):
        pass

    @abstractmethod
    def delete(self, liked_project_id: int):
        pass

    @abstractmethod
    def add(self, liked_project: LikedProject):
        pass


class LikedProjectRepository(ILikedObjectRepository):

    def get_all_users_like(self, user_id: int):
        session = db_session.create_session()
        return session.query(LikedProject).filter(user_id == LikedProject.user_id).all()

    def delete(self, liked_project_id: int):
        session = db_session.create_session()
        session.delete(session.query(LikedProject).filter(liked_project_id == LikedProject.liked_project_id).first())
        session.commit()

    def add(self, liked_project: LikedProject):
        session = db_session.create_session()
        session.add(liked_project)
        session.commit()
