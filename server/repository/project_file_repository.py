from abc import ABC, abstractmethod

from server.domain import db_session
from server.domain.project_file import ProjectFile


class IProjectFileRepository(ABC):
    @abstractmethod
    def get_all_project_files(self, project_id: int):
        pass

    @abstractmethod
    def get_project_file(self, project_file_id: int):
        pass

    @abstractmethod
    def add(self, project_file: ProjectFile):
        pass

    @abstractmethod
    def update(self, project_file_id: int, new_project_file: ProjectFile):
        pass

    @abstractmethod
    def delete(self, project_file_id: int):
        pass


class ProjectFileRepository(IProjectFileRepository):
    def get_all_project_files(self, project_id: int):
        session = db_session.create_session()
        return session.query(ProjectFile).filter(project_id == ProjectFile.project_id).all()

    def get_project_file(self, project_file_id: int):
        session = db_session.create_session()
        return session.query(ProjectFile).filter(project_file_id == ProjectFile.id).first()

    def add(self, project_file: ProjectFile):
        session = db_session.create_session()
        session.add(project_file)
        session.expunge_all()
        session.commit()

    def update(self, project_file_id: int, new_project_file: ProjectFile):
        session = db_session.create_session()
        project_file = session.query(ProjectFile).filter(project_file_id == ProjectFile.id).first()
        project_file.file_path = new_project_file.file_path
        project_file.project_id = new_project_file.project_id
        session.expunge_all()
        session.commit()

    def delete(self, project_file_id: int):
        session = db_session.create_session()
        session.delete(session.query(ProjectFile).filter(project_file_id == ProjectFile.id).first())
        session.expunge_all()
        session.commit()
