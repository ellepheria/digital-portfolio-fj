from server.domain import db_session
from server.domain.user import User

from abc import ABC, abstractmethod


class IUserRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_user(self, user_id: int):
        pass

    @abstractmethod
    def get_user_by_username(self, username: str):
        pass

    @abstractmethod
    def get_user_by_email(self, email: str):
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
        return session.query(User).filter(User.user_id == user_id).first()

    def get_user_by_username(self, username: str):
        session = db_session.create_session()
        return session.query(User).filter(username == User.username).first()

    def get_user_by_email(self, email: str):
        session = db_session.create_session()
        return session.query(User).filter(email == User.email).first()

    def add(self, user: User):
        session = db_session.create_session()
        session.add(user)
        session.commit()

    def update(self, new_user: User, user_id: int):
        session = db_session.create_session()
        user = session.query(User).filter(User.user_id == user_id).first()
        user.username = new_user.username
        user.password = new_user.password
        user.email = new_user.email
        user.surname = new_user.surname
        user.name = new_user.name
        user.type_of_activity = new_user.type_of_activity
        user.social_networks = new_user.social_networks
        user.education = new_user.education
        user.phone_number = new_user.phone_number
        user.age = new_user.age
        user.about = new_user.about
        user.technologies = new_user.technologies

        session.commit()

    def delete(self, user_id: int):
        session = db_session.create_session()
        session.delete(session.query(User).filter(User.user_id == user_id).first())
        session.commit()
