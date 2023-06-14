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
    def get_users_with_type_of_activities(self, type_of_activities: [str]):
        pass

    @abstractmethod
    def get_users_with_technologies(self, technologies: [str]):
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
        with db_session.create_session() as session:
            return session.query(User).all()

    def get_user(self, user_id: int):
        with db_session.create_session() as session:
            return session.query(User).filter(User.user_id == user_id).first()

    def get_user_by_username(self, username: str):
        with db_session.create_session() as session:
            return session.query(User).filter(username == User.username).first()

    def get_user_by_email(self, email: str):
        with db_session.create_session() as session:
            return session.query(User).filter(email == User.email).first()

    def get_users_with_type_of_activities(self, type_of_activity: str):
        users = self.get_all()
        result = set()
        for user in users:
            if str(user.type_of_activity).find(type_of_activity) != -1:
                result.add(user)
        return result

    def get_users_with_technologies(self, technology: str):
        users = self.get_all()
        result = set()
        for user in users:
            if str(user.technologies).find(technology) != -1:
                result.add(user)
        return result

    def get_users_with_names(self, name: str):
        users = self.get_all()
        result = set()
        for user in users:
            if str(user.name).find(name) != -1:
                result.add(user)

        return result

    def get_users_with_description(self, description: str):
        users = self.get_all()
        result = set()
        for user in users:
            if str(user.about).find(description) != -1:
                result.add(user)

        return result

    def add(self, user: User):
        with db_session.create_session() as session:
            session.add(user)
            session.commit()

    def update(self, new_user: User, user_id: int):
        with db_session.create_session() as session:
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
        with db_session.create_session() as session:
            session.delete(session.query(User).filter(User.user_id == user_id).first())
            session.commit()
