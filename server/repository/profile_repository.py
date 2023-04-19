from abc import ABC, abstractmethod

from server.domain.profile import Profile
from server.domain import db_session


class IProfileRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_profile_by_id(self, profile_id: int):
        pass

    @abstractmethod
    def get_profile_by_username(self, username: str):
        pass

    @abstractmethod
    def update(self, profile_id: int, profile: Profile):
        pass

    @abstractmethod
    def delete(self, profile_id: int):
        pass

    @abstractmethod
    def add(self, profile: Profile):
        pass


class ProfileRepository(IProfileRepository):

    def get_all(self):
        session = db_session.create_session()
        return session.query(Profile).all()

    def get_profile_by_id(self, profile_id: int):
        session = db_session.create_session()
        return session.query(Profile).filter(profile_id == Profile.user_id).first()

    def get_profile_by_username(self, username: str):
        session = db_session.create_session()
        return session.query(Profile).filter(username == Profile.username).first()

    def update(self, profile_id: int, new_profile: Profile):
        session = db_session.create_session()
        profile = session.query(Profile).filter(profile_id == Profile.user_id).first()
        profile.username = new_profile.username
        profile.name = new_profile.name
        profile.surname = new_profile.surname
        profile.about = new_profile.about
        profile.technologies = new_profile.technologies
        profile.age = new_profile.age
        profile.phone_number = new_profile.phone_number
        profile.education = new_profile.education
        profile.social_networks = new_profile.social_networks
        session.commit()

    def delete(self, profile_id: int):
        session = db_session.create_session()
        session.delete(session.query(Profile).filter(profile_id == Profile.user_id).first())
        session.commit()

    def add(self, profile: Profile):
        session = db_session.create_session()
        session.add(profile)
        session.commit()
