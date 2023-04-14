from domain import db_session
from domain.user import User

from abc import ABC, abstractmethod


class IUserRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_user(self, user_id: int):
        pass

    @abstractmethod
    def add(self, user: User):
        pass

    @abstractmethod
    def update(self, new_user: User, user_id: int):
        pass

    @abstractmethod
    def delete(self, user_id: int):
        pass


class UserRepository(IUserRepository):

    def get_all(self):
        session = db_session.create_session()
        return session.query(User).all()

    def get_user(self, user_id: int):
        session = db_session.create_session()
        return session.query(User).filter(User.id == user_id).first()

    def add(self, user: User):
        session = db_session.create_session()
        session.add(user)
        session.commit()

    def update(self, new_user: User, user_id: int):
        session = db_session.create_session()
        user = session.query(User).filter(User.id == user_id).first()
        user.username = new_user.username
        user.password = new_user.password
        user.email = new_user.email
        user.surname = new_user.surname
        session.commit()

    def delete(self, user_id: int):
        session = db_session.create_session()
        session.delete(session.query(User).filter(User.id == user_id).first())
        session.commit()
