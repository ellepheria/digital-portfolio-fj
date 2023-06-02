from server.domain import db_session
from server.domain.project import Project

from abc import ABC, abstractmethod


class IProjectRepository(ABC):
    @abstractmethod
    def get_all_user_projects_by_id(self, user_id: int):
        pass

    @abstractmethod
    def get_project(self, project_id: int):
        pass

    @abstractmethod
    def add(self, project: Project):
        pass

    @abstractmethod
    def update(self, new_project: Project, project_id: int):
        pass

    @abstractmethod
    def delete(self, project_id: int):
        pass


class ProjectRepository(IProjectRepository):
    def get_all_user_projects_by_id(self, user_id: int):
        session = db_session.create_session()
        return session.query(Project).filter(user_id == Project.user_id).all()

    def get_project(self, project_id: int):
        session = db_session.create_session()
        return session.query(Project).filter(project_id == Project.id).first()

    def add(self, project: Project):
        session = db_session.create_session()
        session.add(project)
        session.commit()
        session.close()

    def update(self, new_project: Project, project_id: int):
        session = db_session.create_session()
        project = session.query(Project).filter(project_id == Project.id).first()
        project.title = new_project.title
        project.description = new_project.description
        project.github_link = new_project.github_link
        project.rating = new_project.rating
        project.cover_path = new_project.cover_path
        project.added_links = new_project.added_links
        session.commit()

    def delete(self, project_id: int):
        session = db_session.create_session()
        session.delete(session.query(Project).filter(project_id == Project.id).first())
        session.commit()
