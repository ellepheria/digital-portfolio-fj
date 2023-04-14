import bcrypt
from flask_jwt_extended import create_access_token

from server.domain.declarative_base import Base
from sqlalchemy import Column, Integer, Text


class User(Base):
    __tablename__ = "users"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    username = Column(
        Text,
        unique=True,
        nullable=False
    )

    email = Column(
        Text,
        unique=True,
        nullable=False
    )

    surname = Column(
        Text,
        nullable=True,
    )

    password = Column(
        Text,
        nullable=True,
    )

    def __str__(self):
        return f'id: {self.id} username: {self.username} email: {self.email} surname: {self.surname}'

    def get_token(self):
        token = create_access_token(identity=[self.username, self.password])
        return token

    @classmethod
    def authenticate(cls, username, password):
        user = cls.query.filter(cls.username == username).one()
        if not bcrypt.verify(password, user.password):
            raise Exception('No user with this password')
        return user

