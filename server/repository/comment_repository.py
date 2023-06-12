from abc import ABC, abstractmethod

from server.domain import db_session
from server.domain.comment import Comment


class ICommentRepository(ABC):
    @abstractmethod
    def get_comments_by_project_id(self, project_id: int):
        pass

    @abstractmethod
    def add(self, new_comment: Comment):
        pass

    @abstractmethod
    def delete(self, comment_id: int):
        pass

    @abstractmethod
    def update(self, new_comment: Comment, comment_id: int):
        pass

    @abstractmethod
    def get_comment(self, comment_id: int):
        pass


class CommentRepository(ICommentRepository):
    def get_comments_by_project_id(self, project_id: int):
        with db_session.create_session() as session:
            return session.query(Comment).filter(project_id == Comment.project_id).all()

    def add(self, new_comment: Comment):
        with db_session.create_session() as session:
            session.add(new_comment)
            session.commit()

    def delete(self, comment_id: int):
        with db_session.create_session() as session:
            session.delete(session.query(Comment).filter(comment_id == Comment.id).first())
            session.commit()

    def update(self, new_comment: Comment, comment_id: int):
        with db_session.create_session() as session:
            comment = session.query(Comment).filter(comment_id == Comment.id).first()
            comment.project_id = new_comment.project_id
            comment.text = new_comment.text
            comment.user_id = new_comment.user_id
            comment.username = new_comment.username
            session.commit()

    def get_comment(self, comment_id: int):
        with db_session.create_session() as session:
            return session.query(Comment).filter(comment_id == Comment.id).first()
