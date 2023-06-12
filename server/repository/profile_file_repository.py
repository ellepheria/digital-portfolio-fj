from abc import ABC, abstractmethod

from server.domain import db_session
from server.domain.profile_file import ProfileFile


class IProfileFileRepository(ABC):
    @abstractmethod
    def get_profile_files(self, user_id: int):
        pass

    @abstractmethod
    def update(self, user_id: int, new_profile_file: ProfileFile):
        pass

    @abstractmethod
    def delete(self, user_id: int):
        pass

    @abstractmethod
    def add(self, new_profile_file: ProfileFile):
        pass


class ProfileFileRepository(IProfileFileRepository):

    def get_profile_files(self, user_id: int):
        with db_session.create_session() as session:
            return session.query(ProfileFile).filter(user_id == ProfileFile.user_id).first()

    def update(self, user_id: int, new_profile_file: ProfileFile):
        with db_session.create_session() as session:
            profile_file = session.query(ProfileFile).filter(user_id == ProfileFile.user_id).first()
            profile_file.photo_path = new_profile_file.photo_path
            profile_file.cover_path = new_profile_file.cover_path
            session.commit()

    def delete(self, user_id: int):
        with db_session.create_session() as session:
            session.delete(session.query(ProfileFile).filter(user_id == ProfileFile.user_id).first())
            session.commit()

    def add(self, new_profile_file: ProfileFile):
        with db_session.create_session() as session:
            session.add(new_profile_file)
            session.commit()
